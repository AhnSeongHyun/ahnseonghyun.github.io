---
title: '(iOS) HTML Tag Remover'
author: 'ash84'
pub_date: '2012-11-19'
description: ''
featured_image: ''
tags: ['dev', 'iOS', '개발', '어플', '한우찾기']
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

한우찾기 앱 개발하면서 최근에 뉴스검색 기능을 추가했는데, 네이버 검색결과의 경우 착하게도 검색어에 대해서 하이라이팅이 되어서 나온다. 아쉽게도 태그로 처리된 하이라이팅은 때론 매우 불필요하기에, 이 부분을 제거해야 한다. 아래의 코드에서는 기본적인 태그와   &quote; 이런 부분을 처리하도록 구성되었다. 정규표현식을 써서 NSRange 를 가져오는 부분이 포인트다. 
 
<script src="https://gist.github.com/4079200.js"></script>



