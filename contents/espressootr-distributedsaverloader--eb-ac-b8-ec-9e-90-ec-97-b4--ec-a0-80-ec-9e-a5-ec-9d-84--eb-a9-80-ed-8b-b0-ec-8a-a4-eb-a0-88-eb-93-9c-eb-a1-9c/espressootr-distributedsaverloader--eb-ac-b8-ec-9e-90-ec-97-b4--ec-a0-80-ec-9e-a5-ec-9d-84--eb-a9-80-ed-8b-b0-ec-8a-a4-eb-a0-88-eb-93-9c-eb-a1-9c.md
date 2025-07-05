---
title: '(espressoOtr) DistributedSaver/Loader, 문자열 저장을 멀티스레드로.'
author: 'ash84'
pub_date: '2013-03-13'
description: ''
featured_image: ''
tags: ['DistributedLoader', 'DistributedSaver', 'espressoOtr', 'github', 'https://github.com/AhnSeongHyun/espressoOtr', '검색엔진', '문자열 저장', '사전 만들기']
---


<span style="font-size: 11pt;">검색 엔진관련 모듈에 있어서 사전은 필수적인 부분인데, 빅 데이터라는 말이 나오면서 사전의 사이즈가 굉장히 커지는것 같다. 원래 사용자가 제공하는 혹은 사용자 검색 로그에서 추출된 데이터로 사전을 만들어서 사용하는데 중간에 빠른 로딩을 위해서 사전을 정렬한 채로 저장하는 방식을 사용하기도 한다. 그런데 **중간에 정렬하는 방식은 사전의 크기에 영향을 많이 받는다. 즉, 크기가 커지면 정렬하는것도 정렬 사전을 만드는것도 다시 로드시 읽어오는 작업도 오래 걸린다. **</span>

<span style="font-size: 11pt;">이러한 문제를 극복할 수 있는 방법은 여러가지가 있지만,** 파일로 저장하는 부분에 있어서 스레드를 이용해서 여러가지 파일에 나누어서 저장하는 방식을 소개하고자 한다. 멀티 스레드를 이용하게 되면 단일 스레드에서 저장하던 방식 보다는 빠르게 저장할 수 있다. 그러나 번거로운 점은 다수의 파일로 나누어서 저장한 만큼 다수의 파일에서 읽어와서 로딩해야한다는 점이다. **</span>

<span style="font-size: 11pt;">[espressoOtr](https://github.com/AhnSeongHyun/espressoOtr) 라이브러리에서는 이러한 부분은 쉽게 제공하기 위해서 **DistributedSaver**, **DistributedLoader** 클래스를 만들었다. 일단 **DistributedSaver**의 코드를 보자. </span>

<script src="https://gist.github.com/AhnSeongHyun/5157516.js"></script>

<span style="font-size: 11pt;">기본적으로 저장할 List<String> 을 받아서 저장하게 되어 있다. 저장할 파일명과 파일 확장자 그리고 몇개의 파일로 나누어서 저장할 것인지에 대한 카운트(distCount) 를 getter/setter를 통해서 받게 되어 있다. save 함수에서는 ExecutorService를 통해서 저장하도록 되어 있는데, 사용자가 지정한 distCount 만큼</span><span style="font-size: 11pt;"> thread pool 을 생성하고 distCount로 저장한 원 데이터를 나눈다. 그리고 나서 각각의 스레드에 나누어진 데이터와 저장할 파일명을 할당하면 된다. SaveRunnableThread 에서는 데이터를 파일에 BufferedStream을 이용해서 저장을 한다. 주의할점 중 하나는 distCount 만큼 파일명에 번호가 붙는다는 것이다. 예를들어, 4라고 지정한다면, db0.txt, db1.txt 이런식으로 파일명이 설정되게 된다. </span>

<script src="https://gist.github.com/AhnSeongHyun/5157522.js"></script>

<span style="font-size: 11pt;">읽어오는 **DistributedLoader** 클래스는 훨씬 단순하다. load() 함수의 인자를 통해서 읽어올 파일의 주소 리스트를 받게 되면 **멀티 스레드로 읽어오는데 이때에는 newCachedThreadPool을 이용하였는데, 이유는 읽어올 파일이 너무 많은 경우에는 그 만큼의 스레드를 생성해서 읽어오는 것이 I/O 속도에는 제한이 있기 때문에 의미가 없을 것이라고 판단하였다. **읽어올 때는 단순히 List<String> 으로 받아오는 것이 아니라, 읽어온 파일명을 키</span><span style="font-size: 11pt;">로, 그 안에 있는 내용(List<string)을  값으로해서 Map 객체를 만들어서 반환한다. 개발자가 어떤 파일에서 읽어왔는지에 대한 정보가 필요 할 수 있을것 같아서 만들어둔 장치이다. </span>

<span style="font-size: 11pt;">자세한 내용은 [espressoOtr](https://github.com/AhnSeongHyun/espressoOtr) 라이브러리를 찾아 보면 되는데, 구코드를 보면 알겠지만 그렇게 어렵게 구현된 코드가 아님을 미리 밝힌다. 필요하다면 잘 사용하시길 바라며, 부족한게 있다면 댓글을 달아주시길 기대한다. </span>

<span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;"></span>



