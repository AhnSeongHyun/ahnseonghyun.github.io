---
title: '(iOS) TestFlight 사용해서 ipa 배포하기'
author: 'ash84'
pub_date: '2017-04-25'
description: ''
featured_image: ''
tags: ['dev', 'IOS', 'IPA', 'ipa 만들기', 'ipa 설치', 'TestFlight', '배포']
---

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>

[<span style="font-size: 11pt;">TestFlight</span>](http://testflightapp.com/)<span style="font-size: 11pt;">에 대해서 알게된 경우는 최근에 티스토리 앱을 개발하는 어떤 개발자가 클리앙에서 테스트 해볼 사람을 모집하면서 였다. </span>[<span style="font-size: 11pt;">TestFlight</span>](http://testflightapp.com/)<span style="font-size: 11pt;"> 의 요점은 개발한 ipa 에 대한 테스트를 수동이 아닌 이메일을 통해서 전달하고 테스트 할수 있도록 한다는 점이다. iOS 개발에는 이해할수 없지만 요상하게도 DEBUG 에서는 잘 되는데 앱상에서 올리기만 하면 안되는 문제가 있는데, ipa 파일로 만들어서 여러 기기에서 테스트함으로써 미처 발견하지 못하는 문제점을 발견할수 있다는 장점이 있다. 사용법을 설명할텐데 미칠만큼 간단하다. </span>

<span style="font-size: 11pt;">**1. 가입하기 **</span>

<span style="font-size: 11pt;">– 그냥 가입하면 되는데 일단 개발자임을 선택해주길 바란다. 이건 사실 가입후에 선택할수 있는 부분이다. 가입을 하고나면 인증메일이 오게 되는데, 본인의 아이폰에서 인증을 받아야 되는것으로 알고 있다.(사실 이부분은 잘 기억이 안난다. 오래전에 가입해서) **<u>근데 이 과정에서 중요한 점은 아이폰의 Safari 웹 브라우저에서만 된다는 점이다. </u>**</span>

<span style="font-size: 11pt;">  
</span>

![](http://ash84.net/wp-content/uploads/1/cfile7.uf.2527A83552B2913F253257.png)

<span style="font-size: 11pt;">**2. 팀만들기 **</span>

<span style="font-size: 11pt;">– 팀을 만들어야 한다. 팀을 만들고 테스터들을 이메일로 초대해서 팀에 넣어야 한다. 일단은 팀을 만들고 나를 팀에 넣었다.</span>

<span style="font-size: 11pt;"> </span>

![](http://ash84.net/wp-content/uploads/1/cfile1.uf.2573793552B2913F3C690D.png)

<span style="font-size: 11pt;">**3. 맥 전용툴 설치하기 **</span>

<span style="font-size: 11pt;">– 사실 직접 ipa를 올리는 방법(웹사이트에서)을 지원하기는 하지만 보다 편한 방법은 TestFli</span><span style="font-size: 11pt;">ght</span><span style="font-size: 11pt;"> Desktop App을 설치하는 것이다. 이것을 설치하게 되면 개발자가 xcode 상에서 ipa 생성을 위해서</span><span style="font-size: 11pt;"> Archive 를 선택하면 자동으로 감지에서 TestFli</span><span style="font-size: 11pt;">ght</span><span style="font-size: 11pt;">에 업로드 하고, 테스터들에게 보낼것인지를 선택할수 있다. 올리는 방법은 아래와 같이 다양하게 있으니 각자의 업무 환경에 맞게 사용하면 된다. </span>

![](http://ash84.net/wp-content/uploads/1/cfile22.uf.2211C63352B291C131CE4D.png)

<span style="font-size: 11pt;">**4. Upload**</span>

<span style="font-size: 11pt;">– 앞에서 TestFli</span><span style="font-size: 11pt;">ght</span><span style="font-size: 11pt;"> Desktop App을 설치했기 때문에 Archive만 해주면 된다. Archive를 하면 맥 화면 오른쪽에 알림으로 업로드 하겠냐는 팝업이 생기게 되고 Upload 를 누르고 code singing을 선택하고 나면 자동으로 upload 가 된다. 그리고 팀내에서 어떤 사람들에게 보낼것인지 선택을 하면 발송이 된다. </span>

<span style="font-size: 11pt;">**5. 발송 확인**</span>

<span style="font-size: 11pt;">– 발송을 하면 테스터의 이메일로 전송이 되고 테스터가 메일을 열어보면 앱에 대한 install 버튼이 있다. 해당 버튼을 누르면 TestFli</span><span style="font-size: 11pt;">ght</span><span style="font-size: 11pt;"> 로 접속이 되고 설치가 되는것을 확인 할 수가 있다. </span>

![](http://ash84.net/wp-content/uploads/1/cfile2.uf.24583B3352B294A8052746.jpg)



