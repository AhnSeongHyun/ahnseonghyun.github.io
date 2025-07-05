---
title: '[C#] CSS 분석은 이제 내게 맡겨라. Bonesoft.CSS.dll'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['An Seong Hyun', 'Analysis CSS', 'Bonesofr.css.dll', 'c#', 'css', 'CSS분석', 'dev', 'EBOOK READER 개발', 'html', '안성현']
---


<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">*<span style="FONT-SIZE: 14pt">**  
 CSS란?**</span>*</span></span>  
<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div class="txc-textbox" style="BORDER-BOTTOM: #c1c1c1 1px solid; BORDER-LEFT: #c1c1c1 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #eeeeee; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #c1c1c1 1px solid; BORDER-RIGHT: #c1c1c1 1px solid; PADDING-TOP: 10px"><span><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">CSS</span></span><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">(</span></span></span><span lang="en" xml:lang="en"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">Cascading Style Sheet</span></span></span></span><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">)는 </span></span></span>[<font color="#002bb8"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">마크업 언어</span></span></span></font>](http://ko.wikipedia.org/wiki/%EB%A7%88%ED%81%AC%EC%97%85_%EC%96%B8%EC%96%B4 "마크업 언어")<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">가 실제 표시되는 방법을 기술하는 언어로, </span></span></span>[<font color="#002bb8"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">HTML</span></span></span></font>](http://ko.wikipedia.org/wiki/HTML "HTML")<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">과 </span></span></span>[<font color="#002bb8"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">XHTML</span></span></span></font>](http://ko.wikipedia.org/wiki/XHTML "XHTML")<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">에 주로 쓰이며, </span></span></span>[<font color="#002bb8"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">XML</span></span></span></font>](http://ko.wikipedia.org/wiki/XML "XML")<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">에서도 사용할 수 있다. </span></span></span>[<font color="#002bb8"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">W3C</span></span></span></font>](http://ko.wikipedia.org/wiki/W3C "W3C")<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">의 표준이며, 레이아웃과 스타일을 정의할 때의 자유도가 높다</span></span></span>  
</div></span></span>

<figure class="wp-caption aligncenter" style="width: 320px">![](http://ash84.net/wp-content/uploads/1/cfile26.uf.1336B61B4B5E46388589C9.jpg)<figcaption class="wp-caption-text">복잡한 CSS는 어떻할건데?</figcaption></figure><span style="LINE-HEIGHT: 2; FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">이런 CSS는 본래 웹 브라우저가 분석을 합니다. 분석을 한 후에, 연결되어 있는 HTML과 합쳐져서 웹 브라우저 상에서 우리가 보게 되는것이지요. 현재 티스토리 블로그 스킨 역시 HTML+CSS 구조로 되어 있습니다. </span></span></span>

**CSS 분석  
**

<div>  
<div style="BORDER-LEFT: #000000 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: #e8e8e8; PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, Sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: #fff; PADDING-TOP: 3px"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 1pt"></span></span></span></span></span></span></span></span></div></div><span style="LINE-HEIGHT: 2; FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt">﻿</span></span></font><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt">﻿</span></span></font><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt">﻿</span></span></font><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt">﻿사실상 CSS은 이미 웹 브라우저가 분석을 해주기 때문에 분석을 할 필요가 있나 라는 생각이 드시는 분들이 계실것 입니다. CSS를 분석해야 하는 경우는, 웹 브라우저가 아닌 곳에서 HTML을 제대로 보여줘야 할 경우이지요. 예를들면, eBook Reader를 만들어야 하는 경우와 같이 말입니다. </span>  
</span></font></span></span></span></span></div></div></span></span><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt">  
<span style="FONT-SIZE: 9pt">  
<div class="txc-textbox" style="BORDER-BOTTOM: #fe8943 1px solid; BORDER-LEFT: #fe8943 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #fedec7; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #fe8943 1px solid; BORDER-RIGHT: #fe8943 1px solid; PADDING-TOP: 10px">**CSS의 예  
**<span style="FONT-SIZE: 9pt">  
  * { font-size: 1em; text-align: center; } </span>  
<span style="FONT-SIZE: 9pt"> body { margin: 0 auto; padding: 0.75em; } </span>  
<span style="FONT-SIZE: 9pt"> div, h1, h2, h3, h4, h5, p { font-size: 1em; text-align: center; } </span>  
<span style="FONT-SIZE: 9pt"> a { text-decoration: none; color: #000044; } </span>  
<span style="FONT-SIZE: 9pt"> div#titlepage h1.part-title { margin-bottom: 0; font-size: 2em;  } </span>  
<span style="FONT-SIZE: 9pt"> div#titlepage h2.part-subtitle { margin-top: 0.5em;  font-size: 1.25em; font-style: italic; font-weight: normal; } </span>  
<span style="FONT-SIZE: 9pt"> div#titlepage h3.title-break { margin-top: 1.25em; margin-bottom: 0.75em; font-size: 1.1em; } </span>  
<span style="FONT-SIZE: 9pt"> div#titlepage h3.author { margin-top: 0; margin-bottom: 1.75em; font-size: 1.25em; } </span>  
<span style="FONT-SIZE: 9pt"> div#titlepage h5 { margin: 0; font-size: 90%; } </span>  
<span style="FONT-SIZE: 9pt"> div#titlepage h5 a { color: #222222; } </span>  
<span style="FONT-SIZE: 9pt"> div#titlepage div#docImprint { margin: 2em 0; } </span>  
<span style="FONT-SIZE: 9pt"> div#docImprint p { margin: 0.1em 0; } </span>  
</div></span>  
</span></font></span></span></span></span></div></div></span></span><span style="LINE-HEIGHT: 2; FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt">위의 CSS는 한 ePUB 책의 CSS를 가져온것입니다. 복잡하진 않지만, 개발자가 한줄 한줄 읽어서 파싱(Parsing)하고 그것을 다시 자료구조에 넣어서 응용한다고 생각하면 머리가 아파온다. ㅠ</span>  
</span></font></span></span></span></span></div></div></span></span><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt">**Bonesoft.CSS.dll 을 통해서 분석하자!!**

<div>  
<div style="BORDER-LEFT: #000000 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: #e8e8e8; PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, Sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: #fff; PADDING-TOP: 3px"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 1pt"></span></span></span></span></span></span></span></span></div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt">Bonesoft.css.dll 을 이용하면 CSS 파일을 분석할 수가 있다. 자, 일단 다운 받으시고.</span></span></font></span></span></span>  
</div></div>  
[](http://ash84.net/wp-content/uploads/1/cfile2.uf.191CC4054B5E427E3A0F3F.dll)cfile2.uf.191CC4054B5E427E3A0F3F.dll<span style="FONT-SIZE: 10pt">받으신 dll을 참조추가 한후, 아래와 같이 코딩을 해주면 쉽게 파싱을 할 수가 있다. </span>

<div class="txc-textbox" style="BORDER-BOTTOM: #cbcbcb 1px solid; BORDER-LEFT: #cbcbcb 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #ffffff; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #cbcbcb 1px solid; BORDER-RIGHT: #cbcbcb 1px solid; PADDING-TOP: 10px"><span style="FONT-SIZE: 10pt">        </span><font color="#193da9"><span style="FONT-SIZE: 10pt">    using </span></font><span style="FONT-SIZE: 10pt">BoneSoft.CSS;</span><span style="FONT-SIZE: 10pt">            BoneSoft.CSS.</span><font color="#0686a8"><span style="FONT-SIZE: 10pt">CSSParser</span></font><span style="FONT-SIZE: 10pt"> parser =</span><font color="#193da9"><span style="FONT-SIZE: 10pt"> new </span></font><span style="FONT-SIZE: 10pt">BoneSoft.CSS.</span><font color="#0686a8"><span style="FONT-SIZE: 10pt">CSSParser</span></font><span style="FONT-SIZE: 10pt">();</span>  
<span style="FONT-SIZE: 10pt">            parser.ParseFile(CSS_Filename);</span>  
<span style="FONT-SIZE: 10pt">     </span>  
<span style="FONT-SIZE: 10pt">            </span><font color="#193da9"><span style="FONT-SIZE: 10pt">public </span></font><font color="#0686a8"><span style="FONT-SIZE: 10pt">CSSDocument </span></font><span style="FONT-SIZE: 10pt">css;</span>  
<span style="FONT-SIZE: 10pt">            css = parser.CSSDocument;</span>

</div></span></font></span></span></span></span></div></div></span></span><span style="TEXT-ALIGN: justify; FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt">  
<span style="FONT-SIZE: 10pt">1번째줄에서 객체(parser)를 만들어 주고 있고, 2번째줄에서 만들어진 객체 parser의 함수인 ParseFile()을 호출하면서, css 파일의 경로를 파라미터로 넘겨주고 있다. ParseFile() 함수를 호출하면, 지정한 경로의 css 파일이 파싱이 되어 parser.CSSDocument에 들어가 있다.parser. CSSDocument와 CSSDocument 객체를 만들어서 연결시켜 주면, 계층화되어 분석된 CSSDocument를 볼수가 있다. </span>  
</span></font></span></span></span></span></div></div></span></span><span style="TEXT-ALIGN: justify; FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
**다음시간에는?**  
</div></div></span></span><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
<div>  
<div style="BORDER-LEFT: #000000 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: #e8e8e8; PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, Sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: #fff; PADDING-TOP: 3px"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 1pt"></span></span></span></span></span></span></span></span></div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><font color="#105738"><font color="#e31600"><span style="FONT-SIZE: 10pt">다음시간에는 CSSDocument 의 구조와 실제 CSS 파일을 비교해가면서 어떻게 파싱 결과가 나왔으며, 어떻게 활용할수 있는지 알아보겠습니다</span></font><span style="FONT-SIZE: 10pt">. </span></font></span>  
</div></div>  
</div></div></span></span>

