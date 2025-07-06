---
title: 'uwsgi 기본 사용법 정리'
author: 'ash84'
pub_date: '2016-08-13'
description: '### 개요

- WAS 서버의 일종, 현재 파이썬 서버 중 가장 좋은 성능으로 알려져 있다. 

- 어플리케이션 컨테이너로 파이썬으로 만든 앱을 실행해 주는 역할, WSGI 을 지원한다. 



#### 설치

```bash 
$ pip install uwsgi 
```

#### flask 와 연동 

```bash
uwsgi –http 127.0.0.1:3031 –wsgi-file ./myflaskapp.py –callable app –processes 4 –threads 2 –stats 127.0.0.1:9191
````'
featured_image: ''
tags: ['dev', 'FLASK', 'INI', 'uWSGI', 'uwsgi usage', 'uwsgi 사용법']
---


### 개요

- WAS 서버의 일종, 현재 파이썬 서버 중 가장 좋은 성능으로 알려져 있다. 

- 어플리케이션 컨테이너로 파이썬으로 만든 앱을 실행해 주는 역할, WSGI 을 지원한다. 



#### 설치

```bash 
$ pip install uwsgi 
```

#### flask 와 연동 

```bash
uwsgi –http 127.0.0.1:3031 –wsgi-file ./myflaskapp.py –callable app –processes 4 –threads 2 –stats 127.0.0.1:9191
````
 

#### ini 파일로 간편화 하기 


- 위와 같이 한줄로 써주려면 불편한 부분이 있기 때문에 아래와 같이 .ini 파일로 만들고 바로 uwsgi file.ini 로 실행시킬수 있다. 


<script src="https://gist.github.com/AhnSeongHyun/1a6c47dc956f85c98eda.js"></script>

* http : 실행할 ip 및 포트 

* wsgi-file : 

* callable :

* processes : 프로세스의 수 </span>

* threads : 프로세스내 스레드의 수 </span>

* stats : 현재 uwsgi 상태를 볼수 있는 ip 및 포트(JSON 형식)

* pifile : 백그라운드(&)로 실행시켰을 경우, pid를 기록해 놓을 파일위치 

#### 기동 

```bash
$ uwsgi myflaskapp.ini & 
```

#### 정지

- 정지시, pidfile 의 위치를 지정해 줘야 한다.

```bash
$ uwsgi –stop /tmp/project-master.pid
```

