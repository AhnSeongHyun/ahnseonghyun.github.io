---
title: 'maven log4j-1.2.16.jar 연동시 pom.xml 에러 해결.'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['dev', 'log4j-1.2.16.jar', 'logtj', 'maven', 'pom.xml 에러', '태그를 입력해 주세요.']
---


<span style="font-size: 11pt;">slf4j-log4j를 연계해서 쓰는데, [이전 포스팅](http://ash84.tistory.com/863)에서도 말했지만 slf4j와 lo44j의 버전을 제대로 맞추어야 별 탈없이 붙어서 돌아가게 되는데, 필자의 경우 아래의 버전 조합으로 현재 회사에서 사용하고 있다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">– slf4j-api.1.6.1.jar</span>

<span style="font-size: 11pt;">– slf4j-log4j12-1.6.2.jar </span>

<span style="font-size: 11pt; line-height: 29px;">– log4j-1.2.16.jar</span>

</div><span style="font-size: 15px; line-height: 29px;">  
</span>

<span style="font-size: 11pt; line-height: 29px;">slf4j의 maven 에서 별 탈 없이 제대로 해당 버전을 가져오는 반면에 log4j-1.2.16.jar 의 경우, 가져와도 pom.xml에서 에러를 일으킨다. </span>

<span style="font-size: 11pt; line-height: 29px;">  
</span>

<span style="font-size: 11pt; line-height: 29px;">  
<script src="https://gist.github.com/4393867.js"></script></span>

<span style="font-size: 15px; line-height: 29px;">  
</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><font color="#000000" face="NanumGothic, 나눔고딕, Apple Gothic, sans-serif"><span style="font-size: 11pt; line-height: 29px;">Missing artifact log4j:log4j:bundle:1.2.16</span></font>

</div><font color="#000000" face="NanumGothic, 나눔고딕, Apple Gothic, sans-serif"><span style="font-size: 15px; line-height: 29px;">  
</span></font>

<font color="#000000" face="NanumGothic, 나눔고딕, Apple Gothic, sans-serif"><span style="font-size: 11pt; line-height: 29px;">에러가 나는 이유는** <type>bundle<type>** 때문이라고 한다. 해당 부분을 지워주면 pom.xml의 에러가 사라진다. 해당 부분을 지우더라도 사용하는데는 문제가 없다. </span></font>

<font color="#000000" face="NanumGothic, 나눔고딕, Apple Gothic, sans-serif"><span style="font-size: 15px; line-height: 29px;">  
</span></font>

<font color="#000000" face="NanumGothic, 나눔고딕, Apple Gothic, sans-serif"><span style="font-size: 15px; line-height: 29px;">  
</span></font>



