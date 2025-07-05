---
title: 'powerline 설치후기'
author: 'ash84'
pub_date: '2015-12-10'
description: ''
featured_image: ''
tags: ['dev', 'powerline', 'python shell']
---


![](https://farm1.staticflickr.com/581/23006961403_2b2ba85903_b.jpg)  
 개발환경을 최적화하는게 중요하다고 생각한다. 내가 회사에 있던 집에 있던 어디에 있던 간에 동일한 개발환경(키보드만 빼고)을 가져가고 싶은데, pycharm 을 메인 도구로 사용하고 있어서 settings.jar export 해서 드롭박스 같은 클라우드에 넣어서 읽어서 사용하는 식으로 동기화를 하고 있다. 그러던 중에 shell 쪽도 어두컴컴한 화면에 파란색 글자가 너무 알아보기도 힘들도 좀 알아 보기 좋게 할 수 없을까 싶어서 찾던 중에 powerline 이라는 python 기반의 shell 을 이쁘게 만들어 주는 툴을 찾았다. 아래의 링크는 공식링크이다.

[https://powerline.readthedocs.org/en/latest/index.html](https://powerline.readthedocs.org/en/latest/index.html)

그리고 이건 한국어로 된 설치 후기.

[http://humb1ec0ding.github.io/2013/11/26/ubuntu-powerline-beautify-the-stateline.html](http://humb1ec0ding.github.io/2013/11/26/ubuntu-powerline-beautify-the-stateline.html)

centOS 와 ubuntu 사용하는 모든 서버에 설치했는데 몇가지 유의사항이 있다. 반드시 bash 적용시 설치된 경로를 지정해 줘야 하는데 위의 후기만을 보고 dist-packages 로 지정하지 말고 pip로 설치한 이후에 `pip show powerline-status` 를 통해서 설치 위치를 확인한 뒤에 설치하기를 권장한다. 색깔이 분명하게 나와서 좋고 vim의 경우, 적용해서 실행하면 인코딩을 하단에 알려줘서 좋은것 같다.



