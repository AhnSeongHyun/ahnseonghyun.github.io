---
title: '[Cocoa Design Pattern] 22. Flyweight pattern'
author: 'ash84'
pub_date: '2015-07-03'
description: '![](http://ash84.net/wp-content/uploads/1/cfile24.uf.122D734C4E1C04261DF168.jpg)

**22. 플라이 웨이트 패턴 **

**플라이웨이트 패턴이란?**  
 – 객체를 사용할 때 필요한 메모리의 양과 프로세서 오버헤드를 최소화시킨다.   
 – 인스턴스 공유를 가능하게 하여, 실제 인스턴스의 수를 줄여준다. 

**패턴이 만들어진 동기 **

– 비 – 객체 데이터를 캡슐화하여 객체가 필요한 컨텍'
featured_image: ''
tags: ['cocoa design pattern', 'dev', 'Flyweight', 'IOS', 'ios dev', 'pattern', '아이폰 앱 개발']
---


<div></div><div style="line-height: 2; ">![](http://ash84.net/wp-content/uploads/1/cfile24.uf.122D734C4E1C04261DF168.jpg)

**22. 플라이 웨이트 패턴 **

**플라이웨이트 패턴이란?**  
 – 객체를 사용할 때 필요한 메모리의 양과 프로세서 오버헤드를 최소화시킨다.   
 – 인스턴스 공유를 가능하게 하여, 실제 인스턴스의 수를 줄여준다. 

**패턴이 만들어진 동기 **

– 비 – 객체 데이터를 캡슐화하여 객체가 필요한 컨텍스트에 그 데이터를 사용할수 있게 한다.   
 – 많은 수의 인트선트가 필요할때 저장공간 요구를 줄여준다.   
 – 다른 객체의 대역으로 행동한다. 

**패턴으로 문제 해결**

스프레드 시트의 경우   
 – 행과 열의 모든 셀을 각각의 인스턴스로 표시할 것인가?  
 – 공유가능한 인스턴스 : 셀이 비어 있는 경우, 동일한 값을 가지고 있는 경우 (SpreadSheetCell)  
 – 포맷 정보의 분리 (SpreadSheetCellFormat)

– 인스턴스 공유를 통해서 총 사용하는 인스턴스의 수를 줄일수 있다.   
 – 인스턴스에 저장된 정보의 일부를 따로 클래스화 함으로써 저장을 최소화 시킨다. 

**  
 코코아 사용 예제   
**  
**3가지 목적 :  
**

<div class="txc-textbox" style="border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-top-color: rgb(203, 203, 203); border-right-color: rgb(203, 203, 203); border-bottom-color: rgb(203, 203, 203); border-left-color: rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; ">1. 비-객체 값을 캡슐화   
 2. 메모리 사용 줄이기   
 3. 다른 객체의 대역으로 사용

</div>**비-객체 값을 캡슐화   
**  
 * NSNumber  
  – char, int, long, float 와 같은 숫자형 데이터 타입, bool 과 같인 데이터 타입도 객체형으로 전환 가능  
  – NSNumber 의 슈퍼클래스인 NSValue 가 비객체 데이터 타입에 객체 래퍼를 제공. 

* NSDecimalNumber, NSDate, NSString 등과 같은 클래스 모두 비 객체 값이나 데이터 구조를 감싼다. 

**저장공간 요구 감소 **

NSNumber 인스턴스 공유   
 – 최근에 사용한 혹은 자주 사용하는 NSNumber 인스턴스는 캐시에 저장한다. 그리고 요청이 오면 꺼내서 반환함.   
 – 인스턴스 공윤는 해당 클래스가 수정 불가능 할때만 가능하다. 

NSFont, NSColor 역시 수정 불가능한 인스턴스를 캐시하고 재사용함. 

NSCell   
 – NSCell 의 인스턴스는, NSString, NSImage 의 포인터와 같이 상대적으로 단순한 값만 저장.   
 – NSView 가 80바이트를 사용함에 비해 NSCell은 20바이트 사용함. 

– NSTableView와 NSMatrix 에서 사용함으로써 저장공간 감소 효과 

**다른 개개체의 대역으로 사용 **

– 좀더 무거운 다른 객체의 임시 자리표시자 역할 수행

– NSTextView : 텍스트 표시와 입력을 다루는 클래스   
 – 그러나, 배치 저장, 철자확인 과 같은 다양한 텍스트 관련 기능에 대한 부분은 다른 클래스와 협력한다. 

– 복잡한 텍스트 관리 시스템의 플라이웨이트 자리표시자로 NSCell을 사용 

**패턴 사용 결과  **

– 패턴을 사용하는 것은 늘 디자인을 복잡하게 한다.   
 ex) C 언어의 데이터 타입과 NSNumber 사이에서의 데이터 변환 

– 분명히 저장공간과 성능의 최적화 효과가 있다.   
 – 그러나, 만약 NSCell을 NSView 대신에 사용 했다면, 코어 애니메이션과 같은 고급 뷰 기능을 사용할 수 없다.   
 – 성능적인 부분에도 문제가 있을수가 있다. 

– 플라이웨이트의 사용이 복잡도를 증가  
 – 개발하려는 어플리케이션에서 저장공간과 성능의 최적화에 대한 이슈가 있다면 사용해라. 아니면 권장하지 않는다.   
    

  

</div>

