---
title: '[JAVA] correctDirectoryPath(), 디렉토리 경로 한번더 검사하기.'
author: 'ash84'
pub_date: '2012-11-05'
description: '간혹 디렉토리 안에 여러가지 파일에 대해서 접근해야 할때, 디렉토리 경로를 받을때가 있다. 그런데 이 경로를 가지고 뭔가 작업을 할때 머리속에 늘 남는것 중 하나가 바로 사용자의 입력 행태이다. 즉, 사용자는 디렉토리 경로를 다음과 같이 입력할수 있다.'
featured_image: ''
tags: ['dev', 'File', 'Java', '디렉토리 경로 검사', '자바 디렉토리 추출']
---


<span style="font-size: 11pt; ">간혹 디렉토리 안에 여러가지 파일에 대해서 접근해야 할때, 디렉토리 경로를 받을때가 있다. 그런데 이 경로를 가지고 뭔가 작업을 할때 머리속에 늘 남는것 중 하나가 바로 사용자의 입력 행태이다. 즉, 사용자는 디렉토리 경로를 다음과 같이 입력할수 있다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; "><span style="font-size: 11pt; ">./dumpfiles/</span>

<span style="font-size: 11pt; ">./dumpfiles</span>

</div><span style="font-size: 11pt; ">절대 경로, 상대경로에 상관없이 첫번째 경우와 같이 들어오면 큰 문제가 없다. 디렉토리 경로+파일이름의 방식으로 파일의 전체 경로를 지정해 주면 되는데, 두번째 경우는 경로 구분자가 없기 때문에 그게 안된다. 그래서 아래와 같은 코드를 만들어서 디렉토리 경로를 받아서 한번 검사하도록 하고 있다. </span>

<script src="https://gist.github.com/4015494.js"></script>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">아쉽게도 자바에서는 File 클래스가 디렉토리와 파일 모두를 관장한다. 뭔가 디렉토리만을 위한 클래스를 하나 만드는 것도 괜찮은 방법인듯. </span>



