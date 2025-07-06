---
title: '[findbugs] FileWriter, FileReader DM_DEFAULT_ENCODING 처리하기'
author: 'ash84'
pub_date: '2015-07-03'
description: 'findbugs를 통해서 잠재적 위험 검사를 할때, 일반적으로 텍스트 파일을 읽거나 쓰는 코드에서 DM_DEFAULT_ENCODING 경고가 뜬다.'
featured_image: ''
tags: ['dev', 'DM_DEFAULT_ENCODING', 'encoding', 'FindBugs', 'Found reliance on default encoding', '정적분석툴']
---


<span style="color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">findbugs를 통해서 잠재적 위험 검사를 할때, 일반적으로 텍스트 파일을 읽거나 쓰는 코드에서 DM_DEFAULT_ENCODING 경고가 뜬다. </span></span>

<span style="color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span></span>

<script src="https://gist.github.com/3372046.js"></script>

 

<span style="color: rgb(51, 51, 51); font-size: 11pt; ">해당 잠재적 위험에 대한 내용을 살펴보면,</span>

<span style="color: rgb(51, 51, 51); font-size: 11pt; ">  
</span>

<div class="txc-textbox" style="border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-top-color: rgb(203, 203, 203); border-right-color: rgb(203, 203, 203); border-bottom-color: rgb(203, 203, 203); border-left-color: rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; ">**<span style="color: rgb(51, 51, 51); "><span style="font-size: 10pt; ">Bug</span></span>**<span style="color: rgb(51, 51, 51); font-size: 10pt; ">: </span>

<span style="color: rgb(51, 51, 51); font-size: 10pt; ">Found reliance on default encoding </span><span style="color: rgb(51, 51, 51); font-size: 10pt; ">in com.logamg.analysis.LogAnalysis.analysisLog(String): new java.io.FileReader(File) </span><span style="color: rgb(51, 51, 51); font-size: 10pt; line-height: 2; ">Found a call to a method which will perform a byte to String (or String to byte) conversion, and will assume that the default platform encoding is suitable. This will cause the application behaviour to vary between platforms. Use an alternative API and specify a charset name or Charset object explicitly.</span>

<span style="color: rgb(51, 51, 51); font-size: 11pt; ">  
</span>

**<span style="color: rgb(51, 51, 51); font-size: 10pt; ">Confidence</span>**<span style="color: rgb(51, 51, 51); font-size: 10pt; ">: High,</span><span style="color: rgb(51, 51, 51); font-size: 10pt; "> </span>**<span style="color: rgb(51, 51, 51); font-size: 10pt; ">Rank</span>**<span style="color: rgb(51, 51, 51); font-size: 10pt; ">: Of Concern (19)</span>  
**<span style="color: rgb(51, 51, 51); font-size: 10pt; ">Pattern</span>**<span style="color: rgb(51, 51, 51); font-size: 10pt; ">: DM_DEFAULT_ENCODING</span><span style="color: rgb(51, 51, 51); font-size: 10pt; "> </span>  
**<span style="color: rgb(51, 51, 51); font-size: 10pt; ">Type</span>**<span style="color: rgb(51, 51, 51); font-size: 10pt; ">: Dm,</span><span style="color: rgb(51, 51, 51); font-size: 10pt; "> </span>**<span style="color: rgb(51, 51, 51); font-size: 10pt; ">Category</span>**<span style="color: rgb(51, 51, 51); "><span style="font-size: 10pt; ">: I18N (Internationalization</span></span>

</div><span style="color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span></span>

<span style="font-size: 15px;"> </span>

<span style="color: rgb(51, 51, 51); font-size: 11pt; ">즉, 인코딩 지정에 대한 문제이다. 사실 위의 코드의 부분에서의 문제가 아니라, FileReader 나 FileWriter 를 BufferedReader, BufferedWriter 쓸때 문제가 생긴다. 즉, 이런식으로 말이다. </span>

 

<script src="https://gist.github.com/3372052.js"></script>

<span style="color: rgb(51, 51, 51); font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">인코딩 문제라는것은 알았는데, 대안 API(Alternative API)를 쓰라고만 나와서 약간 막막했는데, </span>

<span style="font-size: 11pt; ">다음과 같이 수정하면 된다. </span>

<span style="font-size: 15px; line-height: 22px;">  
</span>

<span style="font-size: 15px; line-height: 22px;">  
</span>

<script src="https://gist.github.com/3372056.js?file=gistfile1.java"></script>



