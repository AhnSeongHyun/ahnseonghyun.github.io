# Makefile for ash84.io static site

PORT ?= 8000
PYTHON_TARGETS ?= scripts tests

.PHONY: help build tags git-meta post-index search clean run new format lint test

help: ## 사용 가능한 타겟
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-10s %s\n", $$1, $$2}'

build: ## 전체 빌드: zvc + tags + git meta + post index + sitemap + robots + CNAME + ads.txt + pagefind
	uv run zvc build
	uv run python scripts/generate_tags.py
	uv run python scripts/generate_git_meta.py
	uv run python scripts/generate_post_index.py
	uv run python scripts/generate_sitemap.py
	uv run python scripts/generate_robots.py
	echo "ash84.io" > ./docs/CNAME
	echo "google.com, pub-8699046198561974, DIRECT, f08c47fec0942fa0" > ./docs/ads.txt
	npx -y pagefind --site docs

tags: ## 태그 페이지만 생성
	uv run python scripts/generate_tags.py

git-meta: ## docs/meta/git.json 생성
	uv run python scripts/generate_git_meta.py

post-index: ## docs/meta/posts.json 생성 (prev/next)
	uv run python scripts/generate_post_index.py

search: ## pagefind 검색 인덱스만 생성
	npx -y pagefind --site docs

clean: ## docs/ 산출물 정리
	uv run zvc clean

run: build ## 빌드 후 로컬 서버 (http://localhost:$(PORT))
	uv run python -m http.server $(PORT) --directory ./docs

format: ## 포맷팅 (ruff format)
	uv run ruff format $(PYTHON_TARGETS)

lint: format ## 정적 분석 (ruff check)
	uv run ruff check $(PYTHON_TARGETS)

test: ## 테스트 (pytest)
	uv run pytest -q

# Usage: make new NAME=2025-test
new: ## 새 글 디렉터리 생성 (NAME=slug)
	@if [ -z "$(NAME)" ]; then \
		echo "Error: NAME is required. Usage: make new NAME=2025-test"; \
		exit 1; \
	fi
	@mkdir -p contents/$(NAME)
	@touch contents/$(NAME)/$(NAME).md
	@echo "Created contents/$(NAME)/$(NAME).md"
