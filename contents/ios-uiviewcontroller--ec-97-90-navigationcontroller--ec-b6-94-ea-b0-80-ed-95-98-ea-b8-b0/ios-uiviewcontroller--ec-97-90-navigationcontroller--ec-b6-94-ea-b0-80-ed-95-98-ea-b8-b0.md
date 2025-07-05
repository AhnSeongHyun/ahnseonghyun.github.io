---
title: '(iOS) UIViewController 에 NavigationController 추가하기'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['(iOS) UIViewController 에 NavigationController 추가하기', 'dev', 'IOS', 'NavigationController', 'UIViewController']
---


<span style="font-size: 11pt;"></span><span style="font-size: 11pt;"></span><span style="font-size: 11pt;">맨날 까먹는 부분이라 메모차 적어둔다. NavigationController로 시작 할 경우 AppDelegate 에서 잡아주고 시작하지만 중간에 presentModalViewController 함수를 통해서 띄울경우,</span><span style="font-size: 11pt;"> 아래와 같이 설정해 주면 된다. 간단히 말해서 뜨기 전에 미리 NavigationController를 연결해주는것이 핵심이다. </span>

<script src="https://gist.github.com/AhnSeongHyun/5361735.js"></script>



