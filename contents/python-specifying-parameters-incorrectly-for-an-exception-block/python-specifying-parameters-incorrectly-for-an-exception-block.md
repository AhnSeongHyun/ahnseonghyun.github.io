---
title: 'Python - 예외처리 블록에 대한 잘못된 파라미터 지정'
author: 'ash84'
pub_date: '2017-05-25'
description: '본 글은 Toptal에 올라온 [Buggy Python Code: The 10 Most Common Mistakes That Python Developers Make](https://www.toptal.com/python/top-10-mistakes-that-python-programmers-make) 글을 보고 공부하면서 쓴 글이다. 번역 + 개인의 공부내용이라고 생각하면 될 것 같다.

**Common Mistake #3: Specifying parameters incorrectly for an exception blo'
featured_image: ''
tags: ['dev', 'Python', 'toptal', 'except', 'try except', 'multiple exception']
---

본 글은 Toptal에 올라온 [Buggy Python Code: The 10 Most Common Mistakes That Python Developers Make](https://www.toptal.com/python/top-10-mistakes-that-python-programmers-make) 글을 보고 공부하면서 쓴 글이다. 번역 + 개인의 공부내용이라고 생각하면 될 것 같다.
<hr/>
**Common Mistake #3: Specifying parameters incorrectly for an exception block**

**예외처리 블록에 대한 잘못된 파라미터 지정**


```python
try:
    l = ["a", "b"]
    int(l[2])
except ValueError, IndexError: # To catch both exceptions, right?
    pass
```

위의 코드에서의 문제는 `except` 단계에서 리스트 관련 예외처리가 걸려들지 않는다.(역자 : `IndexError` 에 `l[2]` 가 걸려질것이라고 생각하고 코드를 구현했기에.) Python2.x 상에서 `except Exception, e` 구문은 예외처리를 위해서 사용되어 지는데 추가적인 조사가 가능하게 하기 위해서 옵션인 두번째 파라미터를 지정한다(`e`)

결과적으로, 위의 코드에서 `IndexError` 예외는 `except` 에 걸리지 않는다; 대신에 `IndexError`은 매개변수에 바인딩이 된다. (역자 : ValueError as IndexError 가 되는것으로 IndexError 가 변수로 바인딩 된다.

예를 들어, 아래의 코드를 보면
```python 
try:
    l = ["a", "b"]
    int(l[2])
except IndexError, ValueError :
    print ValueError
    pass
```

`IndexError`가 `except`에서 잡혀지는데, ValueError 를 print 해보면, list index out of range
라고 나온다. 즉 IndexError, ValueError 는 IndexError, e 에서 e 대신에 ValueError가 변수로 바인딩 된 것이다.) 


`except` 구문에서 다중 예외처리를 하는 적절한 방법은 첫번째 파라미터를 모든 예외가 포함된 `tuple`로 지정하는 것이다. 또한, 높은 이식성을 위해서 `as` 키워드를 사용하면 Python2 와 Python3을 모두 지원할 수 있다:

```python
try:
    l = ["a", "b"]
    int(l[2])
except (IndexError, ValueError) as e:
    pass
```

