---
title: 'drone.io - server 설치하기'
author: 'ash84'
pub_date: '2020-03-29'
description: ''
featured_image: ''
tags: ['server', 'ci', 'drone.io', 'drone']
---

최근에 drone.io 를 사용할 일이 있었는데, 생각보다 자료가 없어서 이번에는 server 구성에 대해서 다루고 다음 글에서는 agent 에 대해서 다룰 예정이다. 

### 개요

- 사이트 : [https://drone.io/](https://drone.io/)
- jenkins, travis-ci, github actions 처럼 CI 및 CD 까지 할 수 있는 툴

### 특징

- yaml 문법으로 정의 할 수 있다,.(젠킨스에 비해서 편하다)
- [다양한 plugins 를 기반으로 하고 있다.](http://plugins.drone.io/)
- `golang` 로 되어 있다.

### 구성

- server : drone.io 사이트에 대한 서버 역할
- agent : 개별 repository 에서 실행하는 pipeline 을 수행하는 역할, runner 라고 표현한다. 
    - Docker Runner, Exec Runner, SSH Runner 


## server 설치하기

- 다양한 VCS 를 제공하지만 여기서는 github 와 연결하는 것을 기반으로 설명한다.
- [https://docs.drone.io/installation/providers/github](https://docs.drone.io/installation/providers/github)



### 1) github OAuth app 만들기

- `github > Settings > Developer Settings > OAuth Apps` 에서 OAuth app 을 만든다. 
- callback url 을 지정하려면 public url 이 있어야 하는데 테스트 시에는 `ngrok` 을 이용해서 public url 을 가져올 수 있다. ([https://medium.com/@jccguimaraes/run-a-drone-ci-pipeline-locally-f4bfb4741c53](https://medium.com/@jccguimaraes/run-a-drone-ci-pipeline-locally-f4bfb4741c53))
- public url 을 가지고 github oAuth apps 의 callback url 에 해당 값을 넣고 app 을 만든다.


![](https://s3.ap-northeast-2.amazonaws.com/static.ash84.io/images/blog/drone-io-server/github-oauth-app.png)


### 2) drone server 설치하기

- server 와 agent(runner) 사이의 인증을 위해서 shared secret 을 만든다

```
$ openssl rand -hex 16
> adc394d69c6ef00a933c32be5144ca18
```

- download

```shell 
$ docker pull drone/drone:1.6.0
```


- configurations & run

```shell
$ docker run \
      --volume=/var/lib/drone:/data \
      --env=DRONE_AGENTS_ENABLED=true \
      --env=DRONE_GITHUB_SERVER=https://github.com \
      --env=DRONE_GITHUB_CLIENT_ID=${DRONE_GITHUB_CLIENT_ID} \
      --env=DRONE_GITHUB_CLIENT_SECRET=${DRONE_GITHUB_CLIENT_SECRET} \
      --env=DRONE_RPC_SECRET=${DRONE_RPC_SECRET} \
      --env=DRONE_SERVER_HOST=${DRONE_SERVER_HOST} \
      --env=DRONE_SERVER_PROTO=${DRONE_SERVER_PROTO} \
      --publish=80:80 \
      --publish=443:443 \
      --restart=always \
      --detach=true \
      --name=drone \
      drone/drone:1.6.0
```

- `DRONE_RPC_SECRET` : 앞에서 설정한 shared secret 값을 넣어준다. server 와 agent(runner) 가 통신할때 사용한다.
- `DRONE_GITHUB_CLIENT_ID, DRONE_GITHUB_CLIENT_SECRET` : 앞 단계에서 github oAuth app 을 만들었는데, 그 상세정보에 있는 `client_id`,  `client_secret` 를 넣어준다. 
- `DRONE_SERVER_HOST, DRONE_SERVER_PROTO` : DRONE_SERVER_HOST, DRONER_SERVER_PROTO 는 drone 에서 github repo 를 Activate 할때  webhook 지정 시 사용된다. 예를 들어 DRONER_SERVER_PROTO=http, DRONE_SERVER_HOST=127.0.0.1 로 지정하게 되면 [http://127.0.0.1](http://127.0.0.1) 로 repo 내 webhook 설정에 http://127.0.0.1 로 설정된다.

![](https://s3.ap-northeast-2.amazonaws.com/static.ash84.io/images/blog/drone-io-server/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-03-29+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+6.31.58.png)
