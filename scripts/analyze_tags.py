#!/usr/bin/env python3
"""
Tag Analysis Script for ash84.io

Analyzes all tags and suggests consolidation opportunities.
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
                # Remove brackets and quotes, split by comma
                value = value[1:-1]  # Remove [ ]
                items = [item.strip().strip("'\"") for item in value.split(',')]
                data[key] = items
            else:
                # Remove quotes
                data[key] = value.strip("'\"")

    return data


def collect_all_tags():
    """Collect all tags with their usage count."""
    tags_counter = Counter()
    contents_path = Path('contents')

    # Find all markdown files
    for md_file in contents_path.rglob('*.md'):
        try:
            content = md_file.read_text(encoding='utf-8')
            frontmatter_text = extract_frontmatter(content)

            if not frontmatter_text:
                continue

            metadata = parse_frontmatter(frontmatter_text)
            tags = metadata.get('tags', [])

            for tag in tags:
                if tag:  # Skip empty tags
                    tags_counter[tag] += 1

        except Exception:
            continue

    return tags_counter


def categorize_tags(tags_counter):
    """Categorize tags into different groups."""

    categories = {
        'programming_languages': [],
        'frameworks_libraries': [],
        'tools_platforms': [],
        'korean_duplicates': [],
        'english_duplicates': [],
        'single_use': [],
        'popular': [],
        'case_variants': defaultdict(list),
        'spacing_variants': defaultdict(list),
    }

    # Programming languages
    prog_langs = {
        'python', 'java', 'javascript', 'c#', 'c++', 'go', 'rust', 'ruby', 'php',
        'swift', 'kotlin', 'typescript', 'scala', 'r', 'matlab', 'objective-c',
        'objective c', 'c', 'js', 'ts'
    }

    # Common frameworks/libraries
    frameworks = {
        'react', 'vue', 'angular', 'django', 'flask', 'spring', 'express',
        'nextjs', 'nuxt', 'fastapi', 'rails', 'laravel', 'vert.x', 'jquery'
    }

    # Tools and platforms
    tools = {
        'git', 'github', 'docker', 'kubernetes', 'aws', 'azure', 'gcp',
        'vscode', 'xcode', 'intellij', 'postman', 'nginx', 'redis', 'mongodb',
        'postgresql', 'mysql', 'elasticsearch'
    }

    for tag, count in tags_counter.items():
        tag_lower = tag.lower()

        # Categorize by type
        if tag_lower in prog_langs:
            categories['programming_languages'].append((tag, count))
        elif tag_lower in frameworks:
            categories['frameworks_libraries'].append((tag, count))
        elif tag_lower in tools:
            categories['tools_platforms'].append((tag, count))

        # Single use tags
        if count == 1:
            categories['single_use'].append((tag, count))

        # Popular tags (>= 10 posts)
        if count >= 10:
            categories['popular'].append((tag, count))

        # Case variants (same tag, different case)
        categories['case_variants'][tag_lower].append((tag, count))

        # Spacing variants
        normalized = tag_lower.replace(' ', '').replace('-', '').replace('_', '')
        categories['spacing_variants'][normalized].append((tag, count))

    # Filter to only show actual duplicates
    categories['case_variants'] = {k: v for k, v in categories['case_variants'].items() if len(v) > 1}
    categories['spacing_variants'] = {k: v for k, v in categories['spacing_variants'].items() if len(v) > 1}

    return categories


def suggest_consolidations(tags_counter):
    """Suggest tag consolidations."""

    suggestions = []

    # Language variations
    lang_groups = {
        'Python': ['python', 'Python', 'PYTHON', 'python3', 'python2'],
        'JavaScript': ['javascript', 'JavaScript', 'JS', 'js', 'Java Script'],
        'iOS': ['ios', 'IOS', 'iOS', 'i os', 'i OS'],
        'Android': ['android', 'Android', 'ANDROID'],
        'C#': ['c#', 'C#', 'csharp', 'CSharp'],
        'C++': ['c++', 'C++', 'cpp', 'CPP'],
    }

    for canonical, variants in lang_groups.items():
        found_variants = []
        total_count = 0
        for variant in variants:
            if variant in tags_counter:
                found_variants.append((variant, tags_counter[variant]))
                total_count += tags_counter[variant]

        if len(found_variants) > 1:
            suggestions.append({
                'type': 'language_consolidation',
                'canonical': canonical,
                'variants': found_variants,
                'total_posts': total_count
            })

    # Common tech term duplicates
    tech_groups = {
        'API': ['api', 'API', 'Api'],
        'REST': ['rest', 'REST', 'Rest'],
        'ML': ['ml', 'ML', 'machine learning', 'Machine Learning'],
        'AI': ['ai', 'AI', 'artificial intelligence'],
    }

    for canonical, variants in tech_groups.items():
        found_variants = []
        total_count = 0
        for variant in variants:
            if variant in tags_counter:
                found_variants.append((variant, tags_counter[variant]))
                total_count += tags_counter[variant]

        if len(found_variants) > 1:
            suggestions.append({
                'type': 'tech_term_consolidation',
                'canonical': canonical,
                'variants': found_variants,
                'total_posts': total_count
            })

    return suggestions


def main():
    """Main analysis function."""

    print("🔍 Analyzing tags...")
    print()

    # Collect all tags
    tags_counter = collect_all_tags()

    print(f"📊 Total unique tags: {len(tags_counter)}")
    print(f"📝 Total tag usages: {sum(tags_counter.values())}")
    print()

    # Top 20 tags
    print("🏆 Top 20 Most Used Tags:")
    print("-" * 60)
    for tag, count in tags_counter.most_common(20):
        print(f"  #{tag:<40} {count:>5} posts")
    print()

    # Categorize tags
    categories = categorize_tags(tags_counter)

    print(f"💻 Programming Languages: {len(categories['programming_languages'])}")
    for tag, count in sorted(categories['programming_languages'], key=lambda x: -x[1])[:10]:
        print(f"  #{tag:<20} {count:>4} posts")
    print()

    print(f"🔧 Frameworks/Libraries: {len(categories['frameworks_libraries'])}")
    for tag, count in sorted(categories['frameworks_libraries'], key=lambda x: -x[1])[:10]:
        print(f"  #{tag:<20} {count:>4} posts")
    print()

    print(f"🛠️  Tools/Platforms: {len(categories['tools_platforms'])}")
    for tag, count in sorted(categories['tools_platforms'], key=lambda x: -x[1])[:10]:
        print(f"  #{tag:<20} {count:>4} posts")
    print()

    print(f"⚠️  Single-use tags: {len(categories['single_use'])} (consider removing)")
    print()

    # Case variants
    if categories['case_variants']:
        print(f"🔤 Case Variants (same tag, different case): {len(categories['case_variants'])}")
        print("-" * 60)
        for normalized, variants in sorted(categories['case_variants'].items(),
                                          key=lambda x: -sum(v[1] for v in x[1]))[:20]:
            total = sum(v[1] for v in variants)
            print(f"  '{normalized}' -> {total} total posts")
            for tag, count in sorted(variants, key=lambda x: -x[1]):
                print(f"    #{tag:<30} {count:>4} posts")
        print()

    # Consolidation suggestions
    suggestions = suggest_consolidations(tags_counter)

    if suggestions:
        print("💡 Consolidation Suggestions:")
        print("-" * 60)
        for suggestion in suggestions:
            print(f"\n  Consolidate to: #{suggestion['canonical']}")
            print(f"  Total posts: {suggestion['total_posts']}")
            print("  Variants to merge:")
            for variant, count in suggestion['variants']:
                print(f"    #{variant:<30} {count:>4} posts")
        print()

    # SEO recommendations
    print("🎯 SEO Recommendations:")
    print("-" * 60)
    print("  1. Keep: Popular tags (>= 10 posts)")
    print(f"     Count: {len(categories['popular'])}")
    print()
    print("  2. Consider removing: Single-use tags")
    print(f"     Count: {len(categories['single_use'])}")
    print()
    print("  3. Consolidate: Case variants and duplicates")
    print(f"     Potential merges: {len(categories['case_variants']) + len(suggestions)}")
    print()
    print("  4. Use canonical forms:")
    print("     - Programming languages: Python, JavaScript, Java (capitalized)")
    print("     - Platforms: iOS, macOS, Android (official capitalization)")
    print("     - Technologies: API, REST, SQL (uppercase acronyms)")
    print()


if __name__ == '__main__':
    main()
