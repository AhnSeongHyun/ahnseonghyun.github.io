---
title: '리눅스에서 pyodbc 이용해서 mssql과 연동하기'
author: 'ash84'
pub_date: '2014-11-27'
description: '일반적으로 python-mssql 라이브러리들은 윈도우를 기반으로 동작한다. 이때 pyodbc나 pymssql 들은 내부적으로 윈도우에 설치된 SqlClient 등의 라이브러리에 의존하게 된다. 

**문제 : 리눅스 환경에서는 SqlClient 와 같은 라이브러리가 없는데 어디에 의존해야 할까?**

pyodbc 를 기준으로 설명하자면, 리눅스 환경. CentOS, Ubuntu, MAC OSX 등의 환경에서는 unixODBC 와 FreeTDS 라는 라이브러리가 필요하다. 

    

**[ unixODBC  ](http://ww'
featured_image: ''
tags: ['MSSQL', 'Python', 'dev', 'freetds', 'open-source', 'pyodbc', 'unixODBC']
---
일반적으로 python-mssql 라이브러리들은 윈도우를 기반으로 동작한다. 이때 pyodbc나 pymssql 들은 내부적으로 윈도우에 설치된 SqlClient 등의 라이브러리에 의존하게 된다. 

**문제 : 리눅스 환경에서는 SqlClient 와 같은 라이브러리가 없는데 어디에 의존해야 할까?**

pyodbc 를 기준으로 설명하자면, 리눅스 환경. CentOS, Ubuntu, MAC OSX 등의 환경에서는 unixODBC 와 FreeTDS 라는 라이브러리가 필요하다. 

    

**[ unixODBC  ](http://www.unixodbc.org/)**

 – non winodws platform 상에서 표준 ODBC를 사용할수 있도록 해주는 라이브러리.  

 – 설치법  

-  centos : 
```
yum install unixODBC unixODBC-devel 
```

-  ubuntu : 
```
apt-get install unixodbc-dev unixodbc-bin unixodbc 
```

    

**[ FreeTDS  ](http://www.freetds.org/)**

 – 유닉스, 리눅스를 위한 라이브러리 집합으로 MS SQL  Server, Sybase 데이터베이스와의 통신을 위한 라이브러리  

 – TDS(Tabular Data Stream)프로토콜 에 대한 오픈소스 구현체이다.  

 – 설치법 :  [ ftp://ftp.freetds.org/pub/freetds/stable/freetds-stable.tgz ](ftp://ftp.freetds.org/pub/freetds/stable/freetds-stable.tgz)  다운로드후, 다음의 작업 수행. 

 
 

 <script src="https://gist.github.com/AhnSeongHyun/0b3b802c75784c6f1693.js"></script> 

 설치시, 만약 unixODBC 를 먼저 설치했다면, `./configure` 하는 부분에서 다음과 같이 실행해 준다. 

 <script src="https://gist.github.com/AhnSeongHyun/e21b71e85832c4c7c0ee.js"></script> 

**설치후 해야할 일**

 – 두개의 파일을 설정해야 하는데 `/etc/odbcinst.ini`, `/etc/obbc.ini`

 – `/etc/odbcinst.ini` 에서는 다음과 같이 마지막줄에 FreeTDS 추가할 것을 명시해준다. 즉, 여기서는 드라이버를 FreeTDS 를 쓰겠다고 지정하는것이다.  

 <script src="https://gist.github.com/AhnSeongHyun/5c03139a99b6e2935be3.js"></script> 

 – `/etc/odbc.ini` 에서는 실제 연결할 데이터베이스에 대한 정보를 입력한다.  

<script src="https://gist.github.com/AhnSeongHyun/9906b7f4fdb7da32e2c2.js"></script>

<script src="https://gist.github.com/AhnSeongHyun/3690774bf40cca02333d.js"></script>
 

**자, 이제 연동하는 법**

- `/etc/freetds.conf` 추가

```
[DB_PRM]
host=10.10.1.116
port=1443
tds version=7.0
dump file=/tmp/freetds.log
```

- **중요한점은 connect 함수에서 연결시, 앞에서 /etc/odbc.ini 에서 [MSSSQLTEST] 라고 영역을 지정해 두었던 것을 Connect 함수의 DSN 부분에 써주어야 한다. 이유는 모르겠지만, server 로 해서 ip 나 호스트 이름을 지정하게 되면 연결이 되지 않는다.**



