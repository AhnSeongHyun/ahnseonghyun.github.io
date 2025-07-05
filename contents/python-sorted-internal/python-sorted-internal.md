---
title: 'python sorted 에 대해서.'
author: 'ash84'
pub_date: '2018-05-18'
description: ''
featured_image: 'https://images.unsplash.com/photo-1460058418905-d61a1b4a55fe?ixlib=rb-0.3.5&s=a8b0de48d09d5f907d871be8b775b5b3&auto=format&fit=crop&w=889&q=80'
tags: ['dev', 'Python', 'sorted', 'list.sort()']
---

sorted 에 대해서 질문을 받았고 잘 대답을 하지 못해서 복기차원에서 이 글을 쓴다. 대부분의 내용은 [Sorting HOW TO](https://docs.python.org/3/howto/sorting.html) 라는 글에서 가져왔음을 밝힌다. 
<hr>

### list.sort() vs sorted()
- `list.sort()` 는 리스트 내부에서 정렬된다. 그에 비해 `sorted()` 는 정렬된 값을 돌려준다. 그렇기 때문에 원래 값을 유지하면서 정렬된 결과를 얻고 싶다면 `sorted()` 를 사용하면 된다. `list.sort()` 는 값을 돌려주지 않기 때문에 받게 되면 None 을 받게 된다. 

- `list.sort()` 는 리스트 형에 한해서만 동작하지만, `sorted()` 는 iterable(순회가능) 한 자료형에 대해서 동작한다. 

```python
>>> sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
[1, 2, 3, 4, 5]
```

### Key Functions 
-  둘 다 `key` 파라미터를 가지고 있는데, 비교를 하는 기준으로 사용된다. 

```python
>>> sorted("This is a test string from Andrew".split(), key=str.lower)
['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
```

- `key` 파라미터는 함수여야 하고, 하나의 입력값과 반환값을 가진다. 
- key 파라미터로 전달된 함수는 입력 레코드마다 한번씩 호출되어진다. 
- 일반적 패턴은 클래스나 복잡한 객체들을 정렬할 때 사용한다. 

```python
>> student_objects = [
...     Student('john', 'A', 15),
...     Student('jane', 'B', 12),
...     Student('dave', 'B', 10),
... ]
>>> sorted(student_objects, key=lambda student: student.age)   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

### Operator Module Functions

- 파이썬에서 좀더 편하게 사용할수 있는 접근자 함수를 제공하고 있음. 
- operator 모듈의 `itemgetter()`, `attrgetter()`, `methodcaller()`

```python 
>>> from operator import itemgetter, attrgetter
>>> sorted(student_tuples, key=itemgetter(2))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
>>> sorted(student_objects, key=attrgetter('age'))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
>>> sorted(student_tuples, key=itemgetter(1,2))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
>>> sorted(student_objects, key=attrgetter('grade', 'age'))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
```

- 위의 예제에서도 볼 수 있듯이 `itemgetter()`, `attrgetter()` 는 복잡한 자료형내(객체나)에 있는 특정 값을 가져오는 함수들이고, 하나 뿐만 아니라 여러개의 값을 가져오게 할 수도 있다. 

- `methodcaller()` 는 말 그대로 어떤 메소드를 호출해 주는 역할을 하는 함수이다. 

```python
>>> from operator import methodcaller
>>> f = methodcaller('name')
>>> class B():
...   def name(self):
...     print("test")
...
>>> b = B()
>>> f(b)
test
```

### Sort Stability and Complex Sorts
- 정렬은 stable 을 지원한다. 
- [stable, unstable 정렬](http://egloos.zum.com/entireboy/v/3516993)은 같은 키의 기준일떄 기존의 순서를 보존하느냐의 차이이다. 

```python
>>> data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
>>> sorted(data, key=itemgetter(0))
[('blue', 1), ('blue', 2), ('red', 1), ('red', 2)]
```

- 위의 코드를 보면 `itemgetter(0)` 를 통해서 키 값을 지정하고 있는데, blue 라는 값이 같은키인데, 처음 들어가 있던 순서 `('blue', 1), ('blue', 2)` 가 정렬후에도 보장되는 것을 볼 수 있다. 

- 내부적으로 Hybrid Algorithm 중 하나인 [Timsort](https://webdev.teledit.com/creditcard_client/general/euc-kr) 알고리즘을 사용하고 있고 이 알고리즘은 데이터셋내 이미 존재하는 순서를 이용하는 이점을 가지고 있다. 
 

Reference 
- [Python sorted 알고리즘 Timsort](https://medium.com/@fiv3star/python-sorted-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-timsort-dca0ec7a08be)
