---
title: '[C#] Image들을 PDF로 저장하기'
author: 'ash84'
pub_date: '2009-09-25'
description: '**  
****  
 Image를 PDF로 저장하기 위한 C# 소스코드 **'
featured_image: ''
tags: ['C#', 'Convert Image to PDF', 'dev', 'IMAGE TO PDF', 'Make pdf file', 'pdf 만들기', 'developer', 'programming']
---
**  
**<span style="font-size: 11pt; "><span style="font-family: Dotum; ">**  
 Image를 PDF로 저장하기 위한 C# 소스코드 **<div><div style="BORDER-LEFT: #000000 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: #e8e8e8; PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, Sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: #fff; PADDING-TOP: 3px"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 1pt"></span></span></span></span></span></span></span></span></div><div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><font color="#474747">﻿</font><span style="FONT-SIZE: 10pt"><font color="#474747">﻿</font><span style="FONT-FAMILY: Dotum"><font color="#474747">﻿</font><span style="FONT-SIZE: 10pt"><font color="#474747">﻿ </font></span></span></span></span></div><div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><font color="#474747"><span class="Apple-style-span" style="color: rgb(51, 51, 51); font-size: 15px; line-height: 29px; ">ResultPath : 실제 저장할 주소 (C:\TEMP.PDF)</span></font></span></span></span></span></div></div></span></span>

<span style="font-size: 11pt; "><span style="font-family: Dotum; ">  
 ArrayList :  이미지 파일들이 실제 있는 경로의 집합</span></span>

<span style="font-size: 11pt; "><span style="font-family: Dotum; ">  
 그래서 소스가 실행되면, 이미지 들을 하나씩 읽어와서 하나의 PDF 파일에 차례대로 </span></span>  
<span style="font-size: 11pt; "><span style="font-family: Dotum; ">  
 이미지를 넣어서 PDF 파일을 만든다. </span></span>

<span style="font-size: 11pt; "><span style="font-family: Dotum; ">  
 아래의 소스코드를 실행하기 위해서는 다음의 Dll이 필요하다. </span></span>

  
[](http://ash84.net/wp-content/uploads/1/cfile29.uf.136CB40B4ABC166017FD11.dll)cfile29.uf.136CB40B4ABC166017FD11.dll

<textarea class="C#" name="code" style="MARGIN: 2px; WIDTH: 712px; HEIGHT: 377px">  public String SaveToPDF(String ResultPath, ArrayList imgPathList)  
  {  
             // PDF 문서를 생성하기 위해 Document를 생성  
             PdfDocument PDFDocument = new PdfDocument();</textarea>

         
        // 페이지의 세로를 Pixel로 변환  
             //int PageHeightPx = (int)(((double)842 / 72) * 96);  
                 int PageCount = imgPathList.Count;  
             for (int i = 0; i

<font color="#e31600">**<span style="font-size: 11pt; "><span style="font-family: Dotum; ">주의점</span></span>**<span style="font-size: 11pt; "><span style="font-family: Dotum; "><div><div style="BORDER-LEFT: #000000 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: #e8e8e8; PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, Sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: #fff; PADDING-TOP: 3px"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 1pt"></span></span></span></span></span></span></span></span></div><div style="LINE-HEIGHT: 1.7"><span class="Apple-style-span" style="font-family: 굴림; font-size: 12px; "><span style="font-size: 11pt; "><span style="font-family: Dotum; "><font class="Apple-style-span" color="#000000">이미지 파일 자체를 첨부하여 PDF 를 만드는 경우, 프로그램이 실행되는동안 해당 이미지 파일에 대한 삭제 </font></span></span><span style="font-size: 11pt; "><span style="font-family: Dotum; "><font class="Apple-style-span" color="#000000">및 접근은 제한될수 있기 때문에 그러한 프로세스가 필요한 경우에는 이미지를 Image 객체에 담아서 사용하는 것이 좋다.</font></span></span></span></div></div></span></span></font>



