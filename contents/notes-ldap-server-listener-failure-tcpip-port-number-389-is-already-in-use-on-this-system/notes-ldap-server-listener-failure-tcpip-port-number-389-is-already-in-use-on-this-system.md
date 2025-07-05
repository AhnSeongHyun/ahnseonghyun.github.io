---
title: '(Notes) LDAP Server: Listener failure, TCP/IP port number [389] is already in use on this system'
author: 'ash84'
pub_date: '2012-12-27'
description: ''
featured_image: ''
tags: ['LDAP', 'notes']
---


<span style="font-size: 11pt; line-height: 2;">Domino/Notes 서버를 윈도우 2008 서버에 설치한 이후 가동시켰을때, 아래와 같은 에러가 발생한다. 에러인 즉, 이미 서버에서 389번 포트를 사용하고 있어서 Domino의 LDAP 서버에서 389번 포트를 사용 할 수 없다는 애기다.</span>

<span style="font-size: 11pt;"> </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">LDAP Server: Listener failure, TCP/IP port number [389] is already in use on this system</span>

</div><span style="font-size: 11pt;">notes.ini를 바꾼다고 해결될 내용은 아니고, 본 </span>[<span style="font-size: 11pt;">링크</span>](http://zatz.com/dominopower/article/what-to-do-when-your-ldap-ports-already-in-use/)<span style="font-size: 11pt;">에 가보면 domino admin을 통해서 변경하는 방법을 알려주고 있다. 그러나 필자의 경험상 domino admin에 익숙하지 않은 사람이라면 윈도우 서버의 AD(Active Directory)를 중지시키는 것이 하나의 방법인것 같다. 왜냐하면 389 번 포트를 AD에서 사용하고 있기 때문에 발생하는 문제이기 때문이다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 15px; line-height: 29px;">ps) 도메인에 대한 부분은 잘 확인해 보길 바란다. 자칫, 원격접속이 안되서 IDC로 가야하는 불상사가 생길수 있으니 말이다. </span>



