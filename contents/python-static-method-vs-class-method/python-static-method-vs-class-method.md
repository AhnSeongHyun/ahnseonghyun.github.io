---
title: 'python static method vs. class method'
author: 'ash84'
pub_date: '2022-08-21'
description: '사내에서 파이썬 코드를 짜다보면 static method와 class method를 혼용해서 사용하는 경우가 개인별로 있었는데 이 부분에 대해서 개인적으로 조사를 해서 전달할 기회가 있었다. 파이썬 책도 많이 봤고, 공식 레퍼런스도 봤지만 대부분 사용법에 대해서 애기가 대체로 있고, 언제 두개를 구분해서 사용해야하는 지에 대해서는 나와있지 않아서 몇개의 레퍼런스를 정리해봤다. 

### [파이썬 코딩의 기술, 108p](http://www.yes24.com/Product/Goods/94197582)

파이썬에는 클래스별로 생성자를'
featured_image: ''
tags: ['Python', 'dev', 'Class', 'static method', 'class method']
---

사내에서 파이썬 코드를 짜다보면 static method와 class method를 혼용해서 사용하는 경우가 개인별로 있었는데 이 부분에 대해서 개인적으로 조사를 해서 전달할 기회가 있었다. 파이썬 책도 많이 봤고, 공식 레퍼런스도 봤지만 대부분 사용법에 대해서 애기가 대체로 있고, 언제 두개를 구분해서 사용해야하는 지에 대해서는 나와있지 않아서 몇개의 레퍼런스를 정리해봤다. 

### [파이썬 코딩의 기술, 108p](http://www.yes24.com/Product/Goods/94197582)

파이썬에는 클래스별로 생성자를 한 개만 만들수 있다.( `__init__ `)
클래스에 필요한 다른 생성자를 정의하려면 `@classmethod`를 사용하자. 
구체(concrete) 서브 클래스를 만들고 연결하는 범용적인 방법을 제공하려면 클래스메소드의 다형성을 이용하자. 

### [Fluent Python, 328p](http://www.yes24.com/Product/Goods/30231768)

class method는 대안 생성자를 구현하기 위해서 주로 사용된다.
본질적으로 static method는 클래스 본체 안에 정의된 평범한 함수일 뿐이다?
* 저자생각 - static method는 왜 쓰는지 모르겠다. 클래스와 함께 작동하지 않는 함수를 정의하려면 단지 함수를 모듈에 정의하면 된다.  함수가 클래스를 건드리지 않지만 클래스와 연관이 있어서 클래스 가까이 두고 싶을수는 있을것이다. 그런 경우에는 클래스의 바로 앞이나 뒤에 함수를 정의하면 된다. 

### ****[The definitive guide on how to use static, class or abstract methods in Python](https://julien.danjou.info/guide-python-static-class-abstract-methods/)****

* Fluent Python의 technical reviewer, Leonardo Rochael 

**static method** 

- 바운드 메소드(인스턴스메소드를 사용할 수 있는 상태) 도 객체이기에 이것도 비용이 든다.
- static method를 사용하면 가독성 측면에서 좋다. (객체의 상태에 의존하지 않는다는 것을 알려준다.)

**class method**

- factory method 로서의 활용
- static method를 사용할 수 있지만 상속 객체생성시 클래스명이 하드 코딩 되기 때문에 상속에서 사용할 수가 없다.
- 하나의 static method에서 여러개의 static method를 호출하는 경우, class method를 써야한다. 왜냐하면 상속시의 클래스 명 하드코딩으로 인한 문제가 발생할 수 있다.

## 🧐 개인적인 생각

- 개인적으로는 Fluent Python의 저자의 생각과 비슷하다.
- static method를 사용함에 있어서 항상 고민되는 것은 호출시 dot을 통해서 연결이 되어서 가독성이 좋아지는 정도인데, 그건 적절한 class에 추가했을 때인것 같다. 애매하면 함수가 낫지 않을까 싶다.
- 개인적인 생각과는 다르게 사내에서 이번 기회에 정한 규칙은
    - 다른 생성자를 만들 때, class method를 사용한다.
    - 그 외는 static method를 사용하되, nested static method에서는 class method를 사용한다.
    

ps) 이번기회에 스스로 몰랐던 것을 알게 되어서 너무 좋다. 알고서 잘 짜는건 어렵다.
