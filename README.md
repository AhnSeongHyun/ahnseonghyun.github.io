# ash84.io

개인 기술 블로그(ash84.io) 소스. 마크다운(`contents/`) → 정적 HTML(`docs/`) → GitHub Pages.

- 생성기: [zvc](https://pypi.org/project/zvc/) 0.1.8 (Python 3.12+, `uv`)
- 테마: `themes/ledger` (IBM Plex Sans KR · Mono, 라이트/다크, pagefind 검색)
- 2007년부터 970여 편

## 요구 사항

- Python 3.12+ 와 [uv](https://docs.astral.sh/uv/)
- Node.js (검색 인덱스 생성용 `npx pagefind`)

## 명령

```bash
make help        # 타겟 목록
make build       # zvc + tags + git meta + post index + sitemap + robots + CNAME + ads.txt + pagefind
make run         # 빌드 후 http://localhost:8000 (PORT=9000 make run)
make clean       # docs/ 정리
make new NAME=post-slug   # contents/post-slug/post-slug.md 생성
make format      # ruff format (scripts, tests)
make lint        # ruff check
make test        # pytest
```

부분 빌드: `make tags`, `make git-meta`, `make post-index`, `make search`.

## 글 작성

`contents/{slug}/{slug}.md`. 이미지는 같은 디렉터리에 두면 글 경로로 복사된다.

```markdown
---
title: '제목'
author: 'ash84'
pub_date: '2026-01-10'
description: '목록과 SEO에 쓰이는 한 줄 설명'
featured_image: 'cover.jpg'   # 선택
tags: ['dev', 'essay']         # 인라인 리스트만 인식 (YAML 블록 리스트 - 항목 은 zvc가 읽지 못함)
---
```

- `pub_date`가 URL이 된다: `/2026/01/10/{slug}/`
- `status: draft`면 빌드에서 제외
- 태그 정리: `uv run python scripts/normalize_tags.py` (dry-run) → `--apply`

## 디렉터리

```
contents/        글 원본 (slug 디렉터리별 md + 이미지)
themes/ledger/   현재 테마 (index/post/tag 템플릿, partials/, assets/css, assets/js)
themes/chronicle/, themes/solopreneur/   이전 테마 (config.yaml theme.name 으로 전환)
scripts/         빌드 후처리 (tags, sitemap, robots, git meta, post index, 태그 정규화)
tests/           pytest
plans/           작업 계획 문서
docs/            빌드 산출물 = GitHub Pages 루트 (직접 편집 금지)
```

## 배포

`main` 푸시 → GitHub Pages가 `docs/`를 서빙. 도메인 ash84.io.
