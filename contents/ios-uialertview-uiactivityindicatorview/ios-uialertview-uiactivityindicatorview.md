---
title: '[iOS] UIAlertView + UIActivityIndicatorView'
author: 'ash84'
pub_date: '2011-05-06'
description: ''
featured_image: ''
tags: ['dev', 'IOS', 'UIActivityIndicatorView', 'UIAlertView', '로딩뷰']
---


<meta content="text/html; charset=UTF-8" http-equiv="Content-Type"></meta>  
<meta content="text/css" http-equiv="Content-Style-Type"></meta>

<title></title>  
<meta content="Cocoa HTML Writer" name="Generator"></meta>  
<meta content="1038.35" name="CocoaVersion"></meta><style type="text/css">
p.p1 {margin: 0.0px 0.0px 0.0px 0.0px; font: 11.0px Menlo; min-height: 13.0px}
p.p2 {margin: 0.0px 0.0px 0.0px 0.0px; font: 11.0px Menlo; color: #d12c26}
p.p3 {margin: 0.0px 0.0px 0.0px 0.0px; font: 11.0px Menlo; color: #713ea3}
p.p4 {margin: 0.0px 0.0px 0.0px 0.0px; font: 11.0px Menlo; color: #3e1f7c}
p.p5 {margin: 0.0px 0.0px 0.0px 0.0px; font: 11.0px Menlo}
span.s1 {color: #000000}
span.s2 {color: #713ea3}
span.s3 {color: #4e8186}
span.s4 {color: #3e1f7c}
span.s5 {color: #bb2d9d}
span.s6 {color: #2c2ecf}
span.Apple-tab-span {white-space:pre}
</style><span style="font-family: Dotum; font-size: 10pt; color: rgb(0, 0, 0); line-height: 2; text-align: justify; "><span style="font-size: 11pt; "></span><span style="font-size: 11pt; ">한우찾기 앱을 만들면서 사실 자바스크립트를 통해서 데이터를 긁어오는 과정을 시간을 측정해 보니, Wi-Fi 사용시에는 사용자가 느리다고 느끼지는 않지만, 3G를 사용할때는 그렇지가 않더라구요. 그래서 로딩뷰를 하나 구성하게 되었습니다. 이미 앞선</span></span>[<span style="font-size: 11pt; "> <로딩뷰 관련 포스팅> </span>](http://ash84.tistory.com/680 "[http://ash84.tistory.com/680]로 이동합니다.")<span style="font-family: Dotum; font-size: 11pt; color: rgb(0, 0, 0); line-height: 2; text-align: justify; ">에서 말했던 것 처럼, 원래는 echofon 형태의 로딩 스타일을 쓰다가 별루 이쁘지 않아서 바꾸게 되었는데요. 그게 바로 UIAlertview 에 UIActivityIndicatorView 붙여서 쓰는 것인데요. 아래의 사진처럼 나오게 됩니다. </span>

<span style="font-size: 11pt; ">  
</span><font color="#000000"><span style="font-size: 11pt; ">  
</span></font>

<div style="text-align: justify; "></div><figure class="wp-caption aligncenter" style="width: 320px">![](http://ash84.net/wp-content/uploads/1/cfile1.uf.207F183D4DC3D3921C857A.PNG)<figcaption class="wp-caption-text">요런 느낌?</figcaption></figure>

 

<script src="https://gist.github.com/3353947.js"></script>

<span class="s1">  
<span style="line-height: 2; font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">처음 위의 [alert Show] 하는 부분에 것은 어떤 작업이 시작할때, 그리고 alert 내리는 부분은 어떤 작업이 끝날 때 호출하면 됩니다. 좀더 커스터 마이징 해서 쓸수 도 있을것 같네요^^ </span></span></span>



