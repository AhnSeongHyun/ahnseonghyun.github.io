---
title: '[pull request] spgen, generate mysql stored procedure'
author: 'ash84'
pub_date: '2016-08-05'
description: ''
featured_image: ''
tags: ['dev', 'generate stored procedure', 'MySQL', 'sp', 'spgen', 'stored procedure']
---


#### **앞서서, 프로시저에 대한 이야기**

 ORM 이 추세이긴 하지만 여전히 사용하는 곳이 있다. 물론 로직이 숨어 있다는 문제, 가독성이 떨어지는 문제가 있지만 여전히 성능면에서는 최고의 방법이 아닌가 싶다.(이견이 있으시다면 댓글로,, <del datetime="2015-07-20T23:36:34+00:00">댓글구걸</del>)

현재 회사에서는 모든 데이터베이스 관련된 로직은 저장 프로시저(Stored Procedure) 방식으로 구현되고 있다. 개인적으로 이전 회사에서는 이런식으로 작업을 하지 않았고, ORM을 이용하거나 작은 프로젝트 같은 경우 Raw SQL을 이용했었는데 사실 적응하기 쉽지 않았던 것이 사실이다. 그럼에도 불구하고 한 가지 장점을 발견했는데:

– 작업의 분리 : 사실 웹 개발자가 DB 에서 데이터가져오고 하는 부분까지 다 해야 하지만 회사내에서는 워낙 프로시저 및 DB 관련 작업만 전담하는 팀이 따로 있다. 그래서 어떤 웹개발 작업이 들어오면 보통 DB 프로시저 개발하는 분과 일반 웹 개발자가 같이 작업하게 된다. 프로시저에서 어떤 데이터가 어떤 형태로 올것인지만 정의하고 나면 각자 작업을 해서 붙이는 식으로 작업을 한다. DB에 대한 지식이 조금은 적어지는 단점아닌 단점이 있을수는 있지만, 작업의 편의성적인 측면에서는 좋았던 것 같다.

 단점이라면 이상한 모임의 [im-developer](https://weirdmeetup.slack.com/messages/im-developer/) 채널에서도 애기했던 것 처럼, 가독성과 디버깅 문제가 있을 수 있다. 확실히 프로시저명 자체에서 모든것을 보여주지 않으면 다른 개발자(db 작업을 하지 않은)는 명확하게 해당 프로시저가 어떤 일을 하는지 알수가 없다. 그래서 어떤 문제가 생겼을 경우, 프로시저를 파헤쳐서 어떤 일을 하는지 파악해야 하는 번거로움이 있다.(그나마 그 안에 로그가 있으면 다행) 그리고 디버깅 적인 측면에서 로그가 남지도 않고, 물론 남길수도 있지만, DB서버는 대체적으로 분리되어 있는지라 보기가 어렵다. 재현해서 DB프로시저가 문제인지 그외의 다른 웹개발 파트가 문제인지 체크해 봐야 한다. 또 다른 단점으로는 DB 자체에 대한 종속성(Dependancy)을 들수 있는데 프로시저에 대한 기능이나 문법의 지원은 사실 DB마다 다르기 때문에 저장프로시저가 많아지고 한 프로젝트에서 대부분이 핵심기능을 저장프로시저에서 한다면, 특정 DB에 종속될 가능성이 높다.

#### **[spgen](https://github.com/jongha/spgen)**

 발단은 이렇다. 최근 시작한 프로젝트에서 저장프로시저를 사용해야 하는데, 꽤 많은 테이블이 있고, 해당 테이블들 마다. `select, update, delete, insert` 관련된 저장프로시저를 만들어줘야 하는 상황이었다. 다들 수작업으로 만드는데 어떻게 하면 좀더 쉽게 만들수 없을까 생각하다가, 우연치 않게 github를 찾아보게 되었다. 그리고 발견한게 [spgen](https://github.com/jongha/spgen). 뭐 여타의 다른 언어의 툴이 있었겠지만, 이것을 선택했다. 이유는 일단 파이썬으로 되어 있다는점, 그리고 한국 개발자가 만들었기 때문이다. 두번째 이유는 뭐 그리 문제가 생기기 전까지는 큰 장점으로 작용하진 않는데 첫번째 이유는 중요한데, 현재 프로젝트도 파이썬이고 주 언어가 파이썬이기 때문에 Ruby, Go 등의 내가 잘 알지 못하는 언어로 되어 있다면 언어자체를 배우는 시간이 더 필요하다.

```
usage: spgen.py [-h] [-P PORT] [-u USER] [-p PASSWORD] [-d] host database [tables [tables ...]]

$ spgen.py -uim -ppw localhost mydb table1 table2 

positional arguments:
    host                  Host to connect.
    database              Database name.
    tables                Table name. e.g table1 table2

optional arguments:
    -h, --help            show this help message and exit
    -P PORT, --port PORT  Port number to use for connection or 0 for default.
    -u USER, --user USER  User for login.
    -p PASSWORD, --password PASSWORD Password to use when connection to server.
    -d, --debug           Set Debug mode.
```

 spgen 은 별도의 설정파일 없이 커맨드라인을 통해서 실행 할 수도 있고, 라이브러리로 import 해서 사용할 수 있다. 사용해보니 좋은점도 있었지만 한 가지 아쉬운 점은 table 을 선택할 수가 없는 부분이 많았다. 내가 하는 프로젝트는 하나의 DB 내에서 여러 Table 이 있고, 하나의 화면 구현이 결국은 하나의 Table에 대한 저장프로시저의 구현과 같기 때문에, 자칫 [spgen ](https://github.com/jongha/spgen)을 사용하면 모든 Table에 다 프로시저를 생성해 버리는 문제가 생길것 같았다. 그래서 인자로 tables 를 받아서 개발자가 지정한 Table에 한해서만 저장 프로시저를 생성하도록 하였다.  
<script src="https://gist.github.com/AhnSeongHyun/9c3a5610b23cbd90b504.js"></script>

위의 diff 에서 보면, 추가한 부분을 알 수 있는데 `if not self.tables:` 부분은 이전에 내가 넣었던 부분이고, tables 를 통해서 받은 사용할 테이블 리스트와 mysql db 의 `show tables;` 을 통해서 나온 테이블 리스트와의 교집합에 해당 하는 Table 에 한해서만 저장 프로시저를 생성하도록 하였다.

꽤 오래전에 만드신 것 같아서 PULL REQUEST 가 받아질까? 하는 걱정도 있었지만, 다행히 잘 받아졌다. 단순히 기능을 추가한 것과 별개로 PR을 위해서 기본적으로 README.md 도 고치고, 테스트 케이스를 통과하기 위해서 ```travis.yml``` 도 수정하고, 새로운 파이썬 버전에 대한 테스트도 추가하는 등등의 작업을 하였는데, 뭔가 기여하고 있고 좀더 낫게 만들고 있다는 느낌을 받게 되는것 같다. PR을 보내는 과정이나 보내고 나서 기다리는 과정은 재밌고, 즐겁다. 마치 뭔가 허락을 받는 아이같은 느낌. [spgen](https://github.com/jongha/spgen) 은 지금은 `add(insert), update, delete` 에 한해서 프로시저를 생성하고 있고, 이 글을 쓰는 지금은 로컬에서 약간 더 수정한 버전을 가지고 현재 진행하는 프로젝트에서 잘 사용하고 있다.



