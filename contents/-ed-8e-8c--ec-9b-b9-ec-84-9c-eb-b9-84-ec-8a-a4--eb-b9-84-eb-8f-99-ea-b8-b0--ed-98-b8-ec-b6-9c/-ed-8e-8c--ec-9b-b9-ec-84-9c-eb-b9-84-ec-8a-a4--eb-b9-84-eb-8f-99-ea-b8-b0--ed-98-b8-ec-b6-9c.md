---
title: '[펌] 웹서비스 비동기 호출'
author: 'ash84'
pub_date: '2015-07-03'
description: '웹 서비스의 비동기 호출 방법에 대해 정리한 글입니'
featured_image: ''
tags: ['dev']
---


<table align="center" border="0" cellpadding="0" cellspacing="0" width="760"><tbody><tr><td colspan="2" height="100" valign="top"><style><p>				p, td, ul, ol, li { font-size:12px; line-height:140%; margin-top:0; margin-bottom:0; }
				body { font-size:12px; }
			</style>웹 서비스의 비동기 호출 방법에 대해 정리한 글입니다

닷넷 1.x 기반의 비동기 웹 서비스 호출 방법을 알아 본 뒤 2.0 의 이벤트 기반 비동기 호출에 대해 알아 봅니다

아래의 글을 참고해 주세요

———————————————————————————————————

**<span style="FONT-SIZE: 11pt; FONT-FAMILY: 돋움">『 비 동기 웹 서비스 호출』<span></span></span>**

**<span style="FONT-SIZE: 11pt; FONT-FAMILY: 돋움"> </span>**

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">.NET Framework </span><span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">는 파일에 대한<span> I/O </span>및 네트워크 통신 등에 <span style="COLOR: blue">비 동기 호출 메커니즘</span>을 지원해 왔다<span>.</span></span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">또한<span> ADO.NET 2.0 </span>에서는 데이터베이스 관련 작업에도 비 동기 호출을 지원하기 시작했다<span>.</span></span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">물론 <span style="COLOR: blue">ASP.NET XML WebService </span><span style="COLOR: blue">에서도 비 동기 호출을 지원</span>한다<span>.</span></span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">이번 글에서는 웹 서비스에서의 비 동기 호출 방법에 대해 알아보도록 한다<span></span></span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움"> </span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">우선 알아두어야 할 것이 비 동기 웹 서비스 호출이<span> .NET Framework 1.x </span>와<span> 2.0 </span>의 차이점이 있다는 것이다<span>. </span></span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">즉 <span style="COLOR: blue">.NET Framework 2.0</span><span style="COLOR: blue">에서는 기존의<span> 1.x </span>에서의 비 동기 호출 보다 직관적이고 이벤트 지향적으로 변경</span>되었다<span>.</span></span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움"> </span>

<font size="2">**<span style="FONT-FAMILY: 돋움; ">1. .NET Framework 1.x </span>****<span style="FONT-FAMILY: 돋움; ">에서의 웹 서비스 비 동기 호출<span></span></span>**</font>

<font size="2">**<span style="FONT-FAMILY: 돋움; "><span></span></span>**</font> 

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">우선 예전 방식<span>(1.x) </span>에서의 비 동기 호출 방법에 대해 알아보자<span>.</span></span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">아래와 같이 간단한 웹 서비스의<span> HelloWorld </span>웹 메서드를 만들어 보자<span>.</span></span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움"><span></span></span> 

<table border="1" cellpadding="0" cellspacing="0" style="BORDER-RIGHT: medium none; BORDER-TOP: medium none; FONT-SIZE: 9pt; MARGIN: auto auto auto 5.4pt; BORDER-LEFT: medium none; LINE-HEIGHT: 140%; BORDER-BOTTOM: medium none; FONT-FAMILY: verdana,굴림; BORDER-COLLAPSE: collapse; mso-border-alt: solid windowtext .5pt; mso-yfti-tbllook: 480; mso-padding-alt: 0cm 5.4pt 0cm 5.4pt; mso-border-insideh: .5pt solid windowtext; mso-border-insidev: .5pt solid windowtext"><tbody><tr style="mso-yfti-irow: 0; mso-yfti-firstrow: yes; mso-yfti-lastrow: yes"><td style="BORDER-RIGHT: black 1pt solid; PADDING-RIGHT: 5.4pt; BORDER-TOP: black 1pt solid; PADDING-LEFT: 5.4pt; FONT-SIZE: 9pt; PADDING-BOTTOM: 0cm; BORDER-LEFT: black 1pt solid; WIDTH: 429.7pt; LINE-HEIGHT: 140%; PADDING-TOP: 0cm; BORDER-BOTTOM: black 1pt solid; FONT-FAMILY: verdana,굴림; BACKGROUND-COLOR: transparent; mso-border-alt: solid windowtext .5pt" valign="top" width="573"><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><font size="2">[WebMethod]</font></span>

<font size="2"><span style="COLOR: blue; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt">public</span><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><span style="COLOR: blue">string</span> HelloWorld(<span style="COLOR: blue">string</span> name)</span></font>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><font size="2">{</font></span>

<font size="2"><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><span style="mso-spacerun: yes">      </span><span style="COLOR: green">//</span></span><span style="COLOR: green; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt">고의로 약<span> 2</span>초 정도 지연시간을 준다</span><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"></span></font>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><font size="2">System.Threading.Thread.Sleep(2000);</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><font size="2"> </font></span>

<font size="2"><span style="COLOR: blue; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt">return</span><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"> “Hello ” + name;</span></font>

<font size="2"><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt">}</span><span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움"></span></font>

</td></tr></tbody></table>    
 

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">이렇게 웹 메서드가 만들어 지고 난 후 클라이언트 프로그램을 만들어 웹 참조<span>(Web References)</span>를 하도록 한다<span>.</span></span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">웹 서비스를 참조 하면 아래 그림처럼 클라이언트의 웹 참조 항목아래에 보면 **<span>References.cs</span>**<span></span>라는<span></span></span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">클래스가 있다<span> (References.cs </span>파일은 <span>‘</span>모든 파일 표시<span>’</span>를 해야 나타난다<span>)</span></span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움"><span></span></span> 

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움"><shapetype coordsize="21600,21600" filled="f" id="_x0000_t75" o:preferrelative="t" o:spt="75" path="m@4@5l@4@11@9@11@9@5xe" stroked="f"><stroke joinstyle="miter"></stroke><formulas><f eqn="if lineDrawn pixelLineWidth 0"></f><f eqn="sum @0 1 0"></f><f eqn="sum 0 0 @1"></f><f eqn="prod @2 1 2"></f><f eqn="prod @3 21600 pixelWidth"></f><f eqn="prod @3 21600 pixelHeight"></f><f eqn="sum @0 0 1"></f><f eqn="prod @6 1 2"></f><f eqn="prod @7 21600 pixelWidth"></f><f eqn="sum @8 21600 0"></f><f eqn="prod @7 21600 pixelHeight"></f><f eqn="sum @10 21600 0"></f></formulas><path gradientshapeok="t" o:connecttype="rect" o:extrusionok="f"></path><lock aspectratio="t" v:ext="edit"></lock></shapetype></span>

![](http://pds.devpia.com/MAEUL/8/csharp_lec/2000/1286/1.gif)

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">이 파일은 웹 서비스를 원격 호출 가능케 하는 **<span>Proxy </span>클래스**인데<span>,</span></span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">파일을 열어 보면 우리가 작성한 웹 메서드인<span> HelloWorld </span>에 관련된 메서드가 총<span> 3</span>개 있음을 알 수 있다<span>.</span></span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움"><span></span></span> 

<table border="1" cellpadding="0" cellspacing="0" style="BORDER-RIGHT: medium none; BORDER-TOP: medium none; FONT-SIZE: 9pt; MARGIN: auto auto auto 5.4pt; BORDER-LEFT: medium none; LINE-HEIGHT: 140%; BORDER-BOTTOM: medium none; FONT-FAMILY: verdana,굴림; BORDER-COLLAPSE: collapse; mso-border-alt: solid windowtext .5pt; mso-yfti-tbllook: 480; mso-padding-alt: 0cm 5.4pt 0cm 5.4pt; mso-border-insideh: .5pt solid windowtext; mso-border-insidev: .5pt solid windowtext"><tbody><tr style="mso-yfti-irow: 0; mso-yfti-firstrow: yes; mso-yfti-lastrow: yes"><td style="BORDER-RIGHT: black 1pt solid; PADDING-RIGHT: 5.4pt; BORDER-TOP: black 1pt solid; PADDING-LEFT: 5.4pt; FONT-SIZE: 9pt; PADDING-BOTTOM: 0cm; BORDER-LEFT: black 1pt solid; WIDTH: 549pt; LINE-HEIGHT: 140%; PADDING-TOP: 0cm; BORDER-BOTTOM: black 1pt solid; FONT-FAMILY: verdana,굴림; BACKGROUND-COLOR: transparent; mso-border-alt: solid windowtext .5pt" valign="top" width="732"><font size="2"><span style="COLOR: gray; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt">///</span><span style="COLOR: green; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"></span><span style="COLOR: gray; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><remarks/></span></font>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><font size="2">[System.Web.Services.Protocols.SoapDocumentMethodAttribute(“http://tempuri.org/Hello  
World”, RequestNamespace=”http://tempuri.org/”, ResponseNamespace=”http://tempuri.org/  
“, Use=System.Web.Services.Description.SoapBindingUse.Literal, ParameterStyle=System.Web.Services.Protocols.SoapParameterStyle.Wrapped)]</font></span>

<font size="2"><span style="COLOR: blue; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt">public</span><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><span style="COLOR: blue">string</span>**<span style="COLOR: red">HelloWorld</span>**(<span style="COLOR: blue">string</span> name) {</span></font>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><font size="2"><span style="mso-spacerun: yes">   </span><span style="mso-spacerun: yes"> </span><span style="COLOR: blue">object</span>[] results = <span style="COLOR: blue">this</span>.Invoke(“HelloWorld”, <span style="COLOR: blue">new</span><span style="COLOR: blue">object</span>[] {name});</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><font size="2"><span style="mso-spacerun: yes">    </span><span style="COLOR: blue">return</span> ((<span style="COLOR: blue">string</span>)(results[0]));</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><font size="2">}</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><font size="2"><span style="mso-spacerun: yes">        </span></font></span>

<font size="2"><span style="COLOR: gray; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt">///</span><span style="COLOR: green; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"></span><span style="COLOR: gray; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><remarks/></span></font>

<font size="2"><span style="COLOR: blue; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt">public</span><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"> System.IAsyncResult **<span style="COLOR: red">BeginHelloWorld</span>**(<span style="COLOR: blue">string</span> name, System.AsyncCallback callback  
, <span style="COLOR: blue">object</span> asyncState) {</span></font>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><font size="2"><span style="mso-spacerun: yes">    </span><span style="COLOR: blue">return</span><span style="COLOR: blue">this</span>.BeginInvoke(“HelloWorld”, <span style="COLOR: blue">new</span><span style="COLOR: blue">object</span>[] {name}, callback, asyncState);</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><font size="2">}</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><font size="2"><span style="mso-spacerun: yes">        </span></font></span>

<font size="2"><span style="COLOR: gray; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt">///</span><span style="COLOR: green; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"></span><span style="COLOR: gray; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><remarks/></span></font>

<font size="2"><span style="COLOR: blue; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt">public</span><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><span style="COLOR: blue">string</span>**<span style="COLOR: red">EndHelloWorld</span>**(System.IAsyncResult asyncResult) {</span></font>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><font size="2"><span style="mso-spacerun: yes">    </span><span style="COLOR: blue">object</span>[] results = <span style="COLOR: blue">this</span>.EndInvoke(asyncResult);</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><font size="2"><span style="mso-spacerun: yes">    </span><span style="COLOR: blue">return</span> ((<span style="COLOR: blue">string</span>)(results[0]));</font></span>

<font size="2"><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt">}</span><span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움"></span></font>

</td></tr></tbody></table><span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움"> </span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">우리가 작성한<span> HelloWorld </span>이외에도 **<span>BeginHelloWorld</span>**<span>, **EndHelloWorld**</span>메서드가 자동으로 추가되어 있다<span>.</span></span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">이 두 메서드가 바로<span> 1.x </span>에서 비 동기 웹 서비스 호출을 위해 자동으로 생성되는 메서드 인 것이다<span>.</span></span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움"> </span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">클라이언트에서 비 동기로 웹 서비스를 호출하는 코드를 보자</span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움"><span></span></span> 

<table border="1" cellpadding="0" cellspacing="0" style="BORDER-RIGHT: medium none; BORDER-TOP: medium none; FONT-SIZE: 9pt; MARGIN: auto auto auto 5.4pt; BORDER-LEFT: medium none; LINE-HEIGHT: 140%; BORDER-BOTTOM: medium none; FONT-FAMILY: verdana,굴림; BORDER-COLLAPSE: collapse; mso-border-alt: solid windowtext .5pt; mso-yfti-tbllook: 480; mso-padding-alt: 0cm 5.4pt 0cm 5.4pt; mso-border-insideh: .5pt solid windowtext; mso-border-insidev: .5pt solid windowtext"><tbody><tr style="mso-yfti-irow: 0; mso-yfti-firstrow: yes; mso-yfti-lastrow: yes"><td style="BORDER-RIGHT: black 1pt solid; PADDING-RIGHT: 5.4pt; BORDER-TOP: black 1pt solid; PADDING-LEFT: 5.4pt; FONT-SIZE: 9pt; PADDING-BOTTOM: 0cm; BORDER-LEFT: black 1pt solid; WIDTH: 549pt; LINE-HEIGHT: 140%; PADDING-TOP: 0cm; BORDER-BOTTOM: black 1pt solid; FONT-FAMILY: verdana,굴림; BACKGROUND-COLOR: transparent; mso-border-alt: solid windowtext .5pt" valign="top" width="732"><font size="2"><span style="COLOR: green; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt">//</span><span style="COLOR: green; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt">웹 서비스 객체<span></span></span></font>

<font size="2"><span style="COLOR: blue; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt">private</span><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"> localhost.Service1 proxy;</span></font>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><font size="2"> </font></span>

<font size="2"><span style="COLOR: green; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt">//</span><span style="COLOR: green; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt">비동기로<span> HelloWorld </span>호출<span></span></span></font>

<font size="2"><span style="COLOR: blue; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt">private</span><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><span style="COLOR: blue">void</span> button1_Click(<span style="COLOR: blue">object</span> sender, System.EventArgs e)</span></font>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><font size="2">{</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><font size="2"><span style="mso-tab-count: 1">        </span><span style="COLOR: blue">this</span>.proxy = <span style="COLOR: blue">new</span> localhost.Service1();</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><font size="2"><span style="mso-tab-count: 1">        </span>proxy.**<span style="COLOR: blue">BeginHelloWorld</span>**(“MKEX”,<span style="COLOR: blue">new</span> System.AsyncCallback(CallbackMethod),<span style="COLOR: blue">null</span>);</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><font size="2">}</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><font size="2"> </font></span>

<font size="2"><span style="COLOR: blue; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt">public</span><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><span style="COLOR: blue">void</span> CallbackMethod(IAsyncResult ar)</span></font>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><font size="2">{<span style="mso-tab-count: 1">       </span></font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><font size="2"><span style="mso-tab-count: 1">        </span><span style="COLOR: blue">string</span> result = proxy.**<span style="COLOR: blue">EndHelloWorld</span>**(ar);</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt"><font size="2"><span style="mso-tab-count: 1">        </span>MessageBox.Show(result);</font></span>

<font size="2"><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt">}</span><span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움"></span></font>

</td></tr></tbody></table><span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움"> </span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">HelloWorld </span><span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">웹 메서드를 비 동기로 호출하기 위해서는 **<span>BeginHelloWorld</span>**<span></span>을 호출해야 한다<span>.</span></span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">이때 매개변수를 전달하고 비 동기 작업 완료 시 호출 될<span> Callback </span>메서드를 지정한다<span>. </span></span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">Callback </span><span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">메서드에서는 다시 **<span>EndHelloWorld</span>**<span></span>를 호출하여 비 동기 작업 상태 및 참조 매개변수를 넘겨준다<span>(</span>있을   
경우<span>)</span></span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움"> </span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">이 샘플 프로젝트를 수행해 보면 웹 메서드를 호출하고 난 뒤 기다리는 시간 동안 블로킹이 되지 않고 다른 작업을<span></span></span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">수행할 수 있음을 알 수 있다<span>. </span>즉 비 동기로 웹 서비스가 호출되는 것이다<span></span></span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움"> </span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움"></span> 

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움"></span> 

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움"></span> 

<font size="2">**<span style="FONT-FAMILY: 돋움; ">2. .NET Framework 2.0 </span>****<span style="FONT-FAMILY: 돋움; ">에서의 웹 서비스 비 동기 호출<span></span></span>**</font>

<font size="2">**<span style="FONT-FAMILY: 돋움; "><span></span></span>**</font> 

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">이제<span> 2.0</span>에서의 비 동기 웹 서비스 호출 방법에 대해 알아보자<span>.</span></span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">위의 샘플과 동일한 웹 서비스를 만들고 클라이언트에 웹 참조를 한 뒤 **<span>Reference.cs</span>**<span></span>의 코드를 살펴 보자<span>.</span></span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움"><span></span></span> 

<table border="1" cellpadding="0" cellspacing="0" style="BORDER-RIGHT: medium none; BORDER-TOP: medium none; FONT-SIZE: 9pt; BORDER-LEFT: medium none; LINE-HEIGHT: 140%; BORDER-BOTTOM: medium none; FONT-FAMILY: verdana,굴림; BORDER-COLLAPSE: collapse; mso-border-alt: solid windowtext .5pt; mso-yfti-tbllook: 480; mso-padding-alt: 0cm 5.4pt 0cm 5.4pt; mso-border-insideh: .5pt solid windowtext; mso-border-insidev: .5pt solid windowtext"><tbody><tr style="mso-yfti-irow: 0; mso-yfti-firstrow: yes; mso-yfti-lastrow: yes"><td style="BORDER-RIGHT: black 1pt solid; PADDING-RIGHT: 5.4pt; BORDER-TOP: black 1pt solid; PADDING-LEFT: 5.4pt; FONT-SIZE: 9pt; PADDING-BOTTOM: 0cm; BORDER-LEFT: black 1pt solid; WIDTH: 554.4pt; LINE-HEIGHT: 140%; PADDING-TOP: 0cm; BORDER-BOTTOM: black 1pt solid; FONT-FAMILY: verdana,굴림; BACKGROUND-COLOR: transparent; mso-border-alt: solid windowtext .5pt" valign="top" width="739"><font size="2"><span style="COLOR: gray; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">///</span><span style="COLOR: green; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"></span><span style="COLOR: gray; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><remarks/></span></font>

<font size="2"><span style="COLOR: blue; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">public</span><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><span style="COLOR: blue">event</span><span style="COLOR: #2b91af">HelloWorldCompletedEventHandler</span>**<span style="COLOR: red">HelloWorldCompleted</span>**;</span></font>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="mso-spacerun: yes">        </span></font></span>

<font size="2"><span style="COLOR: gray; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">///</span><span style="COLOR: green; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"></span><span style="COLOR: gray; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><remarks/></span></font>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="mso-spacerun: yes"> </span>[System.Web.Services.Protocols.<span style="COLOR: #2b91af">SoapDocumentMethodAttribute</span>(<span style="COLOR: #a31515">“http://tempuri.org/HelloWo  
rld”</span>, RequestNamespace=<span style="COLOR: #a31515">“http://tempuri.org/”</span>, ResponseNamespace=<span style="COLOR: #a31515">“http://tempuri.org/”</span>,   
Use=System.Web.Services.Description.<span style="COLOR: #2b91af">SoapBindingUse</span>.Literal, ParameterStyle=System.Web.Services.Protocols.<span style="COLOR: #2b91af">SoapParameterStyle</span>.Wrapped)]</font></span>

<font size="2"><span style="COLOR: blue; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">public</span><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><span style="COLOR: blue">string</span>**<span style="COLOR: red">HelloWorld</span>**(<span style="COLOR: blue">string</span> name) {</span></font>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="mso-spacerun: yes">    </span><span style="COLOR: blue">object</span>[] results = <span style="COLOR: blue">this</span>.Invoke(<span style="COLOR: #a31515">“HelloWorld”</span>, <span style="COLOR: blue">new</span><span style="COLOR: blue">object</span>[] {name});</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="mso-spacerun: yes">    </span><span style="COLOR: blue">return</span> ((<span style="COLOR: blue">string</span>)(results[0]));</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2">}</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="mso-spacerun: yes">        </span></font></span>

<font size="2"><span style="COLOR: gray; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">///</span><span style="COLOR: green; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"></span><span style="COLOR: gray; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><remarks/></span></font>

<font size="2"><span style="COLOR: blue; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">public</span><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><span style="COLOR: blue">void</span>**<span style="COLOR: red">HelloWorldAsync</span>**(<span style="COLOR: blue">string</span> name) {</span></font>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="mso-spacerun: yes">    </span><span style="COLOR: blue">this</span>.HelloWorldAsync(name, <span style="COLOR: blue">null</span>);</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2">}</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="mso-spacerun: yes">        </span></font></span>

<font size="2"><span style="COLOR: gray; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">///</span><span style="COLOR: green; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"></span><span style="COLOR: gray; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><remarks/></span></font>

<font size="2"><span style="COLOR: blue; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">public</span><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><span style="COLOR: blue">void</span>**<span style="COLOR: red">HelloWorldAsync</span>**(<span style="COLOR: blue">string</span> name, <span style="COLOR: blue">object</span> userState) {</span></font>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="mso-spacerun: yes">    </span><span style="COLOR: blue">if</span> ((<span style="COLOR: blue">this</span>.HelloWorldOperationCompleted == <span style="COLOR: blue">null</span>)) {</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="mso-spacerun: yes">        </span><span style="COLOR: blue">this</span>.HelloWorldOperationCompleted = <span style="COLOR: blue">new</span> System.Threading.<span style="COLOR: #2b91af">SendOrPostCallback</span>(<span style="COLOR: blue">this</span>.OnHelloWorldOperationCompleted);</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="mso-spacerun: yes">    </span>}</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="mso-spacerun: yes">    </span><span style="COLOR: blue">this</span>.InvokeAsync(<span style="COLOR: #a31515">“HelloWorld”</span>, <span style="COLOR: blue">new</span><span style="COLOR: blue">object</span>[] {</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="mso-spacerun: yes">                </span>name}, <span style="COLOR: blue">this</span>.HelloWorldOperationCompleted, userState);</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2">}</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="mso-spacerun: yes">        </span></font></span>

<font size="2"><span style="COLOR: blue; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">private</span><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><span style="COLOR: blue">void</span>**<span style="COLOR: red">OnHelloWorldOperationCompleted</span>**(<span style="COLOR: blue">object</span> arg) {</span></font>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="mso-spacerun: yes">    </span><span style="COLOR: blue">if</span> ((<span style="COLOR: blue">this</span>.HelloWorldCompleted != <span style="COLOR: blue">null</span>)) {</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="mso-spacerun: yes">        </span>System.Web.Services.Protocols.<span style="COLOR: #2b91af">InvokeCompletedEventArgs</span> invokeArgs = ((System.Web.Services.Protocols.<span style="COLOR: #2b91af">InvokeCompletedEventArgs</span>)(arg));</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="mso-spacerun: yes">        </span><span style="COLOR: blue">this</span>.HelloWorldCompleted(<span style="COLOR: blue">this</span>, <span style="COLOR: blue">new</span><span style="COLOR: #2b91af">HelloWorldCompletedEventArgs</span>(invokeArgs.  
Results, invokeArgs.Error, invokeArgs.Cancelled, invokeArgs.UserState));</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="mso-spacerun: yes">    </span>}</font></span>

<font size="2"><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">}</span><span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움"></span></font>

</td></tr></tbody></table><span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움"> </span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">1.x </span><span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">의<span> Reference.cs </span>와 확연히 달라진 코드임을 알 수 있다<span>.</span></span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">즉<span> 1.x </span>에서의<span> BeginXXX, EndXXX </span>와 같은 메서드는 없어지고 대신 비 동기 완료를 통지 받기 위한 이벤트<span>(</span></span><font size="2">**<span style="COLOR: #2b91af; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">HelloWorldCompletedEventHandler</span>**<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">)</span></font><span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">와<span></span></span><span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">비 동기 웹 메서드</span><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"></font></span><span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">코드<span>(</span></span>**<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2">HelloWorldAsync</font></span>**<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">), </span><span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">이벤트 호출 코드<span>(</span></span><font size="2">**<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">OnHelloWorldOperationComplete</span>**<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">)</span></font><span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움"></span><span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">자동으로 생성된 것을 볼 수 있다<span>.</span></span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움"> </span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움">클라이언트에서 비 동기로 웹 서비스를 호출하는 코드를 보자</span>

<span style="FONT-SIZE: 9pt; FONT-FAMILY: 돋움"><span></span></span> 

<table border="1" cellpadding="0" cellspacing="0" style="BORDER-RIGHT: medium none; BORDER-TOP: medium none; FONT-SIZE: 9pt; BORDER-LEFT: medium none; LINE-HEIGHT: 140%; BORDER-BOTTOM: medium none; FONT-FAMILY: verdana,굴림; BORDER-COLLAPSE: collapse; mso-border-alt: solid windowtext .5pt; mso-yfti-tbllook: 480; mso-padding-alt: 0cm 5.4pt 0cm 5.4pt; mso-border-insideh: .5pt solid windowtext; mso-border-insidev: .5pt solid windowtext"><tbody><tr style="mso-yfti-irow: 0; mso-yfti-firstrow: yes; mso-yfti-lastrow: yes"><td style="BORDER-RIGHT: black 1pt solid; PADDING-RIGHT: 5.4pt; BORDER-TOP: black 1pt solid; PADDING-LEFT: 5.4pt; FONT-SIZE: 9pt; PADDING-BOTTOM: 0cm; BORDER-LEFT: black 1pt solid; WIDTH: 554.4pt; LINE-HEIGHT: 140%; PADDING-TOP: 0cm; BORDER-BOTTOM: black 1pt solid; FONT-FAMILY: verdana,굴림; BACKGROUND-COLOR: transparent; mso-border-alt: solid windowtext .5pt" valign="top" width="739"><font size="2"><span style="COLOR: blue; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">private</span><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><span style="COLOR: blue">void</span> button3_Click(<span style="COLOR: blue">object</span> sender, <span style="COLOR: #2b91af">EventArgs</span> e)</span></font>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2">{</font></span>

<font size="2"><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><span style="mso-spacerun: yes">    </span><span style="COLOR: green">//</span></span><span style="COLOR: green; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">웹 서비스 객체<span></span></span></font>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="mso-spacerun: yes">    </span>localhost.<span style="COLOR: #2b91af">Service1</span> proxy = <span style="COLOR: blue">new</span> WindowsApplication4.localhost.<span style="COLOR: #2b91af">Service1</span>();</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="COLOR: green">    //</span><span style="COLOR: green; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">비동기 완료시 통지받을 이벤트 핸들러 등록<span></span></span></font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="mso-spacerun: yes">    </span>proxy.HelloWorldCompleted +=   
<span style="COLOR: blue">new</span> WindowsApplication4.localhost.<span style="COLOR: #2b91af">HelloWorldCompletedEventHandler  
</span>(proxy_HelloWorldCompleted);</font></span></font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"></font></span> </font></span>

<font size="2"><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><span style="mso-spacerun: yes">    </span><span style="COLOR: green">//</span></span><span style="COLOR: green; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">비동기로<span> HelloWorld </span>호출<span></span></span></font>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="mso-spacerun: yes">     </span>proxy.HelloWorldAsync(<span style="COLOR: #a31515">“MKEX”</span>);</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2">}</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"> </font></span>

<font size="2"><span style="COLOR: green; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">//</span><span style="COLOR: green; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">비동기 웹 서비스 호출 완료시 수행되는 이벤트 메서드<span></span></span></font>

<font size="2"><span style="COLOR: blue; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">public</span><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><span style="COLOR: blue">void</span> proxy_HelloWorldCompleted(<span style="COLOR: blue">object</span> sender,localhost.  
<span style="COLOR: #2b91af">HelloWorldCompletedEventArgs</span> e)</span></font>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2">{</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="mso-spacerun: yes">    </span><span style="COLOR: #2b91af">MessageBox</span>.Show(e.Result);</font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2">}</font></span>

</td></tr></tbody></table>    
 

<font size="2"><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">1.x </span><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">와는 달리 보다 직관적이고 이벤트 지향적으로 변경되었음을 알 수 있다<span>.</span></span></font>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2">비 동기 작업 완료시 통지받을 이벤트를 등록하고,</font></span><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2">비동기 웹 메서드를 호출하기 위해<span>  
XXXAsync </span>메서드를 호출한다. </font></span></font></span><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2">이 이벤트 핸들러 메서드에서는 전달된   
매개변수<span>(<span style="COLOR: #2b91af">HelloWorldCompletedEventArgs</span>)</span>를 통해 웹 메서드의 반환값을 가져올 수 </font></span><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2">있게   
되는 것이다<span>.</span></font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"> </font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"></span> <span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><span style="COLOR: red; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes; mso-bidi-font-family: 굴림"><font size="2">※ 주의사항</font></span></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><span style="COLOR: red; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes; mso-bidi-font-family: 굴림"><font size="2"><span></span></font></span>  </span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes; mso-bidi-font-family: 굴림"><font size="2">앞서 샘플 코드에서는 비 동기 작업 완료 통지를 받기 위한 이벤트를 웹 메서드 호출할 때   
등록했었는데<span>, </span></font></span></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes; mso-bidi-font-family: 굴림"><font size="2">아래처럼<span>..</span></font></span></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes; mso-bidi-font-family: 굴림"><font size="2"><span></span></font></span>  </span>

<table border="1" cellpadding="0" cellspacing="0" style="BORDER-RIGHT: medium none; BORDER-TOP: medium none; FONT-SIZE: 9pt; MARGIN: auto auto auto 5.4pt; BORDER-LEFT: medium none; LINE-HEIGHT: 140%; BORDER-BOTTOM: medium none; FONT-FAMILY: verdana,굴림; BORDER-COLLAPSE: collapse; mso-border-alt: solid windowtext .5pt; mso-yfti-tbllook: 480; mso-padding-alt: 0cm 5.4pt 0cm 5.4pt; mso-border-insideh: .5pt solid windowtext; mso-border-insidev: .5pt solid windowtext"><tbody><tr style="mso-yfti-irow: 0; mso-yfti-firstrow: yes; mso-yfti-lastrow: yes"><td style="BORDER-RIGHT: black 1pt solid; PADDING-RIGHT: 5.4pt; BORDER-TOP: black 1pt solid; PADDING-LEFT: 5.4pt; FONT-SIZE: 9pt; PADDING-BOTTOM: 0cm; BORDER-LEFT: black 1pt solid; WIDTH: 549pt; LINE-HEIGHT: 140%; PADDING-TOP: 0cm; BORDER-BOTTOM: black 1pt solid; FONT-FAMILY: verdana,굴림; BACKGROUND-COLOR: transparent; mso-border-alt: solid windowtext .5pt" valign="top" width="732"><font size="2"><span style="COLOR: green; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">//</span><span style="COLOR: green; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">비동기 완료시 통지받을 이벤트 핸들러 등록<span></span></span></font>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2">proxy.HelloWorldCompleted += <span style="COLOR: blue">new</span> WindowsApplication4.localhost.<span style="COLOR: #2b91af">HelloWorldCompletedEventHandler</span>(proxy_HelloWorldCompleted);</font></span>

<font size="2"><span style="COLOR: green; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">//</span><span style="COLOR: green; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">비동기로<span> HelloWorld </span>호출<span></span></span></font>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2">proxy.HelloWorldAsync(<span style="COLOR: #a31515">“MKEX”</span>);</font></span>

<span style="FONT-SIZE: 12pt; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes; mso-bidi-font-family: 굴림"> </span>

</td></tr></tbody></table><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes; mso-bidi-font-family: 굴림"><font size="2"> </font></span></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2">여기에 주의사항이 있다<span>.</span></font></span></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span></span></font></span> <font size="2"><span style="FONT-FAMILY: 'Times New Roman'; ; mso-font-kerning: 0pt; mso-no-proof: yes; mso-ascii-font-family: 돋움체; mso-fareast-font-family: 돋움체"></span></font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="FONT-FAMILY: 'Times New Roman'; ; mso-font-kerning: 0pt; mso-no-proof: yes; mso-ascii-font-family: 돋움체; mso-fareast-font-family: 돋움체">***<span style="COLOR: red; FONT-FAMILY: 'Times New Roman'; ; mso-font-kerning: 0pt; mso-no-proof: yes; mso-ascii-font-family: 돋움체; mso-fareast-font-family: 돋움체">“</span><span style="COLOR: red; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes">이벤트는 한번만 등록되어야 한다</span>******<span style="COLOR: red; FONT-FAMILY: 'Times New Roman'; ; mso-font-kerning: 0pt; mso-no-proof: yes; mso-ascii-font-family: 돋움체; mso-fareast-font-family: 돋움체">”</span>******<span style="COLOR: red; FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"></span>***</span></font></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"></span></font>  </span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2">만일 윈폼 응용프로그램과 같이 웹 서비스 프록시 객체를 미리 생성하고 난 뒤 그 객체를   
계속적으로 사용할 경우<span></span></font></span></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2">위 처럼 웹 메서드를 호출할 때 마다 완료 이벤트를 등록하면 중복 등록되게 되는 것이다<span>.</span></font></span></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2"><span></span></font></span>  </span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2">따라서 이런 경우라면<span>, </span>반드시 프록시 객체의 생성하는 곳에서 각 웹 메서드에 해당하는   
완료 이벤트를 미리 등록하고 난 뒤<span></span></font></span></span><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"><font size="2">실제 웹 메서드 호출할때는 별도로 등록하지 않도록   
해야 한다<span>.</span></font></span></span>

<span style="FONT-FAMILY: 돋움체; ; mso-hansi-font-family: 'Times New Roman'; mso-font-kerning: 0pt; mso-no-proof: yes"></span> 

</td></tr></tbody></table>출처 : [http://www.devpia.com/MAEUL/Contents/Detail.aspx?BoardID=18&MAEULNO=8&no=1286](http://www.devpia.com/MAEUL/Contents/Detail.aspx?BoardID=18&MAEULNO=8&no=1286)

<div id="daum_book" style="CLEAR: both; BORDER-RIGHT: #eeeeee 1px solid; PADDING-RIGHT: 10px; BORDER-TOP: #eeeeee 1px solid; PADDING-LEFT: 10px; PADDING-BOTTOM: 10px; MARGIN: 5px 0px 0px; BORDER-LEFT: #eeeeee 1px solid; WIDTH: 94%; PADDING-TOP: 10px; BORDER-BOTTOM: #eeeeee 1px solid">[![](http://photo-book.hanmail.net/images/book/large/911/l9788956740911.jpg)](http://book.daum.net/bookdetail/book.do?bookid=KOR9788956740911) [NET.XML 웹서비스 STEP BY STEP](http://book.daum.net/bookdetail/book.do?bookid=KOR9788956740911) [상세보기](http://book.daum.net/bookdetail/book.do?bookid=KOR9788956740911)<div id="p_author_area" style="MARGIN-BOTTOM: 8px"><span id="p_author">아담 프리맨 외</span> 지음 | <span id="p_publish">정보문화사</span> 펴냄 </div><div style="OVERFLOW: hidden; HEIGHT: 52px"><span id="p_description" style="MARGIN: 2px; FONT: 12px/1.5 Dotum, Sans-Serif">개발자 군에서도 초급, 중급 수준에서 xml 웹 서비스를 빠르고 쉽게 개발하는 과정을 단계별 학습 방식으로 접근하고 있다. 비즈니스에서 바로 이용할 수 있는 신용카드 번화 검증 서비스를 선정한 후, 기본 기능을 구현하는 과정부터 시작하여 고급 기능을 점차적으로 추가해 나가면서 xml 웹 서비스 개발 코드의 완성도를 높여가는 구조로 짜여 있다. 이 책은 채택한 시나리오의 일관성을 유지하면서 실제 어플리케이션 개발에 </span></div></div>

