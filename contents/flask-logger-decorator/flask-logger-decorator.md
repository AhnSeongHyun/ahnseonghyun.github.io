---
title: 'flask logger decorator(데코레이터)와 함께 사용하기'
author: 'ash84'
pub_date: '2017-04-03'
description: ''
featured_image: ''
tags: ['Decorator', 'dev', 'FLASK', 'Logger', 'Python', 'flask 웹서버']
---

###기본로그 세팅하기###


로그에 대한 부분이 늘 걱정이긴 한데, 사실 따로 python logger 클래스를 사용해서 로그는 남기는 클래스를 만들고 만드는 프로젝트 마다 붙여서 사용하는 식으로 했었는데 이번에 flask 에 있는 logger 를 이용해 보기로 했다. 기본적으로 다음과 같은 몇개의 핸들러를 제공하고 있다. 

- FileHandler  – 로그 메시지를 파일에 남긴다. 

- RotatingFileHandler – 로그메시지를 파일에 남기고, 특정수 이상이면 다음파일로 넘겨서 로그를 만드는 핸들러, maxBytes 라는 생성자의 파라미터가 있음.

- NTEvenetLogHandler – 윈도우 시스템의 시스템 이벤트 로그에 남긴다. 만약 윈도우에 배포된다면 사용해라. 

- SysLogHandler –  유닉스 syslog


로그핸들러를 선택하고 나면, 아래와 같이 세팅을 해줘야 한다. app.logger 인스턴스에 `addHandler()` 메서드를 이용해서 선택한 로그핸들러를 등록하는 작업이라고 보면된다. 

<script src="https://gist.github.com/AhnSeongHyun/4c9449a41fdd56494468.js"></script>

일별로그를 파일에 남겨야 하는 요구사항이 있어서 레퍼런스를 찾던중에[TimedRotatingFileHandler](https://docs.python.org/2/library/logging.handlers.html) 를 찾았는데 시간과 관련지어서 로그를 분리해주는 핸들러이다. 다음과 같이 핸들러 등록작업을 해주었다. 

<script src="https://gist.github.com/AhnSeongHyun/4b56641bb81198fb4c67.js"></script>

위에서는 app.debug 에 따라서 세팅을 하고 말고를 설정했지만, 무조건 사용할 것이라서 특별히 분기타게 하진 않았다. TimedRotatingFileHandler 부분에서 when 부분에서 D 를 설정하면 일별로그를 남기겠다는 것이고 interval 을 1로 주어야 하루 단위로 파일을 쪼개준다. 파일명에 대한 부분은 filename 에 지정하고, 제일 처음에는 지정한대로 즉, test.log 대로 나오지만 지정한 시간이 지나면 새로운 파일이 생기면서 test.log + 날짜 시간 이(test.log.2014-11-10_17-23-54 )나오게 된다. 사용하는 방법(로그를 남기는 방법)은 그리 어렵지 않은데, app.logger.warn(msg), app.logger.debug(msg) 이런식으로 사용하면 된다.



###활용하기###


Flask 의  메인이 되는 즉, 어떤 URL 로 들어오는 함수에서 들어오는 요청에 대한 정보를 남기고 싶어졌다. 그렇다고 모든 flask view함수(@app.route 로 시작하는) 의 첫째줄에 app.logger.handler(“register”) 이런식으로 써주는건 너무 삽질이라는 생각에, 데코레이터(decorator)를 활용해 보기로 했다. 여러가지 정보를 남길수 있겠지만 일단 여기에서는 어느 URL로 들어왔는지 그리고 접속한 클라이언트 IP 정도만 남기도록 하였다. 

<script src="https://gist.github.com/AhnSeongHyun/f48ba3f675e147a1a0fc.js"></script>


url_log 라는 이름으로 데코레이터(decorator) 함수를 만들었고, 그 안에서 함수를 실제로 호출하기 직전에 flask 의 request 객체를 이용해서 URL과 IP 주소를 남기도록 하였다. 이렇게 하고 모든 URL과 맵핑되는 함수에 다음과 같이 적어준다. <script src="https://gist.github.com/AhnSeongHyun/f3fcd40e258f585e4878.js"></script>


몇군데 적어주고 나서 실행해 보면 다음과 같은 에러가 나오는 것을 확인할 수 가 있다. 정확히는 하나의 flask view 함수에서는 나지 않지만, 2개 이상의 view 함수들에 적용할 경우 발생하는 에러다. 

```
Traceback (most recent call last):  
  
   File “payon.py”, line 77, in <module>  
     @basicLog  
   File “/usr/lib/python2.6/site-packages/flask/app.py”, line 1013, in decorator  
     self.add_url_rule(rule, endpoint, f, **options)  
   File “/usr/lib/python2.6/site-packages/flask/app.py”, line 62, in wrapper_func  
     return f(self, *args, **kwargs)  
  
   File “/usr/lib/python2.6/site-packages/flask/app.py”, line 984, in add_url_rule  
     ‘existing endpoint function: %s’ % endpoint)  

AssertionError: **View function mapping is overwriting an existing endpoint function: newFunc
```

에러를 확인해 보면 overwriting 이라는 부분이 눈에 띄는데 여러개의 view 메소드 즉, register, signin 등의 메소드에 적용했을때 데코레이터 함수를 거치면서 newFunc 라는 이름이 View Fuction 으로 인식하기 때문에 발생하는 문제이다.

<br/><br/>

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>

<br/>

알다시피 flask 의 view function(register, signin과 같은)의 이름은 유일해야 한다. 즉 메소드 이름이 겹치면 발생되는 에러이다.(실제로 같은 두개의 View Function 을 같은 메소드 이름으로 만들면 에러를 볼 수 있다.) 즉 아래와 같이 되는 경우에 발생한다.

<script src="https://gist.github.com/AhnSeongHyun/c037fe2a1b7e6f922b27.js"></script>

위와 같은 문제를 방지하려면 데코레이터에 다음과 같이 functools 는 함수와 호출가능한 객체가 동작하는데 필요한 도구를 제공하는 역할을 하는데 그 안에서 wraps 는 랩핑되는 호출가능한 객체의 속성을 업데이트 하는 역할을 하는데 데코레이터를 쓸때 유용하다고 한다. 그 이유는 변형된 즉, 랩핑된 함수의 원래 속성을 가지게 만드는 역할을 하고 있다. 

<script src="https://gist.github.com/AhnSeongHyun/013bf0df134a7a8d25f3.js"></script>


그래서 위와 같이 func 인자, 이 인자로 VIew function 이 들어오게 되고, 이게 결국 랩핑되는 호출가능한 객체이다. 그 객체를 @wraps(func) 처리를 해주면 각각의 View Function 들이  newFunc 라는 랩핑된 이름이 아닌 고유의 유일한 이름을 가지고 구별되게 됨으로써 flask 실행시 에러를 일으키지 않게 된다. 
 
데코레이터를 활용하면 좀더 메서드에서 선작업(pre-process) 을 지정할 수가 있다. 본 글에서는 단순히 로그를 처리하는 작업을 했는데 좀더 나아간다면 암호환된 키를 체크한다던지 하는 등의 매 함수마다 체크하는 작업들을 하는것도 좋을것 같다. 데코레이터가 좋은 점은 반복코드를 줄여줄수 있다는 점이고 일반적인 함수호출 부분과 같은 역할을 하는것 같지만, 메인코드가 아닌 함수 선언 위쪽에 위치함으로써 좀더 개발자로 하여금 깔끔한 코드를 작성하게 하는것 같다. 

functools 에는 데코레이터 및 함수와 관련된 몇가지 기능들이 있으니 한번 살펴보면 좋은데 [PyMOTW](http://pymotw.com/2/functools/) 에 들어가서 보면 좀더 예제와 함께 잘 이해할 수가 있다. 

