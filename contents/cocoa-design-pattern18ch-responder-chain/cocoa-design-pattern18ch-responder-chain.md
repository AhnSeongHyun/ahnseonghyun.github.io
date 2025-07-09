---
title: '[Cocoa Design Pattern]18ch. Responder Chain'
author: 'ash84'
pub_date: '2011-06-17'
description: '**코코아 디자인 패턴 18장. 리소폰더 체인**
**'
featured_image: ''
tags: ['cocoa design pattern', 'dev', 'iPhone dev', 'ResponderChain', '리스폰더 체인', '코코아 디자인 패턴']
---


<div style="text-align: justify; line-height: 2; ">**<span style="font-size: 11pt; ">코코아 디자인 패턴 18장. 리소폰더 체인</span>**</div><span style="font-size: 11pt; ">  
</span>**<div style="text-align: justify;"></div><div style="text-align: justify;"><span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>![](http://ash84.net/wp-content/uploads/1/cfile7.uf.117C973D4E1A5978320787.jpg)  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 9pt; ">  
</span>[<span style="font-size: 9pt; ">2011/06/11 – [Technique/iOS Dev] – [Cocoa Design Pattern] 17ch. Outlet, Target, Action</span>](http://ash84.tistory.com/711)  
<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>

</div>**

<span style="font-size: 11pt; ">  
</span>**<span style="font-size: 11pt; ">리스폰더 체인이란? </span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
  </span>**<span style="font-size: 11pt; ">– 코코아 그래픽 애플리케이션의 핵심적이고 중요한 요소</span>  
<span style="font-size: 11pt; ">  
  – 책임사슬 패턴(Chain of Responsibility)</span>  
<span style="font-size: 11pt; ">  
</span>**  
<span style="font-size: 11pt; ">  
 패턴이 만들어진 동기 </span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
  </span>**<span style="font-size: 11pt; ">– 사용자 이벤트의 정확한 전달</span>  
<span style="font-size: 11pt; ">  
 – 현재 활성화 되어 있는 인터페이스 객체는 무엇이고, 어떻게 액션 메시지를 전달할 것인가. </span>  
<span style="font-size: 11pt; ">  
</span>**  
<span style="font-size: 11pt; ">  
 패턴으로 문제 해결</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
 – </span>**<span style="font-size: 11pt; ">책임사슬패턴은 메시지의 전송자와 수신자 객체 관계를 최대한 분리시키는 것이 목적 </span>  
<span style="font-size: 11pt; ">  
 – 수신객체들이 연결 리스트로 구성되어 있고, 각 객체들이 메시지를 무시 혹은 수신하는 순차적인 시스템 </span>  
<span style="font-size: 11pt; ">  
</span>**  
<span style="font-size: 11pt; ">  
 용어 </span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
  </span>****<span style="font-size: 11pt; ">NSResponder</span>  
<span style="font-size: 11pt; ">  
  </span>**<span style="font-size: 11pt; ">– 사용자 입력을 다룰수 있는 개체들은 모두 NSResponder의 서브클래스</span>  
<span style="font-size: 11pt; ">  
  – 키보드, 마우스, 터치등의 상자 입력에 대응하는 역할</span>  
<span style="font-size: 11pt; ">  
  – NSWindow, NSView, NSViewController, NSDrawer 등이 모두 NSResponder의 서브 클래스</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
  * 사용자의 초점이 어디에 맞춰져 있는지 자동적으로 코코아 프레임워크에서 기억.</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
  </span>**<span style="font-size: 11pt; ">Key</span>**<span style="font-size: 11pt; "></span>**<span style="font-size: 11pt; ">Window</span>  
<span style="font-size: 11pt; ">  
  </span>**<span style="font-size: 11pt; ">– 입력을 받는 윈도우를 키 윈도우</span>  
<span style="font-size: 11pt; ">  
</span>**  
<span style="font-size: 11pt; ">  
 Main Window</span>  
<span style="font-size: 11pt; ">  
  </span>**<span style="font-size: 11pt; ">– 현재 초점이 맞춰져 있는 문서 창을 메인 윈도우</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
 * 키윈도우와 메인 윈도우가 하나의 인터페이스 인 경우도 있지만, 서로 다른 인터페이스인 경우 있음. </span>  
<span style="font-size: 11pt; ">  
</span>**  
<span style="font-size: 11pt; ">  
 NSApplication 의 역할 </span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
  </span>**<span style="font-size: 11pt; ">– 애플리케이션 객체는 키 윈도우와 메인 윈도우를 항상 기억하도록 되어 있음.</span>  
<span style="font-size: 11pt; ">  
  – keyWindow, mainWindow 를 통해서 해당 개개체에 대한 레퍼런스를 얻을수 있음. </span>  
<span style="font-size: 11pt; ">  
</span>**  
<span style="font-size: 11pt; ">  
 FirstResponder</span>  
<span style="font-size: 11pt; ">  
  </span>**<span style="font-size: 11pt; ">– 현재 초점이 맞춰져 있는 뷰를 지칭함</span>  
<span style="font-size: 11pt; ">  
  – 리스폰더 체인의 첫번째 객체</span>  
<span style="font-size: 11pt; ">  
  – -firstResponder : 첫번째 리스폰더에 대한 레퍼런스 </span>**<span style="font-size: 11pt; ">리스폰더 체인</span>  
<span style="font-size: 11pt; ">  
  </span>**<span style="font-size: 11pt; ">– 다수의 수신 객체가 엮여져 있는 형태로 액션 메시지의 대해서 각 노드가 ignore 또는 accept 를 하는 구조</span>  
<span style="font-size: 11pt; ">  
  – nextResponder : 주어진 수신객체의 다음 수신객체를 반환</span>  
<span style="font-size: 11pt; ">  
  – setNextResponder : 다음 객체를 재설정하고 싶을때 사용</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
  – 일반적으로 주어진 뷰의 다음 수신객체는 슈퍼뷰(super view)</span>  
<span style="font-size: 11pt; ">  
  – 윈도우 내 콘텐츠 뷰의 다음 수신객체는 윈도우. </span>  
<span style="font-size: 11pt; ">  
  – 윈도우의 다음 수신 객체는 nil. </span>  
<span style="font-size: 11pt; ">  
  – 리스폰더 체인의 마지막 노드가 윈도우 창이다. </span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
  예외) NSWindowContorller에 의해서 제어되고 있는 윈도우 창은 컨트롤러가 최종 수신 객체임 </span>  
<span style="font-size: 11pt; ">  
  예제) 304p</span>  
<span style="font-size: 11pt; ">  
  </span>  
<span style="font-size: 11pt; ">  
  – 모든 리스폰더 체인은 nil로 끊어지기 때문에, 무한 루프의 위험성이 없다.</span>  
<span style="font-size: 11pt; ">  
  – 윈도우가 여러개인 환경에서는 모든 각각의 윈도우가 리스폰더 체인을 가짐.</span>  
<span style="font-size: 11pt; ">  
  – 윈도우 내 사용자의 선택이 바뀔때 마다 리스폰더체인이 업데이트 됨.</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
  – acceptResponder : 새로운 수신객체가 될 객체에게 전달</span>  
<span style="font-size: 11pt; ">  
  – resignFirstResponder : 현재 리스폰더에게 FirstResponder를 반환하라는 메시지를 전달</span>  
<span style="font-size: 11pt; ">  
 – becomeFirstResponder : 새로운 첫번째 리스폰더가 될 객체에게 전달 – 키보드가 마우스 입력의 경우,</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
 NSApplcation 객체가 입력을 NSEvent 객체로 변환한 다음. 리스폰더 객체를 찾는다.</span>  
<span style="font-size: 11pt; ">  
  – 리스폰더 체인은 계층구조를 이용해서 FirstResponder를 찾아냄. </span>  
<span style="font-size: 11pt; ">  
</span>**  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
 확장된 리스폰더 체인</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
  </span>**<span style="font-size: 11pt; ">– 키 윈도우와 메인 윈도우의 리스폰더 체인을 아우르고, 또한 공용의 NSApplication 인스턴스와 </span>  
<span style="font-size: 11pt; ">  
    NSDocumentController 인스턴스를 포함한 확장 리스폰더 체인.</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
  – nil을 target을 갖는 메시지를 담당.</span>  
<span style="font-size: 11pt; ">  
  – 메뉴 항목의 경우 다양한 종류의 메시지 구현이 쉽지 않다.</span>  
<span style="font-size: 11pt; ">  
  – 키 윈도우와 메인 윈도우의 리스폰더 체인 만으로는 이벤트 핸들링이 불충분한 경우.</span>  
<span style="font-size: 11pt; ">  
  – 확장된 리스폰더 체인의 순서</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
  1. 키 윈도우의 리스폰더 체인의 첫번째 리스폰더를 처음 시도. </span>  
<span style="font-size: 11pt; ">  
  2. 뷰 계층 구조의 리스폰더 체인을 따라 메시지 전달.</span>  
<span style="font-size: 11pt; ">  
  3. 윈도우 객체를 시도</span>  
<span style="font-size: 11pt; ">  
  4. 윈도우의 델리게이트를 시도(주로 NSDocument의 인스턴스)</span>  
<span style="font-size: 11pt; ">  
  5. 만약, NSWindowController가 있다면 시도.  </span>  
<span style="font-size: 11pt; ">  
  6. 1-5의 순서를 메인 윈도우에 적용 </span>  
<span style="font-size: 11pt; ">  
  7. NSApplication 객체와 그의 델리게이트를 시도</span>  
<span style="font-size: 11pt; ">  
  8. NSDocumentController 가 있다면 시도. </span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
 예제) 306P – 307P</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
 – 키 윈도우 == 메인윈도우의 경우, 확장된 리스폰더 체임의 검색 길이는 짧아 짐. </span>  
<span style="font-size: 11pt; ">  
 – 인터페이스 빌더 이용시, 컨트롤을 첫번째 리스폰더에 연결하면, 실제로는 해당 액션에 대한 target를 nil로 지정.</span>  
<span style="font-size: 11pt; ">  
 – 어떤 컨트롤의 액션메시지를 확장된 리스폰더 체인에 전달하고 싶다면 action의 target을 nil로 지정하면 됨. </span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
 [mycontrol setAction:@selector(terminate)];</span>  
<span style="font-size: 11pt; ">  
 [mycontrol setTarget : nil];</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
 NSApplication의 -sendAction:to:from: 메소드에서 확장된 리스폰더 체인으로 보내는 방법 </span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
    [NSApp sendAction:@selector(terminate) to:nil from:self];</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
 메시지를 보내지 않으면서 어떤 객체가 대응하도록 되어 있는지 알고 싶다면, </span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
      id myTarget = [NSApp  targetAction:@selector(terminate) to:nil from:self];</span>  
<span style="font-size: 11pt; ">  
</span>**  
<span style="font-size: 11pt; ">  
 확장된 리스폰더 체인 탐색하기</span>  
<span style="font-size: 11pt; ">  
  </span>**<span style="font-size: 11pt; "> – 리스폰더 체인의 정보를 출력해서 볼수가 있음 : 308p 예제 </span>  
<span style="font-size: 11pt; ">  
</span>**  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
 리스폰더 체인에 객체 삽입하기 </span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
  </span>**<span style="font-size: 11pt; ">– 수동으로 객체 삽입 가능 : NSResponder 의 서브클래스면 가능함.</span>  
<span style="font-size: 11pt; ">  
  – 뷰와 뷰의 superView 사이에 뷰 컨트롤러를 삽입해야 하는 경우</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
  NSResponder * theNextResponder  = [myview nextResponder];</span>  
<span style="font-size: 11pt; ">  
 [myview setNextResponder : myViewController];</span>  
<span style="font-size: 11pt; ">  
 [myviewController setNextResponder:theNextResponder];</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
  – 뷰 컨트롤러가 뷰 다음에 위치하게 되면, 그 뷰가 활성화될 경우에만 작동하게 됨. </span>  
<span style="font-size: 11pt; ">  
   (주어진 윈도우가 하나 이상의 뷰/뷰 컨트롤러 짝을 가지고 있는 경우를 위해서임)</span>  
<span style="font-size: 11pt; ">  
  </span>  
<span style="font-size: 11pt; ">  
  – 리스폰더 체임의 어느위치에 객체를 삽입하느냐에 따라 컨트롤러가 언제 어느 식으로 사용자 입력에 대응하도록 할 것인지를 조정 할 수 있음</span>**<span style="font-size: 11pt; ">. </span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
  </span>****<span style="font-size: 11pt; ">리스폰더 체인 활용하기 </span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
  </span>**<span style="font-size: 11pt; ">– 이미 존재하고 있는 리스폰더 체인을 사용하는 것이 가장 편함. </span>  
<span style="font-size: 11pt; ">  
 – 자동검열 기능, 텍스트의 선택여부에 따른 액션 지정 등은 컨텍스트에 민감한 행동 기능을 리스폰더 체인을 통해서 단순화 시킬수가 있다. </span>  
<span style="font-size: 11pt; ">  
</span>**  
<span style="font-size: 11pt; ">  
 코코아 사용예제 </span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
  </span>****<span style="font-size: 11pt; ">– </span>**<span style="font-size: 11pt; ">코코아에서 리스폰더 체인은 핵심임. </span>  
<span style="font-size: 11pt; ">  
  – 사용자 입력은 NSApplication 객체가 책임을 지고 적합한 리스폰더 체인에게 전달됨.</span>  
<span style="font-size: 11pt; ">  
  – 키 윈도우와 메인 윈도우의 리스폰더 체인을 아우르고, 또한 공용의 NSApplication 인스턴스와 </span>  
<span style="font-size: 11pt; ">  
     NSDocumentController 인스턴스를 포함한 확장 리스폰더 체인.</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
  – nil을 target을 갖는 메시지를 담당.</span>  
<span style="font-size: 11pt; ">  
  – 애플리케이션의 상태에 따라 목표물이 동적으로 좌우되는 액션을 구현해야 한다면, target을 nil로 지정.</span>  
<span style="font-size: 11pt; ">  
  – 복사하기/붙여넣기, 눈금자 조절기능, undo/redo 등의 기능이 확장 리스폰더 체인의 대상</span>  
<span style="font-size: 11pt; ">  
  – 컨텍스트 인식 메뉴들도 리스폰더 체인을 많이 활용  </span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
  </span>**<span style="font-size: 11pt; ">패턴 사용 결과 </span>**  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
  – 다양한 사용자 입력을 처리 할수 있는 유연성을 제공함.</span>  
<span style="font-size: 11pt; ">  
  – 다양한 액션 기능을 최소한의 코드로 구현 가능함.</span>  
<span style="font-size: 11pt; ">  
  – 리스폰더 체인을 활용해서 애플리케이션에 특화된 컨텍스트 인식기능의 구현 가능.  </span>



