---
title: '(iOS) 클래스를 통째로 저장하기, NSCoding'
author: 'ash84'
pub_date: '2013-05-03'
description: '단순히 문자열을 저장하는 것만으로 앱내 데이터 저장에는 확실히 한계가 있다. 그리고 문자열을 저장하고 읽어올때 다시 파싱을해서 읽어오는 방식은 그리 달갑지도 않고 빠른 앱 개발 방식에도 한계가 있다. 그래서 Objective-c 에서는 [NSCoding](https://developer.apple.com/library/mac/#documentation/Cocoa/Reference/Foundation/Protocols/NSCoding_Protocol/Reference/Refer'
featured_image: ''
tags: ['dev', 'IOS', 'NSCoding', 'objective-c nscoding protocol', '객체 저장', '클래스 저장', '파일 저장']
---


<span style="font-size: 11pt;">단순히 문자열을 저장하는 것만으로 앱내 데이터 저장에는 확실히 한계가 있다. 그리고 문자열을 저장하고 읽어올때 다시 파싱을해서 읽어오는 방식은 그리 달갑지도 않고 빠른 앱 개발 방식에도 한계가 있다. 그래서 Objective-c 에서는 [NSCoding](https://developer.apple.com/library/mac/#documentation/Cocoa/Reference/Foundation/Protocols/NSCoding_Protocol/Reference/Reference.html) 프로토콜을 준수하면 [NSKeyedArchiver](https://developer.apple.com/library/mac/#documentation/Cocoa/Reference/Foundation/Classes/NSKeyedArchiver_Class/Reference/Reference.html)를 이용해서 객체내 데이터를 쉽게 저장할수 있는 방법을 제시하고 있다. </span>

<span style="font-size: 11pt;">일단 아래와 같이 [NSCoding](https://developer.apple.com/library/mac/#documentation/Cocoa/Reference/Foundation/Protocols/NSCoding_Protocol/Reference/Reference.html) 프로토콜을 준수하는 코드를 만든다. 간단하게, 아래의 두 함수를 구현하면 된다. </span>

<span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;"></span>

<span style="font-size: 11pt;">  
<script src="https://gist.github.com/AhnSeongHyun/5508064.js"></script>  
</span>

<span style="font-size: 11pt;">encodeWithCoder 함수에서는 인코딩을 수행하는데, </span><span style="font-size: 11pt;">변수에 값을 저장할 키를 지정하면 된다. 이때 주의할점은 encode 함수를 변수의 형에 맞게 써주어야 한다는 점이다. initWithCoder 함수에서는 디코딩을 수행하는데 지정한 키를 전달해주면 값을 가져올수 있다. 이때 역시 형에 맞는 decode 함수를 사용하면 된다. </span>

<span style="font-size: 11pt;">이제 [NSKeyedArchiver](https://developer.apple.com/library/mac/#documentation/Cocoa/Reference/Foundation/Classes/NSKeyedArchiver_Class/Reference/Reference.html) 를 이용해서 데이터를 저장하고, 가져오는 부분을 만들어 보도록하자. </span>

<span style="font-size: 11pt;">  
<script src="https://gist.github.com/AhnSeongHyun/5508120.js"></script>  
</span>

<span style="font-size: 11pt;">saveArrayToFile 함수는 파일로 저장하는 함수인데, [NSKeyedArchiver](https://developer.apple.com/library/mac/#documentation/Cocoa/Reference/Foundation/Classes/NSKeyedArchiver_Class/Reference/Reference.html) 를 이용해서 저장대상 데이터(dataCollection, 이 안에는 n 개의 Saving 객체가 들어있다.</span><span style="font-size: 11pt;">)을 인코딩 한후, 인코딩된 데이터는 data에 들어가게되고, data는 지정한 파일명으로 저장되게된다. loadDataFromFile 함수는 반대로 지정한 파일에서 디코딩을 한후, </span><span style="font-size: 11pt;"> dataCollection 으로 가져오는 코드이다. </span>

<span style="font-size: 11pt;">한번 해보면 그리 어렵지 않은데, 단순히 plist로 문자열을 저장하는 방식에 비해서 복잡 스럽긴 하지만, 단순한 데이터가 아닌 하나의 클래스로 표현되어야만 하는 데이터를 문자열로 구분자를 넣어서 저장하는 것은 사실 무리수이다. 문자열을 저장하는 것과 다르게 위와 같이 저장하게 되면 파일을 열었을때 의미를 파악할수 있게 구성되어 있지는 않다는 것에 유의하자. </span>

<span style="font-size: 11pt;">**ps) 좀더 이해하기 쉽게 java의 serialization, python 의 pickle 같은 개념이라고 보면 된다. **</span>

<span style="font-size: 11pt;">**2013.09.03 상속관계에서의 NSCoding 프로토콜 구현 **</span>

<span style="font-size: 11pt;">상속관계에서 NSCoding 프로토콜을 구현할때에 주의사항이 있다. 당연한 이야기겠지만 encodeWithCoder 함수와 initWithCoder 함수에서 상위 클래스의 해당 함수를 호출해 주어야 한다. 그렇지 않으면 상속을 받은 클래스는 NSCoding 프로토콜을 구현시, 본인 클래스에 한해서만 저장 혹은 로드를 하는 문제점이 발생된다. </span>

<script src="https://gist.github.com/AhnSeongHyun/6433486.js"></script>



