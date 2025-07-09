---
title: '(iOS) crashlytics 을 이용한 crash 관리 및 github 연동'
author: 'ash84'
pub_date: '2013-10-30'
description: 'vingle 에 갔을 때, 앱 개발 관련 소개를 들으면서 crashlytics 라는 서비스가 있다고 해서 메모해 두었는데, 실제 업무에 적용해 보았다.([crashlytics 는 트위터에 인수되었다고 한다.](http://besuccess.com/2013/01/28496/))'
featured_image: ''
tags: ['Crashlytics', 'Crashlytics logger', 'dev', 'github', 'IOS']
---


<span style="font-size: 11pt;"></span><span style="font-size: 11pt;"></span><span style="font-size: 11pt;">vingle 에 갔을 때, 앱 개발 관련 소개를 들으면서 crashlytics 라는 서비스가 있다고 해서 메모해 두었는데, 실제 업무에 적용해 보았다.(</span>[crashlytics 는 트위터에 인수되었다고 한다.](http://besuccess.com/2013/01/28496/)) <span style="background-color: transparent; font-size: 11pt;">일단 crashlytics 는 간단히 말해서 앱에서 crash 가 나게되면 해당 정보를 서버로 전송해주고 개발자는 해당 사이트의 웹을 통해서 확인하는 방식인데, 좋은 점은 crash 가 떨어졌을때 아이폰을 가지고 crash 로그를 확인하면 메모리 주소가 나와서 진짜 문제가 있는 부분을 찾기 어려운 경우가 많은데, </span><span style="background-color: transparent; font-size: 14.44444465637207px; line-height: 32.22222137451172px;">crashlytics은 비교적 정확히 문제를 찾아 준다는 점이다. </span><span style="background-color: transparent; font-size: 11pt; line-height: 2;"> </span><span style="background-color: transparent; font-size: 11pt; line-height: 2;"> 일단 개별적으로 구축할 수도 있겠지만 몇 개 안되는 앱을 개발하는 과정에서 사실 큰 공수가 아닐 수 없기 때문에 사용하게 되었다. </span>

<span style="font-size: 11pt;">**가입 방법**</span>

<span style="font-size: 11pt;">그냥 가입하면 되는게 아니라 crashlytics 홈페이지에 가서 가입 신청을 누르고 이메일 주소를 입력하고 나서 기다리면 만 하루정도 후에 가입 관련 이메일이 오고 가입되게 된다. </span>

<span style="font-size: 11pt;">**설치 방법 **</span>

<span style="font-size: 11pt;">iOS 냐 Andriod 냐에 따라 다른데, 일단 iOS 기준으로 설명하자면, crashlytics 에서 맥에 설치할수 있는 플러그인 같은 프로그램을 제공하고 해당 프로그램을 설치하면 아래와 같이 맥상단의 메뉴에 작은 아이콘으로 표시될것이다. 그리고 나서 해당 플러그인에서 하라는 데로 하면 된다. </span>

![](http://ash84.net/wp-content/uploads/1/cfile24.uf.243DAB475270B066133246.png)

<span style="font-size: 11pt;">crashlytics framework 를 xcode 안에 넣고, apple script를 본인의 xcode project 의 build phase 에 넣고 build 를 하고 마지막으로 발급된 key를 appDelegate.m 파일내  </span><span style="background-color: transparent; font-size: 11pt; line-height: 1.5;">didFinishLaunchingWithOptions: 함수내 제일 상단에 다음의 코드처럼 적어주면 된다. </span>

<span style="background-color: transparent; font-size: 9pt; line-height: 1.5;">  
</span>

<span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;"></span>

<span style="font-size: 11pt;">  
</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size:10pt;">[</span><span class="s2" style="font-size: 10pt;">Crashlytics</span><span class="s1" style="font-size: 10pt;"></span><span class="s3" style="font-size: 10pt;">startWithAPIKey</span><span class="s1" style="font-size: 10pt;">:</span><span style="font-size: 10pt;">@”349123401928340283</span><span style="font-size: 10pt;">“</span><span style="font-size:10pt;">];</span>

</div><span class="s1">  
</span>

<span style="font-size: 11pt;">**관리 **</span>

<span style="font-size: 11pt;">crash 가 오게 되면 맥의 플러그인에 보여지게 되고, 웹에서도 볼수 있다. 맥의 플러그인에서 누르면 사실 웹으로 이동하고 각각의 crash 된 것을 볼수가 있다. 같은 부분에서 발생한것은 취합해서 보여주고 몇명의 유저가 crash 를 겪었는지를 보여준다. </span>

<span style="font-size: 11pt;">  
</span>

![](http://ash84.net/wp-content/uploads/1/cfile1.uf.2434154B5270B0A426A810.png)

<span style="font-size: 11pt;">  
</span>

![](http://ash84.net/wp-content/uploads/1/cfile8.uf.2136AD4A5270B0C91ED357.png)

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">**github와 연동 **</span>

<span style="font-size: 11pt;">웹상의 관리자에서 settings => app 에 들어가게 되면 Integration 이라는 메뉴가 있는데 해당 메뉴에 가면 현재는 10개의 서비스와 연동되는 것을 볼수가 있다. 그중에 github와 연동을 활성화하면 자동으로 활성화가 되고 crash가 발생하면 issue로 등록할 repository 를 지정해 주면 끝난다. </span>

<span style="font-size: 11pt;">  
</span>

![](http://ash84.net/wp-content/uploads/1/cfile27.uf.214AAB3A5270B0DC27FD0A.png)

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">그래서 crash 가 발생이 되면 </span><span style="background-color: transparent; font-size: 11pt; line-height: 2;">Crashlytics 서비스에서 볼수가 있게 되고, 자동으로 지금 사용하는 git<span style="font-size: 11pt;">hub repository 로 들어가게 된다. 아래와 같이 말이다. 그러나 github 에 올라간 이슈의 처리에 대해서는 </span></span><span style="font-size: 12px; line-height: 18px; background-color: transparent;"><span style="font-size: 11pt;">Crashlytics 에 반영되지는 않는다.</span> </span>

<span style="background-color: transparent; font-size: 11pt; line-height: 1.5;">  
</span>

![](http://ash84.net/wp-content/uploads/1/cfile8.uf.275421345270B1293585A9.png)

<span style="background-color: transparent; font-size: 11pt; line-height: 1.5;">  
</span>

<span style="background-color: transparent; font-size: 9pt; line-height: 1.5;">  
</span>

<span style="background-color: transparent; font-size: 11pt; line-height: 2;">**안드로이드는?**</span>

<span style="font-size: 11pt;">당연히 된다. [http://www.sjava.net/342](http://www.sjava.net/342) 를 참고하면 된다. </span>

<span class="s1">  
</span>

<span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;"></span>



