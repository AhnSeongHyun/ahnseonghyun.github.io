---
title: 'ngrok 를 이용한 localhost 를 public domain 연결하기'
author: 'ash84'
pub_date: '2020-01-13'
description: ''
featured_image: ''
tags: ['ngrok', 'domain']
---

테스트를 하거나 아니면 인증 쪽 관련 작업들을 하려고 하면 localhost 에서 띄우면 되는데 도메인이 필요한 경우들이 있다. 예를 들면 github 에서 webhook  테스트를 한다고 할 때 도메인을 입력해야 github 상에서 이벤트가 발생했을 때 webhook 을 받을수 있다. (github 입장에서 localhost 는 자기자신이니..😅) 또는 모바일과 연동 테스트를 진행할 때도 도메인을 만들기 전이나 실서버 올리기 전에 임시로 테스트를 하기 위해서도 유용할 것 같다. 😙

![ngrok%20localhost%20public%20domain/Untitled.png](https://live.staticflickr.com/65535/49304043123_abb75e334e_z.jpg)

이럴때 사용하는 것이 ngrok 이라는 서비스이다. ngrok 은 내 컴퓨터에 [localhost](http://localhost) 로 띄운 서버를 ngrok 도메인을 붙여서 임시적(?) 으로 사용할 수 있게 해준다. 

[price plan](https://ngrok.com/pricing) 은 free 도 제공하고 있고, 하나의 도메인만 사용할 경우에는 free 도 충분하다. 서브 도메인을 사용하거나 whitelist access 같은 좀 더 복잡한 그리고 분당 연결 수 같은 부분을 추가적으로 늘리려면 여러가지 price plan 을 선택 할 수 있다. 

일단 가입을 하고 나면 ngrok 을 다운로드 받으면 된다. 거의 모든 운영체제를 지원하고 있다. 간단히 사용하는 방법은 다음과 같다.  

일단 localhost 로 python 기본 http server 5000번 포트를 연다. 

```shell

    > python3 -m http.server 5000
    Serving HTTP on 0.0.0.0 port 5000 (http://0.0.0.0:5000/) ...
```

```shell
    > ngrok http 5000    
    ngrok by @inconshreveable                                                                                    (Ctrl+C to quit)
    
    Session Status                online
    Account                       ahnseonghyun (Plan: Free)
    Version                       2.3.35
    Region                        United States (us)
    Web Interface                 http://127.0.0.1:4040
    Forwarding                    http://a0bedc75.ngrok.io -> http://localhost:5000
    Forwarding                    https://a0bedc75.ngrok.io -> http://localhost:5000
    
    Connections                   ttl     opn     rt1     rt5     p50     p90
                                  0       0       0.00    0.00    0.00    0.00

 ```

위와 같이 `ngrok` 명령어와 연결하고자 하는 port 번호를 입력하면 http, https [ngrok.io](http://ngrok.io) 의 서브도메인이 생성된다. 해당 주소로 요청을 보내면 실제 python server 의 다음과 같이 로그가 찍히는 것을 확인 할 수 가 있다. 

```shell
    ❯ python3 -m http.server 5000
    Serving HTTP on 0.0.0.0 port 5000 (http://0.0.0.0:5000/) ...
    127.0.0.1 - - [31/Dec/2019 13:29:45] "GET / HTTP/1.1" 200 -
    127.0.0.1 - - [31/Dec/2019 13:29:46] code 404, message File not found
    127.0.0.1 - - [31/Dec/2019 13:29:46] "GET /favicon.ico HTTP/1.1" 404 -
    127.0.0.1 - - [31/Dec/2019 22:14:37] "GET / HTTP/1.1" 200 -
    127.0.0.1 - - [31/Dec/2019 22:14:37] code 404, message File not found
    127.0.0.1 - - [31/Dec/2019 22:14:37] "GET /favicon.ico HTTP/1.1" 404 -
```

그리고 아래와 같이 실제 ngrok Dashboard 에 status 에서도 확인 할 수 있다. ngrok 이 떠있는 상태에서 ctrl+c 를 누르고 취소를 하면 연결을 사라지게 된다. 

![ngrok%20localhost%20public%20domain/Untitled%201.png](https://live.staticflickr.com/65535/49304043238_5060d65236_z.jpg)
