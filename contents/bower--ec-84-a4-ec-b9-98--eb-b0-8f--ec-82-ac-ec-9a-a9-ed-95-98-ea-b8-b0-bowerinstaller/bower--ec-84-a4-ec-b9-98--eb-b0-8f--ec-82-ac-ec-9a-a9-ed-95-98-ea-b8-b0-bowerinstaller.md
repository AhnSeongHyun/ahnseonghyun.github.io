---
title: 'bower 설치 및 사용하기, bower-installer'
author: 'ash84'
pub_date: '2015-03-23'
description: ''
featured_image: ''
tags: ['bower', 'brower-installer', 'dev', 'grunt', 'JavaScript', 'Node.js', 'npm', '패키지관리']
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

python, flask 를 이용해서 웹 서비스나 API를 구축하는것이 주 업무다 보니 사실 flask 는 너무 유연해서 뒷단(백엔드 부분은) uwsgi 나 mod_wsgi – apache의 조합으로 사용해 왔는데, 앞단(프론트 엔드)을 어떻게 해야 할지 고민하다가 예전에 본 [outsider 님의 슬라이드](http://www.slideshare.net/rockdoli/adieu-springsprout2014)를 보고 bower, grunt 등에 대해서 테스트 해보게 되었다.

**npm 설치**

원래 node.js를 안해봤던 터라, npm으로 설치하라고 하는데, npm은 node.js를 깔아야 자동으로 설치가 된다고 하고 뭔가 약을 산 느낌.. 아무튼, 여기를 가서 윈도우용 nodejs를 설치.

[https://nodejs.org/](https://nodejs.org/) 

커맨드 창에서 node -v 라고 치면 버전 나오면 설치 완료된것이다. 

```
$ node -v
v0.12.0
```
npm -v 쳐보면 제대로 설치 된것을 확인할 수가 있다. 

**bower 설치**

```
$ npm install -g bower 
```

bower -v 로 설치 확인해보자. 하나의 프로젝트 예를들면, test 를 만들고 그 안이 나중에 app.py(main)이 python, flask 로 작업할떄 위치하는 공간이라고 가정하자.

**bower 사용하기**

```
$ mkdir test
$ cd test
$bower install jquery
```

bower는 특이하게 모든 것의 기준의 **현재 디렉토리 기준**으로 설치가 된다. 위에서 처럼 jquery 를 bower를 이용해서 설치하게 되면, **현재 디렉토리 기준 ./bower_components 가 생성**되고 하위에 install 한 패키지가 생긴다. 삭제는 uninstall 을 사용하면 된다.

```shell
$bower install jquery bootstrap
```

여러개를 인스톨 하려면 아래와 같이 한칸띄고 써주면 된다.

flask를 많이 사용하는 나로서는 ./bower_components 에 설치되는 것이 짜증이지만 일단은 참고 인터넷에서 매번 찾아서 내려받는 수고를 하지 않아도 된다는 것에 감사하자. 물론 CDN를 쓰면 더 좋겠지만, 그 외의 다른 CDN 이 없지만 bower를 지원하는 라이브러리들은 쉽게 내려받아서 <내 프로젝트에 배치 할수 있는것이 장점인것 같다. 찾을려면 search 명령어를 사용하면 된다.


```
$ bower search table //패키지 명에 table 이 들어간 패키지들을 찾느다.
 
$ bower lookup table //패키지 명이 table 인 패키지를 찾는다.
 
$ bower info jquery //해당 패키지의 정보, 버전정보를 보여준다.

bower init
```
bower init 을 하게 되면 해당 디렉토리(현재 test)에 bower.json 이라는 파일이 생기는데, 설치한 패키지에 대한 정보를 명시하는 역할로 npm 에서 package.json, maven 에서 pom.xml 과 같은 역할이라고 보면 될것 같다. bower init 을 하게되면 사실 바로 bower.json 이 생기는 것이 아니라, 여러가지 문답형으로 물어 보는데, 별 다른것은 없고 만약 이전에 bower install 을 이용해서 패키지를 설치 했다면, 설치된 패캐지를 bower.json에 넣을것인지 물어보는데 넣는다고 y를 누르면 dependencies 부분에 아래와 같이 생기게 된다. 

<script src="https://gist.github.com/AhnSeongHyun/cc9857d6333c2a17f8c9.js"></script>

개인적으로는 bower install을 하기 전에 bower init 을 하고 bower install을 할때 아래와 같이 -save 옵션을 줌으로써 bower.json 에 의존성을 기록하게 하는것이 제일 좋은것 같다. 

```
$ bower install jquery -save
```

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>

**bower-installer 사용하기**

앞에서도 언급했지만, ./bower_components 에 패키지들을 다운로드 받아 주는데 문제는 **flask 에서 사용하는 static/css, static/js 가 더 편하기 때문에 어떻게 하면 옮길수가 있을까 했는데  
 bower-installer**라는 것이 있다. 아래와 같이 설치를 하면되는데

```
$ npm install -g bower-installer
```

설치하고 나서 해줘야 할 부분은 다음과 같이 js, css 부분을 static/js, static/css 로 옮긴다는 지정을 bower.json에 아래와 같이 추가 해주어야 한다.

```
“install”: {
  “path”: { 
    “css”: “static/css”, 
    “js”: “static/js” 
  }
```

그리고 나서 아래와 같이 bower-installer를 실행해 준다. ./test 에서 bower.json 이 있는 위치에서 실행해야 한다.

```
$ bower-installer 
```

실행하고 나면 기존의 ./bower_components 는 그대로 있고(삭제되는것이 아니다.) static/js, static/css 에 가보면 하위 디렉토리로 /static/js/bootstrap,/static/js/bootstrap-table, /static/js/jquery 이런식으로 되어있고 그 안에 js 파일이 있는 것을 확인 할 수 있다.


다음에는 **grunt** 를 이용해서 이러한 자바스크립트 파일들은 검증 하거나, 작게 만들거나 하는 식의 작업을 해보도록 하겠다.


**Reference**

– [Grunt와 Bower 를 이용한 웹 프론트엔드 제작하기](https://medium.com/sunhyoups-story/grunt%EC%99%80-bower%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%9B%B9-%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%94%EB%93%9C-%EC%A0%9C%EC%9E%91%ED%95%98%EA%B8%B0-bfa32e6614c1)

– [bower : 웹 프론트앤드 패키지 관리자](http://blog.outsider.ne.kr/933)

