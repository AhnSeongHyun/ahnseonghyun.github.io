---
title: 'jinja template - extend block 이용하기'
author: 'ash84'
pub_date: '2018-05-19'
description: '기존에는 `{%include "head.html" %}` 이런식으로 html 내 특정 부분, 즉 자주 사용하는 부분을 모든 페이지에 붙여서, `include` 지시자를 이용해서 가져오는 방식을 사용해 왔었다. 작은 프로젝트에서는 head.html 을 따로 두고 그 안에서 css 및 기타 `` 부분에 들어가는 코드를 작성해서 재활용 했었다.

그런데 최근에 body 에서 navigation bar 와 footer (상단, 하단)만 두고 가운데의 컨텐츠 부분만 상단 혹은 하단의 링크에 따라서 바꿔서 보여줘야 하는 요구사항이 있었는데 생'
featured_image: 'http://www.pocoo.org/_images/jinja-logo.png'
tags: ['dev', 'FLASK', 'jinja', 'template']
---

기존에는 `{%include "head.html" %}` 이런식으로 html 내 특정 부분, 즉 자주 사용하는 부분을 모든 페이지에 붙여서, `include` 지시자를 이용해서 가져오는 방식을 사용해 왔었다. 작은 프로젝트에서는 head.html 을 따로 두고 그 안에서 css 및 기타 `` 부분에 들어가는 코드를 작성해서 재활용 했었다.

그런데 최근에 body 에서 navigation bar 와 footer (상단, 하단)만 두고 가운데의 컨텐츠 부분만 상단 혹은 하단의 링크에 따라서 바꿔서 보여줘야 하는 요구사항이 있었는데 생각보다 페이지가 많았고, 상단, 하단에 대한 html 코드 부분도 상당했다. 이전과 같은 방법으로 사용한다면 n 개의 페이지를 만들고 그 안에 include 를 상단 include, 하단 include 이런식으로 만들어 줘야만 해서 뭔가 불편한것 같아서 jinja template 레퍼런스를 참고 하니, 하나의 부모 템플릿을 만들고 그 안에 block 을 지정해두고, 해당 템플릿을 활용 하는 다른 페이지들은 block 부분만 필요하다면 구현해 주면 된다.

`{% include %}` 방식보다 좋은점이라면 단연 코드의 양이 많은 부분을 템플릿으로 두고, 그 안에서 각 페이지마다 커스텀 할 수 있는 부분들을 지정해서 페이지에서 구현하기 때문에 각 페이지별 코드의 양이 적어진다는 사실이다.(케바케겠지만.) 해보니까 좋은데, 중요한 점은 부모 템플릿에서 어느 부분을 커스텀 할지 정하는 지가 중요한것 같다. 예를 들면, layout.html 이 부모 템플릿이고 그것을 확장(extend)  해서 사용하는 페이지를 아래의 코드처럼 지정할수가 있겠다.

<script src="https://gist.github.com/AhnSeongHyun/df70a876e0c7836edc53.js"></script>

jqeury의 `document.ready()` 와 같은 함수의 경우, 부모 템플릿(layout.html) 에서 정의했기 때문에 확장해서 사용하는 페이지에서 정의해도 소용이 없다. 실행되지 않는다는 이야기이다. 이를 위해서는 `ready()` 에 block을 설정하고 페이지에서는 함수를 호출하는 부분만 써주면 된다. <script src="https://gist.github.com/AhnSeongHyun/aed7e67ef87cc4311242.js"></script>



