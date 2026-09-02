#!/usr/bin/env python3
"""Normalize frontmatter tags across contents/ so zvc and the tag pages see one clean list.

Rules (only the tags section of the frontmatter is rewritten):
- YAML block list (`- tag`) -> inline list `['a', 'b']` (zvc 0.1.8 parses inline lists only)
- hashtag strings (`'#a #b'`) -> separate tags
- empty tags dropped, HTML entities decoded (`&amp;` -> `&`)
- consolidate_tags.CONSOLIDATION_RULES applied (case / variant merge), duplicates removed

Usage:
    uv run python scripts/normalize_tags.py           # dry run, prints planned changes
    uv run python scripts/normalize_tags.py --apply   # rewrite files (no backup files; use git)
"""

from __future__ import annotations

import html
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import consolidate_tags

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
TAGS_LINE_RE = re.compile(r"^tags:[ \t]*(.*)$", re.MULTILINE)
CONTENTS_DIR = Path("contents")


@dataclass(frozen=True)
class TagsSection:
    tags: list[str]
    start: int
    end: int


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
        value = value[1:-1]
    return value.strip()


def split_inline(value: str) -> list[str]:
    inner = value.strip()[1:-1]
    return [unquote(part) for part in inner.split(",") if part.strip()]


def find_tags_section(frontmatter: str) -> TagsSection | None:
    """Locate the tags section (inline, block list or scalar) inside the frontmatter text."""
    match = TAGS_LINE_RE.search(frontmatter)
    if not match:
        return None
    value = match.group(1).strip()
    start, end = match.start(), match.end()
    if value.startswith("["):
        return TagsSection(split_inline(value), start, end)
    if value:
        return TagsSection([unquote(value)], start, end)

    tags: list[str] = []
    for line_match in re.finditer(r"\n([^\n]*)", frontmatter[end:]):
        line = line_match.group(1)
        if line.startswith("- "):
            tags.append(unquote(line[2:]))
            end = match.end() + line_match.end()
        else:
            break
    return TagsSection(tags, start, end)


def strip_markup(tag: str) -> str:
    """'<b>태그' -> 'b태그', '<hr/>' -> 'hr'. Tag names must not carry HTML angle brackets."""
    if "<" not in tag and ">" not in tag:
        return tag
    return tag.replace("<", "").replace(">", "").rstrip("/").strip()


def expand_hashtags(tag: str) -> list[str]:
    if not tag.startswith("#"):
        return [tag]
    return [part.strip() for part in tag.replace("#", " ").split()]


def normalize_tags(tags: list[str]) -> list[str]:
    expanded: list[str] = []
    for tag in tags:
        expanded.extend(expand_hashtags(strip_markup(html.unescape(tag).strip())))
    non_empty = [tag for tag in expanded if tag]
    return consolidate_tags.consolidate_tags(non_empty)


def quote(tag: str) -> str:
    return f'"{tag}"' if "'" in tag else f"'{tag}'"


def format_inline(tags: list[str]) -> str:
    """Empty input renders `tags: []` so a stray `['']` no longer yields an empty tag."""
    return "tags: [" + ", ".join(quote(tag) for tag in tags) + "]"


def rewrite(content: str) -> str | None:
    """Return the rewritten document, or None when nothing changes."""
    match = FRONTMATTER_RE.match(content)
    if not match:
        return None
    frontmatter = match.group(1)
    section = find_tags_section(frontmatter)
    if section is None:
        return None
    normalized = normalize_tags(section.tags)
    current_text = frontmatter[section.start : section.end]
    new_text = format_inline(normalized)
    if current_text == new_text:
        return None
    new_frontmatter = frontmatter[: section.start] + new_text + frontmatter[section.end :]
    offset = match.start(1)
    return content[:offset] + new_frontmatter + content[offset + len(frontmatter) :]


def iter_markdown_files(root: Path = CONTENTS_DIR):
    return sorted(root.glob("*/*.md"))


def main(argv: list[str]) -> int:
    apply = "--apply" in argv
    changed = 0
    for path in iter_markdown_files():
        content = path.read_text(encoding="utf-8")
        updated = rewrite(content)
        if updated is None:
            continue
        changed += 1
        before = find_tags_section(FRONTMATTER_RE.match(content).group(1))
        after = find_tags_section(FRONTMATTER_RE.match(updated).group(1))
        print(f"{path.parent.name}: {before.tags} -> {after.tags}")
        if apply:
            path.write_text(updated, encoding="utf-8")
    mode = "applied" if apply else "dry run"
    print(f"{mode}: {changed} files")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
