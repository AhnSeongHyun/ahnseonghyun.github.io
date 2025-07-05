---
title: '1) 구글 사이트를 이용해서 위키 만들기'
author: 'ash84'
pub_date: '2012-01-17'
description: ''
featured_image: ''
tags: ['google sites', '개발문서', '개인 개발 위키', '구글 사이트도구', '위키']
---


<div style="text-align: justify; line-height: 2; "><span style="font-size: 10pt; "><span style="font-size: 11pt; ">  
<span style="font-size: 11pt; ">  
</span><figure class="wp-caption aligncenter" style="width: 625px">![](http://ash84.net/wp-content/uploads/1/cfile22.uf.1648A33A4F15A04B31AB58.jpg)<figcaption class="wp-caption-text">언제봐도 Trac 은 멋지다. </figcaption></figure>

</span><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span><font color="#000000"><span style="font-size: 11pt; ">최근에 라이브러리를 만들면서 오픈 소스 형식으로 여러 사람들이 볼수 있는 위키 혹은 개발 문서 사이트를 만들고 싶었다. 처음에 택한 도구는 당연 </span></font><font color="#840000"><span style="font-size: 11pt; ">트랙(Trac)</span></font><font color="#000000"><span style="font-size: 11pt; ">이었다. 테터툴즈라는 좋아라하는 오픈소스 프로젝트의 도구로 쓰기도 했었고, 이전에 다녔던 회사에서도 사용했던 도구여서 괜찮을 거라 생각했다. 하지만 Trac의 단점은 위키부분만 분리해서 쓰기에는 조금 불편하다는 점이었다.(적어도 나에게는) </span></font>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>

<figure class="wp-caption aligncenter" style="width: 609px">![](http://ash84.net/wp-content/uploads/1/cfile1.uf.18300A444F15A08B151D90.png)<figcaption class="wp-caption-text">위키피디아</figcaption></figure>

</span><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span><font color="#000000"><span style="font-size: 11pt; "> </span></font>

</div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; "><span style="font-size: 11pt; "><font color="#000000"><span style="font-size: 11pt; ">두번째로 생각한 것은 </span></font><font color="#0686a8"><span style="font-size: 11pt; ">위키(WiKi) 사이트</span></font><font color="#000000"><span style="font-size: 11pt; ">이다. 위키피디아의 시스템도 개발 문서 및 오픈 소스 프로젝트 형식으로 괜찮을 것이라는 생각이 들었다. mediawiki 나 여타의 다른 위키를 찾아 봤지만, 가장 큰 문제는 서버에 대한 임대 문제이다. 회사에 설치 하자니 좀 캥기는 것도 있고, 왠지 모르게 호스팅 업체를 이용하자니 비용적인 부분이 부담이 되었다. </span></font></span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><font color="#000000">  
<span style="font-size: 11pt; ">  
</span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; "><span style="font-size: 11pt; "><font color="#000000"><span style="font-size: 11pt; ">그러던 중 찾은 것이</span>**<span style="font-size: 11pt; "> 구글 사이트 도구</span>**<span style="font-size: 11pt; ">이다. </span></font></span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><font color="#000000">  
<span style="font-size: 11pt; ">  
</span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; "><span style="font-size: 11pt; "><font color="#000000"><span style="font-size: 11pt; ">일단 로그인을 하고 사이트 도구를 누르면 바로 이런 화면이 나온다. </span></font></span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><font color="#000000"><span style="font-size: 11pt; "> </span></font><figure class="wp-caption aligncenter" style="width: 640px">![](http://ash84.net/wp-content/uploads/1/cfile10.uf.152F3F3E4F159EEC01BD82.png)<figcaption class="wp-caption-text">DocumentExtractor는 이미 작업중인 개발관련 위키이다.</figcaption></figure>

<span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><font color="#000000">  
<span style="font-size: 11pt; ">  
</span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; "><span style="font-size: 11pt; "><font color="#000000">  
<span style="font-size: 11pt; ">  
</span><span style="font-size: 11pt; ">  
 일단 만들기른 눌러보자. 만들기를 누르면 아래와 같이 템플릿과 이름을 작성할수 있는 부분이 나오게 된다. 먼저 템플릿 부터 보자. 템플릿은 가장 중요하다. 왜냐하면 기본적인 사이트의 레이아웃을 정하기 때문이다. 다양한 형식의 템플릿이 있지만, 우리의 목적인 위키이다. 검색 하다 “Wiki”</span></font></span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><font color="#000000">  
<span style="font-size: 11pt; ">  
</span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 15px; line-height: 29px;"><font color="#000000"><span style="font-size: 11pt; "> </span><figure class="wp-caption aligncenter" style="width: 640px">![](http://ash84.net/wp-content/uploads/1/cfile9.uf.1218743E4F159F03127CAA.png)<figcaption class="wp-caption-text">다양한 템플릿이 존재한다. </figcaption></figure>

</font></span><font color="#000000"><span style="font-size: 11pt; ">  
</span><span style="font-size: 11pt; ">  
</span>

</font>

</div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><font color="#000000">  
<span style="font-size: 11pt; ">  
</span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; "><span style="font-size: 11pt; "><font color="#000000"><span style="font-size: 11pt; ">다양한 형식의 위키 사이트를 볼 수가 있다. 일단은 가장 복잡해 보이지 않는 </span></font><font color="#ff8b16"><span style="font-size: 11pt; ">“Simple Wiki”</span></font><font color="#000000"><span style="font-size: 11pt; ">를 선택해보자. 해당 위키 템플릿을 선택하면 미리보기를 해 볼수도 있고, 또 바로 선택할 수도 있다. 일단 해당 템플릿을 선택하고 나면 이름을 정해야 한다. </span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>![](http://ash84.net/wp-content/uploads/1/cfile10.uf.126A78504F159F510EADF7.png)

</font></span><font color="#000000"><span style="font-size: 11pt; ">  
</span><span style="font-size: 11pt; ">  
  </span></font>

</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><font color="#000000">  
<span style="font-size: 11pt; ">  
</span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><font color="#000000"><span style="font-size: 10pt; "><span style="font-size: 11pt; "><span style="font-size: 11pt; ">여기서는 BaboWiki</span></span></span><span style="font-size: 9pt; "><span style="font-size: 10pt; "><span style="font-size: 11pt; "><span style="font-size: 11pt; "> 라는 이름으로 만들어 보도록 하자. 일단 입력하면 소문자의 형태로 url 이 자동적으로 생성된다. 물론 본인이 원하는 다른 url을 지정 할 수 있다. </span></span></span></span><span style="background-color: rgb(255, 255, 255); font-family: Arial, sans-serif; font-size: 11px; line-height: 17px; text-align: left; "><span style="font-size: 9pt; "><span style="font-size: 10pt; "><span style="font-size: 11pt; "><span style="font-size: 11pt; ">이 이름은 겹치면 안되기 때문에 잘 선택해서 쓰자. (원래는 TestWiki라고 지었으나 같은 이름이 있어서 거절되었다.)</span></span></span></span></span></font></div><span style="font-size: 11pt; ">  
</span><font color="#000000"><span style="text-align: left; background-color: rgb(255, 255, 255); line-height: 2; "><div style="text-align: justify;"><span style="font-size: 11pt; ">  
</span><font face="Arial, sans-serif"><span style="line-height: 17px;">  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>![](http://ash84.net/wp-content/uploads/1/cfile27.uf.123BA1484F159F6A061010.png)

</span><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>

</font></div><span style="font-size: 11pt; ">  
</span>

</span></font><font color="#000000" style="line-height: 2; "><span style="text-align: left; background-color: rgb(255, 255, 255); line-height: 2; "><div style="text-align: justify;"><span style="font-size: 11pt; ">  
</span><font face="Arial, sans-serif"><span style="line-height: 17px;">  
<span style="font-size: 11pt; ">  
</span></span></font></div><span style="font-size: 11pt; ">  
</span><font face="Arial, sans-serif"><div style="text-align: justify;"><span style="font-size: 11pt; ">  
</span><span style="font-size: 9pt; line-height: 2;text-align: justify;  "><span style="font-size: 10pt; "><span style="font-size: 11pt; "><span style="font-size: 11pt; ">이름을 입력하고 나서는 테마를 정할수도 있다. 그리고 기타 옵션이 있는데 해당 사이트에 대한 공개 및 보안 설정을 할 수가 있으며, 사이트에 대한 설명을 쓸 수도 있다. 그리고 성인 콘텐츠가 포함되어 있는지의 여부 역시 체크할수 있다.</span></span></span></span></div><span style="font-size: 11pt; ">  
</span>

</font>

</span></font><font color="#000000"><span style="text-align: left; background-color: rgb(255, 255, 255); line-height: 2; "><font face="Arial, sans-serif"><div style="text-align: justify;"><span style="font-size: 11pt; ">  
</span><span style="font-size: 9pt; line-height: 17px;text-align: justify;  "><span style="font-size: 10pt; "><span style="font-size: 11pt; "><span style="font-size: 11pt; "> </span></span></span></span></div><span style="font-size: 11pt; ">  
</span>

</font><div style="text-align: justify;"><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span><figure class="wp-caption aligncenter" style="width: 640px">![](http://ash84.net/wp-content/uploads/1/cfile3.uf.165DAA364F159F91061EBD.png)<figcaption class="wp-caption-text">짜잔!!</figcaption></figure>

<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify;"><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span><font face="Arial, sans-serif"><div style="text-align: justify;"><span style="font-size: 11pt; ">  
</span><span style="font-size: 9pt; line-height: 17px; "><span style="font-size: 10pt; "><span style="font-size: 11pt; "><span style="font-size: 11pt; "> 자, 이제 사이트를 만들었다. </span></span></span></span></div><span style="font-size: 11pt; ">  
</span>

</font>

<div style="text-align: justify;"><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span><font face="Arial, sans-serif"><div style="text-align: justify;"><span style="font-size: 11pt; ">  
</span><span style="font-size: 9pt; line-height: 17px; "><span style="font-size: 10pt; "><span style="font-size: 11pt; "><span style="font-size: 11pt; ">다음 시간에는 본격적으로 메뉴사용법과 개발 문서를 담을 수 있는 위키를 만들어 보도록 하자. </span></span></span></span></div><span style="font-size: 11pt; ">  
</span>

</font>

</span><span style="text-align: left; background-color: rgb(255, 255, 255); "><font face="Arial, sans-serif"><div style="text-align: justify;"><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

</font>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></span><span style="font-size: 11pt; "> </span></font>



