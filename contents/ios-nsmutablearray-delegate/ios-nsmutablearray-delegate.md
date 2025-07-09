---
title: '(iOS) NSMutableArray + Delegate'
author: 'ash84'
pub_date: '2013-12-06'
description: '별 다른건 아니고 Objective-C 에서 데이터를 관리할때 사용하는 자료구조인 `NSMutableArray` 를 자주 사용하는데 네트워크 요청이나 위치 서비스 요청을 위한 큐(Queue)를 만들때 최근에 주로 사용해 왔다. 특히 하나의  `NSMutableArray` 를 감싸서(wrapping) 사용하는데 주로 singlet'
featured_image: ''
tags: ['delegate', 'dev', 'IOS', 'NSMutableArray', 'Objective-C', '요청 큐']
---


<span style="font-size: 11pt;">별 다른건 아니고 Objective-C 에서 데이터를 관리할때 사용하는 자료구조인 `NSMutableArray` 를 자주 사용하는데 네트워크 요청이나 위치 서비스 요청을 위한 큐(Queue)를 만들때 최근에 주로 사용해 왔다. 특히 하나의 </span><span style="background-color: transparent; font-size: 11pt; line-height:2;"> `NSMutableArray` 를 감싸서(wrapping) 사용하는데 주로 singleton 과 delegate 를 결합해서 사용한다. 단연 이점이라면 하나의 아이폰 앱내에 하나의 객체만을 가지고 add, remove, get 하는 식으로 어떤 요청객체 들을 넣고 관리 할수 있다는것이 장점이다. 내부적으로 `NSMutableArray` 객체를 하나를 가지고 그에 접근할수 있는 add, remove, get 등의 함수를 만들고 그 함수에서 어떤 처리를 했을때, 등록된 delegate를 호출하게 되는 방식이다. 그렇게 되면 add 를 하는 객체는 add 를 하고 다음 로직을 진행하고 add가 되었다는 것을 알게된 다른 처리 클래스는 delegate 가 발생되었을때 그에따른 처리를 할 수 있다. </span>

<span style="background-color: transparent; font-size: 9pt; line-height: 2;">  
</span>

<script src="https://gist.github.com/AhnSeongHyun/7818716.js"></script>

<script src="https://gist.github.com/AhnSeongHyun/7818722.js"></script>

<span style="font-size: 11pt;">소스코드를 별것 없다. 그냥 예제라고 생각하면 되고 쓰는 사람에 맞게 수정해서 쓰면 된다. 아래의 그림을 보자. </span>

<span style="font-size: 11pt;">  
</span>

![](http://ash84.net/wp-content/uploads/1/cfile1.uf.217CE44D52A178491DFA82.png)

<span style="line-height: 29px; font-size: 15px; text-align: justify;">위의 그림을 보면, 어떤 객체에서 실시간 위치 정보를 받아서 서버에 전송하는 부분을 개발한다고 했을때, 위치정보의 업데이트가 언제 될지 모르기 때문에 어떤 함수를 호출하고 기다리는 것 이 아니라면 위와 같이 어떤 요청 큐에 넣으면 알아서 위치정보를 가져와서 전송해 주는 부분을 개발할 수 있다. (전송결과를 기다리냐 안기다리느냐의 차이가 있을수는 있다.) 그림에서 `NotificationRequestList` 를 </span><span style="background-color: transparent; font-size: 15px; line-height: 29px;">`NSMutableArray + Delegate` 방법으로 구현하였고, 그에 따른 delegate 수신을 requestor 클래스에서 받아서 처리하도록 하였다. </span><span style="line-height: 29px; font-size: 15px; background-color: transparent;">같은 방법으로 </span>`<code style="line-height: 29px; font-size: 15px; background-color: transparent;">NSMutableDicionary + delegate`<span style="line-height: 29px; font-size: 15px; background-color: transparent;"> 의 조합도 활용할 수 있을 것이다. </span>



