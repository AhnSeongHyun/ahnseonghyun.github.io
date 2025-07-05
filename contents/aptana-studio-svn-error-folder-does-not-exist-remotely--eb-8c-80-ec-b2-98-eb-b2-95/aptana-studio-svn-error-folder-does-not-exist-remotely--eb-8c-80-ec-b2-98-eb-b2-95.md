---
title: 'Aptana Studio SVN error folder '' does not exist remotely 대처법'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['Aptana Studio', 'dev', 'SVN', 'SVN error folder '' does not exist remotely', '이클립스']
---


<span style="font-size: 11pt;"></span><span style="font-size: 11pt;">몇개의 서버를 사용하고 있고 각각의 서버에 SVN이 설치되어 있는데 Aptana Studio 에서 SVN 플러그인을 다운받아서 설치해서 잘 쓰고 있었다. 그런데 새로운 서버의 SVN 에 연결하려고 하니 연결은 되는데 소스 디렉토리를 클릭하니까 아래와 같은 에러가 발생하는 것을 확인 하였다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">SVN error folder ‘SOURCE’ does not exist remotely</span>

</div><span style="font-size: 11pt;">즉, 한마디로 애기하면 원격으로 접근할수 없다. 이애기인데 여러가지 루트로 검색을 해 본결과 서버에 설치된 SVN 의 버전을 Aptana Studio 에서 지원하지 못해서 생기는 문제로 판명 되었다. 아래의 링크가 처음에 Aptana Studio 에서 SVN 플러그인을 설치할때 본 자료이다.([@haruair](https://twitter.com/haruair) 님의 자료는 언제나 깔끔하다.)</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">[http://haruair.com/blog/857](http://haruair.com/blog/857)</span>

</div><span style="font-size: 11pt;">자료에서 보면 http://subclipse.tigris.org/update_1.6.x 를 플러그인 사이트로 지정함으로써 찾게 하고 있는데, svn1.7 이상은 지원하지 못하는것 같다. tigris.org 에 가서 찾아보니 update_1.8.x 가 나온것을 확인 할 수가 있었다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">[http://subclipse.tigris.org/update_1.8.x/](http://subclipse.tigris.org/update_1.8.x/)</span>

</div><span style="font-size: 11pt;">위의 링크를 플러그인 설치할때 넣게 되면 svn 1.7 이상 버전과도 잘 호환되는것을 확인 할 수가 있다. 위의 에러 역시 사라지고 디렉토리에 접근 할 수가 있다. 이클립스나 Aptana Studio 에서 subclipse.tigris.org 을 잘 확인해 봐야 할것 같다. </span><span style="font-size: 11pt;"> </span>



