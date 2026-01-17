---
title: '(Hadoop) standalone 모드에서 wordcount 실행하기.'
author: 'ash84'
pub_date: '2013-08-03'
description: 'wordcount 말 그래도 단어수를 세는 것으로 하둡의 기본적인 예제이다. 하둡의 hello world 라고 해도 좋을것 같다. 기본적으로 예제가 담긴 jar파일을 가지고 있어서 굳이 찾을 필요는 없고, 분석 대상 텍스트 파일을 input이라는 디렉토리에 넣어두자.'
featured_image: ''
tags: ['Hadoop', 'wordcount', 'wordcount 예제']
---
<span style="font-size: 11pt;">wordcount 말 그래도 단어수를 세는 것으로 하둡의 기본적인 예제이다. 하둡의 hello world 라고 해도 좋을것 같다. 기본적으로 예제가 담긴 jar파일을 가지고 있어서 굳이 찾을 필요는 없고, 분석 대상 텍스트 파일을 input이라는 디렉토리에 넣어두자. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; text-align: justify; line-height: 2;"><span style="font-size: 11pt;"></span><span style="font-size: 11pt;"></span><span style="font-size: 11pt;">./bin/hadooop jar hadoop-examples-1.2.0.jar wordcount </span><span style="font-size: 11pt;">input output</span>

</div><span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">이렇게 하면 실행이 되고 결과가 output 디렉토리에 떨어지게 된다. 결과는 part-r-00000 으로 나오는데 확인해</span><span style="font-size: 11pt;"> 보면, </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; text-align: justify; line-height: 2;"><span style="font-size: 11pt;"></span><span style="font-size: 11pt;">“Let    1</span>

<span style="font-size: 11pt;">—      17</span>

<span style="font-size: 11pt;">60      1</span>

<span style="font-size: 11pt;">Afghanistan.    1</span>

<span style="font-size: 11pt;">All     2</span>

<span style="font-size: 11pt;">America 4</span>

<span style="font-size: 11pt;">America’s       2</span>

<span style="font-size: 11pt;">…</span><span style="font-size: 11pt;"></span>

</div><span style="font-size: 11pt;">이런식으로 단어:</span><span style="font-size: 11pt;">개</span><span style="font-size: 11pt;">수 형식으로 나오는 것을 확인할 수 있다. </span>

<span style="font-size: 11pt;">주의할점은 wordcount 예제 실행시, **반드시 output 디렉토리는 완전 삭제된 상태여야 한다는 점**이다. 완전 삭제(내용포함)가 되어 있지 않으면 아래와 같은 에러를 뱉어낸다. 주의하시길. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; text-align: justify; line-height: 2;"><span style="font-size: 11pt; line-height: 1.5;">13/08/04 02:41:05 ERROR security.UserGroupInformation: PriviledgedActionException as:kall99 cause:org.apache.hadoop.mapred.FileAlreadyExistsException: Output directory output already exists</span>

<span style="font-size: 11pt;">org.apache.hadoop.mapred.FileAlreadyExistsException: Output directory output already exists</span><span style="font-size: 11pt;"></span>

</div>

