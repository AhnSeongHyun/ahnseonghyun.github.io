---
title: '(sql) Distinct 중복제거'
author: 'ash84'
pub_date: '2015-09-24'
description: ''
featured_image: ''
tags: ['dev', 'DISTINCT', 'MySQL', 'SQL', 'sql distinct', '중복제거']
---


<span style="font-size: 11pt;">SQL 쪽 공부를 최근에 벼락치기로 했는데, Distinct 에 대해서 약간의 이해가 안되서 정리할겸 올린다. 용어를 찾아보면 중복제거라고 하는데, 말 그대로다. 반대로 all 이라는 것이 있는데 이건 select 문에서 아무것도 지정하지 않아도 되는 것이다. </span>

<span style="font-size: 11pt;">예를 들어, 아래의 sql의 실행했다고 가정해 보자. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; text-align: justify; line-height: 2;"><span style="font-size: 11pt;">select age, name</span>

<span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;"></span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">from test</span>

</div><table align="justify" border="0" cellpadding="0" cellspacing="0" class="txc-table" style="border: none; border-collapse: collapse; font-family: 돋움; font-size: 12px; width: 638px;" width="638"><tbody><tr><td style="width: 301px; height: 24px; border: 1px solid rgb(204, 204, 204);"><span style="font-size: 10pt;"> age</span>

</td><td style="width: 337px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-top-width: 1px; border-top-style: solid; border-top-color: rgb(204, 204, 204);"><span style="font-size: 10pt;">name </span>

</td></tr><tr><td style="width: 301px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> 1</span>

</td><td style="width: 337px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 10pt;">ash84 </span>

</td></tr><tr><td style="width: 301px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> 1</span>

</td><td style="width: 337px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 10pt;">ash84 </span>

</td></tr><tr><td style="width: 301px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> 10</span>

</td><td style="width: 337px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 10pt;">tom </span>

</td></tr><tr><td style="width: 301px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> 10 </span>

</td><td style="width: 337px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size:10pt;">tom</span>

</td></tr></tbody></table><span style="font-size: 11pt;">중복이 된 결과가 나올수 있다. 이런 경우에 만약 중복을 제거 하고 싶다면, </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; text-align: justify; line-height: 2;"><span style="font-size: 11pt;">select distinct age, name</span>

<span style="font-size: 11pt;">from test</span>

</div><table border="0" cellpadding="0" cellspacing="0" class="txc-table" style="border: none; border-collapse: collapse; font-size: 12px; width: 637px;" width="637"><tbody><tr><td style="width: 300px; height: 24px; border: 1px solid rgb(204, 204, 204);"><span style="font-size: 10pt;"> age</span>

</td><td style="width: 336px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-top-width: 1px; border-top-style: solid; border-top-color: rgb(204, 204, 204);"><span style="font-size: 10pt;">name </span>

</td></tr><tr><td style="width: 300px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> 1</span>

</td><td style="width: 336px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 10pt;">ash84 </span>

</td></tr><tr><td style="width: 300px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> 10 </span>

</td><td style="width: 336px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size:10pt;">tom</span>

</td></tr></tbody></table><span style="font-size: 11pt;line-height:2">이렇게 실행이 되게 된다. 중복을 제거한다는 면에서 편한 키워드라고 생각 될수 있지만 주의할점이 있는데 select 문에서 가져오려는 컬럼 하나에 대해서 수행되지 않는다. 예를 들어, 아래와 같이 데이터가 있다고 하자. </span>

<table border="0" cellpadding="0" cellspacing="0" class="txc-table" style="border: none; border-collapse: collapse; font-size: 12px; width: 637px;" width="637"><tbody><tr><td style="width: 300px; height: 24px; border: 1px solid rgb(204, 204, 204);"><span style="font-size: 10pt;"> age</span>

</td><td style="width: 336px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-top-width: 1px; border-top-style: solid; border-top-color: rgb(204, 204, 204);"><span style="font-size: 10pt;">name </span>

</td></tr><tr><td style="width: 300px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> 1</span>

</td><td style="width: 336px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 10pt;">ash84 </span>

</td></tr><tr><td style="width: 300px; height: 37px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> 10 </span>

</td><td style="width: 336px; height: 37px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 10pt;">tom</span>

</td></tr><tr><td rowspan="1" style="width: 300px; height: 37px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> 10  </span></td><td rowspan="1" style="width: 336px; height: 37px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size:10pt;">tim </span>

</td></tr></tbody></table><span style="font-size: 11pt;line-height:2">이런식으로 있다고 해서 10 이라는 값이 중복인데 distinct 로 제거할 수는 없다. 이 부분에 대해서는 서브쿼리를 사용한다든지 하는 다른 해결방법을 찾는것이 좋을것 같다. </span>



