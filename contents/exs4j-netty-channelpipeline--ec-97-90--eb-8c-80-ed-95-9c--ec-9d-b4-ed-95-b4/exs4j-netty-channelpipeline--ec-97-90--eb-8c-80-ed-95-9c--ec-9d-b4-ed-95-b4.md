---
title: '(exs4j) Netty ChannelPipeline 에 대한 이해.'
author: 'ash84'
pub_date: '2013-03-08'
description: '현재 개발하고 있는 [exs4j](https://github.com/AhnSeongHyun/exs4j) 에서는 네트워크 파트는 전적으로 [Netty](http://netty.io)가 담당하고 있다. 이유는 여러가지가 있겠지만 쉽게  서버를 구성할 수 있고 pipeline을 변경함에 따라 HTTP 통신 방식도 지원할 수 있기 때문이다.(v1.6 지원예정) [Netty ](http://netty.io)에서 여러가지 예제를 제공하고 있기 때문에 쉽게 따라 할수 있는데 필자 역시 따'
featured_image: ''
tags: ['ChannelPipeline', 'ChannelPipelineFactory', 'espressoOtr', 'exs4j', 'GitHub', 'Netty']
---
<span style="font-size: 11pt;">현재 개발하고 있는 [exs4j](https://github.com/AhnSeongHyun/exs4j) 에서는 네트워크 파트는 전적으로 [Netty](http://netty.io)가 담당하고 있다. 이유는 여러가지가 있겠지만 쉽게  서버를 구성할 수 있고 pipeline을 변경함에 따라 HTTP 통신 방식도 지원할 수 있기 때문이다.(v1.6 지원예정) [Netty ](http://netty.io)에서 여러가지 예제를 제공하고 있기 때문에 쉽게 따라 할수 있는데 필자 역시 따라 하면서 배우고 적용하고 있는 중이다. </span>

<script src="https://gist.github.com/AhnSeongHyun/5114409.js"></script>

<span style="font-size: 11pt;">위의 코드는 [exs4j](https://github.com/AhnSeongHyun/exs4j) 서비스 부분의 JsonPipelineFactory 에 있는 코드인데, Json 디코딩과 엔코딩을 위한 decoder와 encoder 그리고 framer, handler 를 ChannelPipeline 에 설정하고 있다. 다음의 코드를 보자</span>

<script src="https://gist.github.com/AhnSeongHyun/5114413.js"></script>

<span style="font-size: 11pt;">이 코드는 Netty의 HttpSnopServer 라는 예제를 이용해서 Http 통신을 지원하기 위한 pipeline 을 구성하는 코드이다. 보시면 decoder, encoder, deflater, handler를 지정하고 있다. </span>

<span style="font-size: 11pt;">그냥 쓰면 되는것을** 한가지 의문**이 들었는데, **Netty 내부에서는 저 decoder, encoder 들이 통신상의 read(), write()시 동작을 해야할텐데 도데체 어떻게 동작을 하는 것일까? 하는 생각이 들었다. decoder, encoder라는 이름이 혹시 어떤 키값이 되어서 read()를 하면 decoder 라는 이름으로 저장된 객체를 읽어와서 수행하는것인가? 그렇다면 handler, framer, deflater는 또 모지?**</span>

<span style="font-size: 11pt;">여러 의문을 풀고자[ Netty 3.6 API](http://netty.io/3.6/api/) 문서를 살펴보았다. 정리하자면 이렇다. **(의역, 오역이 있을수 있음을 인정한다.)**</span>

<span style="font-size: 11pt;">**  
**</span>

<span style="font-size: 11pt;">**ChannelPipeline**</span>

<span style="font-size: 11pt;">정의 : ChannelHandler 의 리스트. </span>

<span style="font-size: 11pt;">역할 : 네트워크 상의 흐름을 가로채거나 해서 처리한다. </span>

<span style="font-size: 11pt;">**특징 **</span>

<span style="font-size: 11pt;">– Intercepting Filter Pattern 에 의해서 구현되어 있다. </span>

<span style="font-size: 11pt;">– 이것을 이용해서 전체를 제어할수 있다. </span>

<span style="font-size: 11pt;">**사용법**</span>

<span style="font-size: 11pt;">– Channel에 ChannelPipeline을 붙여야 한다. </span>

<span style="font-size: 11pt;">– 일단 한번 붙이면 Channel과 pipeline 이 영구적으로 결합된다. </span>

<div style="line-height: 2;"><span style="font-size: 11pt;">– Channel은 현재 붙은 ChannelPipeline을 떼어내지 않으면 다른것을 붙일수 없다.</span></div><div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;"></span>

서버가 데이터를 받을때 : UpStream : receive, socket.read(), inBoundData 

<div><span style="font-size: 11pt;">서버가 데이터를 보낼때 : DownStream : send, socker.write(), outBoundData </span></div></div><div></div><div><script src="https://gist.github.com/AhnSeongHyun/5114437.js"></script></div><div><span style="font-size: 15px; line-height: 22px;">  
</span></div><div></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">데이터를 받는다고 하면 1, 2, 5 가 호출된다. 그리고 데이터를 보낸다고 하면 4, 3이 호출이 된다. ChannelPipeline 에 등록해 놓은 것에 대한 구분은 해당 클래스가 UpStreamHandler 를 구현했는지, DownStreamHandler를 구현했는 지에 의해서 결정된다. 그런데 만약 5번 핸들러에서UpStreamHandler , DownStreamHandler 를 모두 구현하였다면, 125, 543 순으로 호출된다. </span></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">  
</span></div><div></div><div style="text-align: justify;"><span style="font-size: 11pt;">실제로 Netty의 예제에서 많이 나오는 SimpleChannelHandler 는 둘 다를 구현하고 있다. </span></div><div></div><div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><div><span style="font-size: 10pt;">public class SimpleChannelHandler implements ChannelUpstreamHandler, ChannelDownstreamHandler {…}</span></div></div><div></div><div></div><span style="font-size: 11pt;">****</span>

Building a Pipeline

<div></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">Request, Receive I/O Event 를 처리 할 때 여러가지 핸들러를 쓰게 된다. 전형적인 서버는 아래와 같은 핸들러들을 가지고 있을 것이다. (물론, 프로토콜이나 비지니스 로직에 따라 약간씩 다를듯) </span></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">  
</span></div><div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><div></div><div><span style="font-size: 11pt;">Protocol Decoder – 받은 바이너리 데이터(ChannelBuffer)를 해석해서 자바 오브젝트로 변경</span></div><div></div><div><span style="font-size: 11pt;">Protocol Encoder – 보낼 Java 오브젝트를 프로토콜 데이터(ChannelBuffer) 로 변경</span></div><div></div><div><span style="font-size: 11pt;">ExecutionHandler – applies a thread model</span></div><div></div><div><span style="font-size: 11pt;">Business Logic Handler – </span><span style="font-size: 11pt; line-height: 2;">실제 비지니스 로직을 수행할 핸들러 </span></div></div><div><span style="font-size: 9pt; line-height: 2;">  
</span></div><div><span style="font-size: 9pt; line-height: 2;">  
</span></div><div><span style="font-size: 9pt; line-height: 2;">  
</span></div><div><span style="font-size: 11pt; line-height: 1.5;">**Thread Safety**</span></div><div style="line-height: 2;"><span style="font-size: 9pt; line-height: 2;">  
</span></div><div style="line-height: 2; text-align: justify;"><span style="font-size: 11pt; line-height: 2;">ChannelHandler 는 언제든지 추가와 삭제가 가능하다. 왜냐하면 ChannelPipeline은 스레드에 안전하기 때문이다. 한예로, 중요한 정보의 교환시 SslHandler 를 추가할수 있고 교환후에 삭제 할 수도 있다.</span></div><span style="font-size: 11pt;">[Netty 3.6 API](http://netty.io/3.6/api/) 문서에 있는 ChannelPipeline 에 대한 내용을 위에 적었는데 이것 외에도 pitfall 이라고 해서 ‘위험’적인 부분에 대해서 설명해 놓은 부분도 있으니 참고해서 보면 좋을것 같다.(필자는 잘 이해가 안되었음)</span>

<span style="font-size: 11pt;">문서를 통해서 품고 있었던 ChannelPipeline 에 대한 의문점을 풀게 되었다. 정리를 하자면 아래와 같다. </span>

<span style="font-size: 11pt;"> </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">**ChannelPipeline addLast() 함수를 통해서 추가될때 붙여지는 이름과 데이터 송수신 사이에서의 관계는 없으며 그 관계는 addLast() 함수를 통해서 ChannelHandler 객체가 UpStreamHandler 를 구현했느냐 DownSteramHandler 를 구현 했느냐에 따라서 결정된다. **</span>

</div><div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;">**<span style="font-size: 11pt;">handler, framer, deflater 로 설정한 ChannelHandler 역시 </span><span style="font-size: 11pt; line-height: 2;">UpStreamHandler, </span><span style="font-size: 11pt; line-height: 2;">DownSteramHandler</span>**<span style="font-size: 11pt; line-height: 2;">** 둘중 하나 혹은 둘다를 구현하고 있는 경우이다. 둘다를 구현하는 경우, 송수신시 모두 추가한 순서에 포함되어 수행되어 진다. **</span>

</div>

