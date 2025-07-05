---
title: '(iOS) TableViewCell 선택시, 색변경.'
author: 'ash84'
pub_date: '2015-09-24'
description: ''
featured_image: ''
tags: ['dev', 'how to change tabbar selected color', 'tabbar item color', 'UITabbarController']
---


<span style="font-size: 11pt;">SelectionStyle을 지정할 수 있는 것으로 알고 있는데, None, Gray, Blue 이렇게 지정할 수있는데 다른 색을 주는 방법을 찾아보니 아래의 방법이 있었다. cell 자체에 selectedBackgroundView 라는 속성에 새로 원하는 색을 가진 UIView를 만들어서 연결 시켜주면 된다. 커스텀 셀을 만들때에는 해당 클래스 안에서 넣어주면 된다.</span>

<span style="font-size: 11pt;"> </span>

<script src="https://gist.github.com/AhnSeongHyun/6561389.js"></script>



