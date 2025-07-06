---
title: '(오픈소스) BasicUIWebViewController'
author: 'ash84'
pub_date: '2013-02-13'
description: '앱을 만들다 보면 주로 Naver, Daum Open API와 연동하는 경우가 많은데, 데이터를 가져오더라도 상세 데이터를 보려면 UIWebView를 쓸수 밖에 없다. BasicUIWebViewController 는 ViewController 에 웹 컨텐츠를 보여줄 수 있는 UIWebView 를 붙이고 해당 웹 컨텐츠가 로딩 될때의 진행상황을 표시해주기 위해서 UIProgressBar 를 붙였다. 또한 해당 웹 페이지의 타이틀(document.title)을 가져와서 제일 상단'
featured_image: ''
tags: ['BasicUIWebViewController', 'Opensource', 'WebViewController', '오픈소스']
---


<span style="font-size: 11pt;">앱을 만들다 보면 주로 Naver, Daum Open API와 연동하는 경우가 많은데, 데이터를 가져오더라도 상세 데이터를 보려면 UIWebView를 쓸수 밖에 없다. BasicUIWebViewController 는 ViewController 에 웹 컨텐츠를 보여줄 수 있는 UIWebView 를 붙이고 해당 웹 컨텐츠가 로딩 될때의 진행상황을 표시해주기 위해서 UIProgressBar 를 붙였다. 또한 해당 웹 페이지의 타이틀(document.title)을 가져와서 제일 상단에 보여주도록 하였다. 제일 상단은 툴바가 아닌 imageview를 붙이고 X 표시 역시 이미지 뷰이다. 해당 이미지를 클릭하면 ViewController 가 내려가도록 작업해 두었다. 코드를 github 에 들어가서 보면 알수 있듯이 별로 어려운 소스가 아니다. 다만 다른 개발자 분들이 귀찮으실까바 정리하는 의미에서 올린다. 라이센스 따위는 없다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;">github : [https://github.com/AhnSeongHyun/BasicUIWebViewController](https://github.com/AhnSeongHyun/BasicUIWebViewControllera)

</div>![](http://ash84.net/wp-content/uploads/1/cfile7.uf.145EA83F5119C16C0E6013.jpg)



