---
title: '(iOS) MkMapView 기본 마커 및 CLGeocoder 이용하기'
author: 'ash84'
pub_date: '2013-09-05'
description: '아래의 코드는 사실은 리스트뷰에서 어떤 아이템을 선택했을때 발생하는 delegate 함수에서 동작하는 코드이다. 간단한데, 선택한 아이템은 기본적으로 위도와 경도를 가지고 있고 아래의 코드에서 하는 일은 누르면 해당 위도와 경도에 해당하는 주소를 가져오고, 해당 위치에 기본 핀마커를 삽입하고, 지도를 해당 위치로 확대하는 작업을 한다.'
featured_image: ''
tags: ['CLGeocoder', 'dev', 'iOS Map', '위도 경도 주소변환', '지도 보여주기']
---


<span style="font-size: 11pt;">아래의 코드는 사실은 리스트뷰에서 어떤 아이템을 선택했을때 발생하는 delegate 함수에서 동작하는 코드이다. 간단한데, 선택한 아이템은 기본적으로 위도와 경도를 가지고 있고 아래의 코드에서 하는 일은 누르면 해당 위도와 경도에 해당하는 주소를 가져오고, 해당 위치에 기본 핀마커를 삽입하고, 지도를 해당 위치로 확대하는 작업을 한다. </span>

<script src="https://gist.github.com/AhnSeongHyun/6434056.js"></script>



