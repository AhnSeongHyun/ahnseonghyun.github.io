---
title: 'DocumentExtractor 의 기본 구조'
author: 'ash84'
pub_date: '2012-09-05'
description: '국내 유명 업체의 문서추출기가 있겠지만, 굳이 hwp를 사용하지 않는다면 이용할 필요가 없다. 문서추출기(Document Extractor)에 대한 오픈소스가 많이 있지만 여기서 소개할 것은 Apache POI를 이용해서 좀더 쓰기 쉽게 만든 자바(java) 기반의 문서추출기인 [Document](https://github.com/AhnSeongHyun/DocumentExtractor)'
featured_image: ''
tags: ['Apache.poi', 'DocumentExtractor', 'github', 'Open Source', '문서 추출기', '오픈소스', '워드에서 문서 내용 추출']
---


<span style="font-size: 11pt; ">국내 유명 업체의 문서추출기가 있겠지만, 굳이 hwp를 사용하지 않는다면 이용할 필요가 없다. 문서추출기(Document Extractor)에 대한 오픈소스가 많이 있지만 여기서 소개할 것은 Apache POI를 이용해서 좀더 쓰기 쉽게 만든 자바(</span><span style="font-size: 11pt; ">java) 기반의 문서추출기인 </span>[Document](https://github.com/AhnSeongHyun/DocumentExtractor)<span style="font-size: 11pt; ">[Extractor](https://github.com/AhnSeongHyun/DocumentExtractor) 이다. 본 소스는 github 를 통해서 제공하고 있다. </span>

<span style="font-size: 11pt; ">  
</span>

<figure class="wp-caption aligncenter" style="width: 320px">![](http://ash84.net/wp-content/uploads/1/cfile23.uf.192A634050476F440625E3.jpg)<figcaption class="wp-caption-text">codercat</figcaption></figure>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">[Document](https://github.com/AhnSeongHyun/DocumentExtractor)</span><span style="font-size: 11pt; ">[Extractor](https://github.com/AhnSeongHyun/DocumentExtractor) 는 크게 **두 가지 파트**로 구성되어 있다. **하나는 Extractor**</span>**<span style="font-size: 11pt; "> 이고, 다른 하나는 Extractor</span><span style="font-size: 11pt; ">Manager</span>**<span style="font-size: 11pt; ">** 이다.** Extractor 는 인터페이스(Interface)로 현재는 2가지 구현 추상 클래스를 가지고 있다. 구현 추상 클래스는 문서에서  어떤 것을 추출할 것인지에 따라 ImageExtractor, TextExtractor 가 있다. 말 그대로 문서에서 이미지를 추출할지, 텍스트를 추출할지에 따라 구분된 것이다. 그리고 이 클래스들이 실제 각종 문서형식에서 이미지와 텍스트를 추출하는 작업을 한다. </span>

<span style="font-size: 11pt; ">ExtractorManager의 역할은 사용자가 쉽게 이미지 추출 혹은 텍스트 추출을 할 수 있도록 도와주는 역할을 한다. ExtractImage(), ExtractText() 함수를 제공하고 있으며, 각각의 함수는 전달된 파일경로 및 이름을 가지고 적절한 Extractor를 연결해 주는 역할을 한다. </span>

<span style="font-size: 11pt; ">먼저 Extractor 관련해서 클래스 다이어그램을 보자. </span>

![](http://ash84.net/wp-content/uploads/1/cfile6.uf.181D694E504760DA364704.png)

<span style="font-size: 11pt; ">이클립스의 ObjectAid 를 이용해서 코드에서 바로 추출한 클래스 다이어그램이다. 보시다시피 인터페이스는 아무런 역할도 하고 있지 않고, 각각의 Extractor 구현 추상클래스를 통해서 실제 로직이 움직인다고 보면된다. Extractor 인터페이스가 내용이 없음에도 두는 이유는 최대한 인터페이스를 활용하기 위함이다. </span>

<span style="font-size: 11pt; ">ImageExtractor, TextExtractor 구현 추상클래스는 부모클래스로 여러</span><span style="font-size: 11pt; "> 각각의 문서 형식에 맞게 상속받은 자식 </span><span style="font-size: 11pt; ">클래스를 가진다</span><span style="font-size: 11pt; ">. </span><span style="font-size: 11pt; ">TextExtractor 클래스를 상속받는 몇 개의 클래스를</span><span style="font-size: 11pt; "> 보자면 다음과 같다. </span>

![](http://ash84.net/wp-content/uploads/1/cfile30.uf.145E1947504769E105BE33.png)

<span style="font-size: 11pt; ">당연히 추상클래스에서 지정한 추상메소드를 구현하고 있는것을 볼 수 있다. ImageExtractor 역시 마찬가지의 구조로 되어 있다고 보면 된다. </span>

<span style="font-size: 11pt; ">  
</span>

![](http://ash84.net/wp-content/uploads/1/cfile23.uf.163D9939504B06542DA636.png)

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 15px; line-height: 29px;">ExtractorManager 클래스에 대해서 알아보자. 다이어그램이라고 보기에도 민망한 수준이지만 주목해야 할 부분은 ExtractText(), ExtractImage() 함수를 제공하고 있다는 점이다. 또한 private 함수로 파일 타입에 따른 텍스트 및 이미지 추출함수가 있다. public 으로 지정된 ExtractText() 와 ExtractImage() 에서 해당 함수들을 호출하는 구조이다. 쉽게 이해할수 있는 구조라고 생각된다. </span>

<span style="font-size: 15px; line-height: 29px;">[DocuemntExtractor](https://github.com/AhnSeongHyun/DocumentExtractor) 의 가장 최상위단 구조에 대해서 살펴보았다. 다음 포스팅에서는 실제 ExtractorManager를 이용해서 텍스트와 이미지를 추출하는 코드에 대해서 살펴보도록 하자. </span>

<span style="font-size: 15px; line-height: 29px;">  
</span>



