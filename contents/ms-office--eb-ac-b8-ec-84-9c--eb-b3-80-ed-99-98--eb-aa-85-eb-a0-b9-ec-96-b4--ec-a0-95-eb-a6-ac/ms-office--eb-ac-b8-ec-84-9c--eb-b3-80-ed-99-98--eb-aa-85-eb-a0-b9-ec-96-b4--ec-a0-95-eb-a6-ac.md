---
title: 'MS Office 문서 변환 명령어 정리.'
author: 'ash84'
pub_date: '2012-08-06'
description: ''
featured_image: ''
tags: ['Apache.poi', 'excelcnv.exe', 'ms document convertor', 'ppcnvcom.exe', 'wordconv.exe', '문서 변환', '워드 변환', '파워포인트 변환']
---


<span style="font-size: 11pt; font-family: Gulim, 굴림, AppleGothic, sans-serif; ">최근에 문서파일 내 텍스트 추출에 대한 [오픈소스(Apache.POI)](http://poi.apache.org/)를 패키징해서 테스트 하던 중에 비정상적인 MS 2003-2007 문서에 대한 내용추출이 안되는 문제가 있었다. 오픈소스 자체의 한계인지도 모르겠지만, 찾은 대안중에 하나가 바로 이러한 문서들을 상위버전의 문서로 변환해서 내용을 추출하는 것이다. 즉, ppt, doc, xls 등의 확장자를 가진 문서들을 pptx, xlsx, docx 로 만들어서 [오픈소스](http://poi.apache.org/)</span><span style="font-family: Gulim, 굴림, AppleGothic, sans-serif; font-size: 15px; line-height: 29px; ">[(Apache.POI)](http://poi.apache.org/)</span><span style="font-family: Gulim, 굴림, AppleGothic, sans-serif; font-size: 11pt; line-height: 2; ">로 내용을 추출하는 방식이다. </span>

<span style="font-size: 11pt; font-family: Gulim, 굴림, AppleGothic, sans-serif; ">일단 이 방식의 단점은 윈도우에서만 가능하다는 점인데, MS에서 제공하는 문서 변환기를 다운로드 받아야 한다. 링크는 다음과 같다. </span>

![](http://ash84.net/wp-content/uploads/1/cfile9.uf.16449446501DBE2630B154.jpg)

[<span style="color: rgb(68, 68, 68); font-family: Gulim, 굴림, AppleGothic, sans-serif; font-size: 11pt; ">http://w</span><span style="color: rgb(68, 68, 68); font-family: Gulim, 굴림, AppleGothic, sans-serif; font-size: 11pt; ">ww.microsoft.com/en-us/download/details.aspx?id=3</span>](http://www.microsoft.com/en-us/download/details.aspx?id=3)

<span style="font-size: 11pt; font-family: Gulim, 굴림, AppleGothic, sans-serif; ">위의 링크에서 받아서 설치한우, cmd(커맨드창) 명령어를 통해서 문서를 변환할수 있다. 명령어는 다음과 같다. </span>

<script src="https://gist.github.com/3372088.js"></script>

문서 추출 관련 오픈소스 링크 :[ https://github.com/AhnSeongHyun/DocumentExtractor](https://github.com/AhnSeongHyun/DocumentExtractor)

<span style="font-size: 11pt; "><span style="color: rgb(0, 51, 153); ">  
</span></span>



