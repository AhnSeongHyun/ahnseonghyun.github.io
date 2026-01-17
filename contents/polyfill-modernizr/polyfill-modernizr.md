---
title: 'polyfill & modernizr'
author: 'ash84'
pub_date: '2016-01-24'
description: ''
featured_image: ''
tags: ['dev', 'modernizr', 'polyfill', 'tutorial', 'web-development']
---
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>


이렇게 정리하게 된 계기는 이전에 올린 [console.log() 의 IE7에 대한 이슈](http://ash84.net/2015/12/23/console-log-browser-support/)때문에 시작이 되었다.

> [@sh84ahn](https://twitter.com/sh84ahn) [https://t.co/aOTeHRNAIJ](https://t.co/aOTeHRNAIJ) 구버전 IE에서도 서비스를 사용한다면 이런 폴리필도 예비로 넣어두는 것도 좋을 것 같아요. 디버그 플래그를 같이 넣는다거나 번들링 도구로 제거하는게 가장 좋겠지만요 ㅎㅎ
> 
> — 용균 (@haruair) [2015년 12월 22일](https://twitter.com/haruair/status/679432210148024324)

<script async="" charset="utf-8" src="//platform.twitter.com/widgets.js"></script>

위와 같이 [haruair](https://twitter.com/haruair) 님이 폴리필에 대해서 언급해주시면서 개인적으로 잘 모르는 부분이라 정리를 한다.

####  polyfill 

- 필요 이유 : 브라우저가 여러가지가 생겨서, 브라우저 파편화가 발생됨. 비슷하게라도 결과를 보여줘야 하는데, 여러가지 방법을 동원, 이런 방식을 shim(끼움새), fallback 이라고 한다.
- Polyfill 이란 파편화를 보이는 브라우저에 삽입하는 자바스크립트 소스로 브라우저를 스스로 판별하여 해당 브라우저에 필요한 shim 을 알아서 끼워준다.
- 영국의 개발자 Remy Sharp 가 처음 용어를 사용하였다.
- poly(여러가지방법), fill(공백을 메운다.) 라는 의미 즉, 브라우저간의 지원 공백을 다양한 방법으로 메우는것.

#### [modernizr](http://modernizr.com)

![](https://farm2.staticflickr.com/1520/23942400513_ee25c1f352_o.png)

[http://modernizr.com](http://modernizr.com) 은 HTML5, CSS3 의 특징들을 조합해서 JS로 만들어 주는 도구이다. 아쉽게도 [console-polyfill](https://github.com/paulmillr/console-polyfill) 은 포함되어 있지 않다. 원래 modernizr 는 load 함수를 지원해서 다른 polyfill(modernizer)자바스크립트를 `load()`해서 쓸 수 있었는데(대부분의 한글 사용법이 이 방식을 설명), 추후 yepnope 라는 모듈을 통해서 지원해 왔었다.

<script src="https://gist.github.com/AhnSeongHyun/78eb7dd214161d405398.js"></script>

yepnope 가 개발유지를 하지 않으면서 [modernizr 에서도 더 이상 직접적인 로드(load)를 지원하지 않는다.](https://github.com/Modernizr/Modernizr/issues/1666) 즉, 제공하는 것 외에, 현재 브라우저에서 어떤 기능이 가능한가 가능하지 않은가는 판별할 수 있는데, 그에 관한 js 의 로드는 알아서 해야하는 것 같다.


10. [기타 HTML5 Polyfill 을 모아놓은 사이트](https://github.com/Modernizr/Modernizr/wiki/HTML5-Cross-browser-Polyfills)


