---
title: 'iOS7 beta4, 블루투스 관련 문제'
author: 'ash84'
pub_date: '2013-08-04'
description: '최근에 알바식으로 iOS7 앱 변경 작업을 하고 있는데 블루투스 쪽에서 좀 이상한 부분이 있어서 일단 포스팅을 한다. 문제의 현상은 `CBCentralManager` 객체를 통해서 주변의 블루투스 기기를 찾은후, 연결 하려는 기기에 대해서 연결을 한다음에 기기에 해당하는 객체인 `CBPeripheral` 에 writeValue 로 어떤 값을'
featured_image: ''
tags: ['CBCentralManager', 'CoreBluetooth', 'dev', 'ios6', '블루투스', '코어 블루투스']
---


<span style="font-size: 11pt;"></span><span style="font-size: 11pt;"></span><span style="font-size: 11pt;">최근에 알바식으로 iOS7 앱 변경 작업을 하고 있는데 블루투스 쪽에서 좀 이상한 부분이 있어서 일단 포스팅을 한다. 문제의 현상은 `CBCentralManager` 객체를 통해서 주변의 블루투스 기기를 찾은후, 연결 하려는 기기에 대해서 연결을 한다음에 기기에 해당하는 객체인 `CBPeripheral` 에 writeValue 로 어떤 값을 보내는데 그 다음에 unknown 에러가 발생하는 것이다. </span>

<span style="font-size: 11pt;">이 부분에 대해서 가장 큰 문제는 현재 iOS6 에서는 발생이 안된다는 점이고, pre-release 도큐먼트를 확인해 보면 몇가지 core bluetooth 부분에 추가되는 클래스나 함수 그리고  deprecated 되는 변수화 함수가 있는것 같은데, 그 부분과 내부적으로 영향을 미치는 지는 알수가 없으니 답답하다. </span>

<span style="font-size: 11pt;">https://devforums.apple.com/thread/190201?tstart=0</span>

<span style="font-size: 11pt;">Apple Developer Forums 에서도 이 부분은 확실히 버그라고 여기는 것 같다. 나 역시 같은 기기로 다은 iOS 탑재 아이폰5로 테스트 했을때 iOS6 에서는 문제가 발생되지 않는것을 확인하였다. 포럼에서는 연결된 디바이스를 아이폰 내 블루투스 설정에 들어가서 forget device를 해주어야 한다고 하는데, 좀더 테스트를 해봐야 할것 같다. </span>

<span style="font-size: 11pt;">beta4 가 나와서 gm 버전이 곧 나올것 처럼 사람들이 애기하곤 하는데.. 글쎼다. 블루투스 쪽도 약간의 문제가 있는것 같고 iOS7 beta4 를 설치해서 사용해 보면 iOS6 보다 이상하게 터치후 액션이 느린것을 확연하게 느낄수 있다. 또한 status 바 부분 역시 맥부기의 다른 프로그래머들도 아직은 수정할 단계가 아니라고 한다. </span>

<span style="font-size: 11pt;">좀더 지켜보자. iOS7.</span>



