---
title: '[C/C++] strlen() 과 String 클래스의 length()함수의 차이점.'
author: 'ash84'
pub_date: '2017-04-17'
description: '문자열의 갯수를 구하는 함수만큼 공통적으로 여러 언어에서 구현되어 있는 기능도 드문것 같습니다. 오늘 소개할 내용은 C++ 의  내에 있는 char * 형의 문자열의 갯수를 세어주는 `strlen()` 함수에 대해서 이야기 하려고 합니다. 제목처럼 일반적인 객체지향의 언어 자바나 C#의 String 클래스에서 사용하는 length() 함수와 어떻게 다른지 이야기 하려고 합니다. 물론 아시는 분들도 있겠지만.^^   

먼저 C++ 에서 사용하는 경우를 살펴볼까요? 대부분 다음과 같이 사용하겠지요.'
featured_image: ''
tags: ['c#', 'dev', 'Java', 'length()', 'String class', 'string.h', 'strlen']
---

문자열의 갯수를 구하는 함수만큼 공통적으로 여러 언어에서 구현되어 있는 기능도 드문것 같습니다. 오늘 소개할 내용은 C++ 의 <string.h> 내에 있는 char * 형의 문자열의 갯수를 세어주는 `strlen()` 함수에 대해서 이야기 하려고 합니다. 제목처럼 일반적인 객체지향의 언어 자바나 C#의 String 클래스에서 사용하는 length() 함수와 어떻게 다른지 이야기 하려고 합니다. 물론 아시는 분들도 있겠지만.^^   

먼저 C++ 에서 사용하는 경우를 살펴볼까요? 대부분 다음과 같이 사용하겠지요.

<script src="https://gist.github.com/3353781.js"></script>


count 는 얼마일까요? 당연히 3입니다. 그러면 자바에서 문자열의 길이를 가져오는  함수를 사용하는 경우를 볼까요? 이 경우에도 3이 나옵니다. 그러면 도데체 무엇이 다를까요? 여러분도 아시다 시피 영문자와 숫자는 각각 1byte를 소비하는것으로 알고 있습니다. 그러나 한글의 경우에 달라지지요. 즉 1byte 가 아니라, 2byte를 차지합니다. 

그러기 때문에, 
<br/>

C++
```
char * name = “김문수”;
int count = strlen(tom);
```
<br/>


JAVA

```
String name = “김문수”; 
System.out.println(name.length());
```

이 둘의 결과는 다르게 나옵니다. 위의 `strlen()` 함수의 경우에는 한글 3글자기 때문에 6byte. 즉 6이 나오게 되는 것입니다. 그러나, 자바의 경우에는 한글의 경우에도 영어와 마찬가지로 3이 나오게 됩니다. 


C++에서 사용하기 `strlen()` 함수의 경우에는 현재 검사 대상인 char * 포인트가 가리키는 곳의 사용 바이트 수를 체크합니다. 때문에 한글의 경우, 2byte 이기 때문에 길이가 다르게 나오는 것이고, 자바에서는 `length()` 함수에서 하는 일은 말 그대로 글자수를 체크해 주는 것입니다.  

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- ash84.net_링크광고 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="8167194879"
     data-ad-format="link"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>

최근에 알게된 사실은 외국의 문자에서는 3바이트 짜리 문자도 있다고 하더군요. 사실 자바 개발자 분들이나 혹은 다른 개발자 분들이 strlen()을 쓰실때 그렇게 길이라고 생각하고 쓰실수도 있지만, 더 큰 문제는 다양한 개발자들이 개발해 놓은 소스코드 내에서 `strlen()` 함수가 랩핑되어져서 `length()` 처럼 표현되었을 경우, 혼란을 가져올수 있다는 것입니다.  또 다른 문제는 사실상 다국어에 대한 처리가 없다면 상관이 없지만 혼합되 문자열의 처리의 경우 strlen()만으로 글자수를 체크한 다는 것은 조금은 버거운 일이 아닌가 하는 생각이 들었습니다.  
