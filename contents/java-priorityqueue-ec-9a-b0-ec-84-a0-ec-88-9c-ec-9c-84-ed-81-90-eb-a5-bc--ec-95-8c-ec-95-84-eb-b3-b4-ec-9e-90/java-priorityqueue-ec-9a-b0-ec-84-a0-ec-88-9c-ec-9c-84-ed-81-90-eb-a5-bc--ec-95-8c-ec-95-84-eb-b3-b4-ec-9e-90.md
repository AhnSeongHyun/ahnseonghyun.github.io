---
title: '[Java] PriorityQueue(우선순위큐)를 알아보자.'
author: 'ash84'
pub_date: '2013-01-03'
description: '일반적인 큐(Queue)는 선입선출(FIFO)의 구조를 가진다는 것은 다들 아시고 있을 것이라고 생각된다. 그렇다면 PriorityQueue 는 일반적인 큐와 어떻게 다를까? 

PriorityQueue는 내부적으로 Natural Ordering 에 따라서 정렬하는 큐이다. 그래서 다음의 코드를 테스트 해보면 당연히 10이라는 숫자가 나와야 하는데, 실제로는 1이라는 숫자가 나오는 것을 확인 할수 있다. 



또 다른 예를 보자'
featured_image: ''
tags: ['dev', 'Java', 'PriorityQueue', 'queue', '우선순위 큐', '태그를 입력해 주세요.']
---

일반적인 큐(Queue)는 선입선출(FIFO)의 구조를 가진다는 것은 다들 아시고 있을 것이라고 생각된다. 그렇다면 PriorityQueue 는 일반적인 큐와 어떻게 다를까? 

PriorityQueue는 내부적으로 Natural Ordering 에 따라서 정렬하는 큐이다. 그래서 다음의 코드를 테스트 해보면 당연히 10이라는 숫자가 나와야 하는데, 실제로는 1이라는 숫자가 나오는 것을 확인 할수 있다. 

<script src="https://gist.github.com/4432167.js"></script>

또 다른 예를 보자. 아래와 같이 무작위로 숫자 값을 넣었을 경우에는 어떻게 될까?

<script src="https://gist.github.com/4432175.js"></script>

ASC Ordering 된 상태로 출력되는것을 확인 할수 있을것이다. 이것이 가장 큰PriorityQueue의 특징이다. PriorityQueue는 널을 허용하지 않는다. 왜냐하면 PriorityQueue는 기반 자체가 natural ordering에 기초하고 있기 때문에 정렬할수 없는 null은 허용되지가 않는다.

PriorityQueue의 head는 가장 적은 값이 온다. 만약 다수의 엘리먼트가 가장 적은값이라면, 헤드는 그 중에 하나가 되는데 어떤것이 될지는 모른다. 

**메소드들**

<div style="color: rgb(0, 0, 0); font-family: 나눔고딕; line-height: 2; font-size:12pt;"><div><div></div><div><table align="justify" border="0" cellpadding="0" cellspacing="0" class="txc-table" style="border:none;border-collapse:collapse;;font-family:나눔고딕;font-size:13px" width="604"><tbody><tr><td style="width: 151px; height: 24px; border: 1px solid rgb(204, 204, 204); background-color: rgb(217, 229, 255);"><span style="font-size: 11pt;"> </span><span style="font-size: 11pt;">함수</span>

</td><td style="width: 151px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-top-width: 1px; border-top-style: solid; border-top-color: rgb(204, 204, 204); background-color: rgb(217, 229, 255);"><span style="font-size: 11pt;"> 기능</span>

</td><td style="width: 151px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-top-width: 1px; border-top-style: solid; border-top-color: rgb(204, 204, 204); background-color: rgb(217, 229, 255);"><span style="font-size: 11pt;">element 삭제유무</span>

</td><td style="width: 151px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-top-width: 1px; border-top-style: solid; border-top-color: rgb(204, 204, 204); background-color: rgb(217, 229, 255);"><span style="font-size: 11pt;">비어있는 경우 </span>

</td></tr><tr><td style="width: 151px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-lef**t-color: rgb(204, 204, 204);"><span style="font-size: 11pt;"> </span><span style="color: rgb(0, 0, 0); font-family: 나눔고딕; font-size: 11pt; line-height: 2;">peek </span></td><td style="width: 151px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 11pt;"> head를 가져옴.</span>

</td><td style="width: 151px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 11pt;">X</span>

</td><td style="width: 151px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 11pt;">return null</span><span style="font-size: 11pt;"> </span>

</td></tr><tr><td style="width: 151px; height: 23px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"><span style="font-size: 11pt;"> </span><span style="color: rgb(0, 0, 0); font-family: 나눔고딕; font-size: 11pt; line-height: 2;">poll </span></td><td style="width: 151px; height: 23px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 11pt;"> </span><span style="font-size: 11pt;">head를 가져옴.</span>

</td><td style="width: 151px; height: 23px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 11pt;">O</span>

</td><td style="width: 151px; height: 23px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 11pt;"> return null</span>

</td></tr><tr><td style="width:151;height:24;border-bottom:1px solid #ccc;border-right:1px solid #ccc;border-left:1px solid #ccc;;"><span style="font-size: 11pt;"> </span><span style="color: rgb(0, 0, 0); font-family: 나눔고딕; font-size: 11pt; line-height: 2;">remove </span></td><td style="width: 151px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 11pt;"> </span><span style="font-size: 11pt;">head를 가져옴.</span>

</td><td style="width: 151px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 11pt;">X</span>

</td><td style="width:151;height:24;border-bottom:1px solid #ccc;border-right:1px solid #ccc;;"><span style="font-size: 11pt;"> throw exc</span><span style="font-size: 11pt;">eption</span>

</td></tr><tr><td style="width: 151px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"><span style="font-size: 11pt;"> </span><span style="color: rgb(0, 0, 0); font-family: 나눔고딕; font-size: 11pt; line-height: 2;">element </span></td><td style="width: 151px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 11pt;"> </span><span style="font-size: 11pt;">head를 가져옴.</span>

</td><td style="width: 151px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 11pt;">O</span>

</td><td style="width: 151px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="color: rgb(0, 0, 0); line-height: 2; font-size: 11pt;"> throw exception</span><span style="font-size: 11pt;"> </span>

</td></tr></tbody></table></div><div></div></div><div><div><span style="font-size: 11pt;">계산 복잡도</span></div><div></div><div><table align="justify" border="0" cellpadding="0" cellspacing="0" class="txc-table" style="border:none;border-collapse:collapse;;font-family:돋움;font-size:13px" width="604"><tbody><tr><td style="width: 302px; height: 24px; border: 1px solid rgb(204, 204, 204); background-color: rgb(217, 229, 255);">**<span style="font-size: 11pt;"> </span><span style="font-size: 11pt;">함수</span>**

</td><td style="width: 302px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-top-width: 1px; border-top-style: solid; border-top-color: rgb(204, 204, 204); background-color: rgb(217, 229, 255);"><span style="font-size: 11pt;"> 계산복잡도</span></td></tr><tr><td style="width: 302px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"><span style="font-size: 11pt;"> </span><span style="color: rgb(0, 0, 0); font-family: 나눔고딕; font-size: 11pt; line-height: 2;">offer, poll, remove, add</span></td><td style="width: 302px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 11pt;"> </span><span style="color: rgb(0, 0, 0); font-family: 나눔고딕; font-size: 11pt; line-height: 2;">O(log(n))</span>

</td></tr><tr><td style="width:302;height:24;border-bottom:1px solid #ccc;border-right:1px solid #ccc;border-left:1px solid #ccc;;"><span style="font-size: 11pt;"> </span><span style="color: rgb(0, 0, 0); font-family: 나눔고딕; font-size: 11pt; line-height: 2;">remove(obj), contains(obj)</span></td><td style="width:302;height:24;border-bottom:1px solid #ccc;border-right:1px solid #ccc;;"><span style="font-size: 11pt;"> </span><span style="color: rgb(0, 0, 0); font-family: 나눔고딕; font-size: 11pt; line-height: 2;">linear time</span></td></tr><tr><td style="width:302;height:24;border-bottom:1px solid #ccc;border-right:1px solid #ccc;border-left:1px solid #ccc;;"><span style="font-size: 11pt;"> </span><span style="color: rgb(0, 0, 0); font-family: 나눔고딕; font-size: 11pt; line-height: normal;">peek, element</span></td><td style="width:302;height:24;border-bottom:1px solid #ccc;border-right:1px solid #ccc;;"><span style="font-size: 11pt;"> </span><span style="color: rgb(0, 0, 0); font-family: 나눔고딕; font-size: 11pt; line-height: normal;">constant time </span></td></tr></tbody></table></div></div></div></div></div>

**주의사항**

**1. Iterator 사용시, 정렬보장.**

그러나, iterator를 사용시에는 주의해야 한다. PriorityQueue는 기본적으로 natural ordering 이 되는데, iterator() 함수를 이용해서 Iterator를 생성했을 때에는 그것이 보장되지 않는다. 다음의 코드를 실행시켜 보자. 

<script src="https://gist.github.com/4432186.js"></script>

앞에서 말한대로라면 for문을 이용해서 `poll()` 함수로 element들을 빼 왔을때에는 정렬된 채로 나왔었기 때문에 Iterator를 이용할때에도 같은 결과가 나와야 하는데, while 문을 이용해서 출력해보면 정렬된 결과가 나오지 않는 것을 확인할 수가 있다. 필자가 실행 시켰을 경우에는 다음과 같은 결과가 나왔다. 

<div align="left" style="font-size:12pt;"><font face="Consolas" size="2"><span style="font-size: 10pt;">  
</span></font></div><div align="left"><div class="txc-textbox" style="font-size:12pt; border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><div align="left"><font face="Consolas" size="2"><span style="font-size: 11pt;">1</span></font></div><div align="left"><font face="Consolas" size="2"><span style="font-size: 11pt;">2</span></font></div><div align="left"><font face="Consolas" size="2"><span style="font-size: 11pt;">5</span></font></div><div align="left"><font face="Consolas" size="2"><span style="font-size: 11pt;">4</span></font></div><div align="left"><font face="Consolas" size="2"><span style="font-size: 11pt;">3</span></font></div><div align="left"><font face="Consolas" size="2"><span style="font-size: 11pt;">9</span></font></div><div align="left"><font face="Consolas" size="2"><span style="font-size: 11pt;">6</span></font></div><div align="left"><font face="Consolas" size="2"><span style="font-size: 11pt;">10</span></font></div><div align="left"><font face="Consolas" size="2"><span style="font-size: 11pt;">7</span></font></div><div align="left"><font face="Consolas" size="2"><span style="font-size:11pt;">8</span></font></div></div><div align="left" style="font-size:12pt;"><font face="Consolas" size="2"><span style="font-size: 10pt;">  
</span></font></div> 

**2. 동기화**  

동기화되어있지는 않으며, thread-safe를 위해서는 [PriorityBlockingQueue](http://docs.oracle.com/javase/6/docs/api/java/util/concurrent/PriorityBlockingQueue.html) class 를 사용할것을 권장하고 있다. 

</div></div>

