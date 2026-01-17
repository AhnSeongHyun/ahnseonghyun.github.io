---
title: '[C#] Serial Port 구분하기.'
author: 'ash84'
pub_date: '2009-11-20'
description: '![](http://ash84.net/wp-content/uploads/1/cfile29.uf.1460001B4B0654F75990D2.PNG)

실제 프로그래밍을 하다보면 요즘 컴퓨터는 COM Port 가 없는 경우가 많기 때문에 젠더를 통해서 USB로 연결되고 실제 보드'
featured_image: ''
tags: ['.net', 'C#', 'com port', 'dev', 'ManagementObject', 'ManagementObjectSearcher', 'Serial Port', 'Win32_SerialPort', 'programming']
---
![](http://ash84.net/wp-content/uploads/1/cfile29.uf.1460001B4B0654F75990D2.PNG)

<div style="text-align: justify; line-height: 2; "><span style="font-family: Dotum, gulim, tahoma, sans-serif; font-size: 15px; line-height: 2; ">실제 프로그래밍을 하다보면 요즘 컴퓨터는 COM Port 가 없는 경우가 많기 때문에 젠더를 통해서 USB로 연결되고 실제 보드나 기기는 UART로 연결이 되면서 제어판에서는 통신포트로 잡힌다. 하지만, 다수의 젠더를 사용해서 기기를 연결하는 경우, 컴퓨터는 포트번호를 통해서만 구분할 뿐이다. 때문에 Application에서 만약 포트번호가 바뀌어져 버린다면 기기를 연결할 수가 없다. </span></div><span style="font-size: 11pt; "><span style="font-family: Dotum; ">  
 그렇기 때문에 꽂혀져 있는 포트중 내가 사용해야 하는 포트를 구별해야할 필요가 있다. </span></span>

**<span style="font-size: 11pt; "><span style="font-family: Dotum; ">네임스페이스 추가 : using System.Management;</span></span>**<span style="font-size: 11pt; "><span style="font-family: Dotum; "></span></span>

<script src="https://gist.github.com/3781069.js"></script>



