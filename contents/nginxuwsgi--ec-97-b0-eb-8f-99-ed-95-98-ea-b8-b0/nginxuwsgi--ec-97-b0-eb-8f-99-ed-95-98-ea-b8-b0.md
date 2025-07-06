---
title: 'nginx-uwsgi 연동하기'
author: 'ash84'
pub_date: '2015-07-03'
description: '### uwsgi – flask 기본 연동 

기존의 uwsgi 소개글에서는 http 옵션을 통해서 바로 웹을 띄웠었는데 여기에서는 기본적으로 소켓의 형태로 띄워지게 된다. 앞단에서 nginx 의 request 를 전달받아서 처리하는 형태라고 보면 된다. 


### nginx 설정 수'
featured_image: ''
tags: ['dev', 'nginx uwsgi connection', 'nginx uwsgi 연동하기', 'python nginx', 'WAS', 'Web Server', '웹서버']
---


### uwsgi – flask 기본 연동 

<span style="font-size: 11pt; line-height: 2;">기존의 uwsgi 소개글에서는 http 옵션을 통해서 바로 웹을 띄웠었는데 여기에서는 기본적으로 소켓의 형태로 띄워지게 된다. 앞단에서 nginx 의 request 를 전달받아서 처리하는 형태라고 보면 된다. </span>

<script src="https://gist.github.com/AhnSeongHyun/657f6266ea6192c678be.js"></script>

### nginx 설정 수정하기

<span style="font-size: 11pt; line-height: 2;">정말 친절하게도 nginx 에서는 uwsgi 관련 설정을 기본으로 제공한다. 이전의 포스트에서 보면 알겠지만, conf 내에 보면 uwsgi_param 같이 이미 마련해두었다. </span>

<span style="font-size: 11pt;">nginx.conf 의 일부분을 다음과 같이 수정한다. </span>

<span style="font-size: 11pt;"><script src="https://gist.github.com/AhnSeongHyun/f2502d560980a5f2f9d9.js"></script></span>

<span style="font-size: 11pt; line-height: 2;">자동으로 uwsgi_params 라는 파일을 가져온다(/conf내에 default 로 존재), 그리고 uwsgi 에서 설정한 소켓으로 request 를 pass 하도록 설정한다. </span>

<span style="font-size: 9pt; line-height: 2;">  
</span>

<span style="font-size: 11pt; line-height: 2;">**주의할점 : uwsgi 와 nginx 의 관계를 보면 nginx 는 웹서버로 앞단에서 요청을 받는것이다. 때문에 uwsgi 가 켜져 있지 않으면 별도의 에러화면을 볼수가 있다. 별 문제 없이 uwsgi 를 켜주면 된다. **</span>



