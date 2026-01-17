---
title: 'audio5.js 를 이용한 음원 재생 및 제어'
author: 'ash84'
pub_date: '2016-12-02'
description: '이번 프로젝트 하면서, 주문이 들어왔을 때 웹상에서 특정 소리로 사용자에게 알려줘야하는 부분이 있었는데, 음원 재생관련 라이브러리를 찾아 보다가 괜찮은 것이 있어서 예제코드를 남긴다. 

http://zohararad.github.io/audio5js/



좀더 위의 링크에 들어가서 보면 세세한 조절을 할 수가 있도록 제공하고 있다. 예를 들면, `seek` 기'
featured_image: ''
tags: ['JavaScript', 'audio', 'audio5.js']
---
이번 프로젝트 하면서, 주문이 들어왔을 때 웹상에서 특정 소리로 사용자에게 알려줘야하는 부분이 있었는데, 음원 재생관련 라이브러리를 찾아 보다가 괜찮은 것이 있어서 예제코드를 남긴다. 

http://zohararad.github.io/audio5js/

<script src="https://gist.github.com/AhnSeongHyun/f7f313dcfaefc282a680ec5221898e56.js"></script>

좀더 위의 링크에 들어가서 보면 세세한 조절을 할 수가 있도록 제공하고 있다. 예를 들면, `seek` 기능을 제공하고 있기도 하다. 위의 예제를 쓰고 나서 추가적으로 요청사항이 들어와서 특정 상황에서 재생하고 끝난후 어떤 데이터를 체크해서 다시 재생하는 것을 구현해야할 필요가 있었는데, 대부분의 상황을 해당 라이브러리에서 지원하고 있었다. 

추가적으로 지원하는 브라우저 버전은 아래와 같다.

- IE8, IE9
- Chrome 23 (Mac)
- Firefox 17 (Mac)
- Safari 6
- Opera 12 (Mac)
- Safari Mobile (iOS 6.0)
- Webkit Mobile (Android 4.0.4)


