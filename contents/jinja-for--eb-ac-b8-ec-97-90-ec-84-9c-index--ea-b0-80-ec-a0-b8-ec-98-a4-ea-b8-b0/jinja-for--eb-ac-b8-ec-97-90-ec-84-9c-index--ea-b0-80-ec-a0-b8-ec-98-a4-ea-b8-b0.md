---
title: 'jinja template for 문에서 index 가져오기'
author: 'ash84'
pub_date: '2016-08-13'
description: '보통 jinja template 에서 for 문을 사용하게 되면 아래와 같이 어떤 리스트 내에 아이템을 탐색하게 되고 리스트내에 아이템을 직접 가져오는데 index가 필요한 경우, 예를들면 특정 index 만 건너뛰고 싶은 경우가 있는데 그럴경우는 `loop.index` 로 접근해서 index를 가져올수 있다. 아래의 코드를 보면 이해가 쉽다.'
featured_image: ''
tags: ['dev', 'FLASK', 'jinja', 'jinja for loop index']
---


보통 jinja template 에서 for 문을 사용하게 되면 아래와 같이 어떤 리스트 내에 아이템을 탐색하게 되고 리스트내에 아이템을 직접 가져오는데 index가 필요한 경우, 예를들면 특정 index 만 건너뛰고 싶은 경우가 있는데 그럴경우는 `<span style="font-size: 11pt;">loop.index</span>`<span style="font-size: 11pt;"> 로 접근해서 index를 가져올수 있다. 아래의 코드를 보면 이해가 쉽다. </span>

<script src="https://gist.github.com/AhnSeongHyun/5bb7c33dab28b00cc963.js"></script>

[2013/10/28 – [Programming/Flask] – (flask) jinja2 {% include %} 활용](http://ash84.tistory.com/entry/flask-jinja2-include-활용)



