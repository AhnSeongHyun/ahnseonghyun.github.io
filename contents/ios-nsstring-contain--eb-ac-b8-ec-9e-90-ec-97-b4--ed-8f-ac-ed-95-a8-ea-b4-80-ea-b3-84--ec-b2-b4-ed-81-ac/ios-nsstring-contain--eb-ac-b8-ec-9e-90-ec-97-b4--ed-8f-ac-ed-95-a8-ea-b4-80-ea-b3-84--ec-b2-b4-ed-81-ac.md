---
title: '(iOS) NSString contain, 문자열 포함관계 체크'
author: 'ash84'
pub_date: '2013-01-29'
description: '은근히 하나의 문자열 안에 또다른 문자열이 포함되어 있는지를 체크해야 하는 경우가 많다. 예를 들어 어떤 url 에 acces_token=sflkjpsojfs 이러식으로 담겨서 온다고 가정해 보자. 해당 URL 문자열에 access_token 이라는 문자열이 포함되어 있는지 확인을 한뒤 split 으로 처리하는 것이 순서일 것이다. 문자열의'
featured_image: ''
tags: ['dev', 'iOS', 'NSString Contain', 'String contain']
---
<span style="font-size: 11pt;"></span><span style="font-size: 11pt;"></span><span style="font-size: 11pt;">은근히 하나의 문자열 안에 또다른 문자열이 포함되어 있는지를 체크해야 하는 경우가 많다. 예를 들어 어떤 url 에 acces_token=sflkjpsojfs 이러식으로 담겨서 온다고 가정해 보자. 해당 URL 문자열에 access_token 이라는 문자열이 포함되어 있는지 확인을 한뒤 split 으로 처리하는 것이 순서일 것이다. 문자열의 포함여부를 체크하는 코드는 아래와 같다. 아래의 코드에서는 rangeOfString: 으로 체크하고 있다. </span>

<script src="https://gist.github.com/4639461.js"></script>



