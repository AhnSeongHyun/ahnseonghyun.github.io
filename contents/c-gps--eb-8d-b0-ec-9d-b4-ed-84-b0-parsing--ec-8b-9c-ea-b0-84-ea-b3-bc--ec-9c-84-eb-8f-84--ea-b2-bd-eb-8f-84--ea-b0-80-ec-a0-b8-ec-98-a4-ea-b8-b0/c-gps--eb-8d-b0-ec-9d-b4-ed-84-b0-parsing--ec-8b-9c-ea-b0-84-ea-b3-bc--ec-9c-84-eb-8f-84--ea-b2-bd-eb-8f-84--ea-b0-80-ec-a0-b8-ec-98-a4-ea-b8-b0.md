---
title: '[C#] GPS 데이터 Parsing 시간과 위도 경도 가져오기'
author: 'ash84'
pub_date: '2025-01-25'
description: ''
featured_image: ''
tags: ['c#', 'dev', 'GPS', 'GPS 시간정보 가져오기', 'GPS 위도경도', 'Latitude', 'Longitude']
---

이번시간에는 GPS 정보를 가져오는 부분을 다루려고 합니다. 다들 알다시피 GPS는 보통 시리얼 통신을 통해서 Com Port로 들어오게 됩니다. 그런데 GPS라고 해서 Latitude와 Longitude가 바로 들어오는 것이 아니라 GPS NEMA 프로토콜의 형태로 들어오게 되고 그 프로토콜을 해석해서 Application에서 필요한 정보를 우리가 취득하면 되는것이겠지요.


GPS 시리얼 포트를 통해서 받는 법이라던지, NEMA 프로토콜 자체에 대해서 궁금하신 분은 밑의 포스팅을 참고해주시기 바랍니다.


[NEMA 프로토콜](https://ko.wikipedia.org/wiki/NMEA_0183)
 


## GPS NEMA Protocol 에서 시간, 위도, 경도 가져오기


아래의 ReadGPSData() 함수는 GPS Port를 연 후, 데이터가 들어오는 부분에 대해서 처리하는 부분입니다. SerialPort 클래스의 DataReceived 이벤트가 발생하게 되면 this.Invoke 를 호출하고 Invoke 대상이 ReadGPSData가 되는 것이지요.



GPS NEMA 프로토콜에는 여러 섹션이 있는 데 GPRMC는 들어온 GPS 데이터에 대한 요약본이라고 보시면 될것 같습니다. 그래서 여기서는 GPRMC를 대상으로 시간과 위도, 경도를 가져오는 방법을 설명하도록 하겠습니다.


## 시간 / 날짜 정보 가져오기


GPRMC 프로토콜에서 가장 중요한 부분은 바로 ‘A’ 라고 표시 되어 있는 부분입니다. A과 V값이 올수 있는데 A는 Valid, V는 Invalid 를 나타냅니다. 때문에 아래의 코드에서도 GPRMC를 추출한 후에 바로 다음에 하는것이 A인지 V인지를 체크하는 작업입니다. A이면 바로 시간과 위치, 경도를 구하게 되고 아니면 그냥 계속 데이터를 받아오게 됩니다.

134807.000 라고 써 있는 부분이 시간정보를 나타내는 부분입니다. NEMA 프로토콜에 대해서는 자세히 설명하지는 않겠지만, 꼭 한번 보시는것이 도움이 됩니다. 이 부분은 13시 48분 07.00 초(hhmmss.sss) 라는것을 나타내게 됩니다. 시간정보는 그리니치 천문대(GMT)를 기준으로 나타내기 때문에 우리나라의 경우 시(hour) 정보에 +9 를 해 줘야 맞는 시간이 됩니다.

날짜의 경우 110808 이라는 부분에 해당하는데 DDMMYY 형식이기 때문에 2008년 08월 11일이라는 것을 나타내고 있습니다. 날짜의 경우 뒷의 숫자만 나오기 때문에 +2000을 해줘야 합니다. 


**개발자 세트 구매하기** 🤟
<iframe src="https://coupa.ng/chcDbD" width="120" height="240" frameborder="0" scrolling="no" referrerpolicy="unsafe-url" browsingtopics></iframe>
<iframe src="https://coupa.ng/chcDdd" width="120" height="240" frameborder="0" scrolling="no" referrerpolicy="unsafe-url" browsingtopics></iframe>
<iframe src="https://coupa.ng/chcDdZ" width="120" height="240" frameborder="0" scrolling="no" referrerpolicy="unsafe-url" browsingtopics></iframe>


## 위도 / 경도 가져오기

위도, 경도 정보는 3732.6627,N,12701.3549,E 이 부분에 해당하는 부분입니다. 3732.6627 이 위도를 나타내고 12701.3549 이 경도를 나타내고 있습니다. 위도 37도 35.0079분, 경도 127도 1.6446분을 나타내고 있습니다. 프로토콜에서는 친절하게 데이터가 나오지 않기 때문에 받은 데이터를 가지고 Split 함수를 가지고 프로토콜 표를 보면서 추출해 내야 합니다. 

---

<script src="https://gist.github.com/3386234.js"></script>



<small>이 포스팅은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받습니다.</small>
