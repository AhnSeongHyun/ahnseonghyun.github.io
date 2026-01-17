---
title: 'jmeter non GUI mode'
author: 'ash84'
pub_date: '2015-07-07'
description: '[apache jmeter](http://jmeter.apache.org/) 라고 서버 Load Testing 툴인데, [사용법](http://codeigniter-kr.org/lecture/view/289/page/1)은 인터넷 보면 나와있다. 대부분이 윈도우 상에서 조건을 입력하고, 어떤 결과화면을 볼것인지를 설정하는 식으로 설명이 되어 있는데, 윈도우에서 설명한다는 약간의 아쉬움 점을 가지고 있다. 꽤 많은 테스트를 할 경우, 내 컴퓨터 상의 윈도우에서 테스트를 돌리다보면, 서버 보다 내 컴퓨터가 먼저 죽는 경우가 있다. 이'
featured_image: ''
tags: ['jmeter', 'jmeter non gui mode', 'tutorial']
---
[apache jmeter](http://jmeter.apache.org/) 라고 서버 Load Testing 툴인데, [사용법](http://codeigniter-kr.org/lecture/view/289/page/1)은 인터넷 보면 나와있다. 대부분이 윈도우 상에서 조건을 입력하고, 어떤 결과화면을 볼것인지를 설정하는 식으로 설명이 되어 있는데, 윈도우에서 설명한다는 약간의 아쉬움 점을 가지고 있다. 꽤 많은 테스트를 할 경우, 내 컴퓨터 상의 윈도우에서 테스트를 돌리다보면, 서버 보다 내 컴퓨터가 먼저 죽는 경우가 있다. 이건 jvm 메모리의 문제라기 보다는 컴퓨터의 메모리가 적어서 생기는 이슈이기도 하다.

그래서 많은 사용자를 대상으로 할때에는 다른 테스트 서버에서 테스트를 하고 싶어지는데, 앞서 말한것 처럼 대부분의 설명이 윈도우 기반이다 보니 jmeter non GUI Mode에 대한 설명을 찾기가 쉽지 않았다. 일단 기존의 윈도우에서 사용하던 설정 중에서 결과를 보는 화면관련 된 부분을 삭제하고, ThreadGroup 과 HttpRequest 부분만 두고 저장한다. 저장하게 되면 name.jmx 파일의 형태로 저장이 되는데, 이 파일이 있어야 리눅스 상에서 커맨드 툴을 이용해서 테스트를 할 수 가 있다.

<script src="https://gist.github.com/AhnSeongHyun/ff7f2964af8c44f3a424.js"></script>

조금 불편한 부분이기도 한데 ab 나 siege 처럼 시간이나 동접자수, 총 요청수를 파라미터로 지정할 수 있는게 아니라 jmx 파일을 통해서 지정해야 한다. 때문에 조금 번거로운 부분이 있다.

<script src="https://gist.github.com/AhnSeongHyun/314058d4e94a90a23f3c.js"></script>

파라미터를 보면 `-n` 과 `-t` 는 무조건 지정해야 한다. `-n` 은 GUI 모드를 사용하지 않겠다는 것이고 `-t`는 test.jmx 에 대한 지정을 위한 파라미터이다. `-j` 는 로그파일을 남기는 것인데, 필요하면 남기는것이 좋을것 같다. `-H`와 `-P` 는 proxy 관련 부분이다. 테스트를 하다보면 너무 많은 테스트로 인해서 테스트 자체가 느리게 수행되는것을 느낄수가 있는데, jmeter 실행 스크립트 내 jvm 메모리 관련 부분을 올려주면 좀 더 빠르게 실행되는것을 알수 있다. 기본은 512로 설정되어서 나오는데, 1024나 메모리 여유가 된다면 그 이상도 필요하다고 생각한다. 그래프를 뽑을수 없는 단점도 있지만, 대규모의 테스트를 하고 싶을때거나 리눅스 환경에서 테스트 해야할 때에는 non-gui mode를 이용해야 할 것 같다.

[5 Ways To Launch a JMeter Test without Using the JMeter GUI](https://blazemeter.com/blog/5-ways-launch-jmeter-test-without-using-jmeter-gui "5 Ways To Launch a JMeter Test without Using the JMeter GUI")



