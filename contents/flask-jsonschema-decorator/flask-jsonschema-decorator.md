---
title: '(flask) jsonschema 를 이용해서 request.json 검사하기'
author: 'ash84'
pub_date: '2017-04-03'
description: ''
featured_image: 'https://avatars0.githubusercontent.com/u/2182898?v=3&s=200'
tags: ['dev', 'FLASK', 'Python', 'JSON', 'jsonschema', 'Decorator']
---

API에서 파라미터의 유효성 검사는 필수적인 요소이긴 하지만, 개발자로서 여간 귀찮은 일이 아닐 수 없다. API의 양이 많을수록 할 일은 많아진다. 세세하게 체크할 부분은 해야하지만 기본적으로 파라미터 유무, 파라미터의 데이터 형을 체크하는 부분이 필요했다. API는 기본적으로 JSON 을 `POST`로 받는 식으로 구성되어 있어서 JSON을 검증하는 부분이 필요했다. 

JSON 검증을 위해서 [jsonschema](https://pypi.python.org/pypi/jsonschema) 를 활용할 수 있다는 것을 알았는데, 문제는 라이브러리를 써서 검증할 수 있지만, 일단 **스키마가 있어야 한다는 사실**이다. [jsonschema](https://pypi.python.org/pypi/jsonschema) 라이브러리는 단순히 스키마에 대한 검증을 해주는 도구이다.

스키마를 만들기 위해서 [jsonschema.net](http://jsonschema.net/) 을 이용했다. 이 사이트는 요청하려는 JSON Payload를 넣게 되면 해당 Payload에 맞는 스키마를 추출해 주는 작업을 해준다. 예를 들어, 아래와 같이 회원가입을 하는 JSON Payload가 있다고 가정해보자. 

```json
{
    "user_id":"test123", 
    "name":"TEST", 
    "password":"test123", 
    "email":"test@gmail.com",
    "mobile":"01012341234", 
    "birthday":"19701121",
    "gender":1
}
```

payload 에 대한 스키마를 뽑기 위해서 해당 JSON을 [jsonschema.net](http://jsonschema.net) 에 붙여넣기를 한다.  

![https://flic.kr/p/QRhLmR](https://c2.staticflickr.com/1/527/32062904185_44e4fa2308_z.jpg)


위와 같은 방법으로 JSON 스키마를 뽑게 되면 아래와 같이 나온다. 

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "user_id": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "password": {
      "type": "string"
    },
    "email": {
      "type": "string"
    },
    "mobile": {
      "type": "string"
    },
    "birthday": {
      "type": "string"
    },
    "gender": {
      "type": "integer"
    }
  },
  "required": [
    "user_id",
    "name",
    "password",
    "email",
    "mobile",
    "birthday",
    "gender"
  ]
}
```

자세히 살펴보면, `properties` 하는 부분에 각각의 항목에 대한 허용되는 타입이 정해져 있다. 입력한 값에 대해서 분석을 해서 type을 추출해서 보여주고 있고, 차후에 request json payload에 해당 항목의 타입이 스키마와 맞지 않으면 invalid 처리가 된다. 그리고 바로 아래에 보면 `required` 라고 하는 부분이 있는데 **그 부분은 어떤 항목(key)를 강제할 것인지를 정하는 부분**이다. 예를 들어 성별(gender)을 받을 수도 있지만, 안 받을 수도 있는 optional 한 값이라고 하면 해당 부분을 `required`에서 빼면 된다. 기타 좀더 상세한 설정은 [http://json-schema.org/](http://json-schema.org/) 에서 jsonschema 에 대해서 좀 더 살펴본 후 수정해서 사용하면 된다. 



#### **적용하기**####


##### **기본 라이브러리 사용** ######
앞서서 JSON Payload 를 이용해서 JSON 스키마를 뽑아내는 작업을 진행했다. 이제는 해당 스키마를 python의 jsonschema 라이브러리를 이용하는 방법을 알아보자. 

```python 
from jsonschema import validate, ValidationError
# A sample schema, like what we'd get from json.load()
schema = {
...     "type" : "object",
...     "properties" : {
...         "price" : {"type" : "number"},
...         "name" : {"type" : "string"},
...     },
... }
validate({"name" : "Eggs", "price" : 34.99}, schema)
```

간단한 사용법은 이렇다. `schema` 변수에 우리가 검증하고자 하는 스키마(dict 형태)를 넣고, `validate` 함수를 이용해서 검증하고자 하는 json 을 검증하면된다. `validate` 함수는 invalid 한 경우 2가지 에러를 발생시키는데 하나는 `ValidationError` 이고 다른 하나는 `SchemaError` 이다. 말 그대로 스키마가 문제가 있으면 `SchemaError` 를, 검증이 실패한 경우이면, `ValidationError`를 발생시킨다. 

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>

##### **flask decorator 로 활용하기** ######

이제 flask의 요청을 받는 함수에서 사용해 보자. 당연히 요청을 받는 함수 안에서 처리하는게 좋지만, Python의 decorator 를 이용하는게 더 깔끔하게 처리 할 수 있고, 무엇보다도 요청처리 함수 안에서는 비지니스 로직을 구현하고 이런 처리는 decorator 를 작성해서 위임하는게 좋다고 생각했다. 

```python 
@json_schema('signup_api')
def signup():
    .... 
```

위와 같이 `json_schema` 라는 decorator 를 만들고, 인자값을 어떤 스키마가를 지칭하는 키(key) 값을 주면 `json_schema` 데코레이터에서 해당 스키마와 현재 요청으로 들어온 `request.json`과 비교해서 문제가 있으면 **invalid parameter 400** 에러를 반환하는 식으로 구현하였다. 

```python

def json_schema(schema_name):
    """
    지정한 API 에 대해서 지정한 schema_name로 검사한다.
    :param schema_name: 검사대상 스키마 이름
    :return: 에러나면 40000 에러
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            try:
                request.on_json_loading_failed = on_json_loading_failed_return_dict
                validate(request.json, current_app.config['API_JSON_SCHEMA'][schema_name])
                return func(*args, **kw)
            except ValidationError as e:
                logger.exception(traceback.format_exc())
                return ResponseData(code=HttpStatusCode.INVALID_PARAMETER).json
        return wrapper
    return decorator
```

지금 생각해보면, API의 함수명을 키 값으로 활용하는것도 나을 것 같다는 생각이 든다. 일일히 decorator 에 인자로 문자열을 전달하는 것은 키값이 변경시 문제가 발생할 수 있다는 생각이 든다. 

##### **정리** #####

꽤 많은 API를 작성해야 하고 API의 요청으로 들어오는 값들을 검증하기 위해서 개발해야 하는 부분도 있지만, JSON 스키마를 이용하면 분명히 편리한 점이 있는 것 같다. 기본적인 파라미터 유무나 형식 등을 신경쓰지 않고 공통된 응답처리가 가능하다는 점 그리고 요청 처리 함수 안에서 좀 더 비지니스 로직에 집중할 수 있다는 점을 가장 큰 장점으로 느꼈다. 


<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script> 

**추출한 JSON 스키마들을 어디에 둘 것인가?** 에 대한 고민이 있었지만, 간단하게하려고 config 파일에 두고 `current_app.config` 에서 읽어오게 했다. 이렇게 사용할 때의 문제점은 많은 API에 JSON 스키마를 적용할 경우, 스키마들이 많아지고 관리하기 어려워진다는 문제인 것 같다. 스키마를 어디에 두고 어떻게 가져올 것인지에 대한 설계할 때 고려가 필요한 것 같다. 

이 글과 더불어서 채문창님의 [JSON과 PYTHON API의 만남](https://github.com/mcchae/JSON-Schema/blob/master/JSON-API.md) 이라는 글을 읽어보면 좋을것 같다. 비슷한 글이지만, 스키마에 맞게 자동 데이터생성 이라는 부분이 있는데, JSON 스키마를 이용해서 테스트를 위한 데이터를 생성할 수 있다. 



### Reference ###
- http://json-schema.org
- https://pypi.python.org/pypi/jsonschema
- http://jsonschema.net

