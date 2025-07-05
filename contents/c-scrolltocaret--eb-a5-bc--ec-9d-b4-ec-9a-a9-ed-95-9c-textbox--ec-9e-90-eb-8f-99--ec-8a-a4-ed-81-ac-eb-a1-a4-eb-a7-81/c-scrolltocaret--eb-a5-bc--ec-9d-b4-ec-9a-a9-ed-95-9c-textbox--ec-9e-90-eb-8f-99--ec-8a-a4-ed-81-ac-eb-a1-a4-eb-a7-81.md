---
title: '[C#] ScrollToCaret 를 이용한 TextBox 자동 스크롤링'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['An Seong Hyun', 'c#', 'dev', 'ScrollToCaret', 'TextBox', '안성현', '자동스크롤링']
---


<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">TextBox는 본래, 사용자의 데이터 입력을 받아 들이는 기능을 주로 하지만, 때때로 데이터를 보기위해서 쓰이기도 합니다. 특히, 저는 시리얼 포트를 통해서 들어오는 데이터를 한눈에 보기 위해서 자주 사용하는데요, 이런 실시간 데이터를 받아와서 TextBox로 보여줄때 처리해줘야 하는 부분에 대해서 알려드리도록 하겠습니다. </span></span></span></span></div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
</span></span></div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">![](http://ash84.net/wp-content/uploads/1/cfile25.uf.156091204B7F349957304E.jpg)</span></span></span></span></div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><font class="Apple-style-span" face="Dotum" size="4"><span class="Apple-style-span" style="LINE-HEIGHT: 28px; FONT-SIZE: 15px">  
</span></font></div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">TextBox에 텍스트를 표시하기 위해서는 Text 속성을 이용해서 입력할 수가 있습니다. </span></span></span></span></div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2">  
</div>  
<div style="TEXT-ALIGN: center; LINE-HEIGHT: 2"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div class="txc-textbox" style="BORDER-BOTTOM: #cbcbcb 1px solid; BORDER-LEFT: #cbcbcb 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #ffffff; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #cbcbcb 1px solid; BORDER-RIGHT: #cbcbcb 1px solid; PADDING-TOP: 10px"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">textBox1.Text = “Hello World”;</span></span></span></span>  
</div></span></span></div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2">  
</div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">그런데 여러줄을 표시하고 싶을때는, MultiLine 속성을 </span></span><font color="#193da9"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">True</span></span></font><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">로 놓고 </span></span></span></span></div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2">  
</div>  
<div style="TEXT-ALIGN: center; LINE-HEIGHT: 2"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div class="txc-textbox" style="BORDER-BOTTOM: #cbcbcb 1px solid; BORDER-LEFT: #cbcbcb 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #ffffff; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #cbcbcb 1px solid; BORDER-RIGHT: #cbcbcb 1px solid; PADDING-TOP: 10px"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">textBox1.Text +=”Hello world” + System.Environment.NewLine</span></span></span></span>  
</div></span></span></div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2">  
</div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">이런식으로 써 주면 됩니다. </span></span><font color="#e31600"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">여기서 질문!! 그렇다면, TextBox의 Height 범위를 넘어버린 텍스트는 어떻게 표시가될까요?</span></span></font><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"> 안타깝게도, 넘어가버린 텍스트는 현재의 마우스 드래깅을 하기 전에는 절대 보이지 않습니다. (혹은 스크롤바를 마우스를 이용해서 내리거나)</span></span></span></span></div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2">  
</div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">그렇다면, TextBox의 세로 영역을 넘어버려도 텍스트를 어떻게 내려가면서 보여줄수 있을까요?</span></span></span></span></div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2">  
</div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2">**<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">ScrollToCaret( )</span></span></span></span>**</div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2">  
<div>  
<div style="BORDER-LEFT: #000000 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: #e8e8e8; PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, Sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: #fff; PADDING-TOP: 3px"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 1pt"></span></span></span></span></span></span></span></span></div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><font color="#474747"><span class="Apple-style-span" style="LINE-HEIGHT: 18px; FONT-FAMILY: 굴림; COLOR: rgb(51,51,51)">**<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">ScrollToCaret()</span></span></span></span>**</span><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">﻿</span></span></span></span></font><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">﻿</span></span></span></span></font><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">﻿ 를 이용하면, 자동으로 스크롤링하게 만들수가 있습니다. </span></span>**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">ScrollToCaret() 함수는 현재 컨트롤의 내용을 현재 캐럿 위치까지 스크롤하는 함수 입니다.</span></span>**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"> 즉, 범위가 넘어버려도 내용이 TextBox의 아랫부분까지 내용이 현재 있다면, ScrollToCaret() 함수를 사용하면, 그 부분까지 자동으로 내려가게 되는 것 입니다. </span></span></span></span></font></span></span></span>  
</div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><font color="#474747">  
</font></span></span></span></div></div></div>  
<div style="TEXT-ALIGN: center; LINE-HEIGHT: 2">  
<div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div class="txc-textbox" style="BORDER-BOTTOM: #f3c534 1px solid; BORDER-LEFT: #f3c534 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #fefeb8; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #f3c534 1px solid; BORDER-RIGHT: #f3c534 1px solid; PADDING-TOP: 10px"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">textBox1.ScrollToCaret();</span></span></span></span></font></span></span></span>  
</div></span></span></font></span></span></span></div></div></div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2">  
<div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><font color="#474747">  
</font></span></span></span></div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><font color="#474747">  
</font></span></span></span></div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><font color="#474747">**<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">주의사항</span></span></span></span>**</font></span></span></span></div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><font color="#474747">  
<div>  
<div style="BORDER-LEFT: #000000 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: #e8e8e8; PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, Sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: #fff; PADDING-TOP: 3px"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 1pt"></span></span></span></span></span></span></span></span></div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">﻿</span></span></span></span></font><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">﻿</span></span></span></span></font><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">﻿ScrollToCaret() 함수를 이용할때에는 주의할 점이 하나 있는데요. </span></span></span></span>  
</font></span></span></span>  
</div></div></font></span></span></span></div></div></div>  
<div style="TEXT-ALIGN: center; LINE-HEIGHT: 2">  
<div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><font color="#474747">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
<div><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div class="txc-textbox" style="BORDER-BOTTOM: #cbcbcb 1px solid; BORDER-LEFT: #cbcbcb 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #ffffff; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #cbcbcb 1px solid; BORDER-RIGHT: #cbcbcb 1px solid; PADDING-TOP: 10px"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">textBox1.Text +=”Hello world” + System.Environment.NewLine</span></span></span></span>  
<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">textBox1.ScrollToCaret();</span></span></span></span>  
</div></span></span>  
</div></div></div></font></span></span></span></div></div></div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2">  
<div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><font color="#474747">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
<div>  
<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">위와 같이 쓰면 동작하지 않는 다는 것입니다. 대신에 </span></span></span></span><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div class="txc-textbox" style="BORDER-BOTTOM: #f3c534 1px solid; BORDER-LEFT: #f3c534 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #fefeb8; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #f3c534 1px solid; BORDER-RIGHT: #f3c534 1px solid; PADDING-TOP: 10px">  
<div style="TEXT-ALIGN: center"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">textBox1.AppendText(“Hello world” + System.Environment.NewLine);</span></span></span></span>  
<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">textBox1.ScrollToCaret();</span></span></span></span>  
</div></div></span></span>

<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">AppendText()</span></span>**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"> 함수를 이용해서 텍스트를 하나씩 추가해주면서 ScrollToCaret()함수를 쓰면, 바로바로 내용이 있는 곳 까지 자동으로 내려가게 됩니다. </span></span></span></span>

<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">![](http://ash84.net/wp-content/uploads/1/cfile21.uf.125F6E204B7F31AE3E298A.gif)</span></span><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">MSDN 주의사항 </span></span></span></span>  
<span class="Apple-style-span" style="WIDOWS: 2; TEXT-TRANSFORM: none; TEXT-INDENT: 0px; BORDER-COLLAPSE: separate; FONT: medium Gulim; WHITE-SPACE: normal; ORPHANS: 2; LETTER-SPACING: normal; COLOR: rgb(0,0,0); WORD-SPACING: 0px; -webkit-border-horizontal-spacing: 0px; -webkit-border-vertical-spacing: 0px; -webkit-text-decorations-in-effect: none; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px"><span class="Apple-style-span" style="TEXT-ALIGN: left; BORDER-COLLAPSE: collapse; FONT-FAMILY: Verdana; FONT-SIZE: 11px; -webkit-border-horizontal-spacing: 2px; -webkit-border-vertical-spacing: 2px"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 9pt">  
<div class="txc-textbox" style="BORDER-BOTTOM: rgb(254,137,67) 1px solid; BORDER-LEFT: rgb(254,137,67) 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: rgb(254,222,199); PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: rgb(254,137,67) 1px solid; BORDER-RIGHT: rgb(254,137,67) 1px solid; PADDING-TOP: 10px"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 9pt">컨트롤에 포커스가 없거나 캐럿이 컨트롤의 표시 가능 영역에 있는 경우 </span><span style="FONT-SIZE: 9pt">이 메서드는 효과가 없습니다.</span></span></span></div></span></span></span></span></span>  
<font class="Apple-style-span" color="#333333" face="굴림" size="3"><span class="Apple-style-span" style="LINE-HEIGHT: 24px; FONT-SIZE: 12px"><font class="Apple-style-span" color="#474747" face="Dotum" size="3"><span class="Apple-style-span" style="LINE-HEIGHT: 22px; FONT-SIZE: 13px">  
</span></font></span></font>

</div></div></div></font></span></span></span></div></div></div>

