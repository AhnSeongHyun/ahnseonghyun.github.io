---
title: 'Python - 리스트 순회중 수정하는 문제'
author: 'ash84'
pub_date: '2017-06-06'
description: '본 글은 Toptal에 올라온 [Buggy Python Code: The 10 Most Common Mistakes That Python Developers Make](https://www.toptal.com/python/top-10-mistakes-that-python-programmers-make) 글을 보고 공부하면서 쓴 글이다. 번역 + 개인의 공부내용이라고 생각하면 될 것 같다.



**Common Mistake #5: Modifying a list while iterating over it**

**리스트 순회'
featured_image: ''
tags: ['dev', 'Python', 'toptal', 'Modifying a list while iterating over it']
---

본 글은 Toptal에 올라온 [Buggy Python Code: The 10 Most Common Mistakes That Python Developers Make](https://www.toptal.com/python/top-10-mistakes-that-python-programmers-make) 글을 보고 공부하면서 쓴 글이다. 번역 + 개인의 공부내용이라고 생각하면 될 것 같다.

<hr/>

**Common Mistake #5: Modifying a list while iterating over it**

**리스트 순회중 수정하는 문제**

```python
>>> odd = lambda x : bool(x % 2)
>>> numbers = [n for n in range(10)]
>>> for i in range(len(numbers)):
...     if odd(numbers[i]):
...         del numbers[i]  # BAD: Deleting item from a list while iterating over it
...
Traceback (most recent call last):
  	  File "<stdin>", line 2, in <module>
IndexError: list index out of range
```

순회중인 리스트 혹은 배열에서 아이템을 삭제하는것은 어느 경험있는 개발자에게나 잘 알려진 문제이다. 그러나 위의 코드에서는 문제가 명백하지만, 숙련된 개발자들도 더 복잡한 코드에서 예기치 못하게 걸려들 수도 있다. 

위의 코드를 단순화 시켜서 순회중인 리스트안에서의 삭제 문제를 좀 더 적게 걸리게 할 수 있다. 그러한 방식중에 하나가 리스트 축약(list comprehension) 이다. 

```python 
>>> odd = lambda x : bool(x % 2)
>>> numbers = [n for n in range(10)]
>>> numbers[:] = [n for n in numbers if not odd(n)]  # ahh, the beauty of it all
>>> numbers
[0, 2, 4, 6, 8]
``` 
<hr/>

> 역자주 : 원문에서도 나와 있듯이 `잘 알려진` 문제인데, 처음 자바 개발할 때 [fail-fast iterator](http://happystory.tistory.com/33) 라는 개념에 대해서 배우면서 알게 되었던 것 같다. 리스트 축약을 통해서 구현한 2번째 코드에서 `numbers[:]` 를 통해서 원래 numbers 를 replace 한다는 점이 중요한 것 같다. 


**Reference**

- [What does list[:] = […] do in Python](https://stackoverflow.com/questions/32448414/what-does-list-do-in-python)
- [fail-fast iterator java](http://happystory.tistory.com/33)
