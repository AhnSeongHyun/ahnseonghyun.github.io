# Ledger theme

ash84.io의 현재 테마. "엔지니어의 장부": 개발 노트·회고·에세이를 한 리스트에, 개발자스러움은 장식이 아니라 실제 구조(프론트매터·git·URL·마크다운 레벨)를 드러내는 방식으로.

## 파일

```
index.html          홈: 소개 · 장부(posts/since/commits/last write) · changelog · --tag 칩 · 연도 그룹
post.html           글: 브레드크럼 · 제목 · 날짜+#태그 · 본문 · history · prev/next · 외부 링크 · TOC
tag.html            /tags/{tag}/  (generate_tags.py가 렌더)
tags-index.html     /tags/        (generate_tags.py가 렌더)
partials/
  head-common.html  meta · Google Fonts(IBM Plex Sans KR, Plex Mono) · 테마 초기화 스크립트 · GA · base.css
  header.html       ash84.io · --writing --tags --about · 검색 버튼   ({% set nav %}로 활성 표시)
  links.html        github · x · instagram · linkedin · gallery · playlist
  search.html       검색 오버레이 마크업 + ledger.js/search.js 로드
  theme-button.html 상태바 해/달 토글 (kbd t)
assets/css/
  base.css          토큰(3상태) · 리셋 · 헤더 · 브레드크럼 · 링크 · 커밋 리스트 · 상태바 · 검색 오버레이
  style.css         홈·태그 페이지 (장부, 필터, 연도 그룹, 행)
  post.css          글 (본문 타이포, 코드블록, hljs 토큰 3색, TOC, history, prev/next)
assets/js/
  ledger.js         테마 토글 · 단축키 · 연도 카운트 · TOC · words/read time · 코드블록 장식 · git.json/posts.json 로드
  search.js         pagefind 검색 오버레이 (window.ledgerSearch.open/close)
```

## 디자인 토큰

`base.css`의 `:root`가 라이트 전체 팔레트를 정의하고, `@media (prefers-color-scheme: dark)`의 `:root:not([data-theme="light"])`와 `:root[data-theme="dark"]`가 같은 토큰을 다크로 재정의한다. 컴포넌트는 토큰만 참조한다.

| 토큰 | 라이트 | 다크 | 용도 |
|---|---|---|---|
| `--bg` / `--ink` | #FFFFFF / #16181C | #0E1013 / #E6E8EB | 바탕 / 본문 |
| `--muted` / `--line` | #6C717A / #E3E5E8 | #8C929C / #23272E | 보조 텍스트 / 구분선 |
| `--surface` | #F6F7F9 | #14171B | 상태바, 인라인 코드, TOC 박스 |
| `--hl` | #FFE566 | #8A7A1E | 형광펜(링크 hover, 강조) |
| `--code-bg` 등 | 밝은 패널 | 어두운 패널 | 코드블록 |
| `--tok-a/b/c` | 파랑 / 갈색 / 빨강 | 밝게 | hljs: 키워드·문자열·변수 |

타이포: 본문 IBM Plex Sans KR 17.5px / 1.8, 폭 680px, `word-break: keep-all`. 메타·날짜·경로는 IBM Plex Mono.

## 런타임 계약

| 파일 | 스키마 | 사용 |
|---|---|---|
| `/meta/git.json` | `{generated_at, total_commits, changelog:[{hash,date,message}], posts:{slug:[{hash,date,message}]}}` | 홈 `[data-commits]`, `[data-changelog]`; 글 `article[data-slug]` → `[data-history]` |
| `/meta/posts.json` | `[[slug, title, link, pub_date], …]` 최신순 | 글 `[data-pn]` prev/next (newer = index-1, older = index+1) |
| `/pagefind/pagefind.js` | pagefind 1.x | `search.js`가 dynamic import, excerpt는 `<mark>`만 유지해 텍스트 노드로 재구성 |

데이터가 없거나 fetch가 실패하면 해당 섹션은 `hidden` 유지. 페이지는 JS 없이도 읽힌다.

## 단축키

`t` 테마 · `/` 또는 `⌘K` 검색 · 검색 안에서 `↑↓` 이동, `↵` 열기, `esc` 닫기.

## 수정 가이드

- 새 CSS/JS 링크는 `?v={% include 'build/asset-version.html' %}`를 붙인다 (Pages 10분 캐시 무효화).
- 프론트매터에서 온 값은 항상 `| e`.
- 새 페이지 템플릿은 `head-common` → 페이지 CSS → `header` → 본문 → 상태바 → `search` 순서.
- 상태바 왼쪽은 "경로처럼 읽히는" 문자열(`~/contents · 970 posts`, `contents/{slug}/{slug}.md`). 오른쪽은 검색·테마 버튼.
- 로컬 확인: `make run` 후 http://localhost:8000. 모바일·다크는 same-origin iframe 하네스로 (CLAUDE.md Verification 참고).
