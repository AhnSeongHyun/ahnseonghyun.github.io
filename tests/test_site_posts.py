from pathlib import Path

import site_posts
from generate_git_meta import Commit


def write_post(root: Path, slug: str, frontmatter: str) -> Path:
    folder = root / slug
    folder.mkdir()
    path = folder / f"{slug}.md"
    path.write_text(f"---\n{frontmatter}\n---\n\n본문\n", encoding="utf-8")
    return path


def test_read_post_parses_inline_tags_and_link(tmp_path):
    path = write_post(
        tmp_path,
        "self-proof",
        "title: '자기증명'\npub_date: '2026-06-02'\ndescription: 'd'\ntags: ['essay', 'cto', '']",
    )
    post = site_posts.read_post(path)
    assert post == site_posts.Post(
        slug="self-proof",
        title="자기증명",
        link="/2026/06/02/self-proof/",
        pub_date="2026-06-02",
        description="d",
        tags=("essay", "cto"),
    )
    assert post.url == "https://ash84.io/2026/06/02/self-proof/"
    assert post.html_path == Path("docs/2026/06/02/self-proof/index.html")


def test_read_post_ignores_block_list_tags_drafts_and_bad_dates(tmp_path):
    block = write_post(tmp_path, "block", "title: b\npub_date: '2026-01-01'\ntags:\n  - a")
    draft = write_post(tmp_path, "draft", "title: d\npub_date: '2026-01-01'\nstatus: draft")
    bad = write_post(tmp_path, "bad", "title: b\npub_date: soon")

    assert site_posts.read_post(block).tags == ()
    assert site_posts.read_post(draft) is None
    assert site_posts.read_post(bad) is None


def test_load_posts_newest_first(tmp_path):
    write_post(tmp_path, "old", "title: o\npub_date: '2020-01-01'")
    write_post(tmp_path, "new", "title: n\npub_date: '2026-01-01'")

    assert [p.slug for p in site_posts.load_posts(tmp_path)] == ["new", "old"]


def commit(hash_, date, *slugs):
    return Commit(hash_, date, "msg", tuple(f"contents/{s}/{s}.md" for s in slugs))


def test_modified_from_commits_skips_bulk_commits_and_keeps_newest():
    commits = [
        commit("c3", "2026-09-03", *[f"p{i}" for i in range(30)]),  # bulk: ignored
        commit("c2", "2026-08-08", "p1", "p2"),
        commit("c1", "2026-06-02", "p1"),
    ]
    modified = site_posts.modified_from_commits(commits, bulk_limit=20)

    assert modified == {"p1": "2026-08-08", "p2": "2026-08-08"}


def test_modified_from_commits_ignores_files_outside_contents():
    commits = [Commit("c1", "2026-01-01", "m", ("themes/ledger/post.html", "Makefile"))]

    assert site_posts.modified_from_commits(commits) == {}


def test_last_modified_prefers_git_only_after_publication():
    post = site_posts.Post("p", "t", "/2026/06/02/p/", "2026-06-02")

    assert site_posts.last_modified(post, {"p": "2026-08-08"}) == "2026-08-08"
    assert site_posts.last_modified(post, {"p": "2026-03-10"}) == "2026-06-02"
    assert site_posts.last_modified(post, {}) == "2026-06-02"


def test_modified_dates_returns_empty_when_git_unavailable():
    assert site_posts.modified_dates(lambda args: None) == {}
