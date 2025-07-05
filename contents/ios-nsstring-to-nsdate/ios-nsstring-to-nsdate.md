---
title: '(iOS) NSString to NSDate'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['dev', 'IOS', 'NSDate 변환', 'NSString to NSDate']
---


<span style="font-size: 11pt;">데이터를 저장하다 보면  NSDate 를 결국 문자열의 형태로 저장할 수 밖에 없다. 당연히 텍스트 파일에 저장하니까 그런데, 다시 파일에서 데이터로 복원할때는 당연히 NSDate 형식으로 바꾸어서 써야 할때가 있다. 아래의 코드를 보자. </span>

<span style="font-size: 11pt;">  
</span>

<script src="https://gist.github.com/4639507.js"></script>

<span style="font-size: 11pt;">가장 중요한 부분은 포맷터의 설정이다. NSString to NSDate를 할때에는 NSDateFormatter를 이용해서 문자열을 어떤 형식의 NSDate 로 변경할 것인지를 설정해 주는 부분이다. 그래서 그 포맷터를 이용해서 NSString 을 NSDate로 변환하면 된다. </span>



