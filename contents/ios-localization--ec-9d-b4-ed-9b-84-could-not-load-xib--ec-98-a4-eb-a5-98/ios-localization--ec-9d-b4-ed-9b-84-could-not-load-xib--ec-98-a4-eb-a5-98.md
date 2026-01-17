---
title: '(iOS) Localization 이후, could not load XIB 오류'
author: 'ash84'
pub_date: '2013-12-19'
description: '일단 이 문제의 전제는 처음에 언어가 en 으로 설정되어 있었다는 가정하에 출발을 한다. 필자가 겪은 상황은 이렇다. en으로 되어 있는 상황에서 한국어, 일본어 등이 추가된다. 그래서 나는 Localized.strings 파일을 만든다. 이 파일의 역할을 지역화를 하는데 있어서 키-값을 저장하는 역할을 한다. 즉, “NAME”=”NAME”; 이라고 저장을 하면 기존의 @”NAME” 을 그대로 넣었던 것에서 @”NAME”을 키로 해서 값을 가져와서 넣는방식으로 한다. 그리고'
featured_image: ''
tags: ['could not load XIB', 'dev', 'iOS', 'localization', '지역화']
---
<span style="font-size: 11pt;">일단 이 문제의 전제는 처음에 언어가 en 으로 설정되어 있었다는 가정하에 출발을 한다. 필자가 겪은 상황은 이렇다. en으로 되어 있는 상황에서 한국어, 일본어 등이 추가된다. 그래서 나는 Localized.strings 파일을 만든다. 이 파일의 역할을 지역화를 하는데 있어서 키-값을 저장하는 역할을 한다. 즉, “NAME”=”NAME”; 이라고 저장을 하면 기존의 @”NAME” 을 그대로 넣었던 것에서 @”NAME”을 키로 해서 값을 가져와서 넣는방식으로 한다. 그리고 나서 지역화를 위해서 한국어와 일본어를 추가하였다. 원래는 `viewController` 자체도 지역화를 할수 있는데 하지 않는다고 빼고, 모든문자열에 대한 지역화는 Localized.strings 에서 담당을 하도록 하였다. 앞서 한국어와 일본어를 추가했기 때문에 </span><span style="background-color: transparent; font-size: 11pt; line-height: 2;">Localized.strings 에도 한국어와 일본어를 추가할 수 있다. 추가하고 “NAME” = “이름”;  이런식으로 지정하면 지역화가 완료된다. </span>

<span style="background-color: transparent; font-size: 9pt; line-height: 2;">  
</span>

<span style="background-color: transparent; font-size: 11pt; line-height: 2;">필자가 겪은 문제는 이후에 발생이 된다. DEBUG 모드, 즉 개발자가 아이폰에 넣어서 테스트할때에는 별다른 문제가 생기지 않았는데 앱스토어에 올리고 승인된 이후, 새버전을 다운을 받아서 실행을 해보면 문제가 생긴다. 문제는 앱이 켜지자마자 CRASH가 떨어진다는 점이다. </span>

<span style="background-color: transparent; font-size: 11pt; line-height: 2;">  
</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="color: rgb(0, 0, 0); font-family: Arial, 'Liberation Sans', 'DejaVu Sans', sans-serif; font-size: 14px; line-height: 2; text-align: left; background-color: rgb(255, 255, 255);">Terminating app due to uncaught exception ‘NSInternalInconsistencyException’, reason: ‘Could not load NIB in bundle: ‘NSBundle /.app> (loaded)’ with name ‘MainWindow”</span>

</div><span style="background-color: transparent; font-size: 9pt; line-height: 2;">  
</span>

<span style="font-size: 11pt;">문제의 포인트는 iOS 앱에서 `rootViewController` 로 지정된 `viewController`의 xib 파일을 찾지 못해서 발생이 된다. </span><span style="background-color: transparent; font-size: 11pt; line-height: 1.5;">`initWithNibName` 으로 `UIViewController` 객체를 생성하는 경우 xib 파일의 이름을 넣어주는데 이 부분은 사실 컴파일 과정에서는 문제가 되지 않는다. 그렇다면 문제는 왜 발생한 것일까? </span>

<span style="background-color: transparent; font-size: 9pt; line-height: 2;">  
</span>

<span style="font-size: 11pt;">위의 필자가 했던 행위중에 `viewController` 자체를 지역화를 하지 않는다고 빼는 부분이 있는데 문제는 그 과정에서 단순히 지역화에서의 제외가 아니라 프로젝트 자체에서 제외가 된것이다. 실제로 에러 이후에 xcode 의 프로젝트를 살펴보니 해당 xib파일을 볼수가 없었다. </span>

<span style="font-size: 11pt;">복구 하는 방법은 당연히 xib파일을 넣어주면 되고 필자 같이 `viewController`를 지역화에서 제외한 경우에는 반드시 프로젝트를 확인해야 한다. 사실 아직도 의문인것은 왜 debug 과정에서는 문제가 생기지 않았느냐 하는 점이다. usb 케이블로 개발자 폰에 빌드를 해서 넣으면 잘 되는데, ipa파일로 만들어서 넣으면 안되는 요상한 경우였다. </span>

<span style="font-size: 11pt;">이번 계기로 사실은 테스트에 대해서 ipa 파일로 내부 테스트용을 배포하고 올려야 겠다는 생각을 하게 되었다. </span>



