---
title: '(Java) 상수 인터페이스 패턴'
author: 'ash84'
pub_date: '2013-02-06'
description: ''
featured_image: ''
tags: ['dev', 'Interface', 'Java', 'design-pattern', '상수 인터페이스 패턴', '안티 패턴', '인터페이스']
---
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script> 

Effective Java 에 나왔던 내용이라서 정리한다. 잘 쓰는 패턴이 아닌 쓰지말라는 패턴을 정리하긴 처음인데, 정리하면 다음과 같다. 

**상수 인터페이스 패턴**

일종의 안티패턴이다. 기본적으로 인터페이스는 클래스가 해야하는 일을 정의해야하는 것이 목적상 역할이 맞는데, 상수 인터페이스 패턴은 인터페이스에 메소드가 없이 static final 상수만이 존재하는 인터페이스를 지칭한다. 문제는 구현 클래스가 구현시 해당 상수가 이미 인터페이스에 정의되어 있어서 클래스 내부에서 같은 이름의 상수를 쓸수가 없는 문제가 있다는 것이다. 그리고 상수는 클래스 내에 둠으로써 의미를 부여하는 것이 맞다. 

그렇다면, 상수를 외부에 공개하고 싶을때는 어떻게 해야할까?

> 1) enum 타입으로 정의 

> 2) 인스턴스를 생성할 수 없는(private 생성자) 유틸리티 클래스 정의 


요약하자면,  인터페이스는 타입을 정의할때만 사용해야 하며 상수를 외부에 제공하기 위해서는 사용해서는 안된다.
