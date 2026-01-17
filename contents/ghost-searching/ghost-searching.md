---
title: '[Ghost] 검색기능 추가하기'
author: 'ash84'
pub_date: '2016-05-09'
description: 'Ghost 블로그를 사용한지도 몇개월이 되었는데, 마크다운 기반으로 작성하고 작성툴 역시 깔끔하지만 요상하게 2가지 부분에서 Ghost 블로그가 아쉬움이 있다. 하나는 **카테고리**고, 다른 하나는 **검색**이다. 

검색은 admin 상에서 제공하고 있기는 하지만, 블로그이면서 동시에 위키처럼 사용하기 때문에 가급적이면 블로그에서 검색이 이루어졌으면 하는 바램이었다. 아쉽게도 [ghost blog](http://blog.ghost.org) 에 가면 검색에 대한 부분은 [Swiftype](http://academy.ghost.o'
featured_image: 'https://images.unsplash.com/photo-1508161887025-ebd8f2813550?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=2f43153987d39aa20d3fc5f2053f4cf6&auto=format&fit=crop&w=1950&q=80'
tags: ['blog', 'custom search api', 'ghost', 'ios-development', 'python', 'search']
---
Ghost 블로그를 사용한지도 몇개월이 되었는데, 마크다운 기반으로 작성하고 작성툴 역시 깔끔하지만 요상하게 2가지 부분에서 Ghost 블로그가 아쉬움이 있다. 하나는 **카테고리**고, 다른 하나는 **검색**이다. 

검색은 admin 상에서 제공하고 있기는 하지만, 블로그이면서 동시에 위키처럼 사용하기 때문에 가급적이면 블로그에서 검색이 이루어졌으면 하는 바램이었다. 아쉽게도 [ghost blog](http://blog.ghost.org) 에 가면 검색에 대한 부분은 [Swiftype](http://academy.ghost.org/how-to-add-swiftype-search-to-your-ghost-blog/)을 이용하던지, [Google Custom Search](http://academy.ghost.org/how-to-add-google-custom-search-to-your-ghost-blog/) 를 이용하도록 안내하고 있다. 


<a data-flickr-embed="true"  href="https://www.flickr.com/photos/sh84ahn/27038657236/in/dateposted-public/" title="스크린샷 2016-05-17 오후 10.01.08"><img src="https://farm8.staticflickr.com/7223/27038657236_6c2c62b324_z.jpg" width="552" height="549" alt="스크린샷 2016-05-17 오후 10.01.08"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>


일단 Google Custom Search 를 이용해보려고 했다. 기본적으로 검색이 가능한 UI(input box+ 검색버튼)를 제공한다는 점이 처음에는 쉽게 느껴졌지만, 버튼을 없앨수 없고 무엇보다도 블로그의 테마와 충돌로 인해서 뭔가 아쉬운 느낌이 들었다. 그럼에도 불구하고 Custom Search 는 몇가지 디자인과 함께 검색 결과를 어떻게 보여줄 것인가를 선택 할 수 있는 화면을 제공하고 있다. 별도의 이슈가 없다면 Custom Search 를 붙이는 것을 추천한다. 


<a data-flickr-embed="true"  href="https://www.flickr.com/photos/sh84ahn/27006743132/in/dateposted-public/" title="스크린샷 2016-05-19 오전 7.50.47"><img src="https://farm8.staticflickr.com/7499/27006743132_c6fa6c4f14_z.jpg" width="640" height="422" alt="스크린샷 2016-05-19 오전 7.50.47"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>


뭔가 블로그 테마와 이질적이지 않은 느낌으로 검색화면을 만들고 싶다는 생각이 들었고, 사용자가 input 박스에 검색어를 입력하고 엔터를 치면 `/search?q=python` 이런식으로 전송이 되고 검색 결과가 보여지길 원했다. 이 부분은 위해서 **2가지를 사용하였는데 하나는 검색을 위한 API이고, 다른 하나는 Ghost 상에서 사용자 커스텀 페이지를 만드는 부분이다. **

####Custom Search API 를 이용하기####

Custom Search 의 경우 [API](https://developers.google.com/custom-search/json-api/v1/using_rest#making_a_request)로 구글에서 제공하고 있기 때문에 사용할 수가 있다. 기본적인 API 형식은 아래와 같다. 

`GET https://www.googleapis.com/customsearch/v1?key=INSERT_YOUR_API_KEY&cx=017576662512468239146:omuauf_lfve&q=lectures`


보면 알겠지만, **key 는  API KEY**를 의미하는데, 이것은 google developer console 에 들어가서 발금을 받으면 되고 **cx는 custom search engine ID**를 의미하는데, custom search engine 설정할때 발급이 되는 부분이다. 자세한 부분은 [가이드링크](https://developers.google.com/custom-search/json-api/v1/using_rest)를 참고하면 된다. 두개의 항목 외에 여러가지가 있겠지만, 가장 중요한건 `q`로 당연히 검색 키워드가 들어간다. 해당 API를 이용하게 되면 검색 결과를 JSON으로 받을 수 있고 이제 그것을 호출하고, 화면에 보여주기만 하면 된다. 

####Ghost Custom Page Template####

Ghost 는 기본적으로 자바스크립트의 **Handlebars** 를 이용해서 템플릿 파일들을 구현하고 있다. 그래서 페이지를 구성하는 파일들은 .hbs 파일확장자를 가지고 있다. .hbs 파일의 안을 보면 HTML, JS 그리고 Handlebars 에서 사용하는 템플릿 문법들이 있다. 

커스텀 페이지 템플릿을 만들기 위해서는 2가지 작업을 해야한다. 

1. `page-{{slug}}.hbs` 를 만든다. 즉, 내가 원하는 URL의 주소를 `{{slug}}` 부분에 붙여서 파일을 만든다. 해당 파일은 ghost 의 사용중인 theme 디렉토리의 하위에 있어야 한다. 

2. admin 에서 새 글을 쓰는데, 위에서 지정한 이름과 같게 Post URL을 지정하고, Static Page 의 형태로 저장한다. (Turn this post into a static page)

예를들면, `/search` 라는 커스텀 페이지 템플릿을 만든다고 하자. 그러면 일단 `page-search.hbs` 파일을 만들고, admin 에 가서 search 라는 Post URL로 정적 페이지를 만들어서 저장하면 된다. 그리고 나서 `/search` URL을 웹브라우저에 입력해 보면 해당 페이지가 나오는 것을 확인 할 수가 있다. 

블로그 화면의 사이드바 검색박스에서 키워드를 입력하고 엔터를 치면, `/search?q=keyword` 로 요청을 보내게 하였고, `page-search.hbs` 에서는 해당 키워드를 가져와서 Google Custom Search API 를 호출한후, 결과를 HTML 으로 보여주도록 하였다. 굳이 코드는 생략을 하는데 별 다른 코드는 없고, 해당 페이지 들어가자마자 Ajax 호출을 하고 결과를 그려주는 식이다. 


**이슈**

몇가지 아직 안되는 부분들은 페이징처리, 검색결과내 검색 키워드 하이라이팅 같은 기본적으로 검색에서 되어야 하는 부분들일것이다. 페이징처리는 Custom Search API에서 지원을 해주고 있고, 하이라이팅은 좀더 고민을 해봐야 할것 같다. 



