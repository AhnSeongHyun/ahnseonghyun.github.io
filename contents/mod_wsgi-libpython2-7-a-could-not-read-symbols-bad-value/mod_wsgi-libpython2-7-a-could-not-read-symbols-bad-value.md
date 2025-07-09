---
title: 'mod_wsgi libpython2.7.a could not read symbols bad value'
author: 'ash84'
pub_date: '2015-06-01'
description: ''
featured_image: ''
tags: ['apache', 'dev', 'mod_wsgi', 'Python']
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

centos 에서 python을 설치하지 않아도 되지만 2.7 이상의 버전을 사용하기 위해서는 소스설치를 해야한다. [여기](http://ash84.net/2015/02/17/centos-6x-python-27-%EC%97%85%EA%B7%B8%EB%A0%88%EC%9D%B4%EB%93%9C/)(댓글을 잘 보시길) 읽으면 할수 있을텐데, mod_wsgi 를 사용해서 apache와 연결해서 서버를 띄우고 나서 해당 url로(wsgi 와 연결된 url) 호출시 아파치의 에러로그에 아래와 같은 메시지가 나올수 있다.

> libpython2.7.a could not read symbols bad value

위에서 `libpython2.7.a` 라는 부분에서 버전에 따라서 조금씩 달라질 수 있는데, `mod_wsgi` 에서도 이부분을 [Unable To Find Python Shared Library](https://code.google.com/p/modwsgi/wiki/InstallationIssues#Unable_To_Find_Python_Shared_Library) 라고 설명하고 있다. mod_wsgi에서 python의 shared library 를 사용하는데 찾지 못하는 문제로 해결방법이 여러가지 있지만 선호하는 방식은 해당 라이브러리를 런타임시 참조하는 위치, lib나 usr/lib 로 복사해 놓으라는 것이다. 그게 /usr/local/lib 와 같은 디렉토리에 있는 경우에는 해당 디렉토리를 ‘/etc/ld.so.conf’ 에 추가하면 된다고 설명하고 있다. 추가를 위해서는 `ld.so.conf.d` 디렉토리에 들어가서 파일을 하나 만들고 그 안에 /usr/local/lib 라고 입력해두면 된다. 그리고 나서는 `ldconfig` (새로운 라이브러리가 업데이트 되었음을 인식시키고, dynamic linking table을 업데이트 시킨다.)를 통해서 인식시켜주면 된다.

실행하기 전에 이미 잘 연결되어 있는지 보려면, `ldd` 명령어를 이용해서 검사해보면 된다.

<script src="https://gist.github.com/AhnSeongHyun/464345f7024c3d74460d.js"></script>



