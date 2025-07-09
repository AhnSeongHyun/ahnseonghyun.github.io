---
title: '[MFC] Draw PNG'
author: 'ash84'
pub_date: '2011-05-31'
description: ''
featured_image: ''
tags: ['dev', 'draw png', 'mfc', 'png', 'png mfc', '리소스', '비트맵']
---


<div><div style="line-height: 2; text-align: justify; "><span style="font-size: 10pt; "><span style="font-family: Dotum; "><div><div style="line-height: 2; "><div class="txc-textbox" style="border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-top-color: rgb(203, 203, 203); border-right-color: rgb(203, 203, 203); border-bottom-color: rgb(203, 203, 203); border-left-color: rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; "><span style="font-size: 11pt; ">매일매일 개발하는 소스코드를 올리고 있습니다. 원래는 프로젝트가 끝나고 올리려고 했으나, 그러다 보니 까먹는 경우가 있어서 이렇게 매일매일 올리는 소스코드 입니다. 제가 쓴 소스코드의 문제 혹은 개선점이 있으면 언제든지 댓글 달아 주세요 </span>

<span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; ">  
 PNG를 쓰는 이유는 단 하나다. 배경의 투명처리 때문. 하지만 DC로 그릴경우에는 MFC의 리소스에 등록해서 그러야 하는 불편함이 있고, PNG 리소스 등록도 번거롭다. 가장 큰 문제는 리소스를 많이 쓰면 팀 작업간의 SVN Conflict가 자주 날수 있기에. 아래와 같이 png의 경우 파일로 보여주는 것도 나쁘지 않다. </span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
 The reason of using PNG image file is one. becauseof Transparent. But you draw any grpahic using DC, you have to register Resource of MFC. It is very inconvenient. The important problem of using resource is that you may experience SVN Confilict in team works. so it is not bad that load png file:</span> 

</span></span></div></div><script src="https://gist.github.com/3263943.js"></script>



