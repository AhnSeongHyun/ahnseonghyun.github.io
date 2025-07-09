---
title: 'optimizely를 이용한  A/B Testing'
author: 'ash84'
pub_date: '2015-05-31'
description: '이번에는 optimizely를 이용한 A/B Testing에 대해서 간단하게 알아 보도록 하겠다.


## 방식

optimizely 의 방식은 구글 애널리틱스와 다르게, 원본 페이지의 특정 부분, 예를 들면 로그인 버튼의 여러 디자인을 테스트 한다고 하면 한 페이지에 대한 디자인 시안은 optimizely.com 에서 수정하고 그것을 변수로 반영할수 있는 js 를 원본 페이지에 넣게 되면 원본페이지 로딩시 지정한 디자인으로 나오게 되는것이다. 즉, 구글 애널리틱스와 다른점은 여러개의 페이지를 만드는 것이 아니라 하나의 페이지에서'
featured_image: ''
tags: ['a/b testing optimizely', 'dev', 'Optimizely']
---


이번에는 optimizely를 이용한 A/B Testing에 대해서 간단하게 알아 보도록 하겠다.


## 방식

optimizely 의 방식은 구글 애널리틱스와 다르게, 원본 페이지의 특정 부분, 예를 들면 로그인 버튼의 여러 디자인을 테스트 한다고 하면 한 페이지에 대한 디자인 시안은 optimizely.com 에서 수정하고 그것을 변수로 반영할수 있는 js 를 원본 페이지에 넣게 되면 원본페이지 로딩시 지정한 디자인으로 나오게 되는것이다. 즉, 구글 애널리틱스와 다른점은 여러개의 페이지를 만드는 것이 아니라 하나의 페이지에서 개발자가 정의한 디자인으로 랜덤하게 나오게 되는 것이다.


## 절차

가입을 하고, create new project를 통해서 웹 프로젝트를 만든다.

<div class="jetpack-video-wrapper">[![1](https://farm8.staticflickr.com/7748/18285820875_ce53bbfbdb_z.jpg)](https://flic.kr/p/tRRBtH)</div>2. 하나의 프로젝트 안에서 몇개의 실험(experiment)를 가질 수 있는데 아래와 같이 새로운 실험을 만든다. 이때 실험할 url을 써줘야 한다.

<div class="jetpack-video-wrapper">[![2](https://farm8.staticflickr.com/7768/18259397336_afc68b16be_n.jpg)](https://flic.kr/p/tPwbFs)</div><div class="jetpack-video-wrapper">[![2-1](https://farm9.staticflickr.com/8791/18098088860_490c4655be_z.jpg)](https://flic.kr/p/tzgrhQ)</div>3. url이 인식되고나면 변수를 설정해야 하는데 화면에서 HTML 요소들에 마우스 우클릭을 하면 아래와 같은 화면을 볼수가 있고 수정하고 싶은대로 수정하면 된다.

<div class="jetpack-video-wrapper">[![3](https://farm8.staticflickr.com/7766/18259397136_cf3b5e4515_n.jpg)](https://flic.kr/p/tPwbC1)</div>색깔과 사이즈를 변경한 상태로 더 변수를 추가하고 싶으면 Add Variation을 누르고 추가하면 된다. save now를 누른다.

<div class="jetpack-video-wrapper">[![4](https://farm8.staticflickr.com/7737/18259397206_29c568c302_z.jpg)](https://flic.kr/p/tPwbDd)</div>일단 변수에 대한 지정이 끝나면 URL Targeting 을 해야하는데 보통 테스팅이 될 곳을 지정하면 된다. **해당 페이지가 있는 곳을 지정하면 된다. 이때 주의할점이 원URL이 다른 url로 리다이렉트 되는 경우라면 종착지 url을 써줘야 한다. **

<div class="jetpack-video-wrapper">[![5](https://farm9.staticflickr.com/8856/18098011478_79192c103d_n.jpg)](https://flic.kr/p/tzg3hE)</div>상단에 saved 버튼을 누르면 저장이 되고 Start Experiment 버튼을 누르면 별도의 문제가 없다면 바로 실험이 시작된다. 여기서는 일단 누르지 않고  
 다시 외부로 나가서 우리가 만든 실험을 누르면 정보를 볼수가 있는데 Traffic Allocation 을 수정해서 세개의 (원본 포함) URL이 어떤 비율로 보여질지를 설정해야 한다.

<div class="jetpack-video-wrapper">[![6](https://farm9.staticflickr.com/8893/18285820325_32a27e19c9_z.jpg)](https://flic.kr/p/tRRBje)</div><div class="jetpack-video-wrapper">[![7](https://farm9.staticflickr.com/8824/17663217274_0ca9bdebea_n.jpg)](https://flic.kr/p/sUQB7S)</div>마지막으로 해야할 일은, Settings 에 가서 js 파일을 테스트에 해당하는 웹페이지의 다음부분에 바로 지정해 줘야 한다. 이렇게 하고 나서 실험시작(play, start experiment) 버튼을 누르면 실험이 시작되고 실시간으로 결과가 기록되게 된다.

<div class="jetpack-video-wrapper">[![8](https://farm8.staticflickr.com/7750/17665235083_dbaacf469c_n.jpg)](https://flic.kr/p/sV1WWF)</div>[http://loginabtesting.herokuapp.com/](http://loginabtesting.herokuapp.com/)


## 사용후기

사용하기는 분명 구글 애널릭스틱보다 편하고 가장 큰 장점은 실시간성이라는 생각이 든다. 바로바로 반영할 수 있고, 또한 코드를 집어 넣는것이 아니라 js 파일 링크를 넣는것이기 때문에 사용자는 딱 한번만 코드를 넣으면 되고 그 이후의 모든 수정을 js를 대상으로 이루어진다. 실시간으로 수정된 것들이 반영이 되고 그에따라 바로바로 결과에 반영된다.



