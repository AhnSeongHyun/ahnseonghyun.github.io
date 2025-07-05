---
title: '[JAVA] @Override eqauls() 함수'
author: 'ash84'
pub_date: '2017-03-24'
description: ''
featured_image: ''
tags: ['dev', 'Effective Java', 'equals 함수 오버라이드', 'equals() 재정의', 'equals()함수', 'Java']
---


<span style="font-size: 11pt; ">****</span><span style="font-size: 11pt; "> **Effective Java** 에 나오는 내용중 **[항목8]** 번에 해당하는 내용인데 equals()  메소드의 오버라이드에 대한 내용이 정리되어 있다. 요약하자면, 기본형(primitive) 타입은 == 을 이용해서 검사하고, 클래스 형은 자바에서 제공하는 것이라면, equals() 메소드를 사용하면 된다. 그리고 기본형 중에서 double, float 형은**[Double.Compare()](http://docs.oracle.com/javase/6/docs/api/java/lang/Double.html#compare(double, double)),[ Float.Compare()](http://docs.oracle.com/javase/6/docs/api/java/lang/Float.html#compare(float, float))** 함수를 쓰도록 권장한다. 파라미터로 들어오는 Object 형은 **instanceof** 를 통해서 반드시 클래스 타입을 검사하고, 변환해서 사용하라고 한다. 파라미터 타입인 Object 타입은 바꾸지 말고. 읽어보면 좋은 내용이다. equals() 함수를 override 해서 사용하시는 분이라면 필독필요.</span>

<span style="font-size: 11pt; "> </span>

<script src="https://gist.github.com/3978638.js"></script>



