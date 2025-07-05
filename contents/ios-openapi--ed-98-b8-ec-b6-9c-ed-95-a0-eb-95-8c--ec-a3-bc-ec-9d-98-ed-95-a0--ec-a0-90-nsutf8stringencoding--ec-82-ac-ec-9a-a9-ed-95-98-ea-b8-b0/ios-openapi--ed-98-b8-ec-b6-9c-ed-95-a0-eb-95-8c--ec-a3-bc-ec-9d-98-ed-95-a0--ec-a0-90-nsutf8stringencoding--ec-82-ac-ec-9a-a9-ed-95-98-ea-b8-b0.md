---
title: '(iOS) OpenAPI 호출할때 주의할 점. NSUTF8StringEncoding 사용하기'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['dev', 'IOS', 'Objective-C', 'OpenAPI', 'url encoding', '네이버 검색 API']
---


<span style="font-size: 11pt;">올해 한우찾기 v2.3.5 버전을 개발하면서 새로 넣은 기능이 바로 뉴스검색 기능이었다. 간단히 네이버 OpenAPI 검색 기능을 이용해서 한우관련 뉴스를 사용자가 직접 검색할 수 있도록 제공하는 기능이었는데 만드는 과정에서 특별한 문제가 있어서 이렇게 디버그 포스팅을 한다. </span>

<span style="font-size: 11pt;">보통 OpenAPI는 URL을 이용해서 값을 전달하는 방식을 이용한다. 예를들어 아래와 같은 URL과 같은 형식이다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">http://openapi.naver.com/search?key=776db6919965</span><span style="font-size: 11pt;">4df9385aa576bd4dcef&query=한우</span><span style="font-size: 11pt;">&target=news&start=1&display=10</span>

</div><span style="font-size: 11pt;">key부분을 따로 발급받아서 웹 브라우저에 붙이면 검색된 결과 10개가 RSS<XML)의 형식으로 보일것이다. 실제 한우찾기 내부 코드에서는 다음과 같은 코드를 이용해서 위의 URL을 던져서 결과를 파싱하는 방식으로 진행하였다. </span>

<span style="font-size: 11pt;">  
<script src="https://gist.github.com/4363290.js"></script>  
</span>

<span style="font-size: 11pt;">문제는 query 부분에 공백이 들어갈 경우에 생긴다. 예를 들어 한우가 아닌 **“한우 찾기”** 라고 query 부분에 입력을 해서 브라우저에 붙여보면 공백 부분에 **“%20”** 이라는 문자가 생긴것을 볼 수가 있다. 그래서 반드시 </span><span style="font-size: 11pt;">NSString 으로 URL을 구성하는 과정에서 마지막에 아래와 같이 </span><span style="font-size: 11pt;">**stringByAddingPercentEscapesUsingEncoding:**</span><span style="font-size: 11pt;">**NSUTF8StringEncoding** 작업을 해줘야 한다. 해주지 않으면 검색 시스템에서 공백인지를 인지하지 못해서 검색결과가 나오지 않는 문제가 생긴다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">  
<script src="https://gist.github.com/4363270.js"></script></span>



