---
title: '(Java) Effective Java 정리 파편.'
author: 'ash84'
pub_date: '2013-02-19'
description: '별거는 아니고 Effective 자바 읽으면서 몇가지 메모한 사항들 정리한다.  

**[항목45. 지역변수의 유효범위를 최소화하자.]**'
featured_image: ''
tags: ['dev', 'Java', 'forEach', 'for문', 'library', '지역변수의 범위']
---
<span style="font-size: 11pt;">별거는 아니고 Effective 자바 읽으면서 몇가지 메모한 사항들 정리한다.  </span>

**<span style="font-size: 11pt;">[항목45. 지역변수의 유효범위를 최소화하자.]</span>**

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">지역변수의 유효범위를 최소화 하는 가장 강력한 방법은 그 변수가 최초 사용되는 곳에 선언하는 것이다. </span>

<span style="font-size: 11pt;">C언어 스타일의 함수 제일 앞에 변수를 선언하는 방식은 버리자.</span>

<span style="font-size: 11pt;">(사견: 각자의 언어에 맞는 스타일을 쓰자.)</span>

<span style="font-size: 9pt; line-height: 1.5;">  
</span>

<span style="font-size: 11pt; line-height: 1.5;">지역변수의 선언과 초기화에 주의하자. 올바른 초기화가 될때 선언을 하지.</span>

<span style="font-size: 11pt;">While 보다는 for문을 사용하자.</span>

<span style="font-size: 11pt;">메소드를 작고 한가지 일만 하게 한다면 자연스럽게 지역변수의 유효범위는 작아진다.</span>

</div>**<span style="font-size: 11pt;">[항목 46. </span><span style="font-size: 11pt;">for문 보다는 foreach 문을 쓰자.]</span>**

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">성능 저하는 없다</span>

<span style="font-size: 11pt;">여러개의 중첩된 컬렉션에 대해서 반복처리를 할때는 foreach가 더 좋다.</span>

<span style="font-size: 11pt;">Iterable<E> 를 구현한다면 해당 클래스에 대해서 foreach를 쓸수 있다. 이건 해보자.</span>

<span style="font-size: 11pt;">foreach 를 쓸수 없는 세가지 경우</span>

<span style="font-size: 11pt;">필터링</span>

<span style="font-size: 11pt;">변환- 컬렉션 아이템내 값의 변경</span>

<span style="font-size: 11pt;">병행 반복처리 </span>

<span style="font-size: 11pt;">위의 경우라면 일반 for문을 사용하자.</span>

</div>**<span style="font-size: 11pt;">[항목 47. 라이브러리를 사용하고 배우자]</span>**

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">표준 라이브러리르 사용하자. 검증되었다.</span>

<span style="font-size: 11pt;">시간 낭비하지 말자</span>

<span style="font-size: 11pt;">라이브러리는 자동적으로 좋아진다.</span>

<span style="font-size: 11pt;">자바가 새로 나오면 썬 사에 가서</span>

<span style="font-size: 11pt;">[java5-feat] [java6-feat]을 읽자</span>

<span style="font-size: 11pt;">프로그래머라면</span>

<span style="font-size: 11pt;">Java.lang</span>

<span style="font-size: 11pt;">Java.util</span>

<span style="font-size: 11pt;">Java.io</span>

<span style="font-size: 11pt;">패키지에 익숙해져라</span>

<span style="font-size: 11pt;">있는 것을 다시 만들지 말라.</span>

</div>

