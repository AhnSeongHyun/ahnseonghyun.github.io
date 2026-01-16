#!/usr/bin/env python3
"""Generate sitemap.xml from built docs folder."""

import os
from datetime import datetime
from pathlib import Path

DOCS_DIR = Path("./docs")
BASE_URL = "https://ash84.io"
OUTPUT_FILE = DOCS_DIR / "sitemap.xml"


def get_lastmod(file_path: Path) -> str:
    """Get last modification date of a file."""
    mtime = os.path.getmtime(file_path)
    return datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")


def generate_sitemap():
    """Generate sitemap.xml from all index.html files in docs."""
    urls = []

    # Add homepage
    homepage = DOCS_DIR / "index.html"
    if homepage.exists():
        urls.append({
            "loc": BASE_URL + "/",
            "lastmod": get_lastmod(homepage),
            "priority": "1.0",
        })

    # Find all index.html files in subdirectories
    for index_file in sorted(DOCS_DIR.rglob("*/index.html")):
        rel_path = index_file.parent.relative_to(DOCS_DIR)

        # Skip assets folder
        if str(rel_path).startswith("assets"):
            continue

        url_path = str(rel_path).replace(os.sep, "/")
        urls.append({
            "loc": f"{BASE_URL}/{url_path}/",
            "lastmod": get_lastmod(index_file),
            "priority": "0.8",
        })

    # Generate XML
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]

    for url in urls:
        xml_lines.extend([
            "  <url>",
            f"    <loc>{url['loc']}</loc>",
            f"    <lastmod>{url['lastmod']}</lastmod>",
            f"    <priority>{url['priority']}</priority>",
            "  </url>",
        ])

    xml_lines.append("</urlset>")

    # Write sitemap
    OUTPUT_FILE.write_text("\n".join(xml_lines) + "\n", encoding="utf-8")
    print(f"Generated sitemap.xml with {len(urls)} URLs")


if __name__ == "__main__":
    generate_sitemap()
