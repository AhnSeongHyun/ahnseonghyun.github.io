---
title: '(vert.x) logging.properties 파헤치기'
author: 'ash84'
pub_date: '2013-05-25'
description: ''
featured_image: ''
tags: ['logging.properties', 'vert.x', 'vert.x 로그 설정', 'vertx logging.properties', 'vertx.log']
---


<span style="font-size: 11pt;">앞선 포스팅에서 logging.properties 를 이용해서 로그파일인 vertx.log 파일의 위치를 변경하였는데 이번에는</span><span style="font-size: 11pt;"> logging.properties내 설정된 다른 항목들을 보도록 하자. </span>

<script src="https://gist.github.com/AhnSeongHyun/5641740.js"></script>

<span style="font-size: 11pt;">JUL 기반으로 되어 있다는 것을 앞서서 애기했는데, 사실 저 설정들은 모두 자바 문서에 명시가 되어 있는 부분이다. </span>

<span style="font-size: 15px; line-height: 29px;">  
</span>

<span style="font-size: 15px; line-height: 29px;">#n : 라인수 </span>

<span style="font-size: 11pt;">**#1 : handlers 부분에 두개의 핸들러, `ConsoleHandler`, `FileHandler` 를 지정하고 있다. **</span>

<span style="font-size: 11pt;">**FileHandler**</span>

<span style="font-size: 11pt;">– 간단한 파일 로깅 핸들러로, 특정 파일에 쓰거나 여러파일에 돌아가면서 쓰는 역할을 한다. 여러 파일에 쓰기 위해서는 각각의 파일에 주어진 사이즈 한계에 도달하면 그 파일을 닫고 새로운 파일을 열어서 쓰는 작업을 수행을 하며, 이때</span><span style="font-size: 11pt;">에는 파일이름에 0, 1, 2 이런식으로 이름이 붙게 된다. 기본적으로 버퍼에 쓰고 각각의 로그 쓰기가 끝나는 시점에 flush가 된다. 기본적인 포맷터는 `XMLFormatter`를 사용하도록 설정되어 있다. </span>

<span style="font-size: 11pt;">– 설정하는 방법 : 기본적으로 각각의 FileHandler 는 아래의` LogManager`설정에 따라서 초기화 된다. 특정하기 지정하지 않으면 기본설정으로 동작한다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">  
</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;">- <span style="font-size: 10pt;">java.util.logging.FileHandler.level : Handler의 로그 레벨 설정 (defaults to </span><span class="s1" style="font-size: 10pt;">Level.ALL</span><span style="font-size: 10pt;">).</span>
- <span style="font-size: 10pt;">java.util.logging.FileHandler.filter : Filter 클래스의 이름 지정 (defaults to no </span><span class="s1" style="font-size: 10pt;">Filter</span><span style="font-size: 10pt;">).</span>
- <span style="font-size: 10pt;">java.util.logging.FileHandler.formatter  </span>
- <span style="font-size: 10pt;">: </span><span class="s1" style="font-size: 10pt;">Formatter</span><span style="font-size: 10pt;"> class 지정 (defaults to </span><span class="s1" style="font-size: 10pt;">java.util.logging.XMLFormatter</span><span style="font-size: 10pt;">)</span>
- <span style="font-size: 10pt;">java.util.logging.FileHandler.encoding  : 캐릭터셋 지정 (defaults to the default platform encoding).</span>
- <span style="font-size: 10pt;">java.util.logging.FileHandler.limit :  하나의 로그파일에 쓸수 있는 최대 로그의 양(바이트기준), 0이면 제한 없음. (defaults to no limit).</span>
- <span style="font-size: 10pt;">java.util.logging.FileHandler.count  :  순환하는 파일의 출력개수 지정. </span><span style="font-size: 10pt;">(defaults to 1).</span>
- <span style="font-size: 10pt;">java.util.logging.FileHandler.pattern  : 로그 파일 이름의 패턴 지정 (d</span><span style="font-size: 10pt;">efaults to “%h/java%u.log”).</span>
- <span style="font-size: 10pt;">java.util.logging.FileHandler.append  :FileHandler를 다른 존재하는 파일에 추가(append)할것인지 설정. (defaults to false)</span>

</div><span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">그 밖에도 `ErrorHandler`, `SocketHandler` 등이 있으니 그건 JavaDoc을 참고하면 될것 같다. </span>

<span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;"></span>

<span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span>

<span class="s2">[<span style="font-size: 11pt;">http://docs.oracle.com/javase/6/docs/api/java/util/logging/package-summary.html</span>](http://docs.oracle.com/javase/6/docs/api/java/util/logging/package-summary.html)</span>

<span style="font-size: 11pt;">**ConsoleHandler**</span>

<span style="font-size: 11pt;">– ConsoleHandler 로그를 System.err 로 내보내는 역할을 하고 기본적으로 SimpleFormatter를 사용한다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;"></span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;">- <span style="font-size: 10pt;">java.util.logging.ConsoleHandler.level specifies the default level for the </span><span class="s1" style="font-size: 10pt;">Handler</span><span style="font-size: 10pt;"> (defaults to </span>[<span class="s2" style="font-size: 10pt;">Level.INFO</span>](http://level.info/)<span style="font-size: 10pt;">).</span>
- <span style="font-size: 10pt;">java.util.logging.ConsoleHandler.filter specifies the name of a </span><span class="s1" style="font-size: 10pt;">Filter</span><span style="font-size: 10pt;"> class to use (defaults to no </span><span class="s1" style="font-size: 10pt;">Filter</span><span style="font-size: 10pt;">).</span>
- <span style="font-size: 10pt;">java.util.logging.ConsoleHandler.formatter specifies the name of a </span><span class="s1" style="font-size: 10pt;">Formatter</span><span style="font-size: 10pt;"> class to use (defaults to </span><span class="s1" style="font-size: 10pt;">java.util.logging.SimpleFormatter</span><span style="font-size: 10pt;">).</span>
- <span style="font-size: 10pt;">java.util.logging.ConsoleHandler.encoding the name of the character set encoding to use (defaults to the default platform encoding)</span>

</div><div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;"></span><span style="font-size: 11pt; line-height: 2;">#2 : `SimpleFormatter` 의 포맷을 지정하는 부분이다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">#3 : ConsoleHandler 의 formatter를 #2에서 지정한  `SimpleFormatter` 로 지정한다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">#4 : ConsoleHandler 의 로그레벨을 INFO로 변경한다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">#5 : FileHandler 의 로그레벨을 INFO로 변경한다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">#6 : FileHandler의 formatter를 `org.vertx.java.core.logging.impl.VertxLoggerFormatter` 로 지정한다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">– `java.util.logging.Formatter` 추상클래스를 상속받는데,  `format()` 함수를 재정의(override) 하고 있다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">– [현재 스레드이름] 시간 로그레벨 [로거이름] 로그메시지 </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">#7 : FileHandler.pattern 을 지정함으로써 경로와 로그파일이름을 지정한다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt; line-height: 1.5;">#10</span><span style="font-size: 11pt; line-height: 1.5;"> : .level 을 INFO로 지정한다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">#11 : org.vertx.level 을 INFO 로 지정한다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">#12 :  com.hazelcast.level=SEVERE로 지정한다. </span>

</div><div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">#10~12 번은 아직 파악이 되지는 않았지만 유추해보기로는 #11는 vertx 자체의 로그 레벨을 지정하는 것으로 보이고, #12은 hazelcast 내 로그 레벨을 지정하는 것으로 보인다. </span></div><div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">logging.properties 에 대해서 조사해봤는데, 추후에 vert.x 를 이용해서 서버를 만들때에도 로그를 처리하는 부분은 반드시 고려되어야 할 부분이라고 생각한다. 하나의 verticle만 돌아가면 상관이 없지만, 여러개가 돌아가는 상황에서는 어떻게 로그형식을 정하고, 위치와 이름을 정하는 것은 필수적인 일이라는 생각이 든다. </span></div><div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">다음에는 log4j, slf4j를 사용하는 방법에 대해서 알아보도록 하겠다. </span></div><div style="text-align: justify; line-height: 2;"></div>

