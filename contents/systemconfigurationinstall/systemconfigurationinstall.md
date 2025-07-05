---
title: 'System.Configuration.Install'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['dev', 'Installer Class', 'System.Configuration.Install']
---


**<span style="FONT-SIZE: 9pt"><font color="#000000" face="맑은 고딕"><span style="font-size: 11pt;"></span></font></span>****<span style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="font-size: 11pt;">System.Configuration.Install ?</span></font></font></span>**

<span style="font-size: 11pt;">  
</span>

**<span style="FONT-SIZE: 9pt"><font color="#000000" face="맑은 고딕"><span style="font-size: 11pt;"> </span></font></span>**

<span style="font-size: 11pt;">  
</span>

<font face="맑은 고딕"><font color="#000000"><span style="font-size: 11pt; color: black;">– </span><span style="FONT-SIZE: 9pt; COLOR: black; mso-themecolor: text1"><span style="font-size: 11pt;">사용자 자신의 구성 요소에 대한 사용자 지정 설치 관리자를 쓸 수 있게 해주는 클래스를 제공합니다</span><span style="font-size: 11pt;">. </span></span><span>[<span style="font-size: 11pt; color: black;">Installer</span>](http://msdn2.microsoft.com/ko-kr/library/system.configuration.install.installer(VS.80).aspx)</span><span style="font-size: 11pt; color: black;"></span><span style="FONT-SIZE: 9pt; COLOR: black; mso-themecolor: text1"><span style="font-size: 11pt;">클래스는</span><span style="font-size: 11pt;"> .NET Framework</span><span style="font-size: 11pt;">의 모든 사용자 지정 설치 관리자에 대한 기본 클래스입니다</span><span style="font-size: 11pt;">. </span></span><span>[<span style="font-size: 11pt; color: black;">Installer.Installers</span>](http://msdn2.microsoft.com/ko-kr/library/system.configuration.install.installer.installers(VS.80).aspx)</span><span style="font-size: 11pt; color: black;"></span><span style="FONT-SIZE: 9pt; COLOR: black; mso-themecolor: text1"><span style="font-size: 11pt;">속성의 경우 설치 관리자에는 다른 설치 관리자의 컬렉션이 자식으로 포함되어 있습니다</span><span style="font-size: 11pt;">. </span><span style="font-size: 11pt;">설치 관리자가 실행될 때</span><span style="font-size: 11pt;">, </span><span style="font-size: 11pt;">설치 관리자는 해당 자식을 순환하고</span><span style="font-size: 11pt;"> System.Configuration.Install.Installer.Install, System.Configuration.Install.Installer.Commit, System.Configuration.Install.Installer.Rollback </span><span style="font-size: 11pt;">또는</span><span style="font-size: 11pt;"> System.Configuration.Install.Installer.Uninstall</span><span style="font-size: 11pt;">를 호출합니다</span><span style="font-size: 11pt;">.</span></span></font></font>

<span style="font-size: 11pt;">  
</span>

<font face="맑은 고딕"><font color="#000000">**<span style="font-size: 11pt;">└</span>****<span style="font-size: 11pt;"> Installer Class </span>**</font></font>

<span style="font-size: 11pt;">  
</span>

**<span style="FONT-SIZE: 9pt"><font color="#000000" face="맑은 고딕"><span style="font-size: 11pt;"> </span></font></span>**

<span style="font-size: 11pt;">  
</span>

<font color="#000000">**<span style="FONT-SIZE: 9pt"><font face="Times New Roman"><span style="font-size: 11pt;">– </span></font></span>**<span style="font-size: 11pt; color: black; font-family: 굴림;">사용자</span><span style="font-size: 11pt; color: black; font-family: Verdana, sans-serif;"></span><span style="font-size: 11pt; color: black; font-family: 굴림;">지정</span><span style="font-size: 11pt; color: black; font-family: Verdana, sans-serif;"></span><span style="font-size: 11pt; color: black; font-family: 굴림;">설치의</span><span style="font-size: 11pt; color: black; font-family: Verdana, sans-serif;"></span><span style="font-size: 11pt; color: black; font-family: 굴림;">기반을</span><span style="font-size: 11pt; color: black; font-family: Verdana, sans-serif;"></span><span style="font-size: 11pt; color: black; font-family: 굴림;">제공합니다</span><span style="FONT-SIZE: 8.5pt; COLOR: black; FONT-FAMILY: 'Verdana','sans-serif'; mso-fareast-font-family: 굴림; mso-bidi-font-family: 굴림; mso-font-kerning: 0pt"><span style="font-size: 11pt;">. </span></span></font>

<span style="font-size: 11pt;">     </span><font face="맑은 고딕"><font color="#000000">**<span style="font-size: 11pt; color: black;">Installer</span>****<span style="FONT-SIZE: 9pt; COLOR: black; mso-themecolor: text1"><span style="font-size: 11pt;">를 사용하려면 다음 단계를 수행해야 합니다</span><span style="font-size: 11pt;">. </span></span>**</font></font>

<span style="font-size: 11pt;">  
</span>

- <font face="맑은 고딕"><font color="#000000">**<span style="font-size: 11pt;">Installer</span>****<span style="font-size: 11pt;"></span>****<span style="FONT-SIZE: 9pt"><span style="font-size: 11pt;">클래스를 상속합니다</span><span style="font-size: 11pt;">.</span></span>**</font></font>
- <span style="COLOR: windowtext">[**<span style="FONT-SIZE: 9pt; COLOR: black; mso-themecolor: text1"><font color="#000000" face="맑은 고딕"><span style="font-size: 11pt;">Install</span></font></span>**](http://msdn2.microsoft.com/ko-kr/library/system.configuration.install.installer.install(VS.80).aspx)</span><font face="맑은 고딕"><font color="#000000">**<span style="font-size: 11pt;">, </span>**<span style="COLOR: windowtext">[**<span style="font-size: 11pt; color: black;">Commit</span>**](http://msdn2.microsoft.com/ko-kr/library/system.configuration.install.installer.commit(VS.80).aspx)</span>**<span style="font-size: 11pt;">, </span>**<span style="COLOR: windowtext">[**<span style="font-size: 11pt; color: black;">Rollback</span>**](http://msdn2.microsoft.com/ko-kr/library/system.configuration.install.installer.rollback(VS.80).aspx)</span>**<span style="font-size: 11pt;"></span>****<span style="font-size: 11pt;">및 </span>**<span style="COLOR: windowtext">[**<span style="font-size: 11pt; color: black;">Uninstall</span>**](http://msdn2.microsoft.com/ko-kr/library/system.configuration.install.installer.uninstall(VS.80).aspx)</span>**<span style="font-size: 11pt;"></span>****<span style="FONT-SIZE: 9pt"><span style="font-size: 11pt;">메서드를 재정의합니다</span><span style="font-size: 11pt;">.</span></span>**</font></font>
- <span style="COLOR: windowtext">[**<span style="FONT-SIZE: 9pt; COLOR: black; mso-themecolor: text1"><font color="#000000" face="맑은 고딕"><span style="font-size: 11pt;">RunInstallerAttribute</span></font></span>**](http://msdn2.microsoft.com/ko-kr/library/system.componentmodel.runinstallerattribute(VS.80).aspx)</span>**<span style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="font-size: 11pt;">를 파생 클래스에 추가한 다음 </span><span style="font-size: 11pt;">true</span><span style="font-size: 11pt;">로 설정합니다</span><span style="font-size: 11pt;">.</span></font></font></span>**
- **<span style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="font-size: 11pt;">설치할 응용 프로그램의 어셈블리에 파생 클래스를 배치합니다</span><span style="font-size: 11pt;">.</span></font></font></span>**
- **<span style="FONT-SIZE: 9pt"><font face="맑은 고딕"><font color="#000000"><span style="font-size: 11pt;">설치 관리자를 호출합니다</span><span style="font-size: 11pt;">. </span><span style="font-size: 11pt;">예를 들어</span><span style="font-size: 11pt;">, InstallUtil.exe</span><span style="font-size: 11pt;">를 사용하여 설치 관리자를 호출합니다</span><span style="font-size: 11pt;">.</span></font></font></span>**

<span style="font-size: 11pt;">  
</span>

**<span style="FONT-SIZE: 9pt; COLOR: black; mso-themecolor: text1"><font color="#000000" face="맑은 고딕"><span style="font-size: 11pt;"> </span></font></span>**



