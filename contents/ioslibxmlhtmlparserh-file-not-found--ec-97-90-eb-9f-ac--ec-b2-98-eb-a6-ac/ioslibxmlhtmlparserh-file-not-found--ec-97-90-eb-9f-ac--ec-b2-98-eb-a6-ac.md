---
title: '(iOS)libxml/HTMLparser.h file not found 에러 처리'
author: 'ash84'
pub_date: '2015-07-03'
description: '이전 포스팅에서 iOS  App  개발시, 각종 HTML 파서들을 연동하는 방법들을 소개했는데 그러한 라이브러리에 사용하는 것중 하나가 libxml2 라이브러리이다. 기본적으로 프로젝트'
featured_image: ''
tags: ['dev', 'HTML Parsing', 'HTML 파싱', 'libxml/HTMLparser file not found', 'libxml2', '아이폰 앱', '앱 개발']
---


<span style="font-size: 10pt; color: rgb(0, 0, 0); "><span style="font-size: 11pt; "><span style="font-size: 11pt; "></span><span style="font-size: 11pt; "></span><span style="font-size: 11pt; ">이전 포스팅에서 iOS  App  개발시, 각종 HTML 파서들을 연동하는 방법들을 소개했는데 그러한 라이브러리에 사용하는 것중 하나가 libxml2 라이브러리이다. 기본적으로 프로젝트 세팅에 가서 </span></span><span style="font-size: 11pt; ">다음과 같이 해주면된다. </span></span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; line-height: 2; "><span style="font-size: 11pt; color: rgb(0, 0, 0); "><span style="font-size: 11pt; ">Header Search Paths </span></span>

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">– </span><span style="color: rgb(0, 0, 0); font-family: Arial, 'Liberation Sans', 'DejaVu Sans', sans-serif; font-size: 11pt; "> </span><span style="color: rgb(0, 0, 0); font-family: Arial, 'Liberation Sans', 'DejaVu Sans', sans-serif; font-size: 11pt; ">“${SDKROOT}/usr/include/libxml2”</span>

<span style="color: rgb(0, 0, 0); font-family: Arial, 'Liberation Sans', 'DejaVu Sans', sans-serif; font-size: 11pt; "><span style="font-size: 11pt; ">–  recursive option 켜기 </span></span>

</div><div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; line-height: 2; "><font color="#000000" face="Arial, Liberation Sans, DejaVu Sans, sans-serif" size="2"><span style="line-height: 20px; font-size: 11pt; "><span style="font-size: 11pt; ">Other Link Flags</span></span></font>

<font color="#000000" face="Arial, Liberation Sans, DejaVu Sans, sans-serif" size="2"><span style="line-height: 20px; font-size: 11pt; "><span style="font-size: 11pt; ">– -lxml2 입력 </span></span></font>

</div><font color="#000000" face="Arial, Liberation Sans, DejaVu Sans, sans-serif" size="2"><span style="line-height: 20px;">  
</span></font>

<font color="#000000" face="Arial, Liberation Sans, DejaVu Sans, sans-serif" size="2"><span style="line-height: 20px;">  
</span></font>

<font color="#000000" face="Arial, Liberation Sans, DejaVu Sans, sans-serif" size="2">  
</font>

![](http://ash84.net/wp-content/uploads/1/cfile5.uf.1325C7465080181F16C495.jpg)

<font color="#000000" face="Arial, Liberation Sans, DejaVu Sans, sans-serif" size="2"><span style="line-height: 20px;">  
</span></font>

![](http://ash84.net/wp-content/uploads/1/cfile10.uf.0132A9465080181F04FF58.jpg)

<font color="#000000" face="Arial, Liberation Sans, DejaVu Sans, sans-serif" size="2"><span style="line-height: 20px;">  
</span></font>

<font color="#000000" face="Arial, Liberation Sans, DejaVu Sans, sans-serif" size="2"><span style="line-height: 2;">  
</span></font>

<font color="#000000" face="Arial, Liberation Sans, DejaVu Sans, sans-serif" size="2"><span style="line-height: 2; font-size: 11pt; ">그런데 주의할 점. Always Search User Paths 부분도 반드시 Yes로 되어 있어야 한다. 이 부분도 신경써 줘야 한다. 그리고 가급적이면, Target 설정과 Project 설정을 맞춰 주는게 좋다. 만약 개발을 하는데 디버그 단계에서 문제가 없었는데 배포(Distribution) 단계에서 문제가 생긴다면, 설정을 빨리 비교해 보는게 상책이다. </span></font>

<font color="#000000" face="Arial, Liberation Sans, DejaVu Sans, sans-serif" size="2"><span style="line-height: 20px;">  
</span></font>

<font color="#000000" face="Arial, Liberation Sans, DejaVu Sans, sans-serif" size="2"><span style="line-height: 2;"><span style="font-size: 11pt; "></span><span style="font-size: 11pt; "></span>  
</span></font>

<span style="font-size: 11pt; "></span><font color="#000000" face="Arial, Liberation Sans, DejaVu Sans, sans-serif" size="2"><span style="line-height: 20px;">  
</span></font>



