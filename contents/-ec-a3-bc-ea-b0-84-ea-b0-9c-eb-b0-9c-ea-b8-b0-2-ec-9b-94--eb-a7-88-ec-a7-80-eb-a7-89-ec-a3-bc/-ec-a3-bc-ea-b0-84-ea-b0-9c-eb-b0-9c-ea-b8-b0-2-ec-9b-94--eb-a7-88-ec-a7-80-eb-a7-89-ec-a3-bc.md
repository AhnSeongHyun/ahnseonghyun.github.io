---
title: '#주간개발기, 2월 마지막주.'
author: 'ash84'
pub_date: '2013-03-01'
description: '마치 주간보고 쓰는 느낌이긴 한데, 꼭 에버노트에 스크립한 내용, 내가 몰라서 찾아 보았던 내용들을 매주 금요일 간단하게 나마 정리해 보는 것도 나중에 좋을것 같아서. 언제 끝이 날지 모르겠지만. 
**서버 **

**'
featured_image: ''
tags: ['안성현', 'developer', '주간개발기', '코딩중독', '코중이']
---
<span style="font-size: 11pt;"></span><span style="font-size: 11pt;"></span><span style="font-size: 11pt;">마치 주간보고 쓰는 느낌이긴 한데, 꼭 에버노트에 스크립한 내용, 내가 몰라서 찾아 보았던 내용들을 매주 금요일 간단하게 나마 정리해 보는 것도 나중에 좋을것 같아서. 언제 끝이 날지 모르겠지만. </span>

<span style="font-size: 11pt;">**서버 **</span>

**<span style="font-size: 11pt;">– </span><span style="font-size: 9pt; line-height: 1.5;"><span style="font-size: 11pt;">Data too long for column ‘title</span><span style="font-size: 11pt;">‘ at row 1</span></span>**

<span style="font-size: 9pt; line-height: 1.5;"><span style="font-size: 11pt;">: exs4j </span><span style="font-size: 11pt;line-height: 2;">검색결과를 저장하는 title 필드에 대해서 varchar(50)으로 설정했었는데, 그 부분을 넘어서는 결과가 들어왔을때 mysql에서 나는 에러였다. 단순하게 TinyText 형식으로 변경해서 해결.</span></span>

<span style="font-size: 9pt; line-height: 1.5;"><span style="font-size: 11pt;line-height: 2;">  
</span></span>

<span style="font-size: 9pt; line-height: 1.5;"><span style="font-size: 11pt;line-height: 2;">  
</span></span>

<span style="font-size: 9pt; line-height: 1.5;">  
</span>

<span style="font-size: 11pt; line-height: 1.5;">**– 다음 트위터 검색 OpenAPI 개발**</span>

<span style="font-size: 9pt; line-height: 1.5;"><span style="font-size: 11pt;line-height: 2;">: 오픈 이라고 하기엔 애매하지만 팀 서버에 자바로 HTML 파싱을 하고 데이터를 HTTP Get 방식을 이용해서 검색어를 전달하면 다시 결과를 json으로 전달받는 API를 만들었다. 처음 Tomcat+JSP 를 이용해서 웹 프로그랭(맞나?)을 해서 서버에 올렸다. 와르(.WAR)도 만들어보고. 여간 재밌는 경험이 아니였다. 이번주 단연 최고의 사건. 한가지 아쉬운점은 처음에 twitText 에 부분을 html 부분을 넣었었는데, 아이폰 앱에서 처리하기가 쉽지 않아서 보기하고 그냥 텍스트만 보여주는 방식으로 전환하였다. </span><span style="font-size: 11pt;"> </span></span>

<span style="font-size: 9pt; line-height: 1.5;"><span style="font-size: 11pt;">  
</span></span>

<span style="font-size: 9pt; line-height: 1.5;"><span style="font-size: 11pt;">  
</span></span>

<figure class="wp-caption aligncenter" style="width: 580px">![](http://ash84.net/wp-content/uploads/1/cfile23.uf.037D9E4E5130D1CA33BE18.jpg)<figcaption class="wp-caption-text">이번주 사진 : 당면은 넣지 말자. </figcaption></figure>

<span style="font-size: 9pt; line-height: 1.5;"><span style="font-size: 11pt;">  
</span></span>

<span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;"></span>

<span style="font-size: 11pt;">**아이폰 앱**</span>

<span style="font-size: 11pt;">**– 비동기 이미지뷰 소스**</span>

<span style="font-size: 11pt;">: 다음을 이용한 실시간 트위터 연동을 개발했는데, 문제는 앱의 테이블 뷰에서 이미지 url을 가져오는데 무척이나 버벅이는 부분이 있었다. 테이블뷰가 테이블셀을 그리는데, 이미지를 가져와야 하는 부분이 있어서 그런가 보다 싶었다. 만들어야 하나 말아야 하나 하다가 검색해보니 아래의 링크에 만들어 놓은 분이 있어서 가져다 씀. 버벅거림을 줄일수가 있다.(</span>[<span style="font-size: 11pt;">http://j0kers.tistory.com/157</span>](http://j0kers.tistory.com/157)<span style="font-size: 11pt;">)</span>

<span style="font-size: 11pt;">**– 만들고 있는 아이폰 앱 다시 재 심사 요청. **</span>

<span style="font-size: 11pt;">**기타 **</span>

<span style="font-size: 11pt;">**– 팀 소스 작업 몇가지 추가한 부분 정도. **</span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">그리 많이 쓰진 않았지만, OpenAPI 개발 틱한 작업을 프로토타입이지만 해 본 것이 가장 큰 경험이었던 한주였고, exs4j는 storing part, cli part 로 branch 를 나누어서 작업하기 시작했다. storing part 가 가장 주 목적으로 작업을 계속 이어나갈 예정이다. 앱작업은 일단 하나 올린상태이니 일주일은 벌었고, 다른 개발 중인 앱으로 돌아와서 다시 작업을 재개해야 할듯. </span>



