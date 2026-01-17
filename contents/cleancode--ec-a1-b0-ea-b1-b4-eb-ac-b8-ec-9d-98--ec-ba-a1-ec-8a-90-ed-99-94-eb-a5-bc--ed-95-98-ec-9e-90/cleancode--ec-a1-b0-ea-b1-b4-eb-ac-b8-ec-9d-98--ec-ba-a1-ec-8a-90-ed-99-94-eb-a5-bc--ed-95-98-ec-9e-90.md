---
title: '[CleanCode] 조건문의 캡슐화를 하자.'
author: 'ash84'
pub_date: '2012-03-17'
description: 'CleanCode의 신봉자로서 맨 처음 여러분께 소개해드릴 내용을 그리 거창한 것도, 특별한 디자인패턴을 요하는 기술도 아니지만 개인적으로 CleanCode라는 책을 읽고 가장 많이 사용하는 부분을 가장 먼저 소개해 드릴려고 합니다.'
featured_image: ''
tags: ['clean-code', 'G28', '조건문을 캡슐화하라', '클린코드']
---
<div style="color: rgb(51, 51, 51); font-family: 굴림; text-align: justify; font-size: 9pt; line-height: 2; "><span style="font-size: 15px; line-height: 2; ">CleanCode의 신봉자로서 맨 처음 여러분께 소개해드릴 내용을 그리 거창한 것도, 특별한 디자인패턴을 요하는 기술도 아니지만 개인적으로 CleanCode라는 책을 읽고 가장 많이 사용하는 부분을 가장 먼저 소개해 드릴려고 합니다. </span></div><div style="text-align: justify; line-height: 2; "><font color="#333333" face="굴림">  
</font></div><div style="text-align: justify; line-height: 2; "><span style="color: rgb(51, 51, 51); font-family: 굴림; font-size: 15px; line-height: 2; ">**<div class="txc-textbox" style="border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-top-color: rgb(203, 203, 203); border-right-color: rgb(203, 203, 203); border-bottom-color: rgb(203, 203, 203); border-left-color: rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; ">조건문의 캡슐화를 하자. 

</div>** 

</span></div><div style="text-align: justify; line-height: 2; "><span style="color: rgb(51, 51, 51); font-family: 굴림; font-size: 15px; line-height: 2; ">CleanCode의 **“냄새와 발견법”** 부분에서 **G28**에 해당하는 부분입니다. 일단 말이 좀 어려울수도 있는데, 쉽게 풀어서 이야기 하면 if 조건절에 들어가는 문을 함수화하자는 이야기 입니다. 일단 아래의 코드를 보시죠.  
  
  </span></div><script src="https://gist.github.com/3390548.js"></script>

<div style="text-align: justify; line-height: 2; "></div><div style="line-height: 2; "><span style="font-family: 굴림; font-size: 15px; line-height: 2; "><div style="text-align: justify; "> 최근에 분석하고 있는 회사내 특정 코드에 대한 부분인데요, 일반적으로 문자열 변수에 대한 널유무를 체크하는 부분입니다. 그렇다면 위의 조건문을 캡슐화를 한다면 어떻게 하는게 좋을까요? 저는 이렇게 했습니다.<script src="https://gist.github.com/3390549.js"></script>

<span style="font-size: 11pt; line-height: 2; ">  
 일단 위의 코드를 보시면 그 전에는 <font color="#5c7fb0">지저분해있던 문자열의 널을 체크하는 두개의 조건문을 하나로 합치면서 이 부분이 확실하게 문자열의 널 유무를 체크하는 것이라는 점에서 IsTextBufferNull 이라는 이름을 통해서 확실하게 제공하고 있습니다.</font> 이런 경우에는 개발자가 굳이 저 함수를 들어가보지 않아도 이름만 잘 짓는다면, 함수의 역할에 대해서 쉽게 유추할 수 있는 부분을 줄수 있어서 매우 좋다고 생각합니다. </span><span style="color: rgb(51, 51, 51); font-size: 11pt; line-height: 2; ">또 다른 예를 볼까요?</span>

<script src="https://gist.github.com/3390551.js"></script>

  <span style="color: rgb(51, 51, 51); font-size: 11pt; line-height: 2; ">위의 코드는 설정 클래스에 있는 값을 가져와서 다른 클래스에서 조건문에서 검사해서 특정 수행을 하는 코드입니다. 실제 제가 손을 대기전의 모습입니다. 일단 문제를 파악해 보면, m_로 시작하는 문구가 많아서 쉽게 조건문에서 무엇을 하는지 눈에 들어오지가 않습니다. 물론 Clean Code 책을 읽어보면 저러한 접두어에 대한 부분 역시 최근에는 IDE의 지원으로 인해서 굳이 할 필요 없다고 합니다. (이 부분에는 언어적 사견이 있음.) </span><span style="color: rgb(51, 51, 51); font-size: 11pt; line-height: 1.5; ">그래서 일단 이렇게 바꿔보았습니다. </span><span style="color: rgb(51, 51, 51); font-size: 11pt; line-height: 1.5; "> </span>

</div></span></div><script src="https://gist.github.com/3390552.js"></script>  
  
<span style="font-family: 굴림; font-size: 11pt; line-height: 2; "><div style="text-align: justify; "><span style="font-size: 11pt; line-height: 2; ">   
 일단 함수화하기전의 문제점은 조건문이 길어지게 되면 당연히 조건문 자체에 대한 가독성이 떨어지게 됩니다. 위의 코드의 경우에는 조건문 자체가 그리 복잡하지는 않지만 대부분의 소스에서는 &&, || 과 각종 연산자를 사용하면서 조건문이 복잡해지고, 지역변수 혹은 멤버변수가 아닌 외부 클래스의 변수를 끌어다쓰게 되면 조건문이 더러워질수 밖에 없습니다. 위의 고친 코드가 주는 효과는 2가지 입니다. 일단 첫 사례와 같이 함수화 해서 의미있는 이름을 제공함에 따라 개발자는 당연히 함수 내부를 보지 않아도 <font color="#5c7fb0">대략적인 기능을 함수이름을 통해서 제공받을수 있습니다.</font> 개발자는 UsePatternException()이라는 함수명을 보고, “아, 몬지는 모르겠는데 패턴제외 라는 것을 사용하는지 여부를 체크하는거구나” 라고 인식 할 수가 있습니다. 

두번째 효과는 <font color="#5c7fb0">함수화한 조건문의 이름의 일관성으로 인해서 생기는 학습의 효과</font>입니다. 일단 함수명 역시 클린코드에서는 비슷한 역할을 할때에는 일관성 있는 이름을 제공하라고 이야기하고 있습니다. 즉, UsePatternException()이라는 함수를 개발자가 내부를 들여다 보면, “아 , 설정 클래스의 특정 변수의 값을 체크해서 판별하는 구나” 라고 생각하게 되고, 비슷한 이름의 UseTextException(), UseSpecialCharException() 함수 역시 대략적인 세부 기능에 대해서 유추 할수 있게 됩니다. 

이번 시간에는 조건의 캡슐화에 대해서 알아 보았습니다. 첫 시간에 이 주제를 잡은 가장 큰 이유는 특별한 패턴이나 지식이 없더라도 이름만 지을줄 안다면 소스코드 상에서 CleanCode의 사례를 구현해 볼수 있는 가장 작은 단위이기 때문에 소개하게 되었습니다. 

저 역시 새로만드는 코드보다는 유지보수하고 남이 짜 놓은 소스를 고치는 경우가 많기 때문에 당연히 이런 사례들을 많이 보게 되는데 소스코드를 싹 바꾸겠다라고 하면 한도 끝도 없기 떄문에 <font color="#5c7fb0">그때 그때 자신이 고치거나 유지보수한 부분에서 위와 같은 부분이 있다면 바꾸는것 부터 시작하는것이 쉬운 Clean Code 실천의 첫 걸음이라고 생각합니다. </font>  
  

</span></div></span><span style="color: rgb(51, 51, 51); font-family: 굴림; font-size: 11pt; line-height: 2; "><div style="text-align: justify;"></div></span><span style="color: rgb(51, 51, 51); font-family: 굴림; font-size: 11pt; line-height: 2; "><div style="text-align: justify;"></div></span>



