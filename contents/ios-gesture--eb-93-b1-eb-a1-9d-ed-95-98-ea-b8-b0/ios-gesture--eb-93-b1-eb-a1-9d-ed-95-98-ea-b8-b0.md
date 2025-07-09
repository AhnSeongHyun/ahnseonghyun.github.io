---
title: '(iOS) Register gesture'
author: 'ash84'
pub_date: '2013-05-03'
description: '요즘 대부분의 앱들은 Gesture를 지원하는 앱들이 많은데, iOS의 각 컨트롤에 Gesture 객체를 등록해 주면된다. Gesture 객체는 기본적인 설정을 해주고, 해당 Gesture가 발생했을때 수행할 함수를 지정해 주면 된다. 너무 쉽게 설명했는데, 사실 그게 단데. 예를 들어, 왼쪽으로 swipe gesture를 준다고 하자.'
featured_image: ''
tags: ['dev', 'gesture', 'IOS', 'objective c gesture recognizer', 'Swipe', 'tap', 'UIGesture', 'uilabel tap', 'uilabel touchupinside', '제스처']
---


<span style="font-size: 11pt;">요즘 대부분의 앱들은 Gesture를 지원하는 앱들이 많은데, iOS의 각 컨트롤에 Gesture 객체를 등록해 주면된다. Gesture 객체는 기본적인 설정을 해주고, 해당 Gesture가 발생했을때 수행할 함수를 지정해 주면 된다. 너무 쉽게 설명했는데, 사실 그게 단데. 예를 들어, 왼쪽으로 swipe gesture를 준다고 하자. </span>

<span style="font-size: 11pt;">  
<script src="https://gist.github.com/AhnSeongHyun/5508217.js"></script>  
</span>

<span style="font-size: 11pt;">일단 swipe는 UISwipeGestureRecognizer 객체를 이용해서 설정을 하는데 생성할때, @selector로 Gesture</span><span style="font-size: 11pt;">가 발생했을때 발동될 함수를 지정해 주면 된다. 위의 예제에서는 왼쪽 Gesture를 이용해서 webV</span><span style="font-size: 11pt;">iew에서 뒤로가기를 구현한 사례이다.  swipe 의 경우, 반드시 그 방향을 지정해 주어야 한다. 그리고 마지막으로</span><span style="font-size: 11pt;"> addGestureRecognizer 를 통해서 webView에 만든 gesture를 등록하면 된다. </span>

<span style="font-size: 11pt;">**다음으로  UILabel 에 Tap 에 대한 Gesture를 등록하는 작업을 해보자**. UILabel 은 원래 어떤 행위를 위한 컨트롤이 아니라 보기만을 위한 컨트롤이다. 그럼에도 불구하고 때론, 어떤 행위를 지정해 주고 싶을때가 있다. 예를들어, 눌렀을때 반응하도록 말이다. </span>

<span style="font-size: 11pt;">  
<script src="https://gist.github.com/AhnSeongHyun/5508290.js"></script>  
</span>

<span style="font-size: 11pt;">위의 코드를 보면 알겠지만 Tap은 Swipe와 달리 UITapGestureRecognizer를 사용한다. 그리고 설정시에 반드시, numberOfTapsRequired를 지정함으로써 </span><span style="font-size: 11pt;">몇번 Tap을 해야 Gesture 로 인지할것인지를 지정해야 한다. 그 외에는 모두 swipe와 같다. 그런데 아쉽게도 제대로 수행되지 않는다. 그 이유는 **UILabel에 UserInteractionEnabled 라는 속성때문이데, UILabel 의 경우 NO로 설정되어 있다. 때문에 제대로 된 기능을 위해서는 YES로 명시적으로 지정해 주어야한다. **</span>

<span style="font-size: 11pt;">Gesture를 만들고 연결하는 작업에 대해서 알아 보았는데, 여러가지 다른 Gesture가 있기 때문에 공식문서를 보면서 확인해 보는것도 좋을것같다. 세세한 동작을 지원하기 위해서는 방향과 행위의 횟수 등의 설정들을 지정해서 사용하면 가능할것으로 본다. </span>



