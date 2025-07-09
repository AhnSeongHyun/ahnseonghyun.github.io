---
title: 'python response data for flask'
author: 'ash84'
pub_date: '2015-01-30'
description: 'flask 로 작업하는 경우가 두가지인데, view 를 만들거나 아니면 json 형태로 api 결과를 리턴하는 경우를 만들거나. 그런데 첫번쨰는 머 `render_template` 사용하는 거고, 두번째 api 결과의 경우 보통 공통적인 api 결과 형식/포맷을 만들어서 반환하기 마련이다. 여러가지 방식이 있겠지만, 선호하는 방식은 meta 와 data 로 나누는 것인데 meta 에는 code 가 들어가는데 http status code 혹은 확장할 경우 확장코드가 들어가고 message 는 보통 에러의 경우 상세 에러메시지가 들어'
featured_image: ''
tags: ['dev', 'FLASK', 'Python']
---

flask 로 작업하는 경우가 두가지인데, view 를 만들거나 아니면 json 형태로 api 결과를 리턴하는 경우를 만들거나. 그런데 첫번쨰는 머 `render_template` 사용하는 거고, 두번째 api 결과의 경우 보통 공통적인 api 결과 형식/포맷을 만들어서 반환하기 마련이다. 여러가지 방식이 있겠지만, 선호하는 방식은 meta 와 data 로 나누는 것인데 meta 에는 code 가 들어가는데 http status code 혹은 확장할 경우 확장코드가 들어가고 message 는 보통 에러의 경우 상세 에러메시지가 들어간다. </span><span style="font-size: 11pt; line-height: 1.5;">data 부분에는 리스트 형식이나 사전 형식으로 그때 그때 다른 데이터가 들어가는데 사실 이건 api 에 따라 다르다. 

이런 형식들을 주로 아래의 python 클래스로 만들어서 사용하는데 `.json` 이나 `.to_dict` 같은 함수/프로퍼티를 만들어서 사용하는 데 그 함수/프로퍼티에서는 json 으로 리턴을 한다. 그런데 flask 에서는 `jsonify` 라는 좋은 함수가 있어서 그것을 활용해서 사용한다. 일반 json 으로 리턴을 하게 되면 결국 flask 에서 리턴할때 또 status code 를 넣어줘야 하는데 그게 귀찮아서 ㅎㅎ 그냥 flask 에서 사용할때는 `.json` 에서 바로 `jsonify()` , statuscode 로 리턴하는게 나은것 같다.  
 
<script src="https://gist.github.com/AhnSeongHyun/f28cd88f6bc01e2b2a3a.js"></script>

 
