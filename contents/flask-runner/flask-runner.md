---
title: 'flask-runner'
author: 'ash84'
pub_date: '2016-08-08'
description: 'Flask 에서 개발을 할 때, Debug 옵션을 키고 app 에 기본 내장된 개발서버를 사용한다. 그런데 파일을 수정하면 재시작하는 기능은 좋은데, `host` 나 `port` 를 지정해 놓고 사용하다가 변경할때 귀찮은 부분이 있다. 특히 `port` 같은 경우 특정포트를 지정해두면 꼭 다음날에 누군가 쓰고 있어서 다시 수정해서 실행해야 하는 번거로움이 있다. 

[flask-runner](https://github.com/miguelgrinberg/Flask-Runner) 는 커맨드라인으로 Flask 앱을 실행할 때 옵션들을 줘'
featured_image: ''
tags: ['FLASK', 'runner', 'flask-runner', 'dev', 'Programming', 'Python']
---

Flask 에서 개발을 할 때, Debug 옵션을 키고 app 에 기본 내장된 개발서버를 사용한다. 그런데 파일을 수정하면 재시작하는 기능은 좋은데, `host` 나 `port` 를 지정해 놓고 사용하다가 변경할때 귀찮은 부분이 있다. 특히 `port` 같은 경우 특정포트를 지정해두면 꼭 다음날에 누군가 쓰고 있어서 다시 수정해서 실행해야 하는 번거로움이 있다. 

[flask-runner](https://github.com/miguelgrinberg/Flask-Runner) 는 커맨드라인으로 Flask 앱을 실행할 때 옵션들을 줘서 실행할 수 있는 라이브러리다. host, port 뿐만 아니라, debug, reload 등을 설정 할 수도 있다. 

<script src="https://gist.github.com/AhnSeongHyun/e298af1d81b6bf08b17a97ddbdf5a358.js"></script>

위와같이 사용하는데, 자주 변경되는 부분은 커맨드라인에서 사용하고, 변경이 안되는 부분, host 같은 부분을 고정해놓고 사용하면 편할것 같다. Djnago 에 있는 manager.py 와 처럼 [flask-runner](https://github.com/miguelgrinberg/Flask-Runner) 를 이용해서 manager.py 라고 명명하고 커맨드에서 실행해서 사용하고 있다. 

**References**
- https://github.com/miguelgrinberg/Flask-Runner
