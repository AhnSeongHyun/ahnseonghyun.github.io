---
title: '(iOS) 날짜에서 요일 가져오기'
author: 'ash84'
pub_date: '2013-05-20'
description: ''
featured_image: ''
tags: ['dev', 'iOS', 'NSDAT', 'NSDate 변환', '날짜 계산 Objective-c', '날짜 요일']
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

날짜에서 요일을 가져오는 부분인데, 인터넷에서 찾아보다보니 여러가지 방법이 있는 것을 알게 되었다. C라이브러리를 사용하는 방법이 있고 첼러의 공식을 사용하는 것이 있는데, 필자는 COCOA클래스를 이용하는 방법을 선택했다. 이유는 늘 그렇듯 잘 만들어 놓은것을 사용하는것이 좋다.(순정이 짱) 아래의 코드는 [여기서](http://www.cocoadev.co.kr/283) 가져온 코드인데,  `getDayOfWeek:` 함수에서 년월일을 인자로 받고 있는데, 그 부분을 감싸는 하나의 함수를 더 만들어서 `NSDate` 형으로 인자를 넘기면 거기서 연월일을 가져와서 해당 함수에 요청하고 결과값으로 요일을 가져오도록 구성하였다. [NSDateUtils](http://ash84.tistory.com/957)는 이전 포스팅에서 말했던것 처럼 그냥 `NSDate`처리를 위한 유틸 클래스 이다. 

<script src="https://gist.github.com/AhnSeongHyun/5615983.js"></script>



