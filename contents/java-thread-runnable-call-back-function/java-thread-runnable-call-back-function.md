---
title: '(Java) Thread, Runnable 콜백함수'
author: 'ash84'
pub_date: '2013-05-29'
description: '최근에 [자바 네트워크 관련 책](http://book.naver.com/bookdb/book_detail.nhn?bid=1583597)을 보고 있는데(조금 옛날책) 스레드에 관련된 내용이 나와서 정리한다. [이전에 ExcutorService 에 대해서 썼을때](http://ash84.tistory.com/933)는 Runnable 의 run()함수가 void 형을 리턴하도록 되어 있기 때문에 결과 값을 받을수 없다고 설명했었는데, 이 책에서는 콜백 함수를 이용해서 각 스레드'
featured_image: ''
tags: ['dev', 'Java', 'Runnable', '스레드', '스레드 결과', '스레드 콜백함수', '콜백함수']
---
<span style="font-size: 11pt;">최근에 [자바 네트워크 관련 책](http://book.naver.com/bookdb/book_detail.nhn?bid=1583597)을 보고 있는데(조금 옛날책) 스레드에 관련된 내용이 나와서 정리한다. [이전에 ExcutorService 에 대해서 썼을때](http://ash84.tistory.com/933)는 Runnable 의 run()함수가 void 형을 리턴하도록 되어 있기 때문에 결과 값을 받을수 없다고 설명했었는데, 이 책에서는 콜백 함수를 이용해서 각 스레드의 결과를 받을수 있다고 설명하고 있다. </span>

<span style="font-size: 11pt;">그전에 폴링(polling) 방식에 대해서 설명을 하자면, 이건 스레드내 어떤 플래그를 두고 그 플래그를 스레드 내에서 처리가 완료가 되면 변경해 주고 스레드 밖에서는 그것을 계속 체크해서 변경되면 값을 가져오는 방식이다. 다들 알다시피 이 방식의 문제점은 필요이상의 일을 너무 많이 한다는 것이다. </span>

<span style="font-size: 11pt;">콜백함수는 폴링방식과는 반대다. 즉, **폴링방식은 메인이 스레드에게 물어보는 방식이라면 콜백방식은 스레드가 메인에 알려주는 방식**이다. 콜백함수는 2가지 방식으로 작성을 하는데, 하나는 메인 프로그램의 **클래스 메소드를 호출하거나 아니면 인스턴스 메소드를 호출**하는 방식이다. </span>

<script src="https://gist.github.com/AhnSeongHyun/5667540.js"></script>

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>

<span style="font-size: 11pt;">위의 클래스는 Runnable 를 구현한 것인데, 초기값을 받고 단순 계산을 하는 작업이다. 코드에서 보면 처음에 클래스 오버로드된 </span><span style="font-size: 11pt;">생성자 부분에서 callback 객체를 받고 있는데 ThreadTestMain 클래스를 받고 있다. 이 객체를 받아서 스레드 클래스 멤버에 저장을 한다. 그리고 나서 run() 함수가 완료 후에, 생성자에서 받은 callback 객체를 이용해서 계산된 값을 `callBack2(sum)` 함수를 이용해서 전달하고 있다. 클래스 메소드를 이용한 경우는 위와 같이 생성자에서 callback 객체를 받을 필요 없이, 주석처리된 부분처럼 호출해주면 된다. 예제는 Runnable를 사용했는데 Thread 클래스를 상속받을때도 마찬가지로 구현해 주면 된다. </span>

<script src="https://gist.github.com/AhnSeongHyun/5667566.js"></script>

<span style="font-size: 11pt;">어떤 방식이 더 좋다고는 말할수 없겠지만 필자의 경우 Callable 방식이 더 편한것은 사실이다. 그러나 늘 새로짜는 것이 아니고 어떤 관공서나 회사는 자바 4를 사용할수 있다는 점에서 이러한 방식도 알아둘 필요는 있는것 같다. </span>



