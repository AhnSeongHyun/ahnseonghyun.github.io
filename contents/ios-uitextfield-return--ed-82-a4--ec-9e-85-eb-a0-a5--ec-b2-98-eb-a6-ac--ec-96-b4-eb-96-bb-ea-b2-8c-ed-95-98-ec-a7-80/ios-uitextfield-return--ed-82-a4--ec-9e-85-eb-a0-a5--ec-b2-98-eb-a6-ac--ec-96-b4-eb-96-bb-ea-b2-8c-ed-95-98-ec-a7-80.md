---
title: '(iOS) UITextField, Return 키 입력 처리 어떻게하지?'
author: 'ash84'
pub_date: '2015-07-03'
description: 'UITextField 를 뷰에 넣은 상태에서 사용자가 누르면 당연히 텍스트 입력을 해야하니까 키보드가 올라오는데 그 상태에서 텍스트를 입력하고 나서 Return key를 누른다면 다양한 행동들을 해줘야한다. 카톡이라면 당연히 다음글로 넘어가야 할테도 어떤 앱에서는 그냥 바로 전송하는 경우도 있다. 이러한 행동을 해주기 위해서는 아래의 코드처럼 UITextFiledDelegate 의 t'
featured_image: ''
tags: ['dev', 'IOS', 'ios keyboard', 'keyboard enter', 'Keyboard return key', 'UITextField Keyboard', '엔터키 입력']
---


<span style="font-size: 11pt;">UITextField 를 뷰에 넣은 상태에서 사용자가 누르면 당연히 텍스트 입력을 해야하니까 키보드가 올라오는데 그 상태에서 텍스트를 입력하고 나서 Return key를 누른다면 다양한 행동들을 해줘야한다. 카톡이라면 당연히 다음글로 넘어가야 할테도 어떤 앱에서는 그냥 바로 전송하는 경우도 있다. 이러한 행동을 해주기 위해서는 아래의 코드처럼 UITextFiledDelegate 의 t</span><span style="font-size: 11pt; line-height: 1.5;">extFieldShouldReturn 에서 처리해 주면 된다. 아래의 코드는 .h 파일과 .m이 섞여있는 코드이니 주의해서 보길 바란다. </span>

<span style="font-size: 11pt; line-height: 1.5;">  
</span>

<span style="font-size: 11pt; line-height: 1.5;">  
</span>

<script src="https://gist.github.com/4586277.js"></script>



