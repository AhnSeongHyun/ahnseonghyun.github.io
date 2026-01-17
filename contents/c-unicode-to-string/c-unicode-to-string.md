---
title: '[C#] Unicode To String'
author: 'ash84'
pub_date: '2010-07-19'
description: ''
featured_image: ''
tags: ['C#', 'dev', 'Unicod', 'Unicode to String', 'UTF-8']
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

간단한 코드다. 일명 Unicode 값 이라고 하는 것을 대입을 하면, 그에 맞는 문자를 불러와 주는 기능이다. codePage 라고 하는 것은 해당 Unicode가 소속된 국가나 지역을 의미한다. 자신이 불러와야 하는 언어가 어느 나라. 어디 지역인지 코드 페이지를 모른다면, UTF-8 codePage 인 65001을 넘겨주면 된다. 

예) UnicodeToString(“\u0041”, 65001); //’A’ 출력 
<script src="https://gist.github.com/3263969.js"></script>



