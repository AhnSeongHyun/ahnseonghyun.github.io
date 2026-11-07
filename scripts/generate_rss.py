#!/usr/bin/env python3
"""Generate docs/rss.xml: RSS 2.0 with the full HTML body of the newest posts.

The body is taken from the built page (docs/.../index.html, div.post-content) so the
feed matches what zvc rendered, with relative links and images made absolute.
Runs after `zvc build`.
"""

from __future__ import annotations

import re
import sys
from datetime import UTC, datetime
from email.utils import format_datetime
from pathlib import Path
from xml.sax.saxutils import escape

import lxml.html
from site_posts import SITE_URL, Post, load_posts

OUTPUT_PATH = Path("docs/rss.xml")
FEED_SIZE = 30
TITLE = "ASH84"
DESCRIPTION = "Software Engineering, Product Management, Leadership, and Life"
# Control characters XML 1.0 forbids (stray backspaces have shown up in frontmatter).
XML_INVALID_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")


def xml_text(value: str) -> str:
    """Escape for an XML text node and drop characters XML cannot carry at all."""
    return escape(XML_INVALID_RE.sub("", value))


def extract_body(html: str, base_url: str) -> str:
    """Inner HTML of div.post-content with links made absolute; '' when not found."""
    root = lxml.html.fromstring(html)
    nodes = root.find_class("post-content")
    if not nodes:
        return ""
    node = nodes[0]
    node.make_links_absolute(base_url)
    inner = (node.text or "") + "".join(
        lxml.html.tostring(child, encoding="unicode") for child in node
    )
    return inner.strip()


def pub_date_rfc822(date: str) -> str:
    return format_datetime(datetime.strptime(date, "%Y-%m-%d").replace(hour=9, tzinfo=UTC))


def render_item(post: Post, body: str) -> str:
    lines = [
        "    <item>",
        f"      <title>{xml_text(post.title)}</title>",
        f"      <link>{post.url}</link>",
        f'      <guid isPermaLink="true">{post.url}</guid>',
        f"      <pubDate>{pub_date_rfc822(post.pub_date)}</pubDate>",
        f"      <description>{xml_text(post.description)}</description>",
    ]
    lines += [f"      <category>{xml_text(tag)}</category>" for tag in post.tags]
    body = XML_INVALID_RE.sub("", body)
    if body:
        lines.append(
            f"      <content:encoded><![CDATA[{body.replace(']]>', ']]]]><![CDATA[>')}]]></content:encoded>"
        )
    lines.append("    </item>")
    return "\n".join(lines)


def render_feed(items: list[str], build_date: datetime | None = None) -> str:
    build_date = build_date or datetime.now(UTC)
    head = "\n".join(
        [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"'
            ' xmlns:content="http://purl.org/rss/1.0/modules/content/">',
            "  <channel>",
            f"    <title>{TITLE}</title>",
            f"    <link>{SITE_URL}/</link>",
            f"    <description>{DESCRIPTION}</description>",
            "    <language>ko</language>",
            f"    <lastBuildDate>{format_datetime(build_date)}</lastBuildDate>",
            f'    <atom:link href="{SITE_URL}/rss.xml" rel="self" type="application/rss+xml" />',
        ]
    )
    tail = "\n  </channel>\n</rss>\n"
    return head + "\n" + "\n".join(items) + tail


def body_for(post: Post) -> str:
    try:
        html = post.html_path.read_text(encoding="utf-8")
    except OSError:
        return ""
    return extract_body(html, post.url)


def main() -> int:
    posts = load_posts()[:FEED_SIZE]
    items = [render_item(post, body_for(post)) for post in posts]
    OUTPUT_PATH.write_text(render_feed(items), encoding="utf-8")
    print(f"rss: {len(items)} items -> {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
