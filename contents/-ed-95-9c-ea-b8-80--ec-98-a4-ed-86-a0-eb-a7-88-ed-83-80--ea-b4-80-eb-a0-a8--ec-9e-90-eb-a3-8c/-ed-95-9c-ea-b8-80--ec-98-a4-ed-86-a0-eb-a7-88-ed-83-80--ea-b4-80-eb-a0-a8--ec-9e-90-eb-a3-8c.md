---
title: '# 한글 오토마타 관련 자료'
author: 'ash84'
pub_date: '2011-02-18'
description: ''
featured_image: ''
tags: ['Automata', '가상 키보드', '오토마타', '초성 중성 종성', '한글', '한글 오토마타']
---


<div style="text-align: justify; line-height: 2;"><span style="font-size:10pt;"><span style="font-family: Dotum; font-size: 11pt; "> 이번 프로젝트가 언어 및 문자에 관련된 것이라서 조합자 중에서 특히 우리나라 말의 경우 초성 중성 종성이 있는데 그것들이 실제로 프로그래밍의 어떤 컨트롤 상에서 제공이 제대로 되는 경우가 없습니다. 사용자의 키보드 입력은 제대로 처리 하지만, 마우스로 버튼을 눌러서 한글의 제대로된 입력을  하려고 한다면 초성 중성 종성 조합 알고리즘을 만들어야 하는데. 그와 관련된 자료 및 소스 코드 입니다. </span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="font-weight: bold; text-align: justify; line-height: 2;"><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>

<figure class="wp-caption aligncenter" style="width: 640px">![](http://ash84.net/wp-content/uploads/1/cfile1.uf.1129E33B4D612F1C010E44.jpg)<figcaption class="wp-caption-text">한글은 위대하다.  
</figcaption></figure>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span><span style="font-weight: bold; font-size: 11pt; ">C/C++에서 이용가능 한 자료 </span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt; ">  
</span>[](http://ash84.net/wp-content/uploads/1/cfile23.uf.177229334D6129FD354657.zip)cfile23.uf.177229334D6129FD354657.zip  
<span style="font-size: 11pt; ">– 모바일 프로젝트에서 이용 불가 </span></div><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; "></span>

<span style="font-weight: bold;"><span style="font-size: 11pt; ">C#에서 이용가능 한 자료   
</span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; text-align: justify; line-height: 2;"><span style="font-size: 11pt; ">  
</span>[](http://ash84.net/wp-content/uploads/1/cfile21.uf.1423C2364D612869226059.zip)cfile21.uf.1423C2364D612869226059.zip

<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span><span style="font-size:10pt;"><span style="font-family: Dotum; font-size: 11pt; ">– </span></span><span style="color: rgb(0, 0, 0); font-family: arial; line-height: normal; font-size:10pt;">[<span style="font-size:10pt;"><span style="font-family: Dotum; font-size: 11pt; ">http://codepedia.tistory.com/</span></span><wbr><span style="font-size:10pt;"><span style="font-family: Dotum; font-size: 11pt; ">42</span></span></wbr>](http://codepedia.tistory.com/42)</span>  
<span style="font-size: 11pt; ">  
</span><span style="color: rgb(0, 0, 0); font-family: arial; line-height: normal; font-size:10pt;"><span style="font-size:10pt;"><span style="font-family: Dotum; font-size: 11pt; ">– 모바일 프로젝트에서 이용가능</span></span></span>  
<span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; "></span>

  
<span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt; ">  
 MixString 라이브러리로 처음에 PC 버전을 개발 했는데, 약간 수정해서 개발을 했습니다. 수정은 동료가. 제가 저 라이브러리를 찾았거든요. 그리고 C# 기반의 모바일 프로그램에 해당 라이브러리를 쓰려고 하니까 데스크톱 프로젝트라서 만들 수 없다고 하더군요. 도저히 개발할 시간은 없구.. 해서 찾은게 두번째 라이브러리 입니다. 두번째 라이브러리에서는 특이하게 자판에 기초하고 있어서, 영문자를 Input() 함수에 넣어야 한글이 나오는 방식이더라구요. 예를 들면 “a” 를 입력하면 “ㅁ” 이 나오는 방식입니다. 만약 r 대신에 R을 누르면 “ㄲ” 이 나오는 방식입니다. </span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">점점 느끼는 것이지만, 역시 개발자들이 여러가지 결과물들을 블로그에 올리는 것이 좋다는 생각이 든다. 저작권 같은 개념도 중요하긴 하지만, 개발자는 자신이 개발해 봐야 안다. 그런데 모든것을 다 해볼 수는 없고, 책에서는 이론만 알려주기 떄문에 오픈소스, 커뮤니티, 블로그 등을 통해서 자신이 올린 소스를 보여주고 공유하는게 맞는것 같다. </span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">제가 올린 것 역시, 제가 만든건 아니지만 그래두 반드시 필요한 사람이 있을거라 믿기에.^^</span>  
<span style="font-size: 11pt; ">  
</span></div><div style="line-height: 2;"><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>



