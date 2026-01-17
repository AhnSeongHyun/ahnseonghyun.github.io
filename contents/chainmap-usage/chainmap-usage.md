---
title: ' ChainMap 사용법 정리'
author: 'ash84'
pub_date: '2018-07-13'
description: 'Python3.3 에서 처음 나온  ChainMap 은 익히 잘 알고 있는 collections 모듈에 위치해 있다. 3.3 에 나왔지만, 생각보다 많이 알려지지 않은 이유는 기존의 다른 방식의 코딩으로 대체가능한 영역이라서 인것 같다. ChainMap의 기본적인 역할은 quickly linking a number of mappings 이라고 소개하고 있다. 

즉, 맵핑 형식을 이어주는 역할로 보면 될 것 같다. 그리고 dict 를 새로 생성하거나 여러번 `update()` 함수를 호출하는것 보다 빠르다고 설명하고 있다. 간단히'
featured_image: ''
tags: ['Python', 'chainmap', 'tutorial']
---
Python3.3 에서 처음 나온  ChainMap 은 익히 잘 알고 있는 collections 모듈에 위치해 있다. 3.3 에 나왔지만, 생각보다 많이 알려지지 않은 이유는 기존의 다른 방식의 코딩으로 대체가능한 영역이라서 인것 같다. ChainMap의 기본적인 역할은 quickly linking a number of mappings 이라고 소개하고 있다. 

즉, 맵핑 형식을 이어주는 역할로 보면 될 것 같다. 그리고 dict 를 새로 생성하거나 여러번 `update()` 함수를 호출하는것 보다 빠르다고 설명하고 있다. 간단히 설명하면 ChainMap 은 기존의 list 안에 dict 을 넣고 for 문을 돌려서 무엇인가를 찾거나 update 하거나 했던 일들을 쉽게 해준다.


```python
>>> from collections import ChainMap
>>> ChainMap()
ChainMap({})
>>> ChainMap() # 아무것도 넣지 않으면 빈 채로 반환 

>>> default = {'db':'127.0.0.1', 'port':3306}
>>> custom = {'db':'ash84.net', 'port':3306, 'lib':'pymysql'}
>>> ChainMap(default, custom)
ChainMap({'db': '127.0.0.1', 'port': 3306}, {'db': 'ash84.net', 'port': 3306, 'lib': 'pymysql'})

>>> chain_map.maps # 전달된 mappings 들은 list 에 저장되고 maps 를 통해서 접근가능
[{'db': '127.0.0.1', 'port': 3306}, {'db': 'ash84.net', 'port': 3306, 'lib': 'pymysql'}]

# 조회는 키가 발견될때 까지 연속적으로 찾는다. 
## 반대로 쓰기, 업데이트, 삭제는 오직 첫번째 mappings 에서만 이루어진다. 

>>> for k, v in chain_map.items():
...   print(k, v)
... 
port 3306
db 127.0.0.1
lib pymysql

>>> chain_map['port']=33306
>>> chain_map
ChainMap({'db': '127.0.0.1', 'port': 33306}, {'db': 'ash84.net', 'port': 3306, 'lib': 'pymysql'})

## new_child 사용법 

>>> chain_map.new_child(m=1)
ChainMap(1, {'db': '127.0.0.1', 'port': 33306}, {'db': 'ash84.net', 'port': 3306, 'lib': 'pymysql'})
>>> chain_map.new_child(m="test")
ChainMap('test', {'db': '127.0.0.1', 'port': 33306}, {'db': 'ash84.net', 'port': 3306, 'lib': 'pymysql'})
>>> chain_map.new_child(m="test").maps
['test', {'db': '127.0.0.1', 'port': 33306}, {'db': 'ash84.net', 'port': 3306, 'lib': 'pymysql'}]

## new_child(m) 함수는 m 값을 주지 않을 경우 {} 를 .maps 내 첫번째에 위치시키고 
## 기존의 가지고 있던 다른 mappings 들을 복사한다. 
## m 을 주어지면 해당 값을 maps 에 첫번째에 넣고 나머지 복사 

## parents 사용법 
## 제일 첫번째것을 제외한 나머지 것들을 새로운 ChainMap 으로 만들어서 반환 
>>> chain_map
ChainMap({'db': '127.0.0.1', 'port': 33306}, {'db': 'ash84.net', 'port': 3306, 'lib': 'pymysql'})
>>> chain_map.parents
ChainMap({'db': 'ash84.net', 'port': 3306, 'lib': 'pymysql'})

## 검색단계에서 첫번째 mappings 를 제외할때 편함 

## 예 https://www.blog.pythonlibrary.org/2016/03/29/python-201-what-is-a-chainmap/

>>> from collections import ChainMap
>>> car_parts = {'hood': 500, 'engine': 5000, 'front_door': 750}
>>> car_options = {'A/C': 1000, 'Turbo': 2500, 'rollbar': 300}
>>> car_accessories = {'cover': 100, 'hood_ornament': 150, 'seat_cover': 99}
>>> car_pricing = ChainMap(car_accessories, car_options, car_parts)
>>> car_pricing['hood']
500
```

특이한 점이 몇가지가 있는데, 업데이트는 첫번째 mapping 을 대상으로만 이루어진다는 점이다. 그런데 조회를 할때, 해당 키가 첫번째에 없으면 다음번 mapping 대상에서 찾아서 보여준다는 점이다. `new_child` 함수는 특이하게 ChainMap 이라서 mapping 형식만 인자를 통해서 받을 수 있을것처럼 보이지만 아무 값이나 넣어서 첫번째에 위치 시켜버린다. `parents` 는 뭔가 부모 mapping 객체를 찾을 것 처럼 보이지만 사실은 maps 리스트의 첫번째 것을 제외한 나머지를 새로운 ChainMap 으로 만든다. 

어디에 써 먹을지는 잘 모르겠지만, 제일 마지막에 있는 예제를 보면 키가 겹치지 않는다는 가정의 dict 들에서 통합해서 찾고 싶으면 기존의 `update` 를 통해서 합치고 찾았던 거에 비해서,  ChainMap 으로 연결하고 한번에 원하는 키를 통해서 찾을 수 있는건 편할 것 같다. 
 
