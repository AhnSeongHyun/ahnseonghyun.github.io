---
title: '[C/C++]  IsHangul(char * input_text) 입력 문자열 한글 판단.'
author: 'ash84'
pub_date: '2011-11-24'
description: ''
featured_image: ''
tags: ['C/C++', 'Cleancode', 'C언어', 'dev', 'IsHangul()', '문자열', '클린코드', '한글']
---


<div><div></div><div style="line-height: 1.5; "></div><div style="line-height: 2; "><div class="txc-textbox" style="border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-top-color: rgb(203, 203, 203); border-right-color: rgb(203, 203, 203); border-bottom-color: rgb(203, 203, 203); border-left-color: rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; "><span style="font-size: 11pt; ">매일매일 개발하는 소스코드를 올리고 있습니다. 원래는 프로젝트가 끝나고 올리려고 했으나, 그러다 보니 까먹는 경우가 있어서 이렇게 매일매일 올리는 소스코드 입니다. 제가 쓴 소스코드의 문제 혹은 개선점이 있으면 언제든지 댓글 달아 주세요 </span>

<span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 11px;  "><span style="font-family: Dotum; "><span style="font-size: 11pt; "><span style="font-family: Dotum; "><span style="font-size: 11pt; ">뿌리깊은 나무를 본 영향인지 모르겠지만, 아무튼 최근에 소스분석을 하면서 느낀점은 한글인지 여부를 &0x80으로 if 문에 바로 쓰시는 분들이 계신데,그렇게 쓰면 코드가 clean 하지가 않고 해당 코드에 대한 의미를 알지 못하는 다른 분들이 볼때는 창피한 코드가 될수 있습니다. 조금은 번거로울수 있지만, 함수로 빼서 명확한 이름을 할당 함으로써 다른 개발자로 하여금 의미 혼동이 없게 하는 방법을 사용합니다. 보기좋은 떡이 먹기도 좋은것 처럼, 깨끗한 코드가 당신이 어떤 프로그래머인지를 말합니다. </span></span></span></span></span></div><div style="text-align: justify;"><span style="font-size: 13px; line-height: 19px; "></span>

</div><script src="https://gist.github.com/3263926.js"></script>



