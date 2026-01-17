---
title: '(iOS) 회전을 하면서 UIViewController 띄우기'
author: 'ash84'
pub_date: '2013-05-08'
description: '단일 뷰 어플리케이션 같은 경우, 설정뷰를 보여주려면 그냥 아래에서 위로 올라오는 것 보다 회전하는 애니메이션을 주면서 보여주는 것이 훨씬 보기에 좋다.(주관적인수 있음) presentViewController 를 이용해서 UIViewController를 보여주면 그냥 아래에서 위로 올라오지만 아래와 같이 보여줄 ViewController의'
featured_image: ''
tags: ['dev', 'iOS', 'modalTransitionStyle', 'Objective-C', 'presentViewController', '회전 뷰 컨트롤러']
---
<span style="font-size: 11pt;"></span><span style="font-size: 11pt;"></span><span style="font-size: 11pt;">단일 뷰 어플리케이션 같은 경우, 설정뷰를 보여주려면 그냥 아래에서 위로 올라오는 것 보다 회전하는 애니메이션을 주면서 보여주는 것이 훨씬 보기에 좋다.(주관적인수 있음) presentViewController 를 이용해서 UIViewController를 보여주면 그냥 아래에서 위로 올라오지만 아래와 같이 보여줄 ViewController의 modalTransitionStyle을 지정해 주면 회전하면서 보여지게 된다.</span>

<script src="https://gist.github.com/AhnSeongHyun/5543912.js"></script>



