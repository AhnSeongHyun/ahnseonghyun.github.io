---
title: 'Python - 파이썬 범위 규칙에 대한 잘못된 이해'
author: 'ash84'
pub_date: '2017-06-01'
description: ''
featured_image: ''
tags: ['dev', 'Python', 'scope', 'UnboundLocalError']
---

 
본 글은 Toptal에 올라온 [Buggy Python Code: The 10 Most Common Mistakes That Python Developers Make](https://www.toptal.com/python/top-10-mistakes-that-python-programmers-make) 글을 보고 공부하면서 쓴 글이다. 번역 + 개인의 공부내용이라고 생각하면 될 것 같다.
<hr/>
**Common Mistake #4: Misunderstanding Python scope rules**

**파이썬 범위 규칙에 대한 잘못된 이해**

파이썬 범위 해석은 [LEGB](https://blog.mozilla.org/webdev/2011/01/31/python-scoping-understanding-legb/)(**L**ocal, **E**nclosing, **G**lobal, **B**uilt-in)에 기초하고 있다고 알려져 있다. 충분히 직설적인것 같은데? 실제로 파이썬에서 작동하는 방식에는 약간의 미묘한 차이가 있
다. 

아래를 보면:
```python 
>>> x = 10
>>> def foo():
...     x += 1
...     print x
...
>>> foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in foo
UnboundLocalError: local variable 'x' referenced before assignment
```

무엇이 문제일까? 위의 코드는 에러가나는데, 이유는 범위 내에서 변수에 할당을 할때 변수는 자동적으로 파이썬에 의해서 그 범위에서의 로컬 변수로 간주되어 진다.(컴파일러가 로컬변수로 인지한다.) 그래서 `UnboundLocalError` 가 발생한다. 

lists 를 사용할때 더 이상한데, 아래의 예를 살펴보자:

```python 

lst = [1, 2, 3]
def foo1():
    lst.append(5)
foo1()
print lst

def foo2():
    lst +=[5]

foo2()
...
[1, 2, 3, 5]
Traceback (most recent call last):
  File "cm_4.py", line 19, in <module>
    foo2()
  File "cm_4.py", line 16, in foo2
    lst +=[5]
UnboundLocalError: local variable 'lst' referenced before assignment

```

왜 `foo2`는 문제가 있는데 `foo1`은 잘될까? 

그 이유는 이전 예제의 문제와 동일하지만, 좀 더 미묘한 부분이 있다. `foo1` 은 `lst` 에 할당을 하지 않지만, `foo2`는 할당을 하고 있다. `lst += [5]` 는 실제로 `lst = lst + [5]` 의 단축형이라는 것을 알면, `lst`에 값을 할당하려고 시도하고 있는 것이다. 그러나 `lst`에 할당하고자 하는 값은 아직 정의되지 않은 `lst`를 기반으로 한다. 

<hr>
> 역자주 : 이번 글은 좀 번역이 망했는데, 중요한 것은 **할당 시점에 컴파일러가 로컬변수로 간주한다**는 점인것 같다. outer scope 의 값을 가져오기 위해서는 `global` 변수를 사용하면 된다. 


**Reference**

- [Why am I getting an UnboundLocalError when the variable has a value?](https://docs.python.org/2/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value)
