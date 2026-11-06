#!/usr/bin/env python3
"""Shared post metadata for the build scripts.

`load_posts()` reads every published post's frontmatter from contents/ (newest first).
`modified_dates()` derives a per-post "last content change" date from git, ignoring
bulk commits (migrations, tag normalization) that touch many posts at once: a commit
that rewrites 900 frontmatters is not an update of 900 articles, and reporting it as
one makes every lastmod identical, which crawlers then ignore.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

from generate_git_meta import CONTENTS_DIR as GIT_CONTENTS_DIR
from generate_git_meta import FIELD_SEPARATOR as FS
from generate_git_meta import RECORD_SEPARATOR as RS
from generate_git_meta import Commit, GitRunner, parse_log, run_git

SITE_URL = "https://ash84.io"
CONTENTS_DIR = Path("contents")
DOCS_DIR = Path("docs")
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

# A commit touching more than this many posts is treated as housekeeping, not an edit.
BULK_COMMIT_SLUGS = 20


@dataclass(frozen=True)
class Post:
    slug: str
    title: str
    link: str  # /YYYY/MM/DD/slug/
    pub_date: str
    description: str = ""
    tags: tuple[str, ...] = field(default_factory=tuple)

    @property
    def url(self) -> str:
        return f"{SITE_URL}{self.link}"

    @property
    def html_path(self) -> Path:
        return DOCS_DIR / self.link.strip("/") / "index.html"


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
        value = value[1:-1]
    return value.strip()


def read_field(frontmatter: str, key: str) -> str:
    match = re.search(rf"^{key}:[ \t]*(.*)$", frontmatter, re.MULTILINE)
    return unquote(match.group(1)) if match else ""


def read_tags(frontmatter: str) -> tuple[str, ...]:
    """Inline list only (`tags: ['a', 'b']`), matching what zvc 0.1.8 understands."""
    raw = read_field(frontmatter, "tags")
    if not (raw.startswith("[") and raw.endswith("]")):
        return ()
    items = (unquote(item) for item in raw[1:-1].split(","))
    return tuple(item for item in items if item)


def read_post(path: Path) -> Post | None:
    """Parse one markdown file. Drafts, bad dates and files without frontmatter yield None."""
    match = FRONTMATTER_RE.match(path.read_text(encoding="utf-8"))
    if not match:
        return None
    frontmatter = match.group(1)
    if read_field(frontmatter, "status") == "draft":
        return None
    pub_date = read_field(frontmatter, "pub_date")
    if not DATE_RE.fullmatch(pub_date):
        return None
    slug = path.parent.name
    year, month, day = pub_date.split("-")
    return Post(
        slug=slug,
        title=read_field(frontmatter, "title") or path.stem,
        link=f"/{year}/{month}/{day}/{slug}/",
        pub_date=pub_date,
        description=read_field(frontmatter, "description"),
        tags=read_tags(frontmatter),
    )


def load_posts(contents_dir: Path = CONTENTS_DIR) -> list[Post]:
    """Every published post, newest first (ties broken by slug for a stable order)."""
    posts = [post for post in map(read_post, sorted(contents_dir.glob("*/*.md"))) if post]
    posts.sort(key=lambda post: (post.pub_date, post.slug), reverse=True)
    return posts


def _slugs(commit: Commit) -> set[str]:
    slugs: set[str] = set()
    for file in commit.files:
        parts = file.split("/")
        if len(parts) >= 3 and parts[0] == GIT_CONTENTS_DIR:
            slugs.add(parts[1])
    return slugs


def modified_from_commits(commits: list[Commit], bulk_limit: int = BULK_COMMIT_SLUGS) -> dict:
    """slug -> date of the newest non-bulk commit touching that post."""
    modified: dict[str, str] = {}
    for commit in commits:  # newest first
        slugs = _slugs(commit)
        if not slugs or len(slugs) > bulk_limit:
            continue
        for slug in slugs:
            modified.setdefault(slug, commit.date)
    return modified


def modified_dates(run: GitRunner = run_git) -> dict[str, str]:
    """Read git once and return slug -> last edit date. Empty when git is unavailable."""
    raw = run(
        [
            "log",
            "--date=short",
            f"--format={RS}%h{FS}%ad{FS}%s",
            "--name-only",
            "--",
            GIT_CONTENTS_DIR,
        ]
    )
    return modified_from_commits(parse_log(raw)) if raw else {}


def last_modified(post: Post, modified: dict[str, str]) -> str:
    """The date to advertise as lastmod: the git edit date when it is after publication."""
    edited = modified.get(post.slug, "")
    return edited if edited > post.pub_date else post.pub_date


if __name__ == "__main__":
    for post in load_posts()[:5]:
        print(post.pub_date, post.link, post.tags)
    sys.exit(0)
