---
title: '(iOS) NSNotification 생성 및 사용 코드'
author: 'ash84'
pub_date: '2013-04-23'
description: 'NSNotification은 아이폰 프로그래밍에서 빠질수 없는 것인데, 굳이 함수 호출이 아니여도 메시지를 미리 등록하고 연결된 함수를 정의해두면 해당 메시지를 보냈을때 위치에 상관없이 연결된 함수가 호출되는 편리한 구조이다. 
  
#### 1. 메시지 등록하기

 


– 등록하는 코드는 다음과 같다. NSNotificationCent'
featured_image: ''
tags: ['dev', 'iOS', 'Notification', 'notificationcenter', 'NSNotification', 'NSNotificationCenter', 'postNotificationName', '알림']
---
<span style="font-size: 11pt;">NSNotification은 아이폰 프로그래밍에서 빠질수 없는 것인데, 굳이 함수 호출이 아니여도 메시지를 미리 등록하고 연결된 함수를 정의해두면 해당 메시지를 보냈을때 위치에 상관없이 연결된 함수가 호출되는 편리한 구조이다. </span>

<span style="font-size: 11pt;">  
#### 1. 메시지 등록하기

 

</span>

<span style="font-size: 11pt;">– 등록하는 코드는 다음과 같다. NSNotificationCenter 객체를 만들고 addObserver 함수를 이용해서 등록하면 된다. 등록시 주의사항중 하나는 selector 지정시 해당 함수의 인자는 NSNotification 형식 이어야 한다는 점이다. 필자의 경우, 주로 viewDidLoad() 함수에서 등록하는 부분을 수행하도록 처리한다. </span>

<script src="https://gist.github.com/AhnSeongHyun/5444248.js"></script>

<span style="font-size: 11pt;">  
#### 2. 메시지 보내기

 

</span>

<span style="font-size: 11pt;">– 메시지 보내기는 아래와 같은데 더 쉽다. postNotificationName 함수에 앞에서 정의한 이름을 넣어준다. 그리고 같이 전달할 객체를 object에 넣어주면 된다. userInfo 에는 NSDictionary 형태로 데이터를 넣어서 보낼수 있다. 전달된 객체는 연결된 함수에서 NSNotification 파라미터로 받아서 처리할 수 있는 것이다. </span>

<script src="https://gist.github.com/AhnSeongHyun/5444277.js"></script>

<span style="font-size: 11pt;">테스트 해보면 그리 어렵지 않을 것이라 생각된다. (쓴 내용도 별로 없다.) </span>



