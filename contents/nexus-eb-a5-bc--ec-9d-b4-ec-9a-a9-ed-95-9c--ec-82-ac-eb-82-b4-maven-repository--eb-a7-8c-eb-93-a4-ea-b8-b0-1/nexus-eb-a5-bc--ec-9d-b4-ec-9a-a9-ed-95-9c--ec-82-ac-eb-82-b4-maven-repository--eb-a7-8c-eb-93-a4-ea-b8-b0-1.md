---
title: 'Nexus를 이용한 사내 Maven Repository 만들기 1.'
author: 'ash84'
pub_date: '2012-12-20'
description: '앞서 이클립스에 maven을 설치하는 과정에 대해서 설명했는데, 이번 장에는 사내 maven Repository를 구성하는 방법에 대해서 알아보자. 일단 사내 Repository를 구성해야 하는 가장 큰 이유는 매번 참조하고 있는 라이브러리를 가져와야 하는 불편함도 있겠지만, 솔직히 필자에게 더 필요한건 사내에서 만들어진 라이브러리를 Repository에 올려놓고 다른 동료개발자분들이 쉽게 찾아서 쓸수 있게 하는것이 더 중요했다.'
featured_image: ''
tags: ['dev', 'maven', 'Nexus', '사내 repository', '자바', '저장소 연경']
---


<span style="font-size: 11pt;">앞서 이클립스에 maven을 설치하는 과정에 대해서 설명했는데, 이번 장에는 사내 maven Repository를 구성하는 방법에 대해서 알아보자. 일단 사내 Repository를 구성해야 하는 가장 큰 이유는 매번 참조하고 있는 라이브러리를 가져와야 하는 불편함도 있겠지만, 솔직히 필자에게 더 필요한건 사내에서 만들어진 라이브러리를 Repository에 올려놓고 다른 동료개발자분들이 쉽게 찾아서 쓸수 있게 하는것이 더 중요했다. </span>

<span style="font-size: 11pt;">자, 이제 Nexus의 세계로 떠나보자. </span>

**[<span style="font-size: 11pt;">1. Nexus 다운받기. </span>](http://www.sonatype.org/nexus/go)**

<span style="font-size: 11pt;">여타의 다른 블로그 글들은 이전 버전으로 되어 있는 경우로 설명하고 있는데, 그래서 war파일을 받아서 설치하는 식으로 설명을 하고 있는데, nexus 측에서 버전을 개량한것으로 보인다. 그냥 다운 받으면 된다.  zip 혹은 tgz 중 원하는것을 받으면 된다. 필자가 받은 버전은 2.2 버전이다. </span>

![](http://ash84.net/wp-content/uploads/1/cfile7.uf.156EA43650D276AC1502A8.PNG)

<span style="font-size: 11pt;">참고로 필자는 윈도우 데스크톱 환경에서 세팅하고 있음을 미리 애기하는 바이다. 리눅스 서버나 윈도우 서버에 설치할수 있으나 연습삼아서 일단 로컬  환경에 해보고 서버로 이전할 생각이다. </span>

<span style="font-size: 11pt;">**2. 실행하기 **</span>

<span style="font-size: 11pt;">다운 받은 파일에 압축을 풀어보면 디렉토리가 있는데 그 중에서</span><span style="font-size: 11pt;">nexus-2.2-01-bundle 디렉토리로 들어가면 다음과 같은 디렉토리와 파일들이 보인다. </span>

![](http://ash84.net/wp-content/uploads/1/cfile24.uf.163E473A50D276C51D2AA3.jpg)

<span style="font-size: 11pt;">일단 conf에 들어가면** nexus.properties **라는 파일이 있는데, nexus 에 대한 설정정보가 들어가 있는 파일이다. nexus는 jetty 기반으로 만들어졌는데, conf에 들어가면 host, port 및 디렉토리 설정 같은것이 있는데, 기본 포트는 8081로 설정되어 있는것을 볼수 있다. 만약, 8081 포트가 다른 용도로 사용하고 있다면 일단 변경하고 저장하자. </span>

<script src="https://gist.github.com/4342358.js"></script>

<span style="font-size: 11pt;">자, 이제 실행해 보자. bin 디렉토리에 들아가면 nexus.bat 파일이 있다. cmd 창을 열어서 nexus.bat 파일을 실행하도로고 하자. <span style="color: rgb(255, 94, 0);">여기서 주의할점! cmd 창이 UTF-8 로 설정되어 있다면 ASCII 로 바꾸어주자. 왜냐하면 nexus.bat 실행시, 다음과 같은 화면이 보여야 하는데, UTF-8의 경우 문구가 나오지 않는다. 주의하자. </span></span>

![](http://ash84.net/wp-content/uploads/1/cfile6.uf.1527833850D276E6104AC1.PNG)

<span style="font-size: 11pt;">보시는 바와 같이 여러가지 명령어가 있는데, 아래와 같이</span><span style="font-size: 11pt;"> start 명령어를 입력해 보자. nexus 가 start 되는 것을 볼 수가 있다. </span>

![](http://ash84.net/wp-content/uploads/1/cfile24.uf.126D0E3450D2771E1B7103.PNG)

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">좀더 확인을 해 보려면, logs 디렉토리에 있는 wrapper.log 파일을 tail -f 로 열어보면 다음과 같다. </span>

![](http://ash84.net/wp-content/uploads/1/cfile2.uf.2336EF3750D276F51A8BAA.PNG)

<span style="font-size: 11pt;">**3. admin 화면 접속하기. **</span>

<span style="font-size: 11pt; line-height: 2;">포트를 바꾸지 않았다면, http://localhost:8081/nexus 를 웹 브라우저에 입력하도록 하자. 만약 포트를 바꾸었다면 바뀐 포트를 입력하면 된다. 입력하면 아래와 같은 화면이 보여질것인데, 일단 로그인하자. </span>

![](http://ash84.net/wp-content/uploads/1/cfile2.uf.156CF23350D2778618578D.jpg)

 

<span style="font-size: 11pt;">로그인은 기본적으로 **admin/admin123** 이다. 로그인 하고 Repositories를 누르면</span><span style="font-size: 11pt;"> 아래와 같은 화면이 보일것이다. 다양한 Repository 들을 nexus에서 기본적으로 제공하고 있기 때문에 잘 사용하면 된다. </span>

![](http://ash84.net/wp-content/uploads/1/cfile25.uf.11310C3450D277A3136C68.jpg)

<span style="font-size: 11pt;">다음 편에서는 본격적으로 **nexus의 repository를 세팅하는 방법**에 대해서 알아 보도록 하자. </span>

 



