---
title: '[Java] 간단 gson wrapping 하기'
author: 'ash84'
pub_date: '2013-01-11'
description: '여러가지 라이브러리가 있겠지만 단연 json 라이브러리 중에 내가 가장 잘 쓰는 것은 [gson ](http://ash84.tistory.com/775)이다. 쓰기 편해서 일수도 있지만, 함수이름이나 그런것들이 잘 지어져있어서 직관적이다. wrapping 클래스를 만드는 이유는 여러 클래스에서 new 를 이용해서 Gson 객체를 생성하는데, 굳이 그럴 필요가 있을까 싶어서 만들게 되었다. wrapping 클래스에는 toJson()  함수 밖에 없는데 그 이유는 class to'
featured_image: ''
tags: ['clean code', 'dev', 'GSON', 'JSON', 'wrapping class', '클린코드']
---


<span style="font-size: 11pt;">여러가지 라이브러리가 있겠지만 단연 json 라이브러리 중에 내가 가장 잘 쓰는 것은 [gson ](http://ash84.tistory.com/775)이다. 쓰기 편해서 일수도 있지만, 함수이름이나 그런것들이 잘 지어져있어서 직관적이다. wrapping 클래스를 만드는 이유는 여러 클래스에서 new 를 이용해서 Gson 객체를 생성하는데, 굳이 그럴 필요가 있을까 싶어서 만들게 되었다. wrapping 클래스에는 toJson()  함수 밖에 없는데 그 이유는 class to json String 기능만 필요로 했기 때문이다. 약 10개가 넘는 클래스에서 GSon을 객체를 만드는것 보다는 이렇게 static 으로 만들어두고 필요할때 마다 불러다 쓰는 편이 나을것으로 판단했다. </span>

<span style="font-size: 11pt;">클린코드에서 봤는데, 어떤 라이브러리 혹은 오픈소스를 가져다 쓸때, 그대로 가져다 쓰는 것은 아무리 사용법을 잘 알더라고 권장하지는 않는다고 한다. 만들려고 하는 목적에 부합하는 기능만 따로 뽑아서 wra</span><span style="font-size: 11pt;">pper 클래스를 만들어 쓰는 습관을 들여야 겠다. </span>

<script src="https://gist.github.com/4508680.js"></script>



