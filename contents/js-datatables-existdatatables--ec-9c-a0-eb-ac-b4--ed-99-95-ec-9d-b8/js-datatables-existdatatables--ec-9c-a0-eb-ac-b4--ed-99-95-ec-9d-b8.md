---
title: '[js] datatables exist?(datatables 유무 확인)'
author: 'ash84'
pub_date: '2015-08-26'
description: 'datatables 라는 자바스크립트 라이브러리를 자주 사용하는데(좋아서가 아님.) 요상하게 .DataTable() 함수를 2번 호출하면 duplication init 관련 오류가 나고 데이터가 한번 그려지고 그 다음에 다시 새로운 데이터로 그릴려고 하면 갱신이 안되는 문제가 있었다. if 문 처럼 datatables 가 있는지 확인하고 있으면, 한번 그려진 이후이기 때문에 그냥'
featured_image: ''
tags: ['datatables', 'dev']
---


<script src="https://gist.github.com/AhnSeongHyun/9f8f66a7c97da9bec7a1.js"></script>

datatables 라는 자바스크립트 라이브러리를 자주 사용하는데(좋아서가 아님.) 요상하게 .DataTable() 함수를 2번 호출하면 duplication init 관련 오류가 나고 데이터가 한번 그려지고 그 다음에 다시 새로운 데이터로 그릴려고 하면 갱신이 안되는 문제가 있었다. if 문 처럼 datatables 가 있는지 확인하고 있으면, 한번 그려진 이후이기 때문에 그냥 clear() 한후, 데이터 추가하고 그려준다.

 

 



