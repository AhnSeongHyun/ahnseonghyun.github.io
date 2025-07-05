---
title: '[Java] StringAppender, StringBuilder 짭.'
author: 'ash84'
pub_date: '2017-04-25'
description: ''
featured_image: ''
tags: ['append', 'dev', 'Java', 'StringAppender', 'StringBuilder', 'StringBuilder 개선', '자바']
---

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>

별건 아닌데, StringBuilder를 자주 사용하는데 단점이라면 너무 자주 사용해서 new 로 매번 생성한다는 점이고 또 다른 단점은 append() 함수가 하나의 인자만을 받는 다는 점이다. 그래서 StringBuilder를 가지는 클래스를 만들고 자주 사용하면 생성하지 않고 쓰게 하기 위해서 static으로 모든 함수를 만들어봤다. 그리고 매번 `append()` 하고 마지막에 `toString()`  하는 것이 번거로워서 `mergeToStrt()` 함수를 만들었는데, 가변인자로 받고 `toString()`까지 해주도록 하였다. 하지만 이 클래스는 멀티스레드 환경에서 문제가 있을수 있다.  


<script src="https://gist.github.com/4508791.js"></script>



