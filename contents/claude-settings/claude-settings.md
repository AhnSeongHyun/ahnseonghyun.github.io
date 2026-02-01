---
title: 'claude code setup'
author: 'ash84'
pub_date: '2026-02-01'
description: '클로드 세팅'
featured_image: ''
tags: ['claude', 'claude code']
---

클로드 코드(claude code)를 들인지 이제 딱 한달이 지났다. 작업하는 방식 자체도 많이 변했고 이제는 거의 모든 코드 및 자동화 작업을 클로드 코드 통해서 진행을 하고 있다. 최근에 고민했던 부분은 회사에서도 쓰고 개인적으로도 쓰는데 이것을 어떻게 잘 유지를 할지에 대한 부분이었다. 정리를 해보면 

- 2개의 물리적 환경 
    - 회사와 집 
    - 2개의 맥(mac)에서 사용 

- 2개의 논리적 환경 
    - 회사 프로젝트 
    - 개인 프로젝트 


결국 내가 원하는건 2개의 물리적으로 독립된 맥에서 2개의 환경이 잘 쓰이길 원했다. 처음에는 회사 컴퓨터에서만 주로 작업을 하다보니 회사에 관련된 환경만 셋업을 했었는데 집에서도 작업을 할 경우가 있다보니 그것들을 가져올 필요가 있었다. 그리고 2개의 논리적 환경이 공통화된 영역도 있고 다른 영역도 있다. 예르들면, 문서화하는 부분 README.md, CLAUDE.md를 작업후에 정리하는건 똑같은 루틴이지만, git 브랜치 전략이나 세부적인 작업 영역은 다르다. 개인 프로젝트에서는 main 브랜치 위주로 작업하고 커밋하지만 회사에서는 feature-pr 방식으로 일을 한다. 

그래서 지금 마련한 방식은 github에 claude라는 repository를 만들고 거기에 각 workspace/작업영역에 해당하는 관련 설정이나 commands를 넣어두고 그것을 
내려받아서 make sync(delete - copy)를 시키는 방식이다. 

전체적인 구조를 보면 다음과 같다. 

```shell
├── Makefile
├── README.md
├── global
│   ├── CLADUE.md
│   ├── scripts
│   │   └── context-bar.sh
│   └── settings.json
├── personal
│   ├── CLAUDE.md
│   ├── commands
│   │   ├── git-sync.md
│   │   ├── lint-format.md
│   │   └── update-docs.md
│   └── rules
│       └── flutter-project-checklist.md
└── company 
    ├── CLAUDE.md
    └── commands
        └── lint-format.md
```                                 

보통 나는 `~/workspace/personal`, `~/workspace/company` 이렇게 두고 그 하위에 각 영역에 맞는 프로젝트들을 배치를 한다. 그래서 .claude도 
`~/workspace/personal/.claude`, `~/workspace/company/.claude` 이렇게 위치가 된다. 

make sync를 하면 global에 있는 부분은 `~/.claude` 안으로 복사가 되고 나머지는 각 프로젝트로 복사가 되어진다. 

global에 있는 `settings.json`에는 명령어 allow 항목들이 있어서 그것들은 전역적으로 영향을 미친다. 
각 영역에 있는 CLAUDE.md 파일에는 개인과 회사 작업에 있어서 기본적인 지침들이 들어있다. 물론 각 프로젝트의 CLAUDE.md도 만들게 된다. 

commands의 경우, 상위 디렉토리에 있는것을 찾지 못하는 문제가 있어서 아쉽지만 그래서 프로젝트를 만들고 .claude를 구성하면 ln -s로 commnands 를 수동으로 세팅을하면 하위 프로젝트에서도 custom commands를 모두 사용할 수 있다. 

지금 이 세팅이 완벽하진 않지만, 현재의 내 환경에는 맞는것 같고 좀 더 작업을 해보면서 업데이트를 할 예정이다. 
