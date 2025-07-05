---
title: 'nginx header module'
author: 'ash84'
pub_date: '2020-01-22'
description: ''
featured_image: ''
tags: ['nginx', 'cors', 'header', 'add_header']
---

```shell
add_header 'Access-Control-Allow-Origin' '{ DOMAIN }';
add_header 'Access-Control-Allow-Credentials' 'true';
add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS, PUT, HEAD';
add_header 'Access-Control-Allow-Headers' 'Origin,Content-Type,authorization,accept';
```

API 작업할 때는 별다른 이슈가 없지만, 프론트엔드 파트와 작업 할 때는 CORS 이슈에 대해서 생각을 해봐야 한다. 일반적으로 nginx 를 사용한다고 할 때, 위와 같이 적어 주면 해결이 되겠지만 **사실 위의 코드에는 보강해야 할 부분이 있다. **

`401` 은 보통 Authorization 관련된 이슈가 있을 때 발생하게 되는데, 위와 같이 CORS 를 적용하면 `401` status code 를 내려 주는 reponse 에는 CORS 적용이 되지 않는다. 

이유는 `add_header` 부분 때문인데, 이 부분은 사실 nginx의 `ngx_http_headers_module` 을 통해서 사용할 수 있다. 그런데 `add_header` 의 사용법을 보면 이렇다. 

```
    Syntax:	add_header name value [always];
    Default:	—
    Context:	http, server, location, if in location
```

그러니까 위의 CORS 에서 `Access-Control-Allow-Origin` 은 name 이고 value 는 우리가 지정하는 어떤 도메인이 되는 것인데, `always` 는 뭘까? 

`401` 에 제대로 적용되지 않았던 이유는 기본적으로 `add_header` 는 아래의 http 상태코드에 대해서만 적용된다. 

```
    200, 201 (1.3.10), 204, 206, 301, 302, 303, 304, 307 (1.1.16, 1.0.13), or 308 (1.13.0)
```

그렇기 때문에 모든 status code 에 대해서 적용하고 싶으면 `always` 를 뒤에 붙여주면 된다. `always` 는 상태코드와 상관없이 모든 status code 에 대해서 header 를 적용시킨다. 

`ngx_http_headers_module` 은 `add_header` 외에도 `expires`, `add_trailer` 를 지정할 수 있게 해준다. 

References:
- [http://nginx.org/en/docs/http/ngx_http_headers_module.html#add_header](http://nginx.org/en/docs/http/ngx_http_headers_module.html#add_header)** **
