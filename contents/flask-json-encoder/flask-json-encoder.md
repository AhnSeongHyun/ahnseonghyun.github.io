---
title: 'flask - json_encoder 지정하기'
author: 'ash84'
pub_date: '2017-06-16'
description: 'API 상에서 JSON 으로 응답을 내보내기 위해서는 데이터를 Json Serialize(직렬화)를 해야한다. 그런데 json 에서 표현할 수 있는 데이터는 한정이 되어 있어서 각 프로그래밍 언어에 있는 모든 타입을 지원하지는 못한다. Decimal 형도 그런 예 중 하나인데 파이썬에서는 `json.dumps()`를 통해서 주로 직렬화를 하고 그 함수의 기능 중에 `cls` 인자를 통해서 JSONEncoder 를 구현한 서브 클래스를 지정해 주면 해당 인코더로 json 문자열을 만든다. 

flask 에서도 `json.dumps`'
featured_image: ''
tags: ['FLASK', 'dev', 'Python', 'JSON', 'json_encoder']
---

API 상에서 JSON 으로 응답을 내보내기 위해서는 데이터를 Json Serialize(직렬화)를 해야한다. 그런데 json 에서 표현할 수 있는 데이터는 한정이 되어 있어서 각 프로그래밍 언어에 있는 모든 타입을 지원하지는 못한다. Decimal 형도 그런 예 중 하나인데 파이썬에서는 `json.dumps()`를 통해서 주로 직렬화를 하고 그 함수의 기능 중에 `cls` 인자를 통해서 JSONEncoder 를 구현한 서브 클래스를 지정해 주면 해당 인코더로 json 문자열을 만든다. 

flask 에서도 `json.dumps` 를 사용해서 json 문자열을 응답으로 내보낼 수도 있지만, `jsonify()` 를 이미 제공하고 있다. json 을 내보낼때 결국 어떤 객체에서 데이터를 가져오게 된다.  객체 내 형을 변환하거나 추가적으로 같은 내용의 다른 형의 변수를 두는 것도 한 방법이지만, 낭비라는 생각이 들었다. 또한 이런 클래스가 많은 경우 그런 클래스 각각 혹은 몇개의 상위 클래스에 `to_json`을 만들어서 따로 직렬화를 위한 작업을 해줄 수도 있겠지만, 

flask 에서는 `app.json_encoder` 을 제공하고 있어서 `jsonify()` 를 통해서 응답을 보낼 경우, 지정한 인코더를 통해서 생성되도록 할 수 있다. 예를 들어, 아래의 CustomJsonEncoder 는 Decimal 형을 문자열로 치환해서 보내주고 있고, None 인 값에 대해서는 빈 문자열로 치환해서 보내주고 있다. 


<script src="https://gist.github.com/AhnSeongHyun/2329e79ac451edf655789f7243077ef1.js"></script>

JsonEncoder 를 활용하면, 타입에 따라서 json 에서 표시할 때만 다르게 표시하는 것이 가능하다. 예를들면, datetime 형의 경우 포맷(format)을 다르게 표현할 수 있는데, 각 클래스에서 그것을 작업해주는게 아니라 json serialize 되는 시점에 일괄적으로 datetime 형은 특정 포맷으로 변경해서 내보낼 수도 있을것이다. 


