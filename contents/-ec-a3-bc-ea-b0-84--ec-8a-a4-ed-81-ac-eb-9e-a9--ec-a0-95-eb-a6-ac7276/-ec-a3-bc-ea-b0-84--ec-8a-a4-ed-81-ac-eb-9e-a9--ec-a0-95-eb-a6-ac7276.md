---
title: '주간 스크랩 정리(7/2~7/6)'
author: 'ash84'
pub_date: '2012-07-07'
description: ''
featured_image: ''
tags: ['C/C++', 'DevOps', 'KTH', 'memset', 'sqlite3', 'SQLITE3 명령어', 'Time', '배열 초기화', '성능튜닝', '실행시간 측정']
---


**<span style="font-size: 11pt; color: rgb(0, 0, 0); ">리눅스 실행시간 측정 명령어 time</span>**

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">time 실행명령어 </span>

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">이렇게 입력하면 실제 해당 프로그램에 대한 실행 시간을 커널 레벨과 유저 레벨로 확인 할 수 있습니다. 장점이라면 단연 코드안에 time_t 와 같은 시간 측정을 위한 코드를 쓸 필요가 없다는 것이겠죠?</span>

**<span style="font-size: 11pt; color: rgb(0, 0, 0); ">C/C++ 배열의 초기화 속도 </span>**

<span style="font-size: 11pt; "><span style="color: rgb(0, 0, 0); ">최적화 관련된 작업을 수행 중에 찾은 자료입니다. 간단히 말해서 for 문으로 배열을 초기화 하는 것 보다는 memset 을이용하는 것이 더 빠르다고 하네요. 링크 공유 합니다. </span>[<span style="color: rgb(0, 0, 0); ">http://ummae.tistory.com/168</span>](http://ummae.tistory.com/168)</span>

**<span style="font-size: 11pt; color: rgb(0, 0, 0); ">프로그래밍 성능 향상을 위한 C/C++ 튜닝</span>**

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">성능관련 자료를 찾다가, </span><span style="font-size: 11pt; color: rgb(0, 0, 0); ">삼성 SDS 멀티캠퍼스 </span><span style="color: rgb(0, 0, 0); font-family: Dotum; letter-spacing: -1px; line-height: 19px; font-size: 11pt; "> </span><span style="color: rgb(0, 0, 0); font-family: Dotum; letter-spacing: -1px; line-height: 19px; font-size: 11pt; ">“프로그래밍 성능 향상을 위한 C/C++ 튜닝” 교육을 요약한 자료라는 것을 찾았습니다. 성능 튜닝을 위해서라면 한번쯤 읽어보는 것도 좋을 것 같네요. </span><font color="#636363" face="Dotum"><span style="letter-spacing: -1px; line-height: 2; font-size: 11pt; color: rgb(0, 0, 0); ">http://seolis.tistory.com/99</span></font>

<span style="color: rgb(99, 99, 99); font-family: Dotum; letter-spacing: -1px; line-height: 2; ">  
</span>

<span style="color: rgb(99, 99, 99); font-family: Dotum; letter-spacing: -1px; line-height: 2; ">  
</span>

<font color="#636363" face="Dotum"><span style="letter-spacing: -1px; line-height: 2;">**<span style="font-size: 11pt; color: rgb(0, 0, 0); ">SQLITE3 명령어 </span>**</span></font>

<font color="#636363" face="Dotum"><span style="letter-spacing: -1px; line-height: 2;">  
</span></font>

<font color="#636363" face="Dotum"><span style="letter-spacing: -1px; line-height: 2;"><span style="font-size: 11pt; color: rgb(0, 0, 0); ">SQLITE3 파일 데이터베이스 인데, 주로 파일로 생성해서 바로 사옹했었는데, 명령어가 있다는 사실은 처음 알았네요. 간단하게 안에 내용 확인할 때, 굳이 viewer 설치 하는 것 보다 유용할 것 같네요. </span><span style="font-size: 11pt; ">[<span style="color: rgb(0, 0, 0); ">http://atticroom.tistory.com/15</span>](http://atticroom.tistory.com/15)</span></span></font>

<font color="#636363" face="Dotum"><span style="letter-spacing: -1px; line-height: 19px;">  
</span></font>

<font color="#636363" face="Dotum"><span style="letter-spacing: -1px; line-height: 2;">  
</span></font>

<font color="#636363" face="Dotum"><span style="letter-spacing: -1px; line-height: 2;">**<span style="font-size: 11pt; color: rgb(0, 0, 0); ">DevOps(디봅스)</span>**</span></font>

<font color="#636363" face="Dotum"><span style="letter-spacing: -1px; line-height: 2;">  
</span></font>

<font color="#636363" face="Dotum"><span style="letter-spacing: -1px; line-height: 2; font-size: 11pt; color: rgb(0, 0, 0); ">이번주에 유의깊게 읽은 DevOps 에 대한 링크입니다. KTH 쪽 링크가 대부분인데 최근에는 팀원을 모집하더군요. 서비스 운영과 개발을 병행하는 팀에 속하신 분이라면 꼭 읽어보세요. </span></font>

<font color="#636363" face="Dotum"><span style="letter-spacing: -1px; line-height: 2;">  
</span></font>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; "><div style="color: rgb(0, 0, 0); font-family: dotum; ">**<span style="font-size: 11pt; color: rgb(0, 0, 0); ">DevOps,  개발과 운영의 새로운 문화 </span>**</div><div style="color: rgb(0, 0, 0); font-family: dotum; ">[<span style="font-size: 11pt; color: rgb(0, 0, 0); ">http://dev.paran.com/2012/06/20/devops-new-trend-in-developement-and-operations/</span>](http://dev.paran.com/2012/06/20/devops-new-trend-in-developement-and-operations/)</div><div style="color: rgb(0, 0, 0); font-family: dotum; "></div><div style="color: rgb(0, 0, 0); font-family: dotum; ">**<span style="font-size: 11pt; color: rgb(0, 0, 0); ">DevOpsDays Mountain View 2012 Report #1 by KTH</span>**</div><div style="color: rgb(0, 0, 0); font-family: dotum; ">[<span style="font-size: 11pt; color: rgb(0, 0, 0); ">http://dev.paran.com/2012/07/02/devopsdays-mountain-view-2012-report-1-by-kth/</span>](http://dev.paran.com/2012/07/02/devopsdays-mountain-view-2012-report-1-by-kth/)</div><div style="color: rgb(0, 0, 0); font-family: dotum; "></div><div style="color: rgb(0, 0, 0); font-family: dotum; ">**<span style="font-size: 11pt; color: rgb(0, 0, 0); ">DevOpsDays Mountain View 2012 Report #2 by KTH</span>**</div><div style="color: rgb(0, 0, 0); font-family: dotum; ">[<span style="font-size: 11pt; color: rgb(0, 0, 0); ">http://dev.paran.com/2012/07/03/devopsdays-mountain-view-2012-report-2-by-kth/</span>](http://dev.paran.com/2012/07/03/devopsdays-mountain-view-2012-report-2-by-kth/)</div></div><font color="#636363" face="Dotum"><span style="letter-spacing: -1px; line-height: 2;">  
</span></font>

<font color="#636363" face="Dotum"><span style="letter-spacing: -1px; line-height: 2;">  
</span></font>

<font color="#636363" face="Dotum"><span style="letter-spacing: -1px; line-height: 2;">  
</span></font>



