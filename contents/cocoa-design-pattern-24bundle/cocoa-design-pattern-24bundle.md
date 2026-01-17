---
title: '[Cocoa Design Pattern] 24.Bundle'
author: 'ash84'
pub_date: '2011-07-14'
description: '![](http://ash84.net/wp-content/uploads/1/cfile1.uf.111CE2494E1D5B1024A668.jpg)

**'
featured_image: ''
tags: ['best-practices', 'bundle', 'cocoa design pattern', 'design-pattern', 'dev', 'iOS', 'java', '번들']
---
<div style="LINE-HEIGHT: 2"></div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2">  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">![](http://ash84.net/wp-content/uploads/1/cfile1.uf.111CE2494E1D5B1024A668.jpg)</span></span>

**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">번들이란?</span></span>**

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 실행코드와 이미지, 사운드, 문자열, NIB 파일과 같은 리소스의 모음</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 각 리소스의 다른 버전을 동시에 저장, 사용자의 언어나 지역 설정에 따라   
   다른 버전의 리소스를 사용 가능하게 함. </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 자바의 JAR(Java ARchive), C# 프로그래밍의 리소스</span></span>

**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">패턴이 만들어진 동기 </span></span>**

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 필요한 리소스가 내부 저장 공간에 여러버전과 여러 파일로 구성되어있는 경우에도,  
    한 곳에 모을 수 있도록 한다. </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 실행코드와 리소스를 동적으로 로드 할 수 있도록 유연한 플러그인 기법을 구현한다. </span></span>

**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">패턴으로 문제 해결</span></span>**

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 번들 = 디렉토리 : 코드, 리소스등을 파일시스템 디렉토리를 통해서 만든것 </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 계층구조로 구성되어 있다. </span></span>

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">**[구성](http://developer.apple.com/library/ios/#documentation/CoreFoundation/Conceptual/CFBundles/BundleTypes/BundleTypes.html#//apple_ref/doc/uid/10000123i-CH101-SW1 "[http://developer.apple.com/library/ios/#documentation/CoreFoundation/Conceptual/CFBundles/BundleTypes/BundleTypes.html#//apple_ref/doc/uid/10000123i-CH101-SW1]로 이동합니다.")**</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">* Contents</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 모든 번들 리소스 담고 있다. </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">  </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">  * Info.plist : 번들에 대한 정보, Unique 하게 식별 가능한 번들 식별자 문자열을 저장하고 있음. </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">  * Mac OS : 애플리케이션 실행 파일 </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">  * Resources : nib 파일, 그래픽, 문자열, 리소스 파일, 지역별버전(.lproj) 폴더 </span></span>

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 사용자에게 하나의 파일처럼 보이게 하는 효과 있음. (패키지)</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 그러나 언제든지 파인더를 통해서 내부 파일을 볼수 있다. </span></span>

**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">* 번들의 장점 </span></span>  
**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 번들은 패키지이자, 표준 파일 뷰어로 볼수 있기 때문에 편집이 가능하다. </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 이동 복사, 삭제가 가능</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 순진한 사용자는 내부 파일을 볼 일이 없어서 변경의 가능성이 줄어든다. </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 다국어 , 지역화 지원. 원치않는 지역화 리소스 쉽게 제거 </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 여러버전 저장 및 실행코드의 여러버전을 포함 할 수 있음. </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 특정기능에 의존적이 아니라, 서버 또는 다양한 파일시스템에 저장할 수 있다. </span></span>

**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">*배포 </span></span>  
**  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– CD : 번들을 CD로 복사 </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 네트워크 : 문제 야기의 가능성 있음, 번들의 일부만 다운로드 받을 가능성</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– DMG : 디스크이미지로 생성, 이동식 디스크로 마운트 됨 </span></span>

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">* 항상 번들을 사용해야하는 것은 아니다. (독립형 커맨드라인 프로그램 개발 가능)</span></span>

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 번들 제작시, 자동으로 XCode가 이미지, 사운드 파일등과 같은 표준 리소스를 자신이 속하는 곳에 위치시킨다. </span></span>

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"> </span></span>  
**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">코코아 사용 예제 </span></span>**

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 번들을 NSBundle 클래스로 캡슐화 </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 하나의 어플은 적어도 하나의 번들을 가지며, 메인 번들은 [NSBundle mainBundle]을 통해서 접근 가능함. </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– NSApplication – mainBundle – load nib file. </span></span>

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 동적으로 실행코드와 리소스를 불러올 수 있다. (375p)</span></span>

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 현재 언어와 지역 설정에 적합한 버전의 경로 반환</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 지정된 지역화에 해당하는 리소스 버전에 대한 경로 반환 하는 등의 리소스 접근 관련 메소드를 제공함. </span></span>

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– NSBundle은 Foundation 프레임워크에 소속되어 있지만, ApplicationKit 프레임워크에서 카테고리를 통해서 </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">  NSBundle을 여러 방면으로 확장한다. </span></span>

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">* 메인 번들 뿐만아니라 실행코드를 담고 있는 번들에 접근하는 것도 가능함. (I don’t know)</span></span>

**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">동적으로 실행코드 로드하기</span></span>**

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 번들은 어플리케이션 구동시 자동 로드된다. </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 번들을 동적으로 불러들이려면 </span></span>

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">+(NSBundle*)bundleWithPath:(NSString*)fullPath : NSBundle 인스턴스 생성</span></span>

**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">377p 예제 : myPlugin.bundle 을 로드</span></span>**

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 번들 인스턴스 만들고 캡슐화 해도 자동 로드되지 않는다. 해당 코드를 사용할필요가 있을시까지 기다린다. </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 강제로 실행코드를 어플리케이션에 링크하게 하려면, NSBundle의 load 메소드 또는 principalClass 메소드 사용 (I don’t know) </span></span>

</div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2">**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">패턴 사용 결과 </span></span>**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"> </span></span>

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">–  실행코드와 관련 리소스를 한곳에 두어, 어플리케이션 구동시, 리소스 경로를 하드코딩 하지 않아도 된다. </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">–  리소스와 코드를 저장시, 디렉토리 계층 사용의 장단점</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">    : 사용자가 해당 어플리케이션의 번들의 내용물을 보고 편집 할수 있다는 점</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">    : 그러나, 다른 사용자가 어플리케이션을 언제든지 확인, 수정,삭제가 가능하다는 것.  </span></span>

</div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2">  
</div>

