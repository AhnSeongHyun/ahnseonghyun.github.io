---
title: '[ELK] logstash'
author: 'ash84'
pub_date: '2018-05-18'
description: '###개요###
- 자바 기반으로 다양한 로그들을 수집하고 처리해서 내보낼수 있음. 
- 다양한 플러그인(input, filter, output) 을 제공하고 있는 것이 최대의 장점. 

###기본 실행###
```
logstash -f 
```

###Conf 파일 내 구조###
- input, output 은 필수파라미터, filter 는 옵션 
- input 은 데이터소스에서 가져오는 플러그인
- filter는 해당 데이터를 원하는 대로 변경하는 플러그인 
- output 은 Data Destination'
featured_image: 'data:image/png;base64,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'
tags: ['dev', 'logstash', 'elk']
---

###개요###
- 자바 기반으로 다양한 로그들을 수집하고 처리해서 내보낼수 있음. 
- 다양한 플러그인(input, filter, output) 을 제공하고 있는 것이 최대의 장점. 

###기본 실행###
```
logstash -f <conf file>
```

###Conf 파일 내 구조###
- input, output 은 필수파라미터, filter 는 옵션 
- input 은 데이터소스에서 가져오는 플러그인
- filter는 해당 데이터를 원하는 대로 변경하는 플러그인 
- output 은 Data Destination 으로 변경된 데이터를 쓰는 플러그인 

<center>
<img src="https://www.elastic.co/guide/en/logstash/current/static/images/basic_logstash_pipeline.png" width="100%"/>
</center>


간단하게 Apache acesslog 를 가져와서 JSON으로 변환하는 작업을 해보자. 

**first-pipeline.conf**
```

input {
  file {
    path => "/home/system/logs/test/access-2016-02-03.log"
    start_position => beginning
  }
}
filter {
    grok {
        match => { "message" => "%{COMMONAPACHELOG}"}
    }
    geoip{
       source => "clientip"
   }
}
output {
   stdout{ codec => json }
   elasticsearch{}
}

```


- file input plugin 의 기본 동작은 beginning 으로 지정
- unix의 tail -f와 동일. 특정 위치를 지정해서 logstash 의 파일에 대한 처리 시작 위치를 지정 할 수 있다. 

**grok filter plugin**

- 인입되는 데이터의 패턴을 찾아서 특정 필드들로 맵핑 변환 
- 패턴을 설정 해야 한다. 
- Apache accesslog 패턴 지정 : <code>{%COMBINEDAPACHELOG%}</code>

**geoip filter plugin**

- IP 필드를 지정하면, 해당 IP를 통해서 지역 정보를 추출해 주는 작업


###Check conf file###

```
./logstash -f ./first-pipeline.conf --configtest
```
- conf file 을 기반으로 작업이 수행되기 때문에 유효한지를 검사해야 한다. 


###결과###

- 아래의 결과를 보면, apache accesslog 로 들어오는 raw string 을 특정 필드로 맵핑된것을 볼 수 있다. 
- 또한 geoip 항목을 보면, 어디에서 접속했는지에 대한 위치정보를 가져와서 보여주고 있다. 
- 아래의 예제는 output 항목을 stdout 으로 설정했고 codec을 json으로 설정해서 아래와 같이 json 형식으로 보여지고 있다. 
- 다양한 output plugin을 지정해서 다른 분석 시스템이나, 데이터베이스로 로그를 보낼 수 있다. 
 
```
{
	"message": "127.0.0.1 - - [03/Feb/2016:14:43:58 +0900] \"POST /test/web HTTP/1.1\" 200 22410",
	"@version": "1",
	"@timestamp": "2016-02-03T05:43:59.585Z",
	"path": "/home/system/logs/test/access-2016-02-03.log",
	"host": "0.0.0.0",
	"clientip": "127.0.0.1",
	"ident": "-",
	"auth": "-",
	"timestamp": "03/Feb/2016:14:43:58 +0900",
	"verb": "POST",
	"request": "/test/web",
	"httpversion": "1.1",
	"response": "200",
	"bytes": "22410",
	"geoip": {
		"ip": "127.0.0.1",
		"country_code2": "KR",
		"country_code3": "KOR",
		"country_name": "Korea, Republic of",
		"continent_code": "AS",
		"region_name": "13",
		"city_name": "Seongnam",
		"latitude": 37.43860000000001,
		"longitude": 127.13780000000003,
		"timezone": "Asia/Seoul",
		"real_region_name": "Kyonggi-do",
		"location": [127.13780000000003, 37.43860000000001]
	}
}
```

**References**

- [input plugin](https://www.elastic.co/guide/en/logstash/current/input-plugins.html)
- [output plugin](https://www.elastic.co/guide/en/logstash/current/output-plugins.html)
- [filter plugin](https://www.elastic.co/guide/en/logstash/current/filter-plugins.html)
- [codec plugin](https://www.elastic.co/guide/en/logstash/current/codec-plugins.html)
