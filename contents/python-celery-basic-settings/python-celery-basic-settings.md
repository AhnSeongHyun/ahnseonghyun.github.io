---
title: 'python Celery 기본 세팅'
author: 'ash84'
pub_date: '2016-08-15'
description: ''
featured_image: ''
tags: ['bigdata', 'Celery', 'dev', 'Python', 'python celery settings', '병렬처리', '빅데이터', '파이썬']
---


예전부터 써보고 싶었는데 관련 업무가 주어져서(정확히는 그냥 내가 쓰고싶은데 업무시간에 테스트 하고 싶어서) 정리해 본다. 그냥 아주 기본적으로 돌려보는 정도. 

**Broker 세팅(Redis)**

– [redis.io](redis.io) 에서 설치하면 끝 

– 홈페이지에 나와있는 별도의 세팅은 redis.conf에서 하는것이 아님. 

**Task 만들기**

– 하고자 하는 일을 정의하는데 `@app.task` 라고 써둔다. 

<script src="https://gist.github.com/AhnSeongHyun/25df901d9dcd184d6e04.js"></script>

 

– 위의  코드에서 보면 add와 insert_log 같은 task 를 만들었다. 

  

**Task 등록하기**

– 정확히는 이것이 task 를 등록하는것이라고 볼수 있을지 모르겠다. 

```bash
$ celery -A tasks worker —loglevel=info
```

  

**호출하기**

– 우리가 만든 task 를 참조할수 있어야 한다. 

 

<script src="https://gist.github.com/AhnSeongHyun/9dec475c9cf52848f24c.js"></script>

– 단순히 `add.delay()`, `insert_log.delay()` 를 통해서 호출하고 있다. 

– python test.py 를 실행하면, 앞단계에서 켜둔 celery 에서 실행시간이나 결과등의 로그가 나오면서 실행이 되는것을 확인할 수 가 있다



