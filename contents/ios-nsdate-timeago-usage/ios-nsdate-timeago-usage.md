---
title: '[iOS] NSDATE-TimeAgo Usage'
author: 'ash84'
pub_date: '2015-04-16'
description: ''
featured_image: ''
tags: ['dev', 'IOS', 'NSDATE', 'timeago']
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

[https://github.com/kevinlawler/NSDate-TimeAgo](https://github.com/kevinlawler/NSDate-TimeAgo)

얼마전에 [jquery.timeago ](http://ash84.net/2015/03/24/jquery-jquerytimeagojs-%EB%AA%87%EC%B4%88%EC%A0%84-%EB%AA%87%EC%9D%BC%EC%A0%84-%EA%B3%84%EC%82%B0%ED%95%98%EA%B8%B0/)에 대해서 글을 쓴적이 있는데 이번에는 NSDate다. 역시 timeago 를 타임라인을 만드는 과정에서 필요한데, jquery.timeago 에서는 날짜 데이터를 던져서 계산된 값을 가져오는 방식, (어떻게 보면 결국 같지만) NSDate-TimeAgo 에서는 Category 를 이용해서 `NSDate` 에서 바로 호출할 수 있도록 제공해 주고 있다.

<script src="https://gist.github.com/AhnSeongHyun/16d486196b5cbb243a7b.js"></script>

지원하는 언어는 다양한 편이고 당연히 한국어를 지원하고 있다. 프로젝트에 붙여 넣을때 `NSDateTimeAgo.bundle`도 가져다 붙이면 된다. 개인적으로 카테고리를 구현하는건 여전히 어색하긴 하지만 그래도 사용할때는 별도의 객체를 선언 및 생성할 필요가 없다는 점에서는 매우 좋은것 같다.

 

 



