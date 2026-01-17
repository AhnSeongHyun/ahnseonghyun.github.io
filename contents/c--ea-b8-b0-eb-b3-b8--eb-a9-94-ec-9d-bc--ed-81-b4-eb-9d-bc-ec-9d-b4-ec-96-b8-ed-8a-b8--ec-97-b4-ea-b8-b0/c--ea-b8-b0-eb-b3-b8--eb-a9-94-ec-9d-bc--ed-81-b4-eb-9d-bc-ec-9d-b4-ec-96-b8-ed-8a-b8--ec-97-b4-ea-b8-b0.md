---
title: '[C#] 기본 메일 클라이언트 열기'
author: 'ash84'
pub_date: '2010-01-15'
description: '<'
featured_image: ''
tags: ['basic mail clients', 'C#', 'c# 메일 보내기', 'call basic mail clients', 'dev', 'mapi', 'MAPI Wrapper', 'mapi32', '메일 보내기']
---
<div style="LINE-HEIGHT: 2">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
<div style="TEXT-ALIGN: justify">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
<div style="TEXT-ALIGN: justify">  
</div><span style="FONT-SIZE: 11pt">  
<div style="TEXT-ALIGN: justify"><span class="Apple-style-span" style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">기존의 MFC에서는 메일 클라이언트를 열기 위해서는 MAPI 라는것을 사용했었는데, .NET으로 넘어오면서 다양한 라이브러리를 지원해 주면서 파워포인트, 엑셀, 아웃룩 등등 MS Office와 연계해서 사용할 수 있도록 지원해주고 있습니다. </span></span></div><span style="FONT-FAMILY: Dotum">  
<div style="TEXT-ALIGN: justify">  
</div>**<span style="FONT-SIZE: 11pt">Microsoft.Office.Interop.Outlook</span>**<div>  
<div style="BORDER-LEFT: #000000 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: #e8e8e8; PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, Sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: #fff; PADDING-TOP: 3px"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 1pt"></span></span></span></span></span></span></span></span></div>  
<div style="LINE-HEIGHT: 1.7">  
<div style="TEXT-ALIGN: justify"><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt">이미 .NET의 참조추가를 통해서 아웃룩 관련 Dll을 추가하고 그에따른 클래스를 이용해서 아웃룩을 열고 제어할수 있습니다. ﻿</span></span></font><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt">﻿</span></span></font><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt">﻿</span></span></font></span></span></span><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt">하지만 </span>**<font color="#ec9c2c"><span style="FONT-SIZE: 10pt">Microsoft.Office.Interop.Outlook </span></font>**<span style="FONT-SIZE: 10pt">을 사용하는 경우에는 아웃룩 밖에는 열수 없는 단점이 있습니다. 그래서 사용자가 사용하는 메일 클라이언트를 이용하기 위해서는 기존에 쓰던 MAPI32를 Wrap한 Mapi Wrapper 클래스를 이용해야 합니다. </span></span>**<span style="FONT-SIZE: 11pt">MAPI Wrapper Class</span>**

</div>  
<div style="TEXT-ALIGN: justify">  
<div>  
<div style="BORDER-LEFT: #000000 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: #e8e8e8; PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, Sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: #fff; PADDING-TOP: 3px"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 1pt"></span></span></span></span></span></span></span></span></div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt">MAPI </span></span><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt">Wrapper 클래스에서는 Dll Import 이용해서 기존의 Win32에서 사용하는 ﻿</span></span></span></font><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt">﻿</span></span></span></font><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt">﻿</span></span></span></font><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt">﻿ MAPI32.Dll 을 가져와서 사용해야 합니다. </span></span></span><div class="txc-textbox" style="BORDER-BOTTOM: #79a5e4 1px solid; BORDER-LEFT: #79a5e4 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #dbe8fb; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #79a5e4 1px solid; BORDER-RIGHT: #79a5e4 1px solid; PADDING-TOP: 10px"><span style="FONT-SIZE: 11pt">       <span style="FONT-SIZE: 10pt">[DllImport(<font color="#e31600">“MAPI32.DLL”</font>)]</span></span>  
<span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt">        static extern int MAPISendMail(IntPtr sess, IntPtr hwnd, MapiMessage message, int flg, int rsv);</span></span>  
</div>  
[](http://ash84.net/wp-content/uploads/1/cfile6.uf.1351641F4B4FE66446F33C.cs)cfile6.uf.1351641F4B4FE66446F33C.cs  
**<span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 11pt">호출하는 부분 </span></span>**<div>  
<div style="BORDER-LEFT: #000000 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: #e8e8e8; PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, Sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: #fff; PADDING-TOP: 3px"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 1pt"></span></span></span></span></span></span></span></span></div>  
<div style="LINE-HEIGHT: 1.7"> </div></div></font></span></span></span></span></div></div></div></div></div></span></span></div></div></div></div></div></div></div></div>  
<div style="LINE-HEIGHT: 2">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
<div style="TEXT-ALIGN: justify">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
<div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt"><font color="#318561">  
<div class="txc-textbox" style="BORDER-BOTTOM: #9fd331 1px solid; BORDER-LEFT: #9fd331 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #e7fdb5; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #9fd331 1px solid; BORDER-RIGHT: #9fd331 1px solid; PADDING-TOP: 10px">  
<div style="LINE-HEIGHT: 2">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
<div style="TEXT-ALIGN: justify">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
<div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt"><font color="#318561"><span style="FONT-SIZE: 10pt">                              </span><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt">  </span><span style="FONT-SIZE: 10pt">MapiWrapper </span></span></font><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt">mapi = </span></span></span><font color="#193da9"><font size="+0"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt">new</span></span></span></font><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt"></span></span></span></font><span style="FONT-SIZE: 11pt"><font color="#318561"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt">MapiWrapper</span></span></font><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt">();</span></span></span></font></span></span></span></span></font></span></span></span></span></span></span></div></div></div></div></div></div></div></div>  
<div style="TEXT-ALIGN: center; LINE-HEIGHT: 2">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
<div style="TEXT-ALIGN: justify">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
<div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt">                                 </span><span style="FONT-SIZE: 10pt">mapi.AddAttachment(@”C:\MapiWrapper.cs”);</span></span></span></font></span></span></span></span></div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt">                               </span><span style="FONT-SIZE: 10pt">  mapi.SendMailPopup(“”, “”);</span></span></span></font></span></span></span></span></div></div></div></div></div></div></div></div></div></font></span></font></span></span></span></span><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><font color="#474747">  
</font></span></span></span></span></font></span></span></span></span></span></span></div></div></div></div></div></div></div></div>  
<div style="LINE-HEIGHT: 2"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum">  
<div>  
<div style="LINE-HEIGHT: 1.7">  
<div style="TEXT-ALIGN: justify">  
<div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><font color="#474747">  
<div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">MapiWrapper 클래스에 대한 객체를 만들고 첨부파일을 첨부하기 위해서는 AddAttachment() 함수를 사용하고 파라미터 값으로 해당 파일의 경로를 넣어주면 됩니다. 그후, SendMailPopup() 함수를 호출하면 기본 메일 클라이언트가 실행되면서 자동적으로 첨부파일이 첨부 된것을 확인할수가 있습니다.</span></span></span><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">만약, 메일 클라이언트를 실행시키지 않고 그냥 보내고 싶을 경우에는, SendMailDirect() 함수를 호출해서 사용하시면 됩니다. SendMailDirect와 SendMailPopup 함수는 둘다 모두 같은 두개의 파라미터 값을 요구합니다.</span> </span></span>  
     

<div class="txc-textbox" style="BORDER-BOTTOM: #fe8943 1px solid; BORDER-LEFT: #fe8943 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #fedec7; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #fe8943 1px solid; BORDER-RIGHT: #fe8943 1px solid; PADDING-TOP: 10px">  
<div style="LINE-HEIGHT: 1.7">        public int SendMailPopup(string strSubject, string strBody)  
         {  
           return SendMail(strSubject, strBody, MAPI_LOGON_UI | MAPI_DIALOG);  
         }</div>  
<div style="LINE-HEIGHT: 1.7">        public int SendMailDirect(string strSubject, string strBody)  
         {  
             return SendMail(strSubject, strBody, MAPI_LOGON_UI);  
         }  
</div></div>  
<span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt">strSubject 와 strBody 인자값은 각각 보낼 메일의 제목과 본문내용에 대한 파라미터기 때문에, 만약 제목과 본문도 지정해 주고 싶다면, 해당 파라미터에 내용을 넣어주시면 됩니다. </span>**여기서 한 가지 팁(Tip) : 현재 기본 메일 클라이언트 알아오기 **

<div>  
<div style="BORDER-LEFT: #000000 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: #e8e8e8; PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, Sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: #fff; PADDING-TOP: 3px"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 1pt"></span></span></span></span></span></span></span></span></div>  
<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 10pt">﻿</span></font><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 10pt">﻿</span></font><span style="FONT-FAMILY: Dotum"><font color="#474747"><span style="FONT-SIZE: 10pt">﻿</span></font><span style="FONT-SIZE: 10pt"><font color="#474747"><span style="FONT-SIZE: 11pt"><span style="FONT-SIZE: 10pt">위의 MapiWrapper 를 사용하면 현재 사용자 pc에 기본 메일 클라이언트로 메일을 보낼수가 있습니다. 하지만 그런 용도가 아니라 단순히 현재 기본 메일 클라이언트로 지정된것이 무엇인지 알고 싶을때는 아래와 같이 레지스터에서 값을 읽어오면 알수 있습니다. </span></span></font></span></span></span></span><span style="FONT-SIZE: 10pt">  
<div class="txc-textbox" style="BORDER-BOTTOM: #c1c1c1 1px solid; BORDER-LEFT: #c1c1c1 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #eeeeee; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #c1c1c1 1px solid; BORDER-RIGHT: #c1c1c1 1px solid; PADDING-TOP: 10px"><span style="FONT-SIZE: 10pt"><font color="#3058d2">object</font> mailClient   
 = <font color="#6abb9a">Registry</font>.GetValue(<font color="#e31600">@”HKEY_LOCAL_MACHINE\SOFTWARE\Clients\Mail”, “”, “none”</font>);</span>  
</div></span>  
![](http://ash84.net/wp-content/uploads/1/cfile8.uf.11056F164B4FED8C60D720.jpg)  
  
<span id="tx_afterend_mark"></span>  
</div></div></span></div></div>  
</font></span></span></span></span></div></div></div>  
<div style="TEXT-ALIGN: justify"> </div></div></div></span></span></div>

