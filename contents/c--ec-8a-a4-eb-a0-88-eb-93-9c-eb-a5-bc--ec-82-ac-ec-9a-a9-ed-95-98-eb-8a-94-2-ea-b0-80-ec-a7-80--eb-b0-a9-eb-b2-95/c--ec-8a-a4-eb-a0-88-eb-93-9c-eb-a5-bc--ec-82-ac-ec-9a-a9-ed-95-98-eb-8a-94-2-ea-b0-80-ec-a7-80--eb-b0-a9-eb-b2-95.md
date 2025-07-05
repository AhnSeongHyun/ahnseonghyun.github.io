---
title: '[C#] 스레드를 사용하는 2가지 방법'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['An Seong Hyun', 'c#', 'dev', 'ParameterizedThread', 'Thread', 'ThreadStart', '스레드', '안성현', '파라미터가 있는 스레드']
---


<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">프로세스와 스레드에 대한 개념은 어떤 프로그래밍 언어라 하더라두 공통으로 적용이 되는 부분입니다. C#에서 스레드를 사용하는 방식은 파라미터(Parameter)가 있냐 없냐에 따라서 달라집니다. </span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span><span style="FONT-SIZE: 11pt">**<span style="font-size: 11pt; ">파라미터(Parameter)가 없는 경우 </span>**</span></span></div><div style="text-align: justify; line-height: 2; "><span style="color: rgb(71, 71, 71);  font-size: 10pt; line-height: 2; "><span style="font-size: 11pt; ">파라미터가 없는 경우에는 간단합니다. Thread 객체를 선언해 주고, 정의하는 과정에서 ThreadStart 를 만들어주면서 스레드가 동작시킬 함수명을 적어주면 됩니다. </span></span></div><div style="text-align: justify; line-height: 2; "><span><span style="FONT-SIZE: 11pt"><span style="font-size: 11pt; ">  
</span><div style="LINE-HEIGHT:2"><span style="font-size: 11pt; ">  
</span><font color="#474747">  
<span style="font-size: 11pt; ">  
</span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="LINE-HEIGHT: 2"><span style="font-size: 11pt; ">  
</span><font color="#474747"><span style="font-size: 11pt; ">자 한번 볼까요?</span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="LINE-HEIGHT: 2"></div><script src="https://gist.github.com/3786247.js"></script>

<div style="LINE-HEIGHT:2"></div><div style="LINE-HEIGHT: 2"></div><div style="LINE-HEIGHT:2"><font color="#474747"><span style="font-size: 11pt; ">  
</span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="LINE-HEIGHT: 2"><span style="font-size: 11pt; ">  
</span><font color="#474747"><span style="font-size: 11pt; ">test 함수의 경우 void test() 가 생성되어 있어야 합니다. 위와 같이 적으면 스레드 객체를 생성하고 동작시킬 함수를 연결하고 바로 시작(Start()) 됩니다. 물론, 선언 따로, 정의 따로 시작따로 할수도 있겠죠. </span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="LINE-HEIGHT: 2"><span style="font-size: 11pt; ">  
</span><font color="#474747">  
<span style="font-size: 11pt; ">  
</span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="LINE-HEIGHT: 2"><span style="font-size: 11pt; ">  
</span><font color="#474747">![](http://ash84.net/wp-content/uploads/1/cfile10.uf.121F6F054B58285B1B6055.jpg)

<span style="font-size: 11pt; ">  
</span>

</font></div><span style="font-size: 11pt; ">  
</span>

</span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><font size="4"><span style="line-height: 29px; font-size: 15px; ">  
<span style="font-size: 11pt; ">  
</span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><font size="4"><span style="LINE-HEIGHT:2; FONT-SIZE: 15px">**<span style="font-size: 11pt; ">파라미터(Parameter)가 있는 경우 </span>**</span></font></div><div style="text-align: justify; line-height: 2; "><span style="color: rgb(71, 71, 71); font-size: 11pt; line-height: 2; font-weight: bold; ">  
</span></div><div style="text-align: justify; line-height: 2; "><span style="color: rgb(71, 71, 71); font-size: 11pt; line-height: 1.7; ">파라미터가 있는 경우도 크게 어렵지는 않습니다만 Thread 객체를 정의할때, 조금 달라집니다. ThreadStart 대신에 ParameterizedThreadStart를 사용해서 Thread 객체와 동작시킬 파라미터가 있는 함수를 연결시킵니다. </span></div><div style="text-align: justify; line-height: 2; "><span style="color: rgb(71, 71, 71); font-size: 11pt; line-height: 2; font-weight: bold; ">  
</span></div><script src="https://gist.github.com/3786251.js"></script>

<div style="text-align: justify; line-height: 2; "><span style="color: rgb(71, 71, 71);  font-size: 11pt; line-height: 2; font-weight: bold; ">  
</span></div><div style="text-align: justify; line-height: 2; "><span style="color: rgb(71, 71, 71); font-size: 11pt; line-height: 2; font-weight: bold; ">  
</span></div><div style="text-align: justify; line-height: 2; "><font size="4"><span style="LINE-HEIGHT: 2; FONT-SIZE: 15px"><span style="font-size: 11pt; ">  
</span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><font size="4"><span style="LINE-HEIGHT: 29px; FONT-SIZE: 15px"><span style="font-size: 11pt; ">위의 소스코드에서 보는것 처럼, 자신이 전달 하려는 파라미터 값에 대해서는 Start() 함수를 통해서 전달할 수가 있습니다. Start() 함수는 Overload되어있기 때문에 파라미터가 없이 Start()를 할수도 있지만, object 으로 파라미터를 전달해 주기도 합니다. </span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><font size="4"><span style="LINE-HEIGHT: 2; FONT-SIZE: 15px">  
<span style="font-size: 11pt; ">  
</span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><font size="4"><span style="LINE-HEIGHT:2; FONT-SIZE: 15px"><span style="font-size:10pt;"><span style="font-size: 11pt; ">참고로 .NET 1.1 Version 에서는 파라미터가 있는 경우에 대해서는 스레드의 지원이 안되었다고 합니다. 참고하세요^^ </span>  
<span style="font-size: 11pt; ">  
</span>  
**<span style="font-size: 11pt; ">C# 관련 포스팅 </span>**[](http://ash84.tistory.com/563)</span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; line-height: 2; "><div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="font-size: 11pt; ">  
</span><font size="4"><span style="LINE-HEIGHT: 2; FONT-SIZE: 15px"><span style="font-size:10pt;">[<span style="font-size: 9pt; ">2010/01/15 – [Technique/C/C++/C#] – [C#] 기본 메일 클라이언트 열기</span>](http://ash84.tistory.com/563)  
<span style="font-size: 9pt; ">  
</span>[<span style="font-size: 9pt; ">2010/01/26 – [Technique/C/C++/C#] – [C#] CSS 분석은 이제 내게 맡겨라. Bonesoft.CSS.dll</span>](http://ash84.tistory.com/567)  
<span style="font-size: 9pt; ">  
</span>[<span style="font-size: 9pt; ">2010/03/01 – [Technique/C/C++/C#] – [C#] Hippo Chart 사용하기</span>](http://ash84.tistory.com/582)  
<span style="font-size: 9pt; ">  
</span>[<span style="font-size: 9pt; ">2010/02/20 – [Technique/C/C++/C#] – [C#] ScrollToCaret 를 이용한 TextBox 자동 스크롤링</span>](http://ash84.tistory.com/579)  
<span style="font-size: 9pt; ">  
</span>[<span style="font-size: 9pt; ">2010/02/05 – [Technique/C/C++/C#] – [C#]매틀랩과 닷넷 C# 연결하기(Connect Matlab to .NET C#)</span>](http://ash84.tistory.com/573)  
<span style="font-size: 9pt; ">  
</span>[<span style="font-size: 9pt; ">2010/04/22 – [Technique/C/C++/C#] – [C#] WinCE InputPanel(가상 키보드) 위치 조정하기</span>](http://ash84.tistory.com/596)  
<span style="font-size: 9pt; ">  
</span>[<span style="font-size: 9pt; ">2010/03/18 – [Technique/C/C++/C#] – [C#] GPS NEMA Protocol 자료</span>](http://ash84.tistory.com/589)  
<span style="font-size: 9pt; ">  
</span>[<span style="font-size: 9pt; ">2010/07/06 – [Technique/C/C++/C#] – [C#] Bi-Direction TextBox</span>](http://ash84.tistory.com/616)  
<span style="font-size: 9pt; ">  
</span>[<span style="font-size: 9pt; ">2010/07/20 – [Technique/C/C++/C#] – [C#] Unicode To String</span>](http://ash84.tistory.com/619)  
<span style="font-size: 9pt; ">  
</span>[<span style="font-size: 9pt; ">2010/11/18 – [Technique/C/C++/C#] – [C#] 윈폼 컨트롤 박스 없이 마우스 드래그앤 드롭으로 이동.</span>](http://ash84.tistory.com/644)  
<span style="font-size: 9pt; ">  
</span>[<span style="font-size: 9pt; ">2011/02/25 – [Technique/C/C++/C#] – [C#] Click Once 배포오류 fileloadException에 대해서.</span>](http://ash84.tistory.com/676)<span style="font-size: 11pt; "> </span></span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; "><span style="font-size: 11pt; ">  
</span></div></div>

