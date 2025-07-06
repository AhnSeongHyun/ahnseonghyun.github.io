---
title: '[JAVA] 자바에서 싱글턴 패턴을 구현하는 세 가지 방식들.'
author: 'ash84'
pub_date: '2015-07-03'
description: '안티패턴임에도 불구하고, 자주 쓰게 되는 패턴중 하나가 싱글턴 패턴인데, 멀티스레드에 취약하다는 문제점을 가지고 있으면서도 선택된 데이터나 현재 데이터만을 표현할때 좋은것 같다. 이전 포스팅에서도 [H](http://ash84.tistory.com/762) [ashtable 을 이용한 로컬 캐쉬 소스](http://ash84.tistory.com/762)에서도 싱글턴을 썼는데 이번에 이펙티브 자바를 읽으면서 싱글톤에 대한 이야기가 나와서 정리하고자 한다. 

<'
featured_image: ''
tags: ['dev', 'Java', 'Single ton', '디자인패턴', '싱글톤패턴']
---


<span style="font-size: 11pt; ">안티패턴임에도 불구하고, 자주 쓰게 되는 패턴중 하나가 싱글턴 패턴인데, 멀티스레드에 취약하다는 문제점을 가지고 있으면서도 선택된 데이터나 현재 데이터만을 표현할때 좋은것 같다. 이전 포스팅에서도 [H](http://ash84.tistory.com/762) [ashtable 을 이용한 로컬 캐쉬 소스](http://ash84.tistory.com/762)에서도 싱글턴을 썼는데 이번에 이펙티브 자바를 읽으면서 싱글톤에 대한 이야기가 나와서 정리하고자 한다. </span>

<span style="font-size: 11pt; ">가장 기본적인 형태이다. </span>

<script src="https://gist.github.com/3918482.js"></script>

<span style="font-size: 11pt; ">**public static 인스턴스를 만드는 방식이다.** private 생성자로부터 인스턴스가 만들어 지고 final 키워드에 의해서 한번만 초기화가 된다. 이 코드의 장점은 간단하는 점이다. 그런데 조금 유연하지 못한 부분이 있다. </span>

<span style="font-size: 11pt; ">**두번째 방식은 private static final 인스턴스를 만드는 방식이다.** 그렇다면 만들어진 객체를 어떻게 리턴할까? static method를 통해서 생성된 인스턴스를 반환하게 하고 있다. 사실 이 방식이 static factory 메소드에서 다른 여타의 작업들을 하나밖에 없는 객체이지만, 객제가 반환되는 시점에 다른 작업을 추가할 수 있다는 장점이 있다.</span>

<span style="font-size: 11pt; "> </span>

<script src="https://gist.github.com/3918471.js"></script>

<span style="font-size: 11pt; ">**세번째 방식은 좀 생소한데, class 가 아니라, enum 으로 생성해 버리는 것이다.** 보통 enum은 어떤 모드를 구분하고 지정하기 위해서 사용되는데, 이렇게 함수를 가지고 있을수 있다는 것은 처음 알았다. 가장 큰 장점은 단연 serialization 할 경우에 두번째 방식에서는 여타의 작업들을 해주어야만 하나의 객체가 유지되는데, enum 방식은 그럴 필요가 없다는 것이다. </span>

<script src="https://gist.github.com/3918487.js"></script>

<span style="font-size: 11pt; ">원래 싱글턴을 만드는 방식은 여기에는 안 나와있는데, 하나의 인스턴스를 처음에 요청하면 만들고, 그 인스턴스가 null 인지를 다음 요청이 들어올때 체크해서 null 이 아니면 이전에 생성한 것을 반환하는 형태로 많이 사용되었는데, 이러한 방식의 코드의 단점은 멀티 스레드 환경에서 교묘한 시점에 객체가 1개 이상이 반환될 여지가 있다는 점이다. </span>

<span style="font-size: 11pt; ">주의해서 사용하자. </span>



