---
title: '[maven] 기본 설치 및 메이븐 프로젝트 만들기'
author: 'ash84'
pub_date: '2012-12-18'
description: 'maven에 대해서 포스팅 하는 이유는 Java 의 빌드에 대해서 여러가지 방법이 있지만, 가장 jar에 대한 관리가 잘 되기 때문이라는 생각에서였다. 본 글은 이클립스 Juno 버전이 설치되어 있다는 가정하에 진행하도록 하겠다. 기존의 이클립스가 있으신 분들이라면 Juno 버전을 따로 다운 받아서 해보시길 바란다. 
**1. 마켓플레이스에서 다운 받기 **

![](http://ash84.ne'
featured_image: ''
tags: ['JAR', 'Java', 'dev', 'maven', 'project-showcase', '빌드']
---
<span style="font-size: 11pt;">maven에 대해서 포스팅 하는 이유는 Java 의 빌드에 대해서 여러가지 방법이 있지만, 가장 jar에 대한 관리가 잘 되기 때문이라는 생각에서였다. 본 글은 이클립스 Juno 버전이 설치되어 있다는 가정하에 진행하도록 하겠다. 기존의 이클립스가 있으신 분들이라면 Juno 버전을 따로 다운 받아서 해보시길 바란다. </span>

<span style="font-size: 11pt;">**1. 마켓플레이스에서 다운 받기 **</span>

![](http://ash84.net/wp-content/uploads/1/cfile27.uf.03666E5050CFBA4D05EE1B.PNG)

<span style="font-size: 11pt;">보시는 화면처럼 maven 이라고 검색을 하면 몇개의 메이븐 관련 플러그인들이 나오는데, 제일 위에 있는** m2eclipse-wtp : Maven Integration for Eclipse WTP(Incubation)**을 사용하면 된다.  Install 을 누르면 자동적으로 설치될것이고, 이클립스를 한번 restart 할것이다. </span>

<span style="font-size: 11pt;">**2. maven 프로젝트 만들기 **</span>

<span style="font-size: 11pt;">플러그인이 설치된 상태에서 늘 하던대로 **New>Other>Maven Project**를 아래처럼 누른다. </span>

![](http://ash84.net/wp-content/uploads/1/cfile7.uf.0230BF4E50CFBBD111EF09.PNG)

<span style="font-size: 11pt;">그리고 나서 일단 기본적인 maven 프로젝트를 만드는 것이기 때문에 Create a simple project를 체크하도록 하자. 그리고 나서 Next. </span>

![](http://ash84.net/wp-content/uploads/1/cfile2.uf.2228804B50CFBBEF1DACFB.PNG)

<span style="font-size: 11pt;">아래와 같이 정보를 입력하는데 세가지 용어에 대해서 알아보자. 그전에 하나의 artifact를 하나의 jar 라고 간편 생각해보자. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">1. Group Id : artifact 제작을 책임지는 개체, 조직, ex) com.ibm.devworks</span>

<span style="font-size: 11pt;">2. Artifact Id : 실제 Artifact 이름, ex) HelloWorld</span>

<span style="font-size: 11pt;">3. version : aritifact 버전,  mmm.nnn.bbb-qqqqqqq-dd 와 같다. 여기에서 mmm 은 메이저 버전 숫자, nnn 은 마이너 버전 숫자, bbb 는 버그 수정 레벨을 나타낸다. 가끔 qqqqq (수식어) 또는 dd (빌드 숫자)를 버전 넘버에 추가로 붙일 수 있다.</span>

</div>![](http://ash84.net/wp-content/uploads/1/cfile7.uf.25469C4750CFBC591F547B.PNG)

![](http://ash84.net/wp-content/uploads/1/cfile9.uf.20668A4D50CFBE971E8856.jpg)

<span style="font-size: 11pt;">Finish를 누르면 maven 프로젝트가 생성된 것이다. 구조를 한번 보면 다음과 같다. 기존의 자바프로젝트와 다른점이라면, **Maven Dependencies 와 pom.xml** 이라는 것이 생겼다는 것이다. pom.xml에 마우스 우클릭을 하면 maven 항목이 있는데, 그 안에서 Add Dependency 를 선택하자. 구글의 json 파서인 Gson 라이브러리를 추가해보도록 하자. gson 이라고 입력한 결과 화면이다. </span>

![](http://ash84.net/wp-content/uploads/1/cfile22.uf.2122AD4850CFBF402D2B28.PNG)

<span style="font-size: 11pt;">검색된 결과 화면을 볼수 있을것이다. 가장 위에 있는 com.google.code.gson 을 선택해 보자. 선택을 하면 2가지가 바뀌는데 한가지는 pom.xml 을 열어보면 <dependency> 에 gson이 다음과 같이 걸려 있는것을 볼수가 있다. 또 한가지는 Maven Dependencies 에 gson-2.2.2.jar 가 다음과 같이 추가된 것을 볼 수가 있다. 즉, Maven 을 통해서 추가된 라이브러리는 maven 에 의해서 관리가 되는것이다. </span>

<script src="https://gist.github.com/4324000.js"></script>

![](http://ash84.net/wp-content/uploads/1/cfile21.uf.247ECA4A50CFC0DB2BBAFC.jpg)

<span style="font-size: 11pt;">다음 시간에는 아래와 같이 차례대로 알아보도록 할것이다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 9pt; color: rgb(0, 34, 102);">[1](http://ash84.tistory.com/871) [. nexus 를 이용해서 사내 Maven ](http://ash84.tistory.com/871)</span><span style="font-size: 9pt;"><span style="color: rgb(0, 34, 102);">[Repository 만드는 방법. ](http://ash84.tistory.com/871)</span></span>

<span style="color: rgb(0, 34, 102); line-height: 29px;">2. 실제 개발된 자바 프로그램을 maven을 이용해서 jar화 하는 방법.</span>

</div><span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">**Reference**</span>

<span style="font-size: 11pt;"> – [http://www.ibm.com/developerworks/kr/library/tutorial/j-mavenv2/section4.html](http://www.ibm.com/developerworks/kr/library/tutorial/j-mavenv2/section4.html)</span>



