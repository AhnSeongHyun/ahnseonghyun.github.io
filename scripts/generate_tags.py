#!/usr/bin/env python3
"""
Tag Pages Generator for ash84.io

Generates tag pages from all blog posts.
Each tag gets its own page listing all posts with that tag.
"""

import re
from pathlib import Path
from collections import defaultdict
from jinja2 import Environment, FileSystemLoader


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


def collect_posts_by_tag():
    """Collect all posts and group them by tags."""
    tags_dict = defaultdict(list)
    contents_path = Path('contents')

    # Find all markdown files
    for md_file in contents_path.rglob('*.md'):
        try:
            content = md_file.read_text(encoding='utf-8')
            frontmatter_text = extract_frontmatter(content)

            if not frontmatter_text:
                continue

            metadata = parse_frontmatter(frontmatter_text)

            # Get tags
            tags = metadata.get('tags', [])
            if not tags:
                continue

            # Get post info
            title = metadata.get('title', 'Untitled')
            pub_date = metadata.get('pub_date', '')
            description = metadata.get('description', '')

            # Generate post URL from pub_date and directory name
            # pub_date format: '2026-01-10' -> /2026/01/10/post-name/
            if pub_date:
                year, month, day = pub_date.split('-')
                post_name = md_file.parent.name
                post_url = f"/{year}/{month}/{day}/{post_name}/"
            else:
                continue

            post_data = {
                'title': title,
                'pub_date': pub_date,
                'description': description,
                'link': post_url
            }

            # Add post to each tag
            for tag in tags:
                tags_dict[tag].append(post_data)

        except Exception as e:
            print(f"⚠️  Warning: Failed to process {md_file}: {e}")
            continue

    return tags_dict


def sort_posts_by_date(posts):
    """Sort posts by publication date (newest first)."""
    return sorted(posts, key=lambda x: x['pub_date'], reverse=True)


def sanitize_filename(tag):
    """Convert tag name to safe filename."""
    # Replace / with - to avoid directory issues
    safe_name = tag.replace('/', '-')
    # Replace other problematic characters
    safe_name = safe_name.replace('\\', '-')
    safe_name = safe_name.replace(':', '-')
    return safe_name


def generate_tag_pages(tags_dict):
    """Generate HTML pages for each tag."""

    # Setup Jinja2 environment
    env = Environment(loader=FileSystemLoader('.'))
    tag_template = env.get_template('themes/chronicle/tag.html')
    index_template = env.get_template('themes/chronicle/tags-index.html')

    # Create tags directory
    tags_dir = Path('docs/tags')
    tags_dir.mkdir(parents=True, exist_ok=True)

    # Prepare tag list for index page
    tag_list = []

    # Generate page for each tag
    for tag, posts in tags_dict.items():
        # Sort posts by date (newest first)
        sorted_posts = sort_posts_by_date(posts)

        # Render template
        html = tag_template.render(
            tag_info={'name': tag, 'count': len(sorted_posts)},
            posts=sorted_posts
        )

        # Create directory for tag and write index.html
        safe_filename = sanitize_filename(tag)
        tag_dir = tags_dir / safe_filename
        tag_dir.mkdir(parents=True, exist_ok=True)
        tag_file = tag_dir / "index.html"
        tag_file.write_text(html, encoding='utf-8')

        print(f"  ✓ Created {safe_filename}/index.html ({len(sorted_posts)} posts)")

        # Add to tag list
        tag_list.append({
            'name': tag,
            'safe_name': safe_filename,
            'count': len(sorted_posts)
        })

    # Sort tag list by post count (descending), then by name
    tag_list_sorted = sorted(tag_list, key=lambda x: (-x['count'], x['name']))

    # Generate tags index page
    index_html = index_template.render(
        all_tags=tag_list_sorted
    )
    index_file = tags_dir / "index.html"
    index_file.write_text(index_html, encoding='utf-8')
    print(f"\n  ✓ Created tags index page with {len(tag_list_sorted)} tags")

    return len(tags_dict)


def main():
    """Main function."""
    print("🏷️  Generating tag pages...")

    # Collect posts by tag
    tags_dict = collect_posts_by_tag()

    if not tags_dict:
        print("⚠️  No tags found in posts")
        return

    # Generate tag pages
    tag_count = generate_tag_pages(tags_dict)

    print("\n✅ Tag pages generated successfully!")
    print(f"📊 Total tags: {tag_count}")
    print("📍 Location: docs/tags/")

    # Show sample tags
    print("\n📝 Sample tags:")
    for tag in sorted(tags_dict.keys())[:10]:
        print(f"   - {tag} ({len(tags_dict[tag])} posts)")

    if len(tags_dict) > 10:
        print(f"   ... and {len(tags_dict) - 10} more")


if __name__ == '__main__':
    main()
