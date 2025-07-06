---
title: '[Java] List 분배하기, distributeListToSameCapacity()'
author: 'ash84'
pub_date: '2015-07-03'
description: '앞의 포스트에서는 [하나의 리스트에 대해서 n 개의 subList로 분배하는 distributeListToSubList()](http://ash84.tistory.com/874) 함수를 소개했는데, 이번에 소개할 함수는 하나의 리스트를 n개의 동일한 아이템 개수를 가지는 subList로 분배하는 함수이다. 차이점은 distributeListToSubList() 함수는 통제하는 부분이 subList 의 개수인 반면에,  distributeListToSameCapacity() 함'
featured_image: ''
tags: ['dev', 'distributeListToSameCapacity', 'distributeListToSubList', 'Java', '리스트 분배']
---


<span style="font-size: 11pt;">앞의 포스트에서는 [하나의 리스트에 대해서 n 개의 subList로 분배하는 distributeListToSubList()](http://ash84.tistory.com/874) 함수를 소개했는데, 이번에 소개할 함수는 하나의 리스트를 n개의 동일한 아이템 개수를 가지는 subList로 분배하는 함수이다. 차이점은 distributeListToSubList() 함수는 통제하는 부분이 subList 의 개수인 반면에,  distributeListToSameCapacity() 함수는 통제하는 부분이 각 리스트당 아이템의 개수이다. </span>

<span style="font-size: 11pt;">예를 들어, 한 리스트가 10개의 아이템을 가지고 있다고 가정하자. 나는 2개의 아이템을 가지는 리스트들로 분배하고 싶다. 그렇다면 subList는 총 5개가 생길것이다. 만약 3개의 아이템을 가지는 리스트로 분배 한다면 어떻게 될까? 총 4개의 subList가 생기는데, 0, 1, 2번까지의 subList는 3개의 아이템을 가지고 있지만, 마지막 3번의 subList 는 1개의 아이템을 가지고 있을 것이다. </span>

<script src="https://gist.github.com/4357028.js"></script>

<span style="font-size: 11pt;">한 가지, 기존의 리스트에서</span><span style="font-size: 11pt;"> subList() 함수를 이용해서 아이템을 가져올때 new를 함으로써 새로 생성해서 만들어지는 subList에 넣어주었다. 이유는 잘 생각해보시길. </span>

<span style="font-size: 11pt;"></span>



