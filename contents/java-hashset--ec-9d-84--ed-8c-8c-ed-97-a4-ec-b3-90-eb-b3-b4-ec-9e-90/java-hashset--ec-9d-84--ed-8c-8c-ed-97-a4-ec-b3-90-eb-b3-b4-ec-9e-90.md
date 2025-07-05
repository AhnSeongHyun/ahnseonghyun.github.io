---
title: '[Java] HashSet 을 파헤쳐보자.'
author: 'ash84'
pub_date: '2017-04-24'
description: ''
featured_image: ''
tags: ['dev', 'HashMap', 'HashSet', 'Java', 'set']
---

HashSet은 Set 인터페이스를 구현하는 클래스로 내부적으로 HashMap 인스턴스의 지원을 받는다. [GrepCode](http://grepcode.com/file/repository.grepcode.com/java/root/jdk/openjdk/6-b14/java/lang/String.java)에 가서 HashSet을 찾아보자.  

<script src="https://gist.github.com/4449912.js"></script>

위와 같이 HashSet은 내부적으로 HashMap을 가지고 있다. 그렇기 때문에 대부분의 함수가 HashMap의 함수를 Wrapping 해놨다고 볼수 있다. 

**Iterator에 대해서**

Iterator의 성능과 관련해서는 HashSet 인스턴스의 사이즈(number of elements) + 내부에 있는 HashMap 인스턴스의 capacity 의 합에 비례해서 시간이 필요하다고 한다. 때문에 만약 Iteration의 성능을 중요하게 여긴다면, initial capacity 를 매우 높게 혹은 load factor를 매우 낮게 잡는 것은 그리 중요하지 않다고 한다. 왜냐하면 결국 사이즈에 비례하기 때문이다. Iterator는 당연히 fail-fast 방식이다. fail-fast에 대해서는 여기를 참고해 보시면 알수 있다. 단순히 말해서 순차적으로 접근하고 있는 도중에 변경을 하면 ConcurrentModification Exception을 발생시킨다는 것이다. 

동기화는 안된다. 동시에 여러스레드가 접근할 경우, 적어도 한게는 Set을 변경할수 있는 가능성이 있다. 그렇기 때문에 외부적으로 동기화를 시키라고 권장한다. 초기 생성시에 동기화된 Set 인스턴스를 만들고 싶다면, 아래처럼 사용하라고 하고 있다. 이렇게 쓸 때의 장점은 생성시간이 최고(가장짧다.)이며, 동기화가 안되는 접근을 차단할수 있다고 한다.  

```java
Set s = Collections.synchronizedSet(new HashSet(...));
```
 

일반적인 함수는 특별히 살펴볼것이 없다. 대신에 생성자를 살펴보자. HashSet 에서는 **5가지 생성자**를 제공하고 있다. 아래와 같은데,

<script src="https://gist.github.com/4449928.js"></script>

기본 생성자는 그냥 쓰면 되는 것이고, initialCapacity 와 loadFactor를 따로 줄 수 있다. 

**간단히 말해서 HashMap에서 re-hashing 을 결정짓는 요소들이라고 생각하면 된다.** 

생성자 중 특이한 것은  Collection 인스턴스를 받는 생성자이다. 당연히 생성 초기시에 미리 넣을 것을 받는것인데 특이한 점은 받은 인스턴스내 element 의 수를 가지고 적정한 `initialCapacity`를 만들어서 HashMap을 생성하고 있다는 점이다. 그리고 외부에서는 생성할수 없는 5번째 생성자는 같은 패키지 안에서 생성할 경우 사용되는 생성자인데 특이하게 LinkedHashMap을 생성하는 것을 볼수가 있다. 

HashSet을 사용한 예로는 텍스트 파일에서 동일한 길이의 단어를 읽어서 중복 제거가 된 어떤 리스트를 만들고 싶을때, 굳이 `readLine()` 으로 읽어온 뒤 List 에 넣어서 다시 처리하기 보다는 HashSet에 바로 넣어서 자동으로 중복 검사를 하였다.  

물론 파일에서 읽어온 순서가 중요하다던지 특정한 기준으로 정렬을 해야한다면 이야기는 달라진다. HashSet 보다 더 좋은 방법이 있을지도 모른다. 중요한것은 각각의 클래스가 가지고 있는 특성들을 잘 이해해야, 실제 구현환경에서 성능적인 부분도 고려해서 잘 만들수 있을것 같다. 

