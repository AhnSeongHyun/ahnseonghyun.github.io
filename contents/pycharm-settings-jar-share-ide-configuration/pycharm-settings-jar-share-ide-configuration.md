---
title: 'pycharm - settings.jar 개발환경 공유'
author: 'ash84'
pub_date: '2018-05-17'
description: '사내 팀에서 pycharm 을 파이썬 개발 공식툴로 사용하고 있다. 처음에 커뮤니티버전에서 시작해서, 개인 프로페셔널을 쓰다가, 이제는 회사에서 라이센스를 끊어서(기업용) 사용하고 있다. 개인 개발용으로도 구입해서 사용하고 있는데, 회사와 내 개인용 컴퓨터(맥) 간의 pycharm 환경을 동일하게 맞추고 싶었다. 

테마, 폰트, 색깔 같은 외향적인 부분이 가장 크게 맞추고 싶은 부분이었고 개인적으로 사용하는 서버나 그런것들도 다시 설정하기도 귀찮았다. 



개인적으로 사용해보진 않았지만, 좀더 나은 방법은 settings.jar'
featured_image: 'https://www.fullstackpython.com/img/logos/pycharm.jpg'
tags: ['dev', 'pycharm', 'ide', 'settings.jar', 'Python']
---

사내 팀에서 pycharm 을 파이썬 개발 공식툴로 사용하고 있다. 처음에 커뮤니티버전에서 시작해서, 개인 프로페셔널을 쓰다가, 이제는 회사에서 라이센스를 끊어서(기업용) 사용하고 있다. 개인 개발용으로도 구입해서 사용하고 있는데, 회사와 내 개인용 컴퓨터(맥) 간의 pycharm 환경을 동일하게 맞추고 싶었다. 

테마, 폰트, 색깔 같은 외향적인 부분이 가장 크게 맞추고 싶은 부분이었고 개인적으로 사용하는 서버나 그런것들도 다시 설정하기도 귀찮았다. 



개인적으로 사용해보진 않았지만, 좀더 나은 방법은 settings.jar 를 dropbox 나 네이버 클라우드와 같은 것을 이용해서(회사에서 허용이 된다면) 회사컴-집컴의 개발환경을 settings.jar 를 통해서 동기화 시킬수 도 있을것 같다. 



![pycharm settings.jar](https://c1.staticflickr.com/3/2821/33325002360_0f995e6219_b.jpg)

다행히 pycharm 에서는 `Import Settings`, `Export Settings` 를 통해서 해당 기능을 지원하고 있다. Export Setting을 하게 되면, 현재 사용하는 환경에 대해서 jar 로 묶을 화면이 아래와 같이 출력이 되고, 내가 원하는 위치에 settings.jar 를 export 시킬 수 있다. 

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- ash84.net_링크광고 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="8167194879"
     data-ad-format="link"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>

그리고 그 settings.jar 를 가지고 집에서 사용하는 내 컴퓨터에서 Import Settings 를 통해서 환경설정을 맞추면 된다. 가져오는 과정에서도 마찬가지로 선택적으로 항목을 조정해서 가져올 수 있다. 예를 들면, 회사에서 사용하는 서버는 집에서는 접속이 안될수 있고 상이할 수 있기 때문에 그런 부분은 배제하고 import 시키면 된다. 

![pycharm settings.jar](https://c1.staticflickr.com/3/2859/33579837871_883baa8115_b.jpg])


그럼에도 불구하고 차이가 나는 부분이 존재하는데, 필자의 경우 특히 윈도우-맥 환경을 사용하다 보니 맥에서 다시 default keymap 을 조정해야 하는 경우가 있었는데, 이정도는 감수할 만 한것 같다. 
**그리고 또 하나 장점은 jetbrain 사의 다른 IDE에도 Import 가 가능하다는 점이다.** 예를들면, pycharm을 쓰다가 phpstorm 을 쓰게 되면, 다시 그에 맞는 환경을 세팅해야 하는데 그럴 필요 없이 settings.jar 를 가지고 import 후에 다시 일부분 조정해서 사용하면 편하게 사용할 수 가 있다. 






