---
title: 'Python - 함수 디폴트인자의 잘못된 사용'
author: 'ash84'
pub_date: '2017-05-25'
description: '본 글은 Toptal에 올라온 [Buggy Python Code: The 10 Most Common Mistakes That Python Developers Make](https://www.toptal.com/python/top-10-mistakes-that-python-programmers-make) 글을 보고 공부하면서 쓴 글이다. 번역 + 개인의 공부내용이라고 생각하면 될 것 같다. 

**Common Mistake #1: Misusing expressions as defaults for function arguments**'
featured_image: ''
tags: ['Python', 'toptal', 'mutable', 'immutable', 'function argument', 'python function argument type', 'dev']
---


본 글은 Toptal에 올라온 [Buggy Python Code: The 10 Most Common Mistakes That Python Developers Make](https://www.toptal.com/python/top-10-mistakes-that-python-programmers-make) 글을 보고 공부하면서 쓴 글이다. 번역 + 개인의 공부내용이라고 생각하면 될 것 같다. 

**Common Mistake #1: Misusing expressions as defaults for function arguments**

**함수 디폴트인자의 잘못된 사용**

```python 
def foo(bar=[]):
    bar.append("baz")
    return bar

print foo()
print foo()
print foo()
```

보통 이렇게 쓰는 이유는 함수 bar 에서 옵션으로 초기값으로 빈 리스트를 주기 위함이다. 그런데 위의 예저에서처럼 수행하게 되면 우리가 예상할 때는 ['baz'] 가 3번 나와야 하는데 실제로는 아래와 같이 출력된다. 

이러는 이유는 ==**함수의 디폴트 인자는 함수가 정의되는 시점에 오직 한번만 평가된다고 한다.**==(생성 된다는게 맞을듯) 그렇기 때문에 처음에 foo 함수가 정의될때 bar에 빈 리스트가 생성/할당된다. foo() 로 함수가 호출되는 시점에는 bar 는 이미 리스트가 가지고 있기 때문에 계속 baz 값이 들어가게 된다. 

```
>>> foo()
["baz"]
>>> foo()
["baz", "baz"]
>>> foo()
["baz", "baz", "baz"]
```

아래와 같이 None 으로 주고 내부적으로 None 을 체크해서 빈 리스트로 재할당 해주면된다. 

```python 
def foo(bar=None):
    if not bar:
        bar = []
    bar.append("baz")
    return bar
```

이 문제는 리스트냐 아니냐의 문제가 아니라, ==디폴트 값의 형식이 mutable, immutable 의 문제가 중요한 부분이다.== 
Pycharm 을 사용하는 개발자라면 `Default argument value is mutable.` 라는 경고(warning)가 노출 되게 된다. 이럴경우 함수 인자를 살펴볼 필요가 있다. 파이썬에서 mutable, immutable type 은 여기를 참고하면 된다.(https://docs.python.org/2/reference/datamodel.html)

> **immutable**: numeric(int, float ..), string, unicode, tuple, frozenset, bytes

> **mutable**: list, dict, set, byte array, class, class instance 


위의 mutable, immutable 형식들을 가지고 다시 테스트를 해보자. 먼저 int 와 string 을 테스트 해보면 immutable 형이라서 3번 다 같은 값이 나오는 것을 확인 할 수가 있다. 

```python
def int_mutable_test():
    def foo_int(bar=0):
        bar+=2
        return bar

    print foo_int()
    print foo_int()
    print foo_int()

def string_mutable_test():
    def foo_string(bar=''):
        bar+='test'
        return bar

    print foo_string()
    print foo_string()
    print foo_string()
```

```
2
2
2
test
test
test
```

`tuple` 이나 `frozenset` 같은 경우, immutable 형이라서 `add()`, `append()` 같은 함수 자체를 제공하고 있지 않다. 사용자가 정의한 클래스에서 `int`나 `string`을 사용하는 경우는 어떠할까? 예를 들면 User 클래스의 level, job 같은 immutable 멤버변수의 경우라면? (~~구현하기 나름이겠지만.~~)

```python
def class_mutable_test():
    class User(object):
        def __init__(self):
            self.level = 0
            self.items = []
            self.job = ''

        def __str__(self):
            return "job : %s, level : %s, items: %s" %(self.job, str(self.level), self.items)

    def level_up(bar=User()):
        bar.level+=1
        bar.job += 'knignt'
        bar.items.append('Sword')
        return bar

    print level_up()
    print level_up()
    print level_up()
```

```
job : knignt, level : 1, items: ['Sword']
job : knigntknignt, level : 2, items: ['Sword', 'Sword']
job : knigntknigntknignt, level : 3, items: ['Sword', 'Sword', 'Sword']
```

사용자 정의 클래스 자체가 mutable 이기 때문에 함수가 정의되고 평가되는 시점에 생성된 `User()` 인스턴스 bar 가 `level_up()` 함수가 실행될 때 마다 재사용되고 있는 것을 확인 할 수 있다. 
