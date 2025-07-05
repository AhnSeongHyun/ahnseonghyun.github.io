---
title: 'k8s cronjob 제한'
author: 'ash84'
pub_date: '2019-01-20'
description: ''
featured_image: ''
tags: ['k8s', 'cronjob', 'limit', 'startingDeadlineSeconds', 'concurrencyPolicy']
---

원문 : [https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#cron-job-limitations](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#cron-job-limitations)

Cron Job 은 job을 시간에 맞춰서 생성한다. 

Cronjob object는 하나의 crontab 파일. 

crontab 파일(리눅스에서의 cron 포맷으로 생성된) 이 정기적으로 job을 실행시키는 것 

## Cron Job 제한

- 스케쥴된 시간당 하나의 job object 생성
    - 두개나 혹은 생성 자체가 안될수 있다.
    - 작업 자체가 멱등해야한다.(idempotent), 즉 여러번 작업해도 같은 결과물이 나오게 해야한다.

- `startingDeadlineSeconds` 을 크게 설정하고 `concurrencyPolicy` 를 `Allow` 로 설정하면, job 은 항상 적어도 한번만 실행된다.

- Cronjob controller 가 이전 스케쥴된 시간에서 현재시간까지 missed 된 스케쥴을 체크하는데 `100` 개가 넘으면 job 을 시작하지 않고 아래와 같은 메시지를 보여준다.


 > Cannot determine if job needs to be started. Too many missed start time (> 100). Set or decrease .spec.startingDeadlineSeconds or check clock skew.


- `startingDeadlineSeconds` 를 설정하게 되면 이전 스케쥴된 시간에서 현재시간 까지의 missed job을 카운팅 하는 것이 아니라, 지정한 시간동안 카운팅 하게 된다.
    - 200 으로 설정하면 200 초 동안 missed job 을 카운팅 한다.
- 예정된 시간에 cronjob 을 만들지 못한 경우 missed job 으로 카운팅한다.
    - `concurrencyPolicy` 를 `Forbid` 로 설정한 경우, 이전 job 이 실행중이면 생성하려고 시도하면 missed 로 카운팅한다.

## Cronjob ⇒ Job ⇒ Pod

- Crojob 은 Job의 생성만 책임을 진다.
- Job 은 해당 작업을 나타내는 Pod 을 관리한다.
