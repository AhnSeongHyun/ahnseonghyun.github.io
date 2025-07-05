---
title: '(iOS) 로컬 HTML UIWebView 에 뿌리기.'
author: 'ash84'
pub_date: '2017-04-25'
description: ''
featured_image: ''
tags: ['dev', 'html file uiwebview', 'html string uiwebview', 'IOS', 'UIWebView']
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

UIWebView는 아이폰 프로그래밍에서 빠질래야 빠질수가 없는 컨트롤이다. 왜냐하면 웹 브라우저를 보여주지 않더라도 외부 API와 연동을 하더라도 요즘에는 대부분 OAUTH를 이용해서 자체 로그인 페이지를 이용하기 때문에  UIWebView를 안 쓸수가 없다. 그러나 굳이 서버에 있는 웹 페이지가 아닌, 내부에 있는 파일이나 데이터를 가지고 html을 만들어서 보여줘야 할 경우도 있다. 그럴 경우에는 아래와 같이 loadHtmlString: 함수를 호출하면 된다. 
 
<script src="https://gist.github.com/4639306.js"></script></span>

UIWebView는 3가지 로드 함수가 있는데, 일반적으로 사용하는 것은
loadRequest: 함수로 흔히 url String 을 NSURL로 변경해서 요청하는 방식으로 웹 페이지를 부른다. 일반적인 코드는 아래와 같다.  
 

<script src="https://gist.github.com/4639384.js"></script>

UIWebView의 Deletegate를 이용하면 UIWebView의 동작에 따라서 여러가지 행동들을 줄 수가 있다. 예를 들어 웹 페이지가 로딩되는 동안 로딩 화면을 보여주고 싶다면, `webView:shouldStartLoadWithRequest:navigationType:` 에서 처리하면 될 것이다. 다른 예로는 oauth를 이용해서 acess_token을 받아온다고 하면 `webViewDidFinishLoad:` 를 이용해서 웹 페이지 로딩이 끝난 시점에서 URL이나 HTML 자체를 확인해서 가져올 수도 있을 것이다.  
