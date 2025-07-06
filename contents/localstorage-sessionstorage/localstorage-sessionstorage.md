---
title: 'LocalStorage & SessionStorage'
author: 'ash84'
pub_date: '2018-05-31'
description: '#### 개요

 

HTML5 에서 제공하는 클라이언트 데이터를 저장하는 2개의 객체,  
 – 하나의 세션단위로 데이터를 저장하는 SessionStorage  
 – 만료 기간이 없는 LocalStorage

둘다 모두 key, value 로 저장한다는 것과 도메인별로 나눠진다는 부분에서 cookie와 닮아 있다. 둘다 cookie와 다르게 expire 를 지정할 수 없다는 단점과 함께 장점은 문자열이 아닌 객체도 저장이 가능하다는점,

cookie는 최대 20개까지 저장이 되지만(사이트 당), 5MB 라는 크기를 활용할 수'
featured_image: 'https://images.unsplash.com/photo-1414509902153-26bed16bc962?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=511fa809144285f1e89eda78d8068096&auto=format&fit=crop&w=1350&q=80'
tags: ['dev', 'LocalStorage', 'SessionStorage', '로컬스토리지', '세션스토리지']
---


#### 개요

 

HTML5 에서 제공하는 클라이언트 데이터를 저장하는 2개의 객체,  
 – 하나의 세션단위로 데이터를 저장하는 SessionStorage  
 – 만료 기간이 없는 LocalStorage

둘다 모두 key, value 로 저장한다는 것과 도메인별로 나눠진다는 부분에서 cookie와 닮아 있다. 둘다 cookie와 다르게 expire 를 지정할 수 없다는 단점과 함께 장점은 문자열이 아닌 객체도 저장이 가능하다는점,

cookie는 최대 20개까지 저장이 되지만(사이트 당), 5MB 라는 크기를 활용할 수 있다는점, cookie와 다르게 서버로 전송되지 않는다는 장점을 가지고 있다.

지원하는 브라우저는 다음과 같다.

[![image2015-5-26 11-0-53](https://farm9.staticflickr.com/8813/17958475660_9a080915a9_z.jpg)](https://flic.kr/p/tmVT9G)

#### LocalStorage

<script src="https://gist.github.com/AhnSeongHyun/31a790f31aaa828c4418.js"></script>– 주의할점은 절대 명시적/수동적으로 지우지 않는 이상 지워지지 않는다는 점이다. – 만료시간이나, 특정 조건에서의 값을 지우고 싶다면 개발자가 코드로 지워야 한다.(혹은 개발자 툴)

 

#### SessionStorage

<script src="https://gist.github.com/AhnSeongHyun/f69b3fbc4ec573820826.js"></script>

– 만료 시점에 유의해야 한다. 브라우저 종료 뿐만 아니라 브라우저 내에 탭을 생성하는 경우에도 별도의 영역으로 할당되어 서로의 영역을 침범하지 못한다.

#### References :

– [http://www.w3schools.com/html/html5_webstorage.asp](http://www.w3schools.com/html/html5_webstorage.asp)  
 – [http://m.mkexdev.net/59](http://m.mkexdev.net/59)



