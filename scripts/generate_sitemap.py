#!/usr/bin/env python3
"""Generate docs/sitemap.xml from post frontmatter and git history.

- Posts carry the git edit date as <lastmod> (pub_date when never edited). The old
  version stamped every URL with the build time, which makes lastmod meaningless
  and crawlers stop trusting it.
- Tag pages are listed only when they hold MIN_TAG_POSTS or more posts; the rest
  are rendered with noindex by tag.html. 2,000+ single-post tag pages are thin
  duplicates of the post itself.
- No <changefreq>/<priority>: Google ignores both.
"""

from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

from generate_tags import sanitize_filename
from site_posts import SITE_URL, Post, last_modified, load_posts, modified_dates

OUTPUT_PATH = Path("docs/sitemap.xml")
MIN_TAG_POSTS = 2


def tag_entries(posts: list[Post], modified: dict[str, str]) -> list[tuple[str, str]]:
    """(url, lastmod) for every tag with enough posts; lastmod = newest post change."""
    counts: Counter[str] = Counter()
    newest: dict[str, str] = {}
    for post in posts:
        date = last_modified(post, modified)
        for tag in post.tags:
            counts[tag] += 1
            newest[tag] = max(newest.get(tag, ""), date)
    return [
        (f"{SITE_URL}/tags/{sanitize_filename(tag)}/", newest[tag])
        for tag, count in sorted(counts.items())
        if count >= MIN_TAG_POSTS
    ]


def build_entries(posts: list[Post], modified: dict[str, str]) -> list[tuple[str, str]]:
    post_entries = [(post.url, last_modified(post, modified)) for post in posts]
    site_lastmod = max((date for _, date in post_entries), default="")
    entries = [(f"{SITE_URL}/", site_lastmod), (f"{SITE_URL}/tags/", site_lastmod)]
    return entries + post_entries + tag_entries(posts, modified)


def render(entries: list[tuple[str, str]]) -> ET.ElementTree:
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for loc, lastmod in entries:
        url = ET.SubElement(urlset, "url")
        ET.SubElement(url, "loc").text = loc
        if lastmod:
            ET.SubElement(url, "lastmod").text = lastmod
    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ")
    return tree


def main() -> int:
    posts = load_posts()
    entries = build_entries(posts, modified_dates())
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    render(entries).write(OUTPUT_PATH, encoding="utf-8", xml_declaration=True)
    tags = len(entries) - len(posts) - 2
    print(
        f"sitemap: {len(posts)} posts, {tags} tag pages (>= {MIN_TAG_POSTS} posts) -> {OUTPUT_PATH}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
