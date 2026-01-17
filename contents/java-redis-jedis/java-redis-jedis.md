---
title: '[JAVA] jedis를 이용한 Redis 와 연동하기'
author: 'ash84'
pub_date: '2012-09-03'
description: ''
featured_image: ''
tags: ['GitHub', 'Java', 'dev', 'jedis', 'open-source', 'redis', 'redis 연동하기', 'tutorial']
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

In-Memory DB 중에 여러가지가 있겠지만, 요즘에 각광 받는것이 redis 이다. redis 에 대해서는 찾아보시면 많이 나올텐데, 한마디로 말하자면 메모리에 key-value 방식으로 데이터를 저장하는 서버라고 보면 된다.</span><span style="font-size: 11pt;"> 좀더 다양한 설명자료는 검색과 그리고 사이트에서 redis를 다운 받아서 사용해 보면 쉽게 알 수 있다.  

> 그렇다면, 연동은 어떻게 해야할까?

redis 에서는 C부터 시작해서 Scala 까지 </span><span style="font-size: 11pt;">다양한 언어별로 client 링크를 제공해 주고 있다. 대부분 일반 개발자들이 만들어 놓은 오픈소스인데, 그 중에서도 자바(java) 와 관련된 항목은 다음과 같다. 

그 중에서도 [jedis](https://github.com/xetorthio/jedis/)에 대해서 알아보면, **jedis는 redis 에서 추천(recommend) 하는 클라이언트**이고,  github 를 통해서 소스를 제공하고 있다. 해당 github 의 wiki 에 Getting Started 에 가서 보면, git명령어를 통해서 jedis 소스를 다운받고 그리고 maven 을 통해서 패키징을 할 수 있도록 가이드하고 있다.

 하지만, 필자가 Getting Started 에서 하라는 대로 해봤을때에는 솔직히 말해서 쉽게 되지가 않는 문제가 있었다. maven 자체에 익숙하지 못한 부분도 있었고, 맥에서 설치하기란 조금 난감했다. 그래서 jar 화된 것을 찾아보니 다음과 같이[ 2.1.0 버전의 안정화된(stable) 버전](https://github.com/xetorthio/jedis/downloads)을 제공해 주고 있다. 나의 목적은 redis 에 내가 만든 명령어로 통신하는 것이라는 점을 다시 한번 상기시키면서 다운. 

일반적인 방법으로 받은 jar 파일을 추가하고 다음과 같이 RedisTest 라는 자바 프로젝트를 만들었다. 그리고 main 이라는 클래스를 만들고, 다음과 같이 jedis 관련 3가지 클래스를 import 하자. 

일단 가장 쉽게 데이터를 넣고 빼는 작업부터 해보자. 기본적으로 redis 와 통신하기 위한 객체로 JedisPool 객체를 생성한다. 일반 Jedis 객체를 생성하지 않는 이유는 해당 github 의 Getting Started 에서 권장하듯이 에도 나와있듯이 멀티스레드 환경에서 안전하지 않기 때문이다. 스레드 관련된 문제를 해결하기 위해서 JedisPool 객체를 다음과 같이 생성한다. 그리고 pool 객체의 getResource()함수를 이용해서 단일 Jedis 객체를 가져와서 이용하는 방식으로 사용하면 된다. 

getResource() 함수로 가져온 단일 Jedis 객체에 set 과 get 함수를 이용해서 key-value 로 데이터를 넣고 빼는 것 을 볼 수가 있다. Redis 명령어의 SET, GET 명령어를 함수화 한 것인데, Redis 고유 명령어와 jedis 의 함수명들이 대부분 일치하고 있어서, Redis 커맨드를 사용해 본 개발자라면 쉽게 함수를 이용할 수가 있다.  

일단 다 썼으면 종료를 해야하는데, 종료를 할때에는 다음과 같이 두가지 구문을 반드시 입력해 줘야 한다. 하나는 pool로 부터 가져온 Jedis객체를 사용후에 다시 pool 로 반환하는 것이고, 그 이후에 종료를 위해서 JedisPool 의 destory() 함수를 호출하면 종료가 됩니다. 

jedis 의 가장 기본적인 함수를 사용해 보았는데, 생각보다 어렵진 않다. 사용자 입맛에 따라서 쉽게 함수를 호출할 수 있을것으로 생각된다. 어느정도 수준까지 jedis가 지원하는지는 좀더 살펴봐야 겠지만, github 에 나와있는 소개문으로만 판단해 본다면, replication, distribution 등의 기능들도 제공하는것으로 보인다. 

Redis를 실제 업무에 적용하는것은 적용 도메인 마다 다르겠지만, 자바 기반의 환경에서 jedis 를 이용한다면 좀더 쉽게 연동이 가능하고 비지니스 로직에만 집중할 수 있을것 같아서 유용할것으로 생각된다.



