---
title: '(PHP) WKLogger(Wrap KLogger) 로 로그 남기기'
author: 'ash84'
pub_date: '2015-07-03'
description: 'php 로거를 찾고 싶었다. 기존 개발자가 response 를 보내야할 페이지에 로그를 출력하는 만행(?) 을 저질르고 있었고 일단 해야하는 작업(지금도 하고 있는 작업)은 파일 로거를 도입하는것이었다. 당연히 내가 구현하는것 보다는 있는것을 쓰는게 편한데 찾아보니 [KLogger](https://github.com/katzgrau/KLogger) 라는것이 있었다. 사실 지금 생각해 보면 좀더 찾아볼껄 하는 생각이 들었는데 쓰는 방식이 log4j 와 흡사해서 채택하게 되었다.'
featured_image: ''
tags: ['dev', 'KLogger', 'Logger', 'php', 'WKLogger']
---


<span style="font-size: 11pt;">php 로거를 찾고 싶었다. 기존 개발자가 response 를 보내야할 페이지에 로그를 출력하는 만행(?) 을 저질르고 있었고 일단 해야하는 작업(지금도 하고 있는 작업)은 파일 로거를 도입하는것이었다. 당연히 내가 구현하는것 보다는 있는것을 쓰는게 편한데 찾아보니 [KLogger](https://github.com/katzgrau/KLogger) 라는것이 있었다. 사실 지금 생각해 보면 좀더 찾아볼껄 하는 생각이 들었는데 쓰는 방식이 log4j 와 흡사해서 채택하게 되었다. </span>

문제는 [KLogger](https://github.com/katzgrau/KLogger)가 생성할때 마다 파일을 만들어 내는 구조라는 점. 

<div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">기본적인 로거가 가지고 있는 daily 별로 끊어주는 것이 없다는 점이 짜증이 나서 만들어서 풀리케를 보내볼까 생각했지만. 그닥. issue 쪽을 가보니 받아주지 않는것 같다. </span>

[WKLogger](https://github.com/AhnSeongHyun/WKLogger) [(Wrap KLogger)](https://github.com/AhnSeongHyun/WKLogger) 라고 해서 하나 감싼건데 간단하게 말하자면 [KLogger](https://github.com/katzgrau/KLogger)는 클래스로 객체를 생성하는 생성자에서 파일을 만드는 역할을 한다. 그래서 [WKLogger](https://github.com/AhnSeongHyun/WKLogger) 는 클래스가 아니라 각 로그레벨별 함수를 제공하고 그 함수에서는 [KLogger](https://github.com/katzgrau/KLogger)를 생성해서 로그를 남기도록 하는데 로그 파일의 이름을 daily 로 가져오도록 하였다. 그렇게 되면 [KLogger](https://github.com/katzgrau/KLogger) 에서는 같은 파일이름에 대해서는 열어서 추가(append)하기 때문에 일자별 로그로 남게 된다. 

<script src="https://gist.github.com/AhnSeongHyun/7820283.js"></script>

</div>

