---
title: 'A/B Test Post 요청하기'
author: 'ash84'
pub_date: '2015-07-09'
description: ''
featured_image: ''
tags: ['ab', 'ab request post', 'apache']
---


ab 는 [apache bechmark testing](http://httpd.apache.org/docs/2.2/ko/programs/ab.html) 이라는 일종의 툴 인데, apache httpd를 설치하면 ./bin 디렉토리 내에 존재한다. 대략적인 사용법은 다음과 같다.

<script src="https://gist.github.com/AhnSeongHyun/0bccc2e3351c4db6a6b3.js"></script>

특히 가장 많이 사용하는 것이 `-c(concurrency)` 와 `-n(requests)` 옵션인데, 쉽게 애기하면 <storng>동시에 몇명이 총 몇개의 요청을 보낼것인가?를 정의하면 된다.</storng>

 

**./ab -c 50 -n 500 http://daum.net**

 

이런식으로 웹사이트, 웹페이지, 웹 API 등을 테스트 할 수 있다. 그런데 POST 의 경우에는 조금 불편한다. post 옵션은 특이하게 직접 명령어를 쓰는게 아니라 `-P` 옵션을 통해서 파일로 지정을 해야 한다. 그런데 주의할 점이 `-T(content-type)` 옵션으로 `application/x-www-form-urlencoded` 를 지정해 주어야 하고, `-P` 지정 파일에는 URL Encoding 된 데이터를 넣어줘야 한다.

 

**./ab  -T application/x-www-form-urlencoded -n 100 -c 100 -p post.text https://127.0.0.1/test**

 

ab 는 apache 서버를 설치하면 보통 bin 디렉토리에 들어있게 되는데 간단하게 테스트할 때는 좋은 것 같지만 여러군데 웹 사이트에서 찾아본 결과 ab 보다는 jmeter 가 더 낫다고 한다. 실제로 필자의 경우, 같은 조건으로 테스트를 하는데 jmeter 에서는 conenction refused 가 떨어지는것을 확인했지만, ab 에서는 별다른 문제가 없는 경우를 확인했다.

 

[http://stackoverflow.com/questions/10260526/which-gets-the-measurements-right-jmeter-or-apache-ab](http://stackoverflow.com/questions/10260526/which-gets-the-measurements-right-jmeter-or-apache-ab)

위의 글을 보면 좀더 자세한 이야기를 볼 수가 있는데, jmeter는 좀더 범용적으로 테스트 할 수 있어서 사람들이 많이 선호하는것으로 확인된다. 사실 위의 post 요청만해도 매우 불편하기 짝이 없다. 간단한 게 아닌 이상 그냥 jmeter 로 테스트 하시는게 좋을듯. 윈도우 아닌 환경에서 간단히 테스트하긴 굳.



