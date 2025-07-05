---
title: 'Letsencrypt & nginx ssl setting'
author: 'ash84'
pub_date: '2016-08-06'
description: ''
featured_image: 'https://letsencrypt.org/images/letsencrypt-logo-horizontal.svg'
tags: ['nginx', 'letsencrypt', 'SSL', 'http', 'https']
---

[Letsencrypt](https://letsencrypt.org/) 를 적용해 보기로 하고 이 블로그는 Apache 로 운영되고 있어서 [certbot-auto](https://certbot.eff.org/) 을 이용해서 ```--apache``` 옵션을 주고 했는데 뭔가 이상하게 잘 안되었다. Apache 의 설정 문제인지 모르겠지만, 회사에서 가서 후임에게 물어보니 Nginx 는 잘 되었다고 해서 일단 nginx 로 바꾸고 ```certonly``` 옵션을 주고 인증서만 만들었다. 

그리고 아래와 같이 ```/etc/nginx/sites-available``` 에 설정파일을 두고 설정을 해주면 된다. 우분투에 설치한것이라서 저 위치에 있다고 보면 될것이고, 소스 설치하면 설치한 디렉토리 아래에 두면된다. 
 
<script src="https://gist.github.com/AhnSeongHyun/ffa54df838212ec9457702ed9aa76a7a.js"></script>

*.pem 을 지정하는 곳 외에 나머지 부분은 SSL 설정을 위한 부분인데, SSLAB 을 통해서 검사한 후, 등급을 보고 이상이 있으면 가이드를 통해서 수정해 주면 된다. 

그리고 80포트, http:// 로 운영되고 있었던 분이라면, http 로 들어오면 https 로 이동하도록 설정해 주어야 하는데 36번째 줄부터 80포트에 대한 설정이 있고 rewrite 를 통해서 이동 시키면 된다.

**Reference** 
- https://jungipark.github.io/ 




