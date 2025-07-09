---
title: '[C#] Winform(윈폼) 제목표시줄에 안뜨게 하기'
author: 'ash84'
pub_date: '2009-11-24'
description: '![](http://ash84.net/wp-content/uploads/1/cfile29.uf.134855014B0BEAB21F9F39.jpg)Form1과 Form'
featured_image: ''
tags: ['An Seong Hyun', 'c#', 'dev', 'ShowTaskbar', 'Windows Application', 'winform', '속성', '안성현', '윈폼', '제목표시줄', '제목표시줄 표시', '프로그래밍']
---


<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><figure class="wp-caption aligncenter" style="width: 484px">![](http://ash84.net/wp-content/uploads/1/cfile29.uf.134855014B0BEAB21F9F39.jpg)<figcaption class="wp-caption-text">Form1과 Form2가 모두 표시됨.</figcaption></figure></span></span>

<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">C# Windows Application(윈도우즈 어플리케이션)을 개발 하다보면 자연스럽게 많은 메시지 창 및 자식창을 생성하게 됩니다. MessageBox(메시지박스)역시 하나의 자식 윈폼이라고 볼수 있겠지요. 그런데 메시지 박스를 뛰운 경우에는 하나의 어플리케이션 이름만 TaskBar(제목표시줄)에 표시되지만, Form2를 띄운 경우에는 TaskBar(제목표시줄)에 Form2의 이름이 같이 보여지게 됩니다. 사실상 메인 프로그램 폼 만이 제목표시줄에 보여져야 하는데, 그렇다면 과연 이럴땐 어떻게 해야 할까요?</span></span></span>

<div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">﻿</span></span></font><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">﻿</span></span></font><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">﻿</span></span></font><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">﻿ </span></span></font></span></span></span></span>  
**<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">ShowTaskbar 속성을 이용하라!!</span></span>**<div style="BORDER-LEFT: #000000 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: #e8e8e8; PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, Sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: #fff; PADDING-TOP: 3px"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 1pt"></span></span></span></span></span></span></span></span></div>  
<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><figure class="wp-caption aligncenter" style="width: 487px">![](http://ash84.net/wp-content/uploads/1/cfile9.uf.1444DE044B0BEAFE475B79.jpg)<figcaption class="wp-caption-text">Form2의 ShowTaskBar = False;</figcaption></figure></span></span><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">Windows Application(윈도우즈 어플리케이션) 개발시, 디자인모드(Form.cs 파일 클릭)에서 디자인 창(폼)을 클릭하면 자동으로 해당 컨트롤에 대한 속성과 이벤트 창이 보여지게 됩니다. 이때 속성(Propertise) 중에서 ShowTaskbar를 False 로 설정하게 되면, 해당창의 이름이 제목표시줄에 보여지지 않게 됩니다. </span></span></span>

<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><figure class="wp-caption aligncenter" style="width: 605px">![](http://ash84.net/wp-content/uploads/1/cfile25.uf.1544EB044B0BEB2F2DECEB.jpg)<figcaption class="wp-caption-text">Form1 만 표시됨. </figcaption></figure></span></span>

**<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">메인 폼에는 무조건 True</span></span>**

<div style="BORDER-LEFT: #000000 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: #e8e8e8; PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, Sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: #fff; PADDING-TOP: 3px"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 1pt"></span></span></span></span></span></span></span></span></div>  
<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">메인폼에 ShowTaskbar 속성을 False로 두게 되면, 사실상 사용자는 혼란을 겪게 됩니다. 보통의 사용자들은 제목표시줄을 통해서 현재 실행중인 프로그램을 인지하게 되는데, 보이지 않기 때문에 실행되고 있지 않다고 생각하기 때문이죠. 그렇기 때문에 특수한 목적(?)이 아니라면, 메인 폼은 그냥 True로 유지하는 것이 좋습니다. </span></span></span><font color="#c8056a"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">ps) 매번 너무 기본적인 것만, 소개하는것 같네요^^; 그래두 많은 분들께 도움이 됐으면 좋겠습니다. </span></span></span>  
</font>

</div></div></div>  
<div style="TEXT-ALIGN: justify">  
<div>  
<div style="LINE-HEIGHT: 1.7"></div></div></div>

