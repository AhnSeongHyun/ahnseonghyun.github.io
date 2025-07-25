---
title: '[C#] .NET 어셈블리1'
author: 'ash84'
pub_date: '2007-08-13'
description: 'COM 바이너리의 문제점 

– 배포의 문제   
    : 시스템 레지스터에 등록해야 하는 번거로움이 존재한다.   
    : .NET – 배포하고자 하는 어셈블리를 응용프로그램이 있는 위치에 복사하면 된다.'
featured_image: ''
tags: ['.net', 'CLR', 'com', 'dev', '매니페스트', '배포', '버전관리', '버전식별자', '어셈블리']
---


<div style="PADDING-RIGHT: 10px; PADDING-LEFT: 10px; PADDING-BOTTOM: 10px; PADDING-TOP: 10px; BACKGROUND-COLOR: #faffa9">  
<font color="#003366">COM 바이너리의 문제점 </font>

– 배포의 문제   
    : 시스템 레지스터에 등록해야 하는 번거로움이 존재한다.   
    : <font color="#d41a01">.NET – 배포하고자 하는 어셈블리를 응용프로그램이 있는 위치에 복사하면 된다.</font>

– 버전관리의 문제   
   : 이전 버전을 사용하는 여러 프로그램이 새로 배포한 새 버전에 의해서 실행상의   
     문제가 발생할수 있다. 버전관리가 매우 어렵다.

 : <font color="#d41a01">.NET – 동일한 바이너리(어셈블리)의 여러버전이 한 머신안에 설치되어 사용되어 질수 있다. </font> 

</div><font color="#003366">.NET 바이너리(어셈블리)의 5 구성요소 </font>

– 표준 WINDOWS 파일헤더  
   : 해당 모듈이 윈도우 운영체제에 의해서 사용될수 있다는 것을 나타내는데 이용

– 파일을 관리 모듈로 표시하는 CLR 헤어   
   : CLR에 의해서 로드될수 있는 모든 .NET 파일들이 지원해야 하는 정보의 블록]  
   : CLR이 해당 관리파일의 구조 이해를 위해서 필요한 플래그(flag)들이 있다.(

– CIL 코드  
   : 플랫폼과 CPU에 독립적인 CIL이 있어야 함.   
   : 나중에 JIT 컴파일러에 의해서 플랫폼과 CPU에 맞게 컴파일 된다.

– 형식 메타 데이터   
   : 어셈블리 내의 형식에 대한 설명 + 어셈블리에서 참조하는 외부형식에 대한 설명

– 어셈블리 메니 페스트(manifest)  
   : 어셈블리 이름(문자열)  
   : 버전 번호(주번호, 부번호, 빌드번호, 수정번호)  
   : 어셈 블리에 있는 모든 모듈 목록  
   : 참조된 어셈블리들에 대한 정보

<font color="#000000">  단일 파일 어셈블리 – 하나의 모듈 (논리적 어셈블리와 물리적 바이너리사이에 1:1 관계)  
   다중 파일 어셈블리 – Mainfest가 다른 관련된 파일들을 참조하는 형식</font>

   물리적 어셈블리 – 사용자 지정형식과 리소들이 포함된 파일  
    논리적 어셈블리 – 현재 응용 프로그램에서 이용할수 있는 public 형식의 버전관리가 되는 집합체

<div style="PADDING-RIGHT: 10px; PADDING-LEFT: 10px; PADDING-BOTTOM: 10px; PADDING-TOP: 10px; BACKGROUND-COLOR: #ffdaed"><font color="#d41a01">이점  
 – 어셈블리는 코드의 재사용성을 높여준다.   
 – 어셈블리는 형식의 경계를 만든다.   
 – 어셈블리는 버전관리가 되고 자기 설명적 개체이다.   
    : 버전식별자를 통해서 정확한 어셈블리의 로드를 만든다.   
 – 어셈블리는 보안 컨텍스트를 정의한다.  
    :  보안의 수위는 어셈블리 수준에서 정의된다.   
    :  정의된 보안제약사항은 메니페스트에 명시적으로 나열된다. – 어셈블리는 병렬적 실행을 가능하게 한다.   
    :  동일한 어셈블리의 여러 버전을 하나의 머신에 설치하고 로드가 가능.

</font></div>

