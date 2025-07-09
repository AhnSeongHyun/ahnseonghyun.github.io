---
title: 'dnsperf 로 dns서버 성능 측정하기'
author: 'ash84'
pub_date: '2020-02-14'
description: '요즘 DNS 에 대해서 관심을 많이 가지게 되었는데 😂 domain name system 은 도메인 이름을 ip 로 바꿔주거나 그 반대의 역할을 하는 것으로 알고 있다. 일반적으로 AWS Route53, google dns(8.8.8.8, 8.8.4.4) 이 이런 역할을 하는 것으로 보면 된다. 
[https://www.dnsperf.com/#!dns-resolvers](https://www.dnsperf.com/#!dns-resolvers) 에 가면 속도/안정성 같은 부분의 통계를 볼 수 있다. 물론,직접 구축을 할 수도 있는데'
featured_image: ''
tags: ['dns', 'Performance', 'dns-performance', 'dnsperf']
---

요즘 DNS 에 대해서 관심을 많이 가지게 되었는데 😂 domain name system 은 도메인 이름을 ip 로 바꿔주거나 그 반대의 역할을 하는 것으로 알고 있다. 일반적으로 AWS Route53, google dns(8.8.8.8, 8.8.4.4) 이 이런 역할을 하는 것으로 보면 된다. 
[https://www.dnsperf.com/#!dns-resolvers](https://www.dnsperf.com/#!dns-resolvers) 에 가면 속도/안정성 같은 부분의 통계를 볼 수 있다. 물론,직접 구축을 할 수도 있는데 dnsmasq 나 core dns 같은 것을 통해서 만들 수 있다. 

그런데 이것도 어떻게 보면 **서버라서 성능에 대해서 측정을 할 필요가 있다.** 결국 어플리케이션 서버를 만들고 하나의 서버에서 다른 서버 혹은 DB서버를 호출할 때 일반적으로 ip 보다는 도메인을 쓰기 때문에 DNS 서버를 거쳐갈 수 밖에 없다. 당연히 트래픽이 늘면서 DNS 서버에 대한 호출이 늘 수 밖에 없고(캐시를 타겠지만) 그러다 보면 DNS 서버고 부하를 받는다. 

dnsperf 는 DNS 서버에 대한 성능을 측정할 수 있는 도구로 `C` 로 개발이 되어 있다.

다운로드 링크 : [https://www.dns-oarc.net/tools/dnsperf](https://www.dns-oarc.net/tools/dnsperf)

### 설치

### centos

```shell
> wget https://www.dns-oarc.net/files/dnsperf/dnsperf-2.3.2.tar.gz
> tar xfvz dnsperf-2.3.2.tar.gz
> cd dnsperf-2.3.2
> ./configure 
> ./make && make install
```

`configure` 과정에서 BIND 관련 오류가 발생한다면 아래와 같이 라이브러리를 설치해준다. 
```shell
> yum install -y bind-devel \
krb5-devel \
openssl-devel \
libcap-devel \
libxml2-devel \
json-c-devel \
GeoIP-devel    
```

### mac osx
```shell
> brew install dnsperf 
```

### 사용법
```shell
> dnsperf dnsperf -s 8.8.8.8 -d dns-test.txt -l 10 -c 3 -T 3 -Q 10000
```

`-s` : 테스트 할 nameserver 를 지정한다. 

`-d` : input data 로 형식은 아래와 같다. 테스트 할 도메인들의 리스트와 레코드를 적어주면 된다. 

```
google.com A 
naver.com A 
```

`-l` : 테스트를 수행할 시간 

`-c` : 수행할 클라이언트의 수 

`-t` : 스레드의 수 

`-Q` : 초당 쿼리수의 제한 

![dnsperf](https://s3.ap-northeast-2.amazonaws.com/static.ash84.io/images/blog/dnsperf/dnsperf.png)

단위 시간 내 어느정도 처리할 수 있는지, 그리고 동시 처리가 얼만큼 되는지, 쿼리 질의의 전송대비 실패/성공의 비율은 어느정도 되는지,  latency  는 어느정도 되는지 확인 할 수 있다. 

ps) dnsperf 말고 [dnsmeter](https://github.com/DNS-OARC/dnsmeter) 라는 것도 있으니 관심 있으면 둘러봐도 좋을 듯하다.  

**References :**

- [https://www.mankier.com/1/dnsperf](https://www.mankier.com/1/dnsperf)
- [https://www.redhat.com/en/blog/five-nines-dnsmasq](https://www.redhat.com/en/blog/five-nines-dnsmasq)
