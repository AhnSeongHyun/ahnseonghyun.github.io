---
title: 'meier 1.0.1 와 블로그 이사기'
author: 'ash84'
pub_date: '2019-07-23'
description: '몇 주전부터 심심할 때마다 블로그 서버인 [meier](https://github.com/meier-project/meier) 를 고치는 작업들을 하고 있었다. 코드도 낡고, 서버도 낡은 상태로 바꾸고 싶은 마음이 굴뚝 같았는데 그동안 여유가 안났는데 야금야금 바꾸기 시작했다. 여러가지가 있겠지만 그 중에 가장 중요한 것은 `docker` 를 사용하도록 바꾸는 작업이었다. `docker` 를 개인적으로 잘 사용하지 못해서 개인 프로젝트에서 사용해 보고 싶었고, 나중에 컨테이너 기반으로 배포나 그런 것을 실험해 볼 수 있을것 같았다.'
featured_image: ''
tags: ['AWS', 'blog', 'deployment', 'lightsail', 'medical-informatics', 'meier', 'project-showcase']
---
몇 주전부터 심심할 때마다 블로그 서버인 [meier](https://github.com/meier-project/meier) 를 고치는 작업들을 하고 있었다. 코드도 낡고, 서버도 낡은 상태로 바꾸고 싶은 마음이 굴뚝 같았는데 그동안 여유가 안났는데 야금야금 바꾸기 시작했다. 여러가지가 있겠지만 그 중에 가장 중요한 것은 `docker` 를 사용하도록 바꾸는 작업이었다. `docker` 를 개인적으로 잘 사용하지 못해서 개인 프로젝트에서 사용해 보고 싶었고, 나중에 컨테이너 기반으로 배포나 그런 것을 실험해 볼 수 있을것 같았다. 

그래서 Dockerfile 을 만들었고, `alphine` 으로 base image 를 쓰다가 회사 동료가 `slim-stretch` 를 알려줘서 변경했다. dokcker 로 서버로 띄우는 작업까지 완료는 했는데 한가지 문제가 생겼다. 원래 블로그 프로젝트에 테마를 넣기 위한  구조가 `meier > templates > themes > custom_themes` 이런 구조로 있다. 그런데 테마들은 변동 가능한 부분이고, 여러 개를 가질 수 가 있어서, themes 하위에 어떤 블로그 테마를 넣을 때 마다 `docker build` 를 다시 해야 하는 이슈가 있었다. 

찾아보니 외부에서 volume 을 잡을 수 있는 기능이 있어서 연결해서 잘 사용하고 있다. 

```docker
    -v ~/themes:/app/meier/templates/themes
```

Self-Hosted Blog Platform 이라는 목적으로 만든 것이기 때문에 누구나 커스텀해서 자신의 Docker Hub 에 올리고 개인 서버에 docker 를 이용해서 실행할 수 있다. 별도의 공식 계정을 만들어서 travis-ci 를 돌면서  `docker build` 를 수행하고 docker hub 에 push 하는것은 백로그로 넘어둔 상태이다. 

## AWS Lightsail

![](https://live.staticflickr.com/65535/48352879487_cb2cb900d1_b.jpg)

이 글을 게시하는 내 블로그도 meier 로 되어있는데, 막상 dockerize 를 하고 docker hub 에서 다운 받아서 기존의 블로그 서버에서 적용하려고 하니 서버의 운영체제 버전이 너무 낮아서 실행할 수 없는 문제에 봉착했다. 스마일서브에서 원 11,000원 짜리 가상서버를 써오고 있었고, Ubuntu 14 버전을 사용하고 있어서 생기는 문제였다. 새로운 스마일서브 서버를 최신 OS를 받아서 쓸까도 하다가, 이 참에 AWS 로 이사가자는 생각이 들었다. 

![](https://live.staticflickr.com/65535/48279009251_55748b3aeb_b.jpg)

그중에서도 AWS Lightsail 을 선택했는데 이유는 생각보다 세팅하기도 편하고, 가격도 괜찮아서 선택하게 되었다. 서버(Amazon Linux)는 가장 낮은 $3.5 상품을 사용했고, 데이터베이스(mysql5.7) 역시 가장 작은 제품을 선택했다. 

![](https://live.staticflickr.com/65535/48279009356_7c74828868_b.jpg)

Amazon Linux 는 몇개 깔려있는 것이 없어서 `docker`, `nginx` 를 설치했다. 다시 세팅을 해야한다고 하면 좀 더 익숙한 Ubuntu 를 선택할 것 같긴하다. docker 로 meier 를 띄우고, nignx 로 proxy 설정을 한후, 원래의 도메인을 AWS Lightsail 서버의 IP 와 연결하고, Let's Encrypt 를 이용해서 HTTPS 인증서를 세팅하니 끝이 났다.

ps) 누군가 그러더라, 블로그를 만들고 수정하는 것은 마치 공부하기 전에 책상 정리를 하는 것이라고.  

**참고링크 :** 

[https://serverfault.com/questions/836198/how-to-install-docker-on-aws-ec2-instance-with-ami-ce-ee-update](https://serverfault.com/questions/836198/how-to-install-docker-on-aws-ec2-instance-with-ami-ce-ee-update)
