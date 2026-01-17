---
title: '(ngrinder) mac osx 에서 ngrinder 설치하기'
author: 'ash84'
pub_date: '2014-02-12'
description: '웹 서비스 부하테스트를 해야하는 작업이 있었는데 예전에 컨퍼런스에 가서 들었던 [ngrinder](http://www.nhnopensource.org/ngrinder/) 라는 툴이 생각나서 이번 기회에 익히면서 써보기로 하였다. 기본적인 설명이나 컨셉들은 본 글의 제일 하단에 Reference 부분을 참고하면 될것 같다.'
featured_image: ''
tags: ['ngrinder', '모니터링', 'server', '웹서비스 성능측정']
---
<span style="font-size: 11pt;">웹 서비스 부하테스트를 해야하는 작업이 있었는데 예전에 컨퍼런스에 가서 들었던 </span>[<span style="font-size: 11pt;">ngrinder</span>](http://www.nhnopensource.org/ngrinder/)<span style="font-size: 11pt;"> 라는 툴이 생각나서 이번 기회에 익히면서 써보기로 하였다. 기본적인 설명이나 컨셉들은 본 글의 제일 하단에 Reference 부분을 참고하면 될것 같다. </span>

<span style="font-size: 11pt;">설치법은 사실은 대부분 </span>[<span style="font-size: 11pt;">ngrinder 개발자 분이 운영하시는 블로그</span>](http://junoyoon.tistory.com/entry/nGrinder-%EC%84%A4%EC%B9%98%EB%B0%A9%EB%B2%95)<span style="font-size: 11pt;">를 참고를 했다. 들어가면 굉장히 많은 정보를 찾을수가 있는데 필자의 경우 윈도우나 리눅스가 아닌 맥북에어에서 설치해서 사용해야하기 때문에 그 관련된 부분에 대해서 몇가지 추가할 내용을 언급하겠다. </span>

<span style="font-size: 11pt;">위의 링크를 보시면 알겠지만, 컨트롤러와 에이전트 이렇게 2가지를 설치해야 한다. 물리적으로 다른 컴퓨터에 연결하냐는 문제를 떠나서 일단 필자는 같은 컴퓨터에 설치하였다. </span>

#### 1. 컨트롤러 설치

<button class="btn btn-primary btn-xs" onclick="window.location.href='http://sourceforge.net/projects/ngrinder/files/ngrinder-3.2.3/ngrinder-controller-3.2.3-with-tomcat.zip/download'" type="button"> Download </button>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">– 위의 링크에서 war를 가져와서 설치하는 방법이 있는데 필자의 경우 톰캣이 합본된 버전의 컨트롤러를 받았다. 굳이 세팅을 바꿀 필요성을 느끼지 못했고, 톰캣을 이것때문에 따로 설치해서 사용하고 싶지는 않았기에 합본버전을 받았다. </span>

<span style="font-size: 11pt;">– 받고 나서 해야할 가장 중요한 일은jvm 메모리 옵션을 바꿔주는 일인데, /bin/catalina.sh 에 적어주면 된다. </span>

<span style="font-size: 11pt;">– ./bin/startup.sh 로 실행하고 ./bin/shutdown.sh 로 종료 시키면 된다. </span>

<span style="font-size: 11pt;">– 실행되고 나면 http://localhost:8080 으로 접속하면 로그인 화면이 나올것이다. 이때에 admin/admin 으로 로그인 하면 되고 좀더 많은 팁이나 질문들을 로그인을 한뒤 보려면 언어를 한글로 체크하면 된다. </span>

#### 2. 에이전트 설치

<button class="btn btn-primary btn-xs" onclick="window.location.href='http://sourceforge.net/projects/ngrinder/files/ngrinder-3.2.3/ngrinder-core-3.2.3-agent-package.zip/download'" type="button">Download</button>

<span style="font-size: 11pt;">– 위의 다운로드 링크에서 agent를 받으면 된다. </span>

<span style="font-size: 11pt;">– 에이전트를 실행하기 전에 해야할일, JAVA_HOME 설정하기(</span>[<span style="font-size: 11pt;">링크</span>](http://www.mkyong.com/java/how-to-set-java_home-environment-variable-on-mac-os-x/)<span style="font-size: 11pt;">), 이것을 제대로 해주지 않으면 에이전트가 컨트롤러에 접속하지 못하는 문제가 발생되는것 같다. </span>

<span style="font-size: 11pt;">– ./run_agent.sh 로 실행하면 된다. 이때 콘솔창에서 로그가 나오는데 로그상에 문제가 있다면 무엇인가 잘못된 것이다. </span>

#### 3. 에이전트 승인하기

<span style="font-size: 11pt;">컨트롤러에서 테스트할 URL을 입력해서 테스트를 진행하는데 그전에 해야할일이 에이전트를 승인하는 일이다. 관리페이지(http://localhost:8080)에 접속해서 로그인한뒤에 사용자이름(admin)을 눌러보면 메뉴중에 “에이전트 관리” 라는 메뉴가 있다. 해당 메뉴를 눌러서 들어가면 위의 과정을 제대로 거쳤다면 아래와 같은 화면을 볼수 있을 것이다. 컨트롤러에 연결된 에이전트가 나오는데 이때 해당 에이전트를 승인해 주면 된다. </span>

![](http://ash84.net/wp-content/uploads/1/cfile25.uf.275CE74A52FACCBB313C50.png)

<span style="font-size: 11pt;">**Reference**</span>

<span style="font-size: 11pt;">– </span>[<span style="font-size: 11pt;">ngrinder : 아이들도 할수 있는 성능테스트</span>](http://deview.kr/2013/detail.nhn?topicSeq=2)<span style="font-size: 11pt;"> </span>

<span style="font-size: 11pt;">– </span>[<span style="font-size: 11pt;">ngrinder 설치방법</span>](http://junoyoon.tistory.com/entry/nGrinder-%EC%84%A4%EC%B9%98%EB%B0%A9%EB%B2%95)<span style="font-size: 11pt;"> </span>



