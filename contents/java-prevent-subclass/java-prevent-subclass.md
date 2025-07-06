---
title: '[JAVA] 서브클래싱을 막는 방법'
author: 'ash84'
pub_date: '2016-06-22'
description: '서브클래싱(subclassing)을 막는 두가지 방법

**1. class에 final 키워드로 두기**

– 다음과 같이 public final class 로 두게 되면, extends가 되지 않는다. 


**2. 모든 생성자를 private 로 두고 publi'
featured_image: ''
tags: ['dev', 'Final', 'Java', '상속', '서브클래스', '서브클래싱']
---


<span style="font-size: 11pt;">서브클래싱(subclassing)을 막는 두가지 방법</span>

**1. class에 final 키워드로 두기**

<span style="font-size: 11pt; line-height: 2;">– 다음과 같이 public final class 로 두게 되면, extends가 되지 않는다. </span>

<script src="https://gist.github.com/4265837.js"></script>

**2. 모든 생성자를 private 로 두고 public static 으로 생성자 팩토리 메소드 제공.**

<span style="font-size: 11pt; line-height: 2;">– 1번 방법보다 좀더 유연한 방법이라고 한다. 유연한 이유는 Effective Java를 읽어보심이.(항목 1)</span>

<script src="https://gist.github.com/4265899.js"></script>

<span style="font-size: 11pt; line-height: 2;">서브클래싱을 막는 이유는 지금은 내가 쓸때는 서브클래싱을 안하는데 라고 생각하지만, 만약 다른 사람이 쓴다고 생각하면, 사실 어떻게 쓸지 모르기 때문에 코드를 통해서 사용을 제한하는 것이다. </span>



