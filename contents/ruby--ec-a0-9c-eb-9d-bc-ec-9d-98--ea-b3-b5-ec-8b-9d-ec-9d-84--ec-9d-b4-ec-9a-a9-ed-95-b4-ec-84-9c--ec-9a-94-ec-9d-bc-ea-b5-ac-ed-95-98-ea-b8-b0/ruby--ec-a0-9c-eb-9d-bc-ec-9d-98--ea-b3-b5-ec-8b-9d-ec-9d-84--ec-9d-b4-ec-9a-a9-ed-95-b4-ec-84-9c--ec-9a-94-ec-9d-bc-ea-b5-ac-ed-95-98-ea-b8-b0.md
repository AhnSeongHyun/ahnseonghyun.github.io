---
title: '[Ruby] 제라의 공식을 이용해서 요일구하기.'
author: 'ash84'
pub_date: '2012-06-12'
description: ''
featured_image: ''
tags: ['RUBY', 'Zeller's congruence', '루비', '요일구하기', '제라의 공식']
---


<span style="font-size: 11pt; ">Siri Proxy 서버에 올릴 모듈을 개발하던 중에 요일을 체크하는 부분을 개발해야해서 찾아 보던 중 “제라의 공식” 이라는 것이 있다는 것을 알게되었다. 제라의 공식은 기본적으로 그레고리력 1582년 10월 15일 이후에만 적용되는 공식으로 현재의 날짜(연도, 월,일)을 공식에 넣으면 해당하는 요일을 알수 있다는 것이다. </span>

<span style="font-size: 11pt; ">제라의 공식에 대해서 </span>

<span style="font-size: 11pt; ">: [http://www.cyworld.com/widwolf/4432538 ](http://www.cyworld.com/widwolf/4432538)</span>

<span style="font-size: 11pt; ">위의 블로그를 보면 제라의 공식에 대해서 자세히 설명이 되어 있는데, 꽤 유용하게 쓰일것 같다. 왜 저런 공식이 나오는지를 이해하고 싶으신 분이 있으시다면, 아래의 위키피디아 링크를 참고하시길 바란다.(한국어는 없음)</span>

<span style="font-size: 11pt; ">[http://en.wikipedia.org/wiki/Zeller’s_congruence](http://en.wikipedia.org/wiki/Zeller's_congruence)</span>

<span style="font-size: 11pt; ">루비를 이용해서 제라의 공식을 구현한 소스코드는 다음과 같다. </span>

<script src="https://gist.github.com/2903986.js?file=gistfile1.rb"></script>



