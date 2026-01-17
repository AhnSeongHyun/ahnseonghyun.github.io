#!/usr/bin/env python3
"""
robots.txt Generator for ash84.io
"""


def generate_robots():
    """Generate robots.txt file."""

    content = """# ash84.io robots.txt
User-agent: *
Allow: /

# Sitemap
Sitemap: https://ash84.io/sitemap.xml

# Crawl-delay for respectful crawling
Crawl-delay: 1
"""

    with open('docs/robots.txt', 'w') as f:
        f.write(content)

    print("✅ robots.txt generated successfully!")
    print("📍 Location: docs/robots.txt")


if __name__ == '__main__':
    generate_robots()
