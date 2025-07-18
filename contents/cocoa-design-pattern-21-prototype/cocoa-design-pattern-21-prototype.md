---
title: '[Cocoa Design Pattern] 21. Prototype'
author: 'ash84'
pub_date: '2011-07-12'
description: '![](http://ash84.net/wp-content/uploads/1/cfile21.uf.197E8A4E4E1BAD76357DCD.jpg)
**'
featured_image: ''
tags: ['dev', 'IOS', 'prototype pattern', '디자인패턴', '프로토타입']
---


<div></div><div style="line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; ">![](http://ash84.net/wp-content/uploads/1/cfile21.uf.197E8A4E4E1BAD76357DCD.jpg)</span></span>

</div><div style="line-height: 2; ">**<span style="font-size: 10pt; "><span style="font-family: Dotum; ">프로토 타입이란?</span></span>**  
<span style="font-size: 10pt; "><span style="font-family: Dotum; ">– 기능 구현을 위해 복사해서 사용하는 객체 </span></span>  
<span style="font-size: 10pt; "><span style="font-family: Dotum; ">– 기존 객체를 복사해서 사용하는 것은, 새 인스턴스를 생성하는 것 보다 더 유연하다. </span></span>  
<span style="font-size: 10pt; "><span style="font-family: Dotum; ">– 객체간의 강한 의존성 관계를 피하도록 해준다. ‘</span></span>**<span style="font-size: 10pt; "><span style="font-family: Dotum; ">패턴이 만들어진 동기 </span></span>**  
<span style="font-size: 10pt; "><span style="font-family: Dotum; ">– 새로 인스턴스를 생성하는 객체와 해당 객체의 타입간의 의존성을 최소화 </span></span>  
<span style="font-size: 10pt; "><span style="font-family: Dotum; ">– 생성되는 객체의 종류에 대한 정보를 컴파일시 지정하지 않고, 런타임시 조절할 수 있도록 한다. </span></span>

**<span style="font-size: 10pt; "><span style="font-family: Dotum; ">패턴으로 문제 해결</span></span>**  
<span style="font-size: 10pt; "><span style="font-family: Dotum; ">– 핵심기능 : 복사 될수 있다는 것 </span></span>  
<span style="font-size: 10pt; "><span style="font-family: Dotum; ">– NSCopying, NSCoding 프로토콜 제공</span></span>

<span style="font-size: 10pt; "><span style="font-family: Dotum; ">*** NSCopying protocol  – copyWithZone  메소드**</span></span>  
<span style="font-size: 10pt; "><span style="font-family: Dotum; ">– 메소드를 수신하는 객체와 동일한 상태의 객체를 반환해야한다. </span></span>

</div><div style="line-height: 2; margin-left: 4em; "><span style="font-size: 10pt; "><span style="font-family: Dotum; ">1. Shallow Copy</span></span>  
<span style="font-size: 10pt; "><span style="font-family: Dotum; ">– 복사되는 객체와 동일한 값을 저장한다. </span></span>  
<span style="font-size: 10pt; "><span style="font-family: Dotum; ">– 원본을 가리키는 또 다른 포인터를 만드는 것, 포인터 복사 </span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; ">2. Deep Copy</span></span>  
<span style="font-size: 10pt; "><span style="font-family: Dotum; ">– 원본 객체에 저장된 값의 실제 복사본을 저장  
</span></span>

</div><div>  
<span style="line-height: 2; font-size: 10pt; "><span style="font-family: Dotum; ">* 프로토 타입 패턴은 딥 카피를 제공하는 객체와 가장 잘 동작,  
   완벽히 독립적인 사본이 필요한 경우가 있기 때문임. </span></span>  
<span style="line-height: 2; font-size: 10pt; "><span style="font-family: Dotum; ">ex) IB Library의 경우, 복사된 객체는 인터페이스 빌더가 종료된 후에도 동작해야함. </span></span><span style="line-height: 2; font-size: 10pt; "><span style="font-family: Dotum; ">그러나, 대부부의 코코아클래스는 NSCopying 프로토콜을 구현해서 Shallow copy를 반환함. </span></span>

<span style="line-height: 2; font-size: 10pt; "><span style="font-family: Dotum; ">*** Deep Copy가 쉽지 않은 이유**  
   : 참조하고있는 객체중 Shallow copy를 반환하도록 구현되어 있다면, 섞이게 된다. </span></span>

<span style="line-height: 2; font-size: 10pt; "><span style="font-family: Dotum; ">*</span></span>**<span style="font-size: 10pt; "><span style="font-family: Dotum; "> NSArchiver, NSUnarchiver class 는 쉬운 Deep Copy 방식을 제공 </span></span>**  
<span style="line-height: 2; font-size: 10pt; "><span style="font-family: Dotum; ">– 복사되는 객체와 그 객체 내에서 참조하는 모든 객체들이 NSCoding Protocol을 따른다면, Deep Copy 반환</span></span>  
<span style="line-height: 2; font-size: 10pt; "><span style="font-family: Dotum; ">– 347p 예제 : 아카이빙 한 후, 언아카이빙하는 것은 딥 카피를 만들기 위한 억지 기법</span></span>

<span style="line-height: 2; font-size: 10pt; "><span style="font-family: Dotum; ">–  IB 라이브러리에서 객체를 복사할때 사용하는 방식. </span></span>  
<span style="line-height: 2; font-size: 10pt; "><span style="font-family: Dotum; ">– ” 작업중인 .NIB 파일에 객체를 드래그 해서 옮기면, 객체는 기존의 라이브러리 인스턴스르에서 먼저 아카이브 되고나서 언 아카이브하여 추가 편집할 사본을 생성한다. 그리고 .NIB 파일이 저장될 때, 객체들은 다시 아카이브된다. .NIB파일이 로드되면 파일에서 객체가 언아카이브 되어서 IB에 복원된다.”</span></span>

**<span style="font-size: 10pt; "><span style="font-family: Dotum; ">* NSCell – NSCopying프로토콜의 다른 기법인 NSCopyObject() 함수 사용함. </span></span>  
**  
<span style="line-height: 2; font-size: 10pt; "><span style="font-family: Dotum; ">NSCopyObject : 원본이 차지하는 메모리를 그대로 복사해서 Shallow Copy 생성함. </span></span>  
<span style="line-height: 2; font-size: 10pt; "><span style="font-family: Dotum; ">이후, NSCell의 -copyWithZone이 원본에 저장된 속성이 참조한느 객체에 copy 메시지를 보내 복사함. </span></span>  
<span style="line-height: 2; font-size: 10pt; "><span style="font-family: Dotum; ">NSCell은 Shallow copy 와  Deep Copy를 섞어 씀. </span></span>

**  
<span style="font-size: 10pt; "><span style="font-family: Dotum; ">코코아 사용 예제 </span></span>**

<span style="line-height: 2; font-size: 10pt; "><span style="font-family: Dotum; ">– IB 라이브러리 객체는 모두 프로토타입 : 객체를 복사함으로써 IB를 재 컴파일 하지 않아도 확장이 가능함. </span></span>  
<span style="line-height: 2; font-size: 10pt; "><span style="font-family: Dotum; ">– NSMatrix 클래스에서는 프로토타입 NSCell 인스턴스를 사용함. </span></span>  
<span style="line-height: 2; font-size: 10pt; "><span style="font-family: Dotum; ">– 매트릭스에서 행, 열 추가가 있을시에는 필요한 만큼 프로토타입 셀을 복사한다. </span></span>  
<span style="line-height: 2; font-size: 10pt; "><span style="font-family: Dotum; ">– NSMatrix 클래스는 자신이 사용하는 셀에 의존하지 않는다. </span></span>

<span style="line-height: 2; font-size: 10pt; "></span>

<div class="txc-textbox" style="line-height: 2; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-top-color: rgb(203, 203, 203); border-right-color: rgb(203, 203, 203); border-bottom-color: rgb(203, 203, 203); border-left-color: rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; "><span style="font-size: 10pt; "><span style="font-family: Dotum; ">**349p**</span></span>  
<span style="font-size: 10pt; "><span style="font-family: Dotum; ">NSCell의 서브 클래스 </span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; ">MYLabeledBarCell에서 정의한 barValue 역시 NSCopyObject()에 의해서 상속된 변수들과 함께 자동으로 복사된다.  </span></span>

</div><span style="line-height: 2; font-size: 10pt; "><span style="font-family: Dotum; "></span></span>

   
<span style="line-height: 2; font-size: 10pt; "><span style="font-family: Dotum; ">* NSCopyObject() 함수는 포인터를 저장하지 않는 클래스에만 사용해야 한다. </span></span>  
<span style="line-height: 2; font-size: 10pt; "><span style="font-family: Dotum; ">* NSCell의 NSCopyObejct() 사용은 NSCell의 객체를 가리키는 인스턴스 변수를 추가하는 서브클래스 생성하기를 어렵게 만든다. </span></span>

**<span style="font-size: 10pt; "><span style="font-family: Dotum; ">패턴 사용 결과</span></span>**

<div style="text-align: justify;line-height: 2; "><span style="font-family: Dotum; font-size: 13px; line-height: 26px; ">– 객체를 복사하는 작업이 새로운 인스턴스를 생성하는 것 만큼 시간과 비용소요(절약되는 것이 아님)</span></div><span style="font-family: Dotum; font-size: 13px; line-height: 26px; ">  
 – NSMatrix 의 경우, 필요한 셀의 수가 줄어들더라도 프로토타입의 셀 사본을 거의 릴리즈 하지 않는데, 다시 필요할 경우 유지하고 있는 사본을 사용한다. 그러나 메모리가 필요하지 않는 사본을 저장하는데 소비된다는 측며에서 보면 단점이다.</span>

 <span style="line-height: 2; font-size: 10pt; "><span style="font-family: Dotum; ">– 프로토타입 패턴 주의사항 : 프로토타입 객체를 지원하는데 필요한 행동을 문서화 하는 것이 필요함. </span></span>

</div>

