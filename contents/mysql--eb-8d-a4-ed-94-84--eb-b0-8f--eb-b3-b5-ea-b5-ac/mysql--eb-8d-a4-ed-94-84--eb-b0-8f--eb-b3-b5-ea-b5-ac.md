---
title: '[DB] mysql 덤프 및 복구'
author: 'ash84'
pub_date: '2016-08-13'
description: ''
featured_image: ''
tags: ['dev', 'MySQL', 'mysqldump', 'mysqldump option', 'mysqldump query']
---


테이블락이 걸렸다. 왜 걸렸는지 살펴보니 로그 db 가 MYISAM 방식으로 되어 있어서 생긴 문제였다. 이미 수많은 로그를 뒤로하고 운영중인 DB 를 백업해서 INNODB로 변경해서 다시 만들까도 생각해봤지만, 그럴바엔 차라리 mysqldump 를 사용해서 운영서버가 아닌 개발 서버로 옮겨서 분석 작업을 하는게 나을것 같았다. mysqldump는 서비스에 상관없이 데이터 및 구조를 가져올수가 있다.  

나 같은 경우는 매월 데이터를 가져와야 하기 때문에 dump시 쿼리 비슷하게 필요한 데이터만 가져올수 있었으면 했는데, 다행히 `-w 옵션`을 사용하면 다음과 같이 쿼리문의 where 절처럼 조건을 사용해서 가져올수가 있다. 
<script src="https://gist.github.com/AhnSeongHyun/56f0954620e4033cdea4.js"></script>

복구는 다음과 같다.

<script src="https://gist.github.com/AhnSeongHyun/a34b6ed34d6890aa10b8.js"></script>

Stored Procedure, Functions, Trigger 들을 mysqldump 로 가져오려면 다음과 같이 써주면 된다.

<script src="https://gist.github.com/AhnSeongHyun/adf8b15f21e267b60f9b.js"></script>


추가적으로 mysql 대기현상과 관련해서 잘 정리된 링크를 남긴다.


[MySQL 사용 중 발생할 수 있는 대기 현상 장애의 원인과 대처](http://blog.pages.kr/232)
 
**Reference:**

- [http://cloudjak.tistory.com/17](http://cloudjak.tistory.com/17)



