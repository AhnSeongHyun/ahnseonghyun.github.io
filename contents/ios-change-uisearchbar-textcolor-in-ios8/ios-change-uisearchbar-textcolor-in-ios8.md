---
title: '[iOS] Change UISearchBar TextColor in iOS8'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['dev', 'iOS8', 'TextColor', 'UISearchBar']
---


이상하게 가끔 objective-c 에서는 당연히 있을법한 함수를 제공하지 않는 경우가 있다. UISearchBar 에서 텍스트컬러를 변경하고 싶은데 stack overflow를 찾아보니 버전마다 조금씩 설정하는 방식이 다르다. 기존에는 subViews 를 루프 돌면서 UITextField 의 경우 찾는 방식이 있었는데 iOS8 에서는 먹히지 않는다.

<script src="https://gist.github.com/AhnSeongHyun/819fe8856e7371a39623.js"></script>



