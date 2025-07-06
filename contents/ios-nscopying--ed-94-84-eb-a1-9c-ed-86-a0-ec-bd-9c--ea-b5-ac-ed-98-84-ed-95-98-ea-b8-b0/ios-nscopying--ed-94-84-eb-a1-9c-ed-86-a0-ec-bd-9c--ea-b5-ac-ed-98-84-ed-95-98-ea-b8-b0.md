---
title: '(iOS) NSCopying 프로토콜 구현하기'
author: 'ash84'
pub_date: '2015-07-03'
description: '어떤 사용자 정의 클래스의 객체 자체를 copy 해야하는 경우가 있다. 그럴때 사용하는 것이 `NSCopying` 프로토콜이다. 객체를 복사할때는 `'
featured_image: ''
tags: ['deepcopy', 'dev', 'IOS', 'NSCopying', 'NSZONE']
---


<span style="font-size: 11pt;">어떤 사용자 정의 클래스의 객체 자체를 copy 해야하는 경우가 있다. 그럴때 사용하는 것이 </span>`<code style="font-size: 9pt; line-height: 1.5;"><span style="font-size: 11pt;">NSCopying</span>`<span style="font-size: 11pt;"> 프로토콜이다. 객체를 복사할때는 </span>`<code style="font-size: 9pt; line-height: 1.5;"><span style="font-size: 11pt;">copy</span>`<span style="font-size: 11pt;"> 메소드를 사용하면 되는데, 실제로 </span>`<code style="font-size: 9pt; line-height: 1.5;"><span style="font-size: 11pt;">copy</span>`<span style="font-size: 11pt;"> 메소드가 복사를 수행하는 것이 아니라 </span><copy style="font-size: 9pt; line-height: 1.5;"><span style="font-size: 11pt;">`copywithzone:`</span></copy><span style="font-size: 11pt;"> 메소드가 수행하는 것이다. </span>

<div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">cocoa 프레임워크에서 제공하는 클래스들을 보면 NSCopying 프로토콜을 구현하고 있는 것을 레퍼런스 문서를 보면 알수가 있다. 아래의 그림은 </span>`<span style="font-size: 11pt;">NSDictionary</span>`<span style="font-size: 11pt;">, </span>`<span style="font-size: 11pt;">NSString</span>`<span style="font-size: 11pt;"> 의 레퍼런스 문서의 첫 부분인데, 모두 `NSCopying` 프로토콜을 내부적으로 따르고 있다고 설명하고 있다.</span></div>![](http://ash84.net/wp-content/uploads/1/cfile5.uf.231FBA44528DAAED034C20.png)

![](http://ash84.net/wp-content/uploads/1/cfile7.uf.2258AD44528DAAEE207339.png)

<span style="font-size: 11pt;">때문의 아래의 코드가 가능한 것이다. </span>

<span style="font-size: 11pt;">  
</span>

<script src="https://gist.github.com/AhnSeongHyun/7576993.js"></script><span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">  
 그렇지만 내가 만든 클래스는 어떨까? 만약 `copyWithZone:` 메소드를 구현하지 않은채 copy 를 수행하게 되면 에러가 발생이 된다. 아래의 경우는 Reqeust 라는 클래스를 만들고 data 라는 `NSString` 형의 변수를 가지고 있었지만 `copy` 함수 테스트 시, 에러를 발생하는 것을 확인할 수 있었다.</span>

<div><span style="font-size: 11pt;">  
</span><script src="https://gist.github.com/AhnSeongHyun/7577015.js"></script><span style="font-size: 11pt;">  
</span>  
<span style="font-size: 11pt;">  
</span><div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">Terminating app due to uncaught exception ‘NSInvalidArgumentException’, reason: ‘-[Request copyWithZone:]: unrecognized selector sent to instance</span>

</div><span style="font-size: 11pt;">  
 요지는 `NSCopying` 프로토콜을 구현해야한다는 것이고 `copyWithZone:` 메소드를 구현해야 한다. Request 클래스에 몇가지 변수를 더 추가해 보았다. dataSize 라는 int 형 변수를 추가하고 `copyWithZone:` 함수를 아래와 같이 작성하였다.  
</span>

<span style="font-size: 11pt;">  
</span>  
<span style="font-size: 11pt;">  
</span><script src="https://gist.github.com/AhnSeongHyun/7577031.js"></script>

<span style="font-size: 11pt;">  
</span>  
<span style="font-size: 11pt;">  
 메소드를 보면, `NSStirng` 형은 원래 `NSCopying` 프로토콜을 지원하기 때문에 `copyWithZone:` 메소드를 사용해서 복사를 하고 있는데, 기본형인 int 의 경우에는 대입을 통해서 복사를 해주면 된다. </span>

<span style="font-size: 11pt;">  
</span>

</div><div style="line-height: 2;"><span style="font-size: 11pt;">**  
<span style="font-size: 11pt;">Reference:  
</span>**</span>  
<span style="font-size:11pt;">  
 – </span>[<span style="font-size: 11pt;">http://warmz.tistory.com/780</span>](http://warmz.tistory.com/780)<span style="font-size: 11pt;"></span>  
<span style="font-size:11pt;">  
 – </span>[<span style="font-size: 11pt;">http://warmz.tistory.com/779</span>](http://warmz.tistory.com/779)</div>

