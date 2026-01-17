---
title: 'PIL(Python Image Library) 설치하기'
author: 'ash84'
pub_date: '2014-02-13'
description: '간단하게 썸네일을 만들어야 하는 작업이 있어서 python image  관련 라이브러리를 찾던중에 [PIL](https://pypi.python.org/pypi/PIL) 이라는 것을 발견했는데 설치 해야하는 부분에 문제가 생겨서 코멘트를 남긴다. 

**기본 설치**'
featured_image: ''
tags: ['decoder jpeg not available', 'dev', 'pil', 'PIL jpeg', 'PIL 설치', 'Python']
---
<span style="font-size: 11pt;">간단하게 썸네일을 만들어야 하는 작업이 있어서 python image  관련 라이브러리를 찾던중에 [PIL](https://pypi.python.org/pypi/PIL) 이라는 것을 발견했는데 설치 해야하는 부분에 문제가 생겨서 코멘트를 남긴다. </span>

**기본 설치**

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">$sudo pip install PIL</span>

</div><span style="font-size: 11pt;">위와 같이 기본적으로 설치하면 된다. 기본 썸네일을 만드는 코드를 돌려보면, </span>

<script src="https://gist.github.com/AhnSeongHyun/8951055.js"></script>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;"><span style="color: rgb(255, 0, 0);">decoder jpeg not available</span></span>

</div><span style="font-size: 11pt;">라는 문제가 나온다. 이건 jpeg 라이브러리가 없어서 생기는 문제라고 하는데 해결 방법은 아래와 같다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">  
 pip uninstall PIL </span>

<div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">brew install libjpeg </span></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">pip install PIL</span></div></div><div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">원래 우분투에서 apt-get으로 설치하면 되는데 mac osx 에서는 없기 때문에 [Homebrew](http://brew.sh/)를 이용해야한다. </span><span style="font-size: 11pt; line-height: 2; background-color: transparent;">주의할 점은 이미 PIL을 설치했다면 반드시 uninstall을 하고 libjpeg를 설치하고 PIL 을 설치해야 한다는 점이다. </span>

<span style="font-size: 11pt;">ps) 이렇게 설치하기 귀찮은 Python Library는 처음인듯. ㅡㅡ </span>

</div>

**Reference**

– [Homebrew 설치법](http://seraphmate.tistory.com/99)



