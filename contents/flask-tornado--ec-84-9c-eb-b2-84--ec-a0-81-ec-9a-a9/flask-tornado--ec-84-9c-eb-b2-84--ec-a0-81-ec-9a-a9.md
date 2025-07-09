---
title: '(flask) tornado 서버 적용'
author: 'ash84'
pub_date: '2013-10-23'
description: '다들 아시겠지만 flask 내장 서버는 구리고, 사실 어쩔때는1번 이후에 접속이 안될때도 많다. 그래서 flask 문서에서도 배포에서는 사용하지 말라고 권장하고 있기 때문에 tornado 서버를 붙일수가 있다. 여타의 다른 서버를 붙일수가 있는데 링크를 확인하면 된다. 
일단 tornado를 설치하는 법은 아래와 같다. 당연 pip.'
featured_image: ''
tags: ['dev', 'FLASK', 'flask 웹서버', 'Python', 'Tornado']
---


<span style="font-size: 11pt;">다들 아시겠지만 flask 내장 서버는 구리고, 사실 어쩔때는1번 이후에 접속이 안될때도 많다. 그래서 flask 문서에서도 배포에서는 사용하지 말라고 권장하고 있기 때문에 tornado 서버를 붙일수가 있다. 여타의 다른 서버를 붙일수가 있는데 링크를 확인하면 된다. </span>

<span style="font-size: 11pt;">일단 tornado를 설치하는 법은 아래와 같다. 당연 pip.</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; line-height: 2;"><span style="font-size: 11pt;">pip install tornado</span>

</div><span style="font-size: 11pt;">그리고 나서 아래와 같이 tornado를 이용해서 구동하기 위한 import 작업을 해준다. </span>

<span style="font-size: 11pt;">  
</span>

<script src="https://gist.github.com/AhnSeongHyun/7114747.js"></script><span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">기존의 flask의 main 부분에서 기존의 app.run()을 통해서 실행 시켰던 부분을 아래의 코드로 바꿔주면 된다. </span>

<span style="font-size: 11pt;">  
</span><script src="https://gist.github.com/AhnSeongHyun/7114754.js"></script><span style="font-size: 11pt;">  
</span>



