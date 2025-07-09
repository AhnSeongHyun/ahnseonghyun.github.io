---
title: 'centos yum remove httpd'
author: 'ash84'
pub_date: '2015-03-04'
description: 'centos 상에서 아파치 소스를 받아서 설치하다 보면 아래와 같이 redefinition 에러가 발생하는 경우가 있다.

> exports.c:2048: error: redefinition of ‘aphackaprbrigadeputc’


찾아보니 이전에 centos 에 기 설치되어있던 httpd 관련 소스들과의 충돌 때문인데 아래와 같이 삭제해주면 된다. httpd 뿐만 아니라 apr, apr-util 라이브러리도 같이 완전히 삭제해 주어야 원만하게 설치가 된다.

```bash 
$ sudo yum erase httpd ht'
featured_image: ''
tags: ['cenot remove httpd', 'centos', 'centos yum remove httpd', 'dev', 'httpd']
---


centos 상에서 아파치 소스를 받아서 설치하다 보면 아래와 같이 redefinition 에러가 발생하는 경우가 있다.

> exports.c:2048: error: redefinition of ‘aphackaprbrigadeputc’


찾아보니 이전에 centos 에 기 설치되어있던 httpd 관련 소스들과의 충돌 때문인데 아래와 같이 삭제해주면 된다. httpd 뿐만 아니라 apr, apr-util 라이브러리도 같이 완전히 삭제해 주어야 원만하게 설치가 된다.

```bash 
$ sudo yum erase httpd httpd-tools apr apr-util
```

[2014/12/09 – [Programming] – [CentOS] Apache2.4 설치](http://ash84.tistory.com/entry/CentOS-Apache24-설치)



