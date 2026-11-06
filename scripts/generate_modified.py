#!/usr/bin/env python3
"""Write build/modified/{slug}.html for posts edited after publication.

zvc renders templates before any of our scripts run and cannot see git, so the
per-post edit date is handed to post.html as a tiny include file (same trick as
build/asset-version.html). Only posts whose newest non-bulk commit is later than
pub_date get a file; the template falls back to pub_date for the rest.

Runs BEFORE `zvc build` (see Makefile). build/ is gitignored.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

from site_posts import last_modified, load_posts, modified_dates

OUTPUT_DIR = Path("build/modified")


def write_modified(posts, modified: dict[str, str], output_dir: Path = OUTPUT_DIR) -> int:
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)
    written = 0
    for post in posts:
        date = last_modified(post, modified)
        if date == post.pub_date:
            continue
        (output_dir / f"{post.slug}.html").write_text(date, encoding="utf-8")
        written += 1
    return written


def main() -> int:
    written = write_modified(load_posts(), modified_dates())
    print(f"modified dates: {written} posts edited after publication -> {OUTPUT_DIR}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
