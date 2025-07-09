---
title: '(iOS) background/foreground, RemoteNotification 구별하기'
author: 'ash84'
pub_date: '2013-10-15'
description: ''
featured_image: ''
tags: ['Background', 'dev', 'foreground', 'IOS', 'Remote Notification', '백그라운드', '포그라운드']
---

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>

제목이 좀 난감한데;; 상황은 이렇게 Remote Notification은 말 그대로 원격지에서 알람이 오는것인데 애플의 경우 APNS를 통해서 이루어 지는데, 앱의 입장에서 보면 Remote Notification 을 받는 2가지 경우가 있다. 

**1. 앱이 켜져 있는 상태에서 Remote Notification이 오는 경우(foreground)** 

**2. 앱이 꺼져 있는 상태에서 Remote Notification이 오는 경우(background)**
 

이 두경우가 가장 큰 다른점은 앱이 foreground 에 있는 1번의 경우, 살펴보면 알림이 오긴 하지만 팝업이나 화면 상단의 표시되었다가 들어가는 식으로 동작하지 않는다. 라인(Line) 의 경우 다른 채팅창에 있는 경우 back버튼에 (1) 이런식으로 표시가 된다. 당연히 background 에서는 팝업이나 상단 표시가 된다.  또하나의 다른 점은 앱이 foreground에 있기 때문에 알림을 위한 json 에서 지정한 sound가 발생되지 않는다. 이때는 foreground 앱에서 따로 필요하다면 sound를 재생해 주어야 한다.  

 그런데 background 에서 알림이 왔고 사용자가 터치를 하면 앱이 켜지는데 이 상태에서 앱이 Remote Notification 을 받는 delegate는 아래와 같은데 foreground 에서도 아래의 메소드에 처리를 해야한다. </span>

```objective-c
– (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo
```

 그러다 보니 이런 문제가 생긴다. 예를들면, Remote Notification 이 왔을때 어떤 소리를 재생해줘야 한다고 할때 json 의  sound 지정된것을 iOS  에서 재생이 되고, foreground 에서는 iOS 가 json의 sound에서 재생해주지 않기 때문에 sound를 따로 재생을 해주는데 문제는 background 에서 알림이와서 눌러서 들어갈때도 이 sound가 다시 재생이 된다는 것이다.  

그래서 중요한 부분은 background 에서 알림이 왔을때 사용자가 알림을 눌러서 앱에 들어와서 알림을 처리하는 경우와 foreground 에서 알림이 와서 처리하는 경우를 구별해 주어야 한다. 아래의 코드를 보자.

<script src="https://gist.github.com/AhnSeongHyun/6988113.js"></script>

크게 다른것은 없는데 중요한 부분은 앱이 background 에 있거나 종료되었다가 실행되는 경우에는, UIApplication 의 `applicationState` 가 `UIApplciationStateInActive` 상태라는 것이고 foreground 는 당연히 `UIApplciationStateActive` 상태라는 것이 가장 큰 차이다. 그래서 해당 메소드에서 `application.applicationState` 로 구분해 주면 된다. 

 다른 경우 가 좀더 있을지 모르겠는데, 일단은 앱의 `applicationState` 를 이용해서 처리할수 있었다. 보다 좋은 방법이나 다른 경우가 있으면 댓글달아 주시길. 아니면 위의 gist를 수정해 주시는 것도 하나의 방법일듯.^^ 



