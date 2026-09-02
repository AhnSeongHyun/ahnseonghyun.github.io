# Plan: Ledger 테마 구현 (시안 2 · 개발자 컷)
- date: 2026-09-02
- status: done
- author: claude
- approved-by: ash84 (2026-09-02)

> 문서 위치 메모: 전역 규칙은 `docs/plan-*.md`이지만 이 리포의 `docs/`는 zvc 빌드 산출물이자 GitHub Pages 배포 루트다(`make clean` = `zvc clean`이 docs/ 전체 삭제). 배포·삭제를 피하기 위해 `plans/`에 둔다.

## 1. 목적 및 배경

현재 테마 `chronicle`의 문제(2026-09-02 진단):
1. Pretendard를 로드하지만 `font-family`에 없음 → Space Grotesk + 시스템 폰트 혼용
2. 제목 자간 -2px, uppercase 트래킹, `word-break` 미설정 → 한글 단어 중간 줄바꿈
3. Experience/Selected 기본 접힘, 히어로 삭제 → 첫 화면에 정체성 없음
4. Latest가 971편 단일 리스트(날짜+제목만, 1400px 폭)
5. 검정 블록 인용, 2px 표 테두리, 인라인 코드 테두리 → 시각 소음
6. 다크 모드 없음
7. 검색 없음

선택안: 시안 2 **Ledger**(엔지니어의 장부) + 개발자 컷. 시안: https://claude.ai/code/artifact/ed82a8dd-302b-4dd9-8a0c-f49aef1dbcfc

사용자 결정(2026-09-02):
- 코드 패널: 라이트는 밝게, 다크는 어둡게
- changelog/history: 글 관련 커밋만 (`git log -- contents/`)
- 검색: pagefind 도입
- 상태바: 홈에도 유지
- 카피: 이름 제거. 소개는 "Payhere Head of Technology (전 CTO·공동창업자), 전 뱅크샐러드 테크리드. 개발 노트와 회고, 그리고 에세이와 삶."
- 외부 링크 6개 유지: GitHub, X, Instagram, LinkedIn, Gallery(leica.ash84.io), Playlist

## 2. 예상 임팩트

| 영역 | 변경 |
|---|---|
| `themes/ledger/` (신규) | index.html, post.html, tag.html, tags-index.html, assets/css/{style,post}.css, assets/js/{ledger,search}.js |
| `config.yaml` | `theme.name: chronicle` → `ledger` |
| `scripts/generate_git_meta.py` (신규) | `git log -- contents/` → `docs/meta/git.json` (changelog 3건 + slug별 history) |
| `scripts/generate_tags.py` | 테마 경로만 `themes/ledger/` 참조하도록 확인 |
| `Makefile` | build 끝에 `generate_git_meta.py`, `npx pagefind --site docs` 추가. `format`/`lint`/`test` 타겟 추가(전역 규칙) |
| `pyproject.toml` | dev 의존성 pytest, ruff |
| 성능 | 페이지 JS 약 60줄(TOC·words·테마 토글·git.json fetch). pagefind 초기 로드 약 수십 KB, 인덱스 chunk는 검색 시 지연 로드. 빌드 시간 +수 초 |
| SEO | URL 불변. 메타/OG/JSON-LD/GA/AdSense는 chronicle post.html에서 그대로 이식 |
| UX | 전면 변경(홈/글/태그). 다크 모드 신설 |

## 3. 구현 방법 비교

### A. git 메타 주입 방식
| 방법 | 장점 | 단점 |
|---|---|---|
| A1. 빌드 후 HTML 후처리(placeholder 치환) | JS 없이 정적 | zvc 출력 971개 파일 재작성. 느리고 깨지기 쉬움 |
| A2. zvc 컨텍스트 확장 | 가장 깔끔 | zvc는 외부 패키지(0.1.8). 포크 필요 |
| **A3. `docs/meta/git.json` 생성 + 런타임 fetch** | zvc 무수정. generate_tags.py와 같은 패턴. 실패 시 섹션 숨김 | JS 의존(장식 정보라 허용) |

**선택: A3.** zvc는 `post`, `tag_list`, `settings`만 넘기고 `post_list`에는 tags도 없다. 외부 데이터는 후처리 스크립트가 표준 패턴.

### B. 연도 그룹 헤더
| 방법 | 장점 | 단점 |
|---|---|---|
| **B1. 템플릿 `loop.changed(post.pub_date[:4])`** | 빌드 변경 없음. Jinja 표준 | 연도별 개수는 템플릿에서 못 셈 |
| B2. 스크립트가 연도 카운트 JSON | 정확 | 파일 하나 더 |

**선택: B1 + 개수는 런타임 JS로 DOM에서 셈.** 2023년 이전 연도는 `<details>`로 기본 접힘 → 971편 단일 리스트 문제 해소, 새 페이지 불필요.

### C. 검색
| 방법 | 장점 | 단점 |
|---|---|---|
| **C1. pagefind CLI (빌드 후 `docs/` 인덱싱)** | 서버 없음, 한국어 지원, self-hosted 번들 | Node/npx 필요 |
| C2. lunr.js + 직접 인덱스 | 순수 JS | 한국어 토크나이저 직접, 인덱스 크기 |

**선택: C1.** 사용자 결정.

## 4. 구현 단계

- [x] Step 1: `themes/ledger/` 생성. chronicle의 `<head>`(메타·OG·Twitter·JSON-LD·GA·AdSense·hljs) 이식 후 폰트를 IBM Plex Sans KR + IBM Plex Mono(Google Fonts)로 교체. Pretendard 링크 제거
- [x] Step 2: `assets/css/style.css`(홈·태그) 작성. 시안 `ledger2-css` 토큰 3상태(system/light/dark), `word-break: keep-all`, 상태바
- [x] Step 3: `assets/css/post.css` 작성. 밝은/어두운 코드 패널 토큰, `##`/`###` 표기, TOC 그리드, 프론트매터 블록, history
- [x] Step 4: `index.html`. `--flag` 내비, 소개(결정 카피), 장부 4칸(posts·since·commits·last write), changelog 슬롯, 외부 링크 6개, `--tag` 칩(→ `/tags/{tag}/`), `loop.changed` 연도 그룹, 2023 이전 `<details>` 접힘, 상태바
- [x] Step 5: `post.html`. 경로 브레드크럼(`post.path`에서 docs/ 제거·분해), 프론트매터 블록(title·author·pub_date·description·tag_list), 본문, TOC `<aside>`, history 슬롯, prev/next 없음(zvc 미제공 → 생략), 외부 링크, 상태바
- [x] Step 6: `assets/js/ledger.js`. TOC 트리(헤딩 2개 미만 숨김), words·read time, 연도 개수, `t` 키·버튼 테마 토글(localStorage 저장), `/`·`⌘K` → 검색 열기, `/meta/git.json` fetch → changelog/history 채움(실패 시 숨김)
- [x] Step 7: `scripts/generate_git_meta.py`. `git log --format=%h|%ad|%s --date=short -- contents/` 파싱, `--name-only`로 slug 매핑, `docs/meta/git.json` 출력. 함수 단위 분리(파싱/매핑/직렬화)
- [x] Step 8: pagefind. `Makefile build`에 `npx pagefind --site docs` 추가, `assets/js/search.js`에 모달 UI(`/pagefind/pagefind.js` 동적 import)
- [x] Step 9: `tag.html`, `tags-index.html`을 Ledger 스타일로. `generate_tags.py`의 테마 경로 확인
- [x] Step 10: `Makefile`에 `format`(ruff format), `lint`(ruff check), `test`(pytest) 타겟, `.PHONY`, `help` 기본 타겟. `pyproject.toml` dev 의존성
- [x] Step 11: `config.yaml` `theme.name: ledger`. `make build` → `make run`으로 로컬 확인(홈·글·태그·검색·다크·390px)
- [x] Step 12: 태그 잔재 정리는 별도 작업으로 분리(이 plan 범위 밖). 본 plan 완료 후 후속 plan (확인만, 작업 없음)

## 5. 테스트 계획

**단위 테스트** (`tests/test_generate_git_meta.py`):
- [x] 케이스 1: `git log` 한 줄 `해시|날짜|메시지` 파싱. 메시지에 `|` 포함 시에도 분리 정확
- [x] 케이스 2: `--name-only` 출력에서 `contents/{slug}/...` → slug 추출. contents 밖 파일은 무시
- [x] 케이스 3: slug별 history가 최신순, changelog는 상위 3건
- [x] 케이스 4: git 없는 환경(서브프로세스 실패) → 빈 JSON 쓰고 종료 코드 0(빌드 중단 금지)
- [x] 케이스 5: 출력 JSON 스키마 `{generated_at, changelog:[{hash,date,message}], posts:{slug:[...]}}`

**통합 테스트** (`make build` 후):
- [x] 시나리오 1: `docs/index.html`에 연도 헤더 `2026/`, 2023 이전 `<details>` 존재, 상태바 존재, 이름 문자열 미포함
- [x] 시나리오 2: `docs/2026/06/02/2026-self-proof/index.html`에 프론트매터 블록(title·pub_date·tags), 브레드크럼 `2026 / 06 / 02 / 2026-self-proof/`
- [x] 시나리오 3: `docs/2026/01/27/claude-mcp/index.html`에서 코드블록 줄번호·언어 라벨 렌더, TOC 3항목 이상
- [x] 시나리오 4: `docs/meta/git.json` 존재, `posts["2026-self-proof"]`에 커밋 2건(fa8eadd9, 80524475)
- [x] 시나리오 5: `docs/pagefind/pagefind.js` 존재. 로컬 서버에서 "자기증명" 검색 시 결과 1건 이상
- [x] 시나리오 6: `t` 키로 다크 전환 후 새로고침 시 유지. OS 다크 + 명시 라이트 선택 시 라이트 우선
- [x] 시나리오 7: 390px에서 가로 스크롤 없음, 코드블록만 내부 스크롤
- [x] 시나리오 8: `docs/sitemap.xml`, `robots.txt`, `CNAME`, `ads.txt` 기존과 동일하게 생성

## 6. 사이드 이펙트

- 기존 chronicle 테마: 디렉터리 유지. `config.yaml` 한 줄로 롤백 가능 → 해당 없음
- URL/permalink: 변경 없음 → 해당 없음
- 광고/GA: post.html에 동일 위치로 이식. 누락 시 수익 영향 → 이식 체크리스트로 대응
- 빌드 의존성: Node(npx) 추가. GitHub Pages는 docs/ 커밋 배포라 CI 변경 없음. 로컬 빌드 머신에 Node 필요 → README·Makefile help에 명시
- `zvc clean`이 `docs/meta/`, `docs/pagefind/`도 지움 → build 순서에 재생성 포함
- prev/next 링크: zvc가 인접 글 정보를 안 넘김 → 이번 범위에서 제외(시안과 차이). 필요 시 후속 plan(generate 스크립트로 JSON)
- 하위 호환성: 깨짐 없음. 마이그레이션 없음

## 7. 보안 검토

- OWASP: 정적 사이트, 서버 입력 없음. 검색은 클라이언트 측 pagefind. 검색어를 DOM에 넣을 때 `textContent` 사용(XSS 방지)
- git.json: 커밋 해시·날짜·메시지만 노출. 리포는 공개(GitHub Pages) → 신규 노출 정보 없음. 작성자 이메일은 포함하지 않음
- 외부 스크립트: Google Fonts, hljs CDN(기존), GA/AdSense(기존). pagefind는 빌드 산출물로 self-host → 신규 CDN 없음
- 인증/인가 변경: 없음. 민감 데이터: 없음. PCI-DSS: 해당 없음

## 8. 완료 기록 (2026-09-03)

- `make lint && make test` 통과 (ruff check 0건, pytest 7 passed)
- `make build` 성공: 970 posts, tags, `docs/meta/git.json`(98 commits · 972 slugs), sitemap 3,364 loc, pagefind 955 pages(6.1MB, chunk 지연 로드)
- 통합 시나리오 1~8 확인: 연도 그룹 20개(2023 이전 16개 `<details>` 접힘), 프론트매터 블록, 브레드크럼, 코드 5블록 줄번호·언어 라벨, TOC 8항목, history 2건(fa8eadd9·80524475), changelog 3건, commits 98, 390px 가로 스크롤 없음, 상태바 words/read time 채움
- 사이드 이펙트 항목: chronicle 유지 → 해당 없음 / URL 불변 → 해당 없음 / GA·AdSense·OG·JSON-LD 이식 완료 → 대응 완료 / Node 의존 → Makefile help·plan에 명시 / zvc clean 재생성 순서 → build에 포함 / prev·next 제외 → 후속 plan / 하위 호환 → 해당 없음

### plan 대비 차이
- `git log --follow` 대신 `git log -- contents/` 경로 필터 사용. `--follow`는 단일 경로 전용이라 972개 슬러그 일괄 처리 불가. 이동/개명 이력은 추적 안 됨.
- `make format`/`lint` 범위를 `scripts/generate_git_meta.py tests`로 한정. 기존 스크립트 11개는 ruff 미포맷 상태라 전체 적용 시 plan 외 파일 변경 발생. 후속 작업으로 분리.
- 설명문 필터: `clean`/`striptags` 대신 `e`(이스케이프). `<오디세이>`처럼 꺾쇠가 든 본문이 태그로 제거되던 chronicle 동작을 고침.
- 검색 결과 excerpt는 `<mark>`만 살리고 나머지 태그는 텍스트 노드로 재구성 (보안 검토 항목 준수).
- pagefind는 `data-pagefind-body`가 있는 글 페이지만 인덱싱. 홈·태그 페이지 제외.

### 알려진 제약 (zvc 0.1.8)
- 프론트매터 tags가 YAML 블록 리스트(`- 태그`) 형식이면 zvc가 파싱하지 못해 `tag_list`가 빔 → 프론트매터 블록에 tags 줄이 안 나옴 (예: 자기증명). 인라인 리스트 `['a', 'b']`로 쓰면 정상.
- `post_list`에 tags가 없어 홈 `--tag` 필터는 /tags/ 페이지 링크로만 동작.
- pagefind가 한국어 어간 추출을 지원하지 않음. 정확 어절 매칭.
