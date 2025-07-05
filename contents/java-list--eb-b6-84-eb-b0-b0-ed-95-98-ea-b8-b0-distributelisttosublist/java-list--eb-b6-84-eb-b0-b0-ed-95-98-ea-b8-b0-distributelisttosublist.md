---
title: '[Java] List 분배하기, distributeListToSubList()'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['ArrayList', 'dev', 'Distribute list', 'Java', '리스트 분배', '리스트 분할']
---


<span style="font-size: 11pt;">개인적으로 필요할것 같은데 하는 라이브러리를 만드는 작업을 하고 있는데 이름은 espressoOtr 이라고 지었다. (github에 아직은 미공개상태.) 뭐 이름은 내 마음대로니까 거두절미하고, 짜잘한 라이브러리가 있지만, 최근에 만든것을 하나 공개하려고 한다. 대단한건 절대 아니고, 누군가 이미 만들어 쓰고 있을지도 모르지만. </span>

<span style="font-size: 11pt;">하나의 리스트를 n 개의 리스트로 분할하는 함수이다. distributeListToSubList() 함수인데, 한 개의 리스트에 10개의 아이템이 있다고 가정하자. 그러면 나는 이 리스트를 3개의 다른 리스트로 배분하고 싶다. 반드시 3개여야만 한다. 그러면  0번 리스트에는 4개, 1번 리스트에는 4개, 2번 리스트에는 2개가 들어가면 된다. 그런 작업을 해주는 함수이다. </span>

<span style="font-size: 11pt;">  
</span>

<script src="https://gist.github.com/4356976.js"></script>

<span style="font-size: 11pt;line-height:2;text-align:justify;">인자로는 List와 분배하려는 개수를 받는다. 리턴값은 Hashmap<Integer, List>를 반환하도록 하였다. Hashmap의 size()를 가져와서 키로 각각의 분배된 리스트를 가져올 수 있다. Generic을 쓰지 않은 이유는 모든 List에 대해서 수행가능하도록 만들기 위해서이다. </span>



