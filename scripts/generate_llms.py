#!/usr/bin/env python3
"""Generate docs/llms.txt (https://llmstxt.org): a markdown index for LLM crawlers.

Evidence that AI crawlers read this file is thin; it costs one build step, so it is
kept small: who the author is, where the feeds are, the newest posts with their
descriptions, and the largest tags.
"""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

from generate_tags import sanitize_filename
from site_posts import SITE_URL, Post, load_posts

OUTPUT_PATH = Path("docs/llms.txt")
RECENT_POSTS = 50
TOP_TAGS = 20

INTRO = """\
# ash84.io

> 안성현(ash84)의 개인 블로그. 소프트웨어 엔지니어링, 기술 리더십, 회고, 에세이. \
Payhere Head of Technology(전 CTO·공동창업자), 전 뱅크샐러드 테크리드. 2007년부터 한국어로 씀.

- 글 URL: {site}/YYYY/MM/DD/{{slug}}/ (pub_date 기준)
- RSS: {site}/rss.xml (최신 글 전문 포함)
- 사이트맵: {site}/sitemap.xml
- 태그: {site}/tags/
- 소개: https://ash84.notion.site/Ahn-Seong-Hyun-28f5e7909eab80389bace8eddbfdd105
- GitHub: https://github.com/AhnSeongHyun/
- LinkedIn: https://www.linkedin.com/in/seonghyun-ahn-9098a640/
"""


def render(posts: list[Post]) -> str:
    lines = [
        INTRO.format(site=SITE_URL),
        f"## 최근 글 ({len(posts)}편 중 {min(RECENT_POSTS, len(posts))}편)",
        "",
    ]
    for post in posts[:RECENT_POSTS]:
        desc = f": {post.description}" if post.description else ""
        lines.append(f"- [{post.title}]({post.url}) ({post.pub_date}){desc}")
    counts = Counter(tag for post in posts for tag in post.tags)
    lines += ["", f"## 주요 태그 (상위 {TOP_TAGS})", ""]
    for tag, count in counts.most_common(TOP_TAGS):
        lines.append(f"- [{tag}]({SITE_URL}/tags/{sanitize_filename(tag)}/): {count}편")
    return "\n".join(lines) + "\n"


def main() -> int:
    posts = load_posts()
    OUTPUT_PATH.write_text(render(posts), encoding="utf-8")
    print(f"llms.txt: {min(RECENT_POSTS, len(posts))} recent posts -> {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
