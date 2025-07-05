---
title: '[Java] LinkedHashSet, 이건 멀까?'
author: 'ash84'
pub_date: '2017-03-24'
description: ''
featured_image: ''
tags: ['dev', 'HastSet 정렬', 'LinkedHashSet', 'LinkedHashSet 분석', 'LinkedHashSet 성능', 'set interface']
---


<span style="font-size: 11pt;">Set 인터페이스 관련 3번째 포스팅, 지난번 [HashSet](http://ash84.tistory.com/898)에 이어서 LinkedHashSet이다. 기본적으로 Set 인터페이스에서 제공하는 함수를 가지고 있</span><span style="font-size: 11pt;">고, **null은 허용**된다. </span><span style="font-size: 11pt;"> 일단 내부 코드를 보자. </span>

<span style="font-size: 11pt;">  
<script src="https://gist.github.com/4480561.js"></script>  
</span>

<span style="font-size: 11pt;">기본적으로 앞서 애기한 [HashSet ](http://ash84.tistory.com/898)을 상속 받도록 되어 있고, 모든 생성자에는 별도의 인스턴스를 만드는 것이 아니라 부모(super()) 생성자를 초기화하는 방식으로 되어 있다.** 총 4개의 생성자**를 가지고 있는데 모두 아래와 같다. </span>

<span style="font-size: 11pt;">  
<script src="https://gist.github.com/4480563.js"></script>  
</span>

<span style="font-size: 11pt;">생성자를 보면 알겠지만, 모두 부모 생성자를 호출하고 있다. 즉, HashSet의 생성자를 호출하고 있는 것이다. 특히, HashSet의 생성자중 5번째 패키지내에서만 호출할수 있는 생성자를 호출하고 있다. </span>

<span style="font-size: 11pt;">  
<script src="https://gist.github.com/4480568.js"></script>  
</span>

<span style="font-size: 11pt;">**즉, LinkedHashSet은 부모인 HashSet을 만들고 그리고 내부적으로 LinkedHashMap을 만들고 있다. **</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">LinkedHashSet   =>   HashSet   =>   LinkedHashMap</span>

</div><span style="font-size: 11pt;">HashSet의 구현과는 다른데,** 이중 링크드리스트(Double Linked List)를 유지**한다. 이 링크드리스트는 Iteration의 순서를 정하는데, Iteration의 순서는 LinkedHashSet에 삽입된 순서이다. 만약 하나의 element가 재 삽입되더라도 영향을 받지 않는다. 하나의 element 가 재삽입 된다면 s.add(e) 이런식으로 호출이 되는데, s.contains(e)가 true를 리턴하도록 되어 잇다. </span>

<span style="font-size: 11pt;">**HashSet과의 차이점 **</span>

<span style="font-size: 11pt;">가장 큰 차이는 **입력한 순서대로 나온다는 점**이다. </span>

<span style="font-size: 11pt;">  
<script src="https://gist.github.com/4480571.js"></script>  
</span>

<span style="font-size: 11pt;">위의 코드를 보자. 결과 값은 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 16, 19, 18] 이렇게 나온다. 정렬이 된다는 것이 아니다. 보시다시피,</span><span style="font-size: 11pt;"> HashSet은 Set의 가장 큰 특성인 중복제거를 해줄지는 몰라도 입력한 순서를 보장하지는 않는다. </span>

<span style="font-size: 11pt;">**LinkedHashSet은 어떠할까?**</span>

<span style="font-size: 11pt;">**LinkedHashSet은 입력한 순서대로 나온다.** 위에서 언급한것 처럼 재삽입된 경우도 재현해서 테스트해 보았다. </span>

<span style="font-size: 11pt;">  
<script src="https://gist.github.com/4480576.js"></script>  
</span>

<span style="font-size: 11pt;">3을 나중에 넣었는데 위에서 언급한대로 중복되는 것은 삽입이 되지 않는다. 그리고 311을 넣었을때 정렬되지 않은채 제일 마지막에 삽입했기 때문에 제일 뒤에 있는것을 확인 할 수가 있다. </span>

<span style="font-size: 11pt;">재 삽입되는 경우, 내부 코드가 어떻게 돌아가는지 보자. </span>

<span style="font-size: 11pt;">s.ad(e)를 호출하게 되면 부모인 HashSet의 add()가 호출되고 내부적으로 LinkedHashMap을 거져서 HashMap의 put() 함수로 연결되는 것을 볼수가 있다.(GrepCode) 즉, HashMap의 put() 함수를 통해서 element가 삽입되기 때문에 자연스럽게 중복제거가 된다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">LinkedHashSet.add()   =>   HashSet.add()   =>   LinkedHashMap.put()   =>   HashMap.put()</span>

</div><span style="font-size: 11pt;">**HashSet의 CHOATIC Ordering 해결법**</span>

<span style="font-size: 11pt;">위에서 본것 처럼 HashSet은 이상한 정렬을 가진다. 이것은 자바 공식 문서에서도 Choatic ordering 이라고 말하고 있을 정도인데, HashSet은 정렬이 이해할수가 없고, LinkedHashSet은 입력한 순서대로 들어간다. 그러나 정렬을 해야할 경우가 생기기 때문에 정렬을 하려면 다음과 같이** TreeSet을 써서 이전 Set을 copy하는 동시에 정렬하면 된다. **</span>

<span style="font-size: 11pt;">  
<script src="https://gist.github.com/4480579.js"></script>  
</span>

<span style="font-size: 11pt;">**성능문제 **</span>

<span style="font-size: 11pt;">성능은 [HashSet ](http://ash84.tistory.com/898)보다 약간 떨어질 수 있는데 링크드리스트를 유지하는데 비용이 든다고 한다. 한가지 예외로는 LinkedHashSet의 Iteration 은 capacity(capacity 와 size 는 다르다. [HashMap 정리 참고](http://ash84.tistory.com/851))에 상관없이 **Set의 사이즈에 비례하는 시간이 필요하다고 한다. **</span>

<span style="font-size: 11pt;">LinkedHashSet은 두가지 요소에 대해서 성능에 영향을 받는다 initial capacity와 load factor 인데 이것들이 성능에 영향을 주는 이유는** 내부적으로 [HashMap](http://ash84.tistory.com/851)을 사용하기 때문이다.** 주의할 점은 Iteration 은 capacity에 영향을 받는것이 아니라는 점이다. 그렇기 때문에 매우 높은 initial capacity를 줄 필요는 없다. </span>

<span style="font-size: 11pt;">**동기화 **</span>

<span style="font-size: 11pt;">동기화는 LinkedHashSet이 기본적으로 제공하지 않기 때문에 다음과 같이 synchro</span><span style="font-size: 11pt;">nized</span><span style="font-size: 11pt;">Set() 함수를 이용하면 된다. </span>

<div><div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><font face="나눔고딕"><span style="font-size: 11pt;"> Set s = Collections.synchronizedSet(new LinkedHashSet(...)); </span></font>

</div></div><div></div><div><span style="font-size: 11pt;">**Iterator**</span></div><div><span style="font-size: 11pt;">Iterator는 fail-fast 방식이다. fail-fast에 대해서는 [HashSet ](http://ash84.tistory.com/898)을 참고하면 된다.   </span></div>

