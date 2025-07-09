---
title: '(iOS) Category 란?'
author: 'ash84'
pub_date: '2014-02-11'
description: ''
featured_image: ''
tags: ['category', 'dev', 'IOS', '상속', '카테고리 기능']
---

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>

#### 카테고리(Category)

<span style="font-size: 11pt;">– 어떤 클래스에 기능을 추가하는 방식 </span>

<span style="font-size: 11pt;">– 상속(inheritance)를 사용하지 않고, 어떤 클래스에 메소드만을 추가하는 방식</span>

<span style="font-size: 11pt;">– 상속과 다르게 변수는 추가할 수 없고, 메소드만 추가 가능함. </span>

####사용법

##### 파일명

<span style="font-size: 11pt;">– 기존클래스+확장이름</span>

<span style="font-size: 11pt;">– ex) NSString+Dollar, NSString+LongText</span>

##### 코드

<span style="font-size: 11pt;">  
</span>

<script src="https://gist.github.com/AhnSeongHyun/8910637.js"></script><span style="font-size: 11pt;">  
</span>  
<span style="font-size: 11pt;">  
</span><script src="https://gist.github.com/AhnSeongHyun/8910635.js"></script> 

##### 호출


– 호출시에는 확장 클래스를 import 한 상태에서 기존 클래스로 객체를 만들고 추가한 함수를 만들면 된다. 

<script src="https://gist.github.com/AhnSeongHyun/8910662.js"></script>

<span style="font-size: 11pt;">**Reference**</span>

<span style="font-size: 11pt;">– [http://theeye.pe.kr/archives/866](http://theeye.pe.kr/archives/866)</span>



