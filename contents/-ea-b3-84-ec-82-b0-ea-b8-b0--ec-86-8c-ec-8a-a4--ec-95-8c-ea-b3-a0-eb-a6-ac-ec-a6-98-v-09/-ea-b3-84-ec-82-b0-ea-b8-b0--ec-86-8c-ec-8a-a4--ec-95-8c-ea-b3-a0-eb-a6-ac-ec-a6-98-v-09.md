---
title: '계산기 소스 알고리즘 V 0.9'
author: 'ash84'
pub_date: '2007-08-04'
description: '계산기 프로그램은 어찌보면, 매우 간단하다고 생각 할수 있다. 그건, 기능 자체를 간단하다고 간주해 버리면 간단해 진다. 즉, 두수에 대한 사칙연산 만을 지원하는 경우에는 매우 간단하며, 정말 기초적인 부분(함수)으로 구현할수 있다.(물론 한 함수에 통으로 짤 수도 있다.)

그렇지만, 윈도우 계산기를 보면 알듯이, 계산기는 항계산이 기본적으로 되어야 한다. 항 계산 기능은 다음과 같다.'
featured_image: ''
tags: ['c#', 'dev', '계산기 알고리즘', '프로그래밍']
---


계산기 프로그램은 어찌보면, 매우 간단하다고 생각 할수 있다. 그건, 기능 자체를 간단하다고 간주해 버리면 간단해 진다. 즉, 두수에 대한 사칙연산 만을 지원하는 경우에는 매우 간단하며, 정말 기초적인 부분(함수)으로 구현할수 있다.(물론 한 함수에 통으로 짤 수도 있다.)

그렇지만, 윈도우 계산기를 보면 알듯이, 계산기는 항계산이 기본적으로 되어야 한다. 항 계산 기능은 다음과 같다.   
  

<table border="0" cellpadding="0" cellspacing="0" style="WIDTH: 371pt; BORDER-COLLAPSE: collapse" width="495">  
<colgroup>  
<col style="WIDTH: 43pt; mso-width-source: userset" width="57"></col>  
<col style="WIDTH: 28pt; mso-width-source: userset" width="37"></col>  
<col span="7" style="WIDTH: 43pt; mso-width-source: userset" width="57"></col>  
</colgroup><tbody>  
<tr height="39" style="HEIGHT: 29.2pt; mso-height-source: userset">  
<td class="oa1" height="39" style="WIDTH: 43pt; HEIGHT: 29.2pt" width="57">  
<span style="FONT-WEIGHT: bold; FONT-SIZE: 18pt; COLOR: #953735; FONT-FAMILY: '맑은 고딕'; language: en-US; mso-ascii-font-family: '맑은 고딕'; mso-color-index: 5; mso-font-kerning: 12.0pt">2</span><span style="FONT-WEIGHT: bold; FONT-SIZE: 18pt; COLOR: #953735; FONT-FAMILY: '맑은 고딕'; language: ko; mso-ascii-font-family: '맑은 고딕'; mso-color-index: 5; mso-font-kerning: 12.0pt"></span>

</td>  
<td class="oa1" style="WIDTH: 28pt" width="37">  
<span style="FONT-WEIGHT: bold; FONT-SIZE: 18pt; COLOR: #953735; FONT-FAMILY: '맑은 고딕'; language: en-US; mso-ascii-font-family: '맑은 고딕'; mso-color-index: 5; mso-font-kerning: 12.0pt">+</span><span style="FONT-WEIGHT: bold; FONT-SIZE: 18pt; COLOR: #953735; FONT-FAMILY: '맑은 고딕'; language: ko; mso-ascii-font-family: '맑은 고딕'; mso-color-index: 5; mso-font-kerning: 12.0pt"></span>

</td>  
<td class="oa1" style="WIDTH: 43pt" width="57">  
<span style="FONT-WEIGHT: bold; FONT-SIZE: 18pt; COLOR: #953735; FONT-FAMILY: '맑은 고딕'; language: en-US; mso-ascii-font-family: '맑은 고딕'; mso-color-index: 5; mso-font-kerning: 12.0pt">3</span><span style="FONT-WEIGHT: bold; FONT-SIZE: 18pt; COLOR: #953735; FONT-FAMILY: '맑은 고딕'; language: ko; mso-ascii-font-family: '맑은 고딕'; mso-color-index: 5; mso-font-kerning: 12.0pt"></span>

</td>  
<td class="oa1" style="WIDTH: 43pt" width="57">  
<span style="FONT-WEIGHT: bold; FONT-SIZE: 18pt; COLOR: #953735; FONT-FAMILY: '맑은 고딕'; language: en-US; mso-ascii-font-family: '맑은 고딕'; mso-color-index: 5; mso-font-kerning: 12.0pt">*</span><span style="FONT-WEIGHT: bold; FONT-SIZE: 18pt; COLOR: #953735; FONT-FAMILY: '맑은 고딕'; language: ko; mso-ascii-font-family: '맑은 고딕'; mso-color-index: 5; mso-font-kerning: 12.0pt"></span>

</td>  
<td class="oa1" style="WIDTH: 43pt" width="57">  
<span style="FONT-WEIGHT: bold; FONT-SIZE: 18pt; COLOR: #953735; FONT-FAMILY: '맑은 고딕'; language: en-US; mso-ascii-font-family: '맑은 고딕'; mso-color-index: 5; mso-font-kerning: 12.0pt">12</span><span style="FONT-WEIGHT: bold; FONT-SIZE: 18pt; COLOR: #953735; FONT-FAMILY: '맑은 고딕'; language: ko; mso-ascii-font-family: '맑은 고딕'; mso-color-index: 5; mso-font-kerning: 12.0pt"></span>

</td>  
<td class="oa1" style="WIDTH: 43pt" width="57">  
<span style="FONT-WEIGHT: bold; FONT-SIZE: 18pt; COLOR: #953735; FONT-FAMILY: '맑은 고딕'; language: en-US; mso-ascii-font-family: '맑은 고딕'; mso-color-index: 5; mso-font-kerning: 12.0pt">+</span><span style="FONT-WEIGHT: bold; FONT-SIZE: 18pt; COLOR: #953735; FONT-FAMILY: '맑은 고딕'; language: ko; mso-ascii-font-family: '맑은 고딕'; mso-color-index: 5; mso-font-kerning: 12.0pt"></span>

</td>  
<td class="oa1" style="WIDTH: 43pt" width="57">  
<span style="FONT-WEIGHT: bold; FONT-SIZE: 18pt; COLOR: #953735; FONT-FAMILY: '맑은 고딕'; language: en-US; mso-ascii-font-family: '맑은 고딕'; mso-color-index: 5; mso-font-kerning: 12.0pt">2</span><span style="FONT-WEIGHT: bold; FONT-SIZE: 18pt; COLOR: #953735; FONT-FAMILY: '맑은 고딕'; language: ko; mso-ascii-font-family: '맑은 고딕'; mso-color-index: 5; mso-font-kerning: 12.0pt"></span>

</td>  
<td class="oa1" style="WIDTH: 43pt" width="57">  
<span style="FONT-WEIGHT: bold; FONT-SIZE: 18pt; COLOR: #953735; FONT-FAMILY: '맑은 고딕'; language: en-US; mso-ascii-font-family: '맑은 고딕'; mso-color-index: 5; mso-font-kerning: 12.0pt">*</span><span style="FONT-WEIGHT: bold; FONT-SIZE: 18pt; COLOR: #953735; FONT-FAMILY: '맑은 고딕'; language: ko; mso-ascii-font-family: '맑은 고딕'; mso-color-index: 5; mso-font-kerning: 12.0pt"></span>

</td>  
<td class="oa1" style="WIDTH: 43pt" width="57">  
<span style="FONT-WEIGHT: bold; FONT-SIZE: 18pt; COLOR: #953735; FONT-FAMILY: '맑은 고딕'; language: en-US; mso-ascii-font-family: '맑은 고딕'; mso-color-index: 5; mso-font-kerning: 12.0pt">1</span><span style="FONT-WEIGHT: bold; FONT-SIZE: 18pt; COLOR: #953735; FONT-FAMILY: '맑은 고딕'; language: ko; mso-ascii-font-family: '맑은 고딕'; mso-color-index: 5; mso-font-kerning: 12.0pt"></span>

</td></tr></tbody></table>  
 이런 식을 계산 한다고 했을때, 앞에서 부터 계산을 한다면, 결과 값은 62가 되어야 하겠지만 정답은 40 이다. 왜냐하면, 당연히 더하기와 뺄셈 보다 나눗셈과 곱셈의 우선순위가 높기 때문이다. 그렇기 때문에 먼저 곱셈과 나눗셈을 먼저 계산 해야 한다. ![사용자 삽입 이미지](http://ash84.net/wp-content/uploads/1/fl100.jpg)  
 위와 같은 방식으로 해결하는 알고리즘을 짯다. 기본 개념을 설명하자면, 곱셈과 나눗셈을 먼저 처리하고 맨 나중에 더하기와 뺄셈만 남게 해서 연산을 수행하는 방식이다. 연산이 이루어지는 시점은 크게 2가지로 볼수 있다.

<div style="PADDING-RIGHT: 10px; PADDING-LEFT: 10px; PADDING-BOTTOM: 10px; PADDING-TOP: 10px; BACKGROUND-COLOR: #faffa9">1. “=”을 눌렀을때.  
   – 전체 계산 식에 대한 연산이 이루어 져야 한다. 2. 특정 연산자를 눌렀을때.   
    –  첫번째 연산자 이후 부터는 방금 누른 연산자 이전의 계산식에 대한 연산을 수행해  
       야 하며, 연산을 보여주어야 한다

ex)  “*” 를 누르면, 2+3 이 계산되어서 보여져야 하고,   
        “+”를 누르면, 2+3*12 를 연산자 우선 순위에 맞게 계산 되어야 한다.

</div>  
 즉, 버튼이나 입력이 있을때 마다, ArrayList(C#) 에 넣어서 연산자를 누를때(1번이후) 마다 이전의 계산식을 연산하는 방식이다. 곱셈과 나눗셈을 없애고 더하기와 빼기만으로 구성된 식이 나오면, 그것을 처리한다. 다음 연산에서 또 다시 곱셈과 나눗셈이 들어 간다면, 다시 처리를 반복 하게 된다. <div style="PADDING-RIGHT: 10px; PADDING-LEFT: 10px; PADDING-BOTTOM: 10px; PADDING-TOP: 10px; BACKGROUND-COLOR: #ffdaed">  
<font color="#d41a01">Version 0.9의 가장 큰 문제는  ( ) 괄호 처리가 안된다는 것이다. 입력 자체를 텍스트 박스로 받을려고 했지만, 괄호와 여러 계산 불가능한 문자의 처리가 귀찮아서 ReadOnly 설정으로 예외를 방지 했다. 그외에도 루트기능, 승의 기능, 진수 변환의 기능이 없기 때문에 version 2.0으로의 업그레이드에는 이런 기능들이 추가 하려고 한다. </font></div>

