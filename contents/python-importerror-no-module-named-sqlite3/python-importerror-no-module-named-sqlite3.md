---
title: '[Python] ImportError: No module named _sqlite3'
author: 'ash84'
pub_date: '2012-06-23'
description: '파이썬에서 자주 사용하는것 중에 하나가 sqlite3 라이브러리인데, 해당 라이브러리를 사용하기 위해서는 파이썬 소스 첫 머리에서 import sqlite 문을 넣어 주어야 한다. 그런데 import 를 한후에 실행을 시켜보면, 다음과 같은 에러가 떨어진다.'
featured_image: ''
tags: ['dev', 'importError', 'No module named _sqlite3', 'sqlite3', 'Python']
---
<span style="font-size: 11pt; ">파이썬에서 자주 사용하는것 중에 하나가 sqlite3 라이브러리인데, 해당 라이브러리를 사용하기 위해서는 파이썬 소스 첫 머리에서 import sqlite 문을 넣어 주어야 한다. </span><span style="font-size: 11pt; line-height: 2; ">그런데 import 를 한후에 실행을 시켜보면, 다음과 같은 에러가 떨어진다. </span>

<script src="https://gist.github.com/2978144.js?file=gistfile1.py"></script>

<span style="font-size: 11pt; ">살펴보면, sqlite 에 대한 모듈이름을 찾지 못한다는 것인데, 해당 문제가 발생한 원인은 리눅스에 파이썬의 하위버전이 설치되어 있는데, 상위버전으로 업그레이드를 했을 경우, 제대로 되지 않으면 sqlite 모듈이 설치되지 않는 문제인것으로 확인 되었다. 그래서 아래와 같이 yum 명령어를 이용해서 sqlite를 강제로 설치해 주었다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; ">**yum install -y sqlite-devel.x86_64**

</div><span style="font-size: 11pt; ">설치해 주니 잘 되는것을 확인했다. 굳이 어려운 부분은 아니지만 필자는 이 문제때문에 2일간 ssh 창만 바라보았는데 같은 문제를 겪는 분들이 있으면 참고하시길. </span>

[2012/10/11 – [Programming/Python] – [Python] sqlite3 를 손쉽게 쓰도록 만든 클래스](http://ash84.tistory.com/834)

[2012/11/07 – [Programming/iOS] – (iOS) iOS앱 – mysql 연동, 이렇게 하면 쉽다.](http://ash84.tistory.com/846)

[  
](http://ash84.tistory.com/834)



