---
title: 'celery states'
author: 'ash84'
pub_date: '2016-01-11'
description: '아래는 celery 의 state 인데, 보통 celery-flower 조합으로 많이 쓰기 때문에 [flower](https://github.com/mher/flower)를 쓰다보면 조회 조건중에 states 가 있어서 아래와 같이 정리해본다. 즉시 실행하라고 명령하면 STARTED-SUCCESS 또는 FAILURE 로 표시되겠지만, `countdown`을 주어서 실행한 경우에는 즉, 어떤 예약을 거는 경우에는 해당 task가 RECEIVED 로 표시되게 된다. 그리고 [flower](https://github.com/mher/f'
featured_image: ''
tags: ['Celery', 'dev', 'Python', 'state']
---


아래는 celery 의 state 인데, 보통 celery-flower 조합으로 많이 쓰기 때문에 [flower](https://github.com/mher/flower)를 쓰다보면 조회 조건중에 states 가 있어서 아래와 같이 정리해본다. 즉시 실행하라고 명령하면 STARTED-SUCCESS 또는 FAILURE 로 표시되겠지만, `countdown`을 주어서 실행한 경우에는 즉, 어떤 예약을 거는 경우에는 해당 task가 RECEIVED 로 표시되게 된다. 그리고 [flower](https://github.com/mher/flower)상에서 RECEIVED 인 task들은 아직 미 실행 상태이기 때문에 REVOKED(취소) 시킬 수 있다. 아직까지 PENDING 이나 RETRY는 보지는 못한듯, RETRY는 따로 task를 설정해야 하는것으로 알고 있다.

**celery.states.PENDING = ‘PENDING’**  
 – Task state is unknown (assumed pending since you know the id).

**celery.states.RECEIVED = ‘RECEIVED’**  
 – Task was received by a worker.

**celery.states.STARTED = ‘STARTED’**  
 – Task was started by a worker (CELERY_TRACK_STARTED).

**celery.states.SUCCESS = ‘SUCCESS’**  
 – Task succeeded

**celery.states.FAILURE = ‘FAILURE’**  
 – Task failed

**celery.states.REVOKED = ‘REVOKED’**  
 – Task was revoked.(취소)

**celery.states.RETRY = ‘RETRY’**  
 – Task is waiting for retry.

참고로 [flower](https://github.com/mher/flower)는 그 자체로 모니터링이 가능한 UI를 제공하고 있는 동시에, [몇개의 API](http://flower.readthedocs.org/en/latest/api.html)를 제공하고 있는데 미약한편이다. tasks 들은 어떤 실행하는 명령을 delay 나 apply_aync 함수를 통해서 받게되면, [AsyncResult](http://docs.celeryproject.org/en/latest/reference/celery.result.html#celery.result.AsyncResult.id) 를 반환하는데 각각의 task 들을 구분하는 UUID가 그 안에 들어 있다.(정확히는 AsyncResult.id) 이 UUID 를 기반으로 한 task의 상태와 정보를 알수 있도록 구성해 놓은것이 flower이다. 아쉽게도 아직은 flower API에서 UUID 별로 정보를 주는 API를 지원하지는 않는데, [다음버전](https://github.com/mher/flower/pull/505)에 들어갈 것 같다.



