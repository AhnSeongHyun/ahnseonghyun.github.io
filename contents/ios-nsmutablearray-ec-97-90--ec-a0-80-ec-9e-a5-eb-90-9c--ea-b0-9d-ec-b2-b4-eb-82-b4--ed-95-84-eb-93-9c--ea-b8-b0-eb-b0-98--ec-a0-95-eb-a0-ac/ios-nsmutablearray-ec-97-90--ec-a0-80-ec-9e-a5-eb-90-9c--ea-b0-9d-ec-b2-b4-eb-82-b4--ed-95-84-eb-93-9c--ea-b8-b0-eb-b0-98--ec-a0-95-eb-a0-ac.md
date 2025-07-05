---
title: '(iOS) NSMutableArray에 저장된 객체내 필드 기반 정렬'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['dev', 'NSArray', 'NSMutableArray', 'sortUsingDescriptors', '정렬', '클래스 정렬']
---


<span style="font-size: 11pt;">이전에 포스팅에서 NSArray에 대한 String 에 대한 정렬을 하는 것에 대한 포스팅을 했었다. 사실 그렇게도 많이 쓰이긴 하지만, 어떤  데이터 자체를 하나의 클래스화 시키고 그 클래스에 대한 객체를 만들어서 자료구조, Array, List 등에 저장한 후에 정렬해야 하는 경우도 많다. 예를 들어, 아래와 같은 형식의 어떤 소셜데이터를 담는 클래스가 있다고 가정하자. </span>

<span style="font-size: 11pt;"><script src="https://gist.github.com/AhnSeongHyun/5049001.js"></script></span>

<span style="font-size: 11pt;">만약, 트윗수 혹은 랭킹순으로 정렬해서 보고 싶다면 어떻게 해야할까? 정렬을 하겠다는 것은 사실 어떤 관점에서 보겠다는 것에 대한 과정이라고 볼 수 있다. </span>

<span style="font-size: 11pt;"><script src="https://gist.github.com/AhnSeongHyun/5049022.js"></script> </span>

<span style="font-size: 11pt;">방법은 아주 간단한데 Objective-C에서 이미 제공하고 있다. 위에서 처럼 NSSortDescriptor 객체를 사용하는데 생성할때 정렬의 기준이 되는 필드 명을 initWithKey에 명시해 주고, ascending 여부를 결정한다. NO로 할 경우, 당연히 반대인  Descending 이 된다. 그리고 나서 객체가 들어있는 NSMutableArray 의 sortUsingDescriptors 함수의 인자로 생성한 </span><span style="font-size: 11pt; line-height: 2;">NSSortDescriptor 객체를 넣은 NSArray를 전달하면 자동으로 해당 필드명을 기준으로 정렬이 된다. **중요한 점은 정렬된 NSMutableArray가 반환되는 형식이 아니라, 호출한 그 자체가 정렬된다고 보면된다. **</span>



