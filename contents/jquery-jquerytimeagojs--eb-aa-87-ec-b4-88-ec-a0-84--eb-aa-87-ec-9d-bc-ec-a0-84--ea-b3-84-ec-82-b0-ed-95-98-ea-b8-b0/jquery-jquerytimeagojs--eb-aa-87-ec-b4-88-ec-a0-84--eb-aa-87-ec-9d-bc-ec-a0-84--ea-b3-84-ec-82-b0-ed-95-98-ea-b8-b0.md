---
title: '[jquery] jquery.timeago.js 몇초전, 몇일전 계산하기'
author: 'ash84'
pub_date: '2015-03-24'
description: '페이스북이나 최근에 SNS 및 뉴스에서는 특정 일자를 알려주기 보다는 과거의 상대성으로 시간을 표시한다. 예를들면 3일전, 2시간전 이렇게 말이다. 개발자가 일일히 보여지는 날짜 데이터에 대해서 계산해서 만들어 내야하는데 jquery.timeago.js 에서 이 기능을 지원해 준다. 
**사용법 **'
featured_image: ''
tags: ['dev', 'jQuery', 'javascript', 'relative time', 'timeago.js', 'tutorial']
---
<span style="font-size: 11pt;"></span><span style="font-size: 11pt;">페이스북이나 최근에 SNS 및 뉴스에서는 특정 일자를 알려주기 보다는 과거의 상대성으로 시간을 표시한다. 예를들면 3일전, 2시간전 이렇게 말이다. 개발자가 일일히 보여지는 날짜 데이터에 대해서 계산해서 만들어 내야하는데 jquery.timeago.js 에서 이 기능을 지원해 준다. </span>

<span style="font-size: 11pt;">**사용법 **</span>

<span style="font-size: 11pt;">[다운로드](https://github.com/rmm5t/jquery-timeago)를 받고 프로젝트에 넣은후 아래와 같이 html에서 링크를 걸어준다. </span>

<span style="font-size: 11pt;"><script src="https://gist.github.com/AhnSeongHyun/659c0e58a13c4de796f2.js"></script></span>

<span style="font-size: 11pt;">[홈페이지](https://github.com/rmm5t/jquery-timeago)에 보면 다양한 방식으로 사용하는 경우가 있는데, 나는 jquery에서 잡아서 변경하는 식으로 구현하였다. </span>

<span style="font-size: 11pt;"><script src="https://gist.github.com/AhnSeongHyun/63f22607c0807bd4735d.js"></script></span>

<span style="font-size: 11pt;">`span` 태그를 class tg 로 지정하고 그 안에 `data-date` 속성을 두고 원래 날짜 데이터를 두었다. 그리고 해당 속성 값을 가져와서 `timeago()` 를 이용해서 상대적인 과거시간을 가져오도록 하였다. 중요한 점은 한국어로 표시하기 위해서는 반드시 `jquery.timeago.ko.js` 를 링크를 걸어줘야 한다는 점이다. </span>



