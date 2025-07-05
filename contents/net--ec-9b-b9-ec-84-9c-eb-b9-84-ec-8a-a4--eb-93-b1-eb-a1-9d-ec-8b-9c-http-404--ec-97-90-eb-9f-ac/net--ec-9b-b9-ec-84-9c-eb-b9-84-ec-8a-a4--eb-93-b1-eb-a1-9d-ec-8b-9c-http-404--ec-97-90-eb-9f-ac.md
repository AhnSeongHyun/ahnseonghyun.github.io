---
title: '[.NET] 웹서비스 등록시 HTTP 404 에러'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['Active Server Pages', 'dev', 'http404 에러', 'IIS', '웹서비스', '웹서비스 등록', '윈도우 서버 2003']
---


<span style="font-size: 11pt;">C# 으로 만든 웹서비스를 서버에 등록해서 테스트 해야 하는 경우가 많은데</span>  
<span style="font-size: 11pt;">  
</span>  
<span style="font-size: 11pt;">그러한 경우, 간혹, 윈도우 서버 2003 을 쓰다보면, </span>  
<span style="font-size: 11pt;">  
</span>  
**<font color="#666699"><span style="font-size: 11pt;">HTTP 404 </span></font>**<span style="font-size: 11pt;">에러가 나곤한다. </span>  
<span style="font-size: 11pt;">  
</span>

![사용자 삽입 이미지](http://ash84.net/wp-content/uploads/1/47d4e8bd957ec36.jpg)

<span style="font-size: 11pt;">  
</span>  
<u><font color="#d41a01"><span style="font-size: 11pt;">즉, 자신이 만든 웹서비스(Service.asmx)를 IIS 서버에 등록해서, </span>  
<span style="font-size: 11pt;">  
</span>  
<span style="font-size: 11pt;">서버의 웹 브라우저를 통해서 웹서비스 정보를 보려고 할때, </span>  
<span style="font-size: 11pt;">  
 (웹서비스의 주소를 알아야, Visual studio 에서 웹참조를 할수 있다.)</span>  
<span style="font-size: 11pt;">  
</span></font></u>  
<span style="font-size: 11pt;">  
 에러가 발생하는데 , 이러한 에러는 다음과 같이 해결할 수 있다.</span>  
<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">  
</span>  
<span style="font-size: 11pt;">IIS 관리 창을 열어보면, </span>  
<span style="font-size: 11pt;">  
</span>  
**<font color="#008000"><span style="font-size: 11pt;">[웹 서비스 확장]</span></font>**<span style="font-size: 11pt;">을 누른다. </span>  
<span style="font-size: 11pt;">  
</span>  
<span style="font-size: 11pt;">그 안에 보면 </span>

![사용자 삽입 이미지](http://ash84.net/wp-content/uploads/1/47d4e8be9b6e83C.jpg)

<span style="font-size: 11pt;">  
</span>  
<span style="font-size: 11pt;">  
</span>

<div style="text-align: justify;"><font color="#d41a01">**<span style="font-size: 11pt;">[ Active Server Pages ] 금지됨 –> 허용됨</span>  
<span style="font-size: 11pt;">  
 [ ASP .NET v2.0.50727 ] 금지됨 –> 허용됨</span>**</font><span style="font-size: 11pt;"></span></div><span style="font-size: 11pt;">  
</span>  
<span style="font-size: 11pt;">으로 바꾸어 주면, 자신이 올린 웹서비스를 웹브라우저를 통해서 문제 없이 확인할수 있다^^</span>  
<span style="font-size: 11pt;">  
</span>  
<span style="font-size: 11pt;">  
</span>

<div id="daum_book" style="clear: both; border: 1px solid rgb(238, 238, 238); padding: 10px; margin: 5px 0px 0px; width: 94%; text-align: justify;">[![](http://photo-book.hanmail.net/images/book/large/450/l9788975602450.jpg)<span style="font-size: 11pt;"></span>](http://book.daum.net/bookdetail/book.do?bookid=KOR9788975602450) [<span style="font-size: 11pt;">윈도우 서버 2003 무작정 따라하기 (CD-ROM 포함)</span>](http://book.daum.net/bookdetail/book.do?bookid=KOR9788975602450)<span style="font-size: 11pt;"></span>[<span style="font-size: 11pt;">상세보기</span>](http://book.daum.net/bookdetail/book.do?bookid=KOR9788975602450)<span style="font-size: 11pt;">  
</span><div id="p_author_area" style="MARGIN-BOTTOM: 8px"><span id="p_author" style="font-size: 11pt;">박흥선</span><span style="font-size: 11pt;"> 지음 | </span><span id="p_publish" style="font-size: 11pt;">길벗</span><span style="font-size: 11pt;"> 펴냄 </span></div><span style="font-size: 11pt;">  
</span>

<div style="OVERFLOW: hidden; HEIGHT: 52px"><span id="p_description" style="margin: 2px; font-style: normal; font-variant: normal; font-weight: normal; font-size: 9pt; line-height: 1.5; font-family: Dotum, sans-serif;">윈도우 서버 2003의 전반적인 운영체제를 쉽게 풀어쓴 책. 서버 구축에서부터 액티브 디렉터리 활용까지 핵심적인 관리 노하우와 테크닉을 상세하게 설명하고 있다. 네트워크 관리자가 겪는 실무를 중심으로 열두 가지 윈도우 서버 구축 과정을 알려준다. (윈도우 서버 2003 180일 평가판 설치 CD와 유틸리티 CD 제공)</span><span style="font-size: 9pt;"></span></div></div><span style="font-size: 9pt;"></span>



