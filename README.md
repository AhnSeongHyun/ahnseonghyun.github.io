# Markdown to HTML Converter (ZV)

정적 사이트 생성기 - 마크다운 파일을 HTML로 변환합니다.

## 기능

- 마크다운 파일에서 frontmatter 추출
- frontmatter의 날짜를 사용하여 디렉토리 구조 생성
- 마크다운 콘텐츠를 HTML로 변환
- Typer를 사용한 명령줄 인터페이스

## 설치

1. Python 3.12+ 설치 확인
2. 패키지 설치:

```bash
# 개발 모드로 설치
make install
# 또는
pip install -e .
```

## 사용 방법

이 도구는 다음과 같은 명령어를 제공합니다:

### 정리 (Clean)

`public` 디렉토리를 정리합니다:

```bash
make clean
# 또는
zv clean
```

### 빌드 (Build)

`contents` 디렉토리의 모든 마크다운 파일을 HTML로 변환하여 `public` 디렉토리에 저장합니다:

```bash
make build
# 또는
zv build
```

### 개발 서버 (Dev)

사이트를 빌드하고 로컬 개발 서버를 시작합니다:

```bash
make dev
```

## 마크다운 파일 형식

이 도구는 다음과 같은 형식의 frontmatter가 있는 마크다운 파일을 기대합니다:

```markdown
---
title: '제목'
author: '작성자'
date: '2023-01-01'
description: "설명"
---

마크다운 내용...
```

frontmatter의 날짜는 출력 디렉토리 구조에 사용됩니다.

## 출력 구조

`contents/folder/example.md` 파일에 frontmatter에 `date: '2023-01-01'`이 있다면, 출력은 다음과 같습니다:

```
public/2023-01-01/folder/index.html
```
