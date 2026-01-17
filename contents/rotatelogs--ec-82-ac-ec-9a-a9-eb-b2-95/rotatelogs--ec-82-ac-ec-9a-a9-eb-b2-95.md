---
title: 'rotatelogs 사용법'
author: 'ash84'
pub_date: '2015-11-05'
description: '링크 : [https://httpd.apache.org/docs/2.2/ko/programs/rotatelogs.html](https://httpd.apache.org/docs/2.2/ko/programs/rotatelogs.html)

- Apache와 함께 자동 설치
- /usr/local/apache/bin/rotatelogs

 

#### **사용법**

rotatelogs [ -l ] logfile [ rotationtime [ offset ]] | [ filesizeM ]

 

#### **실행 옵션**'
featured_image: ''
tags: ['apache logs', 'dev', 'logrorate', 'roratelogs', 'tutorial']
---
링크 : [https://httpd.apache.org/docs/2.2/ko/programs/rotatelogs.html](https://httpd.apache.org/docs/2.2/ko/programs/rotatelogs.html)

- Apache와 함께 자동 설치
- /usr/local/apache/bin/rotatelogs

 

#### **사용법**

rotatelogs [ -l ] logfile [ rotationtime [ offset ]] | [ filesizeM ]

 

#### **실행 옵션**

 

<table class="confluenceTable tablesorter tablesorter-default stickyTableHeaders"><thead class="tableFloatingHeaderOriginal"><tr class="tablesorter-headerRow"><th class="confluenceTh sortableHeader" data-column="0" tabindex="0"><div class="tablesorter-header-inner">옵션</div></th><th class="confluenceTh sortableHeader" data-column="1" tabindex="0"><div class="tablesorter-header-inner">내용</div></th></tr></thead><tbody><tr><td class="confluenceTd">-l</td><td class="confluenceTd">GMT 대신 지역시간을 사용한다. (BST or DST)</td></tr><tr><td class="confluenceTd">logfile</td><td class="confluenceTd">로그파일의 경로, ‘%’ 가 있으면 strftime(3)의 형식 문자열로 처리, 없으면,초단위 시간 .nnnnnnnnnn을 자동으로 붙인다.</td></tr><tr><td class="confluenceTd">rotationtime</td><td class="confluenceTd">로그파일을 순환할 초단위 시간. 24시간=86400</td></tr><tr><td class="confluenceTd">offset</td><td class="confluenceTd">UTC에서 분단위 시간차이. 생략하면 0으로 가정하여 UTC를 사용한다.  UTC -5 => -300</td></tr><tr><td class="confluenceTd">filesizeM</td><td class="confluenceTd">시간이 아닌 크기를 지정, 최대 파일크기 뒤에 `M`을 붙인다. rotationtime과 offset 대신 이 파라미터를 사용한다.</td></tr></tbody></table> 

- 파이프를 이용해서 아파치의 access, error 로그를 아파치가 직접 쓰지 않고 rotatelogs 가 수행한다.
- Apache 는 서버가 시작할때 파이프로 연결된 rotatelogs 를 실행하고, 죽으면 다시 시작시킨다.
- 파이프로 연결된 로그 프로세스(rotatelogs) 는 Apache httpd 부모 프로세스에서 실행하기 때문에 보통 root로 실행되고 해당 프로세스의 PPID 가 Apache httpd 부모 프로세스의 PID 이다.

 

#### **사용의 예**

 

ErrorLog "|/usr/local/apache/bin/rotatelogs /usr/local/apache/logs/error-%Y-%m-%d.log 86400 +540" TransferLog "|/usr/local/apache/bin/rotatelogs /usr/local/apache/logs/app/access-%Y-%m-%d.log 86400 +540"

- 864000 = 24 시간에 대한 rotationtime(초단위)
- +540 은 UTC에서의 시간차이(UTC+9 => 9 * 60= 540)

 

#### **지시어**

<div class="table-wrap"><table class="confluenceTable tablesorter tablesorter-default stickyTableHeaders"><thead class="tableFloatingHeader"><tr class="tablesorter-headerRow"><th class="confluenceTh sortableHeader" data-column="0" tabindex="0"><div class="tablesorter-header-inner">지시어</div></th><th class="confluenceTh sortableHeader" data-column="1" tabindex="0"><div class="tablesorter-header-inner">내용</div></th></tr></thead><tbody><tr><td class="confluenceTd">%w</td><td class="confluenceTd">1-자리 요일수(주의 첫번째 날은 일요일)</td></tr><tr><td class="confluenceTd">%m</td><td class="confluenceTd">2-자리 달</td></tr><tr><td class="confluenceTd">%M</td><td class="confluenceTd">2-자리 분</td></tr><tr><td class="confluenceTd">%I(대문자 i)</td><td class="confluenceTd">2-자리 시간(12시간 시계)</td></tr><tr><td class="confluenceTd">%H “</td><td class="confluenceTd">2-자리 시간(24시간 시계)</td></tr><tr><td class="confluenceTd">%y</td><td class="confluenceTd">2-자리 연도</td></tr><tr><td class="confluenceTd">%d</td><td class="confluenceTd">2-자리 일</td></tr><tr><td class="confluenceTd">%W</td><td class="confluenceTd">2-자리 주일수(주의 첫번째 날은 월요일)</td></tr><tr><td class="confluenceTd">%U</td><td class="confluenceTd">2-자리 주일수(주의 첫번째 날은 일요일)</td></tr><tr><td class="confluenceTd">%S</td><td class="confluenceTd">2-자리 초</td></tr><tr><td class="confluenceTd">%j</td><td class="confluenceTd">3-자리 날짜수</td></tr><tr><td class="confluenceTd">%Y</td><td class="confluenceTd">4-자리 연도</td></tr><tr><td class="confluenceTd">%b</td><td class="confluenceTd">(지역화된) 3-문자 달 이름</td></tr><tr><td class="confluenceTd">%a</td><td class="confluenceTd">(지역화된) 3-문자 요일 이름</td></tr><tr><td class="confluenceTd">%p</td><td class="confluenceTd">(지역화된) 12시간 시계의 am/pm</td></tr><tr><td class="confluenceTd">%x</td><td class="confluenceTd">(지역화된) 날짜</td></tr><tr><td class="confluenceTd">%c</td><td class="confluenceTd">(지역화된) 날짜와 시간</td></tr><tr><td class="confluenceTd">%X</td><td class="confluenceTd">(지역화된) 시간</td></tr><tr><td class="confluenceTd">%B</td><td class="confluenceTd">(지역화된) 완전한 달 이름</td></tr><tr><td class="confluenceTd">%A</td><td class="confluenceTd">(지역화된) 완전한 요일 이름</td></tr><tr><td class="confluenceTd">%%</td><td class="confluenceTd">문자그대로 `%’</td></tr><tr><td class="confluenceTd">%Z</td><td class="confluenceTd">시간대 이름</td></tr></tbody></table></div> 



