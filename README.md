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

## 테마 기능 (ledger)

| 기능 | 동작 |
|---|---|
| 테마 | 시스템 설정 따름. `t` 키 또는 상태바 해/달 버튼으로 전환, `localStorage.theme`에 저장 |
| 검색 | `/` 또는 `⌘K`. pagefind 정적 인덱스(글 본문만). 한국어 어간 추출 없음 → 어절 단위 매칭 |
| 글 페이지 | `##`/`###` 마크다운 레벨 표기, `tree`형 목차(헤딩 2개 이상일 때), 코드 줄번호·언어 라벨·copy, words·읽기 시간 상태바 |
| 이력 | 홈 changelog(`git log -3 -- contents/`), 글 하단 history(해당 글 커밋). 클릭 시 GitHub 커밋 |
| 이전/다음 | `docs/meta/posts.json` 기준. 최신 글은 newer 숨김 |
| 홈 | 연도 그룹, 2023 이전은 접힘. `--tag` 칩은 `/tags/{tag}/` 링크 |

## 빌드 산출물 (docs/ 안)

| 경로 | 생성 | 용도 |
|---|---|---|
| `assets/` | zvc (`themes/ledger/assets` 복사) | CSS·JS. HTML에서 `?v=<git hash>`로 참조 |
| `tags/{tag}/` | `generate_tags.py` | 태그별 목록 |
| `meta/git.json` | `generate_git_meta.py` | `{generated_at, total_commits, changelog[], posts{slug:[commits]}}` |
| `meta/posts.json` | `generate_post_index.py` | `[[slug, title, link, pub_date], …]` 최신순 |
| `pagefind/` | `npx pagefind --site docs` | 검색 인덱스 (약 6MB, 청크 지연 로드) |
| `sitemap.xml`, `robots.txt`, `CNAME`, `ads.txt` | 스크립트·Makefile | SEO·Pages |

## 트러블슈팅

- **배포 직후 스타일이 어긋남**: Pages가 에셋을 10분 캐시. 에셋 URL에 빌드 해시가 붙으므로 새 HTML이 내려오면 해결. 강력 새로고침(⌘⇧R)
- **태그가 안 나옴**: 프론트매터 `tags`가 YAML 블록 리스트(`- 태그`)면 zvc가 못 읽음. `make lint` 전 `uv run python scripts/normalize_tags.py --apply`
- **검색이 "인덱스 없음"**: `make build`(또는 `make search`)를 안 돌린 상태. Node.js 필요
- **`make build`에서 pagefind 실패**: `npx -y pagefind --version` 확인. 네트워크 필요
- **로컬 `docs/tags/python`과 `Python`이 같은 폴더**: macOS 케이스 무시 파일시스템. Pages(Linux)에서는 `Python`만 존재
- **CI Ruff 실패**: 룰은 `pyproject.toml [tool.ruff.lint]`에 고정. 로컬 `make lint`와 동일 결과여야 함

## 디렉터리

```
contents/        글 원본 (slug 디렉터리별 md + 이미지)
themes/ledger/   현재 테마 (README 참고: 템플릿, partials/, assets/css, assets/js)
themes/chronicle/, themes/solopreneur/   이전 테마 (config.yaml theme.name 으로 전환)
scripts/         빌드 후처리 (tags, sitemap, robots, git meta, post index, 태그 정규화)
tests/           pytest
plans/           작업 계획 문서
docs/            빌드 산출물 = GitHub Pages 루트 (직접 편집 금지)
```

## 배포

`main` 푸시 → GitHub Pages가 `docs/`를 서빙. 도메인 ash84.io.
