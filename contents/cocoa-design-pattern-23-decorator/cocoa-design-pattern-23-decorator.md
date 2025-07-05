---
title: '[Cocoa Design pattern] 23. Decorator'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['cocoa design pattern', 'Composition', 'Decorator', 'dev', 'has-a', 'IOS', 'is-a', '데코레이터', '코코아 디자인 패턴']
---


<div style="LINE-HEIGHT: 2"></div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2">  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">![](http://ash84.net/wp-content/uploads/1/cfile23.uf.205946374E1D407127DB25.jpg)</span></span><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"> </span></span>

**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">데코레이터란?</span></span>**

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 서브클래싱을 통해 기능을 추가하는 대신 컴포지션을 통해서 공통적으로 재사용 가능한 기능을 객체에 추가</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 서브 클래싱은 컴파일 단계에서 정의해야 하지만, 데코레이터는 런타임 단계에서 추가 및 구성 가능함. </span></span>

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">ex) NSScrollView </span></span>

**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">패턴이 만들어진 동기 </span></span>**

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 기존 객체에 여러가지 기능을 추가하고 싶음. 그러나, 클래스 수의 증가가 문제임. </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 서브 클래스 = is – a 관계</span></span>

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">Text – RulerText – BorderedRulerText</span></span>

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 상속을 통해서 필요한 기능을 확장해 나가는 형태, 특정 기능을 위해 계층이 복잡해짐. </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 다중 상속을 통해서 간단한 계층을 시도하지만,   
   다중상속은 클래스의 수를 줄이는것 보다는 상속 관계를 바꿔줌. </span></span>

**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">데코레이터 패턴의 목표 </span></span>**

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">  
<div class="txc-textbox" style="BORDER-BOTTOM: #cbcbcb 1px solid; BORDER-LEFT: #cbcbcb 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #ffffff; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #cbcbcb 1px solid; BORDER-RIGHT: #cbcbcb 1px solid; PADDING-TOP: 10px"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">1. 상속 대신 조합으로 어플리케이션의 동작을 사용자화 한다. </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">2. 런타임의 유연성 제공, 런타임 상태에서 기능을 동적으로 추가 및 제거 가능</span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">3. 클래스 대신 각각의 인스턴스에 기능을 추가한다. </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">4. 필요한 클래스의 수를 줄여준다.</span></span>  
</div></span></span>

**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">패턴으로 문제 해결</span></span>**

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 조합(Composition)은 Has – a 관계를 정의한다. 데코레이터 패턴은 암묵적으로 has-a 관계를 사용한다. </span></span>

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">ex) </span></span>

<div class="txc-textbox" style="BORDER-BOTTOM: #cbcbcb 1px solid; BORDER-LEFT: #cbcbcb 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #ffffff; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #cbcbcb 1px solid; BORDER-RIGHT: #cbcbcb 1px solid; PADDING-TOP: 10px"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">NSClipView 인스턴스가 자신의 도큐먼트 뷰를 데코레이트한다. </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">= NSClipVIew 인스턴스가 도큐먼트 뷰를 소유한다 </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 조합은 런타임시에 구성되고, 동적으로 바꿀수 있다</span></span>  
</div>**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">* NSScrollView </span></span>  
**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– setDocumentView 메소드를 제공해서 내장된 클립뷰의 도큐먼트 뷰를 설정하도록 제공 </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 도큐먼트 뷰는 NSView의 서브클래스라면 가능 즉, 사용자 정의의 커스텀 뷰도 가능하며, 숫자 제한이 없다. </span></span>

**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">코코아 사용 예제 </span></span>**

<div class="txc-textbox" style="BORDER-BOTTOM: #cbcbcb 1px solid; BORDER-LEFT: #cbcbcb 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #ffffff; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #cbcbcb 1px solid; BORDER-RIGHT: #cbcbcb 1px solid; PADDING-TOP: 10px">  
 일반 적인 데코레이터 패턴의 사용 예제 : [http://mrhook.co.kr/79](http://mrhook.co.kr/79)</div>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 이 패턴은 주로 MVC의 뷰 단계 에서만 주로 사용된다. </span></span><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 예외도 있다. </span></span>

**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">NSAttributedString </span></span>  
**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– NSString + (폰트, 문단 스타일, 이미지 내장 등등) : 속성을 데코레이트 </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 자신이 꾸미는 문자열을 수정하지 않는다. 단지, 그 문자열과 추가 정보만을 함께 저장함. </span></span>

*<font color="#e31600"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">365p. 표23.1 중요한 코코아 데코레이터 클래스 </span></span></font>*

**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">액세서리 뷰 </span></span>**

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– </span></span><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">코코아 표준 사용자 인터페이스 패널 : 사용자가 만든 데코레이터 추가 가능하다. </span></span>

**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">NSSavePanel, NSColorPanel 등등</span></span>**  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">**–** setAccessoryView 메소드 제공 : 해당 패널에 원하는 액세서리뷰를 표시 할수 있음.  </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 표준 패널은 다양한 패널 클래스를 서브 클래싱 하지 않아도 기능을 추가 할 수 있다 </span></span>

**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">* OS X 10.5 부터 NSPrintPanel과 NSPageLayout 클래스에  addAccessoryContoller 메서드로 액세서리뷰를 관리 하는 새로운 방식 제공함. </span></span>**

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 액세서리 뷰를 직접 사용하는 것에서 액세서리 뷰 컨트롤러를 사용하게 변화 </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– MVC 패턴의 일관된 사용을 장려, 액세서리 뷰와 어플리케이션 로직 사이에 위치한 컨트롤러 코드를 어디에 구현해야 하는지 명확히 함. </span></span>  
**  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">패턴 사용 결과 </span></span>**<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"> </span></span>

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 객체지향의 상속관계는 강력 그러나, 의존성의 원인임. </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 컴파일시 정적으로 설정되고, 서브클래스의 모든 인스턴스에 영향을 준다. </span></span>

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 컴포지션은 보다 유연한 대안을 제공함. </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 객체를 런타임시 확장하는것은 더 동적이고, 클래스가 아닌 인스턴스 단우에서의 적용이 가능하다. </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 다수의 클래스 사용을 하지 않고도 더 컴포지션으로 다수의 기능을 추가하는 것이 가능하다. </span></span>

<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 다른 프레임 워크 에서는 데코레이터가 꾸미는 객체와 동일한 인터페이스를 갖도록 요구함. </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">– 코코아에서는 제약이 없음. </span></span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"> </span></span>

</div>  
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2">  
</div>

