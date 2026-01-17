---
title: '(exs4j) Convert DOM to JAXB'
author: 'ash84'
pub_date: '2013-02-14'
description: '기존의 ExternSearchEngine 이라는 긴 이름을 버리고 exs4j 라는 이름의 **검색 컨텐츠 서버** 오픈소스를 (아직은 저장이 안된다.) 만들게 된 계기 중 하나는 NHN의 오픈API 커뮤니티에 가면서 였다. 그냥 NHN 구경도 하고 OpenAPI가 뭐 별거 있나 하는 생각에 듣게 되었지만, 세미나 중에 DOM 파싱방식 보다는 Apache HttpClient 와 JAXB 를 활용하는 것이 메모리'
featured_image: ''
tags: ['exs4j', 'HttpClient', 'JAXB', 'Naver OpenApi', 'API']
---
<span style="font-size: 11pt;">기존의 ExternSearchEngine 이라는 긴 이름을 버리고 exs4j 라는 이름의 **검색 컨텐츠 서버** 오픈소스를 (아직은 저장이 안된다.) 만들게 된 계기 중 하나는 NHN의 오픈API 커뮤니티에 가면서 였다. 그냥 NHN 구경도 하고 OpenAPI가 뭐 별거 있나 하는 생각에 듣게 되었지만, 세미나 중에 DOM 파싱방식 보다는 Apache </span><span style="font-size: 11pt;">HttpClient 와 JAXB 를 활용하는 것이 메모리 적인 측면에서 좀더 좋다는 애기를 듣게 되었고, 기존의 DOM Parsing 방식을 버리고 JAXB로 바꾸면서 exs4j 라는 이름을 붙이게 되었다. </span>

<span style="font-size: 11pt;">먼저 이전의 DOM Parsing 코드 부분을 보자. </span>

<span style="font-size: 11pt;"></span>

<script src="https://gist.github.com/AhnSeongHyun/4951979.js"></script>

<span style="font-size: 11pt;">위의 코드는 Naver 검색 관련 Open API 파싱을 하는 부분인데, 각 target 에 따라서 parsing() 함수를 따로 두고 있으며, 함수에서는 Document 를 가져와서 item 이라는 태그를 찾고, 그에 따라서 item 하위에 있는 title, link, description 을 가져와서 TextSearchResult 객체에 넣고 있다. </span>

<span style="font-size: 11pt;">이 코드는 몇 가지 문제점을 지니는데, **가장 큰 문제점은 OpenAPI 요청 실패가 발생했을 경우에 대비가 안되어 있다는 점이다. **즉, Document는 가져올지 몰라도 item 태그를 찾지 못하는 문제가 있다. 또 하나의 문제는 유연성의 문제이다. 코드에서는 3가지 정보만 가져오고 있으나 더 많은 정보를 원하거나 item 상위에 있는 정보를 원할때에는 많은 코드 수정작업을 필요로 한다. </span>

<span style="font-size: 11pt;"><script src="https://gist.github.com/AhnSeongHyun/4952016.js"></script>  
</span>

<span style="font-size: 11pt;">위의 코드에서는 일단 **첫번째 문제점을 HttpStatus 를 확인함으로써 해결하고 있다.** 즉, 별도의 http 통신상의 문제가 발생한 경우라면, 데이터 가져오는 작업을 수행하지 않고 예외를 발생시키고 로그에 http  통신 오류를 표시한다. 두번째  문제의 경우, 아래의 코드를 보자. </span>

<span style="font-size: 11pt;"></span>

<script src="https://gist.github.com/AhnSeongHyun/4952054.js"></script>

<span style="font-size: 11pt;">위의 코드는 데이터를 받아오는 NaverNewsData 클래스이다. 이 클래스에서는 기존의 item 하위의 세 가지 항목만 가져오는 코드에서 좀더 확장 되어서 문서 전체를 클래스로 받아오는 클래스이다. 코드에서 볼수 있듯이, buildDate 등의 다양한 정보를 클래스로 가져올 수 있고, 추후에 필요한 데이터가 있을 경우, 이전 보다는 적은 범위의 코드 수정을 통해서 대처 할 수가 있다. </span>

<span style="font-size: 15px; line-height: 29px;">exs4j는 아직 완성된 상태가 아니다. 결정적으로 검색 질의에 대한 결과를 저장하는 부분과 함께 검색어에 대한 인덱스 관리 부분이 미개발된 상태이다. 아직 개발이 안된 이유는 기존의 ExternSearchEngine 은 exs4j와 달리 단순한 자바 라이브러리를 지향했기 때문이다. exs4j 로 이름을 바꾸면서 netty를 이용한 네트워크 통신 기능을 추가하였고, DOM Parsing 방식에서 JAXB로 변경한 상태이다. </span>

<span style="font-size: 15px; line-height: 29px;">  
</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 15px; line-height: 29px;">github : [https://github.com/AhnSeongHyun/exs4j](https://github.com/AhnSeongHyun/exs4j)</span>

<span style="font-size: 15px; line-height: 29px;">twitter: @exs4j</span>

</div><span style="font-size: 15px; line-height: 29px;">  
</span>



