---
title: '(vert.x) mod-sample 따라하기'
author: 'ash84'
pub_date: '2013-05-16'
description: '아직까지 vert.x에 대한 자료가 많지는 않은데, 설치 이후에 실제 서버를 돌려보기 위해서는 mod 라는 것을 만들어야 하는데 gradle로 되어 있어서 개발 환경 꾸미기도 쉽지 않은것 같다. 그래도 [h](http://helloworld.naver.com) [elloworld.naver.com](http://helloworld.naver.com)에서 vert.x 에 대해서 보고 (최근에 다른 글이 하나 더 올라왔다.) 글 쓰신 분이 운영하시는 블로그에서 [mod-sampl'
featured_image: ''
tags: ['java', 'mod-sample', 'tutorial', 'vert.x', '모듈 만들기']
---
<span style="font-size: 11pt;">아직까지 vert.x에 대한 자료가 많지는 않은데, 설치 이후에 실제 서버를 돌려보기 위해서는 mod 라는 것을 만들어야 하는데 gradle로 되어 있어서 개발 환경 꾸미기도 쉽지 않은것 같다. 그래도 [h](http://helloworld.naver.com) [elloworld.naver.com](http://helloworld.naver.com)에서 vert.x 에 대해서 보고 (최근에 다른 글이 하나 더 올라왔다.) 글 쓰신 분이 운영하시는 블로그에서 [mod-sample](https://github.com/keesun/mod-sample) 라는 것을 만들어 두시고 그것에 대한 사용법을 남겨 주셨다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 15px; line-height: 29px;">글 제목 : [Hello Vert.x module](http://whiteship.me/?p=13619) </span>

<span style="font-size: 11pt;">vert.x 를 설치하고 나서 모든 세팅이 되었다면 바로 그 글을 보고 실습을 해보면 될것 같은데, 글을 보고 하면서 시행착오를 겪었던 몇가지를 적으면 다음과 같다.(도움이 되라는 마음에.)</span>

<span style="font-size: 11pt;">**1. `mk, wmk` 에 대해서 **</span>

<span style="font-size: 11pt;">–  나 같은 멍청이가 또 있을까 싶은데, github에 올려주신 것 안에 `mk`와 `wmk`가 있다. `wmk`는 `mk`의 윈도우 버전인데, 역할을 gradle에 대한 사전 작업을 하는것 같다. 필자는 바보같이 이게 어떤 리눅스 혹은 윈도우 명령어인줄 알고 계속 없는 위치에서 테스트를 했는데 그러지 마시길. </span>

<span style="font-size: 11pt;">**2. log4j 문제. **</span>

<span style="font-size: 11pt;">– 사실 이것도 나한테만 나는 문제인데, 예전에 만든 서버테스트를 맥에어에서 하다 보니 /jre/ext에 log4j, slf4j를 두었었는데, 이것과 mk 에서 gradle 작업을 할때, 버전 차이로 인한 클래스 없는 문제가 생겨서 계속 exception이 떨어지는 것을 확인 할 수가 있었다. `jre/ext`에서 문제가 되는 라이브러리를 삭제하면 문제없이 된다. </span>

<span style="font-size: 11pt;">맥 혹은 유닉스 환경에서 </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">./mk tasks</span>

<span style="font-size: 11pt;">./mk eclipse</span>

</div><span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">이렇게 수행을 하게 되면 이클립스 환경에서 코딩을 하는 개발자라면 import를 통해서 [mod-sample](https://github.com/keesun/mod-sample) 를 프로젝트로 가져올수가 있다. 개인적으로 이 블로그의 자료를 보고  vert.x에서 module에 대한 글을 보니 좀더 이해가 잘 되는것 같다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 15px; line-height: 29px;">다시 한번 [mod-sample](https://github.com/keesun/mod-sample) 를 만드신 [keesun](https://github.com/keesun) 님께 감사의 말씀을 드린다. </span>



