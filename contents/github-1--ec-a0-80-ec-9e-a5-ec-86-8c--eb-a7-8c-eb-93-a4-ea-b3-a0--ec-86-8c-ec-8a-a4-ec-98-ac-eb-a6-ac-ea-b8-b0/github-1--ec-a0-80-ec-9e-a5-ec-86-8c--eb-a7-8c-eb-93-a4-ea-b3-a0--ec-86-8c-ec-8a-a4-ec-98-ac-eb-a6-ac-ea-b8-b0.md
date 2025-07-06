---
title: '(GitHub) 1. 저장소 만들고 소스올리기.'
author: 'ash84'
pub_date: '2012-11-25'
description: '![](http://ash84.net/wp-content/uploads/1/cfile23.uf.1614B13450B2B45A2F0F75.PNG)

일단 github에 가입을 하고 [github for mac](http://mac.github.com/) 을 설치했다는 가정하에 시작을 하겠다.'
featured_image: ''
tags: ['github', 'github 소스 올리기', 'github 연동', 'github 저장소 만들기']
---


<div>![](http://ash84.net/wp-content/uploads/1/cfile23.uf.1614B13450B2B45A2F0F75.PNG)

</div><div></div><span style="font-size: 11pt;">일단 github에 가입을 하고 [github for mac](http://mac.github.com/) 을 설치했다는 가정하에 시작을 하겠다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 15px; line-height: 29px;">GitHub와 Git 에 대한 깊은 이해를 원하는분을 위한 링크</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 15px; line-height: 29px;">–  [GitHub 를 이용하는 전체흐름 이해하기 #1](http://blog.outsider.ne.kr/865)</span>

<span style="font-size: 15px; line-height: 29px;">–  [GitHub 를 이용하는 전체흐름 이해하기 #2](http://blog.outsider.ne.kr/866)</span>

</div><span style="font-size: 15px; line-height: 29px;"> </span>

<span style="font-size: 11pt;">**1. 저장소(repository) 만들기 **</span>

<span style="font-size: 11pt;">– create repository를 누르면 된다. </span>

<span style="font-size: 11pt;">– 아래와 같은 화면이 뜨고 Repository name을 입력하고 설명을 입력하면된다. </span>

<span style="font-size: 11pt;">– 설명은 선택사항이고, 나중에 또 입력할 수 있다. </span>

![](http://ash84.net/wp-content/uploads/1/cfile24.uf.185C984450B16BF52073DA.jpg)

<span style="font-size: 11pt;">– 생성하고 나면 아래의 화면으로 바뀔것이다. 여기서에서 Command line 으로 하면 힘들어 진다. 원래 예전에는 오직 command line을 통해서 했었는데 그건 좀 비효율 적이기 때문에 </span>**<span style="font-size: 11pt;">Setup in mac</span>**<span style="font-size: 11pt;"> 을 누르기를 권장한다. </span>

![](http://ash84.net/wp-content/uploads/1/cfile27.uf.166EA43650B16BF316724B.jpg)

<span style="font-size: 11pt;">**2. local 에 복사하기**</span>

<span style="font-size: 11pt;">– **Setup in mac** 을 누르면 [github for mac](http://mac.github.com/) 이 구동되면서 아래와 같은 화면이 나온다. </span>

<span style="font-size: 11pt;">– exs4j 라는 폴더를 어디에 둘것인지의 여부를 묻는것인데, 필자는 workspace 아래에 두었다. </span>

<span style="font-size: 11pt;">– 나중에 알겠지만 </span><span style="font-size: 11pt;">clone을 하면 .git 파일이 생긴다. </span>

![](http://ash84.net/wp-content/uploads/1/cfile6.uf.166E543650B16BF2160494.jpg)

<span style="font-size: 11pt;">– clone을 하면 아래의 화면에서 처럼 Repository가 로컬에 복사 된 것을 볼 수있다. </span>

![](http://ash84.net/wp-content/uploads/1/cfile7.uf.156D1D3650B16BF1186F63.jpg)

<span style="font-size: 11pt;">**3. 활용편**</span>

<span style="font-size: 11pt;">– 자, 나는 이클립스를 열어서 새로운 자바 프로젝트를 생성하고 이름을 exs4j로 입력 하였다. </span>

<span style="font-size: 11pt;">– 그리고 main () 함수가 있는 main 클래스를 만들었다. </span>

<span style="font-size: 11pt;">– 그리고 나서 github for mac을 열어서 exs4j 를 들어가서 changes를 열면 다음과 같은 화면을 볼 수 있다. </span>

<span style="font-size: 11pt;">– exs4j 밑에 어떤 폴더와 어떤 파일이 생성되었고, 어떤 내용이 추가되었는지를 볼 수 있다. </span>

![](http://ash84.net/wp-content/uploads/1/cfile9.uf.1969D23650B16BED1A26B7.jpg)

<span style="font-size: 11pt;">– 이 상태에서 commit 내용을 적어보자. 나는 first commit 이라고 적었다. </span>

<span style="font-size: 11pt;">– 적은 후에 **commit**을 누른후, 원래 github 서버에 올리려면 **sync**를 누르면 된다. </span>

<span style="font-size: 11pt;">**<span style="color: rgb(255, 0, 0);">– 그러나 처음에는 본 버전이 master 버전이라는 것을 알려줘야 하기 때문에 다른 작업을 하나 해줘야 한다. </span>**</span>

![](http://ash84.net/wp-content/uploads/1/cfile23.uf.176D073650B16BEB1872D8.jpg)

<span style="font-size: 11pt;">– github for mac 의 branches 탭을 선택을 하면 아래와 같은 화면을 볼 수 가 있다. </span>

<span style="font-size: 11pt;">– master 버전에 체킹이 되어 있을것이고, 오른쪽에** Publish** 버튼을 누르자. </span>

<span style="font-size: 11pt;">– 그러면 현재 버전이 처음으로 github에 올라간다. </span>

![](http://ash84.net/wp-content/uploads/1/cfile28.uf.126F683650B16BE913725A.jpg)

<span style="font-size: 11pt;">자, 이제 github의 생성한 Repository 에 가서 확인을 해보자. 아래의 화면처럼 이클립스의 exs4j 프로젝트에서 추가한 내용들을 볼 수 있다. 이렇게해서 쉽게(?) github에 re</span><span style="font-size: 11pt;">pository를 만들고 등록해 보았다. </span>

![](http://ash84.net/wp-content/uploads/1/cfile10.uf.176DD03650B16BE617B0A8.jpg)



