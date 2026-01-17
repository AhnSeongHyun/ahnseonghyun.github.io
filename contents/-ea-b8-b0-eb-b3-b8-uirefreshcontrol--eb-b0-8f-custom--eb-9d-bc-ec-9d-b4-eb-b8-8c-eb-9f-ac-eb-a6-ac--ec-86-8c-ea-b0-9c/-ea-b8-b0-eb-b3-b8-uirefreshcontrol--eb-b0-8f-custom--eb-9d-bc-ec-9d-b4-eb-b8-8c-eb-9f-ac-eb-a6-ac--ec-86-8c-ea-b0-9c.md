---
title: '기본 UIRefreshControl 및 Custom 라이브러리 소개'
author: 'ash84'
pub_date: '2014-11-28'
description: '기본적인 UIRefreshControl 에 대한 사용법이다. UITableView에 addSubView:  하는것만으로도 쉽게 사용할 수 있다. spinner 의 색은 setTintColor 를 이용해서 설정할 수가 있고, backgroundColor 을 지정하면 끌어 당겼을 때의 배경색을 지정할 수가 있다. selector 로 지정한 함수에서 웹서비스를  호출하는 함수를 지정해'
featured_image: ''
tags: ['Objective-C', 'UIRefreshControl', 'UITableView', 'dev', 'tutorial']
---
<script src="https://gist.github.com/AhnSeongHyun/6c83553e8e93838da564.js"></script>

기본적인 UIRefreshControl 에 대한 사용법이다. UITableView에 addSubView:  하는것만으로도 쉽게 사용할 수 있다. spinner 의 색은 setTintColor 를 이용해서 설정할 수가 있고, backgroundColor 을 지정하면 끌어 당겼을 때의 배경색을 지정할 수가 있다. selector 로 지정한 함수에서 웹서비스를  호출하는 함수를 지정해 주면 된다. 

사실 요즘에는 굉장히 많은 라이브러리가 있는데 굳이 UITableView 넣지 않더라도 많은 커스텀 라이브러리들이 있다. 아래의 화면처럼 두개의 이미지가 합쳐지는 것도, 이미지 기반이 아닌 텍스트 기반인 것도 있었다.
 
**몇가지 소개를 하자면 :**

- [ http://www.jackrabbitmobile.com/design/ios-custom-pull-to-refresh-control](http://www.jackrabbitmobile.com/design/ios-custom-pull-to-refresh-control "http://www.jackrabbitmobile.com/design/ios-custom-pull-to-refresh-control") : 위의 화면관련 블로그 글, 해당 링크를 가면 github 주소도 있다.

- [https://www.cocoacontrols.com/controls/xhrefreshcontrol](https://www.cocoacontrols.com/controls/xhrefreshcontrol "https://www.cocoacontrols.com/controls/xhrefreshcontrol") : 중국어로 된… 조금아쉽긴 하지만 그래도 괜찮은 컨트롤

 

- [https://www.cocoacontrols.com/search?utf8=%E2%9C%93&q=refresh](https://www.cocoacontrols.com/search?utf8=%E2%9C%93&q=refresh "https://www.cocoacontrols.com/search?utf8=%E2%9C%93&q=refresh") : CocoaControls에 ‘refresh’ 라고 입력하면 여러 결과가 나온다.

[읽어볼만한 글](http://story.pxd.co.kr/711)인데  pull to refresh 에 대한 UI/UX적인 부분에서의 접근인데 한번쯤 보면 좋을것 같다. 



