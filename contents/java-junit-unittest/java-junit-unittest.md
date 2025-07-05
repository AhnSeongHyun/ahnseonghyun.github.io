---
title: '[JAVA] 단위테스트를 보다 쉽게, JUnit 을 사용하자.'
author: 'ash84'
pub_date: '2017-03-24'
description: ''
featured_image: ''
tags: ['dev', 'Java', 'JUnit', 'unittest', '단위테스트', '안성현', '자바']
---


<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; line-height: 2; ">단위 테스트를 어떻게 구성해야 할까에 대해서 생각해 볼 경우가 종종 있는것 같다. 실제로 필자가 속한 조직에서는 아직 단위테스트에 대한 필요성을 인지 하지 못한것인지는 모르겠지만, 아무튼 새롭게 프로토타입(Prototype)을 구성중인 자바 기반의 문서 이미지 추출 프로젝트에서는 클린코드와 단위테스트를 필수로 포함시키기로 하였다. </span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "></div><div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; ">**[<span style="font-size: 11pt; ">단위 테스트란?</span>](http://ko.wikipedia.org/wiki/%EC%9C%A0%EB%8B%9B_%ED%85%8C%EC%8A%A4%ED%8A%B8 "[http://ko.wikipedia.org/wiki/%EC%9C%A0%EB%8B%9B_%ED%85%8C%EC%8A%A4%ED%8A%B8]로 이동합니다.")**</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><div class="txc-textbox" style="border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-top-color: rgb(203, 203, 203); border-right-color: rgb(203, 203, 203); border-bottom-color: rgb(203, 203, 203); border-left-color: rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; "><span style="font-size: 11pt; ">  
</span><span style="color: rgb(0, 0, 0); font-family: sans-serif; font-size: 15px; line-height: 22px; text-align: -webkit-auto; background-color: rgb(255, 255, 255); "><span style="font-size: 9pt; ">컴퓨터 프로그래밍에서</span><span style="font-size: 9pt; "> </span></span>**<span style="font-size: 9pt; ">유닛 테스트</span>**<span style="color: rgb(0, 0, 0); font-family: sans-serif; font-size: 15px; line-height: 22px; text-align: -webkit-auto; background-color: rgb(255, 255, 255); "><span style="font-size: 9pt; ">란 소스 코드의 특정 모듈이 의도된 대로 정확히 작동하는지 검증하는 절차다. 즉, 모든 함수와 메소드에 대한 테스트 케이스(</span></span><span lang="en" style="color: rgb(0, 0, 0); font-family: sans-serif; font-size: 15px; line-height: 22px; text-align: -webkit-auto; background-color: rgb(255, 255, 255); " xml:lang="en"><span style="font-size: 9pt; ">Test case</span></span><span style="color: rgb(0, 0, 0); font-family: sans-serif; font-size: 15px; line-height: 22px; text-align: -webkit-auto; background-color: rgb(255, 255, 255); "><span style="font-size: 9pt; ">)를 작성하는 절차를 말한다. 이를 통해서 언제라도 코드 변경으로 인해 문제가 발생할 경우, 단시간 내에 이를 파악하고 바로 잡을 수 있도록 해준다. 이상적으로, 각 테스트 케이스는 서로 분리되어야 한다. 이를 위해 가짜 객체(</span></span><span lang="en" style="color: rgb(0, 0, 0); font-family: sans-serif; font-size: 15px; line-height: 22px; text-align: -webkit-auto; background-color: rgb(255, 255, 255); " xml:lang="en"><span style="font-size: 9pt; ">Mock object</span></span><span style="color: rgb(0, 0, 0); font-family: sans-serif; font-size: 15px; line-height: 22px; text-align: -webkit-auto; background-color: rgb(255, 255, 255); "><span style="font-size: 9pt; ">)를 생성하는 것도 좋은 방법이다. 유닛 테스트는 (일반적인 테스트와 달리) 개발자(</span></span><span lang="en" style="color: rgb(0, 0, 0); font-family: sans-serif; font-size: 15px; line-height: 22px; text-align: -webkit-auto; background-color: rgb(255, 255, 255); " xml:lang="en"><span style="font-size: 9pt; ">developer</span></span><span style="color: rgb(0, 0, 0); font-family: sans-serif; font-size: 15px; line-height: 22px; text-align: -webkit-auto; background-color: rgb(255, 255, 255); "><span style="font-size: 9pt; ">) 뿐만 아니라 보다 더 심도있는 테스트를 위해 테스터(</span></span><span lang="en" style="color: rgb(0, 0, 0); font-family: sans-serif; font-size: 15px; line-height: 22px; text-align: -webkit-auto; background-color: rgb(255, 255, 255); " xml:lang="en"><span style="font-size: 9pt; ">tester</span></span><span style="color: rgb(0, 0, 0); font-family: sans-serif; font-size: 15px; line-height: 22px; text-align: -webkit-auto; background-color: rgb(255, 255, 255); "><span style="font-size: 9pt; ">)에 의해 수행되기도 한다.</span></span>

<span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; line-height: 2; ">  
</span></div><div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; line-height: 2; ">단위 테스트에 대해서 막연히 알고 있었고, 필요하다고는 느끼고 있었지만 처음 도입해 보는 과정에서 여러가지 시행 착오가 있었다. </span></div><div style="text-align: justify; line-height: 2; "><span style="font-size: 10pt; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></span><span style="font-size: 10pt; line-height: 2; "><span style="font-size: 11pt; ">가장 큰 문제는 </span>**<font color="#e31600"><span style="font-size: 11pt; ">단위테스트 코드는 어디에 위치하는것 인가? </span></font>**<span style="font-size: 11pt; ">하는 부분이었다. main함수에서 해야하는 것인지(이 경우, 객체를 생성해야 하고 publc 함수 밖에 테스팅 할수 밖에 없다.) ,  해당 클래스 내 함수가 있는 위치에서 따로 뽑아서 해야하는것인지(이럴경우, 객체를 만들 필요가 없고, private 함수까지 테스팅을 할 수 있다.) 고민되는 부분이 있었다. </span></span></div><div style="text-align: justify; line-height: 2; "><span style="font-size: 10pt; line-height: 2; "><span style="font-size: 11pt; ">  
</span></span></div><div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; "><span style="font-size: 11pt; ">또 다른 문제는 </span>**<font color="#e31600"><span style="font-size: 11pt; ">명명법에 대한 문제</span></font>**<span style="font-size: 11pt; ">인다. 같은 함수내에 단위 테스트에 대한 코드를 둔다면, 실제 실행 함수와 어떻게 구별할 것인가? 함수 앞에 test_ 접두어를 붙일수도 있지만, 더 큰 문제는 나 외에 다른 동료들도 이러한 내용을 강제하고 지키도록 동의를 해야한다는 것이다. 그렇지 않는다면, 소스코드는 실제 사용하는 부분과 그리고 테스트 코드 부분을 구분 할 수 없게 되는 문제가 있다. </span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 11pt; ">처음에는 main() 함수가 있는 클래스에 static 함수로 다른 클래스의 실제 사용하는 함수를 테스팅 하는 코드를 넣는 방식으로 하였다. 이 경우 문제점은 여러가지 함수를 테스팅하기 위해서는 main()에서 다양한 static 테스트 함수들을 써야 한다는 점이다. 그래서 좀 불편한것 같았다. </span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; ">**<span style="font-size: 11pt; ">그러던 중 JUnit 에 대해서 알게되었다. 일단 써보면서 특징을 설명하겠다</span>**<span style="font-size: 11pt; ">. </span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; "><span style="font-size: 11pt; ">일단 JUnit을 사용하기 전에, </span>  
<span style="font-size: 11pt; ">  
</span>**  
<span style="font-size: 11pt; ">  
 빌드 패스(Build Path)에서 추가 라이브러리(Add Library)를 눌러서 JUnit을 추가</span>**<span style="font-size: 11pt; ">하도록 하자. 필자는 JUnit3를 설치하였다. 자 그러면, 이제 JUnit 을 본격적으로 사용해 보자. </span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span><figure class="wp-caption aligncenter" style="width: 640px">![](http://ash84.net/wp-content/uploads/1/cfile25.uf.161ECF484F127E0537D1A9.png)<figcaption class="wp-caption-text">빌드경로에서 라이브러리 추가</figcaption></figure>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
  </span>

</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><figure class="wp-caption aligncenter" style="width: 526px">![](http://ash84.net/wp-content/uploads/1/cfile1.uf.122E11494F127E1908F177.png)<figcaption class="wp-caption-text">JUnit3 선택</figcaption></figure>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; "><span style="font-size: 11pt; ">이클립스의 File의 New를 눌러서</span>**<span style="font-size: 11pt; "> JUnit Test Case</span>**<span style="font-size: 11pt; ">를 누르면 테스트 케이스를 만들수 있다. 아래의 화면과 같이 나오게 되면 일단 하단에서 New JUnit3 Test Case를 선택한다. 우리는 앞에서 JUnit3 라이브러리를 추가했기 때문에 이것을 선택해 주면된다. 그리고 나서 되도록 현재 만드는 단위 테스트가 속할 패키지를 지정해 준다. 되도록이면 지정하는 것이 좋다. 왜냐하면 JUnit Test Case 역시 하나의 클래스 파일이기 때문에 패키지로 구분해 주는 것이 가독성 측면에서 좋다.</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span><figure class="wp-caption aligncenter" style="width: 527px">![](http://ash84.net/wp-content/uploads/1/cfile25.uf.15338B494F1282A014A07E.png)<figcaption class="wp-caption-text">JUnit Test Case 추가</figcaption></figure>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>

</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; "><span style="font-size: 11pt; ">패키지 지정을 했으면, 이름(name)을 지정해 주자. 일반적인 클래스 이름이라고 생각하시면 되는데 이때에 일반 클래스를 대상으로 테스트 하는 것이기 때문에 이름에서 어떤 클래스를 테스트 하고 있음을 나타내는 동시에, 이 클래스가 유닛테스트 클래스라는 것을 알려주자. 예를 들어, 내가 ExtractorImage 라는 클래스에 대한 유닛테스트를 만든다고 하면, UnitTest_ExtractorImage 이런식으로</span><font color="#0686a8"><span style="font-size: 11pt; "></span><u><span style="font-size: 11pt; ">UnitTest_ 라는 접두어를 통해서 해당 클래스가 유닛테스트 클래스 임을 알려주자.</span></u></font><span style="font-size: 11pt; "> </span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; "><span style="font-size: 11pt; ">마지막으로는 어떤 클래스에 대한 유닛테스트 인지를 설정하는 부분으로 제일 아래에 있는 </span><u><font color="#318561"><span style="font-size: 11pt; ">class under test 에서 browse를 눌러서 테스트 하려는 클래스를 적어주면 알아서 찾아준다</span></font></u><span style="font-size: 11pt; ">. 자, 입력을 다 했으면, 이제 Next를 누르면 앞에서 입력한 테스트 대상 클래스의 함수들이 나온다. 보시면 알겟지만, Public 함수에 대해서만 테스트를 할 수가 있다. 이 단계에서 테스트를 할 함수를 체크를 한다. 체크를 다했으면 기본적은 단위 테스트의 구성이 끝나고 해당 단위테스트 클래스가 만들어 지는것을 볼 수가 있다. </span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span><figure class="wp-caption aligncenter" style="width: 600px">![](http://ash84.net/wp-content/uploads/1/cfile29.uf.1702EF4F4F1282BE09AEED.png)<figcaption class="wp-caption-text">테스트 대상 클래스 지정</figcaption></figure>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>

<figure class="wp-caption aligncenter" style="width: 526px">![](http://ash84.net/wp-content/uploads/1/cfile24.uf.11580E4A4F1285D61BCFF8.png)<figcaption class="wp-caption-text">테스트 할 함수 지정</figcaption></figure>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 11pt; ">만들어진 단위 테스트 클래스의 내부를 보자. </span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span><span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>

<figure class="wp-caption aligncenter" style="width: 367px">![](http://ash84.net/wp-content/uploads/1/cfile23.uf.201D7B424F128444376A01.png)<figcaption class="wp-caption-text">JUnit 테스트 결과</figcaption></figure>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 11pt; ">우리가 앞에서 지정했던 함수에 대해서 미리 만들어져 있다. 그런데 형태를 보면, public void testExtractorManager() 이런 형태로 원래 함수 test라는 접두어를 붙여서 표시를 하였다. 일단 한번 테스팅을해 보자 테스팅을 하면 이전과 다르게 오른쪽에 JUnit 테스트에 대한 결과를 보여주는 창이 나온다. 보시면 Runs, Errors, Fails 가 있는데 처음 생성을 하면 아래처럼 나오기 때문에 현재는 Fails:4 라고 표시가 되어 있다. </span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; "></span><script src="https://gist.github.com/3620991.js"><span style="font-size: 11pt; "></script><span style="font-size: 11pt; "></span>  
<span style="font-size: 11pt; ">  
</span><font size="2"><span style="line-height: 26px;">  
<span style="font-size: 11pt; ">  
</span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; line-height: 2; ">이제 구현을 해 보자. 일단 각각의 테스트 함수에다가 필요한 테스트 코드들을 넣어준다. 만약 테스트 함수 외의 함수를 넣고 싶다면, test 접두어를 붙이지 않은채 코드를 넣으면 된다. 예를 들어 testExtractImage() 함수에서 특정 디렉토리 경로를 가져오는 함수를 호출해야 한다면, </span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; "></span>

<script src="https://gist.github.com/3620997.js"><span style="font-size: 11pt; "></script><span style="font-size: 11pt; "></span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 11pt; ">이런식으로 GetTestDocPath()를 써주면 된다. 대신에 이 부분은 test접두어로 시작되지 않기 때문에 JUnit test를 실행 시킬때 결과에 표시되지 않는다. 그렇다면, 검사 대상 클래스의 내용이 추가 된다면 어떻게 해야 할까? 다시 앞의 단계를 반복해야할까?</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 11pt; ">수동으로 JUnit 테스트의 결과에 포함되는 테스트 함수를 추가 시키는 방법은 간단하다. 어떤 테스트 하려는 함수를 만들고 그 함수이름의 제일 앞에 test 접두어를 붙여주면 된다. 예를들어, testExtractImage1() 을 만들어 주고 테스트를 돌려보면 아래와 같은 결과를 얻을 수가 있다. </span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><figure class="wp-caption aligncenter" style="width: 366px">![](http://ash84.net/wp-content/uploads/1/cfile9.uf.1525083D4F12846A31F690.png)<figcaption class="wp-caption-text">수동 테스트 함수 추가 결과</figcaption></figure>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 11pt; ">추가된 함수가 결과에 포함된 것을 볼수가 있다. 이렇게 하면 대상 클래스의 내용이 변하더라도 능동적으로 테스트 코드에 추가할 수가 있다. </span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; "><span style="font-size: 11pt; ">자, 이제 다 구현을 하고 JUnit을 돌려보자. 필자가 생각하는 JUnit의 가장 큰 장점은 </span><u><font color="#c8056a"><span style="font-size: 11pt; ">해당 함수에 대한 실행 시간을 표시해 줄수 있다는 것</span></font></u><span style="font-size: 11pt; ">이다. 사실 프로그래머는 성능 측정에 대해서 자유로울 수가 없는데 JUnit 에서는 이런 부분을 쉽게 해결해 준다. 하나의 함수에 대한 실행 시간을 알려줌으로써, 어떤 부분이 병목을 가지고 있는지 테스트 케이스를 구성함으로써, 쉽게 알수가 있다. C 언어에서 처럼 시간을 측정하는 부분을 넣을 필요가 없다.(사실 이 부분은 소스코드를 더럽히기도 하고, 다른 여러가지 툴이 있을것이라 생각된다.)</span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; ">**<span style="font-size: 11pt; ">결론. </span>**</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div class="txc-textbox" style="border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-top-color: rgb(203, 203, 203); border-right-color: rgb(203, 203, 203); border-bottom-color: rgb(203, 203, 203); border-left-color: rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 11pt; ">JUnit을 꼭 사용하자. </span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 11pt; ">그리고 성능 측정을 하고, 개선을 하자. </span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 11pt; ">그리고 쉽게 유지보수 할수 있는 여지를 주자. </span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 11pt; ">마지막으로. 쉽게 인수인계 할수 있을것 같다. </span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; "></span>

<span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>



