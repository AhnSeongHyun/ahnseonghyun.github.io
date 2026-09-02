import normalize_tags

BODY = "\n본문 첫 줄.\n\n```shell\nls -la\n```\n"


def doc(tags_text: str) -> str:
    return (
        "---\n"
        "title: '자기증명'\n"
        "author: ash84\n"
        "pub_date: '2026-06-02'\n"
        "description: \n"
        f"{tags_text}\n"
        "---\n" + BODY
    )


def test_block_list_becomes_inline_and_rest_is_untouched():
    result = normalize_tags.rewrite(doc("tags:\n- 자기증명\n- 커리어"))

    assert result == doc("tags: ['자기증명', '커리어']")
    assert result.endswith(BODY)


def test_hashtag_string_is_split_and_other_tags_kept():
    result = normalize_tags.rewrite(doc("tags:\n- '#ash84 #회고 #2023 #essay'\n- retrospective"))

    # '회고' -> 'retrospective' comes from consolidate_tags rules, then duplicates collapse
    assert result == doc("tags: ['ash84', 'retrospective', '2023', 'essay']")


def test_empty_tags_dropped_and_entities_decoded():
    result = normalize_tags.rewrite(doc("tags: ['', 'moet&amp;chandon', 'dev']"))

    assert result == doc("tags: ['moet&chandon', 'dev']")


def test_consolidation_rules_and_duplicates():
    result = normalize_tags.rewrite(doc("tags: ['python', 'Python', 'dev']"))

    assert result == doc("tags: ['Python', 'dev']")


def test_unchanged_document_returns_none():
    assert normalize_tags.rewrite(doc("tags: ['dev', 'essay']")) is None
    assert normalize_tags.rewrite("no frontmatter here\n") is None
    assert normalize_tags.rewrite("---\ntitle: x\n---\nbody\n") is None


def test_tag_with_single_quote_uses_double_quotes():
    assert normalize_tags.format_inline(["SVN error folder '' does not exist"]) == (
        "tags: [\"SVN error folder '' does not exist\"]"
    )


def test_block_list_stops_at_next_key():
    section = normalize_tags.find_tags_section("tags:\n- a\n- b\nfeatured_image: x.jpg")

    assert section.tags == ["a", "b"]
    assert (
        "featured_image"
        not in "tags:\n- a\n- b\nfeatured_image: x.jpg"[section.start : section.end]
    )
