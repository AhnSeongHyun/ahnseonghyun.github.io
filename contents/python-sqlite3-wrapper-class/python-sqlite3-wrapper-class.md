---
title: '[Python] sqlite3 를 손쉽게 쓰도록 만든 클래스'
author: 'ash84'
pub_date: '2017-04-17'
description: ''
featured_image: ''
tags: ['dev', 'gist', 'Python', 'sqlite3', 'sqlite3 python 연동하기', '파이썬']
---

파이썬(python)에서는 sqlite3 를 기본 라이브러리로 지원하고 있는 것은 누구나 다 아는 사실일텐데, 좀더 쓰기 편한 형태로 CRUD 에 대해서 클래스 랩핑을 해봤다. 함수에서 테이블 이름, Where 문, 혹은 컬럼이나 넣을 데이터 받으면 그에 따라서 쿼리 만들어서 쿼리 실행하도록 하였다. 별도의 예외처리는 안했기 떄문에 필요한 분들이 가져다가 커스텀해서 쓰시길 바란다.  

<script src="https://gist.github.com/3864502.js"></script>



