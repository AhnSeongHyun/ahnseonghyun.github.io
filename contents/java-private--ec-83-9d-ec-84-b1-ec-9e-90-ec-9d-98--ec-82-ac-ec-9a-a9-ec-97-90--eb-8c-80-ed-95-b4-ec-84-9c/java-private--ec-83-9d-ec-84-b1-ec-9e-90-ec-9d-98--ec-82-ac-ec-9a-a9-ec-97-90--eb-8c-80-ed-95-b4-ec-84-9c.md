---
title: '[JAVA] private 생성자의 사용에 대해서.'
author: 'ash84'
pub_date: '2015-07-03'
description: '필자는 데이터 클래스라는 것을 많이 만들어쓰는 편인다. List나 Hashtable 의 변수에 이름을 주는 것 보다 클래스와 멤버에 이름을 줌으로써 좀 더 의미를 명확하게 표현할 수 있기 때문에 자주 사용하는 편이다. 데이터 클래스들의 경우 사실상 클래스에서 행동이라고 하는게 set, get 과 같은 정도의 것 밖에 없는 경우가 많다. 다음의'
featured_image: ''
tags: ['AssertionError', 'date class', 'dev', 'Java', 'private 생성자']
---


<span style="font-size: 11pt;">필자는 데이터 클래스라는 것을 많이 만들어쓰는 편인다. </span><span style="font-size: 11pt;">List나 Hashtable 의 변수에 이름을 주는 것 보다 클래스와 멤버에 이름을 줌으로써 좀 더 의미를 명확하게 표현할 수 있기 때문에 자주 사용하는 편이다. </span><span style="font-size: 11pt;">데이터 클래스들의 경우 사실상 클래스에서 행동이라고 하는게 set, get 과 같은 정도의 것 밖에 없는 경우가 많다. 다음의 케이스를 보자. </span>

<span style="font-size: 11pt;"></span>

<script src="https://gist.github.com/4152877.js"></script>

<span style="font-size: 11pt;">나는 한자와 한글을 담는 데이터 클래스를 만들었다. 그리고 이것이 여러개 있는것이 있는 리스트를 만들고 싶다. 그럴 경우 아래와 같이 사용한다. </span>

<span style="font-size: 11pt;"></span>

<script src="https://gist.github.com/4152895.js"></script>

<span style="font-size: 11pt;">좀더 줄여보면 아래와 같이 사용하는 편이 더 간단한것이라고 생각된다. </span>

<span style="font-size: 11pt;"></span>

<script src="https://gist.github.com/4152899.js"></script>

<span style="font-size: 11pt;">이렇게 사용될 경우, 당연히 생성자 오버로딩을 해야하며, 사실상 생성된 오버로딩만 해당 케이스를 통해서 사용될 경우가 많다. 생성자 오버로딩이 된다면 실질적으로 멤버필드들의 set 메소드를 필요 없게 된다. 이것은 set 은 오버로딩된 생성자를 통해서만 하겠다는 무언의 약속인 것이다. </span>

<script src="https://gist.github.com/4152942.js"></script>

<span style="font-size: 11pt;">이럴경우, 가장 중요한 부분은 바로 기본 생성자에 대한 **private 생성자 처리**이다. private 생성자를 쓰지 않으면 아무 값도 들어가지 않은 생성자가 생겨나게 된다. 문제는 set 함수가 없기 때문에 값을 지정할 수가 없다. 때문에 private 생성자를 써서 컴파일 시점에서 개발자가 기본 생성자로 객체를 만드는 것을 막아야한다. </span>

<span style="font-size: 11pt;">왜 이렇게 사용하는가에 대한 의문이 있을수 있겠지만, 사실 이것은 Hanja 클래스를 데이터 클래스로 쓰겠다는 용도와 생성시에만 값을 넣게 하겠다는 정책의 결과이다. 그렇지만 은근히 이렇게 데이터 클래스를 만들어 사용하는 경우가 많기 때문에 이런 경우 private 생성자를 써주길 바란다. </span>



