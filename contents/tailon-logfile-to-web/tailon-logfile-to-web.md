---
title: 'tailon 으로 로그파일 웹에서 보기'
author: 'ash84'
pub_date: '2016-03-29'
description: '서버에 있는 로그를 웹상의 타인에게 보여줘야 할 경우가 있는데(가급적 이런 경우는 좋지 않은 상황인 경우이다.) 어떻게 할까 찾아보다가 python 으로 된 tailon 이라는 쉽게 커맨드 명령어로 띄울 수 있는 툴이 있어서 소개한다. 

https://github.com/gvalkov/tailon
http://tailon.rtfd.org/

특별한 새로고침 없이 자동으로 로그가 올라오고 **GREP** 이나 **AWK**를 항목이 UI상에 있기 때문에 원하는 검색 키워드를 입력하면 바로 검색해서 보여준다. 한가지 단점은 이상하게'
featured_image: 'http://tailon.readthedocs.org/en/latest/_images/awk.png'
tags: ['dev', 'logfile', 'weblog', 'tailon', 'Python', 'log.io']
---

서버에 있는 로그를 웹상의 타인에게 보여줘야 할 경우가 있는데(가급적 이런 경우는 좋지 않은 상황인 경우이다.) 어떻게 할까 찾아보다가 python 으로 된 tailon 이라는 쉽게 커맨드 명령어로 띄울 수 있는 툴이 있어서 소개한다. 

https://github.com/gvalkov/tailon
http://tailon.rtfd.org/

특별한 새로고침 없이 자동으로 로그가 올라오고 **GREP** 이나 **AWK**를 항목이 UI상에 있기 때문에 원하는 검색 키워드를 입력하면 바로 검색해서 보여준다. 한가지 단점은 이상하게 로그의 마지막 줄이 잘리는 것 처럼 보이는데, 우상단의 `위로화살표` 버튼을 클릭하면 툴바가 사라지고 보여지게 된다. 

######설치######
```
$ pip install tailon
```

######사용법######

```
Usage: tailon [-c path] [-f path [path ...]] [-h] [-d] [-v] [-b addr:port]
              [-r path] [-a] [-m [cmd [cmd ...]]] [--no-wrap-lines]

Tailon is a web app for looking at and searching through log files.

Required options:
  -c, --config path               yaml config file
  -f, --files path [path ...]     list of files or file wildcards to expose

General options:
  -h, --help                      show this help message and exit
  -d, --debug                     show debug messages
  -v, --version                   show program's version number and exit

Server options:
  -b, --bind addr:port            listen on the specified address and port
  -r, --relative-root path        web app root path
  -a, --allow-transfers           allow log file downloads
  -m, --commands [cmd [cmd ...]]  allowed commands (default: tail grep awk)

User-interface options:
  --no-wrap-lines                 initial line-wrapping state (default: true)

Example config file:
  bind: 0.0.0.0:8080      # address and port to bind on
  allow-transfers: true   # allow log file downloads
  relative-root: /tailon  # web app root path (default: '')
  commands: [tail, grep]  # allowed commands
  wrap-lines: true        # initial line-wrapping state

  files:
    - '/var/log/messages'
    - '/var/log/nginx/*.log'
    - '/var/log/xorg.[0-10].log'
    - '/var/log/nginx/'   # all files in this directory
    - 'cron':             # it's possible to add sub-sections
        - '/var/log/cron*'

Example command-line:
  tailon -f /var/log/messages /var/log/debug -m tail
  tailon -f '/var/log/cron*' -a -b localhost:8080
  tailon -f /var/log/
  tailon -c config.yaml -d
```

위의 사용법을 보면 알겠지만, `conf`를 yaml 형식의 파일로 작성하게 되어 있고, `-f` 옵션을 통해서 로그 파일을 지정하면 되고, `-b` 옵션을 통해서 보여질 포트를 지정하면 된다. 
