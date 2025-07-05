---
title: '[Python] 한자 한글 변환 파이썬 소스'
author: 'ash84'
pub_date: '2017-03-28'
description: ''
featured_image: ''
tags: ['dev', 'Python', '파이썬', '한글변환', '한자', '한자변환']
---


<span style="font-size: 11pt; ">한자어가 섞인 글 안에서 한자어를 한글로 교체해서 반환하도록 하는 프로그램이다. 원래는 C로 작성된 모듈을 봤었는데 너무 복잡스럽게 되어있는 문제가 있어서, 좀더 쉽게 할수 있는 방법이 없을까 찾다가 파이썬(Python)으로 짜 보았는데 훨씬 간결하다. 부가적으로 qsort() 와 이진탐색을 사용한다면 좀더 빠르게도 가능하지 않을까 싶다. </span>

<span style="font-size: 11pt; ">실행방식은 다음과 같다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; "><span style="font-size: 11pt; ">>python  htok.py ./hanja-dict.txt input.txt </span>

</div><span style="font-size: 11pt; ">입력한 한자 사전과 입력데이터가 있는 텍스트를 인자로 주면 된다. 인자값이나 인자수를 체크하는 부분은 귀찮아서 개발하지 않았다. 필요한 분들이 각자 알아서 넣으시길. 코드를 보면 알겠지만, hnj-dict는 ‘한자:한글’의 형식으로 입력하면 된다. 다른 형식으로 바꾼다면, 처음에 사전을 읽어오는 부분을 수정하면 될 것이다.  </span>

<script src="https://gist.github.com/3804481.js"></script>



