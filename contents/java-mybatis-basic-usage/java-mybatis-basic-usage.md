---
title: '(Java) mybatis 기본 사용 정리'
author: 'ash84'
pub_date: '2013-02-18'
description: ''
featured_image: ''
tags: ['dev', 'Java', 'mybatis', 'database']
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

**필요 라이브러리**

– mybatis-3.1.1.jar

– mysql-connector-jara-5.1.22-bin.jar

**db.propertise 작성**

– 데이터베이스 연결 정보가 담긴 파일 생성

– 아래의 내용은 mysql을 대상으로 작성된것임

```
 driver=com.mysql.jdbc.Driver  
 url=jdbc:mysql://127.0.01:3306/test  
 username=ash84  
 password=xxxxxx  
```

**mybatisConfig.xml 작성**


 – 이 파일이 중요한 이유는 mybatis 에서 SqlSessionFactory 객체 생성시, 사용되기 때문이다.  

– 또한 데이터베이스와 SQL문을 담고 있는 Mapper.xml 를 연결해 주는 작업을 한다.

– db.propertise 의 경로를 아래와 같은 경로로 설정할 경우, 현재 디렉토리가 아니라, 패키지의 root 에 두어야 한다. 

<script src="https://gist.github.com/AhnSeongHyun/4957570.js"></script>
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>

**Mapper.xml 생성**

– 아래와 같이 쓰고자 하는 sql 문을 작성한다. 

– mapper의 namespace는 뒤에서 실제 자바코드에서 해당 맵퍼를 호출할때 사용되는 구분자 역할을 하기 때문에 주의해서 작성한다. 

– id는 함수명과 같은 역할을 한다고 보면 된다. 

– result_type 은 해당쿼리의 결과를 담을 클래스를 지정하는 것이다. 

<script src="https://gist.github.com/AhnSeongHyun/4957588.js"></script>

**SqlSessionFactory 생성**

– 설정은 앞 단계에서 대부분 완료되었는데, 앞에서 설저한 myBatisConfig.xml 을 이용해서 SqlSessionFactory를 생성해야 한다. 

– 그리고 SqlSessionFactory 를이용해서 Session을 가져와야 한다. 

<script src="https://gist.github.com/AhnSeongHyun/4957598.js"></script>

**iBatis vs. myBatis 비교 링크**

- http://blog.naver.com/vikong?Redirect=Log&logNo=60180433051

