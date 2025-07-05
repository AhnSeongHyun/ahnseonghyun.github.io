---
title: 'maven에서 단위테스트가 안될때, Junit4를 추가하자.'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['dev', 'junit4', 'maven']
---


<span style="font-size: 11pt;"></span><span style="font-size: 11pt;"></span><span style="font-size: 11pt;">maven 빌드 환경을 세팅하고 기존의 Junit 단위테스트 클래스를 maven 의 test (src/test/java)에 넣어서 빌드를 하니 빌드시(package), 이상하게 Junit 에서는 정상적으로 작동하는 maven 빌드에서만 이상하게 fail 이 발생하는 것을 볼수 있었다. </span>

<span style="font-size: 11pt;">간단하게, Junit4를 maven dependency에서 찾아서 연동을 하자. 귀찮으면 아래의 dependency를 붙이면 된다. </span>

<span style="font-size: 11pt;"></span>

<script src="https://gist.github.com/4393655.js"></script>



