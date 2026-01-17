---
title: 'nginx 설치 및 구동'
author: 'ash84'
pub_date: '2015-03-18'
description: '### 개요

– 웹 서버 소프트웨어로, 가벼움과 높은 성능을 목표로 한다. 웹 서버, 리버스 프록시 및 메일 프록시 기능을 가진다. Netcraft의 2011년 1월 웹서버 설문조사에 따르면, nginx는 전체 도메인에서 4번째(7.50%)로 많이 쓰이는 웹서버이며, 활성화된 웹 사이트에 대한 통계에서도 역시 4번째(8.23%)로 많이 사용된다. 

– Nginx는 요청에 응답하기 위해 비동기 이벤트 기반 구조를 가진다. 이것은 아파치 HTTP 서버의 스레드/프로세스 기반 구조를 가지는 것과는 대조적이다. 이러한 구조는 서버에'
featured_image: ''
tags: ['dev', 'nginx', 'Nginx 설치', 'Python', 'uwsgi nginx', 'nginx 설정']
---
### 개요

– 웹 서버 소프트웨어로, 가벼움과 높은 성능을 목표로 한다. 웹 서버, 리버스 프록시 및 메일 프록시 기능을 가진다. Netcraft의 2011년 1월 웹서버 설문조사에 따르면, nginx는 전체 도메인에서 4번째(7.50%)로 많이 쓰이는 웹서버이며, 활성화된 웹 사이트에 대한 통계에서도 역시 4번째(8.23%)로 많이 사용된다. 

– Nginx는 요청에 응답하기 위해 비동기 이벤트 기반 구조를 가진다. 이것은 아파치 HTTP 서버의 스레드/프로세스 기반 구조를 가지는 것과는 대조적이다. 이러한 구조는 서버에 많은 부하가 생길 경우의 성능을 예측하기 쉽게 해준다. 


### 설치 
> 다운로드 : http://nginx.org/en/download.html
### 압축푼후 설치

```
./configure > make 
sudo make install 
```

- 별도의 옵션없이 설치하게 되면, `/usr/local/nginx` 에 설치되게 된다. 
<script src="https://gist.github.com/AhnSeongHyun/c1c6fe333051b29f6ea3.js"></script> 

– /sbin : nginx 바이너리가 실질적인 서버를 실행시키는 역할을 한다. 

– /conf : nginx.conf 등을 비롯한 다양한 conf 가 존재한다. uwsgi 관련 설정도 기본으로 제공한다.


<script src="https://gist.github.com/AhnSeongHyun/37a1ee16d8a820414a65.js"></script>

/logs : 로그 관련 파일 존재 

<script src="https://gist.github.com/AhnSeongHyun/a6de3935a4538a11a019.js"></script> 

### 구동

```
usr/local/nginx/sbin/nginx
```

– 위와 같이 입력하게 되면 기본 디렉토리 즉,`/usr/local/nginx/conf/nginx.conf` 를 설정으로 구동되게 된다. 

### 정지

```
usr/local/nginx/sbin/nginx -s stop
```
