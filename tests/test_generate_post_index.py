from pathlib import Path

import generate_post_index as post_index


def write_post(root: Path, slug: str, frontmatter: str) -> Path:
    folder = root / slug
    folder.mkdir()
    path = folder / f"{slug}.md"
    path.write_text(f"---\n{frontmatter}\n---\n\n본문\n", encoding="utf-8")
    return path


def test_read_post_builds_link_from_pub_date_and_unquotes_title(tmp_path):
    path = write_post(tmp_path, "2026-self-proof", "title: '자기증명'\npub_date: '2026-06-02'")

    assert post_index.read_post(path) == [
        "2026-self-proof",
        "자기증명",
        "/2026/06/02/2026-self-proof/",
        "2026-06-02",
    ]


def test_read_post_skips_drafts_and_invalid_dates(tmp_path):
    draft = write_post(tmp_path, "draft-post", "title: d\npub_date: '2026-01-01'\nstatus: draft")
    bad_date = write_post(tmp_path, "bad-date", "title: b\npub_date: soon")
    no_frontmatter = tmp_path / "plain.md"
    no_frontmatter.write_text("just text\n", encoding="utf-8")

    assert post_index.read_post(draft) is None
    assert post_index.read_post(bad_date) is None
    assert post_index.read_post(no_frontmatter) is None


def test_build_index_sorts_newest_first_then_slug(tmp_path):
    paths = [
        write_post(tmp_path, "older", "title: older\npub_date: '2025-12-30'"),
        write_post(tmp_path, "b-same-day", "title: b\npub_date: '2026-08-08'"),
        write_post(tmp_path, "a-same-day", "title: a\npub_date: '2026-08-08'"),
        write_post(tmp_path, "untitled", "pub_date: '2026-01-01'"),
    ]

    rows = post_index.build_index(paths)

    assert [row[0] for row in rows] == ["b-same-day", "a-same-day", "untitled", "older"]
    assert rows[2][1] == "untitled"


def test_write_index_is_compact_json(tmp_path):
    output = tmp_path / "docs" / "meta" / "posts.json"
    post_index.write_index([["s", "t", "/2026/01/01/s/", "2026-01-01"]], output)

    assert output.read_text(encoding="utf-8") == '[["s","t","/2026/01/01/s/","2026-01-01"]]\n'
