---
title: 'A Mobile Care System with alert mechanism'
author: 'ash84'
pub_date: '2008-09-29'
description: '[](http://ash84.net/wp-content/uploads/1/48e0707f8ebe97H.pdf)48e0707f8ebe97H.pdf  
 특징'
featured_image: ''
tags: ['EMBS', 'gateway', 'healthcare', 'IEEE', 'mobile', 'role-based']
---


[](http://ash84.net/wp-content/uploads/1/48e0707f8ebe97H.pdf)48e0707f8ebe97H.pdf  
 특징

<div class="txc-textbox" style="BORDER-RIGHT: #fe8943 1px solid; PADDING-RIGHT: 10px; BORDER-TOP: #fe8943 1px solid; PADDING-LEFT: 10px; PADDING-BOTTOM: 10px; BORDER-LEFT: #fe8943 1px solid; PADDING-TOP: 10px; BORDER-BOTTOM: #fe8943 1px solid; BACKGROUND-COLOR: #fedec7">– 블루투스를 게이트웨이로 이용한다는 점에서 현재 우리 프로젝트와 유사  
 – 기기의 위치제약에 대해서 설명하고 있음.   
 – ECG와 혈압 데이터를 얻는 과정에서 획득 메카니즘이 다르기 때문에 다른 모듈로 개발 <font color="#c84205">– 모바일 폰이 블루투스로 데이터를 받아서 서버에 전달하는 방식  
</font>  
 – 이상 데이터가 발생시에 서버의 연락 함으로써, 자체적인 알람과 데이터 전송 용량을 줄일수 있다.

– 이상데이터시, 알람에 대해서는 응급의 레벨을 두어서 구분하고 있다.   
<font color="#c84205">– 각 환자에 대한 응급의 데이터 범위는, 환자의 주치의가 환자의 데이터를 보고 설정  
</font>  
 – 응급의 레벨에 따라서, 케어의 전략이 바뀌고, 케어의 전략에 따라서 의료진의 역할이 동적으로 할당되는 방식  
   (현재 우리나라에서는 시행의 어려움이 있음)

<font color="#c84205">– 혈압의 단계를 총 5단계로 구분하고 있다</font>

.- 평가 부분에서는 통신시의 데이터의 정확도와 시나리오 상의 Best Case, Worst Case를 두어서   
   Time Delay에 대해서 평가 하고 있음

</div>장점

<div class="txc-textbox" style="BORDER-RIGHT: #79a5e4 1px solid; PADDING-RIGHT: 10px; BORDER-TOP: #79a5e4 1px solid; PADDING-LEFT: 10px; PADDING-BOTTOM: 10px; BORDER-LEFT: #79a5e4 1px solid; PADDING-TOP: 10px; BORDER-BOTTOM: #79a5e4 1px solid; BACKGROUND-COLOR: #dbe8fb">  
 – 모바일 폰에서 개발함으로 써, 보다 일반적인 형태로 개발했다.  
 – 응급의 레벨을 나눔으로써, 알람으로 생기는 의료진 번거로움을 줄였다. – 각기 다른 역할과 그에 따른 우선 순위를 설정함으로써,   
   환자에게 적합한 의료서비스를 적절한 시점에 제공할 수 있다.

– 모바일 기기내에서 기본적인 이상데이터 추출과 응급상황 판단이 이루어진 다는 점에서 기존의 데이터 변환 및   
   위치 종속성을 해결하기 위해서 사용되었던 모바일 기기의 기능적 확장을 가져왔다.

</div>단점

<div class="txc-textbox" style="BORDER-RIGHT: #9fd331 1px solid; PADDING-RIGHT: 10px; BORDER-TOP: #9fd331 1px solid; PADDING-LEFT: 10px; PADDING-BOTTOM: 10px; BORDER-LEFT: #9fd331 1px solid; PADDING-TOP: 10px; BORDER-BOTTOM: #9fd331 1px solid; BACKGROUND-COLOR: #e7fdb5">– 상호 운용성의 문제에 대한 대처가 없음 <HL7>  
 – 실제 핸드폰 기능과 의료영역에 들어갔을때의 제어에 대한 부분이 명시되어 있지 않음. </div>

