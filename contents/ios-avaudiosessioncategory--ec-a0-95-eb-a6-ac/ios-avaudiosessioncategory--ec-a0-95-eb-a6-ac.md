---
title: '(iOS) AVAudioSessionCategory 정리'
author: 'ash84'
pub_date: '2013-09-17'
description: '다들 알다시피 AVAudioSession 이라는 것을 통해서 iOS 내에서 음악을 재생하는데 `AVAudioSessionCategory `라는 것에 대해서 알아둘 필요가있다. 이것이 왜 중요한지에 대해서 일단 일화를 설명하자면, 
알람소리(Remote Notification 이 아님)를 재생함에 있어서 아이폰 무음모드에서도 재생되는 문제점이 있어서 찾아보니 무음모드와 소리모드를 체크할수 있는 아래의 코드를'
featured_image: ''
tags: ['AVAudioSession', 'AVAudioSessionCategory', 'dev', 'iOS', 'ios7', 'MUTE', 'Objective-C']
---
<span style="font-size: 11pt;">다들 알다시피 AVAudioSession 이라는 것을 통해서 iOS 내에서 음악을 재생하는데 `AVAudioSessionCategory `라는 것에 대해서 알아둘 필요가있다. 이것이 왜 중요한지에 대해서 일단 일화를 설명하자면, </span>

<span style="font-size: 11pt;">알람소리(Remote Notification 이 아님)를 재생함에 있어서 아이폰 무음모드에서도 재생되는 문제점이 있어서 찾아보니 무음모드와 소리모드를 체크할수 있는 아래의 코드를 찾을수 있었다. </span>

<script src="https://gist.github.com/AhnSeongHyun/6589399.js"></script>

<span style="font-size: 11pt;">그런데 문제는 이 코드가 iOS5 부터는 정상동작 하지 않는다는 것이다. 그래서 iOS5 부터는 </span><span style="font-size: 11pt; line-height:2;">`AVAudioSessionCategory`라는 것을 통해서 음악 재생의 스타일을 지정할 수가 있다. 아래의 표를 보자. </span>

<span style="font-size: 9pt; line-height: 1.5;">  
</span>

![](http://ash84.net/wp-content/uploads/1/cfile2.uf.261B414E5237BB6D3929B1.png)

<span style="font-size: 9pt; line-height: 1.5;">  
</span>

<span style="font-size: 9pt; line-height: 1.5;">  
</span>

<span style="font-size: 11pt; line-height: 2;">원래 필자의 프로젝트에 지정되어 있던 것은 `AVAudioSessionCategoryPlayBack` 이었다. 이 설정에 대해 살펴보면 소리/무음에 따른 재생여부는  NO 로 되어 있는데 그렇기 때문에 무음모드에서도 재생이 되었던 것이다. 그 외에 다른 앱에서의 중복 실행 여부, Input(마이크) Output(스피커) 중 어떤것만 활성화 할것인지도 위의 표를 보게되면 알수 있다. </span>

<span style="font-size: 9pt; line-height: 1.5;">  
</span>

<span style="font-size: 11pt; line-height: 1.5;">지정하는 방법은 아래와 같다. </span>

<span style="font-size: 11pt; line-height: 1.5;">  
</span>

<script src="https://gist.github.com/AhnSeongHyun/6589393.js"></script>

<span style="font-size: 9pt; line-height: 1.5;">  
</span>

<span style="font-size: 11pt;">필자는 일단 무음모드에서의 실행이 되면 안되고, 다른 앱에서의 음악/소리 재생을 허용하지 않고, 스피커로 소리를 재생해야 하기 문에 `AVAudioSessionCategorySoloAmbient`를 설정하였다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">**Reference:**</span>

<span style="font-size: 14.545454025268555px; line-height: 26.363636016845703px;">– [http://inhome.tistory.com/52](http://inhome.tistory.com/52)</span>

<span style="font-size: 14.545454025268555px; line-height: 26.363636016845703px;">  
</span>

<span style="font-size: 9pt; line-height: 1.5;">  
</span>

<span style="font-size: 9pt; line-height: 1.5;">  
</span>



