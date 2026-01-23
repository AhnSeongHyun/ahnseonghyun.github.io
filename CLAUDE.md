# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build Commands

```bash
make build    # Full build: zvc + tags + sitemap + robots.txt + CNAME + ads.txt
make clean    # Remove generated files in docs/
make run      # Build and serve locally at http://localhost:8000
make tags     # Generate tag pages only
make new NAME=post-name   # Create new post at contents/post-name/post-name.md
```

Package manager: `uv` (Python UV). All Python commands run via `uv run`.

## Architecture

This is a personal tech blog (ash84.io) built with **zvc** (custom static site generator, v0.1.5).

### Directory Structure

- `contents/` - Markdown source files, each in its own directory: `contents/{post-name}/{post-name}.md`
- `docs/` - Generated HTML (served by GitHub Pages). URL structure: `/YYYY/MM/DD/{post-name}/`
- `themes/solopreneur/` - Jinja2 templates (`index.html`, `post.html`, `tag.html`, `tags-index.html`, `footer.html`)
- `scripts/` - Build utilities (sitemap, tags, robots.txt generation)

### Build Pipeline

1. `zvc build` - Parses frontmatter, converts markdown to HTML using `themes/solopreneur/post.html`
2. `generate_tags.py` - Creates `/docs/tags/{tag}/index.html` pages
3. `generate_sitemap.py` - Creates `/docs/sitemap.xml`
4. `generate_robots.py` - Creates `/docs/robots.txt`
5. CNAME and ads.txt files written for GitHub Pages

### Frontmatter Format

```yaml
---
title: 'Post Title'
author: 'ash84'
pub_date: '2026-01-10'
description: 'Post description for SEO and listings'
featured_image: 'image.jpg'  # optional
tags: ['dev', 'essay', 'cto']
---
```

The `pub_date` determines the output URL path (`/YYYY/MM/DD/post-name/`).

### Template Variables

In `post.html`: `post` object with `title`, `author`, `pub_date`, `description`, `featured_image`, `path`, `content`; `tag_list` array; `settings` from config.yaml.

## Configuration

- `config.yaml` - Site settings (theme name, blog title/description/author, publication path)
- `pyproject.toml` - Python 3.12+, depends on `zvc==0.1.5`

## Deployment

Push to `main` branch triggers GitHub Pages deployment from `docs/` directory. Domain: ash84.io

---

## SEO Improvement Plan

### Current Status (2026-01-17)
- **Total posts**: 963
- **Implemented**: Google Analytics, AdSense, meta tags, OG tags, responsive design, code highlighting, sitemap.xml, tag pages
- **Pending**: Schema.org structured data, RSS feed, related posts, series feature

### Priority Tasks

**Phase 1 - Add structured data to `post.html`:**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{{ post.title }}",
  "description": "{{ post.description | clean }}",
  "author": { "@type": "Person", "name": "{{ post.author }}" },
  "datePublished": "{{ post.pub_date }}"
}
</script>
```

**Phase 2 - RSS feed generation** (requires new script and template)

**Phase 3 - Related posts and series features** (requires zvc modifications)
