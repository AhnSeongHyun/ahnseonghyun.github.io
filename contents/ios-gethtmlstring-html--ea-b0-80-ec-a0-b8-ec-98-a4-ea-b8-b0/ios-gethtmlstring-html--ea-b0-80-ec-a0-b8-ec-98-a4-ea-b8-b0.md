---
title: '[iOS] GetHtmlString(), HTML 가져오기'
author: 'ash84'
pub_date: '2017-04-25'
description: ''
featured_image: ''
tags: ['dev', 'get html string', 'HTML Parsing', 'IOS', 'Objective-C', 'Open Source']
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
한우찾기 라이브러리를 만드는 과정에서 가장 먼저 해야할 일은 기존의 자바스크립트 방식을 대체할 수 있는 방안을 찾아야 하는 것이었는데, 그 중에 하나가 HTML 자체를 String 으로 가져와서 파싱하는 방식이다. Objective-C 에서는 NSString 을 통해서 해당 기능을 다음과 같이 제공하고 있다. 

<script src="https://gist.github.com/3519444.js"></script>

 주의 해야할 점이라면, 해당 HTML의 charset에 맞춰서 가져와야 깨지지 않는다는 점이다. 영어/숫자라면 크게 상관없겠지만, 한국어만 해도 charset을 잘못입력하면 깨질수가 있다. 다음의 charset enum을 꼭 참고해서 사용하도록 하자.  

<script src="https://gist.github.com/3519508.js"></script>



