---
title: '(iOS) UIAlertView 초 간단 정리'
author: 'ash84'
pub_date: '2013-01-22'
description: '위와 같이 쓰면된다. title에는 어떤 경고를 줄것인지 쓰면 되고, message에는 상세한 경고 문구를 써 주면 된다. cancelButtonTitle'
featured_image: ''
tags: ['dev', 'ios dev', 'UIActivityIndicatorView', 'UIAlterView']
---


<script src="https://gist.github.com/4598514.js"></script>

<span style="color: rgb(0, 0, 0);"><span style="font-size: 11pt;">위와 같이 쓰면된다. title에는 어떤 경고를 줄것인지 쓰면 되고, message에는 상세한 경고 문구를 써 주면 된다. </span></span><span style="color: rgb(0, 0, 0);   line-height: 2;   font-size: 11pt;">cancelButtonTitle 부분은 왼쪽 버튼 부분에 해당하는 텍스트를 입력하면 된다. 만약 버튼이 하나라면 </span><span class="nl" style="font-size: 11pt; color: rgb(0, 0, 0); line-height: 2;  ">otherButtonTitles:</span><span class="nb" style="font-size: 11pt; color: rgb(0, 0, 0);  line-height: 2; ">nil</span><span class="nb" style="font-size: 9pt;   line-height: 2; "><font color="#000000"><span style="color: rgb(0, 0, 0); font-size: 11pt;"> 이렇게 주자. </span></font></span><span class="nl" style="font-size: 11pt; color: rgb(0, 0, 0);   line-height: 2;  ">otherButtonTitles:</span><span class="nl" style="font-size: 9pt;   line-height: 2;  "><font color="#0086b3"><span style="color: rgb(0, 0, 0); font-size: 11pt;">@”” 이런식으로 처리할 경우 버튼이 2개 나오는데 텍스트가 없기 때문에 빈 버튼만 나오기 때문에 유의하자. </span></font></span>

<span class="nl" style="font-size: 9pt;  line-height: 2;"><font color="#0086b3">  
</font></span>

<font color="#0086b3"><span style="line-height: 2;  color: rgb(0, 0, 0);"><span style="font-size: 11pt;">UIAlterView+UIActivityIndicator를 사용하시는 분들이 계신데, 요즘에는 오픈소스도 많기 때문에 제대로 된 것을 찾아보기를 권장하는 바이뎌, 사용자들의 수준이 너무 올라갔기 때문에 이쁜것을 찾아서 붙여주는 편이 좋다. </span></span></font>

<font color="#0086b3"><span style="line-height: 2;  color: rgb(0, 0, 0);"><span style="font-size: 11pt;">  
</span></span></font>

<font color="#0086b3" style="line-height: 2;"><span style="line-height: 2;  color: rgb(0, 0, 0);"><span style="font-size: 11pt;">개인적으로 </span></span></font><font color="#000000"><span style="font-size: 15px; line-height: 29px;">[https://github.com/samvermette/SVProgressHUD](https://github.com/samvermette/SVProgressHUD) 를 추천하는 바이다. </span></font>

<center>  
![](https://a248.e.akamai.net/camo.github.com/89b9752b23efb8448be214ba32bee0aee8004dbd/687474703a2f2f662e636c2e6c792f6974656d732f3372327830623145314f324630563432326133522f73637265656e73686f7473322e706e67)  
</center>

