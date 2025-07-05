---
title: 'xcode without storyboard'
author: 'ash84'
pub_date: '2016-02-15'
description: ''
featured_image: ''
tags: ['dev', 'Xcode', 'storyboard']
---

이상하게도 난 여전히 스토리보드가 쉽지 않다. 코드를 통해서 <code>UIViewController</code> 를 만들어내고 호출하고 이동하는 것들이 자연스러운 구시대 유물인셈. storyboard 없이 프로젝트를 시작하려면 일단 simple view application을 선택하고, <code>AppDelegate.m</code> 에서 아래와 같이 코딩해주면 된다. 

<script src="https://gist.github.com/AhnSeongHyun/80c89e0a1b24dac9b3f5.js"></script>

그리고나서 Info.plist 에 가서 **"Main storyboard file base name", "Launch screen interface file base name"** 항목 부분을 지워주면 된다. 

<center>
<a data-flickr-embed="true"  href="https://www.flickr.com/photos/sh84ahn/24426604613/in/dateposted-public/" title="test"><img src="https://farm2.staticflickr.com/1681/24426604613_74e4ca5896_b.jpg" width="740" height="220" alt="test"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
</center>

그런데 이렇게하고 나면 위의 스샷과 같이 위 아래에 검은 여백(black panel)이 생긴다. 이부분을 해결하기 위해서는 **가짜의 스플래쉬 이미지를 넣어주면 된다.** (어차피 나중에 스플래쉬 이미지 넣을것이기 때문에)

다시 한번 말하지만, 이건 구시대의 유물이다. 
