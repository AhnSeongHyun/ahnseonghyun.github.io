---
title: '[펌]  Smart Client 웹에 embedded 하는 부분.'
author: 'ash84'
pub_date: '2008-04-25'
description: ''
featured_image: ''
tags: ['c#', 'dev', 'smart client .net']
---


<div id="Lecture_Source">  
<table border="0" cellpadding="5" cellspacing="1" id="Table1" name="Table1" width="100%">  
<tbody>  
<tr>  
<td align="left" style="BORDER-RIGHT: buttonface 0px solid; BORDER-TOP: buttonface 1px solid; BORDER-LEFT: buttonface 0px solid; BORDER-BOTTOM: buttonface 0px solid">  
<table border="0" cellpadding="0" cellspacing="0" id="Table2" width="100%">  
<tbody>  
<tr>  
<td width="140">[![](http://www.hoons.kr/img/hoonsbanner1.gif)](http://www.hoonsbara.com/)</td>  
<td>  
<table border="0" cellspacing="5" id="Table5" width="100%">  
<tbody>  
<tr>  
<td><span id="_ctl0_lblMainCate">[<span id="lblCate">SmartClient 프로그래밍</span>]</span></td></tr>  
<tr>  
<td>![](http://www.hoons.kr/img/arrow.gif)  <span id="lblTitle" style="FONT-WEIGHT: bold; FONT-SIZE: 12pt; COLOR: darkmagenta">[HOONS] (5) 실전 #2 – 윈도우 컨트롤 만들기</span></td></tr></tbody></table></td></tr></tbody></table></td></tr>  
<tr>  
<td align="right" style="BORDER-RIGHT: buttonface 0px solid; BORDER-TOP: buttonface 0px solid; BORDER-LEFT: buttonface 0px solid; BORDER-BOTTOM: buttonface 1px solid">  
<table style="BORDER-RIGHT: buttonface 1px solid; BORDER-TOP: buttonface 1px solid; BORDER-LEFT: buttonface 1px solid; BORDER-BOTTOM: buttonface 1px solid">  
<tbody>  
<tr>  
<td>  
<table border="0" cellpadding="0" cellspacing="7">  
<tbody>  
<tr>  
<td> **작성자** : <span id="lblWriterName">박경훈</span></td>  
<td> **작성일** : <span id="lblWriteDate">2006-09-01 오후 3:03:34</span></td></tr>  
<tr>  
<td> **E-mail** : <span id="lblWriterMail">hoonsbara (at) hotmail.com</span></td>  
<td>** Homepage** : <span id="lblWriterHomepage">[http://blog.hoons.kr](http://blog.hoons.kr/)</span></td></tr></tbody></table></td></tr></tbody></table></td></tr>  
<tr>  
<td>  
<table border="0" cellspacing="5" id="Table5" width="100%">  
<tbody>  
<tr>  
<td style="PADDING-RIGHT: 10px; BORDER-TOP: buttonface 0px solid; PADDING-LEFT: 10px; PADDING-TOP: 10px; BORDER-BOTTOM: buttonface 1px solid"><font face="굴림">  
</font>**<font color="#330000">[스마트 클라이언트(Smart Client) 강좌 순서]</font>**

<table border="1" bordercolordark="white" bordercolorlight="black" cellspacing="0" id="Table1" style="WIDTH: 592px; COLOR: #000000">  
<tbody>  
<tr>  
<td>[(1) 스마트 클라이언트는 무엇인가?](http://www.hoons.kr/Lectureview.aspx?key=Lecture&LECCATE_IDX=29&ref=1&lecture_idx=239)  
[(2) 코드 엑세스 보안(Code Access Security)](http://www.hoons.kr/Lectureview.aspx?key=Lecture&LECCATE_IDX=29&ref=1&lecture_idx=240)  
[(3) 스마트 클라이언트의 주요이슈와 닷넷 2.0에서의 대안](http://www.hoons.kr/Lectureview.aspx?key=Lecture&LECCATE_IDX=29&ref=1&lecture_idx=241)  
[(4) 실전 #1 – 웹 서비스 만들기](http://www.hoons.kr/Lectureview.aspx?key=Lecture&LECCATE_IDX=29&ref=1&lecture_idx=242)  
[**<font color="#009999">(5) 실전 #2 – 윈도우 컨트롤 만들기</font>**](http://www.hoons.kr/Lectureview.aspx?key=Lecture&LECCATE_IDX=29&ref=1&lecture_idx=243)  
[(6) 실전 #3 – 자동 보안설정 프로그램 만들기](http://www.hoons.kr/Lectureview.aspx?key=Lecture&LECCATE_IDX=29&ref=1&lecture_idx=244)  
[(7) 실전 #4 – 클릭온스를 이용한 보안설정 프로그램 배포](http://www.hoons.kr/Lectureview.aspx?key=Lecture&LECCATE_IDX=29&ref=1&lecture_idx=245)</td></tr></tbody></table>  
<span lang="EN-US"><span lang="EN-US"><font face="굴림">이제 웹 브라우저에 임베디드(포함시킬) 될 컨트롤을 만들어 보도록 하겠다. 이 컨트롤은 먼저 서버에서 클라이언트로 배포한 후에 클라이언트에서 서버의 웹 서비스를 직접 호출하게 된다. 그리고 전달받은 데이터를 이 컨트롤에서 보여주게 될 것이다. 다음 그림을 보면 전체적인 아키텍쳐를 이해할 수 있을 것이다.![](http://www.hoons.kr/hoons/lecture/SmartClient/26-030.jpg)  
 [스마트 클라이언트의 전체 구조]

윈도우 품에 대한 선수 지식이 있어야 한다. 하지만 여기서 구현할 컨트롤은 아주 간단한 컨트롤이기 때문에 다음 진행사항을 잘 따라 한다면 쉽게 데이터 그리드 뷰를 만들 수 있을 것이다. 기존 프로젝트에 Windows 컨트롤 라이브러리 프로젝트를 하나 추가하도록 하겠다.

![](http://www.hoons.kr/hoons/lecture/SmartClient/26-031.jpg)  
 [Windows 컨트롤 라이브러리 프로젝트 생성]

 UserControl의 이름을 GridControl로 변경하였다.

![](http://www.hoons.kr/hoons/lecture/SmartClient/26-032.jpg)  
 [GridControl]

그럼 이제 이 UserControl에 데이터그리드뷰 컨트롤을 추가해 보도록 하자.

![](http://www.hoons.kr/hoons/lecture/SmartClient/26-033.jpg)  
 [도구상자]

그리드뷰를 추가하면 폼의 크기를 다음과 같이 늘려 본다.

![](http://www.hoons.kr/hoons/lecture/SmartClient/26-034.jpg)  
 [데이터 그리드뷰]

</font><font face="굴림">데이터를 가져오기 전에 할 UI 준비는 끝났다. 이제 컨트롤이 로드 되는 그 시간에 웹서비스를 호출해서 데이터를 바인딩을 시켜주어야 한다. 먼저 Load 이벤트를 만들어 보도록 하겠다. GridControl 속성에서 Load를 더블 클릭 하도록 하자.![](http://www.hoons.kr/hoons/lecture/SmartClient/26-035.jpg)  
 [Load 이벤트]

 그럼 다음과 같은 로드 이벤트가 만들어 질 것이다.

</font></span>  
<table bgcolor="#efefef" border="1" bordercolordark="white" bordercolorlight="black" cellpadding="5" cellspacing="0" id="Table10" width="100%">  
<tbody>  
<tr>  
<td><font size="2"><span lang="EN-US" style="COLOR: blue; FONT-FAMILY: 돋움체; mso-hansi-font-family: 'Times New Roman'; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes"><span lang="EN-US" style="COLOR: black; FONT-FAMILY: 돋움체; mso-hansi-font-family: 'Times New Roman'; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">  
<span lang="EN-US" style="COLOR: blue; FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">private</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes"><span style="COLOR: blue">void</span> GridControl_Load(<span style="COLOR: blue">object</span> sender, <span style="COLOR: teal">EventArgs</span> e)  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">{  
</span><span lang="EN-US" style="FONT-SIZE: 10pt; FONT-FAMILY: 굴림; mso-no-proof: yes; mso-bidi-font-family: 'Times New Roman'; mso-ansi-language: EN-US; mso-fareast-language: KO; mso-bidi-language: AR-SA">}</span>

</span></span></font></td></tr></tbody></table>  
<span lang="EN-US" style="FONT-FAMILY: 굴림"></span>

Load

</span><span style="FONT-FAMILY: 굴림">이벤트에서는 웹서비스의 데이터를 가져온 다음에 그리드에 바인딩을 하는 작업을 하게 된다<span lang="EN-US">. </span>다음 그림을 참고하면 쉽게 이해할 수 있을 것이다<span lang="EN-US">. <?xml:namespace prefix = o /?>
</span></span>  
![](http://www.hoons.kr/hoons/lecture/SmartClient/26-036.jpg)<font face="굴림">  
 [<span lang="EN-US" style="FONT-SIZE: 10pt; FONT-FAMILY: 굴림; mso-bidi-font-size: 12.0pt; mso-font-kerning: 1.0pt; mso-bidi-font-family: 'Times New Roman'; mso-ansi-language: EN-US; mso-fareast-language: KO; mso-bidi-language: AR-SA">Load </span><span style="FONT-SIZE: 10pt; FONT-FAMILY: 굴림; mso-bidi-font-size: 12.0pt; mso-font-kerning: 1.0pt; mso-bidi-font-family: 'Times New Roman'; mso-ansi-language: EN-US; mso-fareast-language: KO; mso-bidi-language: AR-SA">이벤트에서 하는 일</span>]</font>  
<font face="굴림">  
</font>  
<font face="굴림">  
</font>그럼 이제 웹 서비스로부터 데이터를 받아오기 위해서 웹 참조 설정을 하도록 하겠다.

![](http://www.hoons.kr/hoons/lecture/SmartClient/26-037.jpg)<font face="굴림">  
 [웹 참조 추가]</font>

그럼 웹 참조 창이 뜨게 된다. 이전에 구현한 웹 서비스의 주소로 먼저 서비스를 조회하고, 참조이름을 설정했다면 참조 추가 버튼을 누른다. 피라는 SmartService라는 참조이름을 설정하였다.

![](http://www.hoons.kr/hoons/lecture/SmartClient/26-038.jpg)  
 [웹 참조 추가]

참조가 되었다면 아래와 GridControl 클래스에 다음과 같은 Load이벤트와 메서드를 만들어 보자.

  
<table bgcolor="#efefef" border="1" bordercolordark="white" bordercolorlight="black" cellpadding="5" cellspacing="0" id="Table16" width="100%">  
<tbody>  
<tr>  
<td><font size="2"><span lang="EN-US" style="COLOR: blue; FONT-FAMILY: 돋움체; mso-hansi-font-family: 'Times New Roman'; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes"><span lang="EN-US" style="COLOR: black; FONT-FAMILY: 돋움체; mso-hansi-font-family: 'Times New Roman'; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">  
<span lang="EN-US" style="COLOR: blue; FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">using</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes"> System.Runtime.Serialization.Formatters.Binary;  
</span><span lang="EN-US" style="COLOR: blue; FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">using</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes"> System.IO;  
</span><span lang="EN-US" style="FONT-SIZE: 10pt; COLOR: blue; FONT-FAMILY: 굴림; mso-no-proof: yes; mso-bidi-font-family: 'Times New Roman'; mso-ansi-language: EN-US; mso-fareast-language: KO; mso-bidi-language: AR-SA">using</span><span lang="EN-US" style="FONT-SIZE: 10pt; FONT-FAMILY: 굴림; mso-no-proof: yes; mso-bidi-font-family: 'Times New Roman'; mso-ansi-language: EN-US; mso-fareast-language: KO; mso-bidi-language: AR-SA"> System.IO.Compression;</span>

</span></span></font></td></tr></tbody></table>  
<table bgcolor="#efefef" border="1" bordercolordark="white" bordercolorlight="black" cellpadding="5" cellspacing="0" id="Table17" width="100%">  
<tbody>  
<tr>  
<td><font size="2"><span lang="EN-US" style="COLOR: blue; FONT-FAMILY: 돋움체; mso-hansi-font-family: 'Times New Roman'; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes"><span lang="EN-US" style="COLOR: black; FONT-FAMILY: 돋움체; mso-hansi-font-family: 'Times New Roman'; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">  
<span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">001 <span style="COLOR: blue">private</span><span style="COLOR: blue">void</span> GridControl_Load(<span style="COLOR: blue">object</span> sender, <span style="COLOR: teal">EventArgs</span> e)  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">002 {  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">003 <span style="mso-spacerun: yes">  </span><span style="COLOR: green">//</span></span><span style="COLOR: green; FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">웹서비스 호출  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">004 <span style="mso-spacerun: yes">  </span>SmartService.<span style="COLOR: teal">Service</span> WebSvr = <span style="COLOR: blue">new</span> SmartService.<span style="COLOR: teal">Service</span>();  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">005  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">006 <span style="mso-spacerun: yes">  </span><span style="COLOR: green">//</span></span><span style="COLOR: green; FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">압축 풀기  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">007 <span style="mso-spacerun: yes">  </span><span style="COLOR: blue">byte</span>[] data = <span style="COLOR: teal">Convert</span>.FromBase64String(WebSvr.GetService());  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">008 <span style="mso-spacerun: yes">  </span><span style="COLOR: teal">DataSet</span> ds = <span style="COLOR: blue">null</span>;<span style="COLOR: green">  
</span></span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">009 <span style="mso-spacerun: yes">  </span>ds = DecompressDataSet(data);  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">010  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">011<span style="mso-spacerun: yes">   </span><span style="COLOR: green">//</span></span><span style="COLOR: green; FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">그리드에 바인딩  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">012 <span style="mso-spacerun: yes">  </span>dataGridView1.AutoGenerateColumns = <span style="COLOR: blue">true</span>;  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">013 <span style="mso-spacerun: yes">  </span>dataGridView1.DataSource = ds.Tables[0];   
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">014 }  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">015 <span style="COLOR: blue">public</span><span style="COLOR: teal">DataSet</span> DecompressDataSet(<span style="COLOR: blue">byte</span>[] bytDs)  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">016 {  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">017 <span style="mso-spacerun: yes">  </span><span style="COLOR: teal">DataSet</span> outDs = <span style="COLOR: blue">new</span><span style="COLOR: teal">DataSet</span>();  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">018  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">019 <span style="mso-spacerun: yes">  </span><span style="COLOR: green">//</span></span><span style="COLOR: green; FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">스트림으로 가져오기  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">020 <span style="mso-spacerun: yes">  </span><span style="COLOR: teal">MemoryStream</span> inMs = <span style="COLOR: blue">new</span><span style="COLOR: teal">MemoryStream</span>(bytDs);  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">021 <span style="mso-spacerun: yes">  </span>inMs.Seek(0, 0);  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">022  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">023 <span style="mso-spacerun: yes">  </span><span style="COLOR: green">//1. </span></span><span style="COLOR: green; FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">압축객체 생성<span lang="EN-US">– </span>압축 풀기  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">024 <span style="mso-spacerun: yes">  </span><span style="COLOR: teal">DeflateStream</span> zipStream = <span style="COLOR: blue">new</span><span style="COLOR: teal">DeflateStream</span>(inMs, <span style="COLOR: teal">CompressionMode</span>.Decompress, <span style="COLOR: blue">true</span>);  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">025 <span style="mso-spacerun: yes">  </span><span style="COLOR: blue">byte</span>[] outByt = ReadFullStream(zipStream);  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">026 <span style="mso-spacerun: yes">  </span>zipStream.Flush();  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">027 <span style="mso-spacerun: yes">  </span>zipStream.Close();  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">028  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">029 <span style="mso-spacerun: yes">  </span><span style="COLOR: green">//2. </span></span><span style="COLOR: green; FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">스트림으로 다시변환  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">030 <span style="mso-spacerun: yes">  </span><span style="COLOR: teal">MemoryStream</span> outMs = <span style="COLOR: blue">new</span><span style="COLOR: teal">MemoryStream</span>(outByt);  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">031 <span style="mso-spacerun: yes">  </span>outMs.Seek(0, 0);  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">032 <span style="mso-spacerun: yes">  </span>outDs.RemotingFormat = <span style="COLOR: teal">SerializationFormat</span>.Binary;  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">033  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">034 <span style="mso-spacerun: yes">  </span><span style="COLOR: green">//3. </span></span><span style="COLOR: green; FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">데이터셋으로 <span lang="EN-US">Deserialize  
</span></span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">035 <span style="mso-spacerun: yes">  </span><span style="COLOR: teal">BinaryFormatter</span> bf = <span style="COLOR: blue">new</span><span style="COLOR: teal">BinaryFormatter</span>();  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">036 <span style="mso-spacerun: yes">  </span>outDs = (<span style="COLOR: teal">DataSet</span>)bf.Deserialize(outMs, <span style="COLOR: blue">null</span>);  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">037 <span style="mso-spacerun: yes">  </span><span style="COLOR: blue">return</span> outDs;  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">038 }  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">039  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">040 <span style="COLOR: green">//</span></span><span style="COLOR: green; FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">스트림을 <span lang="EN-US">Byte </span>배열로 변환  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">041 <span style="COLOR: blue">public</span><span style="COLOR: blue">byte</span>[] ReadFullStream(<span style="COLOR: teal">Stream</span> stream)  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">042 {  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">043 <span style="mso-spacerun: yes">  </span><span style="COLOR: blue">byte</span>[] buffer = <span style="COLOR: blue">new</span><span style="COLOR: blue">byte</span>[32768];  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">044 <span style="mso-spacerun: yes">  </span><span style="COLOR: blue">using</span> (<span style="COLOR: teal">MemoryStream</span> ms = <span style="COLOR: blue">new</span><span style="COLOR: teal">MemoryStream</span>())  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">045 <span style="mso-spacerun: yes">  </span>{  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">046 <span style="mso-spacerun: yes">    </span><span style="COLOR: blue">while</span> (<span style="COLOR: blue">true</span>)  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">047 <span style="mso-spacerun: yes">    </span>{  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">048 <span style="mso-spacerun: yes">      </span><span style="COLOR: blue">int</span> read = stream.Read(buffer, 0, buffer.Length);  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">049 <span style="mso-spacerun: yes">      </span><span style="COLOR: blue">if</span> (read <= 0)  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">050 <span style="mso-spacerun: yes">        </span><span style="COLOR: blue">return</span> ms.ToArray();  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">051 <span style="mso-spacerun: yes">      </span>ms.Write(buffer, 0, read);  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">052 <span style="mso-spacerun: yes">    </span>}  
</span><span lang="EN-US" style="FONT-FAMILY: 굴림; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">053 <span style="mso-spacerun: yes">  </span>}  
</span><span lang="EN-US" style="FONT-SIZE: 10pt; FONT-FAMILY: 굴림; mso-no-proof: yes; mso-bidi-font-family: 'Times New Roman'; mso-ansi-language: EN-US; mso-fareast-language: KO; mso-bidi-language: AR-SA">054 }</span>

</span></span></font></td></tr></tbody></table>  
[소스 설명]

  
<table border="1" bordercolordark="white" bordercolorlight="black" cellpadding="5" cellspacing="0" id="Table2" width="100%">  
<tbody>  
<tr>  
<td><font size="2"><span lang="EN-US" style="COLOR: blue; FONT-FAMILY: 돋움체; mso-hansi-font-family: 'Times New Roman'; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">  
<span lang="EN-US" style="COLOR: black; FONT-FAMILY: 돋움체; mso-hansi-font-family: 'Times New Roman'; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">4 줄은 웹 서비스 객체를 초기화 하고 있다. 앞서서 웹 참조 추가할 때 설정한 추가 이름이 바로 여기서 참조하는 네임스페이스 명이 된다.   
 7 줄은 Base64 형식으로 리턴 하는 문자열을 받아서 byte 배열로 변환하고 있다.   
 9 줄은 압축되어 있는 데이터를 압축을 해제하고 압축을 해제한 바이너리 데이터를 DataSet 객체로 Desirailize 하는 작업이다.   
 15~38 줄에 DecompressDataSet() 메서드가 바로 이러한 작업을 대행하는 메서드가 되는것이다. 이번 장은 스마트 클라이언트에 관한 내용을 다루기 때문에 메서드 안에 있는 IO 관련 클래스들의 설명은 생략하도록 하겠다.</span>

</span></font></td></tr></tbody></table>  
<font face="굴림">이렇게 코드가 작성이 되었다면 컴파일을 실행해서 DLL이 잘 만들어 지는지 확인하도록 한다.   
</font>  
<font face="굴림">  
</font>![](http://www.hoons.kr/hoons/lecture/SmartClient/26-039.jpg)<font face="굴림">  
 [생성된 DLL]</font>

그럼 이제 이 컨트롤을 웹 브라우져에 로드해서 한번 실행 시켜 보도록 하겠다. 현재 프로젝트에 ASP.NET 웹 사이트 프로젝트를 하나 추가해 보도록 하겠다.

![](http://www.hoons.kr/hoons/lecture/SmartClient/26-040.jpg)  
 [ASP.NET 웹사이트 추가]  
<font face="굴림"></font>

 앞서 만든 SmartContol.dll을 웹사이트가 생성된 곳으로 가져오도록 하자. 여기서 이 dll을 bin 폴더 안에는 넣으면 로드가 안되므로 bin폴더가 아닌 루트(Root)나 폴더를 생성해서 넣도록 하자. 필자는 웹사이트 루트로 이동 시켰다. 이제 웹 페이지를 하나 만들어서 아래와 같은 코드로 컨트롤을 로드 시켜 보자.

  
<table bgcolor="#efefef" border="1" bordercolordark="white" bordercolorlight="black" cellpadding="5" cellspacing="0" id="Table18" width="100%">  
<tbody>  
<tr>  
<td><font size="2"><span lang="EN-US" style="COLOR: blue; FONT-FAMILY: 돋움체; mso-hansi-font-family: 'Times New Roman'; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes"><span lang="EN-US" style="COLOR: black; FONT-FAMILY: 돋움체; mso-hansi-font-family: 'Times New Roman'; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes">  
<span lang="EN-US" style="FONT-FAMILY: 돋움체; mso-hansi-font-family: 'Times New Roman'; mso-bidi-font-size: 10.0pt; mso-font-kerning: 0pt; mso-no-proof: yes"><span lang="EN-US" style="FONT-SIZE: 10pt; COLOR: blue; FONT-FAMILY: 굴림; mso-no-proof: yes; mso-bidi-font-family: 'Times New Roman'; mso-ansi-language: EN-US; mso-fareast-language: KO; mso-bidi-language: AR-SA"><</span><span lang="EN-US" style="FONT-SIZE: 10pt; COLOR: maroon; FONT-FAMILY: 굴림; mso-no-proof: yes; mso-bidi-font-family: 'Times New Roman'; mso-ansi-language: EN-US; mso-fareast-language: KO; mso-bidi-language: AR-SA">object</span><span lang="EN-US" style="FONT-SIZE: 10pt; FONT-FAMILY: 굴림; mso-no-proof: yes; mso-bidi-font-family: 'Times New Roman'; mso-ansi-language: EN-US; mso-fareast-language: KO; mso-bidi-language: AR-SA"><span style="COLOR: red">id</span><span style="COLOR: blue">=’OBJECT2′</span><span style="COLOR: red">style</span><span style="COLOR: blue">=’WIDTH: 700px; HEIGHT: 600px’</span><span style="COLOR: red">classid</span><span style="COLOR: blue">=’SmartControl.DLL#SmartControl.GridControl’></</span><span style="COLOR: maroon">object</span><span style="COLOR: blue">></span></span></span>

</span></span></font></td></tr></tbody></table>  
  
 classid에서 dll을 참조하는 규칙은 다음과 아래와 같다.  
<font face="굴림"></font>

<table border="1" cellpadding="0" cellspacing="0" class="MsoTableGrid" id="Table3" style="BORDER-RIGHT: medium none; BORDER-TOP: medium none; BORDER-LEFT: medium none; BORDER-BOTTOM: medium none; BORDER-COLLAPSE: collapse; mso-border-alt: solid windowtext .5pt; mso-yfti-tbllook: 480; mso-padding-alt: 0cm 5.4pt 0cm 5.4pt; mso-border-insideh: .5pt solid windowtext; mso-border-insidev: .5pt solid windowtext">  
<tbody>  
<tr style="mso-yfti-irow: 0; mso-yfti-firstrow: yes; mso-yfti-lastrow: yes">  
<td style="BORDER-RIGHT: windowtext 1pt solid; PADDING-RIGHT: 5.4pt; BORDER-TOP: windowtext 1pt solid; PADDING-LEFT: 5.4pt; PADDING-BOTTOM: 0cm; BORDER-LEFT: windowtext 1pt solid; WIDTH: 435.1pt; PADDING-TOP: 0cm; BORDER-BOTTOM: windowtext 1pt solid; mso-border-alt: solid windowtext .5pt" valign="top" width="580">  
**<span lang="EN-US" style="FONT-FAMILY: 굴림">DLL</span>****<span style="FONT-FAMILY: 굴림">파일<span lang="EN-US">#</span>네임스페이스<span lang="EN-US">.</span>클래스<span lang="EN-US"></span></span>**

</td></tr></tbody></table>  
<font face="Times New Roman">이제 준비가 되었다면 브라우져를 열어서 컨트롤이 잘 로드 되는지 확인하도록 하자. 참조 정보가 잘못 설정되었다면 아래처럼 로드 되지 않는다.![](http://www.hoons.kr/hoons/lecture/SmartClient/26-041.jpg)

</font><font face="굴림">[DLL을 찾을 수 없을 때]</font>  
<font face="굴림">![](http://www.hoons.kr/hoons/lecture/SmartClient/26-042.jpg)  
 [네임스페이스나 클래스 설정이 잘못되었을 때]

올바르게 로드 되었다면 다음과 같은 에러 메시지 창이 뜨게 될 것이다.

</font>  
<font face="굴림"></font>![](http://www.hoons.kr/hoons/lecture/SmartClient/26-043.jpg)<font face="굴림">  
 [보안 정책 에러메세지]![](http://www.hoons.kr/hoons/lecture/SmartClient/26-044.jpg)  
 [그리드가 로드 되지만 데이터 바인딩이 되지 않은 데이터그리드뷰]

앞서서 설명했던 코드 엑세스 보안 정책으로 거슬러 올라가 보겠다. 코드 엑세스 보안 정책은 어디에서 어떤 코드를 실행하는지 검사한다고 했었다. 일단 웹에서 실행된 코드는 Internet 영역에서 보안을 검색하게 된다. Internet 보안 영역 에서는 그리드를 로드하고 웹 서비스를 호출하는 것에 대한 권한은 가지고 있다. 하지만 웹 서비스에서 받아온 데이터를 IO 클래스를 이용하여 압축을 해제하는 부분이 보안영역에 포함되어 있지 않은 부분이다. 앞서 설명한대로 수동으로 설정을 하던 자동으로 설정하는 프로그램을 만들던가 무언가의 설정을 해주어야 프로그램이 동작되는 것을 볼 수가 있다. 그럼 이제 URL 영역에 현재 자신의 IP를 등록시켜 보도록 하자. 코드 엑세스 보안을 수동으로 설정하는 부분은 앞에서 다루었기 때문에 따로 설명을 하지는 않겠다. 대신 주의 할 점은 localhost로 실행한 것과 아이피로 설정한 것은 서로 다른 사이트로 인식한다는 것만 알아두자. 수동으로 localhost에 FullTrust 권한을 주도록 하자.

![](http://www.hoons.kr/hoons/lecture/SmartClient/26-045.jpg)  
 [URL 멤버 자격 조건 설정]

이제 권한을 다 주었다면 브라우져를 다시 열어서 다음과 같이 결과가 잘 출력되는지 확인해보자.

![](http://www.hoons.kr/hoons/lecture/SmartClient/26-046.jpg)  
 [데이터 그리드뷰]

</font></td></tr></tbody></table></td></tr></tbody></table></div>

