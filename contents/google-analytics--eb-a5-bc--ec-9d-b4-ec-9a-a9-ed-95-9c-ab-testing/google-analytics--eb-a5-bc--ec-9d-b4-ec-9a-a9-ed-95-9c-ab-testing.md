---
title: 'Google Analytics 를 이용한 A/B Testing'
author: 'ash84'
pub_date: '2015-07-03'
description: '### 방식

– 구글 애널리틱스의 A/B Testing 방식은 2개이상의 페이지(이건 개발자가 개발을 해 놔야 한다.) 를 등록하면 특정 js 파일을 삽입하라고 알려주고 해당 js 파일을 2개 이상의 페이지에서 삽입하면 진입시에 지정한 비율에 따라서 지정된 페이지로 이동이 된다.

[![Image1](https://farm9.staticflickr.com/8861/17928935856_c48de2b037_n.jpg)](https://flic.kr/p/tjjtZJ)</'
featured_image: ''
tags: ['dev', 'GA', 'google analytics a/b testing']
---


### 방식

– 구글 애널리틱스의 A/B Testing 방식은 2개이상의 페이지(이건 개발자가 개발을 해 놔야 한다.) 를 등록하면 특정 js 파일을 삽입하라고 알려주고 해당 js 파일을 2개 이상의 페이지에서 삽입하면 진입시에 지정한 비율에 따라서 지정된 페이지로 이동이 된다.

<div class="jetpack-video-wrapper">[![Image1](https://farm9.staticflickr.com/8861/17928935856_c48de2b037_n.jpg)](https://flic.kr/p/tjjtZJ)</div>### 절차

**  
 1. 기본적인 사이트를 만들고, 웹사이트 추적 코드를 A(원본페이지) 와 B(혹은 C, 대상페이지)에 넣는다.  
**

 * 원본 페이지 : http://loginabtesting.com/logina  
 * 대상 페이지 : http://loginabtesting.com/loginb

**2. 구글 애널리틱스 내 “방문형태” > “실험” 을 누른다. 아래의 화면과 같이 실험을 추가할 수 있는 화면이 나온다.**

<div class="jetpack-video-wrapper">[![183A4DB3-0EF1-4AAD-9772-013FBA627973](https://farm9.staticflickr.com/8783/18229465016_d96582857b_z.jpg)](https://flic.kr/p/tLSLQY)</div>“실험만들기”를 누른다.

<div class="jetpack-video-wrapper">[![DE3F9B2D-8140-4FEB-8579-4F132A0FA60C](https://farm8.staticflickr.com/7799/18229464976_bdffac6361_z.jpg)](https://flic.kr/p/tLSLQh)</div>위와 같이 실험 목적을 추가하는데 별도의 실험 목적을 커스터마이징 하고 싶을 경우, “새 목표 만들기”를 누른다. 실험할 트래픽 비율을 50%, 이 비율이 실제 원본 페이지 접근시 몇 % 나 대안 페이지로 보낼것인지를 정하는 부분이다. 실험구성하기 단계에서는 원본 페이지와 대상(실험)페이지를 입력한다. 대안이 추가로 있을 경우 “대안추가” 버튼을 누르고 입력한다.

그리고나서 실험코드를 받아서 A와 B 사이트에 넣어주는데 주의할 점은

 태그 바로 아래에 입력해야 한다. 1단계에서 구글 추적코드의 경우 아무곳에나 넣어도 되는데, 되도록 전에 넣으면 되는데, 위의실험 코드는 구글 애널리틱스에서 해당 테스팅 페이지의 첫 256Byte 만 읽어오기 때문에 태그 바로 아래에 위치 해야한다. <div class="jetpack-video-wrapper">[![34](https://farm6.staticflickr.com/5329/17769161619_430a4402f5_z.jpg)](https://flic.kr/p/t5cAFv)</div>다음 단계에서는 위에서 입력한 실험코드를 제대로 입력 했는지 확인을 한다. 반드시, 위의 단계를 통과하고 실험을 시작해야 한다.

<div class="jetpack-video-wrapper">[![6](https://farm6.staticflickr.com/5348/17334859603_5da53e8f1b_n.jpg)](https://flic.kr/p/spPFPH)</div>**3. 실험여부 확인 **  
 아래와 같이 logina (원본) 페이지에 접근한다.

<div class="jetpack-video-wrapper">[![7](https://farm9.staticflickr.com/8826/17952261762_88b7ff789f_n.jpg)](https://flic.kr/p/tmo2Yw)</div>접근시 logina(원본) 페이지가 아닌 loginb(대상) 페이지가 뜬다. 아래의 화면을 보면 loginb url 에 google 실험 관련 코드가 있는 것을 볼 수가 있다.

<div class="jetpack-video-wrapper">[![8](https://farm8.staticflickr.com/7722/17334859913_3682a075b7_z.jpg)](https://flic.kr/p/spPFV4)</div>**사용후기**

* 장점 : 아직은 모르겠지만, 하나의 사이트를 구글 애널리틱스를 통해서 분석할다고 했을때는 다른 데이터와 함께 연계해서 보고 분석할때 가치가 있을것으로 판단됨.

* 단점 : 대안 페이지를 개발자가 모두 만들어야 함. 때문에 페이지에 모두 실험코드를 넣어야 하는 번거로움이 있음.



