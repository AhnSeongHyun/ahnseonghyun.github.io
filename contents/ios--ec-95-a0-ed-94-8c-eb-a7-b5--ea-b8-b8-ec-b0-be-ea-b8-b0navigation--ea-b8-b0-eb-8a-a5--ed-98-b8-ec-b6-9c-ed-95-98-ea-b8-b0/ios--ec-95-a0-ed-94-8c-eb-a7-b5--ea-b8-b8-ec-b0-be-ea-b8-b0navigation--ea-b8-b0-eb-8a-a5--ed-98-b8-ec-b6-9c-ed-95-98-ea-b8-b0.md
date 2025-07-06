---
title: '(iOS) 애플맵 길찾기(navigation) 기능 호출하기'
author: 'ash84'
pub_date: '2015-07-03'
description: '다양한 지도 어플들이 있고 그러한 지도 어플 업체나 플랫폼 업체에서 sdk 를 제공하긴 하지만 사실 약간의 문제들이 있다. 예를 들면, 전세계를 대상으로 앱을 만든다고 하면 우리에게 친숙한 네이버나 다음같은 앱을 이용해서 길찾기나 외부 지도앱을 불러올수가 있다. 설령 해당 사용자의 아이폰에 설치가 되어 있다고 해도 해당 지역의 경우 지원이 안될수가 있기 때문에. 무적의 구글맵이 있긴 하지만, 아이폰에서 사용자가 다운을 받아놔야 한다는 단점이 있는데, 애플맵은 기본 설치된 상태'
featured_image: ''
tags: ['dev', 'IOS', 'navigation', '길찾기', '길찾기 구현', '네이버 맵', '다음 맵', '애플']
---


<span style="font-size: 11pt;">다양한 지도 어플들이 있고 그러한 지도 어플 업체나 플랫폼 업체에서 sdk 를 제공하긴 하지만 사실 약간의 문제들이 있다. 예를 들면, 전세계를 대상으로 앱을 만든다고 하면 우리에게 친숙한 네이버나 다음같은 앱을 이용해서 길찾기나 외부 지도앱을 불러올수가 있다. 설령 해당 사용자의 아이폰에 설치가 되어 있다고 해도 해당 지역의 경우 지원이 안될수가 있기 때문에. 무적의 구글맵이 있긴 하지만, 아이폰에서 사용자가 다운을 받아놔야 한다는 단점이 있는데, 애플맵은 기본 설치된 상태로 출고가 되고, 잘 안되는 지역이 있긴 하지만 지울수 없다는 장점도 있다. </span>

<span style="font-size: 11pt;">구현하고 싶은 기능은 내가 만든앱에서 위치정보를 가지고 있다고 할때, 애플 맵의 길찾기 기능을 실행시키는 것이다. 예전에 다음맵에서도 이 작업을 한적이 있는데 다음맵에서는 URL 스키마를 이용해서 작업해 주면 된다. </span>

<script src="https://gist.github.com/AhnSeongHyun/7440757.js"></script>

<span style="font-size: 11pt;">위의 코드를 보자. 일단 애플맵을 실행 시키는 부분은 13번째 줄에서 `openMapsWithItems:` 메소드를 이용해서 호출하고 있다. 저 한 부분이면 되는데, 그 안에 지도에 표시할곳과  실행 옵션을 지정해 주어야 한다. 지도에 표시할 곳들을 여러군데를 지정할수 있게 `MKMapItem` 객체가 들어있는 `NSArray` 로 받고 있다. `MKMapItem` 객체를 만들어 주기 위해서는 `MKPlacemark`객체를 먼저 만들어야 하는데, `MKPlacemark`는 위치 정보와 주소를 지정할 수 있다. 1~5번째 줄이 `MKPlacemark` 를 생성하는 부분인데 주소 지정하는 부분은 빼도 된다. </span>

<span style="font-size: 11pt;">실행옵션에서 중요한 부분은 길찾기 모드로 지정하는 부분이다. 9~11번째 줄이 해당하는 부분인데,  `MKLaunchOptionsDirectionsModeKey` 를 키로 지정해야하고, (다양한 키가 있으니 애플 레퍼런스에서 확인해 보면 된다.) 도보로 가는 경우와 차로 가는 경우를 값으로 설정할 수 있다. 위의 코드는 차를 타고 가는 경우를 지정한 것이다. </span>

<span style="font-size: 11pt;">실행해 보면 아래와 같은 화면을 볼수 있다. 알수없는 위치라고 나오는 이유는 위의 코드에서 주소를 nil 로 넣었기 때문이다. 사실 그 부분은 역지오코딩을 사용해야 한다. 그 부분은 알아서 하심이 ^^ </span>

<span style="font-size: 11pt;">  
</span>

<figure class="wp-caption aligncenter" style="width: 400px">![](http://ash84.net/wp-content/uploads/1/cfile1.uf.245B744F528409820CDD78.jpg)<figcaption class="wp-caption-text">요론 길찾기가 가능. </figcaption></figure>

<span style="font-size: 11pt;">  
</span>

**<span style="font-size: 11pt;">2013.11.18 addressDictionary</span><span style="font-size: 11pt;"> 추가 관련</span>**

<span style="font-size: 11pt;">– 추가하는 부분으로 위의 ‘알수 없는위치’ 부분을 주소로 지정을 하려면 단순히 주소 문자열을 대입시키는 것인 아니라 `NSDictionary` 로 만들어서 `MKPlaceMark` 생성시 전달해 줘야 한다. 이 부분에서 키로 들어가야 하는 부분은 아이폰 주소록 관련 부분에서 ‘Address propery’ 에 키 부분을 참고해야 하는데, 해당 지정시, 아래와 같이 지정하면 된다. 모든 키를 다 지정할 필요는 없고 그 중에서 하나만 지정하면 된다. 필자의 경우에는 street 으로해서 역지오코딩된 값을 전달해 주었다. </span>

<script src="https://gist.github.com/AhnSeongHyun/7523451.js"></script>

 



