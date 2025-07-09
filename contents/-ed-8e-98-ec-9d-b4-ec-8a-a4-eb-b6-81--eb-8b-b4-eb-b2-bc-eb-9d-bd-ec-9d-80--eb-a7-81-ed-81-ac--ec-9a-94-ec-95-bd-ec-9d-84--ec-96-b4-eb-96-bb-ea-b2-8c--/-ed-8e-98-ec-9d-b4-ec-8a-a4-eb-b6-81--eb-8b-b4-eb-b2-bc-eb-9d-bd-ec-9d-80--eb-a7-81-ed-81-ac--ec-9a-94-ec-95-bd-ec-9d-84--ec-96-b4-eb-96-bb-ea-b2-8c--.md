---
title: '페이스북 담벼락은 링크 요약을 어떻게 가져올까?'
author: 'ash84'
pub_date: '2013-07-16'
description: '페이스북이 처음 내가 쓰게되었을 때 가장 신기했던 것은 친구를 찾는다는 것? 친구와 관계를 맺는 다는 것? 친구의 활동이 싸이월드처럼 내가 가서 확인해야 한다는 것? 그런 것들이 아니였다. **단 하나 신기했던 것은 글을 쓰는 창에 url 을 넣게 되면 요약(summary)가 나온다는 점이었다. **
그 당시 생각으로는 
**어떻게 저걸'
featured_image: ''
tags: ['facebook', 'open graph', '담벼락 링크', '오픈그래프', '웹페이지 요약', '페이스북']
---


<span style="font-size: 11pt;">페이스북이 처음 내가 쓰게되었을 때 가장 신기했던 것은 친구를 찾는다는 것? 친구와 관계를 맺는 다는 것? 친구의 활동이 싸이월드처럼 내가 가서 확인해야 한다는 것? 그런 것들이 아니였다. **단 하나 신기했던 것은 글을 쓰는 창에 url 을 넣게 되면 요약(summary)가 나온다는 점이었다. **</span>

<span style="font-size: 11pt;">그 당시 생각으로는 </span>

<span style="font-size: 11pt;">**어떻게 저걸 가져올 수가 있지? **</span>

<span style="font-size: 11pt;">**내가 url 입력을 기다리는 시간은 고작 2~3초 내외인데, 그 시간내에 url 에서 html을 가져와서 데이터를 추출하고, 분석해서, 만들어 낸다는 것 인가? **</span>

<span style="font-size: 11pt;">**역시 페이스북 대단해!! **</span>

<span style="font-size: 11pt;"> </span>

<span style="font-size: 11pt;">이런생각을 가지고 있었다. </span>

<span style="font-size: 11pt;">우연치 않게 포털사 코딩시험에서 HTML 파서를 만들라는 문제를 받게 되었고, 문제 분석을 위해서 각종 사이트들의 소스보기를 통해서 HTML 코드를 보던중 ** 태그 부분에서 <meta> 태그에 대해서 알게 되었다.** 특히 아래와 같은 부분에 대해서 말이다.(시험을 떨어졌지만, 코드는 남았다.)</span>

<script src="https://gist.github.com/AhnSeongHyun/6001123.js"></script>

<span style="font-size: 11pt;">og 가 무엇일까 찾아보니 [opengraph](http://ogp.me/) 의 약자이다. 그렇다면 [opengraph](http://ogp.me/)는 뭘까? 하고 구글신에게 찾아보니 잘 설명되어 있는 웹 페이지를 찾을수 있다. ([링크](http://ogp.me/))</span>

<span style="font-size: 11pt;">한 마디로 말하자면, </span>

<span style="font-size: 11pt;">OpenGraph Protocol 이라는 것은, 소셜 그래프 상에서 어떤 웹 페이지라도 rich object 가 되게 만든다. 너무 어렵게 올수 있을지 모르겠으나,** 내가 이해했을때는 meta 태그를 이용해서 **</span><span style="font-size: 11pt; line-height: 2;">**OpenGraph Protocol 상에서 정해놓은 값들을 지정해 놓는 것이다. 그 지정해 놓은 값들이 한마디로 그 웹페이지에 대한 요약을 나타내는 것이다. **</span>

<span style="font-size: 11pt;">기본요소와 옵션요소가 있다. </span>

<span style="font-size: 11pt;">기본 요소는 4가지로. 아래의 것이 그것이다. </span>

<div class="txc-textbox" style="border: 1px solid #cbcbcb; background-color: #ffffff; padding: 10px;">- <span class="s1" style="font-size: 10pt;">og:title</span><span style="font-size: 10pt;"> – The title of your object as it should appear within the graph, e.g., “The Rock”.</span>
- <span class="s1" style="font-size: 10pt;">og:type</span><span style="font-size: 10pt;"> – The </span>[<span class="s2" style="font-size: 10pt;">type</span>](http://ogp.me/#types)<span style="font-size: 10pt;"> of your object, e.g., “video.movie”. Depending on the type you specify, other properties may also be required.</span>

- <span class="s1" style="font-size: 10pt;">og:image</span><span style="font-size: 10pt;"> – An image URL which should represent your object within the graph.</span>

- <span class="s1" style="font-size: 10pt;">og:url</span><span style="font-size: 10pt;"> – The canonical URL of your object that will be used as its permanent ID in the graph, e.g., “http://www.imdb.com/title/tt0117500/”.</span>

</div><span style="font-size: 11pt;">위의 4가지가 기본적인 메타데이터이다. title은 말 그대로 현재 웹페이지의 타이틀을 나타내고, type은 웹페이지의 타입을 나타내는데, video, book, profile, website등이 있다. 하부적인 요소까지 지정할 수 있기 때문에 그 부분은 좀더 스펙을 보기를 바란다. image 는 웹페이지를 대표하는 이미지, url은 url 이다. </span><span style="font-size: 11pt; line-height: 1.5;">기타 description, determiner, locale 등의 다양한 메타데이터들을 추가적인 옵션 메타데이터가 있기 때문에 잘 보면 된다.</span>

<span style="font-size: 11pt;">**Reference**</span>

<span style="font-size: 11pt;">**– **[OpenGraph Protocol](http://ogp.me) </span>

<span style="font-size: 11pt;">– [페이스북 캐쉬 및 디버깅 관련 포스팅](http://blog.choyoungil.com/67)</span>



