---
title: '(flask) jinja2 {% include %} 활용'
author: 'ash84'
pub_date: '2013-10-28'
description: '대단한건 아니고, flask 는 기본적으로 jinja2 를 템플릿 언어로 사용하는데 사용하다 보면 하나의 template에서 공통적으로 사용되어 지는 부분이 있다. 예를 들면, 같은 css 나, 자바스크립트를 가져오는 header의 부분이나 상단의 navigation 부분, 하단의 footer 부분이 그러한데 일일히 모든 템플릿에 넣어 주기는 귀찮다. 그래서 jinja2 에서는{%  include %} 를 통해서 하나의 html 에서 다른 html 을 가져올수 있도록 해준다.'
featured_image: ''
tags: ['dev', 'Flask', 'html include', 'ignore missing', 'include', 'jinja2', 'jinja2 template', 'Python']
---
<span style="font-size: 11pt;">대단한건 아니고, flask 는 기본적으로 jinja2 를 템플릿 언어로 사용하는데 사용하다 보면 하나의 template에서 공통적으로 사용되어 지는 부분이 있다. 예를 들면, 같은 css 나, 자바스크립트를 가져오는 header의 부분이나 상단의 navigation 부분, 하단의 footer 부분이 그러한데 일일히 모든 템플릿에 넣어 주기는 귀찮다. 그래서 jinja2 에서는{%  include %} 를 통해서 하나의 html 에서 다른 html 을 가져올수 있도록 해준다. 단순히 가져오는 것이라고 생각할수 있는데 내부적으로는 랜더링된 결과를 리턴한다고 한다. </span>

<script src="https://gist.github.com/AhnSeongHyun/7192217.js"></script>

<span style="font-size: 11pt;">위의 예처럼 nav.html 에서는 status 라는 flask 로 부터 받아온 값으로 Login, Logout 을 보여줄지를 결정하는데(그리 좋은 예제는 아님) nav.html 에서 랜더링 된 html 이 include를 사용한 쪽에 포함되는 것이다. </span>

<span style="font-size: 11pt;">include 문에는** ignore missing 옵션이 있는데 해당 옵션은 말 그대로 없으면 무시해라** 라는 옵션이다. 위의 예에서 만약 nav.html 이 존재하지 않는다면, 호출한 페이지를 브라우저에서 열었을때 에러가 발생되고 flask에서는 nav.html이 없다는 에러 메시지가 출력이 된다. 그렇지만 아래처럼 설정하게 되면 없는 부분을 무시하고 나오게 된다.</span>

<span style="font-size: 11pt;"> </span>

<script src="https://gist.github.com/AhnSeongHyun/7192321.js"></script><span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">또 다른 기능중 하나는** 리스트의 형태로 template 를 지정**할수 있는 것이다. 아래와 같이 지정했을때 1번 라인에 nav.html 이 있으면 nav.html 을 보여주지만 없으면 nav2.html 을 보여준다. nav2.html 이 없으면 에러를 뱉어내고 2번 라인처럼 ignore missing 옵션이 켜져 있으면 둘다 없을때 에러를 뱉어내지 않는다. </span>

<span style="font-size: 11pt;">  
</span><script src="https://gist.github.com/AhnSeongHyun/7192325.js"></script><span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">context 와 관련된 부분은 jinja2  해당 부분을 좀더 읽어 보면 될것 같고, 차후에 import, extends 와의 차이점을 적도록 하겠다. </span>

<span style="font-size: 11pt;">  
</span>



