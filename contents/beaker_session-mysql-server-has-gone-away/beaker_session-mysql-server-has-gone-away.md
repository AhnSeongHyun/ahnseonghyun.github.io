---
title: 'beaker_session MySQL server has gone away'
author: 'ash84'
pub_date: '2017-10-26'
description: '매일 아침 와서 현재 개발중인 백오피스를 켜면 Internal Server Error 발생. 로그를 보니 아래와 같은 오류 발생 

```
OperationalError: (pymysql.err.OperationalError) (2006, "MySQL server has gone away (error(32, 'Broken pipe'))") [SQL: u'SELECT beaker_cache.data \\nFROM beaker_cache \\nWHERE beaker_cache.namespace = %(namespace_1)s'] [pa'
featured_image: ''
tags: ['dev', 'Python', 'FLASK', 'session', 'beaker', 'MySQL']
---

매일 아침 와서 현재 개발중인 백오피스를 켜면 Internal Server Error 발생. 로그를 보니 아래와 같은 오류 발생 

```
OperationalError: (pymysql.err.OperationalError) (2006, "MySQL server has gone away (error(32, 'Broken pipe'))") [SQL: u'SELECT beaker_cache.data \\nFROM beaker_cache \\nWHERE beaker_cache.namespace = %(namespace_1)s'] [parameters: {u'namespace_1': '17b85df148204386870d2de3b3beaf40'}]
```

beaker_session github issue 로 찾아보니 떡하니 클로징된 이슈가 있다. 

https://github.com/bbangert/beaker/issues/126

cache 를 쓰지 않기 때문에 `session.sa.pool_recycle` 을 아래와 같이 추가해주었다. 그리고 나서 다음날 다시 같은 현상이 발생하는지 체크했는데, 발생하지 않았다. 

```python 
    session_opts = {
        'session.type': 'ext:database',
        'session.url': app.config['SQLALCHEMY_DATABASE_URI'],
        'session.cookie_expires': True,
        'session.timeout': 600,
        'session.sa.pool_recycle': 250
    }
    app.wsgi_app = SessionMiddleware(app.wsgi_app, session_opts)
    app.session_interface = BeakerSessionInterface()
```

`session.sa.pool_recycle` 에 대한 자세한 내용은 아래의 글을 참고하자. 

- [SQLAlchemy를 사용하면서 MySQL Connection이 끊기는 문제](http://yongho1037.tistory.com/569)

