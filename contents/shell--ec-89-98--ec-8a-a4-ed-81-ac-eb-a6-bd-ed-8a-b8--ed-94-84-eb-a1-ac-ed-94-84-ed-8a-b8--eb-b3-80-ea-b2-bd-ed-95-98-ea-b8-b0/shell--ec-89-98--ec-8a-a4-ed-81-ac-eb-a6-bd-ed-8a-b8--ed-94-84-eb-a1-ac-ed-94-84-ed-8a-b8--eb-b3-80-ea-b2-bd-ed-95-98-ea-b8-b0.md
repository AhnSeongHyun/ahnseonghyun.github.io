---
title: '(shell) 쉘 스크립트 프롬프트 변경하기'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['change shell prompt', 'dev', 'Shell', '쉘', '쉘 프로프트 변경', '프롬프트']
---


<span style="font-size: 11pt;">쉘에서 프롬프트를 변경할일이 있을까 싶기도 하지만 어떤 서버의 경우 요상하리 만큼 로그인후 쉘의 길이가 긴 경우가 있다. 그냥 쓰면 될껄 왜 변경하느냐 하는 분도 있겠지만 길이가 길면 터미널 창에 잘 들어오지도 않고 자바 같은 경우 실행시 좀 짜증나게 되서. 쉘 변경하는 내용을 올린다. </span>

**<span style="font-size: 11pt;">어디서?</span>**

<span style="font-size: 11pt;">필자 같은 경우는 본인 home 디렉토리의 자기 계정내에 있는 .bashrc 에서 수행하였다. 여기서 수행한 이유는 일단은 전체적으로 같은 쉘을 쓸지 말지는 모르는 상황이어서 일단은 내 계정에 대해서는 수행하고자 .bashrc 에서 수정작업을 진행하였다. </span><span style="font-size: 11pt; line-height: 2;">해당 서버를 사용하는 전체에 대한 수정작업을 하고 싶다면, etc/bashrc(bash.basrc) 에서 아래의 작업을 해주면 될것으로 생각된다.(필자역시 해보진 않았다.)</span>

<span style="font-size: 9pt; line-height: 2;">  
</span>

<span style="font-size: 9pt; line-height: 2;">  
</span>

<span style="font-size: 9pt; line-height: 2;">  
</span>

**<span style="font-size: 11pt;">어떻게?</span>**

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; line-height: 2;"><span style="font-size: 11pt;">ash84@b4c2ce95-a9bc-489d-a2b1-3c8cb0bb13f1:~$</span>

</div><span style="font-size: 11pt;">원래 내 계정의 쉘 프로프트이다. 보기만 해도 답답하다. ash84 라는 아이디 다음에 오는 일련의 문자와 숫자들은 도데체 무엇인지 모르겠지만 일단 내가 원하는 것은 현재 계정과 경로만 표시되기를 원했다. .bashrc 를 열어서 제일 하단에 아래의 스크립트를 추가했다. </span>

<span style="font-size: 11pt;"></span>

<script src="https://gist.github.com/AhnSeongHyun/5943257.js"></script><span style="font-size: 11pt;"></span>

<span style="font-size: 11pt;">저장한후, 닫고 나서 바로 다시 로그인을 해서 프롬프트를 확인해 보았다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt; line-height: 2;">ash84@:~$ cd nanpa/</span>

<span style="font-size: 11pt;">ash84@:~/nanpa$</span>

</div><span style="font-size: 11pt;">이상한 문자열이 없어진것을 확인 할 수가 있다. 그리고 더불어서 프롬프트의 색도 빨간색으로 변경을 하였다. 쉘쪽에서 작업을 많이하면 아무래도 검은 바탕에 약간의 색으로 구분할수 있게 하는 편이 좋아서 색도 변경하였다. </span>

<span style="font-size: 11pt;">그렇다면, `PS1` 과 그 문자들이 의미하는 것은 무엇일까?</span>

<span style="font-size: 11pt;">프롬프트의 제어는 쉘 상에서 특별한 변수에 의해서 제어가 된다. `PS1`, `PS2`, `PS3`, `PS4` 변수가 그런것들인데, 각각의 의미하는 바는 아래와 같다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">PS1 – Primary Prompt String(default value : \s-\v$)</span>

<span style="font-size: 11pt;">PS2 – Secondary Prompt String(default value : >)</span>

<span style="font-size: 11pt;">PS3 – select command를 위한 prompt</span>

<span style="font-size: 11pt;">PS4 – shell script 를 디버깅 모드에서 실행시 사용되는 prompt</span>

</div><span style="font-size: 11pt;">각각의 변수를 아래와 같이 확인해 보면 현재 어떤 변수에 어떤값이 할당되어 있는지를 알 수 있다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">echo $PS1</span>

</div><span style="font-size: 11pt;">여기서 우리가 대상으로 하는 것은 로그인을 한후 일반적으로 나오는 프롬프트이기 때문에 당연히 `PS1`을 대상으로 하였고 위에서 수정한 부분 역시 `PS1`을 대상으로 하였다. 자, 이제 그렇다면 `PS1`에 설정한 문자는 어떤 의미일까?</span>

<table align="justify" border="0" cellpadding="0" cellspacing="0" class="txc-table" style="border:none;border-collapse:collapse;;font-family:돋움;font-size:12px" width="604"><tbody><tr><td style="width: 95px; height: 24px; border: 1px solid rgb(204, 204, 204); background-color: rgb(218, 217, 255);"> 설정 문자  

</td><td style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-top-width: 1px; border-top-style: solid; border-top-color: rgb(204, 204, 204); background-color: rgb(218, 217, 255);">** 의미  **

</td></tr><tr><td style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \a

</td><td style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> an ASCII bell character(07) 

</td></tr><tr><td style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \d

</td><td style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> the date in “Weekday Month Date” format (e**.**g., “Tue May 26”)

</td></tr><tr><td style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \D{format}

</td><td style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> format의 지정에 따른 date, strftime(3)

</td></tr><tr><td style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \e

</td><td style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> an ASCII escape character(033)

</td></tr><tr><td style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \h

</td><td style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> the hostname up to the first ‘.’

</td></tr><tr><td style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \H

</td><td style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> the hostname 

</td></tr><tr><td style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \j

</td><td style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> 쉘에 의해서 관리되는 현재 job의 수  

</td></tr><tr><td rowspan="1" style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \l</td><td rowspan="1" style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> 쉘의 터미널 디바이스 이름의 basename 

</td></tr><tr><td rowspan="1" style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \n</td><td rowspan="1" style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> newline 

</td></tr><tr><td rowspan="1" style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \r</td><td rowspan="1" style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> carriage return 

</td></tr><tr><td rowspan="1" style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \s</td><td rowspan="1" style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> 쉘의 이름 </td></tr><tr><td rowspan="1" style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \t

</td><td rowspan="1" style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> 24-hour, 현재시간,  HH:MM:SS

</td></tr><tr><td rowspan="1" style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \T

</td><td rowspan="1" style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> 12-hour, 현재시간, <span style="font-size: 9pt; line-height: 2;">HH:MM:SS</span>

</td></tr><tr><td rowspan="1" style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \@</td><td rowspan="1" style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> 12-hour, 현재시간, am/pm  

</td></tr><tr><td rowspan="1" style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \A

</td><td rowspan="1" style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);">  24-hour, 현재시간,  HH:MM

</td></tr><tr><td rowspan="1" style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \u

</td><td rowspan="1" style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> 현재 사용자 이름  </td></tr><tr><td rowspan="1" style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \v

</td><td rowspan="1" style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> bash 의 버전  

</td></tr><tr><td rowspan="1" style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \V

</td><td rowspan="1" style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> bash 의 릴리즈

</td></tr><tr><td rowspan="1" style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \w</td><td rowspan="1" style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> 현재 working 디렉토리</td></tr><tr><td rowspan="1" style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \W</td><td rowspan="1" style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> 현재 working 디렉토리의 basename</td></tr><tr><td rowspan="1" style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \!</td><td rowspan="1" style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> the history number of this command 

</td></tr><tr><td rowspan="1" style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \#</td><td rowspan="1" style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> the command number of this command 

</td></tr><tr><td rowspan="1" style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \$

</td><td rowspan="1" style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> if the effective UID is 0, a #, otherwise a $ 

</td></tr><tr><td rowspan="1" style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \nnn

</td><td rowspan="1" style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> the character corresponding to the octal number nnn

</td></tr><tr><td rowspan="1" style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \\</td><td rowspan="1" style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> backslash </td></tr><tr><td rowspan="1" style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \[</td><td rowspan="1" style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> begin a sequence of non-printing characters, which could be used to embed a terminal control sequence into the prompt</td></tr><tr><td rowspan="1" style="width: 95px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"> \]</td><td rowspan="1" style="width: 508px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"> end a sequence of non-printing characters</td></tr></tbody></table><span style="font-size: 11pt;">PS1=’\[ \e [0;31m \] \u@:\w$ \[ \e[m\] ‘</span>

<span style="font-size: 11pt;">`PS1` 설정한 부분에서 [0;31] 이 부분은 색을 넣은 부분은데, 색 처리에 대한 코드는 아래의 Reference 에서 색처리 관련 링크를 찾아보면 이해가 될것이다. 위의 설정에서 \u@\w 를 설정함으로써 간단하게 현재 사용자와 현재 디렉토리를 보여주고 있는 것이다. </span>

<span style="font-size: 11pt;">쉘 프롬프트 수정에 대해서 조사하면서 리눅스 쉘에 대해서 모르는게 참 많다는 생각이 들었고 .bashrc 를 통해서 다양한 작업이 가능하겠구나 하는 생각이 들었다. 쉘은 쉘일 뿐이지만 그래두 커스텀을 원하는 개발자가 있다면 참고하시길. </span>

<span style="font-size: 11pt;">**Reference **</span>

<span style="font-size: 11pt;">–</span>[<span style="font-size: 11pt;"> How to : Change/Setup bash custom prompt(PS1)</span>](http://www.cyberciti.biz/tips/howto-linux-unix-bash-shell-setup-prompt.html)

<span style="font-size: 11pt;">– </span>[<span style="font-size: 11pt;">BASH Shell: Change The Color of My Shell Prompt Under Linux or UNIX</span>](http://www.cyberciti.biz/faq/bash-shell-change-the-color-of-my-shell-prompt-under-linux-or-unix/)

 



