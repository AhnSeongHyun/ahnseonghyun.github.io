---
title: '[C#] Click Once 배포오류 fileloadException에 대해서.'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['Ahn Seong Hyun', 'c#', 'Click Once', 'dev', 'fileloadexception', '배포오류', '클릭원스']
---


<div style="text-align: justify; line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; ">요즘 계속 배포작업을 하고 있습니다. 처음 배포 한 msi 파일이 배포오류가 생겼었는데, 그 오류를 자세히 들여가 보면 fileloadException 에 의해서 발생된 오류였다. 처음에는 기본적으로 ini 파일이나, 폰트파일 혹은 외부 dll 파일을 못 읽어서 문제가 생겼나 해서 예외처리를 한 상태에서 해 봤더니, 걸리지 않았다. 그래서 혹시나 해서 devpia에 찾아볼 결과 다음과 같은 결과가 나왔다. </span></span></div><div style="text-align: justify; line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; ">  
  </span></span></div><div style="line-height: 2; "></div><div style="line-height: 2; "><div class="txc-textbox" style="border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-top-color: rgb(193, 193, 193); border-right-color: rgb(193, 193, 193); border-bottom-color: rgb(193, 193, 193); border-left-color: rgb(193, 193, 193); background-color: rgb(238, 238, 238); padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; "><span style="font-size: 10pt; "><span style="font-family: Dotum; ">C++/CLI는 C#과는 달리 런타임 라이브러리를 사용하곤 합니다. (msvcm80.dll)</span></span>

<span style="font-size: 10pt; "><span style="font-family: Dotum; ">이 라이브러리는 닷넷 프레임워크와 함께 설치됩니다.</span></span>

<span style="font-size: 10pt; "><span style="font-family: Dotum; ">하지만 개발시에 Debug 빌드와 함게 사용되는 라이브러리는 Visual Studio 내에만 포함되어 있습니다.  
 (msvcm80d.dll)</span></span>

<span style="font-size: 10pt; "><span style="font-family: Dotum; ">따라서 Debug 빌드로 작성된 exe를 사용하면 이들 디버그용 라이브러리를 찾으려고 할 것이고</span></span>

<span style="font-size: 10pt; "><span style="font-family: Dotum; ">이 라이브러리는 달랑 닷넷 프레임워크만 설치된 곳에는 존재하지 않기 때문에</span></span>

<span style="font-size: 10pt; "><span style="font-family: Dotum; ">오류가 발생합니다.</span></span>

<span style="font-size: 10pt; "><span style="font-family: Dotum; "> </span></span>

**<span style="font-size: 10pt; "><span style="font-family: Dotum; ">배포에 사용하시려면 </span></span>**

**<span style="font-size: 10pt; "><span style="font-family: Dotum; ">Release 빌드를 배포하시거나 Debug용 런타임 라이브러리를 배포하셔야 합니다.</span></span>**

<span style="font-size: 10pt; "><span style="font-family: Dotum; "> </span></span>

<span style="font-size: 10pt; "><span style="font-family: Dotum; ">도움이 되셨기를…</span></span>

</div></div><div style="text-align: justify; line-height: 2; "></div><div style="text-align: justify; line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; ">즉, 원 C# 으로 만든 프로젝트에 MixString 이라는 C++ 외부 라이브러리를 붙였는데, 빌드 형태의 Debug로 해서 빌드를 한후에 Click Once 프로젝트에서 해당 .exe 파일을 대상으로 빌드를 하고, 다른 컴퓨터에서 실행 시켰을 경우, 위와 같은 이유로 에러가 난다는 것이다. </span></span></div><div style="text-align: justify; line-height: 2; "></div><div style="text-align: justify; line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; ">실제로 Release 로 빌드 형태를 바꾸어서 빌드하고, 배포프로젝트에 넣어서 빌드하니 다른 컴퓨터에서도 잘 되었다. </span></span></div><div style="text-align: justify; line-height: 2; "><span style="font-size: 10pt; ">  
</span></div><div style="text-align: justify; line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; ">[http://search.devpia.com/MAEULResult.aspx?KeyW=fileloadexception%20%uBC30%uD3EC%uC624%uB958%20&keyr=title&boardID=17&MAEULNo=8](http://search.devpia.com/MAEULResult.aspx?KeyW=fileloadexception%20%uBC30%uD3EC%uC624%uB958%20&keyr=title&boardID=17&MAEULNo=8)</span></span></div>

