---
title: 'dev-meetup.github.io 개발기'
author: 'ash84'
pub_date: '2017-02-20'
description: '개발자 세미나는 예전보다 훨씬 많이 자주 열리고 있다. 컨퍼런스 단위는 사실 1년에 많이 열리진 않지만, 어떤 단체나 회사에서 주도하기 때문에 홍보가 잘되고 많은 사람들이 참여하기 마련이다. 그렇지만, 밋업이나 세미나 그런 단위는 커뮤니티안에서만 주로 공유가 되고 외부 개발자가 알기가 어려웠다. 물론 찾는 노력을 하면 되지만, 모든 커뮤니티/사이트에 대한 워치독(watchdog)이 될 수는 없다. 

[dev-meetup.github.io](https://dev-meetup.github.io) 는 컨퍼런스보다 작은 단위의 세미나나'
featured_image: 'https://c1.staticflickr.com/4/3720/33589679996_9be27b3415_b.jpg'
tags: ['dev', 'dev-meetup.github.io', 'github', 'travis-ci']
---

개발자 세미나는 예전보다 훨씬 많이 자주 열리고 있다. 컨퍼런스 단위는 사실 1년에 많이 열리진 않지만, 어떤 단체나 회사에서 주도하기 때문에 홍보가 잘되고 많은 사람들이 참여하기 마련이다. 그렇지만, 밋업이나 세미나 그런 단위는 커뮤니티안에서만 주로 공유가 되고 외부 개발자가 알기가 어려웠다. 물론 찾는 노력을 하면 되지만, 모든 커뮤니티/사이트에 대한 워치독(watchdog)이 될 수는 없다. 

[dev-meetup.github.io](https://dev-meetup.github.io) 는 컨퍼런스보다 작은 단위의 세미나나 밋업에 대해서 모아서 보여주기 위해서 만들었다. 처음에는 별도의 서버에 올리려고 생각했고, 익숙한 파이썬을 사용하는 방향으로, python3.6 + japronto 를 이용해서 개발하려고 했다. 그런데 문득 이런 생각이 들었다. 

> **각각의 이벤트를 어떻게 지속적으로 채워질것인가?**


**이 물음에 파싱(parsing) 을 해서 넣는다.** 는 정답이 아니다. 왜냐하면 온오프믹스나 meetup 사이트는 그렇다 쳐도 구글설문이나 블로그, 슬랙을 통해서 공지를 하는 경우가 있기 때문에 파싱으로 대응하기는 어려운 것 같다. 

그래서 github 상에 올려두면 세미나/컨퍼런스를 홍보하고 싶은 사람이 `pull request` 를 보내고 그걸 보여주면 어떨까? 하는 생각을 하게 되었다. 

캘린더와 리스트로 보여주는 것을 결정했고, 캘린더 관련 라이브러리로 [fullcalendar](https://fullcalendar.io/)를 사용했다. 리스트 역시 [fullcalendar](https://fullcalendar.io/) 에서 제공하는 기능을 사용했다. 

![dev-meetup.github.io](https://c1.staticflickr.com/3/2892/33501573771_0bf876c019_b.jpg)

외부에서 다른 개발자가 pull request 를 보내기 위해서 이벤트 정보를 담는 부분을 따로 파일로 분리 하고자 했다. 이유는 2가지 인데, pull request를 원활하게 하기 위해서, 그리고 해당 데이터를 검증 하기 위해서이다. `/data/events.json` 에 이벤트 데이터를 넣어주는데 잘못된 데이터의 경우 fullcalendar 에서 랜더링 하지 못하기 때문에 이를 검증하는 것을 추가했다. 

> PR를 보낼때 마다 json을 어떻게 검증할 수 있을까? 

이 질문은 기존의 사용해봤던 [jsonschema](https://ash84.net/2017/01/03/flask-jsonschema-decorator/) 를 이용해서 python 으로 테스트케이스를 만들어서 돌리게 했다. 어떻게 돌리냐하면, 너무나도 github애서 익숙한 travis-ci 를 이용했다.

![travis-ci](https://cdn.travis-ci.com/images/logos/TravisCI-Full-Color-45e242791b7752b745a7ae53f265acd4.png)

PR 혹은 커밋이 될때마다 travis-ci 를 돌리게 했고, 그 안에서 python-jsonschema 를 이용해서 검증하도록 하였다. 이렇게 하게 되면 fail 이 날 경우 머지(merge)되지 않기 때문에 캘린더의 랜더링이 깨질 염려는 줄일 수가 있다. 

디자인이나 그런 부분은 미숙하기 때문에 [bootstrap-materialkit](https://www.creative-tim.com/product/material-kit)을 연동했다. 그나마 좀 깔끔해진 느낌이다. 

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>


여전히 내가 노가다로 온오프믹스와 각종 페북 그룹페이지, 슬랙 등을 뒤지면서 추가하고 있다. 노가다라고 하지만 생각보다 많은 세미나들이 있다는 사실에 놀라고 있다. 이벤트 추가 작업을 하면서, 회사 및 주변분들에게 밋업/세미나를 적극적으로 추천하고 있다. 또 많은 밋업과 세미나들이 열리고 또 발표자를 기다리는 곳들도 많은 것 같다. 그만큼 성장 할 수 있는 기회도 예전보다 많아진 것 같아서 기분이 좋다. 


ps1) 이 글을 쓰고나서 [Disqus](https://disqus.com) 서비스를 연결해 두었다. 생각보다 밋업들이 등록이나 일정이 갑자기 변경되는 경우가 많아서 댓글 형식으로 올리면 어떨까해서 달게 되었다.  

ps2) 회사 동료분께 부탁해서 로고 및 홈스크린 아이콘을 넣었음. ㅎㅎ 
