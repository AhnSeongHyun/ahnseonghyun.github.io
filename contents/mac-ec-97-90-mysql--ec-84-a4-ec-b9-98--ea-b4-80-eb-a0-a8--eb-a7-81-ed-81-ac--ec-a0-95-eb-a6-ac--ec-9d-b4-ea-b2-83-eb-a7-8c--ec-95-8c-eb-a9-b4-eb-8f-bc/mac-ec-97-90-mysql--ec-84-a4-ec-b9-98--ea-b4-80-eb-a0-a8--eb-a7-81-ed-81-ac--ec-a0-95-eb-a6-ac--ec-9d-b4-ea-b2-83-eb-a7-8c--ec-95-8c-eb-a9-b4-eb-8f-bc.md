---
title: 'mac에 mysql 설치 관련 링크 정리, 이것만 알면돼!!'
author: 'ash84'
pub_date: '2012-10-30'
description: 'mac(osx) 에서 mysql 설치하기 위해서 참고했던 링크들이다. 다른 분들도 도움이 되시길. 

![](http://ash84.net/wp-content/uploads/1/cfile9.uf.2031E54F508F0E710EF62A.jpg)

**1. 설치 및 기본 세팅**
– [http://hoyanet.pe.kr/1942](ht'
featured_image: ''
tags: ['mac', 'mac mysql 설치', 'MySQL', 'mysql 패스워드']
---


<span style="font-size: 11pt; ">mac(osx) 에서 mysql 설치하기 위해서 참고했던 링크들이다. 다른 분들도 도움이 되시길. </span>

![](http://ash84.net/wp-content/uploads/1/cfile9.uf.2031E54F508F0E710EF62A.jpg)

<span style="font-size: 11pt; ">**1. 설치 및 기본 세팅**</span>

<span style="font-size: 11pt; ">– [http://hoyanet.pe.kr/1942](http://hoyanet.pe.kr/1942)</span>

<span style="font-size: 11pt; ">– 단연 중요한것은 패스워드 설정 부분이다. 왜냐하면 msql 은 설치를 해도 패스워드 설정을 해주지 않기 때문에 따로 해주어야 한다. </span>

<span style="font-size: 11pt; ">**2. GUI 접속 툴은 몰 쓸까?**</span>

<span style="font-size: 11pt; ">– [http://jeen.tistory.com/353](http://jeen.tistory.com/353)</span>

<span style="font-size: 11pt; ">– 아쉽게도 mysql은 커맨드 기반이기 때문에 서드파티가 만든 mysql 프로그램이 있어야 한다. 다행이 최근에 발견한 sequel pro 가 그 대안일수 있겠다. 아직 많은 기능을 사용해 보진 않았지만, 나쁘지 않아 보인다. </span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">**3. my.cnf 는 어디에?**</span>

<span style="line-height: 2; font-size: 11pt; ">– </span><span style="font-size: 15px; line-height: 29px;">[http://forums.mysql.com/read.php?11,366143,376017#msg-376017](http://forums.mysql.com/read.php?11,366143,376017#msg-376017)</span>

<span style="font-size: 11pt; ">– 이상하게 설정파일을  /etc/my.cnf 를 찾을 수가 없다면 위의 링크를 참고 하시길. support-files 에 있기 때문에 복사해서 사용하면 된다. </span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">**4. 한글깨짐 문제**</span>

<span style="font-size: 11pt; ">– [[Link]](http://www.imcore.net/mysql-5-5-%ED%95%9C%EA%B8%80-%EA%B9%A8%EC%A7%90%EB%AC%B8%EC%A0%9C-%ED%95%B4%EA%B2%B0%ED%95%98%EA%B8%B0-utf8/) </span>

<span style="font-size: 11pt; ">– 한글 데이터를 넣었는데 깨진다면, my.cnf 안에 설정을 변경해 주어야 한다. </span>



