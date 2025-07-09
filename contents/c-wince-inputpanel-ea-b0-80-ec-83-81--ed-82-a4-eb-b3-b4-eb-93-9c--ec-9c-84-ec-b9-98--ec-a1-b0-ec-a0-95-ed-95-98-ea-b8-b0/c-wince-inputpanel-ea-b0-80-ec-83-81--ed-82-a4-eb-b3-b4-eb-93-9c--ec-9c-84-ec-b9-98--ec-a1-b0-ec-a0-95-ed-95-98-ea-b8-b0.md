---
title: '[C#] WinCE InputPanel(가상 키보드) 위치 조정하기'
author: 'ash84'
pub_date: '2010-04-22'
description: 'WinCE 6.0 환경에서는 보통 키보드와 마우스가 제공되지 않는 환경입니다. 때문에 터치스크린이 마우스를 대체하고 키보드는 SIP 즉, 가상키보드가 그 역할을 대체합니다. 때문에 대부분의 WinCE는 포팅과정에서 가상 키보드'
featured_image: ''
tags: ['c#', 'dev', 'inputpanel', 'SIP', 'Wince', '가상키보드', '위치지정']
---


<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"></div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2">  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">WinCE 6.0 환경에서는 보통 키보드와 마우스가 제공되지 않는 환경입니다. 때문에 터치스크린이 마우스를 대체하고 키보드는 SIP 즉, 가상키보드가 그 역할을 대체합니다. 때문에 대부분의 WinCE는 포팅과정에서 가상 키보드를 넣어주고 있습니다. </span></span><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">C# 개발 환경에서 개발 할 프로그램에서 가상 키보드(SIP)를 호출하기 위해서는 <font color="#5c7fb0">도구상자(ToolBox)</font>에서 InputPanel을 폼에 추가해줘야 합니다. InputPanel을 폼에 추가하면 자동적으로 객체가  생겨나게 됩니다. 그리고 호출은 다음과 같이 하면 됩니다. </span></span>

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">  
<div class="txc-textbox" style="BORDER-BOTTOM: #cbcbcb 1px solid; BORDER-LEFT: #cbcbcb 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #ffffff; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #cbcbcb 1px solid; BORDER-RIGHT: #cbcbcb 1px solid; PADDING-TOP: 10px"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">inputPanel1.Enabled = true; </span></span>  
</div></span></span>

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">특별히 Show(), Hide() 함수가 없이 <font color="#5c7fb0">**Enabled 속성**</font>을 통해서 제어하도록 되어 있습니다. 그런데 본래 I<font color="#c84205">nputPanel 자체가 드래그앤드롭으로 이동이 가능하기 때문에 특별히 위치 지정(Top, Left)을 할 수 없다는 단점을 가지고 있습니다.</font> 위치 지정이 안되면 사실 다른 여타의 컨트롤들을 가리는 등의 사용상의 불편함이 존재할 수가 있습니다. 때문에 위치지정은 필수입니다. (아이폰도 위치가 고정되어 있죠^^)</span></span>

**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">위치지정은 어떻게?</span></span>**

</div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2">  
<div style="BORDER-LEFT: #000000 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: #e8e8e8; PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, Sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: #fff; PADDING-TOP: 3px"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 1pt"></span></span></span></span></span></span></span></span></div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">﻿</span></span></font><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">﻿</span></span></font><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">﻿위치를 지정하는 방법은 native 라이브러리를 p/Invoke 를 이용해서 가져와서 쓰는 방법입니다. 윈도우와 관련된 부분이 많이 닷넷 클래스화가 되었다고 해도 여전히 native 라이브러리의 섬세함을 따라가기에는 부족함이 많다는 것을 느낍니다. 특히 WinCE 상에서는 더 그렇겠죠.^^</span></span>  
</font></span></span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">우선 DllImport 를 위해서는 다음의 네임스페이스를 추가해 주어야 합니다. </span></span><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">  
<div class="txc-textbox" style="BORDER-BOTTOM: #fe8943 1px solid; BORDER-LEFT: #fe8943 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #fedec7; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #fe8943 1px solid; BORDER-RIGHT: #fe8943 1px solid; PADDING-TOP: 10px"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">using System.Runtime.InteropServices;</span></span>  
</div></span></span>

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">네임스페이스를 추가해 준 후에는 다음의 코드를 Class 안에 넣어주시면 됩니다. </span></span>

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">  
<div class="txc-textbox" style="BORDER-BOTTOM: #79a5e4 1px solid; BORDER-LEFT: #79a5e4 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #dbe8fb; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #79a5e4 1px solid; BORDER-RIGHT: #79a5e4 1px solid; PADDING-TOP: 10px"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">        
        [DllImport(“coredll.dll”)]</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">        private static extern int SipShowIM(SIPStatus i);</span></span><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">        [DllImport(“coredll.dll”)]</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">        private static extern bool SipSetInfo(ref SIPINFO pSipInfo);</span></span>

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">        [DllImport(“coredll.dll”)]</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">        private static extern bool SipGetInfo(ref SIPINFO pSipInfo);</span></span>

</div></span></span>

</div></div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">사실 위치 지정을 위해서는 SipSetInfo 만 추가하면 되지만, SipShowIM은 InputPanel의 Enabled 와 같은 역할을 하는 것이고, SipiGetInfo는 설정정보를 가져오는 역할을 하는 함수 입니다. 자, 이렇게 추가를 했으면 그 다음에는 enum 과 구조체(Struct)를 추가해 줍니다. </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">       
<div class="txc-textbox" style="BORDER-BOTTOM: #c1c1c1 1px solid; BORDER-LEFT: #c1c1c1 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #eeeeee; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #c1c1c1 1px solid; BORDER-RIGHT: #c1c1c1 1px solid; PADDING-TOP: 10px">  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">   private struct SIPINFO</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">        {</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">            public Int32 cbSize;</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">            public Int32 fdwFlags;</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">            public RECT rcVisibleDesktop;</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">            public RECT rcSipRect;</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">            public Int32 dwImDataSize;</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">            public Int32 pvImData;</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">        }</span></span>  
</div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">        private struct RECT</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">        {</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">            public Int32 left;</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">            public Int32 top;</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">            public Int32 right;</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">            public Int32 bottom;</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">        }</span></span></div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">       </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">       private enum SIPStatus</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">        {</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">            SIPF_OFF = 0,</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">            SIPF_ON = 1</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">        }</span></span></div></div></span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">추가해 준 후에는 가장 중요한 SetPosition() 함수를 만들면 됩니다. SetPosition 함수는 Top 과 Left 를 파라미터로 받아서 위에서 추가한 SIPINFO 객체에 넣어주고 SIPINFO 객체는 DllImport로 추가한 SipSetInfo 함수로 넘겨주게 됩니다. </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">   
<div class="txc-textbox" style="BORDER-BOTTOM: #cbcbcb 1px solid; BORDER-LEFT: #cbcbcb 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #ffffff; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #cbcbcb 1px solid; BORDER-RIGHT: #cbcbcb 1px solid; PADDING-TOP: 10px"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">       public void SetPosition(Int32 top, Int32 left)</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">        {</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">            SIPINFO mySi = new SIPINFO();</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">            bool result = true;</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">            mySi.cbSize =</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">            System.Runtime.InteropServices.Marshal.SizeOf(typeof(SIPINFO));</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">            result = SipGetInfo(ref mySi);</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">            mySi.rcSipRect.top = top;</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">            mySi.rcSipRect.left = left;</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">            mySi.rcSipRect.bottom = top + 80;</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">            result = SipSetInfo(ref mySi);</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">        }</span></span>  
</div></span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">넘겨준 Top, Left 값에 의해서 화면상에 SIP 가 해당 위치를 기점으로 표시되게 되는것입니다. 그리 어렵지는 않지요^^ InputPanel 을 추가하시고 보여주고 안 보여주고 하는 부분은 Enabled 속성을 통해서 해도되고 추가한 함수 중에 SipShowIM() 함수를 이용해서 제어할 수도 있습니다. </span></span><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">SipShowIM 함수를 이용할때에는 특별히 InputPanel 을 추가하지 않아도 됩니다.   
</span></span>

<div class="txc-textbox" style="BORDER-BOTTOM: #f3c534 1px solid; BORDER-LEFT: #f3c534 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #fefeb8; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #f3c534 1px solid; BORDER-RIGHT: #f3c534 1px solid; PADDING-TOP: 10px"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"> SetPosition(10,10);</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"> SipShowIM(SIPStatus.SIPF_ON);</span></span>  
</div>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">이렇게 쓰셔도 상관 없습니다. 편한대로 쓰시면 됩니다. </span></span><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">  
<div class="txc-textbox" style="BORDER-BOTTOM: #f3c534 1px solid; BORDER-LEFT: #f3c534 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #fefeb8; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #f3c534 1px solid; BORDER-RIGHT: #f3c534 1px solid; PADDING-TOP: 10px"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"> SetPosition(10,10);</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"> inputPanel1.Enabled = true; </span></span>  
</div></span></span>

</div>

