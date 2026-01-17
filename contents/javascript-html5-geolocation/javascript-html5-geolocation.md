---
title: '(javascript) HTML5 geolocation 사용하기'
author: 'ash84'
pub_date: '2013-09-02'
description: ''
featured_image: ''
tags: ['HTML5', 'dev', 'geolocation', 'javascript', '위도 경도', '위치 찾기']
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

<span style="font-size: 11pt;"></span><span style="font-size: 11pt;"></span><span style="font-size: 11pt;">뭐 기술이라고 말할수도 없는데.. 사실 내가 잘 몰랐던 내용이라서 정리한다. HTML5 geolocation 을 이용하는 코드는는 w3cschool 홈페이지에도 나와있듯이 아래와 같다. </span>
 

<script src="https://gist.github.com/AhnSeongHyun/6410306.js"></script>

<span style="font-size: 11pt;line-height:2;text-align:justify;">보면 알겠지만 button 을 눌러서 자바스크립트 함수를 부르는 것인데, 내가 원하는 것은 페이지가 뜨자마자 geolocation 값을 가져오는 것이었다. 그래서 했던 방법이 <body onload=””> 부분에 함수를 호출하도록 두는 것인데, 사실 이 방법도 문제가 있었다. 문제는 위도와 경도 값을 받아서 첫 페이지에서 다른 페이지로 http get 방식을 통해서 전달해야 한다면 onload 후, geolocation 이 위도경도를 가져오는 시점 자체를 알기가 힘들다. 그래서 꼼수지만 사용한 방법은  부분에서 스크립트를 실행하도록 하는 것이다. 이렇게 되면 html 로딩시 좀더 빠른 시점에 geolocation을 가져올수 있다. 물론 이 방법이 정석은 아니라는 생각이 든다. 참고하시길. </span>

<span style="font-size: 11pt;">  
</span>

<script src="https://gist.github.com/AhnSeongHyun/6410347.js"></script>



