import generate_sitemap as sitemap
from site_posts import Post


def post(slug, date, *tags):
    y, m, d = date.split("-")
    return Post(slug, slug, f"/{y}/{m}/{d}/{slug}/", date, tags=tags)


def test_build_entries_lists_home_tags_posts_and_only_shared_tags():
    posts = [post("b", "2026-08-08", "dev", "c/c++"), post("a", "2026-06-02", "dev", "once")]

    entries = sitemap.build_entries(posts, {"a": "2026-09-01"})

    assert entries == [
        ("https://ash84.io/", "2026-09-01"),
        ("https://ash84.io/tags/", "2026-09-01"),
        ("https://ash84.io/2026/08/08/b/", "2026-08-08"),
        ("https://ash84.io/2026/06/02/a/", "2026-09-01"),
        ("https://ash84.io/tags/dev/", "2026-09-01"),
    ]


def test_tag_entries_sanitize_names_like_tag_pages():
    posts = [post("a", "2026-01-01", "c/c++"), post("b", "2026-01-02", "c/c++")]

    assert sitemap.tag_entries(posts, {}) == [("https://ash84.io/tags/c-c++/", "2026-01-02")]


def test_render_writes_loc_and_lastmod_without_changefreq():
    tree = sitemap.render([("https://ash84.io/", "2026-01-01")])
    url = tree.getroot()[0]

    assert [child.tag for child in url] == ["loc", "lastmod"]
    assert url[1].text == "2026-01-01"
