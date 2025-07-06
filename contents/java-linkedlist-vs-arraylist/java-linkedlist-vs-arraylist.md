---
title: '[Java] LinkedList, ArrayList와 뭐가 다른가.'
author: 'ash84'
pub_date: '2017-03-24'
description: '클린코드등의 책을 보면서, 인터페이스에 맞춰서 프로그래밍 하라는 이야기를 많이 들었고, C#의 ArrayList가 익숙해서 그런지 주로 자바에서 사용하는 Collection중 하나가 아래와 같은 List 이다.'
featured_image: ''
tags: ['ArrayList', 'dev', 'Java', 'LinkedList', '자바']
---


<span style="font-size: 11pt;">클린코드등의 책을 보면서, </span><span style="font-size: 11pt;">인터페이스에 맞춰서 프로그래밍 하라는 이야기를 많이 들었고, C#의 ArrayList가 익숙해서 그런지 주로 자바에서 사용하는 Collection중 하나가 아래와 같은 List 이다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; line-height: 2; text-align: justify;"><span style="font-size: 11pt;">List<String> strList = new ArrayList<String>(); </span>

</div><span style="font-size: 11pt;">List는 다양한 상세구현 클래스를 가지고 있는데 그 중</span><span style="font-size: 11pt;">에서 **가장 보편적인 것이 ArrayList** 이고, 이번엔 **LinkedList**에 대해서 알아보도록 하자. 주로 LinkedList 만이 가지고 있는 함수들을 중점적으로 보도록 하겠다. </span><span style="font-size: 11pt; line-height: 2;">대부분의 함수가 ArrayList 에서처럼 임의의 인덱스에 접근 할 수 있는 것과 더불어서 ~First, ~Last 접미어를 붙여서 만든 함수로 </span>**순차적 기능을 강조한 함수**<span style="font-size: 11pt; line-height: 2;">들이 많다. </span>

<span style="font-size: 11pt;">**add 함수 **</span>

<span style="font-size: 11pt;">  
</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; line-height: 2; text-align: justify;">- <span style="font-size: 11pt;">addFirst : 처음에 추가 </span>
- <span style="font-size: 11pt;">addLast </span><span style="font-size: 11pt;">: 끝에 추가</span>

</div><div style="line-height: 2; text-align: justify;"><span style="font-size: 11pt;">  
</span></div><div style="line-height: 2; text-align: justify;"><span style="font-size: 11pt;">**get 함수**</span></div><span style="font-size: 11pt;">  
</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; line-height: 2; text-align: justify;">- <span style="font-size: 11pt;">getFirst() : 처음에 있는것 가져오기 </span><span style="font-size: 11pt;"> </span>
- <span style="font-size: 11pt;">getList()  : 끝에 있는것 가져오기 </span>

**<span style="font-size: 11pt;">  *</span><span style="font-size: 11pt;">get(index) 함수가 그러하듯, getFirst()는 계속 첫번째것만 가져온다. </span>**

</div><span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">**peek 함수**</span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">peek() 함수 역시 getFirst()와 같은 기능을 한다. 즉, 첫번째 element를 가져와서 삭제하지 않는다. </span><span style="font-size: 11pt;"><span style="color: rgb(255, 0, 0);">peek() 함수와 getFirst() 함수의 차이는 element가 없을때 나타난다.</span> </span><span style="font-size: 11pt;">peek() 함수는 LinkedList에 element가 </span><span style="font-size: 11pt;">없을때, 예외를 발생시키지 않고 null을 리턴한다. 그러나 getFirst() 함수는 </span><span style="font-size: 11pt;">NoSuchElementExcpetion 예외를 일으킨다. 당연히 get(0</span><span style="font-size: 11pt;">) 함수는 OutOfIndex 예외를 일으킨다. </span><span style="font-size: 11pt;">peekFirst() 와 peekLast() 함수 역시 null을 리턴한다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">**poll 함수**</span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">poll() 함수는 peek()와 같은점은 null을 리턴한다는 점이고 다른 점은 </span><span style="font-size: 11pt;">빼온것은 삭제 한다는 것이다. pollFirst(), pollLast() 함수역시 마찬가지다. </span>

<span style="font-size: 11pt;">**pop/push 함수 **</span>

<span style="font-size: 11pt;">pop() 과 push 함수는 </span><span style="font-size: 11pt;">삭제하면서 빼오는 역할과 넣는 역할을 하는데 가장 앞에 있는것을 대상으로 한다. <span style="color: rgb(255, 0, 0);">즉, 동작 자체가 stack 구조로 동작하는것을 의미한다.</span> </span><span style="font-size: 11pt;">pop() 을 하면 가장 앞에 것이 빠지고 , </span><span style="font-size: 11pt;">push()를 하면 가장 앞에서 넣는다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">**remove 함수**</span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">removeFirst() 와 removeLast() 함수는 각각 제일 앞에것 뒤에것을 삭제하면서 </span><span style="font-size: 11pt;">동시에 삭제하는 element를 리턴한다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">removeFirstOccurrence(“India”);</span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">removeLastOccurrence(“India”);</span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">이것은 indexOf(), LastIndexOf() 와 같은 개념이라고 보면 된다. 즉, </span><span style="font-size: 11pt;">removeFirstOccurrence 함수는 리스트내에서 india라고 써있는 것 중에서 첫번째 발견되는 것을 삭제한다. </span><span style="font-size: 11pt;">removeLastOccurrence 함수는 리스트내에서 india 라고 써있는 것 중에서 마지막에 발견되는 것을 삭제한다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">아래의 코드를 꼭 한번 실행해 보기를 권장한다. </span>

<span style="font-size: 11pt;">  
</span>

<script src="https://gist.github.com/4379726.js"></script>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;line-height:2;">기본적으로 LinkedList만 가지고 있는 함수에 대해서 알아 봤는데 LinkedList 역시 List 인터페이스를 구현하고 있기 때문에 null 을 포함한 모든 element를 가질수 있다고 한다. 자바문서를 살펴보면 ArrayList와 는 다르게  Queue와 Dequeue 인터페이스를 구현하고 있는것을 볼 수 있는데, 때문에 다양한 순차적 기능을 가진 함수들을 가지고 있을수 있는 것이다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">  </span>



