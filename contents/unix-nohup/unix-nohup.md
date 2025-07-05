---
title: '(UNIX) nohup ?'
author: 'ash84'
pub_date: '2013-01-24'
description: ''
featured_image: ''
tags: ['nohup', 'nohup.out', 'unix', '노홉', '유닉스']
---


<span style="font-size: 11pt;">**nohup**</span>

<span style="font-size: 11pt;">리눅스, 유닉스에서 프로그램을 데몬처럼 실행하고 싶을때 사용하는것인데, </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">명령어 & </span>

<span style="font-size: 11pt;">nohup shell.sh &</span>

</div><span style="font-size: 11pt;">이렇게 호출한다고 한다. nohup을 사용하려면 해당 실행하려는 **파일의 퍼미션이 755 이상 상태**여야만 한다고 한다. nohup의 종료방법은 다음과 같다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">1.** “ps -ef |grep 쉘 스크립트 파일명” **이렇게 하면 실행한 쉘 스크립트의 프로세스 확인</span>

<span style="font-size: 11pt;">2. 그 상태에서 **“kill -9 PID번호”** 명령으로 해당 프로세스를 종료.</span>

</div><span style="font-size: 11pt;">로그의 경우에는 실행한 위치에서 자동으로 `nohup.out`파일이 생성되며 printf(), System.out.println() 내용이 해당 파일에 들어가게 된다. 프로그래머 입장에서는 `tail -f nohup.out` 으로 걸어서 보면 되니까 편하긴 하다. 종료하는 부분이 조금 번거로운. </span>



