---
title: '[Microsoft Ink] InkOveray 위에서 커서모양 바꾸기'
author: 'ash84'
pub_date: '2010-01-20'
description: '필자는 요즘 회사에서 Microsoft Ink 관련 Applicat'
featured_image: ''
tags: ['c#', 'change cursor', 'dev', 'InkOverlay curosr', 'Ink상에서의 커서변화', 'Microsoft.Ink', 'MS INK', '커서변화']
---


<div style="TEXT-ALIGN: justify"><span id="tx_beforestart_mark"></span>  
<span style="TEXT-ALIGN: justify; FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span id="tx_beforestart_mark"></span>필자는 요즘 회사에서 Microsoft Ink 관련 Application을 유지보수 하고 있습니다. 생각보다 복잡한 구조로 되어 있더라구요. 그 와중에 발견한 팁이 하나 있어서 올립니다. </span></span>

<span id="tx_afterend_mark"></span></span></span>  
<div>**  
<span id="tx_afterend_mark"></span>일반적인 Cursor 모양 변화 주기 **  
<div style="BORDER-LEFT: #000000 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: #e8e8e8; PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, Sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: #fff; PADDING-TOP: 3px"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 1pt"></span></span></span></span></span></span></span></span></div></div></div>  
<div style="TEXT-ALIGN: justify"><span style="TEXT-ALIGN: justify; FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt">일반적인 윈도우 어플리케이션에서 마우스 커서에 모양을 변화를 주기 위해서는 다음과 같은 코드를 사용합니다.   
</span>  
</font></span></span></span></span></div>  
<div style="TEXT-ALIGN: justify">  
<div style="LINE-HEIGHT: 1.7"><span style="TEXT-ALIGN: justify; FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"></span></span></div></div><span style="TEXT-ALIGN: center; FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div>  
<div style="LINE-HEIGHT: 1.7"> this.Cursor = System.Windows.Forms.Cursors.Cross;</div></div></span></span><span style="TEXT-ALIGN: justify; FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div></div></span></span><span style="TEXT-ALIGN: justify; FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div></div></span></span><span style="TEXT-ALIGN: justify; FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div>  
<div style="LINE-HEIGHT: 1.7">현재 커서를 Cross 모양의 커서로 바꾸라는 명령입니다. System.Windows.Forms.Cursors에는 우리가 흔히 보는 화상표, 모래시계 등의 커서 모양이 이미 정의되어 있어서 위의 코드 처럼 쓰면 됩니다.   
</div></div></span></span><span style="TEXT-ALIGN: justify; FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div></div></span></span><span style="TEXT-ALIGN: justify; FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
**InkOverlay 상에서는요?**<div>  
<div style="BORDER-LEFT: #000000 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: #e8e8e8; PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, Sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: #fff; PADDING-TOP: 3px"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 1pt"></span></span></span></span></span></span></span></span></div></div></div></div></span></span><span style="TEXT-ALIGN: justify; FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
<div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 11pt">Microsoft Ink 라이브러리를 조금 사용해 보신 분이라면 아시겠지만, ﻿</span></font><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt">﻿</span></font><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 11pt">﻿</span></font><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt">﻿ Ink Picture, InkCollec  
 tor, InkOverlay 등을 화면 컨트롤과 연결시킨 후에 구동 시켜보면, 마우스 커서가 해당 Ink 영역 안에서는 원래 의도한 커서가 아닌 점(Point)의 형태로 나타나는 것을 볼수 있습니다<figure class="wp-caption aligncenter" style="width: 315px">![](http://ash84.net/wp-content/uploads/1/cfile29.uf.1332D8284B5656CD6F5E0A.jpg)<figcaption class="wp-caption-text">잘 보이지가 않네요^^;</figcaption></figure>

</span></font></span></span></span></span>  
 위의 코드를 어딘가에 입력해 보아도 전혀 마우스의 커서는 변화하지 않을것 입니다. <font color="#318561">왜 이런 현상이 벌어지는 걸까요?</font>

**답은 MSDN에 있다!!**

<div>  
<div style="BORDER-LEFT: #000000 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: #e8e8e8; PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, Sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: #fff; PADDING-TOP: 3px"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 1pt"></span></span></span></span></span></span></span></span></div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><font color="#474747">﻿</font><span style="FONT-SIZE: 10pt"><font color="#474747">﻿</font><span style="FONT-FAMILY: Dotum"><font color="#474747">﻿MSDN 을 한번 봅시다. InkOverlay의 Cursor속성에 대한 MSDN의 설명은 다음과 같이 나와있습니다.   
</font></span></span></span>([http://msdn.microsoft.com/ko-kr/library/microsoft.ink.inkoverlay.cursor.aspx](http://msdn.microsoft.com/ko-kr/library/microsoft.ink.inkoverlay.cursor.aspx))</div></div></div></div></div></div></span></span><span style="TEXT-ALIGN: justify; FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
<div></div></div></div></div></div></span></span><span style="TEXT-ALIGN: right; FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
</div></div></div></div></div></div></span></span><span style="TEXT-ALIGN: right; FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
<div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-SIZE: 10pt">  
<div class="txc-textbox" style="BORDER-BOTTOM: #cbcbcb 1px solid; BORDER-LEFT: #cbcbcb 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #ffffff; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #cbcbcb 1px solid; BORDER-RIGHT: #cbcbcb 1px solid; PADDING-TOP: 10px">  
<span style="FONT-SIZE: 10pt">**![](http://ash84.net/wp-content/uploads/1/cfile23.uf.140F68244B5655B47EBAF8.jpg)  
 MSDN 中에서..  
**  
<font color="#112a75">기본 커서인 상속된 </font></span>[<span style="FONT-SIZE: 10pt"><font color="#112a75">Default</font></span>](http://msdn.microsoft.com/library/default.asp?url=/library/en-us/cpref/html/frlrfsystemwindowsformscursorsclassdefaulttopic.asp)<font color="#112a75"><span> 속성으로 설정하면 마우스 커서의 동작이 뷰에 있는 현재 커서의 그리기 특성을 따릅니다. 그런 다음 기본 커서 설정을 유지하면서 개체를 비활성화하면 커서 재정의가 비활성화되고 마우스 커서 설정이 내부 창의 마우스 커서 특성을 따릅니다.  
    
 커서를 <span class="input"><span class="cs"><span style="FONT-SIZE: 10pt">null</span></span><span class="vb"><span style="FONT-SIZE: 10pt">Nothing</span></span><span class="cpp"><span style="FONT-SIZE: 10pt">nullptr</span></span></span><span class="nu"><span style="FONT-SIZE: 10pt">Null 참조(Visual Basic의 경우 </span><span class="input"><span style="FONT-SIZE: 10pt">Nothing</span></span><span style="FONT-SIZE: 10pt">)</span></span></span><span style="FONT-SIZE: 10pt">(Microsoft Visual Basic .NET의 경우 </span><span><span class="input"><span style="FONT-SIZE: 10pt">Nothing</span></span>)로****설정하면 개체의 커서 처리도 비활성화됩니다. </span></font>

  
<font color="#112a75"><span style="FONT-SIZE: 10pt">커서가 기본 설정과 다르게 설정된 경우 개체의 활성화 여부와 관계없이 개체에서 항상 해당 커서를 사용합니다.</span><span style="FONT-SIZE: 10pt">이 속성은 잉크 입력 장치가 아닌 포인터의 시각적 표시를 참조합니다. 잉크 입력 장치는 </span><span>[<span style="FONT-SIZE: 10pt">Microsoft.Ink</span><span class="cs"><span style="FONT-SIZE: 10pt">.</span></span><span class="vb"><span style="FONT-SIZE: 10pt">.</span></span><span class="cpp"><span style="FONT-SIZE: 10pt">::</span></span><span class="nu"><span style="FONT-SIZE: 10pt">.</span></span><span style="FONT-SIZE: 10pt">Cursor</span>](http://msdn.microsoft.com/ko-kr/library/microsoft.ink.cursor.aspx)</span><span style="FONT-SIZE: 10pt"> 클래스로 나타냅니다.</span></font>

</div>  
</span>  
</div></div></div></div></div></div></span></span><span style="TEXT-ALIGN: justify; FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
<div>  
<div style="LINE-HEIGHT: 1.7">즉, InkOverlay가 비활성화 되면 원래의 Cursor를 따르게 되고, 활성화 된 경우에는 그리기의 특성, 즉 점(Point)의 형태로 나타내어 진다는 것입니다. 따라서 InkOverlay 위에서 커서를 바꿔주기 위해서는 InkOverlay 개체를 비활성화 해야 한다는 말입니다. 아래의 코드는 마우스가 움직일 경우, 마우스 클릭이 없는 경우에는 점(Point) 형태의 기본 InkOverlay 커서 속성이 아닌 Arrow(화살표) 속성을 지정하는 코드 입니다.

<span style="FONT-SIZE: 10pt">  
<div class="txc-textbox" style="BORDER-BOTTOM: #cbcbcb 1px solid; BORDER-LEFT: #cbcbcb 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #ffffff; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #cbcbcb 1px solid; BORDER-RIGHT: #cbcbcb 1px solid; PADDING-TOP: 10px">  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-SIZE: 10pt">private void Form_MouseMove(object sender, MouseEventArgs e)  
</span><span style="FONT-SIZE: 10pt">{</span></div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-SIZE: 10pt">            if (e.Button == MouseButtons.None)</span>  
<span style="FONT-SIZE: 10pt">            {</span>  
<span style="FONT-SIZE: 10pt">                <font color="#e31600">if (inkOverlay.CollectingInk == true)</font></span>  
<span style="FONT-SIZE: 10pt"><font color="#e31600">                { }</font></span>  
<span style="FONT-SIZE: 10pt">                else</span>  
<span style="FONT-SIZE: 10pt">                {</span>  
<span style="FONT-SIZE: 10pt"><font color="#3058d2">                   inkOverlay.Enabled = false;</font></span></div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-SIZE: 10pt"><font color="#3058d2">                   this.Cursor = System.Windows.Forms.Cursors.Arrow;</font></span>  
<span style="FONT-SIZE: 10pt">                }</span></div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-SIZE: 10pt">            }</span>  
<span style="FONT-SIZE: 10pt">            else if (e.Button == MouseButtons.Left || e.Button == MouseButtons.Right)</span>  
<span style="FONT-SIZE: 10pt">            {</span></div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-SIZE: 10pt">                <font color="#3058d2">inkOverlay.Enabled = true;</font></span></div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-SIZE: 10pt">            }  
</span><span style="FONT-SIZE: 10pt">}</span></div>  
</div></span>

</div></div></div></div></span></span><span style="TEXT-ALIGN: justify; FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
 마우스 버튼이 없을때는 InkOverlay의 Enabled 속성을 False로 함으로써, 개체를 비활성화 시키고 있습니다. 따라서 비활성화 후에 커서의 모양을 변화시켜주면 원하는 대로 모양이 변화하게 됩니다. 그리고 마우스의 버튼 클릭이 있는 경우에는, Enabled 속성을 True로 함으로써 개체를 활성화 시켜주면 바로 커서의 모양이 바뀌게 됩니다. **<font color="#e31600">주의할 점!! 이것만 기억하자. 꼭꼭꼭!!</font>**

<div>  
<div style="BORDER-LEFT: #000000 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: #e8e8e8; PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, Sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: #fff; PADDING-TOP: 3px"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 1pt"></span></span></span></span></span></span></span></span></div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 11pt">﻿</span></font><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt">﻿</span></font><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 11pt">﻿</span></font><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt">﻿위의 코드에서 <font color="#e31600">빨간 색</font>으로 지정한 부분을 보면 <font color="#e31600">inkOverlay.CollectingInk </font>라는 속성이 있습니다. 간혹, 마우스가 아닌 다른 하드웨어로 부터 신호를 받아서 처리하는 경우, 마우스 이벤트를 강제로 발생 시켜서 </span><span style="FONT-SIZE: 11pt">그리는 경우가 있습니다. 이럴경우,<font color="#e31600"> Ink를 수집(Collect)하고 있는데, 그 와중에 Enabled=false를 하게 되면 런타임 에러가 발생하기 때문에 위의 소스코드 처럼 처리를 하시기 바랍니다. </font></span></font></span></span></span></span>  
</div></div>  
  </div></div></span></span>  
 



