---
title: '(iOS) UITextField와 키보드 액션'
author: 'ash84'
pub_date: '2013-02-01'
description: 'UITextField 를 누르게 되면 바로 키보드가 올라온다. 당연한 것인데 이유는 텍스트 입력을 위해서는 키보드가 필요하기 때문이다. 그런데 사용자가 입력하기 전에 뷰가 보여졌을때 바로 UITextField 에 커서가 옮겨지고 키보드가 올려지게 하려면 어떻게 해야할까? 아래의 코드처럼 FirstResponder 를 UITextField에 주면 된다.'
featured_image: ''
tags: ['dev', 'iOS', 'Keyboard', 'UITextField Keyboard', '키보드', '키보드 액션']
---
<span style="font-size: 11pt;">UITextField 를 누르게 되면 바로 키보드가 올라온다. 당연한 것인데 이유는 텍스트 입력을 위해서는 키보드가 필요하기 때문이다. 그런데 사용자가 입력하기 전에 뷰가 보여졌을때 바로 UITextField 에 커서가 옮겨지고 키보드가 올려지게 하려면 어떻게 해야할까? 아래의 코드처럼 FirstResponder 를 UITextField에 주면 된다. </span>

<span style="font-size: 11pt; line-height: 1.5;"><script src="https://gist.github.com/4655828.js"></script></span>

<span style="font-size: 11pt;">그렇다면 키보드를 내릴려면 어떻게 해야 할까? 단순하다. UITextField 에서 FirstResponder를 가져오면 돤다. 다음의 코드처럼 말이다. </span>

<span style="font-size: 11pt;"><script src="https://gist.github.com/4655868.js"></script></span>



