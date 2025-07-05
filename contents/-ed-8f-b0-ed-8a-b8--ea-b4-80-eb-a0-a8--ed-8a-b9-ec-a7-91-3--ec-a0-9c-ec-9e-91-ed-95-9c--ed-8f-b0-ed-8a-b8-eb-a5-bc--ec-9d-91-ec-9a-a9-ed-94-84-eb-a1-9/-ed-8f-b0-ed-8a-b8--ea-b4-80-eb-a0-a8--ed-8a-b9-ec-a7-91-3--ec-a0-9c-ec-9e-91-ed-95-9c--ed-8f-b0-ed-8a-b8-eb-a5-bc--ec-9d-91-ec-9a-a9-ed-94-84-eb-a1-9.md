---
title: '[폰트 관련 특집] 3. 제작한 폰트를 응용프로그램에 적용하자.'
author: 'ash84'
pub_date: '2010-09-03'
description: ''
featured_image: ''
tags: ['c#', 'Font Class', 'FontCollection', 'InstalledFontCollection', 'PrivateFontCollection', '윈도우 폰트', '폰트 개발', '폰트 적용']
---


<span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">유니코드와 폰트와의 관계 그리고 폰트 제작에 대해서 이전 포스팅에서 알아 보았습니다</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">링크는 아래의 링크를 참고하시면 됩니다</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span>

<span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; "><span style="font-size: 11pt; "></span></div><span style="font-size: 11pt; ">  
</span>

<span style="font-family: '맑은 고딕'; line-height: 26px; font-size:10pt; "><span><span style="font-family: Dotum; "><span style="font-size: 10pt; "><span style="font-size: 10pt; "><span style="font-size: 11pt; ">     </span><font color="#000000">[<span style="font-size: 11pt; ">① </span>](http://ash84.tistory.com/632 "[http://ash84.tistory.com/632]로 이동합니다.")</font></span></span></span></span><span><span style="font-family: Dotum; "><span style="font-size: 10pt; "><span style="font-size: 10pt; "><font color="#000000">[<span style="font-size: 11pt; ">유니코드와 폰트와의 관계</span>](http://ash84.tistory.com/632 "[http://ash84.tistory.com/632]로 이동합니다.")</font></span></span></span></span></span>

<span style="font-size: 11pt; ">  
</span>

<span style="color: rgb(0, 0, 0); font-family: '맑은 고딕'; line-height: 26px; font-size:10pt; "><span><span style="font-family: Dotum; "><span style="font-size: 10pt; "><span style="font-size: 11pt; ">    </span>[<span style="font-size: 11pt; "> ② </span>](http://ash84.tistory.com/633 "[http://ash84.tistory.com/633]로 이동합니다.")</span></span></span><span><span style="font-family: Dotum; "><span style="font-size: 10pt; ">[<span style="font-size: 11pt; ">폰트를 제작학기 위한 툴</span>](http://ash84.tistory.com/633 "[http://ash84.tistory.com/633]로 이동합니다.")</span></span></span></span>

<span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; "><span style="font-size: 11pt; "></span></div><span style="font-size: 11pt; ">  
</span>

<span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">이번 시간에는 폰트를 어떻게 개발에 이용할 것인가에 대해서 좀더 프로그래밍적인 부분에 대해서 이야기 해보고자  
 합니다</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">일단</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">, </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">폰트를 이용하는 부분은 다양하겠지만 레이블</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">, </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">텍스트박스</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">, </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">콤보 박스</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">, </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">리스트박스  
 등의 텍스트 데이터가 쓰여지는 컨트롤에서 광범위하게 적용 할 수 있다고 봅니다</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">.</span></span></span>

<span style="font-size: 10pt; "><span style="font-family: Dotum; ">**<span style="font-size: 11pt; ">  
</span>**</span></span>

<span style="font-size: 10pt; "><span style="font-family: Dotum; ">**<span style="font-size: 11pt; ">그렇다면</span>**</span></span><span style="line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; ">**<span style="font-size: 11pt; ">, </span>**</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; ">**<span style="font-size: 11pt; ">어떻게 그러한 컨트롤들에 폰트를 적용시킬 수 있을까요</span>**</span></span><span style="line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; ">**<span style="font-size: 11pt; ">?</span>**</span></span></span>

<span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; "><span style="font-size: 11pt; "></span></div><span style="font-size: 11pt; ">  
</span>

<span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">먼저 폰트를 윈도우 시스템에 등록을 해야 합니다</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">물론 시스템에 등록하지  
 않고 사용할 수 있는 방법도 있는데</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">, </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">그 방법에 대해서는 차후에 설명하도록 하겠습니다</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">시스템에 등록한다는 것은 어렵게 설명한 것이지만</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">, </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">쉽게 설명하면  
 만들어진 폰트를</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><span style="font-size: 11pt; "></span>**<span style="font-size: 11pt; ">Windows/Fonts </span>**</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; ">**<span style="font-size: 11pt; ">폴더</span>**<span style="font-size: 11pt; ">에 추가하면 되는 것입니다</span></span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">.</span></span></span>

<span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; "><span style="font-size: 11pt; "></span></div><span style="font-size: 11pt; ">  
</span>

<span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">이렇게 </span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">Windows </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">시스템에 폰트를 추가하면</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">, </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">자연스럽게</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> MS </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">워드 혹은 한글</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">(hwp)</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">의  
 폰트 창에서 확인 할 수가 있습니다</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">왜냐하면 해당 오피스 프로그램들의 폰트는 윈도우 시스템에 추가된  
 폰트들을 기반으로 하고 있기 때문입니다</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span>

<span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; "><span style="font-size: 11pt; "></span></div><span style="font-size: 11pt; ">  
</span>

<span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span></span>

<span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; "><span style="font-size: 11pt; "></span></div><span style="font-size: 11pt; ">  
</span>

<span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">개발자가 개발하는 프로그램의 컨트롤에 폰트를 적용하기 위해서는 다음의 코드를 사용해야 합니다</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span>

<span style="font-size: 11pt; "></span>

<script src="https://gist.github.com/3353811.js"><span style="font-size: 11pt; "></script><span style="font-size: 11pt; "></span>

<span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span></span>

<span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; "><span style="font-size: 11pt; "></span></div><span style="font-size: 11pt; ">  
</span>

<span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">위의 코드를 보시면</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">, Font </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">클래스의 객체를 만들어서 </span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">“AppleGothic” </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">폰트를</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> 24pt </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">의 크기로 하여 텍스트 박스에  
 해당 폰트정보를 적용하는 것을 나타내고 있습니다</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">이 과정에서의 전제 조건은 윈도우 시스템에 등록되어  
 있어야 한다는 것이겠지요</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span>

<span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; "><span style="font-size: 11pt; "></span></div><span style="font-size: 11pt; ">  
</span>

<span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span></span>

<span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; "><span style="font-size: 11pt; "></span></div><span style="font-size: 11pt; ">  
</span>

<span style="font-size: 10pt; "><span style="font-family: Dotum; ">**<span style="font-size: 11pt; ">그렇다면</span>**</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; ">**<span style="font-size: 11pt; ">, </span>**</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; ">**<span style="font-size: 11pt; ">앞에서 언급한대로 윈도우 시스템에 등록하지 않으면 쓸 수  
 없을까요</span>**</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; ">**<span style="font-size: 11pt; ">?</span>**</span></span></span>

<span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; "><span style="font-size: 11pt; "></span></div><span style="font-size: 11pt; ">  
</span>

<span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">닷넷에서는 </span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">Font </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">외에도 </span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">FontCollection  
</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">이라는 추상 클래스</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">(abstract class)</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">를 가지고 있는데</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">, msdn</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">을 살펴보면</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">, </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">설치된 글꼴 컬렉션과 전용 글꼴 컬렉션의 기본  
 클래스를 제공한다고 나와 있습니다</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">좀 말이 어렵지요</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">간단히  
 설명하자면</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">,</span></span></span>

<span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; "><span style="font-size: 11pt; "></span></div><span style="font-size: 11pt; ">  
</span>

<span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span></span>

<span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; "><span style="font-size: 11pt; "></span></div><span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>

<div class="txc-textbox" style="border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-top-color: rgb(203, 203, 203); border-right-color: rgb(203, 203, 203); border-bottom-color: rgb(203, 203, 203); border-left-color: rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; "><span><span style="font-size: 10pt; "><span style="font-family: Dotum; ">**<span style="font-size: 11pt; ">FontCollection</span>**<span style="font-size: 11pt; "> (Abstract Class)</span></span></span></span>

<span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; "><span style="font-size: 11pt; "></span></div><span style="font-size: 11pt; ">  
</span>

<span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#0686A8">**<span style="font-size: 11pt; "> </span>**</font></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#0686A8">**<span style="font-size: 11pt; ">– InstalledFontCollection  
</span>**</font></span></span></span>

<span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; "><span style="font-size: 11pt; "></span></div><span style="font-size: 11pt; ">  
</span>

<span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#E31600">**<span style="font-size: 11pt; "> </span>**</font></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#E31600">**<span style="font-size: 11pt; ">–  
 PrivateFontCollection</span>**</font></span></span></span>

<span style="font-size: 11pt; ">  
</span>

</div><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "></span></span></span>

<span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; "><span style="font-size: 11pt; "></span></div><span style="font-size: 11pt; ">  
</span>

<span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span></span>

<span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; "><span style="font-size: 11pt; "></span></div><span style="font-size: 11pt; ">  
</span>

<span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">InstalledFontCollection </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">은 시스템에 설치된 폰트를  
 나타내는 클래스입니다</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">실질적으로</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> Font </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">클래스와 별반  
 다를 게 없다고 보시면 될 것 같습니다</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">. Families </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">속성을 통해서 시스템에 있는 폰트를 이름기반으로  
 검색할 수가 있습니다</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">.</span></span></span>

<span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; "><span style="font-size: 11pt; "></span></div><span style="font-size: 11pt; ">  
</span>

<span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#E31600"><span style="font-size: 11pt; ">PrivateFontCollection </span></font></span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#E31600"><span style="font-size: 11pt; ">은 한마디로 시스템에 설치하지  
 않고 응용프로그램에서 쓸 경우</span></font></span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#E31600"><span style="font-size: 11pt; ">, </span></font></span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#E31600"><span style="font-size: 11pt; ">폰트를 적용할 때 사용할 수 있는 클래스 입니다</span></font></span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#E31600"><span style="font-size: 11pt; ">. MSDN</span></font></span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#E31600"><span style="font-size: 11pt; ">에 보면 시스템에 있는</span></font></span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#E31600"><span style="font-size: 11pt; "> Arial </span></font></span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#E31600"><span style="font-size: 11pt; ">글꼴을 전용버전으로 만들  
 수 있다고 하는데</span></font></span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#E31600"><span style="font-size: 11pt; ">, </span></font></span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#E31600"><span style="font-size: 11pt; ">그 부분에 대해서는 좀더</span></font></span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#E31600"><span style="font-size: 11pt; "> MSDN</span></font></span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#E31600"><span style="font-size: 11pt; ">을 참고하시고</span></font></span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#E31600"><span style="font-size: 11pt; ">, </span></font></span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#E31600"><span style="font-size: 11pt; ">설치 안 해도 되는 폰트를 적용하는 법에 대해서 설명하도록 하겠습니다</span></font></span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#E31600"><span style="font-size: 11pt; ">. </span></font></span></span></span>

<span style="font-size: 11pt; "></span>

<script src="https://gist.github.com/3353815.js"><span style="font-size: 11pt; "></script><span style="font-size: 11pt; "></span>

<span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span></span>

<span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">기존의</span></span><span style="line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> Font </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">클래스를 사용하는 것은 마찬가지이나</span></span><span style="line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">, Font </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">클래스의 객체를 만들 때에는</span></span><span style="line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> Family </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">이름을 넣어야  
 하기 때문에</span></span><span style="line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> PrivateFontCollection </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">객체를 이용해서 그 작업을 해주는 것입니다</span></span><span style="line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">객체를 일단 만드신 후에 </span></span><span style="line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">AddFontFile() </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">함수를 통해 해당  
 폰트파일의 주소</span></span><span style="line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">(File Path)</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">를 넣어주시고</span></span><span style="line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">Font </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">객체에  
 생성자에 해당</span></span><span style="line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> Family </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">이름을 전달해 주시면 됩니다</span></span><span style="line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">.</span></span></span>

<span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; "><span style="font-size: 11pt; "></span></div><span style="font-size: 11pt; ">  
</span>

<span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span></span>

<span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; "><span style="font-size: 11pt; "></span></div><span style="font-size: 11pt; ">  
</span>

<span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">참고로</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">, </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><span style="font-size: 11pt; ">이러한 개발에 적용 가능한 폰트의 형태는 </span>**<font color="#E31600"><span style="font-size: 11pt; ">트루타입의 폰트</span></font>**<span style="font-size: 11pt; ">만  
 가능합니다</span></span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span>

<span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; "><span style="font-size: 11pt; "></span></div><span style="font-size: 11pt; ">  
</span>

<span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span></span>

<span style="font-size: 11pt; ">  
</span>

<figure class="wp-caption aligncenter" style="width: 400px">![](http://ash84.net/wp-content/uploads/1/cfile30.uf.116244054C80BA27510685.jpg)<figcaption class="wp-caption-text">최근 타이포그라피에 관심이 가는 필자.</figcaption></figure>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">이번 포스팅에서는</span></span><span style="line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">, </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">시스템에 폰트를 등록하는 방법과 등록된 폰트를  
 개발 프로그램에 적용하는 방법 그리고 등록되지 않은 폰트를 개발 프로그램에 적용하는 방법에 대해서 알아보았습니다</span></span><span style="line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">.  
</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">사실 저 역시 이번 과제를 통해서 폰트와 유니코드와의 관계 그리고 실제 폰트를 개발한다는 것에 대해서 또한 개발된 폰트를 프로그램에  
 적용하는 과정에 대해서 공부하게 되었던 계기였습니다</span></span><span style="line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">.</span></span></span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 10pt; "><span style="font-family: Dotum; "><span style="font-size: 11pt; ">폰트에 대해서는 </span>**<span style="font-size: 11pt; ">타이포그래피</span>**</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; ">**<span style="font-size: 11pt; ">(Typography) </span>**</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">하시는 분들이 더  
 잘 알거라 생각됩니다</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">아랍어 같은 경우에는 가운데 혹은 마지막에 글자가 위치하면 변형되기도 하고 글자끼리  
 필기체처럼 이어지는 부분이 있어서</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">, </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">폰트를 만들기 어렵더군요</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">새삼  
 폰트디자이너 분들의 수고를 알게 되었습니다</span></span><span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span>



