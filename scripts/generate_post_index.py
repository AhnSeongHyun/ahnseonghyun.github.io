#!/usr/bin/env python3
"""Generate docs/meta/posts.json: every published post, newest first.

Format (compact, one row per post): [[slug, title, link, pub_date], ...]
The Ledger theme fetches it once per browser session to render prev/next links.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
CONTENTS_DIR = Path("contents")
OUTPUT_PATH = Path("docs/meta/posts.json")


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
        value = value[1:-1]
    return value.strip()


def read_field(frontmatter: str, key: str) -> str:
    match = re.search(rf"^{key}:[ \t]*(.*)$", frontmatter, re.MULTILINE)
    return unquote(match.group(1)) if match else ""


def read_post(path: Path) -> list[str] | None:
    """Return [slug, title, link, pub_date] or None for drafts / files without frontmatter."""
    match = FRONTMATTER_RE.match(path.read_text(encoding="utf-8"))
    if not match:
        return None
    frontmatter = match.group(1)
    if read_field(frontmatter, "status") == "draft":
        return None
    pub_date = read_field(frontmatter, "pub_date")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", pub_date):
        return None
    slug = path.parent.name
    year, month, day = pub_date.split("-")
    title = read_field(frontmatter, "title") or path.stem
    return [slug, title, f"/{year}/{month}/{day}/{slug}/", pub_date]


def build_index(paths: list[Path]) -> list[list[str]]:
    rows = [row for row in map(read_post, paths) if row]
    rows.sort(key=lambda row: (row[3], row[0]), reverse=True)
    return rows


def write_index(rows: list[list[str]], output_path: Path = OUTPUT_PATH) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(rows, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8"
    )


def main() -> int:
    rows = build_index(sorted(CONTENTS_DIR.glob("*/*.md")))
    write_index(rows)
    print(f"post index: {len(rows)} posts -> {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
