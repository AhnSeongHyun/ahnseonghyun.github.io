---
title: 'python 3항 연산자'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['3항연산자', 'dev', 'Python', '파이썬']
---


<span style="font-size: 11pt;">이걸 언제 쓰냐라고 생각했지만, 내가 오늘 이 글을 적게 될줄은 ‘나’조차도 몰랐다. 3항 연산자, 일명 if 축약 이라고도 하는데 사실 그리 쓸일이 많지는 않은데 flask 에서 유독 짜증나는 부분이 있어서 쓰게 되었다. flask 에서 함수를 구성하다 보면 초반에 하는 것중 하나가 request 객체에서 get 혹은 post 에 대한 데이터를 가져오는 작업이다. 일반적으로 get 의 경우 `request.args.get("id", None)` 이런식으로 가져오는데 get 의 경우에는 초기값을 줄수가 있다. 때</span><span style="font-size: 11pt;">문에 실제 쿼리스트링에 “id” 가 없더라도 문제가 되지 않는다. 그런데 post 에서 form 데이터를 가져오는 경우 `request.form['id']`이런식으로 가져오게 되는데 이 경우, id가 없으면 400을 뱉는다. 그게 싫은 경우는 id 가 request.form에 있는지 일일히 if문으로 검사를 해야한다. </span>

<span style="font-size: 11pt;">3항 연산자를 사용하면 좀더 깔끔(?) 하게 처리할수 있는데 아쉽게도 파이썬의 3항 연산자는 사실상 if문이라서. 그리 깔끔한지는 모르겠지만. </span>

<script src="https://gist.github.com/AhnSeongHyun/3730228f2ee7c29b9e45.js"></script>



