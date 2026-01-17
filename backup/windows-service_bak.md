---
title: 'Windows Service'
author: 'ash84'
pub_date: '2007-10-05'
description: 'Windows Service   


  
![사용자 삽입 이미지](http://ash84.'
featured_image: ''
tags: ['c#', 'dev', 'Installtutil', 'System.ComponentModel', 'System.Configuration.Install', 'System.ServiceProcess', 'Windows Service', '서비스등록']
---


<span lang="EN-US" style="FONT-SIZE: 18pt"><font face="맑은 고딕"><font color="#000000">Windows Service   
<?xml:namespace prefix = o ns = "urn:schemas-microsoft-com:office:office" /?>
</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 18pt"><font face="맑은 고딕">  
![사용자 삽입 이미지](http://ash84.net/wp-content/uploads/1/el123.JPG) </font>

</span>

  
<font face="맑은 고딕"><span lang="EN-US" style="FONT-SIZE: 11pt">  
</span></font>

  
<div style="PADDING-RIGHT: 10px; PADDING-LEFT: 10px; PADDING-BOTTOM: 10px; PADDING-TOP: 10px; BACKGROUND-COLOR: #faffa9">  
<font face="맑은 고딕"><span>**<font color="#000000">Windows Service 란<span lang="EN-US">?</span></font>**</span></font>

  
<font face="맑은 고딕"><font color="#000000"><span lang="EN-US" style="FONT-SIZE: 11pt">– </span><span style="FONT-SIZE: 11pt">여러 응용프로그램을 백그라운드 프로세스로 운영하는 것<span lang="EN-US"></span></span></font></font>

  
<font face="맑은 고딕"><font color="#000000"><span lang="EN-US" style="FONT-SIZE: 11pt">– exe, dll</span><span style="FONT-SIZE: 11pt">이 아니라<span lang="EN-US"> os</span>가 내부적으로 실행<span lang="EN-US"></span></span></font></font>

  
<font face="맑은 고딕"><font color="#000000"><span lang="EN-US" style="FONT-SIZE: 11pt">– </span><span style="FONT-SIZE: 11pt">구성요소의 서비스 목록에 나열되어 있음<span lang="EN-US"></span></span></font></font>

</div>  
<span lang="EN-US" style="FONT-SIZE: 11pt"><font color="#000000" face="맑은 고딕"> </font>

</span>

  
<font face="맑은 고딕"><font color="#000000">**<span lang="EN-US" style="FONT-SIZE: 11pt">Windows Service </span>****<span style="FONT-SIZE: 11pt">응용프로그램 개발<span lang="EN-US"></span></span>**</font></font>

  
<span lang="EN-US" style="FONT-SIZE: 11pt"><font color="#000000" face="맑은 고딕"> </font>

</span>

  
<font face="맑은 고딕"><font color="#000000"><span lang="EN-US" style="FONT-SIZE: 11pt">– Main( ), OnStart( ), OnStop( ) </span><span style="FONT-SIZE: 11pt">이 필요 <span lang="EN-US"></span></span></font></font>

  
<font face="맑은 고딕"><span lang="EN-US" style="FONT-SIZE: 11pt"><font color="#000000">– </font></span><span style="FONT-SIZE: 11pt"><font color="#000000">참조추가</font><span lang="EN-US"><font color="#000000"> :</font>**<font color="#d41a01">System.Service Process</font>**</span></span></font>

  
**<span lang="EN-US" style="FONT-SIZE: 11pt"><font face="맑은 고딕"> </font>

</span>**

  
**<span lang="EN-US" style="FONT-SIZE: 11pt"><font face="맑은 고딕"> </font>

</span>**

  
<font color="#000000">**<span lang="EN-US" style="FONT-SIZE: 11pt; mso-fareast-font-family: '맑은 고딕'; mso-fareast-theme-font: minor-latin; mso-bidi-font-family: '맑은 고딕'; mso-bidi-theme-font: minor-latin"><span style="mso-list: Ignore"><font face="맑은 고딕">1.</font><span style="FONT: 7pt 'Times New Roman'">    </span></span></span>**<font face="맑은 고딕">**<span lang="EN-US" style="FONT-SIZE: 11pt">Service </span>****<span style="FONT-SIZE: 11pt">파일<span lang="EN-US"> : </span>서비스 동작을 하는 파일<span lang="EN-US">, ServiceBase </span>클래스를 확장한다<span lang="EN-US">. </span></span>**</font></font>

  
<span lang="EN-US" style="FONT-SIZE: 11pt"><font color="#000000" face="맑은 고딕"> </font>

</span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000">public static void Main()</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">        </span>{</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">            </span>System.ServiceProcess.ServiceBase[] ServiceToRun;</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">            </span>ServiceToRun = new ServiceBase[] { new Service() };</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">            </span>System.ServiceProcess.ServiceBase.Run(ServiceToRun);</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">        </span>}</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 11pt"><font color="#000000" face="맑은 고딕"> </font>

</span>

  
<font face="맑은 고딕"><font color="#000000"><span lang="EN-US" style="FONT-SIZE: 11pt">ServiceBase class</span><span style="FONT-SIZE: 11pt">의 배열 인스턴스를 생성해서 현재 서비스 클래스를 추가한다<span lang="EN-US">. </span></span></font></font>

  
<font face="맑은 고딕"><font color="#000000"><span lang="EN-US" style="FONT-SIZE: 11pt">(</span><span style="FONT-SIZE: 11pt">현재<span lang="EN-US"> ServiceBase class</span>를 확장한 클래스를 추가하는 것<span lang="EN-US">)</span></span></font></font>

  
<span lang="EN-US" style="FONT-SIZE: 11pt"><font color="#000000" face="맑은 고딕"> </font>

</span>

  
<font color="#000000">**<span lang="EN-US" style="FONT-SIZE: 11pt; mso-fareast-font-family: '맑은 고딕'; mso-fareast-theme-font: minor-latin; mso-bidi-font-family: '맑은 고딕'; mso-bidi-theme-font: minor-latin"><span style="mso-list: Ignore"><font face="맑은 고딕">2.</font><span style="FONT: 7pt 'Times New Roman'">    </span></span></span>**<font face="맑은 고딕">**<span lang="EN-US" style="FONT-SIZE: 11pt">Override Member </span>****<span style="FONT-SIZE: 11pt">추가<span lang="EN-US"></span></span>**</font></font>

  
<span lang="EN-US" style="FONT-SIZE: 11pt"><font color="#000000" face="맑은 고딕"> </font>

</span>

  
<font face="맑은 고딕"><font color="#000000"><span lang="EN-US" style="FONT-SIZE: 11pt">Protected</span><span style="FONT-SIZE: 11pt">형 멤버를 추가<span lang="EN-US"></span></span></font></font>

  
<?xml:namespace prefix = v ns = "urn:schemas-microsoft-com:vml" /?>
<shapetype adj="1800" coordsize="21600,21600" filled="f" id="_x0000_t86" o:spt="86" path="m,qx21600@0l21600@1qy,21600e"><formulas><f eqn="val #0"></f><f eqn="sum 21600 0 #0"></f><f eqn="prod #0 9598 32768"></f><f eqn="sum 21600 0 @2"></f></formulas><path arrowok="t" gradientshapeok="t" o:connectlocs="0,0;0,21600;21600,10800" o:connecttype="custom" textboxrect="0,@2,15274,@3"></path><handles><h position="bottomRight,#0" yrange="0,10800"></h></handles></shapetype><shape id="_x0000_s1026" style="MARGIN-TOP: 5.65pt; Z-INDEX: 1; LEFT: 0px; MARGIN-LEFT: 245.25pt; WIDTH: 12pt; POSITION: absolute; HEIGHT: 25.5pt; TEXT-ALIGN: left" type="#_x0000_t86"><textbox>  
<table cellpadding="0" cellspacing="0" width="100%">  
<tbody>  
<tr>  
<td style="BORDER-LEFT-COLOR: #f4f4f4; BORDER-BOTTOM-COLOR: #f4f4f4; BORDER-TOP-COLOR: #f4f4f4; BACKGROUND-COLOR: transparent; BORDER-RIGHT-COLOR: #f4f4f4">  
<div>  
<span lang="EN-US" style="mso-no-proof: yes"><font face="맑은 고딕"><font color="#000000"><shapetype coordsize="21600,21600" filled="f" id="_x0000_t75" o:preferrelative="t" o:spt="75" path="m@4@5l@4@11@9@11@9@5xe" stroked="f"><stroke joinstyle="miter"></stroke><formulas><f eqn="if lineDrawn pixelLineWidth 0"></f><f eqn="sum @0 1 0"></f><f eqn="sum 0 0 @1"></f><f eqn="prod @2 1 2"></f><f eqn="prod @3 21600 pixelWidth"></f><f eqn="prod @3 21600 pixelHeight"></f><f eqn="sum @0 0 1"></f><f eqn="prod @6 1 2"></f><f eqn="prod @7 21600 pixelWidth"></f><f eqn="sum @8 21600 0"></f><f eqn="prod @7 21600 pixelHeight"></f><f eqn="sum @10 21600 0"></f></formulas><path gradientshapeok="t" o:connecttype="rect" o:extrusionok="f"></path><lock aspectratio="t" v:ext="edit"></lock></shapetype><shape id="_x0000_i1026" style="VISIBILITY: visible; WIDTH: 12.75pt; HEIGHT: 26.25pt; mso-wrap-style: square" type="#_x0000_t75"><imagedata o:title="" src="file:///C:\DOCUME~1\ADMINI~1\LOCALS~1\Temp\msohtmlclip1\01\clip_image001.emz"></imagedata></shape></font></font></span>

</div></td></tr></tbody></table></textbox></shape><shapetype coordsize="21600,21600" id="_x0000_t202" o:spt="202" path="m,l,21600r21600,l21600,xe"><stroke joinstyle="miter"></stroke><path gradientshapeok="t" o:connecttype="rect"></path></shapetype><shape id="_x0000_s1027" style="MARGIN-TOP: 8.05pt; Z-INDEX: 2; LEFT: 0px; MARGIN-LEFT: 271.55pt; WIDTH: 229.5pt; POSITION: absolute; HEIGHT: 22.65pt; TEXT-ALIGN: left; mso-width-percent: 400; mso-width-relative: margin; mso-height-relative: margin" type="#_x0000_t202"></shape><span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000">– protected override void OnStart(string[] args)</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000">– protected override void OnStop()  
</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font color="#000000" face="맑은 고딕">   < 기본적으로 사용가능>  
 </font>

</span>

  
<shape id="_x0000_s1028" style="MARGIN-TOP: 4.7pt; Z-INDEX: 3; LEFT: 0px; MARGIN-LEFT: 245.25pt; WIDTH: 12pt; POSITION: absolute; HEIGHT: 25.5pt; TEXT-ALIGN: left" type="#_x0000_t86"><textbox>  
<table cellpadding="0" cellspacing="0" width="100%">  
<tbody>  
<tr>  
<td style="BORDER-LEFT-COLOR: #f4f4f4; BORDER-BOTTOM-COLOR: #f4f4f4; BORDER-TOP-COLOR: #f4f4f4; BACKGROUND-COLOR: transparent; BORDER-RIGHT-COLOR: #f4f4f4">  
<div>  
<span lang="EN-US" style="mso-no-proof: yes"><shape id="그림_x0020_1" o:spid="_x0000_i1025" style="VISIBILITY: visible; WIDTH: 12.75pt; HEIGHT: 26.25pt; mso-wrap-style: square" type="#_x0000_t75"><imagedata o:title="" src="file:///C:\DOCUME~1\ADMINI~1\LOCALS~1\Temp\msohtmlclip1\01\clip_image001.emz"></imagedata></shape></span>

</div></td></tr></tbody></table></textbox></shape><shape id="_x0000_s1029" style="MARGIN-TOP: 7.55pt; Z-INDEX: 4; LEFT: 0px; MARGIN-LEFT: 272pt; WIDTH: 229.6pt; POSITION: absolute; HEIGHT: 22.65pt; TEXT-ALIGN: left; mso-width-percent: 400; mso-width-relative: margin; mso-height-relative: margin" type="#_x0000_t202"></shape><span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000">– protected override void OnPause()</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000">– protected override void OnContinue()</font></font></span>

  
<font size="2"><font face="맑은 고딕"><font color="#000000"><span lang="EN-US">                <CanPauseandContinue </span>속성<span lang="EN-US">(True)></span></font></font></font>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font color="#000000" face="맑은 고딕"> </font>

</span>

  
<span lang="EN-US" style="FONT-SIZE: 11pt"><font face="맑은 고딕"><font color="#000000"> </font><span style="Z-INDEX: 4; LEFT: 0pt; POSITION: absolute; mso-ignore: vglayout"><font color="#000000"></font>  
<table cellpadding="0" cellspacing="0" width="100%">  
<tbody>  
<tr>  
<td style="BORDER-LEFT-COLOR: #f4f4f4; BORDER-BOTTOM-COLOR: #f4f4f4; BORDER-TOP-COLOR: #f4f4f4; BACKGROUND-COLOR: transparent; BORDER-RIGHT-COLOR: #f4f4f4">  
<div class="shape" style="PADDING-RIGHT: 7.95pt; PADDING-LEFT: 7.95pt; PADDING-BOTTOM: 4.35pt; PADDING-TOP: 4.35pt" v:shape="_x0000_s1029">  
<font size="2"></font> 

</div></td></tr></tbody></table></span></font>

</span>

  
<span lang="EN-US" style="FONT-SIZE: 11pt"><font color="#000000" face="맑은 고딕"> </font>

</span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font color="#000000" face="맑은 고딕"> </font>

</span>

  
**<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">        </span>protected override void OnStop()</font></font></span>**

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">        </span>{</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">            </span>FileStream fs = new FileStream(@”c:\log_stop.txt”, FileMode.OpenOrCreate, FileAccess.Write);</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">            </span>StreamWriter sr = new StreamWriter(fs);</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">            </span>sr.WriteLine(“MYWindowsService stopped”);</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">            </span>sr.Flush();</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">            </span>sr.Close();</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">        </span>}</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font color="#000000" face="맑은 고딕"> </font>

</span>

  
**<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">        </span>protected override void OnPause()</font></font></span>**

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">        </span>{</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">            </span>FileStream fs = new FileStream(@”c:\log_stop.txt”, FileMode.OpenOrCreate, FileAccess.Write);</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">            </span>StreamWriter sr = new StreamWriter(fs);</font></font></span>

  
<font face="맑은 고딕"><font color="#000000"><span lang="EN-US" style="FONT-SIZE: 9pt"><span style="mso-spacerun: yes">            </span>sr.WriteLine(“</span><span style="FONT-SIZE: 9pt">잠시중지<span lang="EN-US">“);</span></span></font></font>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">            </span>sr.Flush();</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">            </span>sr.Close();</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">        </span>}</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font color="#000000" face="맑은 고딕"> </font>

</span>

  
<span lang="EN-US" style="FONT-SIZE: 11pt"><font color="#000000" face="맑은 고딕"> </font>

</span>

<font size="2"><font face="맑은 고딕"><span lang="EN-US" style="mso-bidi-font-size: 10.0pt">  
<div style="PADDING-RIGHT: 10px; PADDING-LEFT: 10px; PADDING-BOTTOM: 10px; PADDING-TOP: 10px; BACKGROUND-COLOR: #ffdaed">  
<font size="2"><font face="맑은 고딕"><span>**<font color="#000000">* Windows Service Event – 서비스의 상태에 따라 달라진다<span lang="EN-US">. </span></font>**</span></font></font>

  
<span lang="EN-US" style="FONT-SIZE: 11pt"><font color="#000000" face="맑은 고딕">** **</font>

</span>

  
<font size="2"><font face="맑은 고딕"><font color="#000000"><span lang="EN-US" style="mso-bidi-font-size: 10.0pt">Start : OnStart( ), ServiceStarmode(Automatic, manual, Disabled) : </span><span style="mso-bidi-font-size: 10.0pt">어떤식으로 시작하는지<span lang="EN-US"></span></span></font></font></font>

  
<span lang="EN-US" style="mso-bidi-font-size: 10.0pt"><font size="2"><font face="맑은 고딕"><font color="#000000">Stop : OnStop( )</font></font></font></span>

  
<font size="2"><font face="맑은 고딕"><font color="#000000"><span lang="EN-US" style="mso-bidi-font-size: 10.0pt">Pause : OnPause( ) , </span><span style="mso-bidi-font-size: 10.0pt">시스템의 리소스를 따로 보유할 수 있다<span lang="EN-US">. </span></span></font></font></font>

  
<font size="2"><font face="맑은 고딕"><font color="#000000"><span lang="EN-US" style="mso-bidi-font-size: 10.0pt">Continue : OnContinue( ), OnPause</span><span style="mso-bidi-font-size: 10.0pt">와의 반대 기능을 실행할수 있다<span lang="EN-US">. </span></span></font></font></font>

</div></span></font></font>  
<span lang="EN-US" style="FONT-SIZE: 11pt"><font color="#000000" face="맑은 고딕"> </font>

</span>

  
<font color="#000000">**<span lang="EN-US" style="FONT-SIZE: 11pt; mso-fareast-font-family: '맑은 고딕'; mso-fareast-theme-font: minor-latin; mso-bidi-font-family: '맑은 고딕'; mso-bidi-theme-font: minor-latin"><span style="mso-list: Ignore"><font face="맑은 고딕">3.</font><span style="FONT: 7pt 'Times New Roman'">    </span></span></span>**<font face="맑은 고딕">**<span lang="EN-US" style="FONT-SIZE: 11pt">ServiceInstaller, ServiceProcessInstaller </span>****<span style="FONT-SIZE: 11pt">세팅<span lang="EN-US"></span></span>**</font></font>

  
<font face="맑은 고딕"><font color="#000000"><span lang="EN-US" style="FONT-SIZE: 11pt">– Service</span><span style="FONT-SIZE: 11pt">를 수행하는 클래스 외에 <span lang="EN-US">Installer </span>기능을 하는 하나의 클래스를 별로도 <span lang="EN-US"></span></span></font></font>

  
<span style="FONT-SIZE: 11pt"><font face="맑은 고딕"><font color="#000000">추가한다<span lang="EN-US">. </span></font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 11pt"><font color="#000000" face="맑은 고딕"> </font>

</span>

  
**<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000">using System.ComponentModel;</font></font></span>**

  
**<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000">using System.ServiceProcess;</font></font></span>**

  
**<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000">using System.Configuration.Install;</font></font></span>**

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font color="#000000" face="맑은 고딕"> </font>

</span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font color="#000000" face="맑은 고딕"> </font>

</span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000">namespace MyWindowsService</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000">{</font></font></span>

  
**<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes"> </span><span style="mso-spacerun: yes">  </span><u>[RunInstallerAttribute(true)]</u></font></font></span>**

  
<font color="#000000">**<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><span style="mso-spacerun: yes">    </span>//</font></span>**<span lang="EN-US" style="FONT-SIZE: 8.5pt; COLOR: black; FONT-FAMILY: 'Verdana','sans-serif'; mso-fareast-font-family: 굴림; mso-bidi-font-family: 굴림; mso-font-kerning: 0pt"></span>**<span style="FONT-SIZE: 9pt"><font face="맑은 고딕">어셈블리가 설치될 때<span lang="EN-US"> Visual Studio </span>사용자 지정 동작 설치 관리자 <span style="COLOR: black; mso-themecolor: text1">또는 <span lang="EN-US">[<span lang="EN-US" style="COLOR: black; mso-themecolor: text1"><span lang="EN-US">설치</span></span><span lang="EN-US" style="COLOR: black; mso-themecolor: text1"><span lang="EN-US"></span></span><span lang="EN-US" style="COLOR: black; mso-themecolor: text1"><span lang="EN-US">관리자</span></span><span lang="EN-US" style="COLOR: black; mso-themecolor: text1"><span lang="EN-US"></span></span><span lang="EN-US" style="COLOR: black; mso-themecolor: text1"><span lang="EN-US">도</span></span><span lang="EN-US" style="COLOR: black; mso-themecolor: text1"><span lang="EN-US">구(Installutil.exe)</span></span>](http://msdn2.microsoft.com/ko-kr/library/50614e95(VS.80).aspx)</span>의 호출 여부를 지정합니다<span lang="EN-US">.</span></span></font></span>**</font>

  
**<span lang="EN-US" style="FONT-SIZE: 9pt; COLOR: black; mso-themecolor: text1"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes"> </span></font></font></span>**

  
**<span lang="EN-US" style="FONT-SIZE: 9pt"><font color="#000000" face="맑은 고딕"> </font>

</span>**

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">    </span>public class ServiceInstallers **: Installer**</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">    </span>{</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font color="#000000" face="맑은 고딕"> </font>

</span>

  
**<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">        </span>private ServiceInstaller serviceInstaller;</font></font></span>**

  
<font face="맑은 고딕"><font color="#000000">**<span lang="EN-US" style="FONT-SIZE: 9pt"><span style="mso-spacerun: yes">        </span>// </span>****<span style="FONT-SIZE: 9pt">서비스응용프로그램을설치하는인스톨러<span lang="EN-US"></span></span>**</font></font>

  
**<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">        </span>private ServiceProcessInstaller serviceProcessInstaller;</font></font></span>**

  
<font face="맑은 고딕"><font color="#000000">**<span lang="EN-US" style="FONT-SIZE: 9pt"><span style="mso-spacerun: yes">        </span>// </span>****<span style="FONT-SIZE: 9pt">서비스를운용하는프로세스를등록하는인스톨러<span lang="EN-US"></span></span>**</font></font>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">       </span></font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font color="#000000" face="맑은 고딕"> </font>

</span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">        </span>public ServiceInstallers()</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">        </span>{</font></font></span>

  
<font face="맑은 고딕"><font color="#000000"><span lang="EN-US" style="FONT-SIZE: 9pt"><span style="mso-spacerun: yes">            </span>//</span><span style="FONT-SIZE: 9pt">생성자<span lang="EN-US"></span></span></font></font>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">            </span>this.serviceProcessInstaller = new ServiceProcessInstaller();</font></font></span>

  
**<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">            </span>this.serviceProcessInstaller.Account = ServiceAccount.LocalSystem;</font></font></span>**

  
**<span lang="EN-US" style="FONT-SIZE: 9pt"><font color="#000000" face="맑은 고딕"> </font>

</span>**

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font color="#000000" face="맑은 고딕"> </font>

</span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font color="#000000" face="맑은 고딕"> </font>

</span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">            </span>//this.serviceProcessInstaller.Account = ServiceAccount.User;</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">            </span>//this.serviceProcessInstaller.Username = “Administrator”;</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">            </span>//this.serviceProcessInstaller.Password = “6750”;</font></font></span>

  
<font face="맑은 고딕"><font color="#000000"><span lang="EN-US" style="FONT-SIZE: 9pt"><span style="mso-spacerun: yes">            </span>// </span><span style="FONT-SIZE: 9pt">계정과패스워드를정확히입력해야한다<span lang="EN-US">. </span></span></font></font>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font color="#000000" face="맑은 고딕"> </font>

</span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">            </span>this.serviceInstaller = new ServiceInstaller();</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">            </span>**this.serviceInstaller.ServiceName = “Service”;**</font></font></span>

  
<font face="맑은 고딕"><font color="#000000">**<span lang="EN-US" style="FONT-SIZE: 9pt"><span style="mso-spacerun: yes">            </span>// </span>****<span style="FONT-SIZE: 9pt">시스템에서서비스이름으로식별한다<span lang="EN-US">. </span></span>**</font></font>

  
<font face="맑은 고딕"><font color="#000000">**<span lang="EN-US" style="FONT-SIZE: 9pt"><span style="mso-spacerun: yes">            </span>// </span>****<span style="FONT-SIZE: 9pt">서비스이름은<span lang="EN-US">ServiceBase </span>를확장한클래스명이다<span lang="EN-US">. </span></span>**</font></font>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font color="#000000" face="맑은 고딕"> </font>

</span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">            </span>**Installers.Add(serviceInstaller);**</font></font></span>

  
**<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">            </span>Installers.Add(serviceProcessInstaller);</font></font></span>**

  
**<span lang="EN-US" style="FONT-SIZE: 9pt"><font color="#000000" face="맑은 고딕"> </font>

</span>**

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">        </span>}</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="mso-spacerun: yes">    </span>}</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000">}</font></font></span>

  
<span lang="EN-US" style="FONT-SIZE: 9pt"><font color="#000000" face="맑은 고딕"> </font>

</span>

  
**<span lang="EN-US" style="FONT-SIZE: 11pt; mso-fareast-font-family: '맑은 고딕'; mso-fareast-theme-font: minor-latin; mso-bidi-font-family: '맑은 고딕'; mso-bidi-theme-font: minor-latin"><span style="mso-list: Ignore"><font color="#000000"><font face="맑은 고딕">4.</font><span style="FONT: 7pt 'Times New Roman'">    </span></font></span></span>**<font face="맑은 고딕">**<span lang="EN-US" style="FONT-SIZE: 11pt"><font color="#000000">cmd</font></span>****<span style="FONT-SIZE: 11pt"><font color="#000000">에서<span lang="EN-US"> Installtutil</span>을 이용해서 윈도우 서비스 등록   
<span lang="EN-US"></span></font></span>**</font>

  
<span lang="EN-US" style="FONT-SIZE: 11pt; mso-bidi-font-weight: bold"><font face="맑은 고딕">  
<font color="#000000"> ![사용자 삽입 이미지](http://ash84.net/wp-content/uploads/1/gl123.JPG)</font></font>

</span>

  
<font face="맑은 고딕"><font color="#000000"><span lang="EN-US" style="FONT-SIZE: 11pt; mso-bidi-font-weight: bold">Installutill <span style="mso-spacerun: yes">  </span>/i<span style="mso-spacerun: yes">  </span>MyWindowsService.exe : </span><span style="FONT-SIZE: 11pt; mso-bidi-font-weight: bold">서비스 등록<span lang="EN-US"></span></span></font></font>

  
<font face="맑은 고딕"><font color="#000000"><span lang="EN-US" style="FONT-SIZE: 11pt; mso-bidi-font-weight: bold">Installutill <span style="mso-spacerun: yes">  </span>/u<span style="mso-spacerun: yes">  </span>MyWindowsService.exe : </span><span style="FONT-SIZE: 11pt; mso-bidi-font-weight: bold">서비스 해제 <span lang="EN-US"></span></span></font></font>



