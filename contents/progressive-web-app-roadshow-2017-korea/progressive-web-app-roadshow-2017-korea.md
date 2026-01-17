---
title: 'PROGRESSIVE WEB APP ROADSHOW 2017 KOREA'
author: 'ash84'
pub_date: '2017-04-21'
description: '커리어가 웹의 백엔드와 프론트 언저리에 걸쳐져 있는데 확실히 프론트엔드 개발쪽은 변화가 굉장히 빠르게 일어나고 있다는 것을 느낀다. AMP, PWA 에 대해서 도데체 뭔지 그리고 지금 결제 관련 일을 하고 있기 때문에 WebPaymentAPI 에 대해서 좀 더 알고자 참가하게 되었다. 

![](https://c1.staticflickr.com/5/4186/34149995140_1140576652_k.jpg)

행사 준비 자체는 잘 되었던것 같다. 스타벅스 커피도 있었고, 오후에는 도넛을 나눠줘서 다들 즐겁게 먹으면서 봤던것 같다.'
featured_image: 'https://gdg-korea-webtech.firebaseapp.com/pwa-roadshow17/roadshow.svg'
tags: ['AMP', 'PWA', 'ServiceWorker', 'WebPaymentAPI', 'career', 'conference', 'dev']
---
커리어가 웹의 백엔드와 프론트 언저리에 걸쳐져 있는데 확실히 프론트엔드 개발쪽은 변화가 굉장히 빠르게 일어나고 있다는 것을 느낀다. AMP, PWA 에 대해서 도데체 뭔지 그리고 지금 결제 관련 일을 하고 있기 때문에 WebPaymentAPI 에 대해서 좀 더 알고자 참가하게 되었다. 

![](https://c1.staticflickr.com/5/4186/34149995140_1140576652_k.jpg)

행사 준비 자체는 잘 되었던것 같다. 스타벅스 커피도 있었고, 오후에는 도넛을 나눠줘서 다들 즐겁게 먹으면서 봤던것 같다.(나는 몸이 안좋아서 스킵) 

PWA 에 대해서 주로 많은 설명을 들었다. 왜 이게 나오게 되었는지, 지향하는 부분이 어디인지, 그리고 기술적으로 어떻게 구현해야하는지 잘 설명해주고 있다. AMP 에 대해서 그리 많이 듣진 않았는데, 개인적으로 좀 별도의 페이지나 템플릿을 둬야 하나 하는 생각도 들었다. 전략적으로 선택해볼만 하지 않나 싶다. 

![](https://c1.staticflickr.com/5/4171/33724691503_c66a83ca8d_k.jpg)

WebPaymentAPI 는 이전에도 발표를 다른 세미나/컨퍼런스에서 보긴 했었는데 아직도 갈길이 멀다는 생각이 들었다. 이런 표준화? 같은 작업은 top-down 방식으로 작업이 되고 있을텐데, 각 나라별 결제 방식이 조금씩 다르기 때문에 PG나 관련 회사에서 적극적인 참여가 필요하지 않나 싶었다. 결국엔 우리나라 실정과 맞지 않아서 안쓰는 형태로 가지 않을까 싶다. 

<hr>

행사 링크 : https://gdg-korea-webtech.firebaseapp.com/pwa-roadshow17/

**Keynote: Progressive Web Apps: What, Why and How(도창욱)**

<iframe src="//www.slideshare.net/slideshow/embed_code/key/O8KQmBR4Wxmtr" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/cwdoh/pwa-roadshow-seoul-keynote" title="PWA Roadshow Seoul - Keynote" target="_blank">PWA Roadshow Seoul - Keynote</a> </strong> from <strong><a target="_blank" href="https://www.slideshare.net/cwdoh">Chang W. Doh</a></strong> </div>

- 웹의 큰 변화 - Ajax

- 모바일 기기의 증가

- 앱에 비해서 모바일 앱의 기능의 확산 => progressively(점진적인, 점진적으로) => 사용자 경험의 개선 

- 이탈한 사용자를 다시 끌어오기란 어렵다 

- 홈스크린 설치 유도, 우리 페이지는 사용자의 앱 리스트에 없다.

- 서비스 워커 - 오프라인 웹앱에 대한 지원 
- 아직 iOS 지원되지 않음. 모든 브라우저를 지원하지는 못함

- 시작하기 : https 

- PWA 3가지 접근 방법
  - 다시 만들기 => 비난초래, 가장 완벽한 버전
  - 가벼운 버전
  - 하나의 기능으로 시작 

- 과거와 현재의웹에 대한 정리 
- 네이티브 앱과의 차이를 줄이는 방식으로 간다. 


**Session 1: Service Workers for Instant and Offline Experiences(삼성전자 송정기)**

<iframe src="//www.slideshare.net/slideshow/embed_code/key/BFxOHWSPrCnWMR" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/jungkees/pwa-roadshow-korea-service-worker-75350144" title="PWA Roadshow Korea - Service Worker" target="_blank">PWA Roadshow Korea - Service Worker</a> </strong> from <strong><a target="_blank" href="https://www.slideshare.net/jungkees">jungkees</a></strong> </div>

사용자에게 네이티브 앱같은 효과를 주자 

PWA = 안정적, 빠르고, 고객을 쉽게 끌어 들인다. 

기존 모바일 웹사이트를 PWA기술로 보완한다. 
이미 많은 서비스들이 PWA 기술을 이용해서 구현하고 있다. 
PWA를 통해서 마케팅 적인 측면, 이탈율 감속, 실 구매율 증가 등의 효과를 보고 있다. 

flipkart - 홈화면에 추가시, 주소표시줄이 없어짐. 앱처럼 
weigo 
twitter lite - twitter.com

Service Worker

- udacity pwa 만드는 동영상이 있음 
- 해결하고자 하는 문제 1: lie-fi 를 해결하자. 네트워크가 느린 경우 어떻게 페이지 로딩 할것인가? 
  - 결국  컨텐츠 캐싱
  - 네트워크 스택을 가기 전에 서비스워커가 가로채서 제어하는 방식

- 문제 2: 백그라운드 서비스 제공 
  - 푸시 노티피케이션에서 활용 

- 브라우저 서포트 : isServiceWorkerReady? 
- 가능한 브라우저만 지원해도 큰 효과, 메인 페이지에만 일단 적용, 점진적으로 적용하자. 

- 이벤트 기반으 워커(서비스워커)
  - 요청시 발동되는 형태, 서비스 워커가 캐시에서 데이터 가져오기 
  
Dedicated worker의 주기 
- 페이지에 바인딩, 계속 살아 있다. 

서비스워커의 주기  
- 동작이 끝나면 종료 시킬 수 있다. 

pwa.rocks

**Session 2: Securing the Foundation with HTTPS(도창욱)**

<iframe src="//www.slideshare.net/slideshow/embed_code/key/brnvghAXhukfmt" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/cwdoh/pwa-roadshow-seoul-https" title="PWA Roadshow Seoul - HTTPS" target="_blank">PWA Roadshow Seoul - HTTPS</a> </strong> from <strong><a target="_blank" href="https://www.slideshare.net/cwdoh">Chang W. Doh</a></strong> </div>

- 보안의 이슈 
- https 를 쓰면 느리다?
 - 조금이라도 빠르게 하기 위한 장치 필요 
 - first start : 핸드쉐이크가 정상적으로 이루어 질것이라고 예상하는 방식 

- http/2
  - 성능 유지와 보안 강화 

**Session 3: Deep Engagement: Installable apps and Push Notifications(박상현)**


슬라이드 링크 : https://docs.google.com/presentation/d/14_jRqn1xwe29RqXsy-uoVcrbt6tkuAW3sKr3PXZXliw/edit#slide=id.p11

- 바탕화면에 숏컷으로 설치 

  - 설치 정보 명시 : manifest.json 파일로 숏컷에서 보여줄 정보 
  - 개발자 도구 > 애플리케이션 > manifest 확인 

- Push API 
  - VAPID(라이브러리를 통해서 키 생성)



**Session 4: Tooling for Progressive Web Apps: Lighthouse and More(장기효)**

<iframe src="//www.slideshare.net/slideshow/embed_code/key/7MxUnE3qeLwELJ" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/GihyoJoshuaJang/2017googlepwaroadshowlighthouse" title="2017_Google_PWA_Roadshow_Lighthouse" target="_blank">2017_Google_PWA_Roadshow_Lighthouse</a> </strong> from <strong><a target="_blank" href="https://www.slideshare.net/GihyoJoshuaJang">Gihyo Joshua Jang</a></strong> </div>

- LightHouse 라는 툴 : 웹 페이지 성능 측정 도구, PWA 도 측정, 구조적 설계 및 객관적 수치화 
- 크롬 개발자 도구로 쉽게 설치 할 수 있다. 
- lighthouse viewer : report 형태로 제공이 된다. 

- https://developers.google.com/web/tools/lighthouse/?hl=ko

- 옵션 상에서 측정의 기준을 변경 할 수 있다. 

**Session 5: AMP for Progressive Web Apps(조은)**

<iframe src="//www.slideshare.net/slideshow/embed_code/key/LaJSHQI2zP6krN" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/euncho161/amp-and-pwa" title="AMP and PWA" target="_blank">AMP and PWA</a> </strong> from <strong><a target="_blank" href="https://www.slideshare.net/euncho161">Eun Cho</a></strong> </div>


- 모바일 페이지가 느리다. 
- Start fast, Stay fast

- AMP : accelerated mobile page 
  - amp html 
  - amp js
  - amp cache

- 외부 로딩에 민감함. 
- css 작성에 제한이 있음. 
- 우선순위 컨텐츠 로딩 

- 변경할게 많지 않다고 하지만, 적지도 않은듯. 

- AMP and PWA
 
- 참고 사이트 :
  - ampproject.org
  - ampbyexample.com


**Session 6: Web Payments API(방진호)**


슬라이드 링크 - https://docs.google.com/presentation/d/1MwAe4lLVpBEEjEGSj0EQ0nsp-tXL555iUp-OpwZlohI/edit#slide=id.p

- W3C 표준, 브라우저에서 관심을 가진다. 
- 카트 단계에서 취소 하는 고객이 엄청 많다 > 입력하는게 귀찮다. 
- 결제 관련 ux를 cp가 아닌 브라우저에서 만든다. 보여줘야 할 정보는 cp가 브라우저에게 준다. 
- 실제 페이먼트 부분은 아직까지 표준안 논의중. 

Payment Request API

- 결제를 요청하는 API
  - method data : 핸드폰 소액결제, 신용카드 
  - details : 결제 정보 
  - options : 사용자로부터 수집할 정보 

- http://paytest.github.io/
- https://developers.google.com/web/fundamentals/discovery-and-monetization/payment-request/?hl=ko

- 새로운 결제 시스템이 아니다. 사용자가 선택한 정보를 CP로 보내고 그걸 cp가 pg로 보내서 결제를 이루어 진다. 결국 결제는 pg가 수행. 

- 국내에서는 각 pg 마다 간편결제가 있고 그것을 사용하는 곳은 한정적, 티몬페이-티몬, 스마일페이-지마켓

- 실질적으로 payment app 과 연관이 되어야 한다. payment request - payment app  


Payment Handler API

- payment request가 있어야 handler를 쓸수 잇다. 
- payment app에 대한 관리 
- 서비스워커를 이용 
- 웹앱 기반, 설치하는데 별도의 시간 없음 
- 서비스 워커?
  - payment app에 대한 저장 관리 
 
- 현재 handler 는 구현중. 
 

**Session 7: PWA with React.js and Firebase**


**Session 8: PWA with Angular**

- 개인적으로 큰 React.js, Angular는 관심이 적어서 듣질 않음. 
