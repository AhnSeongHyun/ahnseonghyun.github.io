---
title: '(redis) start.sh, stop.sh, cli.sh'
author: 'ash84'
pub_date: '2013-04-19'
description: ''
featured_image: ''
tags: ['redis', 'start.sh', 'stop.sh', '명령어']
---


<span style="font-size: 11pt;">별거 없는데 redis 를 회사에서 서버로 쓰려니까 일일히 명령어 쓰기도 귀찮고 스케쥴 걸거나 그렬려면 또 쉘 스크립트화 해두는게 편해서, start.sh, stop.sh, cli.sh 만들었다. 그냥 복사해서 쓰시면 될듯.</span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 15px; line-height: 22px;">**<span style="font-size: 11pt;">start.sh</span>**</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; line-height: 2;"><span style="color: rgb(0, 0, 0); line-height: 16px; white-space: pre; font-size: 11pt;">/ash84/redis-2.6.9/src/redis-server /ash84/redis-2.6.9/conf/redis.conf</span>

</div><span style="font-size: 15px; line-height: 22px;">  
</span>

<span style="font-size: 15px; line-height: 22px;">**<span style="font-size: 11pt;">stop.sh</span>**</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; line-height: 2;"><span style="font-size: 11pt; line-height: 22px;">/ash84/redis-2.6.9/src/redis-cli shutdown</span>

</div><span style="font-size: 15px; line-height: 22px;">  
</span>

<span style="font-size: 15px; line-height: 22px;">**<span style="font-size: 11pt;">cli.sh</span>**</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; line-height: 2;"><span style="font-size: 15px; line-height: 22px;">****</span><span style="font-size: 11pt; line-height: 22px;">/ash84/redis-2.6.9/src/redis-cli</span>

</div><span style="font-size: 11pt;">별거 없지만 한가지 주의사항은 되도록 절대경로를 쓰는게 좋다는 것이다. 단독으로 쉘에서 실행할때는 상관없는데 프로그래밍을 하다보면 쉘 자체를 내가 만든 프로그램에서 exec 로 호출하거나 하는 경우가 빈번하다. 그럴경우 상대경로로 잡혀있으면 redis를 실행하거나 할수가 없다. </span>



