---
title: '(vert.x) JUL 대신에 slf4j-log4j 사용하기.'
author: 'ash84'
pub_date: '2013-05-27'
description: 'log 관련 이전 포스팅을 일단 언급하자면 아래와 같다. 
[vertx.log 파일 위치 변경하기](http://ash84.tistory.com/976)
[logging.properties 파헤치기](http://ash84.tistory.com/978) 
위의 포스팅에서'
featured_image: ''
tags: ['vert.x log4j', 'vert.x slf4j', 'vertx', 'vertx slf4j', 'vertx.log']
---


<span style="font-size: 11pt;">log 관련 이전 포스팅을 일단 언급하자면 아래와 같다. </span>

<span style="font-size: 11pt;">[vertx.log 파일 위치 변경하기](http://ash84.tistory.com/976)</span>

<span style="font-size: 11pt;">[logging.properties 파헤치기](http://ash84.tistory.com/978) </span>

<span style="font-size: 11pt;">위의 포스팅에서 설명했듯이 vert.x는 기본적으로 JUL(java.util.logging)을 사용하고 있는데 메뉴얼에 나와있는것 처럼 log4j, slf4j 를 사용할 수 있다. 보통 slfj4-log4j를 많이 사용하기 때문에 slf4j 를 연동해보았다. </span>

<span style="font-size: 11pt;">메뉴얼에 나와있는것처럼, 아래의 부분을 일단 vertx.sh(vertx.bat) 에 마지막 java 옵션을 주는 부분에 추가하자. </span>

<script src="https://gist.github.com/AhnSeongHyun/5656736.js"></script>

<span style="font-size: 11pt;">이렇게 설정을 한 후, 반드시 해주어야 할 부분은 slf4j 버전에 해당하는 jar 파일을 $VERTX_HOM/lib 에 추가해야 한다. 그렇지 않으면 slf4j 클래스를 찾지 못해서 예외가 발생하게 된다. log4j 버전에 해당하는 jar파일을 같은 곳에 위치시킨다. 실행해 보면 다음과 같은 메시지를 볼 수가 있다. </span>

<figure class="wp-caption aligncenter" style="width: 640px">![](http://ash84.net/wp-content/uploads/1/cfile21.uf.015EEC3D51A34FEC2CAE0F.png)<figcaption class="wp-caption-text">안보인면 클릭</figcaption></figure>

<span style="font-size: 11pt; line-height: 2;">메시지에 있는 사이트에 가면 좀더 정확한 정보를 얻을수가 있다. 저런 메시지가 뜨는 이유는 아래와 같다.</span>

<span style="font-size: 11pt; line-height: 2;"> </span>

> ### Failedto load class `<code style="font-family: Courier, monospace;">org.slf4j.impl.StaticLoggerBinder`
> 
> This error is reported when the `<code style="font-family: Courier, monospace;">org.slf4j.impl.StaticLoggerBinder` class could not be loaded into memory. This happens when no appropriate SLF4J binding could be found on the class path. Placing one (and only one) of *slf4j-nop.jar*, *slf4j-simple.jar*, *slf4j-log4j12.jar*, *slf4j-jdk14.jar* or *logback-classic.jar* on the class path should solve the problem.
> 
> <span class="label" style="padding: 1px 3px 2px; font-size: 9.75px; font-weight: bold; color: rgb(255, 255, 255); text-transform: uppercase; white-space: nowrap; background-color: rgb(191, 191, 191); border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;">SINCE 1.6.0</span> As of SLF4J version 1.6, in the absence of a binding, SLF4J will default to a no-operation (NOP) logger implementation.
> 
> You can download SLF4J bindings from the project [download page](http://www.slf4j.org/download.html).

<div></div><div></div><span style="font-size: 11pt;"></span><span style="font-size: 11pt;"></span><span style="font-size: 11pt;">해석해 보면 **적절한 sfl4j 바인딩이 안되었기 때문인데, slf4j-nop.jar, slf4j-simple.jar, slf4j-log4j12.jar, slf4j-jdk14.jar 중에 하나가 classpath에 위치해 있어야 한다는 것이다.** slf4j-log4j 를 이전에 java 에서 사용해 보신분들이라면 금방 알것이다. 위의 다운로드 페이지 부분에 들어가서 slf4j에 맞는 slf4j-log4j12.jar를 다운받아서 같은 디렉토리에 위치시켰다. 그래서</span><span style="font-size: 11pt;"> slf4j-log4j 를 위해서 필요한 jar는 아래의 3가지이다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">– slf4j-api-1.6.2.jar</span>

<span style="font-size: 11pt;">– log4j-1.2.16.jar</span>

<span style="font-size: 11pt;">– slf4j-log4j12-1.6.2.jar</span>

</div><span style="font-size: 11pt;">일단 이렇게 하면 실행시켰을때 별다른 문제는 생기지 않는다. **<span style="color: rgb(204, 61, 61);">그런데 생각해 보면 logging.properties는 JUL 을 위해서 설정했던 부분인데, slf4j-log4j 를 위해서도 설정이 필요하지 않을까?</span>** logging.properties 를 인식하지 못하기 때문에 실행디렉토리/logs/vertx.log 가 생기지 않는다. </span>

<span style="font-size: 11pt;">늘상 log4j.properties 를 만들어서 썼던것 처럼 하나를 만들고, vertx.sh(vertx.bat) 파일안에서 기존의 logging.properties 를 지정했던 부분에 만든 log4j.properties 를 지정해 주자. </span>

<script src="https://gist.github.com/AhnSeongHyun/5656777.js"></script>

<span style="font-size: 11pt;">log4j.properties 에 vertx.log대신에 dailyLog.log 라는 파일에 쓰라고 명시해두었다. 다시 실행시켜보자. 아래와 같이 logs 아래에 dailyLog.log 가 생서되고 로그내용이 출력되는것을 볼 수 있다. </span>

 

<figure class="wp-caption aligncenter" style="width: 640px">![](http://ash84.net/wp-content/uploads/1/cfile23.uf.27022A3D51A3505C0F9966.png)<figcaption class="wp-caption-text">안보이면 클릭.</figcaption></figure>

<span style="font-size: 11pt;">log 에 대한 부분은 JUL이 불편하다면 기존의 여러 오픈소스 프로젝트에서 많이 쓰는 slf4j-log4j를 사용하는 것도 그리 어렵지 않게 vert.x에서는 지원하고 있다. </span><span style="font-size: 11pt;"> </span>

<span style="font-size: 11pt;"> </span>

<div></div><div></div>

