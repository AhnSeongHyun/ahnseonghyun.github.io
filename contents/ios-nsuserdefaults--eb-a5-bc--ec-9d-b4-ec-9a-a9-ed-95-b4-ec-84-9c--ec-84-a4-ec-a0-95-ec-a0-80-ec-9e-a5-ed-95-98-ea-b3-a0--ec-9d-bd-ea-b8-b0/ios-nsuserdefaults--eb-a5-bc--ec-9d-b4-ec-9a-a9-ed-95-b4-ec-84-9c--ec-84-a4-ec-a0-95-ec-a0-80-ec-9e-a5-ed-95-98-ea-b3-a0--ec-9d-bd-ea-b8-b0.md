---
title: '(iOS) NSUserDefaults 를 이용해서 설정저장하고 읽기.'
author: 'ash84'
pub_date: '2013-02-01'
description: '어떤 값들은 파일에 저장하는 것이 맞지만 때로는 앱내에 설정으로 저장하는 편이 훨씬 나을수가 있다. 간단한 설정같은 경우에는 파일에 저장하는 것이 더 불편하고 그러한 부분을 구현하는 것이 번거로울수 있다. 그래서 iOS 에서는 NSUserDefaults 라는 것을 통해서 저장할 수 있도록 한다. 저장은 Key, Value형태로 저장이 된다. 아래의 코드를 보면 쉽게 이해할수 있다. 단, 저장할 경우에는 synchronize 를 해주어야 한다. 저장된 데이터는 앱이 삭제되기전'
featured_image: ''
tags: ['dev', 'iOS', 'IOS set settiings', 'NSUserDefaults', 'Objective-C', '설정 저장']
---
<span style="font-size: 11pt;">어떤 값들은 파일에 저장하는 것이 맞지만 때로는 앱내에 설정으로 저장하는 편이 훨씬 나을수가 있다. 간단한 설정같은 경우에는 파일에 저장하는 것이 더 불편하고 그러한 부분을 구현하는 것이 번거로울수 있다. 그래서 iOS 에서는 NSUserDefaults 라는 것을 통해서 저장할 수 있도록 한다. 저장은 Key, Value형태로 저장이 된다. 아래의 코드를 보면 쉽게 이해할수 있다. 단, 저장할 경우에는 synchronize 를 해주어야 한다. 저장된 데이터는 앱이 삭제되기전 까지 유효하다. </span>

<script src="https://gist.github.com/4655665.js"></script>



