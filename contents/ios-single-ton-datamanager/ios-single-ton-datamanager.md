---
title: '(iOS) Single-ton DataManager'
author: 'ash84'
pub_date: '2013-01-18'
description: '자주 쓰는 프로그래밍 방식중 하나인데, 싱글턴으로 DataManager 라는 클래스를 만들어서 그곳에서 앱내에 모든 파일 관련 작업들을 다 해주는 것이다. 다른 각 클래스에서는 singleTon_GetInstance 를 이용해서 그냥 객체 생성하듯 생성하면 되지만 실제로는 하나만 생성이 된다. 아래의 코드는 그냥 간단하다. 저장하고자 하는 데'
featured_image: ''
tags: ['DataManager', 'dev', 'IOS', '아이폰 개발']
---


<span style="font-size: 11pt;">자주 쓰는 프로그래밍 방식중 하나인데, 싱글턴으로 DataManager 라는 클래스를 만들어서 그곳에서 앱내에 모든 파일 관련 작업들을 다 해주는 것이다. 다른 각 클래스에서는 </span><span style="color: rgb(0, 0, 0);  line-height: 2; font-size: 11pt;">singleTon_GetInstance 를 이용해서 그냥 객체 생성하듯 생성하면 되지만 실제로는 하나만 생성이 된다. 아래의 코드는 그냥 간단하다. 저장하고자 하는 데이터가 있으면 NSMutableArray를 받아서 파일이름으로 현재 Application 에 Document 에 저장을 하는 방식이다. </span><span style="color: rgb(0, 0, 0);  font-size: 11pt; line-height: 2; ">읽어올때는 파일이름으로 읽어온다고 보면 된다. 저장되는 형식은 .plist 파일형식이다. </span>

<script src="https://gist.github.com/4568422.js"></script>  
  
<script src="https://gist.github.com/4568397.js"></script>



