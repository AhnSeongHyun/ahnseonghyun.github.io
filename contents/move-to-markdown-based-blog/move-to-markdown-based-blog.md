---
title: 'More Humane Medical Experience'
author: 'ash84'
pub_date: '2025-07-08'
description: '지속가능한 블로그'
featured_image: ''
tags: ['blog', 'markdown', 'static generator']
---

몇일 전에 Notion API를 이용해서 회사 블로그에 글을 쓸 연동하는 얘기가 나와서 찾아보다가, 개인 블로그를 개편하고 싶은 생각이 들었다. 그동안 나는 개인적으로 meier라는 backend는 flask, frontend는 TOAST UI를 이용해서 admin/backoffice를 만들어서 블로그 글을 써왔다. 그렇지만 아쉬웠던 것은 처음 만든 이후에 노션과 옵시디언이 나오면서 더 이상 글을 admin에서 쓰지 않고 노션에서 쓰고 markdown 파일을 다운로드 받아서 그 텍스트를 다시 admin에 옮겨서 저장하는 식으로 작업을 해왔다. 물론 admin에는 draft, private 같은 기능들이 있었다. 이건 wordpress, tistory, ghost 등의 블로그 플랫폼에 있는 기능들을 구현한 것이었다. 그렇지만 노션이나 옵시디언 자체가 별도의 CMS이자 글쓰기 도구로 쓰고 있는 상황에서 이걸 유지해야 하는가에 대한 생각이 들었다.

## 지속가능성에 대한 고민

또 다른 생각은 지속 가능한가? 라는 관점에서의 고민이 있었다. 개발자를 그만두더라도, 다른 일을 하더라도 블로그는 계속할 것 같은데, 물론 블로그를 운영하는 게 개발적으로 어려운 일은 아니지만 AWS Lightsail도 귀찮고 언젠가 내가 돈을 못 내면 서버가 내려가고 내 글이 인터넷상에서 사라지지 않을까? 상대적으로 GitHub 그리고 markdown 파일이 더 오래 살아남지 않을까 하는 생각이 들었다. 만약 GitHub가 대체되더라도 markdown 파일은 나에게 남을 테니. 그런 고민들을 하다가 결국 markdown 기반으로 돌아서기로 했다.

## tool

Astro를 회사 개발 블로그를 만들어서 이번에도 Astro를 먼저 선택했다. 하지만 아쉬운 부분이 theme 시스템이었다. 대부분의 블로그 툴들은 theme를 쉽게 갈아낄 수 있다. 그런데 Astro는 사이트를 만드는 개념이다 보니 theme를 다운로드받아서 사용하는 방식이 아니었다. 예전에 회사 개발 블로그는 https://github.com/danielcgilibert/blog-template 이걸로 만들었었다. 나는 theme를 직접 만들어 쓰는 편이라 theme를 쉽게 갈아끼는 시스템은 필요했다.


## develop


### 구조

직접 만들기로 결심했다. 정확히 시작은 금요일 밤이었고, 토요일까지 이어졌다. 풀타임은 아니었고 어차피 운영하던 것이 있으니까 못 만들어도 상관없다는 주의였다. 구조를 설명하면 다음과 같다.

	- contents 디렉터리 하위에 url path에 해당되는 디렉터리가 있다. 개별 디렉터리가 하나의 포스트(post)의 공간이다. 예를 들어 이 글은 contents/move-to-markdown-based-blog에 위치해 있다. 글마다 디렉터리를 만든 이유는 이미지나 다른 여타의 해당 글에 들어가는 파일들이 다른 디렉터리로 흩어지는 것을 막고 싶었다. 대부분 이미지겠지만.
	- 해당 디렉터리 하위에는 해당 디렉터리와 같은 이름의 .md 파일이 있다. 여기에 본문을 쓴다.
	- .md 파일의 최상단에는 아래와 같은 meta 정보를 담는다. 이건 다른 여타의 static generator가 사용하는 방식이고, Astro에서 경험한 부분을 넣었다.

        ```txt
        ---
        title: '지속가능한 블로그를 만들기 위한 노력'
        author: 'ash84'
        pub_date: '2025-07-08'
        description: '마크다운 기반의 블로그 만들기'
        featured_image: ''
        tags: ['blog', 'markdown', 'static generator']
        ---
        ```

이 정도의 구조를 가지고 있다. 정리해 보니 처음 어떻게 만들지에 대해서 고민했던 것보다 별건 없었다. static generator를 만들어야 하는데 제일 편한 python으로 작업을 했다. uv, typer 등을 사용해서 contents 디렉터리 내 .md 파일을 읽고 html로 변환하는 작업을 진행했다. 여기서 고민했던 것은 어떤 url path를 지정할 것인가? 였다. 예를 들어 실제 접속하는 url path가 /move-to-markdown-based-blog가 될 수도 있지만 /2025/07/08/move-to-markdown-based-blog가 되게 할 수도 있다. 이 부분에서 많이 고민을 했는데 완전 글쓴이가 지정한 대로 갈 것인가? 아니면 규칙을 만들 것인가?에 대한 찰나의 고민이 있었고, 날짜를 넣는 방식을 선택했다. 이유는 날짜별로 나중에 다른 부분에서 보여줄 때 더 나을 것 같았다.

### theme

결국 theme 때문에 이 모든 게 시작이 되었다. 사실 python을 선택한 건 2가지 이유가 있었는데 첫 번째는 내가 제일 편하고 빠르게 코딩할 수 있어서, 두 번째는 기존 내 블로그가 jinja2 template를 기반으로 되어 있기 때문이었다. 그래서 markdown 기반 정적 블로그를 만들되 기존의 내가 쓰고 있던 jinja2 template 기반의 theme를 가져와서 쓰면 좋겠다는 생각이 들었다. 결국 내가 원하는 건 theme를 만들어서 배치시키고 여러 테마 중에 하나를 선택하기를 원하는 것이다. 그러기 위해서 themes 디렉터리 하위에 사용하려는 테마 디렉터리를 배치하는 방식을 선택했다. themes 디렉터리 하위에 여러 테마가 있다고 하면 결국 사용자는 어떤 것을 현재 사용할지를 선택해야 하는데 그것을 위해서 config.yaml을 만들었다.


```yaml
theme: 
  name: solopreneur
blog: 
  title: Ash84
  description: Ash84 Blog 
publication:
  path: ./docs
```

위의 config.yaml을 기준으로 설명하면 해당 파일을 읽어서 themes 하위에 solopreneur라는 테마를 가져와서 읽어와서 사용한다.



### 변환 

config.yaml의 publication 디렉터리에 변환된 html 파일들이 들어간다. 최상단에 index.html이 들어간다. 이 부분이 블로그에 들어가면 보는 첫 화면에 해당한다.
그다음에는 yyyy/mm/dd/xxx/index.html 이렇게 생성을 한다. 그렇게 되면 앞서서 말한 것과 같이 년/월/일/title url path로 접속할 수 있게 된다.



### 마이그레이션 

기존의 MySQL에 있던 약 1000건의 데이터를 가져와서 contents 디렉터리 하위에 markdown 파일로 넣으면서 동시에 파일 내 상단의 meta 정보를 넣어서 생성하는 작업을 진행했다. 이 부분은 사실 기존 DB에 개별 컬럼으로 모두 나누어져 있었고 DDL을 cursor에 주고 바로 시켜서 쉽게 작업할 수 있었다.



### 이사가기 

주말이 지나고 월요일 밤에 이사를 시작했다. 기존 AWS Lightsail에 있었던 DNS Zone을 지우고 Route53에서 A Record 그리고 네임서버들을 설치했다. 기존에 운영되고 있어서 DNS 적용에 계속 시간이 흘렀고, GitHub Page에서 Domain 활성화가 잘 안 되었다. ChatGPT의 도움을 받아서 아래의 명령어를 통해서 잘 전파되고 있는지를 확인했다. 이 부분은 시간이 어느 정도 지나니까 전파가 완료되어서 해소가 되었다. 아직 Lightsail에 있는 instance랑 DB를 내리진 않았다.



## 소회 

뭔가 후련하면서도 시원섭섭하다. 이 세상에 영원한 건 없다는 것을 한 번 더 느꼈다. 그렇지만 여타의 다른 static generator를 사용하지 않고 직접 만들어서 써본 경험은 간만에 느끼는 소소한 재미였다. 시간은 한 파트타임으로 8시간 정도 쓴 것 같다. 코딩하는 재미가 이런 부분에 있었다는 것을 다시 한 번 느꼈다. 별거 아니지만 내 손으로 만드는 것만큼 재밌는 건 없다. 좋은 점은 계속 사용하면서 발전시킬 수 있다는 점이다. 지금은 매우 간단하지만 점점 나한테 필요한 것을 더 추가해 나갈 예정이다.
