---
title: 'flask - jinja2 tojson 필터'
author: 'ash84'
pub_date: '2017-04-03'
description: 'flask 문서를 보다보니 [standard filters](http://flask.pocoo.org/docs/0.12/templating/#standard-filters) 라는 항목이 있는데 `tojson` 이 그 내용이다.(기본적으로 제공하는 필터라는 내용) 간략하게 애기하자면, 어떤 랜더링할 변수에
`tojson` 이라고 jinja2 템플릿 상에서 `|` 를 이용해서 붙이게 되면 json으로 변환된 값을 랜더링해준다. 

예를들어, user 라는 dict 객체에 데이터를 넣어서 전달한다고 할 때, 

```python 
@a'
featured_image: 'http://flask.pocoo.org/docs/0.12/_images/logo-full.png'
tags: ['dev', 'Flask', 'Python', 'jinja2', 'tojson']
---
flask 문서를 보다보니 [standard filters](http://flask.pocoo.org/docs/0.12/templating/#standard-filters) 라는 항목이 있는데 `tojson` 이 그 내용이다.(기본적으로 제공하는 필터라는 내용) 간략하게 애기하자면, 어떤 랜더링할 변수에
`tojson` 이라고 jinja2 템플릿 상에서 `|` 를 이용해서 붙이게 되면 json으로 변환된 값을 랜더링해준다. 

예를들어, user 라는 dict 객체에 데이터를 넣어서 전달한다고 할 때, 

```python 
@app.route('/')
def hello_world():
    user ={}
    user['name'] = 'ash84'
    user['age'] = 24
    user['gener'] = '<strong>male</strong>'

    return  render_template("test.html", user=user)
```

jinja2 template 상에서 `tojson`을 이용해서 `<script>` 상에 자바스크립트 객체로 바로 넣을 수가 있다. 개인적으로 html과 js가 혼합된 방식에서 js의 영역까지 랜더링에 포함하게 하는것을 별로 선호하지는 않지만, 때에 따라서는 잘 쓸수 있을것 같다. 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
 
<script type=text/javascript>
    var user = {{ user | tojson | safe }};
    console.log(user);
</script>
</body>
</html>
```
 
