# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build Commands

```bash
make build    # Full build: zvc + tags + git meta + post index + sitemap + robots.txt + CNAME + ads.txt + pagefind
make clean    # Remove generated files in docs/
make run      # Build and serve locally at http://localhost:8000 (PORT=9000 make run)
make tags / git-meta / post-index / search   # Partial builds
make new NAME=post-name   # Create new post at contents/post-name/post-name.md
make format / lint / test # ruff format, ruff check, pytest (targets: scripts tests)
```

Package manager: `uv` (Python UV). All Python commands run via `uv run`. Node.js is required for `npx pagefind` (search index).

Tag normalization: `uv run python scripts/normalize_tags.py` (dry run) then `--apply`. Rewrites only the `tags:` section of each frontmatter.

## Architecture

This is a personal tech blog (ash84.io) built with **zvc** (custom static site generator, v0.1.8). Active theme: `ledger` (see `config.yaml`).

### Directory Structure

- `contents/` - Markdown source files, each in its own directory: `contents/{post-name}/{post-name}.md`
- `docs/` - Generated HTML (served by GitHub Pages). URL structure: `/YYYY/MM/DD/{post-name}/`. Never edit by hand; `zvc clean` wipes it. Also holds `meta/git.json`, `meta/posts.json`, `pagefind/`
- `themes/ledger/` - Active theme. Jinja2 templates (`index.html`, `post.html`, `tag.html`, `tags-index.html`), `partials/` (head-common, header, links, search), `assets/css/{base,style,post}.css`, `assets/js/{ledger,search}.js`
- `themes/chronicle/`, `themes/solopreneur/` - Previous themes, kept for rollback via `config.yaml`
- `scripts/` - Build utilities (tags, sitemap, robots.txt, git meta, post index, tag normalization)
- `tests/` - pytest for scripts (`tests/conftest.py` puts `scripts/` on `sys.path`)
- `plans/` - Plan documents (not `docs/`, which is build output)

### Build Pipeline

0. `build/asset-version.html` ← `git rev-parse --short HEAD` (gitignored). Templates append it as `?v=` to CSS/JS URLs so a deploy busts the 10-minute GitHub Pages cache
1. `zvc build` - Parses frontmatter, converts markdown to HTML with `themes/{theme}/post.html`, copies theme `assets/` to `docs/assets/`
2. `generate_tags.py` - Creates `/docs/tags/{tag}/index.html` pages (theme name read from `config.yaml`)
3. `generate_git_meta.py` - `git log -- contents/` → `docs/meta/git.json` (home changelog, per-post history)
4. `generate_post_index.py` - `docs/meta/posts.json` (newest first) for prev/next links
5. `generate_sitemap.py`, `generate_robots.py` - sitemap.xml, robots.txt
6. CNAME and ads.txt written for GitHub Pages
7. `npx pagefind --site docs` - static search index; only pages with `data-pagefind-body` (posts) are indexed

### Frontmatter Format

```yaml
---
title: 'Post Title'
author: 'ash84'
pub_date: '2026-01-10'
description: 'Post description for SEO and listings'
featured_image: 'image.jpg'  # optional
tags: ['dev', 'essay', 'cto']  # inline list only; zvc 0.1.8 cannot parse YAML block lists
---
```

The `pub_date` determines the output URL path (`/YYYY/MM/DD/post-name/`). `status: draft` excludes a post from the build.

### Template Variables

In `post.html`: `post` object with `title`, `html`, `created_at` (the pub_date; there is no `post.pub_date`), `description`, `featured_image`, `author`, `path` (`docs/YYYY/MM/DD/slug`); `tag_list` array; `settings`.
In `index.html`: `post_list` items have `title`, `link`, `pub_date`, `description`, `html_content`, `author` (no tags).
`generate_tags.py` renders `tag.html` with `tag_info{name,count}` + `posts`, and `tags-index.html` with `all_tags[{name,safe_name,count}]`. The `clean` filter exists only in zvc's environment; templates use Jinja builtins (`e`, `striptags`, `tojson`) instead.

Runtime (ledger.js): theme toggle (`t`, stored in localStorage as `theme`), search (`/`, ⌘K), TOC tree, reading stats, code block gutter/header, git meta and prev/next from `docs/meta/*.json`.

### Template Rules (ledger)

- Escape everything that comes from frontmatter with `| e` (title, description, tag names, image paths). Tag names once contained `&lt;b&gt;`; unescaped output turned the whole tags page bold.
- Asset links carry `?v={% include 'build/asset-version.html' %}`. Keep it on any new CSS/JS link.
- Shared markup lives in `themes/ledger/partials/` (head-common, header, links, search, theme-button). Include with the repo-root path, e.g. `{% include 'themes/ledger/partials/header.html' %}`. `{% set nav = 'writing' %}` before the header include marks the active `--flag`.
- Anything derived from git or neighbouring posts is not available to zvc: generate JSON in `scripts/` and render at runtime in `assets/js/ledger.js`. Sections stay `hidden` until data arrives.
- `generate_tags.py` renders tag templates with its own Jinja env: the `clean` filter is not there. Use Jinja builtins only.

### Verification

- `make lint && make test`, then `make build` and check `docs/` output with grep (year groups, `?v=`, `meta/*.json`, `pagefind/`).
- Headless Chrome enforces a minimum window width, so a 390px `--window-size` screenshot is cropped, not reflowed. Serve `docs/` locally and load pages in a same-origin iframe harness (`<iframe width=390>`) to check mobile, dark mode (`iframe.contentDocument.documentElement.dataset.theme = 'dark'` after `load`), and search (`contentWindow.ledgerSearch.open()`).
- Live check after push: `curl -sI https://ash84.io/assets/css/post.css` (`cache-control: max-age=600`), `gh run list` for Ruff Lint and pages build.

### Known Pitfalls

- `docs/` is build output and the Pages root. Plans go to `plans/`, never `docs/`.
- zvc passes `post.created_at`, not `post.pub_date`. `post_list` has no tags.
- YAML block-list tags are dropped by zvc. Keep `tags: ['a', 'b']`; `scripts/normalize_tags.py --apply` converts.
- The default `grep` is aliased to ugrep; for counting frontmatter fields, parse with Python instead.
- macOS filesystem is case-insensitive: `docs/tags/python` and `docs/tags/Python` collide locally only.
- Old posts (2007-2013) reference `http://ash84.net/...` images that no longer resolve. Content issue, not theme.

## Configuration

- `config.yaml` - Site settings (theme name, blog title/description/author, publication path)
- `pyproject.toml` - Python 3.12+, depends on `zvc==0.1.8`; dev group `pytest`, `ruff` (line-length 100)

## Deployment

Push to `main` branch triggers GitHub Pages deployment from `docs/` directory. Domain: ash84.io

---

## SEO Improvement Plan

### Current Status (2026-09-03)
- **Total posts**: 970 published
- **Implemented**: Google Analytics, AdSense, meta/OG/Twitter tags, JSON-LD BlogPosting, responsive design, code highlighting, sitemap.xml, tag pages, light/dark theme, pagefind search, prev/next links, per-post git history
- **Pending**: RSS feed, related posts, series feature

### Priority Tasks

**Phase 1 - Structured data**: done in `themes/ledger/post.html` (uses `post.created_at`).

**Phase 2 - RSS feed generation** (new script writing `docs/rss.xml` from frontmatter, like `generate_post_index.py`)

**Phase 3 - Related posts and series features** (tag-based; needs a build script since `post_list` has no tags)
