---
title: 'SQLAlchemy with StoreProcedure'
author: 'ash84'
pub_date: '2016-08-24'
description: ''
featured_image: ''
tags: ['sqlalchemy', 'Python', 'db', 'stored-procedure']
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

제목자체가 역설적이지만, 이렇게 써야 할때가 있다. 예를들면, 레거시를 다시 재개발하는 수준에서 특정 프로시저는 단순히 db를 조회하는 것 이상의 프로그래밍적인 기능을 가지고 있을때가 있다. 또한, 다른 이유로 ORM인 SQLAlchemy와 저장프로시저를 혼합해야할 때가 있는데, 그럴때 따로 저장프로시저용 코드를 쓰기 보다는 SQLAlchemy 를 이용해서 프로시저를 실행하고 값을 가져오는 것이 좋다. 

<script src="https://gist.github.com/AhnSeongHyun/ad3653667d9094db71872683ff0a74fc.js"></script>

개인적으로 SQLAlchemy를 써서 좋다고 생각하는 이유는 유지보수 하는 입장에서 DB연결 문자열 등과 같은 관리포인트도 하나로 유지하면 좋고, ORM 외에 몇개의 프로시저를 위해서 DB연결 라이브러리에 종속적인 코드를 짜고 싶지 않다는 것을 느꼈다.(안된다는 것이 아니다.) 

위의 코드는 Flask-SQLAlchemy 로 짠 코드인데, 일반 SQLAlchemy를 아시는 개발자라면 쉽게 이해할 수 있는 코드이다. 다른 것보다도 `raw_connection()` 함수에 대해서 설명하자면 프록시된 DBAPI 연결 객체를 반환하는데, 실제 DBAPI 연결과 동일한 기능을 수행한다고 한다. 단 `close()` 함수에 한해서는 예외적으로 실제로 연결이 끊어지는 거이 아니라 pool로 리턴되어 진다고 한다.

[원문](http://docs.sqlalchemy.org/en/latest/core/connections.html#sqlalchemy.engine.Engine.raw_connection)은 아래와 같다. 


> **raw__connection(_connection=None)**

>Return a “raw” DBAPI connection from the connection pool.

> The returned object is a proxied version of the DBAPI connection object used by the underlying driver in use. The object will have all the same behavior as the real DBAPI connection, except that its close() method will result in the connection being returned to the pool, rather than being closed for real.

> This method provides direct DBAPI connection access for special situations when the API provided by Connection is not needed. When a Connection object is already present, the DBAPI connection is available using the Connection.connection accessor.
