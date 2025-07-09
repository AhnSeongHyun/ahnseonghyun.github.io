---
title: 'pyodbc-MSSQL 사용시, 한글 문제'
author: 'ash84'
pub_date: '2014-12-01'
description: '[이전에 pyodbc 를 사용하는 부분](http://lab.ash84.net/post/99634203014/pyodbc-procedure)에 대해서 설명했었는데 이번에는 한글 insert 시 깨지는 문제가 생긴다. 이 문제의 해결을 위해서 사실은 사용하는 파이썬쪽, 그리고 돌아가는 리눅스의 LANG, LOCALE 설정, 그리고 PYODBC 와 FreeTDS, UNIXODBC 등의 설정을 모두 UTF8로 설정했음에도 불구하고 발생하는 문제였다. 한 2일 정도 고생하다가, 모든 내용을 StackOverflower 에 올렸다. 
[h'
featured_image: ''
tags: ['dev', 'MSSQL', 'pyodbc', 'utf8', '한글문제']
---


[이전에 pyodbc 를 사용하는 부분](http://lab.ash84.net/post/99634203014/pyodbc-procedure)에 대해서 설명했었는데 이번에는 한글 insert 시 깨지는 문제가 생긴다. 이 문제의 해결을 위해서 사실은 사용하는 파이썬쪽, 그리고 돌아가는 리눅스의 LANG, LOCALE 설정, 그리고 PYODBC 와 FreeTDS, UNIXODBC 등의 설정을 모두 UTF8로 설정했음에도 불구하고 발생하는 문제였다. 한 2일 정도 고생하다가, 모든 내용을 StackOverflower 에 올렸다. 
[http://stackoverflow.com/questions/26503531/why-insert-empty-value-using-pyodbc-in-linux-environment](http://stackoverflow.com/questions/26503531/why-insert-empty-value-using-pyodbc-in-linux-environment)
 

다른 개발자들이 해 본결과로는 이상하게 문자열 형식으로 insert 쿼리를 입력하는 경우에는 문제가 생긴다는 것이다. 

<script src="https://gist.github.com/AhnSeongHyun/df071e819607a46c2464.js"></script> 

아무튼 이 문제는 파라미터 전달 방식으로 데이터를 보내면 해결되는 문제였다. 사실 여전히 왜 이렇게 동작하는지는 의문이다.

<script src="https://gist.github.com/AhnSeongHyun/334e4ca9fbdf75e9f484.js"></script>

링크상에서도 된다고만 하지 왜 그런지는 애길하지 않는다. pyodbc로 mssql을 연동 하면서 느낀점은 정말 꼭 mssql을 써야하는 상황이 아니라면 굳이 연동을 할 필요가 있을까 하는 생각도 들고, 꼭 mssql을 사용하는 상황이라면 차라리 asp.net 을 권하고 싶다.

ps) 한글문제에 대해서 좀더 애기를 하자면, 위의 경우에는 mssql의 nvarchar 에 대해서 한글 inserting 이 안되는 문제에 한한것인데, 어쩔수 없이 varchar 를 써야 하는 경우라면 pyodbc 보다는 pymssql을 사용하는것이 더 편하다. 

[2014/11/27 – [Programming/Linux] – 리눅스에서 pyodbc 이용해서 mssql과 연동하기](http://ash84.tistory.com/1085)
 
