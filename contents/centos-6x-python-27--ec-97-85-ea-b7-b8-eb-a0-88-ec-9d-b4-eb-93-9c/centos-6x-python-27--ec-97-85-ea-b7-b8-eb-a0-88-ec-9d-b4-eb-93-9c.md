---
title: 'CentOS 6.X Python 2.7 업그레이드'
author: 'ash84'
pub_date: '2015-02-17'
description: 'https://github.com/h2oai/h2o/wiki/Installing-python-2.7-on-centos-6.3.-Follow-this-sequence-exactly-for-centos-machine-only

위의 링크가 가장 확실한것 같다. CentOS 를 회사에서 기본 리눅스 서버로 사용하는데 2.6 버전이 설치되어서 나온다. 근데 우분투에서 처럼 다른 곳에서 파이썬 2.7을 받아서 설치하면 끝인줄알았는데 그떄 부터가 지옥 시작이다. 이유는 **CentOS 에서는 yum 이라는 리눅스 패키지 관리 툴/프로그램을 이'
featured_image: ''
tags: ['centos', 'dev', '리눅스', 'python2.7']
---

https://github.com/h2oai/h2o/wiki/Installing-python-2.7-on-centos-6.3.-Follow-this-sequence-exactly-for-centos-machine-only

위의 링크가 가장 확실한것 같다. CentOS 를 회사에서 기본 리눅스 서버로 사용하는데 2.6 버전이 설치되어서 나온다. 근데 우분투에서 처럼 다른 곳에서 파이썬 2.7을 받아서 설치하면 끝인줄알았는데 그떄 부터가 지옥 시작이다. 이유는 **CentOS 에서는 yum 이라는 리눅스 패키지 관리 툴/프로그램을 이용하게 되는데 그것이 python 2.6과 매우 밀접한 연관이 있어서 마구잡이로 2.7로 업그레이드하게 되면 yum을 사용하지 못하는 문제가 생긴다.**

위의 링크를 따라해 보면 알겠지만, 결국 핵심은 python2.7 을 /usr/local/bin 에 설치를 하고 기본 python 은 python2.7을 사용하고 python 2.6은 그냥 두는 방식이다. 단순히 python 2.7만 설치하는게 다가 아니라 easy_install, pip도 버전이 다를수 있으니 **반드시 정독하면서 따라해야 할것.**

 

yum 이 문제될 경우 : [리눅스 Python 2.7 컴파일 설치 ](http://zetawiki.com/wiki/%EB%A6%AC%EB%88%85%EC%8A%A4_Python_2.7_%EC%BB%B4%ED%8C%8C%EC%9D%BC_%EC%84%A4%EC%B9%98)

 

 

[2014/12/09 – [Programming] – [CentOS] Apache2.4 설치](http://ash84.tistory.com/1094)

 

[2014/11/27 – [Programming/Linux] – 리눅스에서 pyodbc 이용해서 mssql과 연동하기](http://ash84.tistory.com/1085)

 

[2013/08/04 – [Programming/DB] – (mysql) mac 에서 mysql삭제하기.](http://ash84.tistory.com/1003)

 

 



