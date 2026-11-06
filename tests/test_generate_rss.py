from datetime import UTC, datetime

import generate_rss as rss
from site_posts import Post

PAGE = """<html><body><article>
<div class="post-content" data-pagefind-body>
<p>intro &amp; <a href="/2020/01/01/other/">link</a></p>
<img src="cover.jpg">
</div>
<section class="hist">ignored</section>
</article></body></html>"""


def test_extract_body_makes_links_absolute_and_drops_wrapper():
    body = rss.extract_body(PAGE, "https://ash84.io/2026/06/02/p/")

    assert body.startswith("<p>intro &amp; ")
    assert 'href="https://ash84.io/2020/01/01/other/"' in body
    assert 'src="https://ash84.io/2026/06/02/p/cover.jpg"' in body
    assert "post-content" not in body
    assert "ignored" not in body


def test_extract_body_returns_empty_when_no_content_div():
    assert rss.extract_body("<html><body><p>x</p></body></html>", "https://ash84.io/") == ""


def test_render_item_escapes_text_and_wraps_body_in_cdata():
    post = Post("p", "A & B <c>", "/2026/06/02/p/", "2026-06-02", "d & e", ("x", "y"))

    item = rss.render_item(post, "<p>body ]]> end</p>")

    assert "<title>A &amp; B &lt;c&gt;</title>" in item
    assert "<description>d &amp; e</description>" in item
    assert "<category>x</category>" in item and "<category>y</category>" in item
    assert "<pubDate>Tue, 02 Jun 2026 09:00:00 +0000</pubDate>" in item
    assert "<![CDATA[<p>body ]]]]><![CDATA[> end</p>]]>" in item


def test_render_item_strips_characters_xml_forbids():
    post = Post("p", "t\x08itle", "/2026/06/02/p/", "2026-06-02", "d\x0cesc")

    item = rss.render_item(post, "<p>bo\x08dy</p>")

    assert "<title>title</title>" in item
    assert "<description>desc</description>" in item
    assert "<p>body</p>" in item


def test_render_item_without_body_has_no_content_encoded():
    post = Post("p", "t", "/2026/06/02/p/", "2026-06-02")

    assert "content:encoded" not in rss.render_item(post, "")


def test_render_feed_has_channel_metadata_and_self_link():
    feed = rss.render_feed(["    <item></item>"], datetime(2026, 1, 1, tzinfo=UTC))

    assert feed.startswith('<?xml version="1.0" encoding="UTF-8"?>')
    assert '<atom:link href="https://ash84.io/rss.xml" rel="self"' in feed
    assert "<lastBuildDate>Thu, 01 Jan 2026 00:00:00 +0000</lastBuildDate>" in feed
    assert feed.endswith("</rss>\n")
