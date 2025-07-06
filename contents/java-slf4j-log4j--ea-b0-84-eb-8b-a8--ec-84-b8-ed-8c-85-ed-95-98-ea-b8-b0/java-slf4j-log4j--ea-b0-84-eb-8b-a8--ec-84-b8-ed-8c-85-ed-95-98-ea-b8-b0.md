---
title: '[JAVA] slf4j-log4j 간단 세팅하기.'
author: 'ash84'
pub_date: '2015-07-03'
description: '개인적으로 log4j 세팅을 그리 좋아하지 않고, logger 라는것 자체가 좀 싫어하는데 많은 사람들이 사용하고 사실상 회사에서 자바 프로젝트를 하려면 안 쓸수가 없다. 때문에 간략하게 나마 정리를 한다. slf4j를 log4j보다 선호하는 이유는 각자 찾아보길 바란다. ([링크](https://www.google.com/search?q=slf4j%EB%A5%BC+%EC%82%AC%EC%9A%A'
featured_image: ''
tags: ['dev', 'Java', 'Log4J', 'log4j.propertise', 'slf4j']
---


<span style="font-size: 11pt;">개인적으로 log4j 세팅을 그리 좋아하지 않고, logger 라는것 자체가 좀 싫어하는데 많은 사람들이 사용하고 사실상 회사에서 자바 프로젝트를 하려면 안 쓸수가 없다. 때문에 간략하게 나마 정리를 한다. slf4j를 log4j보다 선호하는 이유는 각자 찾아보길 바란다. (</span>[<span style="font-size: 11pt;">링크</span>](https://www.google.com/search?q=slf4j%EB%A5%BC+%EC%82%AC%EC%9A%A9%ED%95%B4%EC%95%BC+%ED%95%98%EB%8A%94+%EC%9D%B4%EC%9C%A0&oq=slf4j%EB%A5%BC+%EC%82%AC%EC%9A%A9%ED%95%B4%EC%95%BC+%ED%95%98%EB%8A%94+%EC%9D%B4%EC%9C%A0&aqs=chrome.0.57.10108&sugexp=chrome,mod=9&sourceid=chrome&ie=UTF-8)<span style="font-size: 11pt;">) </span>

**<span style="font-size: 11pt;">1. 일단 slf4j를 다운 받는다. (</span>[<span style="font-size: 11pt;">링크</span>](http://www.slf4j.org/download.html)<span style="font-size: 11pt;">)</span>**

<span style="font-size: 11pt;">아래의 두 파일을 자바 프로젝트 lib 폴더에 복사하자. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; text-align: justify;"><span style="font-size: 11pt;">– slf4j-api.1.6.1.jar</span>

<span style="font-size: 11pt;">– slf4j-log4j12-1.6.2.jar </span>

</div>**<span style="font-size: 11pt;">2. log4j를 다운 받는다. (</span>[<span style="font-size: 11pt;">링크</span>](http://logging.apache.org/log4j/1.2/download.html)<span style="font-size: 11pt;">)</span>**

<span style="font-size: 11pt;">아래의 파일을 자바 프로젝트 lib 폴더에 복사하자. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; text-align: justify;"><span style="font-size: 11pt;">– log4j-1.2.16.jar</span>

</div><span style="font-size: 11pt;">**3. BuildPath 잡아주기.** </span>

<span style="font-size: 11pt;">다음과 같이 잡아주자. </span>

![](http://ash84.net/wp-content/uploads/1/cfile8.uf.0319413850C17E1F21BF8A.PNG)

<span style="font-size: 11pt;">코드는 다음과 같다. </span>

<script src="https://gist.github.com/4230118.js"><span style="font-size: 11pt;"></script>

<span style="font-size: 11pt;">일단 원래 log4j.propertise 는 src 밑에 두면 되는데, 간혹 안 잡히는 경우가 있다.(log4j의 최고 단점) 이럴경우, 아예 디렉토리를 두고 지정하는 방법도 있음을 보여주기 위해서 PropertyConfigurator 를 사용하였다. log4j.propertise를 만들기 싫다면 BasicConfigurator 를 사용하면 된다. </span>

<span style="font-size: 11pt;">다음은 log4j.propertise 를 보자. 간단하게 만들었다.(초보가 만든것임을 알아주시길..) 인터넷에서 몇가지 더 찾아 보긴 했지만, 기본적으로 console로 나오게 하는 것과 file로 나오게 하는 것 두개에 대해서 설정했다. file로 로그가 나올때는 DEBUG도 출력하도록 설정하였다. </span>

<span style="font-size: 11pt;">  
</span>

<script src="https://gist.github.com/4230138.js"><span style="font-size: 11pt;"></script>

<span style="font-size: 11pt; line-height:2;">log4j의 범위에 대한 부분은 스스로 해보면 알수 있을것이라고 생각된다. 이해하는데는 그리 어렵지 않다. log4j.propertise는 여간 귀찮은 일이 아니지만, 한번쯤 이렇게 정리를 해 두면 편할것이라고 생각되어서 정리해둔다. 추가적으로 위의 3가지 jar에 대한 버전을 제대로 맞춰야 제대로 작동이 된다. 단순히 logger.info(“”)함수로 테스트하는 것 보다 logger.info(“{}”) 함수로 테스트 하길 권장한다. </span>



