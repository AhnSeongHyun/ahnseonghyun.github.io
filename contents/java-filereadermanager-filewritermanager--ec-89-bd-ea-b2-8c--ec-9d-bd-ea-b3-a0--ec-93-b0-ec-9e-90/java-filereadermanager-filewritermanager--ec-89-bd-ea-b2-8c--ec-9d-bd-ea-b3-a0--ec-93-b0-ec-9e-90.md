---
title: '[JAVA] FileReaderManager, FileWriterManager 쉽게 읽고 쓰자.'
author: 'ash84'
pub_date: '2012-11-05'
description: '자바에서 파일 읽고 쓰는 부분에 대한 정리차원에서 쓴다. 개인적으로 자주 쓰는 FileReaderManager, FileWriterManager 클래스를 올린다. 유틸리티 클래스(static  함수)로 중요한 부분은 현재 JVM 인코딩을 가져와서 읽고 쓰고 하는 부분이다. [이전 포스팅](http://ash84.tistory.com/783)에서도 언급했지만 findbug 플러그인을 통해서 걸러지는 부분이기도 하거니와 인코딩 문제는 미리 처리해주는게 문자열 관련 처리를 할때'
featured_image: ''
tags: ['dev', 'Java', '파일 쓰기', '파일읽기']
---
<span style="font-size: 11pt; ">자바에서 파일 읽고 쓰는 부분에 대한 정리차원에서 쓴다. 개인적으로 자주 쓰는 FileReaderManager, FileWriterManager 클래스를 올린다. 유틸리티 클래스(static  함수)로 중요한 부분은 현재 JVM 인코딩을 가져와서 읽고 쓰고 하는 부분이다. [이전 포스팅](http://ash84.tistory.com/783)에서도 언급했지만 findbug 플러그인을 통해서 걸러지는 부분이기도 하거니와 인코딩 문제는 미리 처리해주는게 문자열 관련 처리를 할때 좋다.(나중에 못찾는다.) writeLineToFile() 함수에서는 boolean 타입의 인자인 append를 받아서 이어쓰기를 할 것인지를 결정짓게 하였다. </span>

<script src="https://gist.github.com/4015504.js"></script>  
  
<script src="https://gist.github.com/4015503.js"></script>  
  
<script src="https://gist.github.com/4015500.js?file=gistfile1.java"></script>

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>


