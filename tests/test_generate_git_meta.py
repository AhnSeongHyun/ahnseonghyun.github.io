from datetime import datetime, timezone

import generate_git_meta as git_meta

RS = git_meta.RECORD_SEPARATOR
FS = git_meta.FIELD_SEPARATOR

SAMPLE_LOG = (
    f"{RS}bbb4a2e5{FS}2026-08-08{FS}docs: title | with pipe\n\n"
    "contents/odyssey/odyssey.md\n\n"
    f"{RS}fa8eadd9{FS}2026-06-02{FS}ui: selected + typo\n\n"
    "contents/2026-self-proof/2026-self-proof.md\n"
    "themes/chronicle/index.html\n\n"
    f"{RS}80524475{FS}2026-06-02{FS}feat: self-proof\n\n"
    "contents/2026-self-proof/2026-self-proof.md\n"
    "contents/2026-self-proof/cover.jpg\n\n"
    f"{RS}8320f602{FS}2026-08-02{FS}fix: build\n\n"
    "Makefile\n"
)


def test_parse_log_keeps_separator_characters_in_message():
    commits = git_meta.parse_log(SAMPLE_LOG)

    assert [commit.hash for commit in commits] == ["bbb4a2e5", "fa8eadd9", "80524475", "8320f602"]
    assert commits[0].message == "docs: title | with pipe"
    assert commits[0].date == "2026-08-08"
    assert commits[2].files == (
        "contents/2026-self-proof/2026-self-proof.md",
        "contents/2026-self-proof/cover.jpg",
    )


def test_slug_from_path_ignores_paths_outside_contents():
    assert (
        git_meta.slug_from_path("contents/2026-self-proof/2026-self-proof.md") == "2026-self-proof"
    )
    assert git_meta.slug_from_path("themes/chronicle/index.html") is None
    assert git_meta.slug_from_path("Makefile") is None
    assert git_meta.slug_from_path("contents/loose-file.md") is None


def test_group_by_slug_orders_newest_first_and_deduplicates_within_commit():
    posts = git_meta.group_by_slug(git_meta.parse_log(SAMPLE_LOG))

    assert [commit["hash"] for commit in posts["2026-self-proof"]] == ["fa8eadd9", "80524475"]
    assert [commit["hash"] for commit in posts["odyssey"]] == ["bbb4a2e5"]
    assert "Makefile" not in posts
    assert "themes" not in posts


def test_build_meta_changelog_is_top_three_and_schema_is_stable():
    fixed_now = datetime(2026, 9, 2, 12, 0, tzinfo=timezone.utc)
    meta = git_meta.build_meta(git_meta.parse_log(SAMPLE_LOG), total_commits=98, now=fixed_now)

    assert set(meta) == {"generated_at", "total_commits", "changelog", "posts"}
    assert meta["generated_at"] == "2026-09-02T12:00:00+00:00"
    assert meta["total_commits"] == 98
    assert [commit["hash"] for commit in meta["changelog"]] == ["bbb4a2e5", "fa8eadd9", "80524475"]
    assert set(meta["changelog"][0]) == {"hash", "date", "message"}


def test_collect_without_git_returns_empty_meta():
    meta = git_meta.collect(run=lambda args: None)

    assert meta["changelog"] == []
    assert meta["posts"] == {}
    assert meta["total_commits"] == 0


def test_collect_uses_runner_output():
    def fake_run(args):
        if args[0] == "log":
            return SAMPLE_LOG
        if args[0] == "rev-list":
            return "98\n"
        raise AssertionError(f"unexpected git args: {args}")

    meta = git_meta.collect(run=fake_run)

    assert meta["total_commits"] == 98
    assert len(meta["posts"]) == 2


def test_write_meta_creates_parent_directory(tmp_path):
    output = tmp_path / "docs" / "meta" / "git.json"
    git_meta.write_meta({"changelog": [], "posts": {}, "total_commits": 0}, output)

    assert output.exists()
    assert output.read_text(encoding="utf-8").endswith("}\n")
