---
title: '(python) opengraph 라이브러리 리뷰'
author: 'ash84'
pub_date: '2015-10-02'
description: ''
featured_image: ''
tags: ['dev', 'ExtendedOpenGraph', 'opengraph', 'pypi', 'Python', '오픈그래프', '파이썬']
---


<span style="text-align: justify; font-size: 11pt; line-height: 2;">사실 [오픈그래프](http://ogp.me)라는 것에 대해서 알게 된것은 </span>[전 포스팅](http://ash84.tistory.com/1000)<span style="text-align: justify; font-size: 11pt; line-height: 2;">에서 말했지만 우연한 기회였다. 난 그때만 해도 여전히 오픈그래프에 대해서 신기해하고 있던 터라 구글 검색을 해보았는데 파이썬 기반 오픈그래프 파싱 라이브러리가 있었고 분석했던 내용을 소개하고자 한다. </span>

<span style="font-size: 11pt;">인스톨은 아래와 같이 하면 되고 </span>

<div class="txc-textbox" style="border: 1px solid #cbcbcb; background-color: #ffffff; padding: 10px;"><span style="font-size: 11pt;">pip install opengraph </span>

</div><span style="font-size: 11pt;">사용하는 방법은 아래와 같다. </span>

<script src="https://gist.github.com/AhnSeongHyun/6010278.js"></script>

<span style="font-size: 11pt;">간단한 편인데, url=”http://facebook.com” 이렇게 url을 지정하는 방식 외에도 html 문자열 자체를 넣는 방식도 있으니 한번 참고해 볼만 하다. 이 오픈소스의 가장 좋은 기능이라면 단연 json 과 xml 로 변환을 해준다는 것도 있지만 `is_valid()` 함수를 통해서 오픈그래프 프로토콜의 준수여부를 알려준다는 것이다. **(난 사실 그것이 더 단점이라고 생각하기도 한다. 왜냐하면 오픈그래프 파서 라이브러리긴 하지만 페이스북에서는 오픈그래프 프로토콜이 없어도 웹 페이지에 대한 요약본을 만들수 있는데, 이 오픈소스는 그렇진 못하다.)**</span>

<span style="font-size: 11pt;">내부적으로 사용하는 라이브러리는 총 3가지인데, **re, urllib2, BeautifulSoup **이렇게 3가지이다. re 는 대부분 파이썬을 사용하시는 분들이라면 아실듯 한데, 정규표현식을 계산하는 라이브러리고, urllib2는 url 을 열어서 데이터를 가져오는 라이브러리다. 마지막으로 BeautifulSoup은 html 파싱 라이브러리로 사실은 파이썬에서는 HTMLParser 라는 내부 html 파싱 라이브러리를 제공하지만, </span><span style="font-size: 11pt; line-height: 1.5;">BeautifulSoup이 좀더 편하다고 알려져 있다. </span>

<span style="font-size: 11pt; line-height: 1.5;"> </span>

<span style="font-size: 11pt; line-height: 2;">**<span style="font-size: 12pt;">동작 방식</span>**</span>

<span style="font-size: 9pt; line-height: 2;"> </span>

<span style="font-size: 11pt; line-height: 2;">hrml 이냐 url 이냐에 따라서 갈라지긴 하지만, **결과적으로는 html 을 파싱하는 것이다.** 실행해 보면 알겠지만 사실 html 중에서도 부분만 파싱을 하는데 왜 이렇게 오래 걸릴까 하는 분들도 있겠지만 전체 데이터를 가져오기 때문에 오래 걸리는 것이다. 사실 파싱하는 양은 그리 많진 않다. urllib2 를 이용해서 데이터를 가져오고 </span><span style="font-size: 11pt;">BeautifulSoup을 이용해서 파싱을 하고 있다. </span>

<span style="font-size: 9pt;"> </span>

<span style="font-size: 15px; line-height: 29px;"> </span><span style="font-size: 15px; line-height: 29px;">`parser()`</span><span style="font-size: 11pt;"> 함수를 보면 정규표현식을 이용해서 property 속성에서 og 가 있는 것들을 추리고 그 안에서 og:title 이라고 하면 title 값을 가져와서 키값으로 사용하고 content 속성의 값을 해당 키에 대한 값으로 활용하고 있다. 그리고 그 키값들이 오픈그래프 프로토콜의 basic metadata 를 모두 포함하고 있는지를 확인함으로써 `is_valid()`를 판별하고 있다. </span>

<span style="font-size: 11pt;">하나의 파이썬 파일로 되어 있어서 보기엔 그리 어렵지 않고, 쓰기에도 적당한것 같다. pypi 에 가서 opengraph 를 쳐보면 실제로 가장 많은 weight를 가지고 있다.(약간 이름빨도 있는듯, 선점효과랄까) 웹페이지의 요약정보를 파싱하실 일이 있으면 사용하기 좋은 라이브러리다. </span>



