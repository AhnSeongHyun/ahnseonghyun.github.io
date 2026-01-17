---
title: '(iOS) UIAlertView TextField 추가 및 키보드 변경'
author: 'ash84'
pub_date: '2013-09-27'
description: '어떤 정보를 수정하거나 할때 뷰를 Navigation 으로 열어서 하는 방법들이 있겠지만 일단 가장 쉬운것이 팝업이고 iOS에서는 UIAlterView 로 그런것들을 대신할 수 있다. 여기서는 UIAlertView 에서 UITextField 를 사용하는 법을 정리하고자 한다.'
featured_image: ''
tags: ['TextField', 'UIAlertView', 'UIAlertView 텍스트필드 삽입', 'dev', 'ios-development']
---
<span style="font-size: 11pt;">어떤 정보를 수정하거나 할때 뷰를 Navigation 으로 열어서 하는 방법들이 있겠지만 일단 가장 쉬운것이 팝업이고 iOS에서는 UIAlterView 로 그런것들을 대신할 수 있다. 여기서는 UIAlertView 에서 UITextField 를 사용하는 법을 정리하고자 한다. </span>

<span style="font-size: 11pt;">  
</span>

<script src="https://gist.github.com/AhnSeongHyun/6722833.js"></script>

<span style="font-size: 11pt; line-height<br />: 2;">위의 코드에서 살펴보자면, `alertViewStyle` 라는 속성에서  `UIAlertViewStylePlainTextInput` 를 지정해 주면 된다. 그리고 나서 만약 내가 이름이 아니라 어떤 핸드폰 번호 같은 것을 입력하고 할때는 키보드 스타일을 변경해 주어야 한다. 10번째 줄처럼 `texfFieldAtIndex:` 메소드를 이용해서 `UIAlertView` 내 `UITextField` 에 접근하고 키보드 스타일을 변경해 주면 된다. </span>

 

Link : [UIAlertViewDelegate](https://developer.apple.com/library/ios/documentation/uikit/reference/UIAlertViewDelegate_Protocol/UIAlertViewDelegate/UIAlertViewDelegate.html)

</div>

