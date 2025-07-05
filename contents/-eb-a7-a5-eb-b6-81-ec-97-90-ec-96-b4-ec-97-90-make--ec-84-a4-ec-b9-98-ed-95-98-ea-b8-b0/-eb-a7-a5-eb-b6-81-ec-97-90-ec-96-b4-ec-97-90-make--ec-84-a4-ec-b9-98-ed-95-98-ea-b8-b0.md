---
title: '맥북에어에 make 설치하기.'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['command line tools', 'dev', 'Make', 'make mac osx', 'Xcode', '맥에서 make']
---


<span style="font-size: 11pt; ">최근에 오픈소스들을 다운 받아서 설치하고 있는데 그중에서 in-memory DB인 redis 를 맥북에어에 설치하려고 시도중에 make가 새로산 맥북에어에 없어서 redis 를 빌드하지를 못했었다. 그래서 mac  계열에서는 도데체 어떻게 make를 설치해야 하는지에 대해서 찾아보던중 쉽게 할수 있는 방법을 찾았다. Step by Step 으로 알려드리겠다. </span>

![](http://ash84.net/wp-content/uploads/1/cfile25.uf.1665B93450325481312F0D.jpg)

<table border="0" cellpadding="0" cellspacing="0" class="txc-table" style="border:none;border-collapse:collapse;;font-family:돋움;font-size:12px" width="604"><tbody><tr><td style="width:604;height:24;border-bottom:1px solid #ccc;border-right:1px solid #ccc;border-top:1px solid #ccc;border-left:1px solid #ccc;;"><span style="font-size: 10pt; line-height: 2; text-align: justify; ">  1. 맥북에어에 xcode 설치하기 </span>

<span style="font-size: 10pt; ">  2. xcode -> preference -> d</span><span style="font-size: 10pt; ">ownloads -> component 에서 command line tools 를 인스톨 시킨다. </span>

</td></tr></tbody></table><span style="font-size: 11pt; ">이렇게 하게 되면 본인 맥북에어에 make 가 설치가 된다. 보기보다 매우 쉽다. 그런데 xcode 를 설치해야 하는 번거로움이 남아 있을수 있는데, 그런 부분을 보완하기 위해서 아래의 링크를 보면 애플에서 xcode 에서 Command Line Tools 를 따로 패키지를 만들어 배포한다고 한다. 관심있는 부분은 보시길(필자는 아직 써보질 못했다.)</span>

<span style="color: rgb(129, 129, 127); font-family: 돋움, dotum, Tahoma, AppleGothic, sans-serif; letter-spacing: -1px; line-height: 19px; ">[<span style="font-size: 11pt; ">Command Line Tools for XCode</span>](http://jeen.tistory.com/entry/Mac-XCode-no-gcc-yes-Command-Line-Tools-for-XCode)</span>

<span style="font-size: 11pt; ">다음 시간에는 macport 와 redis를 macport 를 이용해서 설치하는 법을 알아보자. </span>



