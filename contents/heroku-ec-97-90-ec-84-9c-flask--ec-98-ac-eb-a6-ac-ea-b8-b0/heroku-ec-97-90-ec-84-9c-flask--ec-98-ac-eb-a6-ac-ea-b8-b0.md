---
title: 'heroku에서 flask 올리기'
author: 'ash84'
pub_date: '2015-03-31'
description: 'heroku 를 아주 간단히 설명하자면 마치 서버를 가지고 있는것 처럼 웹의 공간을 대행해주는 업체인데, 클라우드 어플리케이션 플랫폼이라고한다. 특이하게 git 을통해서 올리고 내리고 함으로써 소스를 서버에 반영할 수 가 있다. heroku 에서는 python 부분은 기본적으로 django를 기본으로 하고 있는데 **[heroku에서 제공하는 flask 가이드](https://devcenter.heroku.com/articles/getting-started-with-python-o)**를 기본으로 해서 설명하겠다.  

가입을 하'
featured_image: ''
tags: ['Flask', 'dev', 'heroku', 'heroku with flask', 'python']
---
heroku 를 아주 간단히 설명하자면 마치 서버를 가지고 있는것 처럼 웹의 공간을 대행해주는 업체인데, 클라우드 어플리케이션 플랫폼이라고한다. 특이하게 git 을통해서 올리고 내리고 함으로써 소스를 서버에 반영할 수 가 있다. heroku 에서는 python 부분은 기본적으로 django를 기본으로 하고 있는데 **[heroku에서 제공하는 flask 가이드](https://devcenter.heroku.com/articles/getting-started-with-python-o)**를 기본으로 해서 설명하겠다.  

가입을 하고나서 toolbelt 라는것을 설치해야 한다. toolbelt 의 역할은 heroku 관련 명령어를 처리하는 역할을 한다. 아래의 링크에 가면 각 플랫폼 별로 설치할수 있는데 필자의 경우 ubuntu 버전으로 설치를 하였다.

> https://toolbelt.heroku.com

 
그리고 나서 아래와 같이 login 작업을 해준다. 


```
heroku login 
Enter your Heroku credentials. 
Email: kenneth@example.com 
Password: Could not find an existing public key. Would you like to generate one? [Yn] 
Generating new SSH public key. Uploading ssh public key /Users/kenneth/.ssh/id_rsa.pub
```
 

로그인 작업을 해주고 나서는 하나의 디렉토리를 만든다. 이 디렉토리가 실제로 내가 작업하는 프로젝트 디렉토리라고보면 된다. 

```
$ mkdir helloflask
$ cd helloflask
```

만든후에는 사실 가이드라인에서는`virtualenv` 를 이용해서 작업을 하도록 권장하고 있는데(원래 그게 맞다.) 여기서는 생략하고 설치해야 할것은 Flask 와 gunicorn 이다. pip 를 이용해서 설치되어 있다는 가정하에 진행</span><span style="font-size: 11pt;">하도록 하자. 

아래와 같이 `helloworld.py` 라고 이전에 만든 프로젝트 디렉토리(helloflask)에 입력한다. 코드는 간단하다.

```
import os
from flask import
Flask app = Flask(name) 

@app.route('/') 
def hello(): 
    return'Hello World!'
```
 
 다음은`Procfile`을 만드는 부분인데, 일종의 설정 .ini 파일이라고 생각하면되겠다. 이 부분에서 많이 헤맸는데, 파일 이름은 별도의 확장자 없이` Procfile `이다.(이건 진짜 이상함)  

```
web: gunicorn hello:app
```

위와 같이 입력하면 된다. 원래의 예제에서는 `--log-file` 부분이 있었는데 별도의 로그를 안썼더니 나중에 배포과정에서 에러가 나서 처음에는 그냥 뺴는게 나을 것 같다.

```
foreman start 
2013-04-03 16:11:22 [8469] [INFO] Starting gunicorn 0.14.6 
2013-04-03 16:11:22 [8469] [INFO] Listening at: http://127.0.0.1:5000 (8469)
```

예제에서 있는 `foreman start` 라는 부분은 `foreman` 은 heroku 에서 toolbelt 설치될때 설치되는데 위의 명령어를 이용해서 로컬에서 테스트 하는 과정이라고 보면 된다.

```shell
pip freeze > requirements.txt
```

virtualenv 를 쓰면 pip freeze 시에 그 가상의 환경안에 있는 `pip list` 만 export 가 된다. 그래서 주로 사용하는데 (독립적인 공간을 사용하기 위해서) 일단 requirements.txt 에서 우리가 만드는 웹이 필요로 하는 파이썬 모듈을 명시해 주어야 한다. 

```
$ git init 
$ git add . 
$ git commit -m "init"
```
 
 배포 작업을 위해서는 일단 git 으로 초기화를 해주고 현재 프로젝트 디렉토리에 있는 파일들을 추가해준다. 그리고 나서 커밋을 한다. 커밋을 하고 나서는` git push`를 해서 heroku 에 넣어야 하는데 일단 처음이기 때문에 다음과 같이 `heroku create `로 공간을 만들어야 한다. 재밌는 점은 어떤 공간이름도 주지 않아도 된다.  


```
heroku create
Creating stark-window-524... done, stack is cedar-14 http://stark-window-524.herokuapp.com/ | git@heroku.com:stark-window-524.git Git remote heroku added
```


생성되고 나면 다음과 같이 git push 명령어를 통해서 공간에 배포를 하면된다. 아래의 명령어는 추후에 소스를 수정하더라도 commit 후 배포할때 자주 사용하는 명령어이다. 


```
git push heroku master 
Counting objects: 10, done. 
Delta compression using up to 8 threads. 
Compressing objects: 100% (8/8), done. 
Heroku To git@heroku.com:stark-window-524.git * [new branch] master -> master
```

 

배포되고 나면,이제 실행을 해야하는데 아래와 같이 ps 명령어를 통해서 키면 된다.(정확히는 모르겠지만, dyno 라는 heroku 내의 컨테이너를 이용한다고 한다.)

```
heroku ps:scale web=1 
Scaling web processes... done, now running 1
```


확인하려면 아래와 같이확인하면 된다. (리눅스의 ps 와 같다.)

```
heroku ps 
web: `gunicorn hello:app`
web.1: up for 5s
```
 
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>


원래 예제에서는 `open`명령어를 통해서 웹페이지를 여는데, ubuntu 에서는 문제가 생긴다. 디스플레이 할수 없기 때문인데, 웹 페이지를 확인 하기위해서는 heroku.com 에 가서 Personal App 부분에서 Setting 부분에 보면 domains 부분에 url을 확인 할 수가 있다. 나중에는 settings 부분에서 이름을 수정함으로써 app.heroku.com 으로 접근할 수가 있다.

말로만 들었던 heroku 를 해봐서 너무 재밌었는데 여러가지 좋은점이 있겠지만, 내가 느낀점은 테스트 서버나 사내 서버로만 여러가지 요즘의 외부 서비스나 툴들을 테스트 할 수가 없다. 도메인을 요구하거나 public ip를 요구하는 경우가 많기 떄문에 그런 툴들을 이용하기 위해서 heroku는 좋은 대안이 될수 있겠다는 생각이 든다. 


