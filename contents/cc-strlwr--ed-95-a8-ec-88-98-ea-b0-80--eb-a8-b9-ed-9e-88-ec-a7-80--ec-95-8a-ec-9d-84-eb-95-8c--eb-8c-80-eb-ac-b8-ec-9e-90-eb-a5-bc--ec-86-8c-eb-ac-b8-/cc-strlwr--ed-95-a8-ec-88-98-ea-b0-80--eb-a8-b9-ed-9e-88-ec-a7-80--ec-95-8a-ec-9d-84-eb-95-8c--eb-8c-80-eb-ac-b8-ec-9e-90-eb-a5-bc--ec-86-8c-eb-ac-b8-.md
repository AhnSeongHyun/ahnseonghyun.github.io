---
title: '[C/C++] strlwr() 함수가 먹히지 않을때? 대문자를 소문자로.'
author: 'ash84'
pub_date: '2011-10-28'
description: ''
featured_image: ''
tags: ['aix', 'C#', 'dev', 'strcasecmp', 'strlwr', '대문자를 소문자로']
---
<div><div></div><div style="line-height: 1.5; "></div><div style="line-height: 2; "><div class="txc-textbox" style="border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-top-color: rgb(203, 203, 203); border-right-color: rgb(203, 203, 203); border-bottom-color: rgb(203, 203, 203); border-left-color: rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; "><span style="font-size: 11pt; "><span style="font-family: Dotum; "><span style="font-size: 11pt; ">매일매일 개발하는 소스코드를 올리고 있습니다. 원래는 프로젝트가 끝나고 올리려고 했으나, 그러다 보니 까먹는 경우가 있어서 이렇게 매일매일 올리는 소스코드 입니다. 제가 쓴 소스코드의 문제 혹은 개선점이 있으면 언제든지 댓글 달아 주세요 </span></span></span>

<span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; ">  
</span>

<div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify;"><span style="font-size: 11pt; ">  
</span><font color="#000000" style="font-family: Dotum; font-size: 15px; line-height: 29px; "><span style="font-size: 11pt; ">strlwr()</span></font><span style="font-family: Dotum; line-height: 29px; font-size: 11pt; "> 이라는 함수는 </span><font color="#0686a8" style="font-family: Dotum; font-size: 15px; line-height: 29px; "><span style="font-size: 11pt; "><string.h></span></font><span style="font-family: Dotum; line-height: 29px; font-size: 11pt; "> 에 있는 함수로 대문자를 소문자로 바꿔주는 함수이다. 그런데 사실 string.h 에 있는 모든 함수들이 모든 환경에서 작동하는 것이 아니다. 본인이 확인할 결과, </span><font color="#e31600" style="font-family: Dotum; font-size: 15px; line-height: 29px; "><span style="font-size: 11pt; ">AIX 서버에서는 몇몇의 함수들이 개발자가 의도하는 대로 움직여 주지 않는다. </span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span><span style="font-size: 11pt; "> </span></font><font face="Dotum" size="2"><span style="line-height: 29px; font-size: 11pt; ">예를 들면, strcasecmp() 함수는 비교를 대소문자 구별없이 해 주는 함수인데, 그 부분은 작동을 하지만, 한글의 경우 간간히 작동하지 않는 현상을 발견했다. 사실 아래의 함수는 그로 인해서 만들게 되었다. strlwr() 함수가 안되기 떄문에 대문자를 소문자로 바꿔주는 함수를 만들었고 사실은 이 다음에 strcmp()함수를 호출함으로써 strcasecmp() 함수의 의도를 풀어 놓은 것이다. </span></font>

</div></div><script src="https://gist.github.com/3260848.js"></script>



