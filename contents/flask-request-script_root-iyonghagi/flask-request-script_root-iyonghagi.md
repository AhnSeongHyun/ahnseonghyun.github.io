---
title: 'flask - request.script_root 이용하기'
author: 'ash84'
pub_date: '2017-08-28'
description: ''
featured_image: ''
tags: ['FLASK', 'Python', 'dev', 'script_root']
---

하나의 웹을 여러 path 에 올려야 할 경우가 있다. 예를 들면, 테스트를 위해서 `/web1`, `/web2` 이런식으로 구성해서 올릴 경우이다. 이런 경우 프론트단에서 URL로 지정해 놓은 값들을 수정해 줘야 한다. 
ajax 를 호출한다고 생각해 보자. 원래 `/web/api/room` 이런식으로 ajax 를 호출하는 경우가 있었다면 `/web1`, `/web2` 에 따라서 `/web1/api/room`, `/web2/api/room` 이렇게 변경해 줘야 한다. 

```javascript
$.ajax({
    url: "/web/api/room",
    type: "POST"
});
```

매번 고쳐주는 일은 번거롭다. 가장 간단하게 생각할 수 있는건 js 상에서 `BASE_URL` 변수를 두고 사용사는 시점에 변경하도록 하는 것이다. 이게 이상적으로 보일 수 있겠지만, 수정 포인트가 여러 곳에서 한곳으로 줄여졌다는 점외에 여전히 옮길 때 마다 수정해줘야 한다는 점은 변하지가 않았다. 

또 한가지 방법은 flask 상에서 `render_template` 통해서 `base_url` 을 전달하고 그것을 아래와 같이 js 의 `BASE_URL` 변수에 전달해서 사용하는 방법이다. **이 방식은 수정할 필요가 없다는 장점은 있지만, html 과 js 가 분리된 경우에는 적용하기가 어렵다.**

```html 
var BASE_URL = "{{ base_url }}";
```

Flask 에서는 [`script_root`](http://flask.pocoo.org/docs/0.12/api/#flask.Request.script_root) 라는 변수를 request 요청 객체 상에서 제공하고 있다. 이 변수는 URI 상에서 최상위 Path 를 반환한다. 예를 들어, 아래와 같은 URL 이 있다고 할 때, request 객체 상에서의 경로 및 URL을 반환하는 함수들은 아래와 같이 표현한다. 

```
http://www.example.com/myapplication/%CF%80/page.html?x=y
```

```
path - u'/π/page.html'
full_path - u'/π/page.html?x=y'
script_root - u'/myapplication'
base_url - u'http://www.example.com/myapplication/π/page.html'
url - u'http://www.example.com/myapplication/π/page.html?x=y'
url_root - u'http://www.example.com/myapplication/'
```

그래서 `request.script_root` 를 html 상에서 head 내에 위치시키고, 실제 BASE_URL을 조합해서 사용하는 부분을 js 파일에 두고 참조해서 사용할 수가 있다. 코드는 아래와 같다. 


```javascript
<head>
<script type="text/javascript">
    var BASE_URL = {{ request.script_root|tojson|safe }};
</script>
</head>
...
<script>
// in js file 
$.ajax({
    url: BASE_URL + "api/room",
    type: "POST"
});
</script>
```

물론 `request.url_root` 나 `request.script_root` 를 백엔드 파이썬코드에서 사용할 수 있는데, 이때 주의할점 중 하나는 request context 안에서 사용해야한다는 점이다. 예를들어, logo 의 url을 만드는 코드가 있다고 할때 아래와 같이 `base_url` 파라미터에서 사용할 경우 context error를 발생시킨다. 

```python 
def get_logo_url(logo_path, base_url=request.script_root):
   ...
```

왜냐하면 함수가 실행되는 시점이 아닌 선언되는 시점에는 flask가 시작되고 요청(request) 가 들어오지 않은 시점이기 때문에 `request.script_root` 를 가져 올 수 없다. 이럴경우, 아래와 같이 함수 안으로 넣어주자. 

```python 
def get_logo_url(logo_path, base_url=None):
   if not base_url:
        base_url = request.script_root
   ...
```


#### Reference  

- http://flask.pocoo.org/docs/0.12/api/#flask.Request.script_root
- [AJAX with jQuery](http://flask.pocoo.org/docs/0.12/patterns/jquery/)
- [jqueryexample](https://github.com/pallets/flask/tree/master/examples/jqueryexample)

