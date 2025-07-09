---
title: '(알고리즘) 버블소트(Bubble Sort)'
author: 'ash84'
pub_date: '2013-07-10'
description: '버블소트라고, 우리나라 말로는 거품정렬이라는 어색한 말인데, 사실은 그냥 자연스러운 정렬방식이다. 알고리즘을 모르는 사람에게 정렬에 대해서 한번 생각해 보라고 하면 나오는게 이 버블소트이다. 내용 자체는 어렵지 않은데, 쉽게 보면 알수 있는 유투브 영상을 투척한다. 한번 동영상으 보고 짜보는 것도 나쁘지 않은듯.'
featured_image: ''
tags: ['algorithm bubble sort', '거품정렬', '버블소트', '알고리즘', '정렬', '정렬 알고리즘']
---


<span style="font-size: 11pt;">버블소트라고, 우리나라 말로는 거품정렬이라는 어색한 말인데, 사실은 그냥 자연스러운 정렬방식이다. 알고리즘을 모르는 사람에게 정렬에 대해서 한번 생각해 보라고 하면 나오는게 이 버블소트이다. 내용 자체는 어렵지 않은데, 쉽게 보면 알수 있는 유투브 영상을 투척한다. 한번 동영상으 보고 짜보는 것도 나쁘지 않은듯. </span>

<span style="font-size: 11pt;">  
</span>

<center>  
<iframe allowfullscreen="" frameborder="0" height="315" src="//www.youtube.com/embed/MtcrEhrt_K0" width="420"></iframe>  
</center><script src="https://gist.github.com/AhnSeongHyun/5958356.js"></script>

<span style="font-size: 11pt;">당연히 연산량은 O(n^2) 이다. 찾아본 바로는 성능이 그리 좋지 않기때문에 많이 화자가 되는 정렬이라고 한다. (오바마 대통령이 구글 에릭슈미트와의 대화에서 언급했다고 함. ㅎㅎ) </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 15px; line-height: 29px;">정렬이 완료되었는지 확인하는 대표적인 방법은 flag 를 이용해서 flag가 0이면 내부 for 문에 진입했더라도 정렬이 다 되어 있는 상태를 의미하기 때문에 빠져나오도록 한 것이다. </span>

<span style="font-size: 15px; line-height: 29px;">  
</span>

<script src="https://gist.github.com/AhnSeongHyun/5958413.js"></script>



