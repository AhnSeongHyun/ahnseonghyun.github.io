---
title: 'health checking open source - checkup'
author: 'ash84'
pub_date: '2019-09-20'
description: ''
featured_image: ''
tags: ['checkup', 'health checking', 'msa', 'Opensource']
---

health check 를 할 수 있는 오픈소스에 대해서 찾아보다가 checkup 이라는 sourcegraph 에서 go 언어로 만든 것을  찾게 되었다. 생각보다 이런 오픈 소스가 없다는 게 신기하긴 한데, 요즘에는 k8s 를 많이 써서 그 안에서 해주기도 하고 이전에는 cron 이나 jenkins 를 이용해서 health checking 작업을 하거나 자체 구축해서 쓰는 경우가 많았던 것 같다. 

[https://github.com/sourcegraph/checkup](https://github.com/sourcegraph/checkup) 

일단 checkup 은 [project status](https://github.com/sourcegraph/checkup/issues/86) 가 애매한 상황이긴 하다. **사용하실 거라면 이 부분을 반드시 유의하길 바란다.** 더 이상 개발이 진행이 되지 않는 것 같기는 한데 현재 기능만으로도 충분한 것 같기도 하다. 

## configuration

일단 JSON 파일(Default: checkup.json)로 단순하게 어떤 서비스를 대상(checkers)으로 할지 그리고 health checking 한 데이터를 어디에 저장할지(storage), 그리고 어떻게 알림을 보낼지(notifiers) 를 명시적으로 정의 할 수 있다. **개인적으로 가장 마음에 드는 부분이긴 하다.** 

```json
    {
       "checkers":[
          {
             "type":"http",
             "endpoint_name":"user-service",
             "endpoint_url":"http://localhost:8000",
             "attempts":3
          },
          {
             "type":"http",
             "endpoint_name":"billing-service",
             "endpoint_url":"http://localhost:8080",
             "attempts":3
          }
       ],
       "storage":{
          "provider":"fs",
          "dir":"./check_files",
          "url":"http://127.0.0.1:2015/check_files"
       }, 
    	 "notifier":{
    			"name": "slack",
    			"username": "username",
    			"channel": "#channel-name",
    			"webhook": "webhook-url"
    		}
    }
```

`checkers` 부분에서 체킹 대상에 대해서 적어 주면 되는데 http, tcp, tls, dns 등의 타입을 제공하고 있다. `storage` 같은 경우 s3, file, github storage, sql storage 를 제공하고 있는데 뒤에서 설명할 status page 는 현재 sql storage 를 지원을 하지 않는다. 위에서는 file 로 설정을 했고, `dir` 로 현재 디레토리를 설정을 했다. 그리고 이 파일이 서빙되는 `url` 을 적어주었다. `notifiers` 항목은 slack 을 지원하고 있는데 위와 같이 이름과 webhook 에 대한 정보를 넣어 주면 된다. 

## Run

일단 help 를 보자. 

```shell
    ❯ checkup --help
    Checkup is distributed, lock-free, self-hosted health
    checks and status pages.
    
    Checkup will always look for a checkup.json file in
    the current working directory by default and use it.
    You can specify a different file location using the
    --config/-c flag.
    
    Running checkup without any arguments will invoke
    a single checkup and print results to stdout. To
    store the results of the check, use --store.
    
    Usage:
      checkup [flags]
      checkup [command]
    
    Available Commands:
      every       Run checks indefinitely at an interval
      help        Help about any command
      message     Post a status message/update
      provision   Provision a storage service
    
    Flags:
      -c, --config string   JSON config file (default "checkup.json")
      -h, --help            help for checkup
          --store           Store results
          --v               Enable logging to standard output
    
    Use "checkup [command] --help" for more information about a command.
```

바로 실행을 시키면 아래와 같이 현재 8080, 8081 port 로 서버가 떠 있기 때문에 아래와 같이 관련 정보들이 나오는 것을 확인 할 수 있다. 

```shell
    ❯ checkup
    == user-service - http://localhost:8000
      Threshold: 0s
            Max: 10.260678ms
            Min: 6.777536ms
         Median: 9.302433ms
           Mean: 8.780215ms
            All: [{10.260678ms } {9.302433ms } {6.777536ms }]
     Assessment: healthy
    
    == billing-service - http://localhost:8081
      Threshold: 0s
            Max: 10.355745ms
            Min: 6.180592ms
         Median: 8.969239ms
           Mean: 8.501858ms
            All: [{10.355745ms } {8.969239ms } {6.180592ms }]
     Assessment: healthy
```

그런데 health checking 자체를 주기적으로 실행하고 싶다면 물론 cron 같은것으로 checkup 자체를 스케쥴링 해도 되지만 자체적으로 기능을 가지고 있다. `every` 라는 명령어를 통해서 시간을 지정하면 아래와 같이 3초에 한번씩 체크를 하게 된다. 

```shell
    > checkup every 3s 
```

아래의 로그에서 보면 3초에 3번씩 호출하는 것을 볼 수 있는데 이유는 위에 checkers 에서 attempt 를 3으로 지정했기 때문이다. 

```
    127.0.0.1 - - [20/Sep/2019 11:24:53] "GET / HTTP/1.1" 200 -
    127.0.0.1 - - [20/Sep/2019 11:24:53] "GET / HTTP/1.1" 200 -
    127.0.0.1 - - [20/Sep/2019 11:24:53] "GET / HTTP/1.1" 200 -
    127.0.0.1 - - [20/Sep/2019 11:24:56] "GET / HTTP/1.1" 200 -
    127.0.0.1 - - [20/Sep/2019 11:24:56] "GET / HTTP/1.1" 200 -
    127.0.0.1 - - [20/Sep/2019 11:24:56] "GET / HTTP/1.1" 200 -
```

하나의 서비스를 내리게 되면 바로 지정한 slack webhook 으로 아래와 같은 알람을 받을 수가 있다. 

![](https://live.staticflickr.com/65535/48762703486_60ef2e0458_z.jpg)

## Status Page

health checking, slakc notify 에 의해서 status page 까지. **3종 세트다.** 물론 자체 구축하는 게 더 나을 수도 있겠지만 굳이 리소스를 들일 필요가 없다면 제공하는 것을 사용할 수 있다. [https://caddyserver.com/](https://caddyserver.com/) 을 사용하라고 권장하고 있지만 python simple http server 도 띄울 수 있다. 

```shell
    > cd checkup 
    > python -m http.server 2015 
```

`checkup/statuspage` 디렉토리에 관련 소스들이 있는데 앞에서 storage 로 연결했던 부분을 설정으로 넣어줘야 한다. `config.js` 를 수정해 주면 되는데 file 로 설정했기 때문에 아래와 같이 설정을 해주었다.

```json 

    checkup.config = {
    	// How much history to show on the status page. Long durations and
    	// frequent checks make for slow loading, so be conservative.
    	// This value is in NANOSECONDS to mirror Go's time package.
    	"timeframe": 1 * time.Day,
    
    	// How often, in seconds, to pull new checks and update the page.
    	"refresh_interval": 60,
    
    	// Configure read-only access to stored checks. This configuration
    	// depends on your storage provider. Any credentials and other values
    	// here will be visible to everyone, so use keys with ONLY read access!
    	"storage": {
    		// Local file system (Caddy recommended: https://caddyserver.com)
    		"url": "http://localhost:2015/check_files"
    	},
    
    	// The text to display along the top bar depending on overall status.
    	"status_text": {
    		"healthy": "Situation Normal",
    		"degraded": "Degraded Service",
    		"down": "Service Disruption"
    	}
    };
```
[http://localhost:2015/statuspage](http://localhost:2015/statuspage) 이런식으로 접근을 하면 볼 수 가 있다. 

정상적인 경우, 

![](https://live.staticflickr.com/65535/48762891162_b41d0aabf8_z.jpg)

에러가 난 경우, 
![](https://live.staticflickr.com/65535/48762703561_e96200473e_z.jpg)
