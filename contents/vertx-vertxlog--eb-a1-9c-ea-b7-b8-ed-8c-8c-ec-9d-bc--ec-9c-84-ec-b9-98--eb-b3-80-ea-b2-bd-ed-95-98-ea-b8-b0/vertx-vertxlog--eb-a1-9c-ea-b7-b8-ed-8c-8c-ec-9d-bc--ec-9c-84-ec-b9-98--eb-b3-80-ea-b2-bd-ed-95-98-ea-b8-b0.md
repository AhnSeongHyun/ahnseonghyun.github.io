---
title: '(vert.x) vertx.log 로그파일 위치 변경하기'
author: 'ash84'
pub_date: '2013-05-24'
description: ''
featured_image: ''
tags: ['logging.properties', 'set vert.x log', 'vert.x', 'vert.x 로그 설정', 'vertx', 'vertx.log']
---


<span style="font-size: 11pt;">vert.x 로그에 대한 내용은 [여기](http://vertx.io/manual.html#logging)를 참고를 하면 된다. 요약하자면 </span>

> <span style="font-size: 9pt;">각각의 verticle 은 자신의 logger를 가지는데, verticle 내부에서 가져와서 사용할 수가 있다. </span><span style="font-size: 9pt;">로그 파일은 기본적으로 vertx.log 파일로 기록이 되고, system temp 디렉토리에  
>  남겨지게 된다. </span>
> 
> 기본적으로 JUL(j<span style="font-size: 9pt;">ava.u</span><span style="font-size: 9pt;">til.l</span><span style="font-size: 9pt;">ogging)</span><span style="font-size: 9pt;">을 사용한다. 이것은  
>  $VERTX_HOME(설치한 위치)</span><span style="font-size: 9pt;">\conf\logging.properties 파일을 이용해서 설정할수가 있다. </span>

<span style="font-size: 11pt;">이렇게 요약을 할 수 있는데, 사용하는 부분은 본 포스팅의 아랫 부분에서 설명하기로 하고 일단 위의 설명에서 보면 system temp 디렉토리에 vert.x 로그 파일이 출력된다고 되어 있는데, OSX 기준으로 /tmp 폴더에 생겨야 하는 파일은 사실은 find 명령어로 찾아 보면 아래의 위치에서 나오고 있다. </span>

<span style="font-size: 11pt;">  
</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">//private/var/folders/3g/6p12cfy948596gcy2ch0frsc0000gn/T/vertx.log</span>

</div><span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">완전 듀스상태다. **저긴 또 어딘데 왜 로그파일이 저기 생길까?** 내가 원하는것은 현재 vert.x 가 실행되는 디렉토리 아래의 logs 폴더 내에 생기거나 혹은 사용자 디렉토리 내에 쓰기를 원하는데 말이다. </span>

<span style="font-size: 11pt;">이러한 부분의 수정을 위해서는 위에 요약한것 처럼 vertx.log 파일의 설정을 조절할 수 있는 </span><span style="font-size: 11pt; line-height: 1.5;">$VERTX_HOME(설치한 위치)</span><span style="font-size: 11pt; line-height: 1.5;">\conf\logging.properties 를 살펴봐야 한다. logging.properties 파일을 열면 아래와 같은 내용이 출력된다. </span>

<span style="font-size: 9pt; line-height: 2;">  
</span>

<span style="font-size: 9pt; line-height: 2;">  
</span>

<script src="https://gist.github.com/AhnSeongHyun/5641740.js"></script>

<span style="font-size: 9pt; line-height: 2;">  
</span>

<span style="font-size: 9pt; line-height: 2;">  
</span>

<span style="font-size: 11pt; line-height: 2;">vert.x 에서는 기본적으로 [JUL](http://docs.xrath.com/java/se/6/docs/ko/api/java/util/logging/package-summary.html) [(](http://docs.xrath.com/java/se/6/docs/ko/api/java/util/logging/package-summary.html)</span>[j](http://docs.xrath.com/java/se/6/docs/ko/api/java/util/logging/package-summary.html) [ava.u](http://docs.xrath.com/java/se/6/docs/ko/api/java/util/logging/package-summary.html) [til.l](http://docs.xrath.com/java/se/6/docs/ko/api/java/util/logging/package-summary.html) [ogging](http://docs.xrath.com/java/se/6/docs/ko/api/java/util/logging/package-summary.html)<span style="font-size: 11pt; line-height: 2;"><span style="font-size: 11pt;">[)](http://docs.xrath.com/java/se/6/docs/ko/api/java/util/logging/package-summary.html)</span>을 사용하는데 해당 부분에 대한 java doc을 참고하면 더 많은 정보를 얻을수가 있다. 다양한 설정들이 있지만 일단은 내가 원하는 위치에 vertx.log 파일을 생성하기 위해서는 `java.util.logging.FileHandler.pattern`부분을 수정해야 한다. 해당 부분을 보면 vertx.log 앞에 **%t 라고 쓰여져 있는데 이것을 일종의 예약어** 같은 것으로 아래와 같은 의미를 가지고 있다. </span>

<span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;"></span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;">- <span style="font-size: 11pt;">“/” the local pathname separator</span>
- <span style="font-size: 11pt;">“%t” the system temporary directory</span>
- <span style="font-size: 11pt;">“%h” the value of the “user.home” system property</span>
- <span style="font-size: 11pt;">“%g” the generation number to distinguish rotated logs</span>
- <span style="font-size: 11pt;">“%u” a unique number to resolve conflicts</span>
- <span style="font-size: 11pt;">“%%” translates to a single percent sign “%”</span>

</div><span style="font-size: 11pt;">**%t는 system tempor**</span><span style="font-size: 11pt;">**ary(시스템 임시) 디렉토리를 의미**한다. 예약어를 적극적으로 활용하면 로그파일의 겹침이나 연속된 로그파일 이름을 명시하는 것이 가능할 것으로 보인다. 여기서는</span>

<span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;"></span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">java.util.logging.FileHandler.pattern=./logs/vertx.log</span>

</div><span style="font-size: 11pt;">  
아래와 같이 설정을 한후, [이전 포스팅](http://ash84.tistory.com/974)의 `JsonVertxModule` 내 `start()`함수에서 기존의 `System.out.println()` 을 이용하던 부분 대신에 `container.getLogger()` 함수를 이용해서 logger를 가져와서 다음과 같이 같은 서버 시작 메시지를 남기도록 하였다. </span>

<script src="https://gist.github.com/AhnSeongHyun/5641780.js"></script>

<span style="font-size: 11pt;">`container`는 Verticle 클래스의 멤버 변수이다. `getLogger()` 를 통해서 로그를, `getConfig()` 를 통해서 설정을 가져올수가 있게 되어 있다. `JsonVertxModule` 클래스가 Verticle 클래스를 상속 받기 때문에 이것이 가능한 것이고, 본 글의 제일 앞 부분에서 언급했던 각각의 verticle 이 자기자신의 logger를 가져올수 있다는 부분이 `container.getLogger()`를 이야기 하는 것이다 .</span>

<span style="font-size: 11pt;">테스트를 해보면 다음과 같이 실행된 위치에 logs 디렉토리 내에 vertx.log 가 생기는 것을 볼 수 있다. 이때에 당연히 logs 디렉토리가 없으면 에러가 발생되게 된다.</span>

<figure class="wp-caption aligncenter" style="width: 640px">![](http://ash84.net/wp-content/uploads/1/cfile26.uf.034E4C3A519F1567196E10.png)<figcaption class="wp-caption-text">클릭해서 보기 </figcaption></figure>

<span style="font-size: 11pt;">logging.properties 에 다른 부분들은 [JUI](http://docs.xrath.com/java/se/6/docs/ko/api/java/util/logging/package-summary.html)에 대한 부분이기 때문에 자바 문서를 한번 보는 것이 필요하다고 생각한다. 다음 포스팅에서 [logging.properties 내 다른 ](http://ash84.tistory.com/978) [JUI](http://ash84.tistory.com/978) [다른 설정들이 의미하는 것](http://ash84.tistory.com/978)과 그리고 log4j, slf4j 등의 다른 로거들을 사용하려면 어떻게 해야하는지 알아보도록 하겠다. </span>



