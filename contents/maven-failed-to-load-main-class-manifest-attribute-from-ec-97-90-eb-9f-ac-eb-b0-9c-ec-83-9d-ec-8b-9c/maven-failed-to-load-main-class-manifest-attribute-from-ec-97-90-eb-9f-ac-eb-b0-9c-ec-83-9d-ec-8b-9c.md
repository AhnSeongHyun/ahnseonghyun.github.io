---
title: 'maven Failed to load Main-Class manifest attribute from..에러발생시.'
author: 'ash84'
pub_date: '2013-01-04'
description: 'java -jar lib.jar 이런식으로 jar를 직접실행하는 경우가 있다. 이런 경우 maven의 pom.xml에 main class를 지정해 주지 않으면 실행할 경우, 다음과 같은 에러가 발생 할 수 있다.'
featured_image: ''
tags: ['dev', 'java', 'main class error', 'main class nor found', 'maven']
---
<span style="font-size: 11pt;">java -jar lib.jar 이런식으로 jar를 직접실행하는 경우가 있다. 이런 경우 maven의 pom.xml에 main class를 지정해 주지 않으면 실행할 경우, 다음과 같은 에러가 발생 할 수 있다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">Failed to load Main-Class manifest attribute from..</span>

</div><span style="font-size: 11pt;">즉, 자바에서 main() 함수가 있는 클래스를 찾지 못하고 있다는 애기인데.. 이를 위해서는 아래와 같이 maven-jar-plugin을 통해서 <mainClass>를 지정해주어야 한다. classPath 를 지정해주는 편이 좋지만, jre/lib/ext 에 모든 참조 라이브러리들을 모아서 쓰는 분이라면 굳이 주석처리된 부분은 해제할 필요는 없다. </span>

<span style="font-size: 11pt;">  
<script src="https://gist.github.com/4442115.js"></script>  
</span>

<span style="font-size: 11pt;">maven을 사용하면서 느낀점중 하나는 굉장히 많은 설정이 있고, 많이 써봐야 한다는 것이다. 프로젝트의 성격에 따라 조금씩 달라질때 마다 정리해 둘 필요가 있는것 같다. </span>



