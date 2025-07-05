---
title: '(vert.x) mod-sample을 이용한 module 만들기'
author: 'ash84'
pub_date: '2013-05-22'
description: ''
featured_image: ''
tags: ['modulle 만들기', 'runmod', 'vert.x', 'vert.x mod']
---


<span style="color: rgb(51, 51, 51); font-size: 11pt;">[지난 포스팅](http://ash84.tistory.com/969)에서 vert.x module을 mod-sample 이라는 잘 만들어진 어떤 것을 이용해서 간단하게 나마 테스트 해보는 시간을 가졌었다. 여러가지 설정을 해야하는데 gradle(나중에 따로 다뤄야 할듯)</span><span style="color: rgb(51, 51, 51); font-size: 11pt;"> 등등 그런 작업들을 쉽게 할수 있도록 구성 된것으로 이번에는 실제로 간단한 모듈을 만드는 작업을 해보았다. </span>

<span style="color: rgb(51, 51, 51); font-size: 11pt;">테스트로 몰 만들면 좋을까 생각을 하다가, **<span style="color: rgb(152, 0, 0);">uri를 파싱해서 json 형태로 반환해주는 것</span>**이 어떨까 하는 생각을 가졌다. 예를 들어, 아래와 같은 결과를 보여주는 것이다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="color: rgb(51, 51, 51); font-size: 11pt;">http://localhost:9090/request?query=vertx&</span><span style="color: rgb(51, 51, 51); font-size: 11pt;">count=10</span>

</div><div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 10pt; font-family: Dotum, 돋움;"><span style="font-size: 11pt;">{ "count" : "10", "query" : "vertx" }</span></span>

</div><span style="font-size: 11pt;">일단 기존의 mod-sample 내에 `indf.json` 이라는 패키지를 만들었고, `Verticle` 클래스를 상속 받는 `JsonVertxModule` 클래스는 만들었다. `Verticle` 클래스는 아래와 같이 추상클래스로 되어 있고 추상 메소드인 `start()`함수를 재정의 하도록 되어 있다. </span>

<span style="font-size: 11pt;">  
</span>

<script src="https://gist.github.com/AhnSeongHyun/5624812.js"></script>

<span style="font-size: 11pt; line-height: 2;">JsonVertxModule 클래스는 재정의 하는 </span>`start()`<span style="font-size: 11pt; line-height: 2;"> 함수를 가지고 있다. 이 함수에서는 제일 처음 </span>`HttpServer`<span style="font-size: 11pt; line-height: 2;"> 객체를 </span>`vertx.createHttpServer()`<span style="font-size: 11pt; line-height: 2;"> 함수로 만든다. 그리고 나서 핸들러를 만들어야 한다. </span>`server.requestHandler()`<span style="font-size: 11pt; line-height: 2;">함수를 통해서 만든 핸들러를 넣어주면 되는데, 이때 익명 클래스로 만들어도 되고, 본 예제처럼 따로 클래스를 빼서 만들어도 된다. 간단한 것이라면 익명 클래스를 만드는 것을 추천한다. </span>

<span style="font-size: 11pt;">  
</span>

<script src="https://gist.github.com/AhnSeongHyun/5624814.js"></script>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">Http의 요청을 받는데 사용되는 `HttpServerRequest` 클래스의 `Handler` 클래스인 `UriToJsonHandler` 클래스를 만들고 내부적으로 해당 클래스는 Handler Interface 를 구현해야 하는데 `handle()` 함수를 작성하면 된다. `HttpServerRequest` 를 제네릭 인자로 설정했기 때문에 `handle()` 함수의 인자로 `HttpServerRequest` 객체를 받을수가 있다. </span>

<span style="font-size: 11pt;">  
</span>

<script src="https://gist.github.com/AhnSeongHyun/5624819.js"></script>

 handle(HttpServerRequest request)함수에서는 말 그대로 uri를 파싱해서 json 문자열로 변환하는 작업을 수행한다. 파싱하는 부분은 크게 어렵지 않기 때문에 생략하기로 하는데 json을 만들때에는 jackson 라이브러리를 사용하였다. jsonStr 을 만들고 나면 이제 클라이언트에게 보내주어야 한다. `request.response` 객체는 `HttpServerResponse` 클래스의 객체인데 `end(String chunk)` 함수를 이용해서 json 문자열을 보내는 작업을 하고 있다.

<span style="font-size: 11pt;">그렇게 핸들을 설정하고나서 `server.listen(port)` 함수를 이용해서 서버를 시작해 주면 된다.</span>

<span style="font-size: 11pt;">코드자체는 몇줄 없어서 크게 어렵지 않다. mod.json 이 mod-sample 내` /src/main/conf`에 위치하고 있고 이 안에는 json 의 형태로 main을 설정해 주도록 되어 있을것이다. 모듈이 변경 되었기 때문에 새로운 모듈로 변경해 주자. **패키지명.클래스명**을 적어주면 된다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">{</span>

<span class="Apple-tab-span" style="font-size: 11pt;"></span><span style="font-size: 11pt;">“main”: “indf.json.JsonVertxModule”</span>

<span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;"></span>

<span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">}</span>

</div><span style="font-size: 11pt;">그리고 나서 해야하는 작업은 `gradle.properties` 를 수정하는 작업이다. 일종의 빌드를 위한 세팅이라고 보면 되는데, 아래와 같이 세팅을 하였다. modulename + version 의 이름로 빌드후,` build/mod/` 아래에 디렉토리가 생성된다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><u>**<span class="s1" style="font-size: 11pt;">modulename=</span><span style="font-size: 11pt;">indf.json.mod-sample</span>**</u>

<span style="font-size: 11pt;">version=</span><span class="s2" style="font-size: 11pt;">0.1</span>

<span style="font-size: 11pt;">gradleVersion=</span><span class="s2" style="font-size: 11pt;">1.1</span>

<span class="s1" style="font-size: 11pt;">vertxVersion=</span><span style="font-size: 11pt;">1.2.0-SNAPSHOT</span>

<span style="font-size: 11pt;">junitVersion=</span><span class="s2" style="font-size: 11pt;">4.10</span>

<span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;"></span>

<span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">rhinoVersion=</span><span class="s2"><span style="font-size: 11pt;">1.7R4</span>  
</span>

</div><span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">빌드는 mod-sample내 `mk`를 이용하면 되는데 `mk clean dist`명령을 통해서 진행하면 된다. 관련사항은 [여기를](http://whiteship.me/?p=13619) 참고하시면 된다. 빌드를 하게 되면 `build/mod/indf.json.mod-sample-v0.1` 이렇게 디렉토리가 생성되는 것을 볼 수가 있다. 일단 이렇게 하면 빌드가 끝난것인데, vertx 가 path가 잡혀있다는 가정하에, 테스트 하길 원하는 디렉토리에 mods 라는 디렉토리를 만들고 그 안에 </span><span style="font-size: 11pt; line-height: 1.5;"> </span><span style="font-size: 11pt; line-height: 1.5;">`build/mod/indf.json.mod-sample-v0.1` 디렉토리를 복사해 넣으면 된다. </span>

<span style="font-size: 9pt; line-height: 1.5;">  
</span>

<span style="font-size: 11pt; line-height: 1.5;">그리고 나서 서버 실행은 아래와 같이 하면 된다. </span>

<span style="font-size: 11pt; line-height: 1.5;">  
</span>

<span style="font-size: 9pt; line-height: 1.5;">  
</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">> vertx runmod indf.json.mod-sample-v0.1</span>

</div><span style="font-size: 11pt;">생각보다 어렵진 않다. mod-sample 덕분이라고 말하고 싶다. 권장하는 부분은 mk clean dist 와 디렉토리 복사하는 부분을 스크립트로 만들어서 사용하는 편이 개발하거나 테스트할때 편하다는 생각이 든다. 물론 이클립스랑 연동이 쉭쉭 되면 좋겠지만. </span>

<span style="font-size: 11pt;">서버를 실행하면 서버 실행 메시지가 뜨게 될것이다. 그리고 나서 웹 브라우저 창에 위의 예제 url을 한번 입력해 보면 json 문자열 형태로 변환이 되어서 나오는 것을 확인할 수가 있다. </span>

 

<span style="font-size: 11pt;">  
</span>

<span class="s2">  
</span>



