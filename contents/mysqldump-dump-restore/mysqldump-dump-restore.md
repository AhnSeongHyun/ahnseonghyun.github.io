---
title: 'mysqldump - dump & restore'
author: 'ash84'
pub_date: '2015-08-31'
description: ''
featured_image: ''
tags: ['dump', 'MySQL', 'mysqldump', 'restore']
---


**mysqldump 덤프뜨기**

 

<script src="https://gist.github.com/AhnSeongHyun/9c2d3d442f28a425d709.js"></script>위의 명령 실행시, 저장프로시저, 트리거 함수, 스키마가 sql로 만들어 진다.   **mysqldump 덤프복원**  <script src="https://gist.github.com/AhnSeongHyun/24bf4acc011a87f37713.js"></script>

명령 실행전, 사용할 계정을 만들고 디비를 만들고 계정의 접근과 계정과 DB를 연결해 줘야 한다.

 

참고 : [http://link2me.tistory.com/431](http://link2me.tistory.com/431)

실행시, 다음과 같은 에러가 뜰 경우, **/etc/my.conf 에 log-bin-trust-function-creators=1 을 추가하고 mysql을 재시작 한다.**

> his function has none of DETERMINISTIC, NO SQL, or READS SQL DATA in its declaration and binary logging is enabled

 

**mysqldump 옵션**

-A, –all-databases Dump all the databases. This will be same as –databases  
 with all databases selected.  
 –add-drop-database Add a ‘DROP DATABASE’ before each create.  
 –add-drop-table Add a ‘drop table’ before each create.  
 –add-locks Add locks around insert statements.  
 -B, –databases To dump several databases. Note the difference in usage;  
 In this case no tables are given. All name arguments are  
 regarded as databasenames. ‘USE db_name;’ will be  
 included in the output.  
 –default-character-set=name  
 Set the default character set.  
 –delayed-insert Insert rows with INSERT DELAYED;  
 -f, –force Continue even if we get an sql-error  
 -x, –lock-all-tables  
 Locks all tables across all databases. This is achieved  
 by taking a global read lock for the duration of the  
 whole dump. Automatically turns –single-transaction and  
 –lock-tables off.  
 -l, –lock-tables Lock all tables for read.  
 –no-autocommit Wrap tables with autocommit/commit statements.  
 -n, –no-create-db ‘CREATE DATABASE /*!32312 IF NOT EXISTS*/ db_name;’ will  
 not be put in the output. The above line will be added  
 otherwise, if –databases or –all-databases option was  
 given.}.  
 -t, –no-create-info  
 Don’t write table creation info.  
 -d, –no-data No row information.  
 -R, –routines Dump stored routines (functions and procedures).  
 –set-charset Add ‘SET NAMES default_character_set’ to the output.  
 Enabled by default; suppress with –skip-set-charset.  
 –tables Overrides option –databases (-B).  
 –triggers Dump triggers for each dumped table  
 -X, –xml Dump a database as well formed XML



