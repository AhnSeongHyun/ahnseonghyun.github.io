---
title: '[C#] 가상 키(Key) 이벤트 보내기'
author: 'ash84'
pub_date: '2015-07-03'
description: '[  
![Apple's Flat Keyboard](http://farm3.static.flickr.com/2543/4153789271_a0a01c21b6.jpg)](http://www.flickr.com/'
featured_image: ''
tags: ['.net', 'An Seong Hyun', 'c#', 'dev', 'SendKeys.Send()', '가상 키 입력', '가상키', '안성현', '프로그래밍']
---


<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2">  
<table class="flickrImgSearch">  
<tbody>  
<tr>  
<td>[<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
![Apple's Flat Keyboard](http://farm3.static.flickr.com/2543/4153789271_a0a01c21b6.jpg)</span></span>](http://www.flickr.com/photos/30647744@N00/4153789271 "Apple's Flat Keyboard")  
<span><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">Apple’s Flat Keyboard by </span></span>[<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">dmuth</span></span>](http://www.flickr.com/photos/30647744@N00)</span><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"></span></span>[<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">![저작자 표시](http://cfs.tistory.com/static/admin/editor/ccl_black01.png)</span></span><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">![동일조건 변경허락](http://cfs.tistory.com/static/admin/editor/ccl_black03.png)</span></span>](http://creativecommons.org/licenses/by-sa/2.0/kr/)</td></tr></tbody></table><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">C#  뿐만 아니라, 많은 프로그래밍 언어에서는 키(KEY) 이벤트를 받아서 처리하는 이벤트 핸들러가 정의되어 있어서 쓰면 되는데, 가상으로 키 이벤트를 보내는 기능이 필요해서 찾아 보게 되었습니다. 그러던 중 발견한것. </span></span></span>

**<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">SendKeys.Send() 함수</span></span>**<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"></span></span>

</div>  
<div style="LINE-HEIGHT: 2"></div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2">  
<div style="BORDER-LEFT: #000000 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: #e8e8e8; PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, Sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: #fff; PADDING-TOP: 3px"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 1pt"></span></span></span></span></span></span></span></span></div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">﻿</span></span></font><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">﻿</span></span></font><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">﻿</span></span></font><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">﻿ </span></span></font></span></span></span></span>  
</div></div>  
<div style="LINE-HEIGHT: 2"></div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">SendKeys.Send() 함수를 이용하면 사용자가 키를 누르지 않았어도 마치 키 입력이 들어온것 처럼 할수가 있습니다. 예를 들어 </span></span></span><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">SendKeys.Send(“{ENTER}”);  //엔터키를 눌렀다. </span></span></span>

<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">이런식으로 보낼수가 있습니다. 자주 쓰는 Ctrl+C, Ctrl+V 같은 경우에는 이렇게 표현할수 있겠죠.</span></span></span>

<font color="#c8056a"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">SendKeys.Send(“^c”); // Ctrl+c 키를 눌렀다. </span></span></span>  
<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">SendKeys.Send(“^v”); // Ctrl+v 키를 눌렀다. </span></span></span></font>

<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">일반 알파벳 키와 합쳐서 쓰기 위해서는 </span></span></span>

<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">Ctrl = ^</span></span></span>  
<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">Shift = +</span></span></span>  
<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">Alt = %</span></span></span>

<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">이런식으로 ” ” 알파벳키 앞에 붙여줘야 합니다. </span></span></span>

**<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">특수키는 어떻게?</span></span>**

</div>  
<div style="LINE-HEIGHT: 2"></div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2">  
<div style="BORDER-LEFT: #000000 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: #e8e8e8; PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, Sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: #fff; PADDING-TOP: 3px"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 1pt"></span></span></span></span></span></span></span></span></div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">﻿</span></span></span></font><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">﻿</span></span></span></font><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">﻿</span></span></span></font><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">﻿그렇다면 특수키를 어떻게 쓸까요? (눈치 빠른 분들은 벌써 눈치 채신듯^^;;)</span></span></span>  
</font></span></span></span></span>  
<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">특수키의 경우네는 ” ”  문자열안에 { } 중괄호를 넣은 그 안에 특수키 이름을 넣어 줍니다. 예를들면</span></span></span><font color="#c8056a"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">SendKeys.Send(“{ENTER}”);</span></span></span>  
<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">SendKeys.Send(“{HELP}”);  </span></span></span>  
<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">SendKeys.Send(“{ESC}”); </span></span></span>  
<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">SendKeys.Send(“{F1}”);  </span></span></span></font>

</div></div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">이런식으로 넣어주면 됩니다. </span></span></span><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">참고 URL : </span></span></span>[<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">http://msdn.microsoft.com/ko-kr/library/system.windows.forms.sendkeys.aspx</span></span></span>](http://msdn.microsoft.com/ko-kr/library/system.windows.forms.sendkeys.aspx)

**<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">C# 관련 이전글 </span></span>**

<div>  
<div style="BORDER-LEFT: #000000 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: #e8e8e8; PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, Sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: #fff; PADDING-TOP: 3px"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 1pt"></span></span></span></span></span></span></span></span></div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">﻿</span></span></span></font><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">﻿</span></span></span></font><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">﻿</span></span></span></font><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">﻿</span></span></span></font></span></span></span></span>[<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">2009/11/24 – [Development] – [C#] Winform(윈폼) 제목표시줄에 안뜨게 하기</span></span></span>](http://ash84.tistory.com/530)  
[<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">2009/11/20 – [Development/C#] – [C#] Serial Port 구분하기.</span></span></span>](http://ash84.tistory.com/526)</div></div></div>  
<div style="TEXT-ALIGN: justify">  
<div>  
<div style="LINE-HEIGHT: 1.7"></div></div></div>

