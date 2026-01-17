#!/usr/bin/env python3
"""
Sitemap Generator for ash84.io

Generates sitemap.xml from built HTML files in the docs directory.
"""

import os
from datetime import datetime
from pathlib import Path
import xml.etree.ElementTree as ET


def get_last_modified(file_path):
    """Get last modified time of a file."""
    try:
        mtime = os.path.getmtime(file_path)
        return datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
    except:
        return datetime.now().strftime('%Y-%m-%d')


def generate_sitemap():
    """Generate sitemap.xml for the blog."""

    # XML namespace
    urlset = ET.Element('urlset', xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    # Add homepage
    url = ET.SubElement(urlset, 'url')
    ET.SubElement(url, 'loc').text = 'https://ash84.io/'
    ET.SubElement(url, 'lastmod').text = datetime.now().strftime('%Y-%m-%d')
    ET.SubElement(url, 'changefreq').text = 'weekly'
    ET.SubElement(url, 'priority').text = '1.0'

    urls_added = []

    # Find all index.html files in docs directory
    docs_path = Path('docs')

    if not docs_path.exists():
        print("❌ Error: docs directory not found. Please run 'make build' first.")
        return

    # Walk through all directories in docs
    for root, dirs, files in os.walk(docs_path):
        # Skip the root docs directory itself
        if root == 'docs':
            continue

        # Skip assets, css, js directories
        if any(skip in root for skip in ['assets', 'css', 'js', 'images']):
            continue

        if 'index.html' in files:
            # Convert path to URL
            # docs/2024/01/15/post-name/index.html -> /2024/01/15/post-name/
            relative_path = os.path.relpath(root, docs_path)
            url_path = '/' + relative_path.replace('\\', '/') + '/'

            # Get last modified time
            index_file = os.path.join(root, 'index.html')
            lastmod = get_last_modified(index_file)

            # Create URL entry
            url = ET.SubElement(urlset, 'url')
            ET.SubElement(url, 'loc').text = f'https://ash84.io{url_path}'
            ET.SubElement(url, 'lastmod').text = lastmod
            ET.SubElement(url, 'changefreq').text = 'monthly'
            ET.SubElement(url, 'priority').text = '0.8'

            urls_added.append(url_path)

    # Pretty print the XML
    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ")

    # Write to file
    sitemap_path = docs_path / 'sitemap.xml'
    tree.write(sitemap_path, encoding='utf-8', xml_declaration=True)

    # Print summary
    print(f"✅ sitemap.xml generated successfully!")
    print(f"📍 Location: {sitemap_path}")
    print(f"📊 Total URLs: {len(urls_added) + 1}")  # +1 for homepage
    print(f"🌐 Homepage + {len(urls_added)} blog posts")

    # Show first few URLs
    print("\n📝 Sample URLs:")
    print("   - https://ash84.io/")
    for url_path in sorted(urls_added, reverse=True)[:5]:
        print(f"   - https://ash84.io{url_path}")

    if len(urls_added) > 5:
        print(f"   ... and {len(urls_added) - 5} more")


if __name__ == '__main__':
    generate_sitemap()
