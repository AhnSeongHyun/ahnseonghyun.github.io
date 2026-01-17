---
title: '[Java] HashMap에 대한 정리.'
author: 'ash84'
pub_date: '2012-11-26'
description: '뭐, 다들 아는 사실이겠지만, HashMap에 대해서 한번 더 정리를 하려고 한다. 필자는 Hashtable을 많이 쓰긴 하는데 HashMap에 대해서 정리를 하는 이유는 단연 **성능**때문이다. 스케일 아웃도 좋지만, 일정 수준이상의 성능 최적화 작업은 늘 필요하기 마련이기 때문이다. 
**HashMap **
– 일단 둘다 key-va'
featured_image: ''
tags: ['HashMap', 'HashMap 성능', 'Hashtable', 'Java', 'dev', 'performance']
---
<span style="font-size: 11pt;">뭐, 다들 아는 사실이겠지만, HashMap에 대해서 한번 더 정리를 하려고 한다. 필자는 Hashtable을 많이 쓰긴 하는데 HashMap에 대해서 정리를 하는 이유는 단연 **성능**때문이다. 스케일 아웃도 좋지만, 일정 수준이상의 성능 최적화 작업은 늘 필요하기 마련이기 때문이다. </span>

<span style="font-size: 11pt;">**HashMap **</span>

<span style="font-size: 11pt;">– 일단 둘다 key-value 형태를 지원하는 Collection이다. (dictionary)</span>

<span style="font-size: 11pt;">– 크게 다른 점은 2가지 : Unsynchronized 와 null 의 허용이다. </span>

<span style="font-size: 11pt;">  
</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">**1. Unsynchronized **</span>

<span style="font-size: 11pt;">– 동기화의 유무는 둘의 차이를 보여주는 가장 큰 factor 이다. </span>

<span style="font-size: 11pt;">– 동시성에 대한 지원을 위해서는 단연 HashTable을 써야 한다. </span>

<span style="font-size: 11pt;">– 아니면 ConcurrentHashMap를 사용하던가,  Collections.synchronizedMap() 을 사용해야 한다.</span>

<span style="font-size: 11pt;">**2. null 허용**</span>

<span style="font-size: 11pt;">– Hashtable 에서는 null을 Key, value로 넣을수 없다. </span>

<span style="font-size: 11pt;">– HashMap에서는 null을 Key, Value에 넣을 수 있다. </span>

</div><span style="font-size: 11pt;">**HashMap, Hashtable 에 영향을 미치는 두가지 **</span>

– <span style="font-size: 15px; line-height: 29px;">HashMap은 get(), put()  함수에 대해서 일정한 시간 성능을 보장한다고 한다. 또한 버킷(buckets)에 골고루 분산해서 저장한다고 한다. </span>

<span style="font-size: 15px; line-height: 29px;">  
</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">**1.  initial capacity(초기용량)**</span>

<span style="font-size: 11pt;">–  capacity : number of buckets : .size()</span>

<span style="font-size: 11pt;">–  초기 생성시의 용량</span>

**<span style="font-size: 11pt;">– HashMap : 11</span>  
<span style="font-size: 11pt;">– Hashtable : 16 </span>**

<span style="font-size: 11pt;">**2. load factor**</span>

<span style="font-size: 11pt;">– buckets 가 얼마나 찾을경우, re-hash 를 발생 시킬것인지를 결정하는 상수 </span>

<span style="font-size: 11pt;">– re-hash시 현재 buckets 의 2배에 해당하는 공간이 필요하다. </span>

<span style="font-size: 11pt;">**– default :0.75(최적화 된 값)**</span>

</div><span style="font-size: 11pt;">결국 성능을 위해서는 HashMap에 들어갈 엔트리의 수와 load factor를 고려해서 initial capacity 를 잘 설정해야 한다. 그래야만 re-hash 이 최소발생이 된다. 자바 문서에서는 다음과 같이 권고하고 있다.</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">initial capacity > (the maximum number of entries/load factor) </span>

</div><span style="font-size: 11pt;">이 상태가 유지가 되면 re-hash 가 일어나지 않는다고 한다. 그래서 테스트를 해보았다. 테스트는 기본적으로 100만건에 대해서 Integer형 Key,Value에 대해서 put() 하는 식으로 진행하였고, 한번은 초기값없이, 한번은 초기값을 위의 계산식에 의해서 계산된 값을 넣어주는 식으로 진행하였다. 측정 대상은 처리 속도이다. </span>

<script src="https://gist.github.com/4134159.js"></script>

<div><div style="text-align: start;"><font color="#000000" face="나눔고딕" size="3"><span style="line-height: normal;"> </span></font></div></div><span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">보시는 것 처럼 분명히 성능 차이가 있다. HashMap에 얼마만큼의 엔트리가 들어갈지 미리 안다는 것은 사실 쉽지가 않다. 대부분의 Collection 들은 불확실한 리스트, 집합 등등을 지원하기 때문에 존재하기 때문이다. 그럼에도 불구하고 어느정도 예측할 수 있다면, 어느정도의 성능향상을 가져올 수 있지 않을까 싶다.   </span>



