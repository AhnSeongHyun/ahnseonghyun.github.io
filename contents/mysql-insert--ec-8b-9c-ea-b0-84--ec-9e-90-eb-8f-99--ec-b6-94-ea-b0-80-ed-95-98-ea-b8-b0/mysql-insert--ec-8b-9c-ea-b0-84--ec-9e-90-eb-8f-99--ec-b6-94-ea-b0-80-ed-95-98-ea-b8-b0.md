---
title: '(mysql) insert 시간 자동 추가하기'
author: 'ash84'
pub_date: '2017-02-24'
description: ''
featured_image: ''
tags: ['dev', 'INSERT 시간 추가', 'MySQL', 'timestamp', 'UPDATE 시간 추가', 'insert', 'update']
---


<span style="font-size: 11pt; ">데이터베이스 입력 시간이 중요할때가 있다. 예를 들면, 어떤 데이터를 수집한다고 할때, 일별 혹은 시간별 데이터를 뽑기 위해서는 입력시간 컬럼을 넣어주는 것이 필요하다. 프로그램상에서 Date 형으로 넣어 줄수도 있겠지만, SQL 은 짧으면 좋다고, INSERT OR UPDATE 시 자동으로 시간을 추가하는 방법을 사용하면 더 좋은것 같다. </span>

**<span style="font-size: 11pt; ">1. TIMESTAMP 컬럼 추가. </span>**

<span style="font-size: 11pt; ">– 원하는 테이블, 즉 INSERT, UPDATE 가 발생하는 테이블에 TIMESTAMP 형의 컬럼을 추가한다. 필자는 register_time 이라는 컬럼을 추가하였다. </span>

**<span style="font-size: 11pt; ">2. Allow Null 해제 </span>**

<span style="font-size: 11pt; ">– register_time 컬럼에 대한 널허용을 해제한다. 널 허용을 하면 기본값이 널로 들어가버린다. </span>

**<span style="font-size: 11pt; ">3. 기본값 지정</span>**

<span style="font-size: 11pt; ">– CURRENT_TIMESTAMP 로 기본값을 지정한다. 이 값에 의해서 현재 시간이 들어가게 된다. </span>

**<span style="font-size: 11pt; ">4. UPDATE시에도 변경을 원한다면, on update CURRENT_TIMESTAMP 지정.</span>**<span style="font-size: 11pt; "> </span>

<span style="font-size: 11pt; ">– 이것을 지정하지 않으면 INSERT 시에만 시간값이 들어가게 되는데, 사용자가 UPDATE 가 필요하다면 위의 옵션을 지정해 주어야만 한다. </span>

<span style="font-size: 11pt; ">여러가지 스탭이 있는것 처럼 애기하지만 실제로는 CREATE TABLE 구문에서 아래와 같이 지정해 주면 된다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; "><span style="font-size: 11pt; ">CREATE TABLE XXX (</span>

<span style="font-size: 11pt; ">…</span>

<span style="font-size: 11pt; "> ‘register_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,</span>

<span style="font-size: 11pt; ">…</span>

<span style="font-size: 11pt; ">)</span>

</div>

