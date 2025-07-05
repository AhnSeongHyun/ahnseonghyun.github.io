---
title: '(mysql) Data truncation: Data too long for column 'xxx' at row 1'
author: 'ash84'
pub_date: '2017-04-03'
description: ''
featured_image: ''
tags: ['data', 'dev', 'LONGTEXT', 'MySQL', 'text', 'TINYTEXT']
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
 mysql 데이터 넣는 부분에서 발생한 문제인데 xxx 는 내가 지정한 컬럼명이다.  

> Data truncation: Data too long for column ‘xxx‘ at row 1

 xxx 에 들어갈 데이터가 너무 크다는 이야기. TEXT 형으로 잡았었는데, 문제가 생겨서 보니 해당 필드는 어떤 웹 페이지 전체가 들어가는 컬럼이었다. TEXT도 적을까 해서 일단은 LONGTEXT 라는 형이 있어서 문제는 해결되긴 하였다.  


mysql 형 TEXT, LONGTEXT 에 대해서 찾아본  것을 정리한다.

4가지 TEXT 형이 있는데, 사이즈에 따라서 분류가 된다. 

<table align="justify" border="0" cellpadding="0" cellspacing="0" class="txc-table" style="border:none;border-collapse:collapse;;font-family:돋움;font-size:12.222222328186035px" width="604"><tbody><tr><td style="width:201;height:24;border-bottom:1px solid #ccc;border-right:1px solid #ccc;border-top:1px solid #ccc;border-left:1px solid #ccc;;"><span style="font-size: 11pt;"> 데이터 타입</span>

</td><td style="width: 201px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-top-width: 1px; border-top-style: solid; border-top-color: rgb(204, 204, 204);"><span style="font-size: 11pt;"> 필요저장공간</span><span style="font-size: 11pt;"> </span>

</td><td style="width: 201px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-top-width: 1px; border-top-style: solid; border-top-color: rgb(204, 204, 204);"><span style="font-size: 11pt;"> 최대저장가능 바이트수  </span>

</td></tr><tr><td style="width: 201px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"><span style="font-size: 11pt;"> </span><span style="color: rgb(102, 102, 102); font-family: 돋움, dotum, Helvetica, sans-serif; line-height: 14.53125px; font-size: 11pt;">TINYTEXT</span>

</td><td style="width: 201px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 11pt;"> 데이터바이트수 +</span><span style="font-size: 11pt;"> 1 바이트</span>

</td><td style="width: 201px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 11pt;"> 255</span>

</td></tr><tr><td style="width:201;height:24;border-bottom:1px solid #ccc;border-right:1px solid #ccc;border-left:1px solid #ccc;;"><span style="font-size: 11pt;"> </span><span style="color: rgb(102, 102, 102); font-family: 돋움, dotum, Helvetica, sans-serif; line-height: 14.53125px; font-size: 11pt;">TEXT</span>

</td><td style="width: 201px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 11pt;"> </span><span style="font-size: 11pt; line-height: 1.5;">데이터바이트수 +</span><span style="font-size: 9pt; line-height: 1.5;"><span style="font-size: 11pt;"> 2</span><span style="font-size: 11pt;"> 바이트</span></span>

</td><td style="width: 201px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 11pt;"> 64,535</span>

</td></tr><tr><td style="width:201;height:24;border-bottom:1px solid #ccc;border-right:1px solid #ccc;border-left:1px solid #ccc;;"><span style="font-size: 11pt;"> </span><span style="font-size: 11pt; line-height: 1.5;">MEDIUMTEXT</span>

</td><td style="width: 201px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 11pt;"> </span><span style="font-size: 11pt; line-height: 1.5;">데이터바이트수 +</span><span style="font-size: 9pt; line-height: 1.5;"><span style="font-size: 11pt;"> 3</span><span style="font-size: 11pt;"> 바이트</span></span>

</td><td style="width: 201px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 11pt;"> </span><span style="font-size: 11pt; line-height: 1.5;">16,777,215</span>

</td></tr><tr><td style="width:201;height:24;border-bottom:1px solid #ccc;border-right:1px solid #ccc;border-left:1px solid #ccc;;"><span style="font-size: 11pt;"> </span><span style="font-size: 11pt; line-height: 1.5;">LONGTEXT</span>

</td><td style="width: 201px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 11pt;"> </span><span style="font-size: 11pt; line-height: 1.5;">데이터바이트수 +</span><span style="font-size: 9pt; line-height: 1.5;"><span style="font-size: 11pt;"> 4</span><span style="font-size: 11pt;"> 바이트</span></span>

</td><td style="width: 201px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 11pt;"> 4,294,967,295</span>

</td></tr></tbody></table><font color="#666666" face="돋움, dotum, Helvetica, sans-serif"><span style="line-height: 14.53125px;">  
</span></font>

mysql의 TEXT타입은 오라클의 CLOB라고 하는 대용량 타입과 동일한 역할.

**사용해야 하는 경우**

– 해당 컬럼에 저장되는 내용을 예측할수 없는 크기일 경우

– 레코드의 전체크기가 64KB 를 넘어서서 더 큰 컬럼을 추가할수 없는 경우, 일부컬럼을 TEXT 로 대체 

**인덱스 생성 관련**

– TEXT 타입 컬럼에 대한 인덱스 생성시, 몇 바이트까지 인덱스 생성할것인 고려 필요.

– 문자집합의 만큼만 생성 가능.

**정렬 관련**

– 정렬 작업시, 컬럼 저장이 10MB저장되어 있더라도 mysql 서버의 ```max_sort_length``` 값만큼만 정렬을 수행


– 좀더 빠른 정렬을 위해서는 값을 줄이는 방법이 좋다.

**기타 사항**

– 임시 테이블 사용시, MEMORY 스토리지 엔진 사용시 TEXT 사용 불가. 

 – SELECT로 컬럼대상 조회시 전체 조회보다는 일부 조회시, ```CAST()```, ```SUBSTRING()``` 함수를 이용해서 VARCHAR 로 변경해서 조회하는 것이 좋을수도 있음. 

<span style="font-size: 11pt;">– INSERT, UPDATE 문장시, SQL자체가 길어지는 문제가 있을수 있는데, 이 경우 mysql 의 ```max_allowed_packet``` 설정에 따라서 이 값보다 크면 오류가 발생된다. 이런 경우 수정을 통해서 충분히 늘려주는 것이 좋다. </span>



