---
title: '(vert.x) verticle에 설정 전달하기'
author: 'ash84'
pub_date: '2013-05-28'
description: 'Verticle을 상속받는 클래스를 만들어야 mod 의 형태나, 일반 파일의 형태로 전달해서 띄우던지 할수가 있는데, Verticle 클래스에서는 `container`라는 객체가 있다. 이 객체가 하는 일은 말 그대로 어떤 것을 담고 있는 클래스인데, 가장 중요한것이 앞서서 말한 logger 이고, 다른 하나는 conf 이다.'
featured_image: ''
tags: ['vert.x', 'vert.x config', 'vert.x settings']
---


<span style="font-size: 11pt;">Verticle을 상속받는 클래스를 만들어야 mod 의 형태나, 일반 파일의 형태로 전달해서 띄우던지 할수가 있는데, Verticle 클래스에서는 `container`라는 객체가 있다. 이 객체가 하는 일은 말 그대로 어떤 것을 담고 있는 클래스인데, 가장 중요한것이 앞서서 말한 logger 이고, 다른 하나는 conf 이다. </span>

<span style="font-size: 11pt;">  
</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">vertx runmod $MOD_NAME -conf ./conf/vas.conf</span>

</div><span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">vert.x에서는 -conf옵션을 통해서 설정 파일을 줄수가 있다. 이렇게 준 설정파일은 `container.getConfig()` 함수를 통해서 json 형태로 값으로 원하는 설정을 가져올수 있다. 즉, 파일 역시 json 형태로 되어 있어야 하고, vertx 구동시 -conf 옵션으로 해당 파일경로를 전달하면 내부적으로 json파싱을 통해서 org.vertx.java.core.json.JsonObject를 받게 된다. 본 객체를 </span><span style="font-size: 11pt;"> 이용해서 key 값을 전달하면 value 를 받게 되는 것이고, 그 값을 설정으로 이용하면 된다. </span>

<span style="font-size: 11pt;">아래의 예제를 보자. host, ip, serverName 을 json 파일에서 지정 하였다. </span>

<script src="https://gist.github.com/AhnSeongHyun/5657740.js"></script>

<span style="font-size: 11pt;">그리고 나서 코드를 수정하였다.`container.getConfig()` 함수에서 JsonObject 를 가져와서 필요한 키를 전달하고 그에 대한 값을 저장하였다. 그리고 나서 저장된 값으로 서버를 구동시킬때 사용하였다. </span>

<script src="https://gist.github.com/AhnSeongHyun/5657744.js"></script>

<span style="font-size: 11pt;">생각보다 -conf 로 전달한다는 것, 그리고 json 형식으로 파일이 되어있다는 점만 기억한다면 그리 어렵지 않을것이라고 생각된다. </span>



