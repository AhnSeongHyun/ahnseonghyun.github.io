---
title: 'celery + supervisord'
author: 'ash84'
pub_date: '2016-06-11'
description: 'celery 를 데몬방식으로 실행해야할 경우, [몇 가지 방법](http://docs.celeryproject.org/en/latest/tutorials/daemonizing.html)이 있는데 그 중에 하나가 supervisor 를 이용하는 것이다. 

```
pip install supervisor 
```

위와 같이 설치하고 나서 현재 celery task 가 있는 프로젝트에서 **supervisord.conf 를 만들고, 마지막줄에 celeryd.conf 를 include 를 한다.**

```
$ echo_supervis'
featured_image: ''
tags: ['Celery', 'daemonize', 'project-showcase', 'python', 'supervisord', 'tutorial']
---
celery 를 데몬방식으로 실행해야할 경우, [몇 가지 방법](http://docs.celeryproject.org/en/latest/tutorials/daemonizing.html)이 있는데 그 중에 하나가 supervisor 를 이용하는 것이다. 

```
pip install supervisor 
```

위와 같이 설치하고 나서 현재 celery task 가 있는 프로젝트에서 **supervisord.conf 를 만들고, 마지막줄에 celeryd.conf 를 include 를 한다.**

```
$ echo_supervisord_conf > supervisord.conf 
$ vi supervisord.conf

...

[include]
files = celeryd.conf

```
그리고 celeryd.conf 를 만들고 아래와 같이 작성한다. 

<script src="https://gist.github.com/AhnSeongHyun/2f64bc70889343bffeee0165ece5ca61.js"></script>

그리고 나서 `supervisord` 로 실행하면 된다. 


**Reference**

- [How to keep Celery running with supervisor](https://thomassileo.name/blog/2012/08/20/how-to-keep-celery-running-with-supervisor/)

