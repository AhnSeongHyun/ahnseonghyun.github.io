---
title: '[JAVA] MD5 + 자릿수'
author: 'ash84'
pub_date: '2017-03-24'
description: ''
featured_image: ''
tags: ['dev', 'Java', 'MD5', 'MD5 자릿수', '자바', '자바 MD5 자릿수']
---


<div></div><div style="line-height: 2; "><div style="text-align: justify; line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">최근에 해쉬테이블의 키 값을 만들기 위해서 입력 문자열에 대한 MD5를 추출하는 자바 소스를 인터넷에서 구했는데, 입력 문자열에 따라서 MD5 로 추출되는 자릿수가 달라서 해쉬테이블의 키 값으로 쓰기에는 조금 불편한 점이 있어서 자릿수 맞추는 부분을 추가하였다. 코드는 간단하다. 해당 클래스 객체를 만들고 자릿수를 지정해 주면 알아서 채우거나 빼준다. 빼는 것은 뒷 자리부터 빼고, 채우는 것은 0~9 까지의 랜덤함수를 통해서 채우도록 하였다. 키 값이 100% 겹치지 않는다고 단언 할 수는 없지만, 테스트 단계에서는 쓸만할듯. </span></span></div><div style="text-align: justify; line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">  
</span></span></div><script src="https://gist.github.com/3202549.js"></script>

</div>

