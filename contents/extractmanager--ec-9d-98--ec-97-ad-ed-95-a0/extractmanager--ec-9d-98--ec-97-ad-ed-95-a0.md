---
title: 'ExtractManager 의 역할'
author: 'ash84'
pub_date: '2012-09-10'
description: ''
featured_image: ''
tags: ['DocumentExtractor', 'ExtractorManager', 'FACTORY', 'TextExtractorFactory', '팩토리패턴']
---


<span style="font-size: 11pt; ">ExtractorManager 가 굳이 필요한가? 에 대한 물음이 들 것이다. 왜냐하면 굳이 각 Extractor 이 파일타입에 따른 상세 구현 Extractor 클래스가 있고 그것을 그냥 쓰면 되지 않는가 하는 물음에서 이다. 그러나 필자가 ExtractorManager 를 만든 이유는 다음과 같다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; ">**1. 파일명을 모르는 상태에서의 텍스트/이미지 추출**

<span style="font-size: 11pt; ">2. 좀더 간편한(simple) 함수의 제공</span>

</div><span style="font-size: 11pt; ">**가장 중요한 부분은 1번의 이유다.** (2번은 모든 개발자가 원하는 것일뿐.) 어떤 문서내 데이터를 가져올때는 해당 문서가 어떤 형식인지 알면 당연히 해당 부분의 Extractor 클래스를 사용해도 무방하나, 그렇지 못한 환경이 더 많을 것으로 예상 되기 때문에 Extractor 클래스를 두었다. </span>

![](http://ash84.net/wp-content/uploads/1/cfile10.uf.117E9F48504B0994205556.png)

<span style="font-size: 11pt; ">클래스 다이어그램을 보면 </span><span style="font-size: 11pt; ">ExtractImage(), ExtractText() 함수를 가지고 있고, 해당함수를 호출해서 사용하면 된다. ExtractorManager 클래스는 두 가지 팩토리 클래스의 객체를 가지고 있는데, TextExtractor</span><span style="font-size: 11pt; ">Factory 와 ImageExtractor 가 그것이다. 해당 팩토리 객체들의 역할은 Exract~()함수에서 실제 Extractor 객체를 연결할 때, 파일 타입에 따라 알맞는 Extractor를 생성해서 반환한다. </span>

<span style="font-size: 11pt; ">다음의 예를 보자. </span>

<script src="https://gist.github.com/3672924.js"></script>

<span style="font-size: 11pt; ">위의 함수에서 보듯이, 팩토리 객체가 </span><span style="font-size: 11pt; ">createExtractor() 함수에 </span><span style="font-size: 11pt; ">FILETYPE</span><span style="font-size: 11pt; "> 값을 넘겨주고 있고, TextExtractor 객체로 파일 타입에 맞는 상세구현 TextExtractor 객체를 받고 있다. 만약 .docx 의 확장자를 가진 파일이 src_file_path 를 통해서 전달되면, FILETYPE 은 DOCX 가 될 것이고, DOCX 파일 타입에 맞는 </span><span style="font-size: 11pt; ">DOCTextExtractor 를 생성해서 전달해 줄것이다. </span>

<script src="https://gist.github.com/3672950.js"></script>

<span style="font-size: 11pt; ">원래는 이러한 파일 타입에 따라서 객체를 생성하는 부분이 ExtractorManager 에 있었는데, 지나치게 new 를 남발하는것 같아서 간단하게 팩토리 클래스를 구현함으로써 나름대로(?) 깔끔하게 정리된것 같다. 추가적으로 더 정리를 한다면, ExtractorManager 를 세분화 하는 방안도 있을 수 있다고 생각되고, 또는 팩토리 클래스는 추상화하는 방안 역시 있을 수 있을 것으로 예상된다. </span><span style="font-size: 11pt; line-height: 2; ">ImageExtractor 역시 마찬가지의 팩토리 클래스에서 객체를 받아와서 사용하는 방식으로 구현되어 있다. </span>



