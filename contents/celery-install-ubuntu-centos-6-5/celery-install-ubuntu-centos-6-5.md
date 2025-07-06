---
title: 'Celery Install Ubuntu & CentOS 6.5'
author: 'ash84'
pub_date: '2015-11-23'
description: '### **celery 설치**

`pip install celery`

### **rabbitmq 설치 **

#### **ubuntu**

`sudo apt-get install rabiitmq-server`

#### **centOS6.5**

ceontOS 에서는 설치하는 것이 복잡한데 잘 따라오면 된다. 먼저 erlang 부터 설치해야 한다. 아래의 텍스트를 `/etc/yum.repos.d/` 디렉토리에 `epel-erlang.repo` 파일명으로 넣는다.

11. erlang 설치하기'
featured_image: ''
tags: ['Celery', 'celery centos', 'dev']
---


### **celery 설치**

`pip install celery`

### **rabbitmq 설치 **

#### **ubuntu**

`sudo apt-get install rabiitmq-server`

#### **centOS6.5**

ceontOS 에서는 설치하는 것이 복잡한데 잘 따라오면 된다. 먼저 erlang 부터 설치해야 한다. 아래의 텍스트를 `/etc/yum.repos.d/` 디렉토리에 `epel-erlang.repo` 파일명으로 넣는다.

11. erlang 설치하기
<script src="https://gist.github.com/AhnSeongHyun/a2ba9e87d9f1c4c5b9e8.js"></script>

이 부분에서  
<script src="https://gist.github.com/AhnSeongHyun/9912913a066bd7b4967c.js"></script>  
 이런식으로 가져올수도 있는데, 이럴 경우 base_url 이 깨진 링크로 잡힐수가 있다. 잘 확인하길 바란다.

15. rabbitmq-server 설치하기
`wget http://www.rabbitmq.com/releases/rabbitmq-server/v3.5.6/rabbitmq-server-3.5.6-1.noarch.rpm`

`sudo rpm -Uvh rabbitmq-server-3.5.6-1.noarch.rpm`

설치하는 것은 순식간이니까 설치가 안되었다고 느낄수도 있으나 설치가 된것이다.

20. rabbitmq-server 설정하기
– /etc/hosts 호스트를 등록한다.  
 – /etc/rabbitmq/rabbitmq.config

<script src="https://gist.github.com/AhnSeongHyun/2fc4a1b0cde52aea2447.js"></script>

기본은 5672 포트로, 관리쪽은 55672 포트로 설정한다는 것이다.

24. rabbitmq-server 시작
– sudo service rabbitmq-server start

26. rabbitmq-server web plugin
– rabbitmq-plugins enable rabbitmq_management  
 – sudo service rabbitmq-server restart

28. rabbitmq-server 사용자 설정
– sudo rabbitmqctl add_user admin 1234  
 – sudo rabbitmqctl set_user_tags admin administrator

**References**

31. [[입 개발] RabbitMQ 설치하기 for CentOS 6.5](https://charsyam.wordpress.com/2014/07/09/%EC%9E%85-%EA%B0%9C%EB%B0%9C-rabbitmq-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0-for-centos-6-5/)
32. [CentOS 6.5 (64Bit)에서 RabbitMQ 3.1.0 설치](http://jmkjb.blogspot.kr/2015/06/centos-65-64bit-rabbitmq-310.html)


