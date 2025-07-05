---
title: '[Java] StringBuilder delete() 시, 현재 길이 체크할것.'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['dev', 'StringBuilder', '방어적 코드 작성', '자바']
---


<span style="font-size: 11pt;">너무 간단한것이긴 한데, 최근에 만든 소스에서 실수를 한적이 있어서 체벌(?)차 이렇게 적는다. 무엇인가 가변 문자열 조합을 위해서는 String 이 단연 후달리는 것은 보편적 자바 개발자라면 다 아는 사실일텐데, 그래서 StringBuilder를 사용하는데 실수 할수 있는 부분이다.</span>

<span style="font-size: 11pt;"> </span>

<span style="font-size: 11pt;">아래의 코드는 쉼표(,) 기반의 문자열을 만들어 나가는 과정이다. 그리고 마지막 쉼표를 제거하는 코드가 있다. 사실 for문안에서 쉼표를 넣을지 말지를 결정할 수 있으나, for 문안에서 비교문을 쓰지 않으려했다.</span>

<span style="font-size: 11pt;"> </span>

<span style="font-size: 11pt;"></span>

<script src="https://gist.github.com/4324126.js"></script>

<span style="font-size: 11pt;text-align:justify; line-height:2;">문제가 되는 부분은 delete() 함수부분이다. for 문을 통해서 StringBuilder.append() 함수에 데이터를 넣기 때문에  for문이 돌지 않으면 StringBuilder 안에 데이터가 없게 되고, length()-1 연산에서 -1이 되면서 문제가 생기는 것이다. 방어적인 코드 작성을 위해서는 다음과 같이 작성해야 한다.</span>

<span style="font-size: 11pt;text-align:justify; line-height:2;">  
</span>

<span style="font-size: 11pt;">  
</span><script src="https://gist.github.com/4324159.js"></script>



