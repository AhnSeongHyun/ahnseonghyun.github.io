---
title: '[Python] 특정로그 파일 이메일로 전달하기'
author: 'ash84'
pub_date: '2023-03-19'
description: '엔진쪽에서 모듈을 개발하다보면 여러가지 일이 생기는데 그중 하나가 바로 엔진 재기동에 관한 부분이다. 엔진 재기동은 여러가지 경우에 일어나는데 주로 내부 모듈이 잘못된 동작을 수행하고 예외처리가 안되었거나 메모리의 잘못된 참조로 인해서 발생이 된다. 


문제는 재기동이 된다는 점이다. 물론 엔진이 다시 켜지는 것은 맞지만 엔진이'
featured_image: ''
tags: ['dev', 'Email', 'Python', 'File']
---


<span style="font-size: 11pt; ">엔진쪽에서 모듈을 개발하다보면 여러가지 일이 생기는데 그중 하나가 바로 엔진 재기동에 관한 부분이다. 엔진 재기동은 여러가지 경우에 일어나는데 주로 내부 모듈이 잘못된 동작을 수행하고 예외처리가 안되었거나 메모리의 잘못된 참조로 인해서 발생이 된다. </span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">문제는 재기동이 된다는 점이다. 물론 엔진이 다시 켜지는 것은 맞지만 엔진이 재기동 되다보니 문제가 생겼었나 하는 착각도 들게 만드는데, 엔진이 재기동되면 일련의 로그파일을 남긴다. 어디서 문제가 생겼는지를 알려주는 로그인데 일명 pstack_~.log 이다. 문제는 서버에 남지만 개발자가 수동적으로 들여다 보기전엔 알수 없다는 사실이다.</span>

<span style="font-size: 11pt; ">그래서 고안한 것이 파이썬으로 해당 로그파일이 떨어지는지를 감시하는 유틸리티이다. 이 유틸은 주기적으로 특정위치에 </span>  
<span style="font-size: 15px; line-height: 29px; ">pstack 파일이 </span><span style="font-size: 11pt; "> 있는지를 확인하고, 로그가 있다면 해당 로그를 등록한 메일이 첨부하여 전송하는 유틸이다. 전송된 로그는 일단 지워버린다.</span>

<span style="font-size: 11pt; ">  
</span>

<script src="https://gist.github.com/2784849.js?file=gistfile1.py"></script>

<span style="font-size: 15px; line-height: 29px;">  
</span>

<div style="text-align: justify; "><div style="line-height: 2; "><span style="font-size: 11pt; ">코드를 보면 while문이 무한 루프를 돌면서 sleep을 5초를 주면서 체크하고 있다. 거의 실시간성 체크라고 볼수도 있겠지만 sleep문을 넣지 않으면 오히려 엔진이나 서버 작업에 더 영향을 줄수 있을것 같아서 일부러 5초를 넣었다. 실제로 넣지 않고 실행을 시키면, 서버의 cpu사용량을 혼자 다 차지한다.</span></div><div style="line-height: 2; "></div><div style="line-height: 2; "></div><div style="line-height: 2; "><span style="font-size: 11pt; ">좀더 발전적으로 생각해 보자. </span></div><div style="line-height: 2; "></div><div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; "><div style="line-height: 2; "><span style="font-size: 11pt; line-height: 2; ">– 일정 시점에 체크 하려면 어떻게 해야 할까?</span></div><div style="line-height: 2; "><span style="font-size: 11pt; ">– 다량의 로그가 있다면?</span></div></div><div style="line-height: 2; "></div><div style="line-height: 2; "></div><div style="line-height: 2; "> </div></div><script src="https://gist.github.com/2822327.js?file=gistfile1.py"></script>

<span style="font-size: 11pt; ">일단 위와 같은 코드를 추가했다. import zipfile 을 넣었으며, toZip() 함수를 작성해서 압푹할 파일 리스트와 압축 파일 이름을 인자로 받는 함수를 작성했다. 그리고 아래와 같이 1개 이상의 로파일이 있을때에는 해당 로그파일들을 압축해서 메일에 첨부해서 전송하는 방식을 사용하였다. </span>

<span style="font-size: 11pt; ">  
</span>

<script src="https://gist.github.com/2822335.js?file=gistfile1.py"></script>



