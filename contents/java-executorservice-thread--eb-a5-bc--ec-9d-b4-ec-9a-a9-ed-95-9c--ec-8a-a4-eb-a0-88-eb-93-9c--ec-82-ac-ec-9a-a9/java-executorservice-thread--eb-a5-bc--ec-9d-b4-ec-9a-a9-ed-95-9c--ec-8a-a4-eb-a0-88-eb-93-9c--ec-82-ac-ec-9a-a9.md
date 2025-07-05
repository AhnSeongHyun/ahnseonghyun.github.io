---
title: '(Java) ExecutorService, Thread 를 이용한 스레드 사용'
author: 'ash84'
pub_date: '2017-04-27'
description: ''
featured_image: ''
tags: ['dev', 'ExecutorService', 'Java', 'Thread', '스레드', '스레드 리턴', '자바 스레드']
---


자바 프로그래밍을 하면서 스레드를 자주 사용하는 편인데, 아무래도 속도가 안나오면 데이터를 많이 처리하는 부분에서 병렬처리를 하는 것이 가장 첫 번째로 생각할 수 있는 처리속도의 향상 방법이라고 할수 있겠다. **Thread 객체를 사용하는 방법과 ExecutorService를 사용하는 방법이 있는데, 필자는 주로 각각 다른 작업을 병렬로 해야하는 경우에는 Thread-Runnable 조합을 이용하고, 같은 작업을 여러개로 나눠서 처리한 뒤 결과를 모아서 정렬, 처리 등을 하는 작업의 경우 ExecutorService-Callable 조합을 사용하고 있다.** 

<script src="https://gist.github.com/AhnSeongHyun/4951392.js"></script>

**Thread-Runnable 조합의 특징을 계산 결과를 리턴할 수 없다는 것이다.** 물론 방법이 없는 것은 아니다. 필자의 경우 싱글톤 클래스를 만들어서 데이터를 스레드 안에서 싱글톤 클래스의 객체를 가져와서 처리된 값을 전달하는 방식으로 하곤 했었는데, 사실 이 방법은 그리 좋은 방법은 아니다. Thread-Runnable 조합의 경우 여러개의 Runnable 상세구현 클래스를 만들어서 각기 다른 로직이 돌아가는 식으로 구성하곤 했었다.  
 

<script src="https://gist.github.com/AhnSeongHyun/4951471.js"></script>

ExcutorService 는 좀더 편리하다. Thread 객체가 가지고 있는 복잡스러운 함수들(왜 이렇게 deprecated가 많은건지..)을 신경쓰지 않고, ThreadPool 을 생성해서 쓸수가 있다. Callable 상세구현 클래스의 가장 큰 특징이라면 단연 처리로직후의 데이터를 리턴 받을 수 있다는 것이다. Future 객체의 `get()` 함수를 통해서 지정한 형식의 데이터를 받을 수가 있다. 해당 데이터는 `call()` 함수의 리턴을 통해서 전달되게 된다. 필자의 경우 위의 예제에서는 List<String>을 사용했지만 사실은 주로 리턴 클래스를 따로 만들어서 반환하는 방식을 주로 사용한다. 예를들어, MaxWord 라는 클래스가 있는데, word, maxCount 멤버 변수를 가지고 있다고 가정하면, `get()` 함수를 통해서 전달 받아서 List 에 넣어서 maxCount 순으로 정렬하는 후처리를 하곤 한다. 

Thread-Runnable 조합에서는 스레드 중지에 대해서 조금 애매하긴 하다. stop 메소드는 deprecated 되었고, flag 방식과 interrupt() 방식이 있는데 조사해본 결과 interrupt()가 좀더 안전하고 try-catch를 통해서 확실한 처리가 가능하다고 한다.

그에 비해서 ExcutorService는 처음 생성시에 ThreadPool로 생성하고 `shutDown()`, `showDownNow()` 메소드를 제공하기 때문에 명시적으로 중지할 수 있다. ExecutorService는 개발자가 복잡한 스레드 처리를 간편하게 쓸수 있다는 점에서 확실한 효과를 가지고 있다고 생각한다. 

이외에도 여러가지 스레드, 동시성 관련 처리가 있는데 아래의 링크들을 살펴보면 좀더 자세히 알 수가 있다. 이외에도 다양한 Thread와 ExecutorService 관련 사용법들이 있을텐데, 앞으로 좀더 사용할때 마다 올리도록 하겠다.  


[java.util.concurrent에 대해 모르고 있던 5가지 사항, Part 1](http://www.ibm.com/developerworks/kr/library/j-5things4.html) 

[java.util.concurrent에 대해 모르고 있던 5가지 사항, Part 2](http://www.ibm.com/developerworks/kr/library/j-5things5.html)

