---
title: '(Hadoop) 설치하기.'
author: 'ash84'
pub_date: '2013-08-03'
description: ''
featured_image: ''
tags: ['Hadoop', 'HDFS', '태그를 입력해 주세요.', '하둡', '하둡설치']
---


<span style="font-size: 11pt;">하둡을 그 많은 사람들이 설치 및 wordcount 예제 돌리는 부분을 올렸는데, 내가 올린다고 뭐가 그리 대단한 포스팅따위가 되리라고 생각하진 않지만, 자의반 타의반으로 정리해야 하는 상황에서 부족한 부분이 있겠지만 일단 정리한다. **<u>분명히 말해두지만, 개인정리용이고, mac osx  상에서 개인적으로 개발 테스트를 위함이니 따라하지 마시길. </u>**</span>

<span style="font-size: 11pt;">[http://apache.tt.co.kr/hadoop/common/hadoop-1.2.0](http://apache.tt.co.kr/hadoop/common/hadoop-1.2.0)</span>

<span style="font-size: 11pt;">미러링 위치인데, 현재(2013.08.03) 기준으로 1.2.0 버전이 release 버전이고 나머진 알파다. 실습은 역시 잘 알려진것으로 하는것이 대세. tar.gz 으로 압축되어 있는 것을 풀면 설치 끝. </span>

<span style="font-size: 11pt;">**실행하기 **</span>

<span style="font-size: 11pt;">실행하기 전에 **세 가지 모드**가 있다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 14.545454025268555px; line-height: 26.363636016845703px;">모드에 상관없이 hadoop/conf/hadoop-env.sh 파일에 JAVA_HOME을 잡아주기. </span>

<span style="font-size: 14.545454025268555px; line-height: 26.363636016845703px;">  
</span>

<span style="font-size: 14.545454025268555px; line-height: 26.363636016845703px;"></span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 14.545454025268555px; line-height: 26.363636016845703px;">export JAVA_HOME=/Library/Java/Home</span>

</div><div style="text-align: justify;"></div><div style="text-align: justify;"></div>**<span style="font-size: 11pt;">1.</span><span style="font-size: 11pt;"> stand-alone </span>**

<span style="font-size: 11pt;">– HDFS가 켜지지 않는 모드, 독립적으로 MapReduce 프로그램 로직 개발시 사용. </span>

<span style="font-size: 11pt;">– hadoop/conf/core-site.xml, </span><span style="font-size: 11pt; line-height: 1.5;">hadoop/conf/mapred-site.xml, </span><span style="font-size: 11pt; line-height: 1.5;">hadoop/conf/hdfs-site.xml 설정파일들에 아무것도 작성되지 않은상태, 즉, <configuration> 만 있고, <property> 가 없는 상태이다. </span>

<span style="font-size: 9pt; line-height: 1.5;">  
</span>

<script src="https://gist.github.com/AhnSeongHyun/6147120.js"></script>

<span style="font-size: 9pt; line-height: 1.5;">  
</span>

<span style="font-size: 11pt; line-height: 1.5;">– 명령어 </span>

<span style="font-size: 11pt; line-height: 1.5;">: hadoop/bin/hadoop 명령어로 실행. </span>

<span style="font-size: 11pt;">**2. pseudo-distribution(가상분산)**</span>

<span style="font-size: 11pt;">– 클러스터가 한대로 구성, 데몬도 한대에서 실행. </span>

<span style="font-size: 11pt;">– stand-alone 과의 가장 큰 차이는 HDFS 가 뜬다는 점. </span>

<span style="font-size: 11pt;">– 관련 설정 </span>

<span style="font-size: 11pt;">:</span><span style="font-size: 11pt; line-height: 1.5;"> </span><span style="font-size: 11pt; line-height: 1.5;">hadoop/conf/core-site.xml(name node 관련 설정)</span>

<script src="https://gist.github.com/AhnSeongHyun/6147125.js"></script>

<span style="font-size: 11pt; line-height: 1.5;">: hadoop/conf/mapred-site.xml(job tracker 관련 설정)</span>

<script src="https://gist.github.com/AhnSeongHyun/6147128.js"></script>

<span style="font-size: 11pt; line-height: 1.5;">: </span><span style="font-size: 11pt; line-height: 1.5;">hadoop/conf/hdfs-site.xml(hdfs 관련 설정)</span>

<script src="https://gist.github.com/AhnSeongHyun/6147129.js"></script>

<span style="font-size: 11pt;">: </span><span style="font-size: 11pt; line-height: 1.5;">hadoop/conf/masters</span><span style="font-size: 9pt; line-height: 1.5;"><span style="font-size: 11pt;">(secondary namenode 위치 설정, localhost 로 설정</span><span style="font-size: 11pt;">)</span></span>

<span style="font-size: 11pt;">: hadoop/conf/slaves(salve 노드의 위치 설정, localhost 설정</span><span style="font-size: 11pt;">)</span>

<span style="font-size: 11pt;">– 명령어 </span>

<span style="font-size: 11pt;">: 시작 </span><span style="font-size: 11pt;">hadoop/bin</span><span style="font-size: 11pt;">/start-all.sh </span>

<span style="font-size: 11pt;">: 종료 </span><span style="font-size: 11pt; line-height: 1.5;">hadoop/bin</span><span style="font-size: 9pt; line-height: 1.5;"><span style="font-size: 11pt;">/stop</span><span style="font-size: 11pt;">-all.sh </span></span>

<span style="font-size: 11pt;">**– full-distribution**</span>

<span style="font-size: 11pt;">: 실제 운영할때 여러대의 서버를 두고 운영하는 방식. 나중에 다루겠음. </span>



