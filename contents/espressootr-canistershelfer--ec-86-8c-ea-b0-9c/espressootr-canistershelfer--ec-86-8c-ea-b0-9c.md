---
title: '(espressoOtr) Canister/Shelfer 소개'
author: 'ash84'
pub_date: '2013-03-09'
description: ''
featured_image: ''
tags: ['Canister', 'espressoOtr', 'exs4j', 'Java', 'qsort', 'Shelfer', '문자열 탐색', '이진탐색']
---


<center>  
<iframe allowfullscreen="" frameborder="0" height="356" marginheight="0" marginwidth="0" mozallowfullscreen="" scrolling="no" src="http://www.slideshare.net/slideshow/embed_code/17052492" style="border:1px solid #CCC;border-width:1px 1px 0;margin-bottom:5px" webkitallowfullscreen="" width="427"></iframe><div style="margin-bottom:5px">**[Canister shelfer](http://www.slideshare.net/sh84ahn/canister-shelfer "Canister shelfer")** from **[SeonyHyun Ahn](http://www.slideshare.net/sh84ahn)**</div></center><span style="font-size: 11pt;">[espressoOtr](https://github.com/AhnSeongHyun/espressoOtr) 에는 Canister/Shelfer 라는 데이터 구조(클래스)가 있다. 위의 설명은 영어로 써서 잘 이해가 안될수도 있는데 간단하게 말하자면 문자열(String)을 위한 구조이다. 그런데 문자열을 제일 앞글자를 기준으로 n 개의 Canister 라는 클래스로 나누어서 저장을 하는것이다. </span>

<span style="font-size: 11pt;">이렇게 나누어서 저장을 하는 가장 큰 목적은 바로 **탐색시 적은 수의 데이터를 대상으로 탐색**을 하고자 하는 목적이다. 사실 이 구조의 고안 자체는 **자동완성**을 위해서 고안을 했었는데, 자동완성의 경우 앞 단어부터 비교를 해야하는 것이 기본이다. (물론 간혹 그러지 않은 경우도 있다.) **때문에 데이터 저장시에 앞 글자를 기반으로 문자열 데이터를 나눠서 저장을 하고, 저장을 할때 마다 내부적으로 정렬을 한다. **</span><span style="font-size: 11pt;">** 탐색시에는 우선적으로 앞 글자를 이진 탐색을 통해서 찾은 후, Canister 안에 있는 데이터에 대해서 다시 이진탐색을 해서 찾는 것이다. **</span>

<span style="font-size: 11pt;">장점은 위의 슬라이드에서도 명시 했지만, 자바의 List 컬렉션과 비슷하게 사용할 수 있었으면 해서 add(), size(), remove() 등의 익숙한 함수들을 작성을 했고, 데이터가 많은 경우 동일한 사이즈에 대한 데이터 탐색 시간은 당연히 적다. **물론 사이드 이펙트도 있다. 제일 앞글자가 같은 문자로 시작하는 단어가 엄청 많은 경우,  Shelfer 내 단일 Canister 에 데이터가 많이 늘어나서 탐색 시간의 개선 효과가 크지 않을 수도 있다. **</span>

<span style="font-size: 11pt;">아직 만든 나도 그렇게 많이 사용해 보진 않았지만, 현재 개발하고 있는 검색 컨텐츠 서버에 index 로 활용하기 위해서 적용중이다. 적용하고 개발하고 테스트 하면서 아마 좀더 필요한 함수가 추가되거나 성능이 개선될 것 같다. </span>



