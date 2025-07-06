---
title: '[JAVA] Comparable 인터페이스 구현'
author: 'ash84'
pub_date: '2015-07-03'
description: '필자는 Comparable 인터페이스를 이용해서 compareTo 함수를 구현하는 것 보다는 사실 Comparator 를 이용해서 정렬에 활용하는 케이스를 자주 사용했었다. (물론 그 안에서 이미 구현되어 있는 기본 클래스의 compareTo()를 사용한다.) 여기서는,** Effective Java** 항목12번에 Comparable 인터페이스의 구현을 고려하자 라는 부분에 대해서 요약해서 정리하고, Watch 클래스를 통해서 시계를 비교하는 compareTo() 함수를 구'
featured_image: ''
tags: ['Comparable', 'CompareTo()', 'dev', 'Effective Java', 'Java', '이펙티브 자바', '자바']
---


<span style="font-size: 11pt;">필자는 Comparable 인터페이스를 이용해서 compareTo 함수를 구현하는 것 보다는 사실 Comparator 를 이용해서 정렬에 활용하는 케이스를 자주 사용했었다. (물론 그 안에서 이미 구현되어 있는 기본 클래스의 compareTo()를 사용한다.) 여기서는,** Effective Java** 항목12번에 Comparable 인터페이스의 구현을 고려하자 라는 부분에 대해서 요약해서 정리하고, Watch 클래스를 통해서 시계를 비교하는 compareTo() 함수를 구현해 보겠다. </span>

<span style="font-size: 11pt;">compareTo()는 비교하는 함수이긴 하지만 equals() 와는 다르고, 자연율([natural ordering](http://stackoverflow.com/questions/5167928/what-is-natural-ordering-when-we-talk-about-sorting), 상식적인 순서)을 고려한다. equals() 함수와 다른점은 동일한지 비교하고, 순서가 같은지도 비교하고, 제네릭 타입을 지원한다는 점이다. </span>

<span style="font-size: 11pt;">**compareTo() 메소드 구현의 보편적 계약**</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">A.compareTo(B) 일때, </span>

<span style="font-size: 11pt;">A < B, return 음수(-)</span>

<span style="font-size: 11pt;">A > B, return 양수(+)</span>

<span style="font-size: 11pt;">A == B, return 0</span>

<span style="font-size: 11pt;">A와 B가 다른 타입이면 ClassCastException</span>

</div><span style="font-size: 11pt;">그 외에도 몇가지 계약이 더 있는데, 필자가 중요하다고 생각하는 것 중 하나는 </span>

<span style="font-size: 11pt;">**(A.compareTo(B) ==0) == (A.equals(B))** 가 되어야 한다는 점이다. 이 부분이 중요한 이유는 compareTo() 를 구현해서 만든 클래스가 객체로 생성되어 Collections 를 구현하는 일반적인 리스트, 집합, 테이블 같은 클래스들에 넣었을 경우, 다르게 동작하기 때문이라고 한다. </span>

<span style="font-size: 11pt;">예를들어, BigDecimal(“1.0”), BigDecimal(“1.0.0”) 을 HashSet과 TreeSet에 각각 넣었을 경우, 어느 쪽에서는 하나의 객체만 들어가고 어느쪽에서는 두개의 객체가 들어갈수 있다고 한다. 이것은 HashSet 과 TreeSet에서 어떤 함수를 기반으로 같은지를 판별하는지에 달려있다고 한다. (</span>[<span style="font-size: 11pt;">일반적으로 Set 인터페이스 구현에서 eauals() 를 사용하는데 TreeSet 만 compareTo() 를 사용한다는.</span>](http://docs.oracle.com/javase/6/docs/api/java/util/TreeSet.html)<span style="font-size: 11pt;">)</span>

<span style="font-size: 11pt;">또한 Comparable<T> 즉, 제네릭을 지원하기 때문에 컴파일 시점에 이미 타입이 결정되고 내부에서 형변환을 할 필요가 없다고한다. 구현시에는 일반적인 숫자형(int, long)은 <,> 로 비교하되, double, float 는 부동소수점 연산시 >,< 로 비교를 하면 compareTo() 함수의 조건을 만족하지 못하기 때문에** Double.compare, Float.compare를 이용하기를 권장**한다고 한다. </span>

<span style="font-size: 11pt;">비교하는 필드가 여러개인 경우, 비교하는 순서가 중요한데, 이 부분은 전적으로 개인이 만든 클래스기 때문에 가장 우선시 되는 필드 부터 비교하고, 같으면 좀 덜 우선시되는 필드를 비교하는 방식으로 진행하면 된다고 한다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">  
</span>

<script src="https://gist.github.com/4129777.js"></script>

<span style="font-size: 11pt;">Watch 클래스에는 다양한 필드가 있다.(접근 지정자는 신경안썼음.) 일단 필자가 생각한 비교의 기준 순서는 **오토매틱의 여부>무브먼트타입>서브 판의 개수>잡다한 기능의 수** 순이다. 다음은 Watch 클래스를 객체화 하고 비교하는 코드이다. </span>

<script src="https://gist.github.com/4129789.js"></script>



