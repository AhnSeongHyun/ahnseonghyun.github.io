---
title: '(iOS) Singleton + NSCoding 자주쓰는 방식 정리'
author: 'ash84'
pub_date: '2013-09-17'
description: '자주쓰는 나만의 방식(?) 이라서 정리하는 것인데, Singleton 을 이용하는 이유는 여러 클래스에서 하나의 객체로 접근하고 싶을때 사용하고 NSCoding 라이브러리를 이용해서 encoding, decoding 을 해서 save, load 함수에서는 사실상 아이폰 앱내 설정 `NSUserDefault` 를 이용해서 저장하고 읽어오면 편하'
featured_image: ''
tags: ['dev', 'NSCoding', 'NSDictionary', 'NSUserDefault', 'singleton']
---


<script src="https://gist.github.com/AhnSeongHyun/6595420.js"></script>

  
<span style="font-size: 11pt;">자주쓰는 나만의 방식(?) 이라서 정리하는 것인데, Singleton 을 이용하는 이유는 여러 클래스에서 하나의 객체로 접근하고 싶을때 사용하고 NSCoding 라이브러리를 이용해서 encoding, decoding 을 해서 save, load 함수에서는 사실상 아이폰 앱내 설정 `NSUserDefault` 를 이용해서 저장하고 읽어오면 편하기 때문이다. </span>

<span style="font-size: 11pt;">그외의 함수는 실제 가져오는 대상이 `NSArray`, `NSDictionary` 냐에 따라 다르긴 한데 함수의 대부분은 사실 이러한 객체들이 가지고 있는 함수명과 비슷하게 쓰는 편이다. 그래야 좀더 구현할때 쉽게 하나의 Objective-C 의 자료구조로 인식하게 되는것 같다. 보통 AppDelegate 에서 처음 앱이 시작할때 Singleton 객체를 생성을 하고 load함수로 저장되어 있는 것을 읽어오면서 시작한다. 그리고 `save`는 그때그때 다른데 보통 `add`, `remove` 이후 하거나 하면 된다. </span>



