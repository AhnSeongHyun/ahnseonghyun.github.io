---
title: 'Windows Service'
author: 'ash84'
pub_date: '2007-10-05'
description: 'Windows Service   


  
![사용자 삽입 이미지](http://ash84.'
featured_image: ''
tags: ['c#', 'dev', 'Installtutil', 'System.ComponentModel', 'System.Configuration.Install', 'System.ServiceProcess', 'Windows Service', '서비스등록']
---

Windows Service  \!\[사용자 삽입 이미지\]\(http://ash84.net/wp-content/uploads/1/el123.JPG\) 

\*\*Windows Service 란?\*\* – 여러 응용프로그램을 백그라운드 프로세스로 운영하는 것 – exe, dll이 아니라 os가 내부적으로 실행 – 구성요소의 서비스 목록에 나열되어 있음

\*\*Windows Service \*\*\*\*응용프로그램 개발\*\* – Main\( \), OnStart\( \), OnStop\( \) 이 필요  – 참조추가 :\*\*System.Service Process\*\* \*\* \*\* \*\* \*\* \*\*1. \*\*\*\*Service \*\*\*\*파일 : 서비스 동작을 하는 파일, ServiceBase 클래스를 확장한다. \*\* public static void Main\(\) \{ System.ServiceProcess.ServiceBase\[\] ServiceToRun; ServiceToRun = new ServiceBase\[\] \{ new Service\(\) \}; System.ServiceProcess.ServiceBase.Run\(ServiceToRun\); \} ServiceBase class의 배열 인스턴스를 생성해서 현재 서비스 클래스를 추가한다.  \(현재 ServiceBase class를 확장한 클래스를 추가하는 것\) \*\*2. \*\*\*\*Override Member \*\*\*\*추가\*\* Protected형 멤버를 추가  
---  
– protected override void OnStart\(string\[\] args\) – protected override void OnStop\(\)  < 기본적으로 사용가능>   
---  
– protected override void OnPause\(\) – protected override void OnContinue\(\) 속성\(True\)>  
---  
\*\* protected override void OnStop\(\)\*\*  \{ FileStream fs = new FileStream\(@”c:\log\_stop.txt”, FileMode.OpenOrCreate, FileAccess.Write\); StreamWriter sr = new StreamWriter\(fs\); sr.WriteLine\(“MYWindowsService stopped”\); sr.Flush\(\); sr.Close\(\); \} \*\* protected override void OnPause\(\)\*\*  \{ FileStream fs = new FileStream\(@”c:\log\_stop.txt”, FileMode.OpenOrCreate, FileAccess.Write\); StreamWriter sr = new StreamWriter\(fs\); sr.WriteLine\(“잠시중지“\); sr.Flush\(\); sr.Close\(\); \}

\*\*\* Windows Service Event – 서비스의 상태에 따라 달라진다. \*\* \*\* \*\* Start : OnStart\( \), ServiceStarmode\(Automatic, manual, Disabled\) : 어떤식으로 시작하는지 Stop : OnStop\( \) Pause : OnPause\( \) , 시스템의 리소스를 따로 보유할 수 있다.  Continue : OnContinue\( \), OnPause와의 반대 기능을 실행할수 있다. 

\*\*3. \*\*\*\*ServiceInstaller, ServiceProcessInstaller \*\*\*\*세팅\*\* – Service를 수행하는 클래스 외에 Installer 기능을 하는 하나의 클래스를 별로도  추가한다.  \*\*using System.ComponentModel;\*\* \*\*using System.ServiceProcess;\*\* \*\*using System.Configuration.Install;\*\*  namespace MyWindowsService \{ \*\* _\[RunInstallerAttribute\(true\)\]_ \*\* \*\* //\*\*\*\*어셈블리가 설치될 때 Visual Studio 사용자 지정 동작 설치 관리자 또는 \[설치관리자도구\(Installutil.exe\)\]\(http://msdn2.microsoft.com/ko-kr/library/50614e95\(VS.80\).aspx\)의 호출 여부를 지정합니다.\*\* \*\* \*\* \*\* \*\*  public class ServiceInstallers \*\*: Installer\*\* \{ \*\* private ServiceInstaller serviceInstaller;\*\* \*\* // \*\*\*\*서비스응용프로그램을설치하는인스톨러\*\* \*\* private ServiceProcessInstaller serviceProcessInstaller;\*\* \*\* // \*\*\*\*서비스를운용하는프로세스를등록하는인스톨러\*\* public ServiceInstallers\(\) \{ //생성자 this.serviceProcessInstaller = new ServiceProcessInstaller\(\); \*\* this.serviceProcessInstaller.Account = ServiceAccount.LocalSystem;\*\* \*\* \*\*  //this.serviceProcessInstaller.Account = ServiceAccount.User; //this.serviceProcessInstaller.Username = “Administrator”; //this.serviceProcessInstaller.Password = “6750”; // 계정과패스워드를정확히입력해야한다.  this.serviceInstaller = new ServiceInstaller\(\); \*\*this.serviceInstaller.ServiceName = “Service”;\*\* \*\* // \*\*\*\*시스템에서서비스이름으로식별한다. \*\* \*\* // \*\*\*\*서비스이름은ServiceBase 를확장한클래스명이다. \*\* \*\*Installers.Add\(serviceInstaller\);\*\* \*\* Installers.Add\(serviceProcessInstaller\);\*\* \*\* \*\*  \} \} \} \*\*4. \*\*\*\*cmd\*\*\*\*에서 Installtutil을 이용해서 윈도우 서비스 등록 \*\* \!\[사용자 삽입 이미지\]\(http://ash84.net/wp-content/uploads/1/gl123.JPG\) Installutill  /i MyWindowsService.exe : 서비스 등록 Installutill  /u MyWindowsService.exe : 서비스 해제