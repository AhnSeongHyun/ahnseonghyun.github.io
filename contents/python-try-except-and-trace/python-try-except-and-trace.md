---
title: '(python) try ~ except and trace'
author: 'ash84'
pub_date: '2015-07-03'
description: '이상하게 파이썬을 빨리 빨리 뚝딱 만드는 언어로 많이 쓰는데(사실 나도 그렇게 쓴다.) 그런데 간호 pypi 에 올려서 욕을 안먹으려면 예외 처리를 해야한다. 당연한 애긴데. ㅎㅎ 아무튼 위의 소스코드를 보면 try: ~ except: 문으로 묶는 것이 기본이다. catch 에 해당하는 것이 except 라고 보면 되는데, Java 처럼 자세히 나'
featured_image: ''
tags: ['dev', 'Python', 'traceback', 'try except', '예외처리', '파이썬']
---


<script src="https://gist.github.com/AhnSeongHyun/7210750.js"></script>

<span style="font-size: 11pt;">이상하게 파이썬을 빨리 빨리 뚝딱 만드는 언어로 많이 쓰는데(사실 나도 그렇게 쓴다.) 그런데 간호 pypi 에 올려서 욕을 안먹으려면 예외 처리를 해야한다. 당연한 애긴데. ㅎㅎ 아무튼 위의 소스코드를 보면 try: ~ except: 문으로 묶는 것이 기본이다. catch 에 해당하는 것이 except 라고 보면 되는데, Java 처럼 자세히 나오지 않기 때문에 traceback 을 추가해줘야 한다. </span><span style="background-color: transparent; font-size: 11pt; line-height: 2;">sys.stdout 을 지정해서 표준출력으로 예외가 발생한 부분을 트레이스 하고 있는데 테스트 해보면 해당 부분 라인이나 정보를 볼 수 있다. 아래와 같이 나온다. </span>

<span style="font-size: 11pt;">  
</span>  
<script src="https://gist.github.com/AhnSeongHyun/7210779.js"></script>



