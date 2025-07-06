---
title: '(espressoOtr) DateTime wrapping 작업'
author: 'ash84'
pub_date: '2013-03-07'
description: '개인적으로 여러가지 데이터 형이 있겠지만 가장 쓰기 불편하고 짜증나는 형은 단연 날짜와 시간에 대한 데이터 형식인 Date(Java 기준, 다른 언어도 크게 다르지 않다.) 일것이다. wrapping 작업을 하는 이유는 사실 우리가 날짜 와 시간 관련 작업을 할때 하는 작업이 그리 다양하지 않다는 가정에서 출발했다. 실제로 내가 가장 필요했던'
featured_image: ''
tags: ['espressoOtr', 'github', 'Java', '자바 라이브러리']
---


<span style="font-size: 11pt;">개인적으로 여러가지 데이터 형이 있겠지만 가장 쓰기 불편하고 짜증나는 형은 단연 날짜와 시간에 대한 데이터 형식인 Date(Java 기준, 다른 언어</span><span style="font-size: 11pt;">도 크게 다르지 않다.)</span><span style="font-size: 11pt;"> 일것이다. wrapping 작업을 하는 이유는 사실 우리가 날짜 와 시간 관련 작업을 할때 하는 작업이 그리 다양하지 않다는 가정에서 출발했다. 실제로 내가 가장 필요했던 것은 현재 날짜/시간을 Date 형식 혹은 특정 포맷 형식의 String 으로 가져오는 작업이다. 아래의 코드와 같이 말이다. </span>

<script src="https://gist.github.com/AhnSeongHyun/5105723.js"></script>

<span style="font-size: 11pt;">날짜와 시간에 대한 작업은 [espressoOtr](https://github.com/AhnSeongHyun/espressoOtr) 라이브러리 안에 EasyDateTime 클래스에 계속 작업을 해나갈 예정이다. 무엇을 작업할 것인지에 대한 내용은 날짜와 시간 관련된 다른 작업이 필요할 경우 그때그떄 추가할 예정이다. Wrapping 작업이 귀찮기는 하지만, 이런식으로 자주 사용하는 것들을 Java에서 제공하는 기본형이라도 해두면 편한것 같다. </span>



