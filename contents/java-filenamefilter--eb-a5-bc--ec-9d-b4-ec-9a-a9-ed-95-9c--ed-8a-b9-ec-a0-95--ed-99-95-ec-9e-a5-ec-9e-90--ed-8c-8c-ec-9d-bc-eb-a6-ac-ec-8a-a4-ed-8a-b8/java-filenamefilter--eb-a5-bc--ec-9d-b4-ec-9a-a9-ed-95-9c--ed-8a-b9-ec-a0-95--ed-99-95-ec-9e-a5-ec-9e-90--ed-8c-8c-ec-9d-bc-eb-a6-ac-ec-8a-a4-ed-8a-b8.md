---
title: '[JAVA] FilenameFilter 를 이용한 특정 확장자 파일리스트 가져오기'
author: 'ash84'
pub_date: '2012-08-23'
description: '파일처리 관련 부분에서 자주 사용되는 부분이 바로 디렉토리에서 파일리스트를 읽어오는 부분이다. 그런데 간혹 원치 않는 파일을 읽어오고 해당 파일에 접근하거나 파싱하는 과정에서 문제가 생길 수가 있다. 때문에 정해진 확장자만 읽어오는 부분이 필요한데, JAVA 에서는 이를 위해서 FilenameFilter 라는 것을 제공한다.'
featured_image: ''
tags: ['dev', 'FilenameFilter', 'Java', '파일 목록가져오기', '파일리스트', '확장자']
---


<span style="font-size: 11pt; ">파일처리 관련 부분에서 자주 사용되는 부분이 바로 디렉토리에서 파일리스트를 읽어오는 부분이다. 그런데 간혹 원치 않는 파일을 읽어오고 해당 파일에 접근하거나 파싱하는 과정에서 문제가 생길 수가 있다. 때문에 정해진 확장자만 읽어오는 부분이 필요한데, JAVA 에서는 이를 위해서 FilenameFilter 라는 것을 제공한다. </span>

<script src="https://gist.github.com/3394292.js"></script>

<span style="font-size: 11pt; ">위의 코드는 java.io 에 있는 File 클래스를 이용해서 디렉토리에 접근하고 listFiles() 라는 함수를 이용해서 해당 디렉토리내 파일의 리스트를 가져올수 있는 코드이다. 일반적으로 디렉토리에서 파일에 관한 정보를 가져오는 코드로 해당 디렉토리내 모든 파일을 가져오는 코드라고 보면된다. </span>

<script src="https://gist.github.com/3394340.js"></script>

<span style="font-size: 11pt; ">위의 코드는 listFiles()의 또 다른 형제(오버로드 함수)를 사용하는 방식을 보여준다. 위의 코드에서는 FilenameFilter 클래스를 재정의한 </span><span style="font-size: 11pt; ">XmlFileFilter의 객체를 인자로 받고 있다. 즉, listFiles(FilenameFilter) 이런 형식이 되는 것인데, 이렇게 지정하면 XmlFileFilter 클래스의 </span><span style="font-size: 11pt; ">재정의(오버라이드)한 함수 accept() 의 결과에 따라서 File[] 형식으로 반환할지가 결정된다. </span>

<script src="https://gist.github.com/3394344.js"></script>

<span style="font-size: 11pt; ">필자는 xml 파일만 걸러내기 위해서 위와 같이 코드를 구성했다. (좀더 간단히도 가능할듯;) 즉, accept() 함수에서 인자로 받고 있는 File dir, String name 을 원하는 대로 검사해서 boolean 형식으로 반환해주면 된다. </span>

<span style="font-size: 11pt; ">딱 정해진 확장자에 대한 정의가 있다면, FilenameFilter 를 재정의해서 사용하는 편이 훨씬 간단할 것으로 예상된다. 예전같았으면, for 문을 돌면서 하나씩 체크를 했어야 했는데 그 부분이 없어지는 것이니까 해당된다면 활용해 보시길</span>



