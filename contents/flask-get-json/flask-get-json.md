---
title: '(flask) JSON 데이터 받기 및 예외처리'
author: 'ash84'
pub_date: '2016-12-06'
description: 'flask 에서 json 데이터를 받아서 처리할 때 reqeust.get_json() 혹은 request.json 을 이용할 수 있는데, mime type을 application/json 타입으로 보내는데, {} 없이 빈 JSON 문자열 조차도 안 보내는 경우가 있을수가 있다. 


```python
from flask import Flask
from flask import request 
app = Flask(__name__)

@app.route("/test", methods=['POST'])
def test():
    pri'
featured_image: ''
tags: ['dev', 'FLASK', 'Python', 'get_json()', 'on_json_loading_failed']
---

flask 에서 json 데이터를 받아서 처리할 때 reqeust.get_json() 혹은 request.json 을 이용할 수 있는데, mime type을 application/json 타입으로 보내는데, {} 없이 빈 JSON 문자열 조차도 안 보내는 경우가 있을수가 있다. 


```python
from flask import Flask
from flask import request 
app = Flask(__name__)

@app.route("/test", methods=['POST'])
def test():
    print request.json #request.get_json()
    return "Hello World!"

```

이런 경우 flask 에서는 400 bad request 를 응답값으로 보낸다. 보내는 이유는 parsing fail이 발생하고 `on_json_loading_failed(e)` 함수가 실행되게 된다. 이 함수는 JSON Decode 실패 시 400 Bad Request를 보내느 것이 기본 구현으로 되어 있다. JSON parsing fail 이 나더라도 400 Bad Request 외의 다른 행동을 정의하기 위해서는 아래와 같은 방법을 사용하면 된다. 


####**1. `on_json_loading_failed()` 재정의 하기**####

- 앞서 `on_json_loading_failed` 함수로 인해서 400 Bad Request 가 리턴되기 때문에 해당 함수를 다르게 동작하도록 재정의 하고, 재정의한 함수를 `request.on_json_loading_failed` 에 연결 시킬 수가 있다. 이 방법이 좋은 점은 함수를 재정의 함으로써 복잡한 기능을 JSON parsing fail 이 발생 했을때 대응 할수가 있다. 예를 들면, 400 bad request 와 함께 JSON 응답을 보내게 할 수도 있고, 특정한 로그를 남기거나 하는 등의 행동을 정의 할 수가 있다. 

- 아래의 예제에서는 에러가 발생했을 때, 기본 빈 dict을 반환하도록 구성하였다. 이렇게 하면 마음놓고 get_json()을 사용 할 수가 있다. 

```python 
def on_json_loading_failed_return_dict(e):
    return {}


@app.route("/test", methods=['POST'])
def test():
    request.on_json_loading_failed = on_json_loading_failed_return_dict
    print request.get_json()
    return "Hello World!" 
```






####**2. `get_json()` silent 파라미터 활용**####

- `get_json()` 함수는 몇가지 파라미터를 제공하는데 그 중에서 `silent` 파라미터는 JSON parsing fail 에 대해서 None 처리 여부를 설정할 수 있다. 기본값을 False인데, 명시적으로 True 로 주면 `get_json()` 호출시 에러가 나지 않고 None을 리턴한다. 

```python
print request.get_json(silent=True)
```
 

**Parameters:**

- force – if set to True the mimetype is ignored.
- silent – if set to True this method will fail silently and return None.
- cache – if set to True the parsed JSON data is remembered on the request.


어떤 방식을 선호하는지는 개인이나 프로젝트 성격에 따라 다를것 같다. 모든 API가 JSON 으로 데이터를 전달하는 방식이라면, `on_json_loading_failed()` 함수를 재정의하고 decorator 등을 활용하는게 좋을것 같다. (필자 역시 최근의 프로젝트에서 그렇게 활용했다.) 

참고로 flask 0.11 버전에서는 `is_json` 이 추가되었는데 이것은 parsing fail 을 감지하는 것이 아니라, mimetype 이 application/json 인지 아닌지를 True | False 로 반환하는 역할을 한다. 


