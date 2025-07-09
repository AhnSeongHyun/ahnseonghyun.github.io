---
title: '(iOS) NSTimer 사용하기'
author: 'ash84'
pub_date: '2013-11-22'
description: '개인적으로 타이머를 그렇게 좋아하진 않는다.(다들 개인적으로 좋아하지 않는 프로그래밍의 한 부분이 있을것이라 생각됨.) 사실 어떤 이벤트가 발생했다는 것을 타이머를 통해서 감지하거나 하는 경우가 있는데 그런 부분에서 잘 사용하진 않는다. 이유는 Objective-C 에는 delegate 라는 막강한 놈이 있고, 그게 아니라면 `NSNotificiation` 을 사용하는 것도 나쁘진 않다.'
featured_image: ''
tags: ['dev', 'IOS', 'NSTimer', 'scheduledTimerWithTimeInterval']
---


<span style="font-size: 11pt;">개인적으로 타이머를 그렇게 좋아하진 않는다.(다들 개인적으로 좋아하지 않는 프로그래밍의 한 부분이 있을것이라 생각됨.) 사실 어떤 이벤트가 발생했다는 것을 타이머를 통해서 감지하거나 하는 경우가 있는데 그런 부분에서 잘 사용하진 않는다. 이유는 Objective-C 에는 delegate 라는 막강한 놈이 있고, 그게 아니라면 `NSNotificiation` 을 사용하는 것도 나쁘진 않다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">그래서 `NSTimer`를 사용할때는 주로 어떤 작업이 몇분후, 몇시간후 발생되기를 원할때이다. 사실 `UILocalNotification` 을이용하는 것도 하나의 방법이긴 하지만 문제는 `UILocalNotification` 은 확인을 해야만 해당 행동을 지정할 수 있다는 단점이 있다. </span>

<span style="font-size: 11pt;">  
</span>

<script src="https://gist.github.com/AhnSeongHyun/7578145.js"></script>

<span style="font-size: 11pt;">  
</span>  
<span style="font-size: 11pt;">  
</span>  
<span style="font-size: 11pt;">`NSTimer` 라는 객체를 생성하면서 시작을 하는데, </span><span style="background-color: transparent; font-size: 11pt; line-height: 2;">`scheduledTimerWithTimeInterval:` 메소드를 이용해서 타이머 작업을 예약하고 있다. TimeInterval 의 단위는 초(sec) 단위이고, selector 에서는 지정한 시간 이후에 발동될 타이머 핸들러 함수를 지정하면 된다. `userInfo` 는 `NSDictionary` 형태로 지정하면 되는데, 타이머 핸들러에 어떤 값을 전달할때 사용하면 해당 타이머 핸들러에서 전달받은 값을 가져와서 어떤 작업을 수행할 수 있다. repeats 부분은 한번만 수행할 것인지 여러번 수행할 것인지를 설정하는 부분이다. </span>

<span style="background-color: transparent; font-size: 9pt; line-height: 1.5;">  
</span>

<span style="font-size: 11pt;">핸들러 함수에서는 timer 의 userInfo 를 가져와서 전달한 값을 가져오고 `[timer invalidate]` 함수로 타이머를 정지하도록 하였다. 아주 기본코드인데, 사실 타이머는 이정도만 알아도 되는것 같다. 백그라운드로 들어갔을때나 블루투스와 같이 쓸때는 좀더 유의해서 사용하면 될듯. </span>



