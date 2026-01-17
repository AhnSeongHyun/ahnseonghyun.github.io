---
title: '[C#] DLL 등록하기 regsvr32.exe'
author: 'ash84'
pub_date: '2012-07-28'
description: ''
featured_image: ''
tags: ['MSDN', 'c# DLL 등록', 'dev', 'dll 등록', 'regsvr32.exe', 'tutorial']
---
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>

C# 코딩을 할때 VS2010 에서 주로 작업을 하게 되는데 작업을 하다보면 DLL을 참조추가 해서 넣게 된다. 그런데서버에서 돌리거나, 배포시에는 해당 DLL들을 레지스트리에 등록해 주어야 한다. 그때 쓰는 명령어가 regsvr32.exe 이다.

다음은 위키피디아에 쓰여있는 regsvr32 에 대한 내용이다. 

```
In computing, regsvr32 (Microsoft Register Server) is a command-line utility in Microsoft Windows operating systems for registering and unregistering DLLs and ActiveX controls in the Windows Registry.[1]
To be used with regsvr32, a DLL must export the functions DllRegisterServer and DllUnregisterServer.[2]
regsvr32 in Windows is comparable to ldconfig in Linux.
```

사용법은 간단하다.  

등록하려면, 다음과 같이 사용하면 된다. 

```
regsvr32 파일이름.dll (dll 등록)

regsvr32 파일이름.dll /u (dll 삭제)
```
 

이미 등록이 되어 있다고 하더라도, 등록시 다시 등록되는 방식이다. 즉, 등록되어 있다고 하더라도 등록명령 실행시, 이미 등록되어 있다고는 알려주지 않는다.

추가적으로, 64bit 에서 Dll 등록시 문제가 생길수 있는데, 그 부분에 대해서는 msdn 링크에서 가이드를 해주고 있다. http://support.microsoft.com/kb/282747/ko
 

