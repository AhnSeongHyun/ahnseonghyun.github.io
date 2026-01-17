---
title: '한우찾기 2.4.0 iOS7 개발기'
author: 'ash84'
pub_date: '2013-10-04'
description: '아이폰5가 나오면서 5인치에 대한 지원 그리고 파싱 부분에 대한 에러가 있어서 할까 말까 하고 있었는데 iOS7 이 되면서 기본적인 UI 컴포넌트가 Flat 스타일로 변경이 되고 해서 한우찾기 역시 2.4.0 버전으로 업그레이드 하게 되었다. 몇가지 특징점을 설명하고자 한다. 
**1. Simple, Simple**'
featured_image: ''
tags: ['네이버 애드포스트', '다음맵', '한우찾기']
---
<span style="font-size: 11pt;">아이폰5가 나오면서 5인치에 대한 지원 그리고 파싱 부분에 대한 에러가 있어서 할까 말까 하고 있었는데 iOS7 이 되면서 기본적인 UI 컴포넌트가 Flat 스타일로 변경이 되고 해서 한우찾기 역시 2.4.0 버전으로 업그레이드 하게 되었다. 몇가지 특징점을 설명하고자 한다. </span>

<span style="font-size: 11pt;">**1. Simple, Simple**</span>

 

<table align="center" border="0" cellpadding="0" cellspacing="5"><tbody><tr><td>![](http://ash84.net/wp-content/uploads/1/cfile21.uf.25166934524E94731CD541.PNG)</td><td>![](http://ash84.net/wp-content/uploads/1/cfile28.uf.263C3934524E9478041489.PNG)</td></tr></tbody></table><span style="font-size: 11pt;">– 기존의 많은 실험적 디자인이 있었던 부분을 엄청나리 만큼 간소화를 했다. 예를 들면 바코드 인식하는 부분에 대해서는 기본의 페이지 컨트롤을 통해서 사용자가 한번 이상의 swipe 를 통해서 보고 선택을 하는 방식이었다면 이번에는 그냥 한 화면에 크게 두개의 버튼을 다른 색깔로 둠으로써 보다 빠르게 선택할수 있도록 구성했다. </span>

<span style="font-size: 11pt;">또 다른 예는 조회결과에 대한 사후 처리이다. 이전에는 저장, 메일전송, 복사 이렇게 세가지 작업을 조회 결과에 대해서 수행할 수가 있었는데 이것들을 하려면 사용자가 모든 결과를 2번 이상의 스크롤링을 통해서 하단의 3가지의 버튼을 통해서 가능했었다. 그런데 이번 버전에서는 UIActivity를 커스텀해서 저장과 메일, 복사 뿐만 아니라 카카오톡, 라인 메신저로 다른 사람에게 공유할수 있도록 구성하였으며, 상단에 위치 하기 때문에 스크롤링을 하지 않아도 결과 페이지의 어떤 위치에서도 선택을 해서 원하는 작업을 수행할 수 가 있다. </span>

<span style="font-size: 11pt;">**2. 다음(Daum) 맵 도입**</span>

<span style="font-size: 11pt;">**  
**</span>

<span style="background-color: transparent; font-size: 9pt; line-height: 1.5;">  
</span>

<span style="background-color: transparent; font-size: 11pt; line-height: 2;">– 처음에 한우찾기에서 사용했던 것은 iOS에서 제공하는 기본 맵이었는데, 기본적으로 구글맵이 보여지다가 구글과 애플이 틀어지면서 애플앱이 보여졌다. 다들 알다시피 애플앱은 국내 지도에는 취약한데 보통 한우찾기에서는 소의 이동동 경로를 보여주다 보니, 주로 지방인 경우가 많고 제대로 표시 되지 않는 경우가 많았다. </span>

<span style="background-color: transparent; font-size: 11pt; line-height: 2;">  
</span>

<span style="background-color: transparent; font-size: 11pt; line-height: 2;"></span>

![](http://ash84.net/wp-content/uploads/1/cfile6.uf.232A4933524E93EA03042C.PNG)

<span style="background-color: transparent; font-size: 11pt; line-height: 2;">  
</span>

<span style="background-color: transparent; font-size: 9pt; line-height: 1.5;">  
</span>

<span style="background-color: transparent; font-size: 9pt; line-height: 2;"><span style="font-size: 11pt;">비록 정확한 경로는 아니지만 그래도 국내 지역이 제대로 표시된 지도를 보여줘야 한다는 생각이 있었고, 다음(Daum) 맵을 </span><span style="font-size: 11pt;">사용하게 되었다. 다음맵 사용에 대한 부분은 좀더 정리해서 블로깅을 할 생각인데, 지금으로서는 꽤 만족스러운 편이다. 한가지 아쉬운건 사용자가 선택하지 않으면 말풍선이 핀에 보이지 않는다는 것 뿐. </span></span>

<span style="background-color: transparent; font-size: 9pt; line-height: 1.5;">  
</span>

<span style="background-color: transparent; font-size: 9pt; line-height: 1.5;">  
</span>

<span style="font-size: 11pt;">**3. 네이버 광고의 도입**</span>

<span style="font-size: 11pt;">– 광고에 대한 부분은 많이 생각한 부분인데, 무료앱인 상황이고 취지 자체가 축산업을 하시는 분들께 도움을 드리고자 시작한 것이긴 하지만 1년에 애플 계정 유지비가 10만원이 들기 때문에 광고를 통해서 유지해야 한다는 생각이 들었다. 개인적으로는 네이버 광고의 방식을 모르겠지만 가능하다면 조금이나마 연관된 광고가 나올수 있었으면 하는 바램이 있다. 수익을 올리는 것도 중요하지만 광고를 통해서 축산업에 도움이 되는 제품을 인터넷으로 싼 가격에 구매할수 있었으면 하는 바램이다. </span>

<span style="font-size: 11pt;">기술적으로 크게 변한건 없지만 사실 가수가 예전 음반을 리마스터링 하는것 같이 새롭게 프로젝트를 생성하고 코드를 정리하고 필요한 코드를 새로 작성하였다. 아이폰 3gs에서 작업을 하던 시절에서 아이폰5s 가 나오는 시대로 변경이 되면서 기존의 느린 네트워크, 느린 cpu 때문에 필요로 했던 로딩창이 실제로 거의 필요없게 되면서 코드를 빼는 행복한 작업을 하기도 하였다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 15px; line-height: 29px;">점차 수요에 맞춰서 좀 더 많고 필요한 기능을 추가했으면 하는 바램이다. </span>



