#!/usr/bin/env python3
"""
Find Korean-English duplicate tags and similar tags
"""

import re
from pathlib import Path
from collections import defaultdict, Counter


def extract_frontmatter(content):
    """Extract frontmatter from markdown content."""
    pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.match(pattern, content, re.DOTALL)
    if match:
        return match.group(1)
    return None


def parse_frontmatter(frontmatter_text):
    """Parse frontmatter text into a dictionary."""
    data = {}
    for line in frontmatter_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()

            # Handle lists (tags)
            if value.startswith('[') and value.endswith(']'):
                value = value[1:-1]
                items = [item.strip().strip("'\"") for item in value.split(',')]
                data[key] = items
            else:
                data[key] = value.strip("'\"")

    return data


def collect_all_tags():
    """Collect all tags with their usage count."""
    tags_counter = Counter()
    contents_path = Path('contents')

    for md_file in contents_path.rglob('*.md'):
        try:
            content = md_file.read_text(encoding='utf-8')
            frontmatter_text = extract_frontmatter(content)

            if not frontmatter_text:
                continue

            metadata = parse_frontmatter(frontmatter_text)
            tags = metadata.get('tags', [])

            for tag in tags:
                if tag:
                    tags_counter[tag] += 1

        except Exception:
            continue

    return tags_counter


def find_korean_english_pairs(tags_counter):
    """Find likely Korean-English duplicate tags."""

    # Common known pairs
    known_pairs = {
        '파이썬': 'Python',
        '자바': 'Java',
        '개발자': 'developer',
        '프로그래밍': 'programming',
        '아이폰': 'iPhone',
        '안드로이드': 'Android',
        '데이터베이스': 'database',
        '알고리즘': 'algorithm',
        '머신러닝': 'machine learning',
        '딥러닝': 'deep learning',
        '인공지능': 'AI',
        '백엔드': 'backend',
        '프론트엔드': 'frontend',
        '웹개발': 'web development',
        '모바일': 'mobile',
        '서버': 'server',
        '클라우드': 'cloud',
        '도커': 'docker',
        '쿠버네티스': 'kubernetes',
    }

    pairs = []
    for korean, english in known_pairs.items():
        korean_variants = [k for k in tags_counter.keys() if korean in k]
        english_variants = [e for e in tags_counter.keys() if english.lower() in e.lower()]

        if korean_variants or english_variants:
            korean_count = sum(tags_counter[k] for k in korean_variants)
            english_count = sum(tags_counter[e] for e in english_variants)

            if korean_count > 0 or english_count > 0:
                pairs.append({
                    'korean': korean_variants,
                    'english': english_variants,
                    'korean_count': korean_count,
                    'english_count': english_count,
                    'canonical': english
                })

    return pairs


def find_similar_tags(tags_counter):
    """Find tags that are very similar (typos, spacing, etc)."""

    similar_groups = defaultdict(list)

    # Group by normalized form
    for tag in tags_counter.keys():
        # Normalize: lowercase, remove spaces/hyphens/underscores
        normalized = tag.lower().replace(' ', '').replace('-', '').replace('_', '')
        similar_groups[normalized].append(tag)

    # Filter to only show groups with multiple tags
    similar = {k: v for k, v in similar_groups.items() if len(v) > 1}

    return similar


def main():
    """Main function."""

    print("🔍 Finding Duplicate and Similar Tags...\n")

    tags_counter = collect_all_tags()

    # Korean-English duplicates
    print("🌏 Korean-English Duplicate Tags:")
    print("-" * 80)

    pairs = find_korean_english_pairs(tags_counter)
    for pair in sorted(pairs, key=lambda x: -(x['korean_count'] + x['english_count'])):
        if pair['korean_count'] > 0 or pair['english_count'] > 0:
            total = pair['korean_count'] + pair['english_count']
            print(f"\n  Canonical: #{pair['canonical']} (Total: {total} posts)")

            if pair['korean']:
                print(f"  Korean variants ({pair['korean_count']} posts):")
                for tag in pair['korean']:
                    print(f"    #{tag:<30} {tags_counter[tag]:>4} posts")

            if pair['english']:
                print(f"  English variants ({pair['english_count']} posts):")
                for tag in pair['english']:
                    print(f"    #{tag:<30} {tags_counter[tag]:>4} posts")

    print("\n")

    # Similar tags
    print("🔀 Similar Tags (different spacing/punctuation):")
    print("-" * 80)

    similar = find_similar_tags(tags_counter)
    for normalized, variants in sorted(similar.items(),
                                      key=lambda x: -sum(tags_counter[v] for v in x[1]))[:30]:
        total = sum(tags_counter[v] for v in variants)
        if total >= 3:  # Only show if total usage >= 3
            print(f"\n  Total: {total} posts")
            for tag in sorted(variants, key=lambda x: -tags_counter[x]):
                print(f"    #{tag:<40} {tags_counter[tag]:>4} posts")

    # Empty/whitespace tags
    print("\n")
    print("⚠️  Problematic Tags:")
    print("-" * 80)

    empty_tags = [tag for tag in tags_counter.keys() if not tag.strip() or tag == ' ']
    if empty_tags:
        print(f"\n  Empty/whitespace tags: {len(empty_tags)}")
        for tag in empty_tags:
            print(f"    '{tag}' ({tags_counter[tag]} posts)")

    single_char_tags = [tag for tag in tags_counter.keys() if len(tag.strip()) <= 2]
    if single_char_tags:
        print(f"\n  Very short tags (<=2 chars): {len(single_char_tags)}")
        for tag in sorted(single_char_tags, key=lambda x: -tags_counter[x])[:20]:
            print(f"    #{tag:<10} {tags_counter[tag]:>4} posts")


if __name__ == '__main__':
    main()
