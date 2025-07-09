---
title: '(iOS)MKPointAnnotation에 정보(i) button 달기'
author: 'ash84'
pub_date: '2014-01-14'
description: 'MKPointAnnotation 에 정보(i) 버튼을 추가하고 싶었다. 지도 관련 액션을 actionsheet 를 이용해서 하거나 다른 버튼을 이용해서 했었는데  
 핀에 버튼을 눌러서 보여주고 싶었다. [cocoacontrols](http://www.cocoacontrols.com/) 에 많은 개발자들이 만든 것이 있지만 좀더 손쉽게 할수 있는 방법이 없을까 하는 차에 찾아보니  
MKMapViewDelegate 를 이용하는 방법이 있었다.

MKPointAnnotation을 MKMapView 에 addAnnotattion 함수'
featured_image: ''
tags: ['dev', 'IOS', 'MapView', 'MKAnnotation Button', 'MKPointAnnotation', 'Objective-C']
---


MKPointAnnotation 에 정보(i) 버튼을 추가하고 싶었다. 지도 관련 액션을 actionsheet 를 이용해서 하거나 다른 버튼을 이용해서 했었는데  
 핀에 버튼을 눌러서 보여주고 싶었다. [cocoacontrols](http://www.cocoacontrols.com/) 에 많은 개발자들이 만든 것이 있지만 좀더 손쉽게 할수 있는 방법이 없을까 하는 차에 찾아보니  
MKMapViewDelegate 를 이용하는 방법이 있었다.

MKPointAnnotation을 MKMapView 에 addAnnotattion 함수를 이용해서 추가했다는 가정하에  
 실제 Annotation이 map에 보여질때 호출되는 `viewForAnnotation` delegate에서 MKPinAnnotationView 를 만들고 annoation 을 넣어준다. 그리고 나서 MKAnnotationView에 `canShowCallOut` 을 YES로 설정하고 , `rightCalloutAccessoryView` 에 아래와 같이 UIButton을 만들어서 설정해주면 된다.
 

<script src="https://gist.github.com/AhnSeongHyun/8414804.js"></script>
 
 해당 정보(i)버튼을 클릭했을때, 어떤 액션을 지정하고 싶으면 `calloutAccessoryControlTapped` delegate에서 지정해주면된다. 필자의 경우에는 여기에서 애플맵을 불러와서 길찾기를  
 수행하도록 지정하였다. 생각보다 어렵지 않은데, 그렇게 많은 버튼타입을 지원해주지 않아서 조금 아쉽다. 그래서 몇가지 쓸만한 MKAnnotationView 커스텀 관련 오픈소스들을 [cocoacontrols](http://www.cocoacontrols.com/) 에서 추려봤다. 미리 말하지만 스샷만 보고 판단하는 지극히 주관적인 판단임을 밝힌다.  

#### [SMCallOutView](https://www.cocoacontrols.com/controls/smcalloutview)

제일 간단한 형태라고 생각되어 지는데, 정보(i) 버튼 대신에 세부사항으로 들어가거나 할때에 쓰면 좋을 예라고 생각된다.

[JPSThumbnailAnnotation](https://www.cocoacontrols.com/controls/jpsthumbnailannotation)

Title, Subtitle, Button 에 사진까지. 단연코 종합선물 세트다. 뭔가 사진으로 MKAnnotation에서 보여주고자 한다면 주저없이 선택할것 같다. 

#### [MultiRowCalloutAnnotationView](https://www.cocoacontrols.com/controls/multirowcalloutannotationview)


한줄이 아니라 여러줄로 보여줄떄 괜찮은 AnntationView이다. 이런 케이스가 있을까 싶기도 한데, 어떤 장소에 내 친구의 체크인 정보를 보여준다거나 할때 상위 몇명만 저런식으로 보여주는것도 괜찮을것 같다.  
