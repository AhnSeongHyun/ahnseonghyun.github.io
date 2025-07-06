---
title: '(flask) Pluggable View, Class 에서 요청처리하기'
author: 'ash84'
pub_date: '2017-03-29'
description: '[Pluggable View](http://flask.pocoo.org/docs/views/?highlight=as_view) 라고 말이 어려운데, 간단하게 말하자면 flask 는 기본적으로 url 과 함수의 맵핑으로 이루어져있다. 아래의 Quick Start 에서도 보면 알겠지만, url “/ ” 는 hello_world() 라는 함수에 맵핑이 되어 있어서 / 로 들어오게 되면 hello_world() 함수로 들어오게 된다.'
featured_image: ''
tags: ['dev', 'FLASK', 'flask multi view', 'Pluggable View', 'Python', '파이썬']
---


<span style="font-size: 11pt;">[Pluggable View](http://flask.pocoo.org/docs/views/?highlight=as_view) 라고 말이 어려운데, 간단하게 말하자면 flask 는 기본적으로 url 과 함수의 맵핑으로 이루어져있다. 아래의 Quick Start 에서도 보면 알겠지만, url “/ ” 는 hello_world() 라는 함수에 맵핑이 되어 있어서 / 로 들어오게 되면 hello_world() 함수로 들어오게 된다. </span>

<span style="font-size: 11pt;">  
</span>

<script src="https://gist.github.com/AhnSeongHyun/7409099.js"></script><span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">사실 flask를 많이 써보신분들은 아시겠지만, 빠르게 개발할수 있다는 측면에서 매우 좋지만 view 즉, url 별로 보여줘야 하는 페이지가 증가하는 경우, 하나의 파이썬 파일에 계속 증가하는 문제가 있다. 그래서 flask 에서는 0.7 버전 부터 </span><span style="background-color: transparent; font-size: 11pt; line-height: 2;">Pluggable View 라는 것을 제공하는데 장고(Django) 의 generic view 에서 영감을 받았다고 한다. </span>

<span style="background-color: transparent; font-size: 9pt; line-height: 2;">  
</span>

<span style="background-color: transparent; font-size: 11pt; line-height: 2;">기본 개념 자체는 기존의 main.py 에서 하던것들을 다른 클래스로 이전하는 것이다. 그리고 main.py 에서 server 를 시각하는데, 그 전에 어떤 url은 어떤 클래스를 보라고 지정을 해준다는 것이다. 간단한 예제를 통해서 알아보자. </span>

<span style="background-color: transparent; font-size: 9pt; line-height: 2;">  
</span>

<span style="background-color: transparent; font-size: 11pt; line-height: 2;">일단 main.py를 보자.</span>

<span style="background-color: transparent; font-size: 9pt; line-height: 2;">  
</span>

<script src="https://gist.github.com/AhnSeongHyun/7409110.js"></script>

<span style="background-color: transparent; font-size: 9pt; line-height: 2;">  
</span>

<span style="font-size: 11pt;">main.py 를 서버를 시작하는 부분인데, 기존의 @app.route() 로 지정하는 것을 모두 제거 하였다. 두가지 URL을 처리할것인데, </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 10pt;">/home?id=0192393</span>

<span style="font-size:10pt;">/garden/02931</span>

</div><span style="font-size: 11pt;">위와 같이 두가지 url을 처리한다고 했을때 어떻게 해야하는지 알아보자. 일단 14번째 줄을 보면 add_url_rule 함수를 통해서 내가 만든 homeView 를 등록하는 부분을 볼수가 있다. 일단 저렇게 등록을 하면 /home URL을 통해서 들어오는 요청은 homeView 에서 처리되는데 homeView 의 클래스인 HomeView 를 보도록 하자. </span>

<script src="https://gist.github.com/AhnSeongHyun/7409110.js"></script>

<span style="font-size: 11pt;">HomeView 에서 중요한 부분은 view를 슈퍼클래스로 가진다는 점이다. 그래서 homeView 객체를 생성할때도 일반적인 생성자로 생성하는 것이 아니라 [as_view()](http://flask.pocoo.org/docs/api/?highlight=as_view#flask.views.View.as_view) 클래스 메소드로 생성하는 것을 볼 수 있다. as_view() 클래스 메소드에 대한 설명을 보면, **[‘Converts the class into an actual view function’](http://flask.pocoo.org/docs/api/?highlight=as_view#flask.views.View.as_view)** 이라고 되어 있는것을 볼수 있다. </span>

<span style="font-size: 11pt;">그리고 HomeView 클래스 안에서는 dispatch_request 메소드를 구현해야하는데, 사실상 이 함수에서 실질적인 view 코드가 동작한다고 보면된다. 그리고 이 메소드에서 </span><span style="background-color: transparent; font-size: 11pt; line-height: 2;">@app.route() 로 지정했던 메소드에서 했던 일들을 적어주면 된다. HomeView 클래스에서는 id 를 가져와서 템플릿에 id를 전달해 주는 것을 볼 수 있다. </span>

<span style="background-color: transparent; font-size: 9pt; line-height: 2;">  
</span>

<span style="font-size: 11pt;">이 방식은 이전의 처리들을 다른 하나의 클래스로 분담해서 해당클래스의 dispatch_request 메소드에서 한다는 점이 특징이라고 볼수 있다. 그런데 http method 중에 get, post, put, delete 메소드 별로 나눠서 작업할 수 있는 방법을 제공하고 있기도 하다. 이 방법을 **[Method based Dispatching](http://flask.pocoo.org/docs/views/?highlight=as_view)** 이라고 flask 문서에서는 설명하고 있다. </span>

<script src="https://gist.github.com/AhnSeongHyun/7409323.js"></script>

<span style="font-size: 11pt;">이 방식은 기존의 View 클래스 대신에 MethodView 클래스를 슈퍼클래스로 하고 있는것을 볼수 있는데, dispatch_request 와 같이 사용할수도 있다. main.py 15번째 줄을 보면 gardenView 를 등록하는 부분을 볼수 있는데, /garden/<flower> 이런식의 URL 을 처리해야 한다면 15번째 줄처럼 등록해 주면된다. </span>

<span style="font-size: 11pt;">그렇게 등록을 하고 /garden/rose 이렇게 호출을 하면 GardenView 의 get(self, flower) 함수가 호출되는 것을 확인할수 있을것이다. 실제로 한번 해보면 그리 어렵지 않을것이다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">ps) 부제를 마음대로 Class 에서 요청처리하기 지었는데, 맞나 모르겠네 ![:)](http://ash84.net/wp-includes/images/smilies/simple-smile.png)</span>

<span style="background-color: transparent; font-size: 9pt; line-height: 1.5;">  
</span>



