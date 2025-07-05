---
title: '(python) html unescape'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['dev', 'html 특수문자 변환', 'Python', 'unescape', '파이썬']
---


<span style="font-size: 11pt;">HTML 가져온 것을 화면에 보여주거나 할때 반드시 해야하는 작업중에 하나가 바로 언이스케이프작업(Unescape) 이다. HTML 안에 특수 문자들은 어떤 일련의 문자열로 표현이 된다. 예를 들면, ” ” 공백은    <, > 은 < > 이런식으로 말이다. 그렇기 때문에 저런 문자들이 원래 우리가 이해하는 특수문자로 바꿔주는 작업을 하는데 그것을 unescape 작업이라고 한다. 반대로 특수문자들을 일련의 약속된 문자열로 바꾸는것은 escape 작업이다. </span>

<span style="font-size: 11pt;">아래의 코드는 파이썬에서 unescape를 하는 코드이다. 별것 없고, 정규식을 사용해서 할수 있는 방법도 있겠지만 원래 기본적으로 가지고 있는 HTMLParser 를 import 하는 식으로 가져와서 이용할 수 있다. </span>

<script src="https://gist.github.com/AhnSeongHyun/5982015.js"></script>



