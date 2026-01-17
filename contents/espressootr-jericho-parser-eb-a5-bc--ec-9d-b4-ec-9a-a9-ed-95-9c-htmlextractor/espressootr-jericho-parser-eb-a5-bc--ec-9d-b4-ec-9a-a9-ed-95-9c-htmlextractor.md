---
title: '(espressoOtr) jericho parser를 이용한 HTMLExtractor'
author: 'ash84'
pub_date: '2013-03-05'
description: 'HTML 파싱은 이제 어떤 서비스와 연동할때 필수적인 부분이 되었다. 그래서 쉽게 쓸수 있게 클래스화 해두면 좋은것 같아서 개인적으로 만들고 있는 [espressoOtr](https://github.com/AhnSeongHyun/espressoOtr) 이라는 자바 라이브버리에 jericho parser 를 이용해서 HTMLExtractor 클래스를 만들었다. jericho 파서는 자바기반 html parser 인데 쉽게 쓸수 있도록 되어 있다. [espressoOtr](htt'
featured_image: ''
tags: ['espressoOtr', 'HTML Parsing', 'HTML 파싱', 'Java', 'Jericho', '태그를 입력해 주세요.']
---
<span style="font-size: 11pt;">HTML 파싱은 이제 어떤 서비스와 연동할때 필수적인 부분이 되었다. 그래서 쉽게 쓸수 있게 클래스화 해두면 좋은것 같아서 개인적으로 만들고 있는 [espressoOtr](https://github.com/AhnSeongHyun/espressoOtr) 이라는 자바 라이브버리에 jericho parser 를 이용해서 HTMLExtractor 클래스를 만들었다. jericho 파서는 자바기반 html parser 인데 쉽게 쓸수 있도록 되어 있다. [espressoOtr](https://github.com/AhnSeongHyun/espressoOtr) 라이브러리에서는 다음과 같이 자주 사용하는 부분에 대해서 jericho 파서를 이용해서 util 클래스를 만들었다. 기본적으로 url 혹은 html String 을 인자로 받을수 있도록 함수를 설계하였는데 솔직한 심정으로 함수이름은 별로라서 몇번의 수정을 가해야 할것 같다. </span>

<script src="https://gist.github.com/AhnSeongHyun/5088957.js"></script>

<span style="font-size: 11pt;">함수가 몇개 되지 않아서 단위테스트를 걸어서 간단하게 나마 걸리는 시간에 대해서 측정을 해보니 주어진 url 안에 html 태그말고 문자열만 가지고 오는 함수</span><span style="font-size: 11pt;">와 <a> 태그를 찾아서 href 링크를 가져오는 함수가 다른 것들에 비해서 오래 걸렷다. 다른 것은 몰라도 href 가져오는 부분에서 body 태그안에 가져오는 등의 추가적인 개발이 필요할 것 같긴하다. </span>

<script src="https://gist.github.com/AhnSeongHyun/5088975.js"></script>

<span style="font-size: 11pt;">위의 XML은 jericho 파서의 maven dependency 이다. 이상하게 잘 안찾아져서 올리는데, 한번 HTML 파싱할일이 있으면 사용해보시길 바란다. </span>



