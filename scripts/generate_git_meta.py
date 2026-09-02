#!/usr/bin/env python3
"""Generate docs/meta/git.json from the git history of contents/.

The Ledger theme reads this file at runtime to show a changelog on the home page
and a per-post history. Only commits touching contents/ are included.

Output schema:
{
  "generated_at": "2026-09-02T12:00:00+00:00",
  "total_commits": 98,
  "changelog": [{"hash": "bbb4a2e5", "date": "2026-08-08", "message": "..."}],
  "posts": {"2026-self-proof": [{"hash": "...", "date": "...", "message": "..."}]}
}
"""

from __future__ import annotations

import json
import subprocess
import sys
from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

RECORD_SEPARATOR = "\x1e"
FIELD_SEPARATOR = "\x1f"
CHANGELOG_SIZE = 3
CONTENTS_DIR = "contents"
OUTPUT_PATH = Path("docs/meta/git.json")

GitRunner = Callable[[list[str]], str | None]


@dataclass(frozen=True)
class Commit:
    hash: str
    date: str
    message: str
    files: tuple[str, ...]


def run_git(args: list[str]) -> str | None:
    """Run a git command and return stdout, or None when git is unavailable."""
    try:
        result = subprocess.run(
            ["git", *args], capture_output=True, text=True, check=True, encoding="utf-8"
        )
    except (OSError, subprocess.CalledProcessError) as error:
        print(f"warning: git command failed, writing empty meta: {error}", file=sys.stderr)
        return None
    return result.stdout


def parse_log(raw: str) -> list[Commit]:
    """Parse `git log --format=<RS>%h<FS>%ad<FS>%s --name-only` output."""
    commits: list[Commit] = []
    for record in raw.split(RECORD_SEPARATOR):
        lines = [line for line in record.split("\n") if line.strip()]
        if not lines:
            continue
        fields = lines[0].split(FIELD_SEPARATOR)
        if len(fields) < 3:
            continue
        commit_hash, date = fields[0].strip(), fields[1].strip()
        message = FIELD_SEPARATOR.join(fields[2:]).strip()
        files = tuple(line.strip() for line in lines[1:])
        commits.append(Commit(commit_hash, date, message, files))
    return commits


def slug_from_path(path: str) -> str | None:
    """contents/{slug}/... -> slug. Paths outside contents/ return None."""
    parts = path.split("/")
    if len(parts) < 3 or parts[0] != CONTENTS_DIR:
        return None
    return parts[1]


def serialize(commit: Commit) -> dict[str, str]:
    return {"hash": commit.hash, "date": commit.date, "message": commit.message}


def group_by_slug(commits: list[Commit]) -> dict[str, list[dict[str, str]]]:
    """Map each post slug to its commits, preserving newest-first order."""
    posts: dict[str, list[dict[str, str]]] = {}
    for commit in commits:
        slugs = {slug for slug in map(slug_from_path, commit.files) if slug}
        for slug in sorted(slugs):
            posts.setdefault(slug, []).append(serialize(commit))
    return posts


def build_meta(commits: list[Commit], total_commits: int, now: datetime | None = None) -> dict:
    now = now or datetime.now(timezone.utc)
    return {
        "generated_at": now.isoformat(timespec="seconds"),
        "total_commits": total_commits,
        "changelog": [serialize(commit) for commit in commits[:CHANGELOG_SIZE]],
        "posts": group_by_slug(commits),
    }


def collect(run: GitRunner = run_git) -> dict:
    """Collect git data. Never raises: a missing git yields an empty meta."""
    log_format = f"--format={RECORD_SEPARATOR}%h{FIELD_SEPARATOR}%ad{FIELD_SEPARATOR}%s"
    raw_log = run(["log", "--date=short", log_format, "--name-only", "--", CONTENTS_DIR])
    raw_count = run(["rev-list", "--count", "HEAD"])
    commits = parse_log(raw_log) if raw_log else []
    total = int(raw_count.strip()) if raw_count and raw_count.strip().isdigit() else 0
    return build_meta(commits, total)


def write_meta(meta: dict, output_path: Path = OUTPUT_PATH) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    meta = collect()
    write_meta(meta)
    print(
        f"git meta: {len(meta['posts'])} posts, {len(meta['changelog'])} changelog entries, "
        f"{meta['total_commits']} commits -> {OUTPUT_PATH}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
