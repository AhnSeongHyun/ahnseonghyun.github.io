---
title: '(maven) jar-dependency 복사하기'
author: 'ash84'
pub_date: '2013-06-26'
description: '필자의 경우 자바 서버쪽에서 java -jar 로 만든 jar 파일을 만드는 경우가 있는데 그때에 maven 으로 연동한 라이브러리들을 모두 가지고 있어야 제대로 구동이 된다. 때문에 pom.xml 에 다음의 부분을 추가해서 jar 를 만들고 target/lib 에 연동된 라이브러리들을 배치(복사) 하도록 해야 한다.'
featured_image: ''
tags: ['dev', 'JAR', 'Java', 'maven', 'maven jar-dependency', '라이브러리 복사하기']
---
<span style="font-size: 11pt;">필자의 경우 자바 서버쪽에서 java -jar 로 만든 jar 파일을 만드는 경우가 있는데 그때에 maven 으로 연동한 라이브러리들을 모두 가지고 있어야 제대로 구동이 된다. 때문에 pom.xml 에 다음의 부분을 추가해서 jar 를 만들고 target/lib 에 연동된 라이브러리들을 배치(복사) 하도록 해야 한다</span>. 

<script src="https://gist.github.com/AhnSeongHyun/5872759.js"></script>

<span style="font-size: 11pt;">이렇게 하고 나면 target 에 jar파일과 함께 lib 폴더가 생기게 된다. 파일과 lib 폴더를 서버에 복사해서 java -jar 로 실행하면 제대로 실행이 되는 것을 확인 할 수가 있다. </span>



