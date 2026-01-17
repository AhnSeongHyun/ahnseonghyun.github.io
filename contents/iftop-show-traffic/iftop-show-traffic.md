---
title: 'iftop 설치, 실시간 트래픽 확인하기'
author: 'ash84'
pub_date: '2017-11-15'
description: '실시간 트래픽을 보고 싶을때가 있는데, 여러가지 툴들이 있겠지만 iftop 을 설치하면 좀 더 간단하게 볼 수 있다. 

![iftop](https://farm5.staticflickr.com/4553/38383480446_08b68be12e_b.jpg)
### 설치하기 

```
# centos
yum install iftop
```
```
# ubuntu
apt-get install iftop
```

### 사용하기 

```
$ iftop
```


좌측에는 서버 IP 우측에는 클라이언트 IP 를 보여준다. 우측에 3컬럼은'
featured_image: ''
tags: ['dev', 'iftop', 'traffic', 'network']
---

실시간 트래픽을 보고 싶을때가 있는데, 여러가지 툴들이 있겠지만 iftop 을 설치하면 좀 더 간단하게 볼 수 있다. 

![iftop](https://farm5.staticflickr.com/4553/38383480446_08b68be12e_b.jpg)
### 설치하기 

```
# centos
yum install iftop
```
```
## ubuntu
apt-get install iftop
```

### 사용하기 

```
$ iftop
```


좌측에는 서버 IP 우측에는 클라이언트 IP 를 보여준다. 우측에 3컬럼은 각각 2초, 4초, 10초 동안의 평균 전송량을 보여준다. 

그리고 하단에 나와있는 정보는 다음과 같은 의미를 가진다. 

- TX : 전송 
- RX : 수신
- TOTAL : 전체 
- cumm : iftop 실행후 현재까지의 총 데이터량
- peak : 피크시의 데이터 
- rates : 각각 2초, 4초, 10초의 평균흐름 

### 실행옵션 

```
$ iftop --help 
Synopsis: iftop -h | [-npblNBP] [-i interface] [-f filter code]
                               [-F net/mask] [-G net6/mask6]

   -h                  display this message
   -n                  don't do hostname lookups
   -N                  don't convert port numbers to services
   -p                  run in promiscuous mode (show traffic between other
                       hosts on the same network segment)
   -b                  don't display a bar graph of traffic
   -B                  Display bandwidth in bytes
   -i interface        listen on named interface
   -f filter code      use filter code to select packets to count
                       (default: none, but only IP packets are counted)
   -F net/mask         show traffic flows in/out of IPv4 network
   -G net6/mask6       show traffic flows in/out of IPv6 network
   -l                  display and count link-local IPv6 traffic (default: off)
   -P                  show ports as well as hosts
   -m limit            sets the upper limit for the bandwidth scale
   -c config file      specifies an alternative configuration file
```


#### `-f` 옵션 사용 ip 필터링해서보기 

- 특정 ip로 들어오는 클라이언트에 대해서만 보고 싶을 때가 있다. 예를들면, 10.10.1.175 로 들어오는 ip 만 따로 보고 싶다고 하면 아래와 같이 `-f` 필터링 옵션을 주면 된다. `-f` 옵션에 대한 값은 [pcap-filter 형식의 필터](http://www.manpagez.com/man/7/pcap-filter/)를 넣어야 한다. 이게 좀 불편한데 대략적인 형식은 아래와 같다. 

  - dst host xxxx	
  - dst net xxxx	
  - dst port xxxx	
  - dst portrange start-end	
  - src host xxxx
  - src net net
  - src port xxxx
  - src portrange start-end
  - gateway xxxx
  - ip proto protocol


```
iftop -f 'ip dst 10.10.1.175'
iftop -i eth0  -f  “dst host Linux.com”
iftop  -i  eth1   -f    “dst port 22″
```


### 인터랙티브 모드 단축키 

- iftop 을 실행한 상태에서 특정키를 눌러서 아래와 같이 실시간으로 표시를 변경할 수 있다. 

```
f - filtering 
t - rx only | tx only | both
p - port display
P - pause
j/k - scroll up/down
b - bar graph on/off
L - lin/log scales
T - cumulative totals
n - name resolution
h - help for more keys and info
```

### 설정파일 

- 설정파일은 `~/.iftoprc` 에 저장하면 사용할 수 있고 실행옵션에서 `-c` 옵션을 이용해서 지정할 수 있다. 
- 자세한 내용은 [iftop manpage](https://linux.die.net/man/8/iftop) 을 확인해보자. 
```
## .iftoprc
## config file for iftop
dns-resolution: no
port-resolution: no
show-bars: yes
promiscuous: yes
port-display: on
hide-source: no
hide-destination: no
use-bytes: yes
line-display: one-line-both
show-totals: yes
log-scale: yes
```


