# Plan: Ledger 후속 4건 (태그 정규화 · prev/next · 스크립트 포맷 · 진단 정정)
- date: 2026-09-03
- status: done
- author: claude
- approved-by: ash84 ("계속 진행", 2026-09-03 — 직전 메시지의 후속 후보 4건에 대한 진행 지시로 해석)

## 1. 목적 및 배경

Ledger 테마 구현(plan-ledger-theme-2026-09-02) 후 남긴 후속 후보와, 재측정으로 드러난 진단 오류 정정.

재측정 결과(contents/ 971편 프론트매터 직접 파싱):
- 태그 2,482개 중 2,090개가 1회 사용, 5회 이상은 74개
- `python` 40 vs `Python` 112 등 대소문자 중복. consolidate_tags.py 룰에 있으나 미적용 파일 존재
- 빈 태그 `''` 42건, 해시태그 문자열 3건(`'#ash84 #회고 #2023 #essay'`, `'#crumbs'`, `'#fxdevconkr'`), HTML 엔티티 6건(`&amp;` 4, `&lt;…&gt;` 2)
- YAML 블록 리스트(`- tag`) 29건 → zvc 0.1.8이 파싱 못 해 `tag_list` 빔. 2021–2026 에세이 대부분이 여기 해당
- **정정**: 이전 진단의 "'랩' 977 · '폰트 뷰' 254 · '가상 키 입력' 63"은 측정 오류(ugrep 파이프). 실제 각 1건. 시안 아티팩트·메모리 문구 수정

## 2. 예상 임팩트

| 영역 | 변경 |
|---|---|
| `contents/*/*.md` 프론트매터 tags 줄 | 블록→인라인 29건, 해시태그 분리 3건, 빈 태그 제거, `&amp;` 디코드, consolidate 룰 적용. 본문·다른 필드 불변 |
| `scripts/normalize_tags.py` (신규) | dry-run 기본, `--apply`로 기록. 백업 파일 만들지 않음(contents/ 안 *_bak.md는 글로 빌드되므로). 되돌리기는 git |
| `scripts/generate_post_index.py` (신규) | `docs/meta/posts.json` = `[[slug, title, link, pub_date], …]` 최신순. draft 제외 |
| `themes/ledger/post.html`, `assets/js/ledger.js`, `assets/css/post.css` | prev/next 내비(런타임, posts.json 1회 fetch 후 브라우저 캐시) |
| `Makefile` | build에 post-index 단계, `PYTHON_TARGETS`를 `scripts tests`로 확대 |
| `scripts/*.py` 기존 9개 | `ruff format` 포맷팅만. 로직 변경 없음(`ruff check`는 이미 통과) |
| 태그 페이지 | 인라인화로 최근 글 태그가 /tags/에 노출. 태그 수 소폭 감소 |
| 성능 | posts.json 약 70KB(gzip 후 약 20KB), 글 페이지 최초 1회 로드 |

## 3. 구현 방법 비교

### A. 태그 정규화 도구
| 방법 | 장점 | 단점 |
|---|---|---|
| A1. consolidate_tags.py 재실행 | 기존 도구 | 인라인 리스트만 파싱. 블록 리스트·해시태그·엔티티 미처리 |
| A2. improve_frontmatter.py 확장 | yaml 라이브러리 | 전체 프론트매터를 yaml로 재직렬화 → 따옴표·순서·description 줄바꿈이 대량 변경. *_bak.md 생성 |
| **A3. 신규 normalize_tags.py, tags 구간만 치환 + consolidate 룰 import** | 변경 최소(tags 줄만), 룰 재사용, dry-run | 스크립트 하나 추가 |

**선택: A3.**

### B. prev/next 데이터
| 방법 | 장점 | 단점 |
|---|---|---|
| B1. 글별 JSON 970개 | 페이지당 200B | docs/ 파일 970개 추가 |
| **B2. posts.json 하나 + 런타임 탐색** | 파일 1개, 브라우저 캐시로 재사용 | 최초 70KB |
| B3. zvc 컨텍스트 | 정적 | zvc 수정 필요 |

**선택: B2.**

## 4. 구현 단계

- [x] Step 1: `scripts/normalize_tags.py` (parse → normalize → format, dry-run/--apply) + `tests/test_normalize_tags.py`
- [x] Step 2: dry-run으로 변경 목록 확인 후 `--apply`. `git diff --stat contents` 로 tags 줄만 바뀌었는지 확인
- [x] Step 3: `scripts/generate_post_index.py` + `tests/test_generate_post_index.py`
- [x] Step 4: post.html에 `[data-pn]` 내비, ledger.js에 posts.json 로더, post.css `.pn`
- [x] Step 5: Makefile build에 `generate_post_index.py`, `post-index` 타겟, `PYTHON_TARGETS ?= scripts tests`
- [x] Step 6: `uv run ruff format scripts` (포맷팅만), `make lint && make test`
- [x] Step 7: 시안 아티팩트(5종) 진단 07 문구 정정·재게시, 메모리 정정
- [x] Step 8: `make build` → 통합 확인 → plan status done

## 5. 테스트 계획

**단위 테스트**
- [x] normalize: 블록 리스트 → 인라인, 나머지 프론트매터·본문 바이트 동일
- [x] normalize: `'#ash84 #회고 #2023 #essay'` → 4개 태그로 분리, 기존 `retrospective` 유지
- [x] normalize: 빈 태그 제거, `&amp;` → `&`
- [x] normalize: `python` → `Python` (consolidate 룰), 중복 제거
- [x] normalize: 변경 없는 파일은 None(멱등)
- [x] post index: pub_date 내림차순, draft 제외, link = /YYYY/MM/DD/slug/, 따옴표 제거된 title
- [x] post index: 프론트매터 없는 파일 무시

**통합 테스트**
- [x] `git diff --stat contents` 변경 파일 수 = dry-run 보고 수, 변경 줄이 tags 구간만
- [x] `make build` 후 `docs/2026/06/02/2026-self-proof/index.html` 프론트매터 블록에 tags 줄 존재, `/tags/자기증명/` 생성
- [x] `docs/meta/posts.json` 길이 = 빌드된 글 수(970), 첫 항목 2026-08-08
- [x] 글 페이지 DOM: prev/next 링크 2개 렌더(최신 글은 next 없음)
- [x] `make lint && make test` 통과

## 6. 사이드 이펙트

- 태그 URL 변화: 정규화된 태그(예 `python`→`Python`)의 기존 `/tags/python/` 경로 소멸. 검색엔진 인덱스 영향 미미(태그 페이지는 noindex 아님이나 트래픽 낮음) → 대응: 기존 consolidation 4회와 동일한 성격, 허용
- 프론트매터 따옴표 스타일: 인라인화 시 `'tag'` 단일 인용 통일. `'` 포함 태그는 `"tag"`
- posts.json은 `zvc clean`으로 삭제 → build 순서에 포함
- 하위 호환: 없음. 마이그레이션: 없음

## 7. 보안 검토

- 정적 파일 생성만. 사용자 입력 없음
- posts.json 렌더는 `textContent`, href는 posts.json의 link(빌드 산출물)만 사용
- OWASP/인증/민감 데이터/PCI-DSS: 해당 없음

## 8. 완료 기록 (2026-09-03)

- normalize_tags `--apply`: 114파일, 삭제 204줄·추가 114줄, tags 구간 외 변경 0줄(`git diff -U0` 검증)
- `make lint && make test`: ruff check 통과(scripts 전체 + tests), pytest 18 passed
- `make build` 성공. posts.json 970건(첫 항목 movie-odyssey 2026-08-08). 자기증명 프론트매터에 tags 줄 렌더, `/tags/자기증명/`·`/tags/커리어/` 생성. 태그 디렉터리 2,462개
- prev/next DOM: 자기증명 → older "AI와 함께 변한 삶" / newer "요즘 관심사 - AI Native Company". 최신 글(오디세이)은 newer 숨김
- 사이드 이펙트: 태그 URL 변경(`python`→`Python` 등) 허용 / 따옴표 통일 적용 / posts.json build 포함 → 대응 완료
- 아티팩트(시안 5종) 진단 07 문구 정정·재게시, 메모리 정정

### 메모
- 테스트 기대값 1건 수정: `'#ash84 #회고 …'` 분리 후 `회고`가 consolidate 룰로 `retrospective`에 병합되어 4개가 됨(룰 준수, 의도된 동작)
- `tags:` 값이 비어 있고 항목도 없는 파일 1건은 그대로 둠(태그 없음과 동일)
- macOS 케이스 무시 파일시스템 때문에 로컬 `docs/tags/python`은 `Python` 디렉터리와 동일. GitHub Pages(Linux)에서는 `Python`만 존재

## 9. 배포 후 핫픽스 (2026-09-03, 라이브 피드백)

| 증상 | 원인 | 조치 | 커밋 |
|---|---|---|---|
| /tags/ 중간부터 전체 볼드 | 태그 `&lt;b&gt;태그`가 정규화의 `html.unescape`로 `<b>태그`가 되어 미이스케이프 출력 | 템플릿 태그명·제목 `e` 필터, 정규화에서 `<` `>` 제거(`b태그`, `hr`), 빈 태그 `['']` 37편 → `[]`, generate_tags 빈 태그 무시 | 41c7be52 |
| 긴 슬러그에서 HISTORY 라벨 글자 단위 꺾임 | `.cl-h` flex 자식에 `overflow-wrap: anywhere` 적용 | `.cl-h { white-space: nowrap }`, span `min-width: 0` | 41c7be52 |
| 상태바 `t theme` → 해/달 아이콘 + 단축키 요청 | — | `partials/theme-button.html` SVG 2종, `data-mode`를 JS가 동기화(토글·OS 변경) | 38165079 |
| 프론트매터 블록 노출 원치 않음 | — | 블록 제거, 제목 아래 `날짜 · #태그` 한 줄(`.post-meta`) | 845a3e18 |
| CI Ruff Lint 실패 63건 | CI가 최신 ruff(0.16.5) 설치, 기본 룰셋 확대(I/UP/BLE/S…) | `[tool.ruff.lint] select = E F W I UP B SIM`, `--fix`(+unsafe: B007·SIM118) 적용, 워크플로 Python 3.12 + `ruff format --check` + pytest. 통과 확인 | 09ee0cc5 |

검증: 라이브 /tags/ `<b>` 0건, 검색 "자기증명" 결과 하이라이트 동작, 다크 모드 3페이지 정상, 390px 가로 스크롤 없음, 죽은 이미지 호스트(ash84.net) 글은 원본 콘텐츠 문제로 범위 외.
