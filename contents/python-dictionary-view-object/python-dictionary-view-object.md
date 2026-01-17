---
title: 'dictionary view object'
author: 'ash84'
pub_date: '2018-07-18'
description: '`dict.keys()`, `values()`, `items()` 과 기존의 python2 와는 다르게 변경 되었다. 기존은 아래와 같이 리스트형을 반환한다. 

```python
    # python2.x
    >>> d = {'a':1, 'b':2}
    >>> keys = d.keys()
    >>> values = d.values()
    >>> items = d.items()
    >>> keys
    ['a', 'b']
    >>> values
    [1, 2]
    >>> items
    [('a''
featured_image: ''
tags: ['Python', 'dict', 'view object']
---
`dict.keys()`, `values()`, `items()` 과 기존의 python2 와는 다르게 변경 되었다. 기존은 아래와 같이 리스트형을 반환한다. 

```python
    # python2.x
    >>> d = {'a':1, 'b':2}
    >>> keys = d.keys()
    >>> values = d.values()
    >>> items = d.items()
    >>> keys
    ['a', 'b']
    >>> values
    [1, 2]
    >>> items
    [('a', 1), ('b', 2)]
```

그리고 반환된 것들은 독립적인 상태로 원래 dictionary 인 `d` 를 수정해도 반영되지 않는다. 

```python
    >>> d['c']=4
    >>> d
    {'a': 1, 'c': 4, 'b': 2}
    >>> keys
    ['a', 'b']
    >>> values
    [1, 2]
    >>> items
    [('a', 1), ('b', 2)]
    >>> type(keys)
    <type 'list'>
    >>> type(values)
    <type 'list'>
    >>> type(items)
    <type 'list'>
```
python3 부터 `keys()`, `values()`, `items()` 는 view objects 를 리턴하는데 이것은 원 dictionary 의 동적인 뷰라고 설명하고 있고, 가장 큰 특징은 원래의 dictionary 내의 키나 값이 변경되면 같이 변경 되게 된다. 

```python
    >>> d = {'a':1, 'b':2}
    >>> keys = d.keys()
    >>> values = d.values()
    >>> items = d.items()
    >>> keys
    >>> dict_keys(['a', 'b'])
    >>> values
    >>> dict_values([1, 2])
    >>> items
    >>> dict_items([('a', 1), ('b', 2)])
    >>> d['c'] = 3
    >>> keys
    >>> dict_keys(['a', 'b', 'c'])
    >>> values
    >>> dict_values([1, 2, 3])
    >>> items
    >>> dict_items([('a', 1), ('b', 2), ('c', 3)])
```

기존의 python2.x 에서 list 형태로 반환되어서 인덱스를 통해서 접근 했던 부분은 이제 에러를 뱉어낸다. 기존의 list 형태로 쓰고 싶으면 `list(keys)` 와 같이 변환을 해주면 된다. 

```python
    >>> keys[0]
    >>> Traceback (most recent call last):
      File "<input>", line 1, in <module>
    TypeError: 'dict_keys' object does not support indexing
    >>> values[0]
    >>> Traceback (most recent call last):
      File "<input>", line 1, in <module>
    TypeError: 'dict_values' object does not support indexing
```

아래와 같이 3가지 연산에 대해서 지원해주고 있다. 

- len(dictview)
- iter(dictview)
- x in dictview

```python
    >>> 'a' in keys
    >>> True
    >>> 3 in values
    >>> True
    >>> items
    >>> dict_items([('a', 1), ('b', 2), ('c', 3)])
    >>> ('a', 1) in items
    >>> True
    >>> 'a' in items
    >>> False
```

pytho2.x 와 다르게 python3 에서는 원 dictionary 에 삽입 혹은 삭제가  `keys()`, `values()`, `items()` 에 영향을 미칠 수 있기 때문에 순회하는 과정에서 삽입/삭제가 일어나게 되면 `RuntimeError` 를 발생 시키거나 순회 실패가 발생할 수도 있다. 

덧) python2 에서도 `dict.viewkeys()`, `dict.viewvalues()`, `dict.viewitems()` 가 존재한다. 

**Reference** 

- [https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects](https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects)
- [https://stackoverflow.com/questions/8957750/what-are-dictionary-view-objects](https://stackoverflow.com/questions/8957750/what-are-dictionary-view-objects)
