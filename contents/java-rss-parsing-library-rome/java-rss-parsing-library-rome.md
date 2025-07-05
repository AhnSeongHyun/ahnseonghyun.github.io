---
title: '(Java) RSS 파싱 라이브러리 ROME'
author: 'ash84'
pub_date: '2017-04-25'
description: ''
featured_image: ''
tags: ['dev', 'Java', 'java rss parser rome', 'rss', 'RSS JAVA Library', 'RSS 파싱', '자바']
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

RSS 파싱 작업을 물론 하위단계 부터 다 구현을 할려고 하면 할수 있겠지만, 바야흐로 오픈소스의 시대. 그리고 자바라는 언어에서 기능을 구현하는데, 찾아보지 않는다는것은 죄악이라는 생각에 찾아보니 [ROME](https://rometools.jira.com/wiki/display/ROME/Home) 이라는 것이 있다. **사실은 [Jakarta FeedParser](http://commons.apache.org/dormant/feedparser/) 라는 것이 있는데 dormant(휴식기) 상태인것 같다. 다운로드나 maven 주소가 없는 상태이다.**


자바캔 : [http://javacan.tistory.com/entry/ReadRSSAtomFeedUsingROME](http://javacan.tistory.com/entry/ReadRSSAtomFeedUsingROME)

위의 주소를 보면 잘 나와있겠지만, URL 을 가지고 feed를 찾고 그 안에 있는 entry 를 찾는 방식이다. 오늘 2시간동안 작업했는데 생각보다 빠르고 괜찮다. 몇가지 유의사항을 적으면 다음과 같다. 


**1. entry.getDescription().getValue() 는 원문 자체가 리턴되지 않는다.**

– 원문 전체가 아닌 자체라고 이야기한 이유는 간단하다. 즉, 우리가 블로그를 통해서 본 글 자체가 아니라, html 과 함께 들어있는 글이 리턴되는 문제가 있다. 사실 이부분의 해결을 위해서는 별도의 htmlParser를 사용하기를 권장한다. 필자의 경우, [jericho parser](http://jericho.htmlparser.net/docs/index.html) 를 사용하였다. 

**2. entry.getPublishedDate()**

– 날짜 형식은 영문으로 나오도록 되어 있다. 때문에 데이터베이스에 넣거나 혹은 파일에 내릴것이라면 간단하게 Date Format 변환을 하는것을 추천한다.  

크게 어려운 내용은 아니기 때문에 별다르게 쓸 말은 없는데, 한가지 아쉬운 점은 RSS리더를 통해서 전문을 가져올 수 없다는 점이다. 즉, 하나의 글에 대한 전문 뿐만 아니라, 전체 블로그 글을 가져올수 있었으면 좋겠다는 생각을 한다.  



