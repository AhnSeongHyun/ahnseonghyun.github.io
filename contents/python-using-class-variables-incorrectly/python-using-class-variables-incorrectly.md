---
title: 'Python - 잘못된 클래스 변수의 사용'
author: 'ash84'
pub_date: '2017-05-24'
description: '본 글은 Toptal에 올라온 [Buggy Python Code: The 10 Most Common Mistakes That Python Developers Make](https://www.toptal.com/python/top-10-mistakes-that-python-programmers-make) 글을 보고 공부하면서 쓴 글이다. 번역 + 개인의 공부내용이라고 생각하면 될 것 같다.

**Common Mistake #2: Using class variables incorrectly**

**잘못된 클래스 변수의 사용*'
featured_image: ''
tags: ['dev', 'Python', 'class variable', 'toptal']
---

본 글은 Toptal에 올라온 [Buggy Python Code: The 10 Most Common Mistakes That Python Developers Make](https://www.toptal.com/python/top-10-mistakes-that-python-programmers-make) 글을 보고 공부하면서 쓴 글이다. 번역 + 개인의 공부내용이라고 생각하면 될 것 같다.
<hr/>
**Common Mistake #2: Using class variables incorrectly**

**잘못된 클래스 변수의 사용** 

```python
class A(object):
    x = 1

class B(A):
    pass

class C(A):
    pass

print A.x, B.x, C.x // 1 1 1 

B.x = 2
print A.x, B.x, C.x // 1 2 1 

A.x = 3
print A.x, B.x, C.x // 3 2 3 
```

`A.x` 만 변경했는데 왜 `C.x` 가 변경되었을까? 파이썬에서, 클래스 변수는 내부적으로 dictionary 로 처리되고  [Method Resolution Order(MRO) ](http://python-history.blogspot.kr/2010/06/method-resolution-order.html)규칙을 따른다. 위의 코드에서, C 클래스에 x 가 없기 때문에, base 클래스에서 찾아진다(Python 이 다중상속을 지원하더라도 오직 A). 다시 말하자면, C 클래스는 A 클래스와 별개로 x 를 자기자신이 가지고 있지 않다. 그러므로 `C.x` 의 레퍼런스는 `A.x` 이다. 이것을 제대로 처리 하지 않으면 문제가 발생한다. [class attributes in Python](https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide)를 좀 더 살펴보도록 하자. 

