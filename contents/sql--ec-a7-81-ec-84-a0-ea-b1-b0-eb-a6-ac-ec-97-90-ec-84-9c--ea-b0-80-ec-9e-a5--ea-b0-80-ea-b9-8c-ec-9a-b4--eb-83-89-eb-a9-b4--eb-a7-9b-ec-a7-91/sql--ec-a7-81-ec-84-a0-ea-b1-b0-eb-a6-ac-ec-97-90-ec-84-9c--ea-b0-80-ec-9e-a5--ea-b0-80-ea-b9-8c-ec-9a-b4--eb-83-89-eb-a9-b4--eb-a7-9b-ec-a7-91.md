---
title: '(SQL) 직선거리에서 가장 가까운 냉면 맛집'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['dev', 'SQL', '위도 경도 직선거리', '직선거리']
---


<span style="font-size: 11pt;">인터넷 매쉬업을 참가했는데 현재위치에서 가장 가까운 어떤 맛집을 찾으려면 어떻게 해야할까? 고민해 보다가 찾아보니 직선거리 말고 지구는 둥그니까 다른 계산법이 있는 것으로 확인되긴 하였다. 그러나 나는 직선거리 방식을 사용했다.(더차피 지구는 완전히 둥글진 않으니까) 아래의 코드를 보면 쉽게 이해가 될듯. </span>

<script src="https://gist.github.com/AhnSeongHyun/6408627.js"></script>

<span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;"></span><span style="font-size: 11pt;"></span><span style="font-size: 11pt;">냉면이라는 맛집을 like 검색을 통해서 찾아내고 그 찾아낸 맛집들 중에서 현재 주어진 위치와 가장 가까운 순으로 찾아서 10개만 보여주는 쿼리이다. mongoDB나 그런것을 사용하면 좀더 편하게 찾을수 있다고 하는데, 좀더 알아 봐야 겠다.</span><span style="font-size: 11pt;"></span>



