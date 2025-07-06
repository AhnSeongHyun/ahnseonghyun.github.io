---
title: '(flask) http get url 처리'
author: 'ash84'
pub_date: '2017-03-30'
description: '당연히 최근에는 오픈API나 혹은 간단하게 웹 서비스를 구성한다고 하면 Http Get 방식으로 데이터를 전달하는데 flask 에서는 다음과 같이 처리 할수 있다. `@app.route()`함수에서 어떤 메소드를 사용할 것인지 지정을 해주고 나면 `request.args.get()` 함수를 통해서 해당 url 로 넘어온 데이터를 가져올 수 있다.'
featured_image: ''
tags: ['dev', 'FLASK', 'flask get method', 'flask get 처리', 'Python']
---


<span style="font-size: 11pt;">당연히 최근에는 오픈API나 혹은 간단하게 웹 서비스를 구성한다고 하면 Http Get 방식으로 데이터를 전달하는데 flask 에서는 다음과 같이 처리 할수 있다. `@app.route()`함수에서 어떤 메소드를 사용할 것인지 지정을 해주고 나면 `request.args.get()` 함수를 통해서 해당 url 로 넘어온 데이터를 가져올 수 있다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">예를 들어, http://127.0.0.1:8000/article?keyword=google&pageCount=1 이런식으로 url을 호출을 하면 해당 데이터를 가져와서 어떤 데이터 연산을 한뒤 페이지를 보여줄수 있는 것이다. </span>

<span style="font-size: 11pt;"></span>

<script src="https://gist.github.com/AhnSeongHyun/6444186.js"></script><span style="font-size: 11pt;">  
</span>



