---
title: '(iOS) 기본 숫자형 NSDictionary에 넣기'
author: 'ash84'
pub_date: '2013-09-17'
description: 'NSDictionary는 키-값 형태로 데이터를 집어넣는것인데, 객제형은 잘 들어가는 대신에 이상하게 int, double과 같은 경우에는 setValue 함수를 사용해도 XCode 에서 에러라고 표시를 한다. 그런 경우에는 아래와 같이 NSNumber 로 한번 감싸주면 된다. int, float, double 등에 맞게 사용하면 된다.'
featured_image: ''
tags: ['dev', 'double nsdictionary', 'iOS', 'NSDictionary']
---
<span style="font-size: 11pt;">NSDictionary는 키-값 형태로 데이터를 집어넣는것인데, 객제형은 잘 들어가는 대신에 이상하게 int, double과 같은 경우에는 setValue 함수를 사용해도 XCode 에서 에러라고 표시를 한다. 그런 경우에는 아래와 같이 NSNumber 로 한번 감싸주면 된다. int, float, double 등에 맞게 사용하면 된다.</span>

<span style="font-size: 11pt;"> </span>

<script src="https://gist.github.com/AhnSeongHyun/6591378.js"></script>



