---
title: '[iOS]HTML 파싱 - HTMLParser 를 이용하기, more fast'
author: 'ash84'
pub_date: '2012-09-24'
description: '한우찾기 관련 포스트에서 밝힌적이 있듯이, HTML 파싱을 핵심으로 하고 있는 한우찾기의 라이브러리화 작업이 한창 진행중이다. 이전의[ HTML 파싱 포스팅](http://ash84.tistory.com/697)'
featured_image: ''
tags: ['dev', 'html', 'HTML Parsing', 'HTMLNode', 'HtmlParser', 'ios html parsing', 'iOS', '파싱']
---
<span style="font-size: 11pt; "><span style="color: rgb(0, 0, 0); ">한우찾기 관련 포스트에서 밝힌적이 있듯이, HTML 파싱을 핵심으로 하고 있는 한우찾기의 라이</span><span style="color: rgb(0, 0, 0); ">브러리화 작업이 한창 진행중이다. 이전의</span>[<span style="color: rgb(0, 0, 0); "> HTML 파싱 포스팅</span>](http://ash84.tistory.com/697)<span style="color: rgb(0, 0, 0); ">에서 기존의 잘 알려진 </span>[<span style="color: rgb(0, 0, 0); ">TFHpple 을 이용하는 방식(XPath)</span>](http://printf.egloos.com/1930529)<span style="color: rgb(0, 0, 0); "> 외에도 자바 스크립트와 UIWebView를 이용하는 방식을 사용했다고 밝힌 적이 있다. </span></span>

<span style="font-size: 11pt; "><span style="color: rgb(0, 0, 0); ">HTML 파싱의 속도는 기본적으로 사용자가 느끼기에는 </span>**<span style="color: rgb(0, 0, 0); ">네트워크 속도</span>**<span style="color: rgb(0, 0, 0); ">에 달려있다고 본다. 즉, 출근길 지하철 안 3G네트워크상에서는 느리게 나올수 밖에 없고, 집에서 와이파이 연결해서 사용할때는 빨리 나올수 밖에 없다. 체감적으로 말이다. 이런 네트워크 속도를 제외하고 빠르게 할 수 있는 부분이 바로 파싱 라이브러리의 성능 부분이라고 할수 있겠다. </span></span>

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">  
</span>

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">필자가 이전에 사용한 [자바스크립](http://ash84.tistory.com/697) [+](http://ash84.tistory.com/697) [UIWebView ](http://ash84.tistory.com/697) [방식](http://ash84.tistory.com/697)에서 속도는 기본적으로 애플의 UIWebView의 자바스크립트 처리 속도에 달려있다. 그러나 아쉽게도 UIWebView는 아이폰의 사파리보다 느리다고 하며, 어떤 외국 포스팅에서는 기본적인 브라우저를 Chrome(크롬)으로 지정할수(프로그래밍적으로) 있다고 하는데 모든 유저가 크롬을 설치한다는 보장이 없기 때문에 현실적으로 어렵다.</span>

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">  
</span>

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">그래서 다양한 HTML 파싱 관련 라이브러리를 찾아보다가 최근에 테스트까지 마친 라이브러리가 있어서 하나 소개하려고 한다. **[HTMLParser](https://github.com/zootreeves/Objective-C-HMTL-Parser)** 라는 라이브러리인데, **[Ben Reeves](https://github.com/zootreeves)** 라는 분이 만든 라이브러리이다.</span>

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">일단 github 의 [Objective-C-HTML-Parser 링크](https://github.com/zootreeves/Objective-C-HMTL-Parser)에 가서 HTMLPase</span><span style="background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); font-size: 11pt; ">r.h, H</span><span style="font-size: 11pt; color: rgb(0, 0, 0); ">TMLParser.m, HTMLNode.h, HTMLNode.m 4개의 파일을 다운 받도록 하자. 해당 github 에도 사용법이 있으니 한번 보도록 하자. 다음과 같이 추가할때는 **반드시 copy 체크와 target 체크**를 하도록 하자. (이거 안하면 나중에 사용할때 요상한 에러가 난다.)</span>

![](http://ash84.net/wp-content/uploads/1/cfile10.uf.162BEA36505D82B10EEEA2.jpg)

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">그 다음에 반드시 해줘야 할일은 프로젝트 세팅에 들어가서 </span><font face="Helvetica, arial, freesans, clean, sans-serif" style="line-height: 2; "><span style="font-size: 11pt; line-height: 22px; color: rgb(0, 0, 0); ">“header search paths” 부분에 </span></font><font face="Helvetica, arial, freesans, clean, sans-serif"><span style="font-size: 11pt; line-height: 22px; color: rgb(0, 0, 0); "> </span></font><span style="font-family: Helvetica, arial, freesans, clean, sans-serif; font-size: 11pt; line-height: 22px; color: rgb(0, 0, 0); ">/usr/include/libxml2 라고 입력해 준다. </span>

<span style="font-family: Helvetica, arial, freesans, clean, sans-serif; font-size: 11pt; line-height: 22px; color: rgb(0, 0, 0); ">  
</span>

![](http://ash84.net/wp-content/uploads/1/cfile8.uf.144FB642505D83080DC8B6.jpg)

<span style="color: rgb(0, 0, 0); font-family: Helvetica, arial, freesans, clean, sans-serif; font-size: 11pt; line-height: 22px; ">  
</span>

<span style="color: rgb(0, 0, 0); font-family: Helvetica, arial, freesans, clean, sans-serif; font-size: 11pt; line-height: 22px; ">그리고 libxml2를 다음과 같이 프레임워크에 추가해주자.</span>

![](http://ash84.net/wp-content/uploads/1/cfile10.uf.1164FB38505D835B165AC7.jpg)

<span style="color: rgb(0, 0, 0); font-size: 11pt; line-height: 2; ">  
</span>

<span style="color: rgb(0, 0, 0); font-size: 11pt; line-height: 2; ">**자, 이제 코드에 적용해 보자.**</span>

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">그리고 나서 사용할 클래스의 헤더파일에서 두 import 문을 사용하도록 하자. </span>

<script src="https://gist.github.com/3765649.js"></script>

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">다음과 같이 HTMLParser 객체를 생성하는데 파싱하려는 HTML 문자열 초기화 문자열로 준다. 그리고 나서 parser 객체에서 파싱하려는 노드를 가져온다. 여기에서는 당연히 body 노드를 가져온다. </span>

<script src="https://gist.github.com/3765655.js"></script>  
  
<script src="https://gist.github.com/3765659.js"></script>

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">바로 위의 코드를 보면 HTMLParser 에서 HTMLNode 로 반환할 수 있는 것은 총 4가지의 doc, body, html, head 이다. 때문에 파싱하려는 대상에 따라서 반환해서 사용하면 된다. body 노드를 반환했고, HTMLNode 클래스의 bodyNode로 받아 왔다. </span>

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">가져온 bodyNode 안에 있는 자식 노드들을 찾는 코드는 다음과 같다. 필자는 태그(tag) 이름으로 찾아오는 부분이 필요했기 때문에 findChildTags 함수를 이용해서, “td” 태그를 다 찾아오기로 했다. </span>

<script src="https://gist.github.com/3765661.js"></script>

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">HTMLNode 클래스에서는 이 함수 외에도, 클래스 이름과 속성(attribute)로도 찾을 수 있는 findChildrenWithAttribute, findChildrenOfClass 등의 함수가 있다. 또한 이런 접근 외에도 nextSibling, previousSibling 등 노드간의 이동을 위한 함수들도 제공하고 있다. 때문에 좀더 상세하게 HTMLNode 에 접근이 필요한 엔지니어라면, 해당 함수들을 사용하는것이 좋겠다. </span>

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">이제 태그이름이 td가 들어간 모든 html 부분을 다 가져왔다. 이제 그 안에서 내가 필요한 값 들을 꺼내오자. 값은 다양한 방법으로 꺼내 올 수가 있다. <td class=”fir”>2007-11-24</td> 이런 html 이 있다고 하면 contents, allContents, rawContents 로 꺼내올수 있다. </span>

<script src="https://gist.github.com/3765713.js"></script>

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">함수 이름에서도 알듯이 rawContents 를 호출하면, html이 그대로 출력된다. contents 를 호출하면 2007-11-24 라는 값이 나온다. allContents 를 호출하면, 2007-11-24 라는 값이 나온다. contents와 allContents 의 차이는 중첩된 html 문에서 차이가 난다. </span>

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">자, 값을 가져와야 하는 부분이 이렇다고 하자. <td><span class=”vol1″>00889384</span></td> 이 부분에서 contents 를 호출하면 아무것도 나오지 않지만, allContents 를 호출하면 00889384 가 출력이 된다. 그 이유는 contents 함수와 allContents 함수를 보면 차이를 알 수 있다. </span>

<script src="https://gist.github.com/3765723.js"></script>

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">contents 함수를 보면, 현재 노드의 자식노드가 있고, 해당 노드가 xml의 content에 해당하면 NSString 으로 변환해서 출력하고 있고, 그게 아니면 nil을 반환한다. 그에반해, allContents 함수는 현재 노드에서 xml content 를 찾도록 한 뒤에 있으면 반환하도록 되어 있다. </span>

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">이런 값을 가져오는 함수 외에도 className, tagName, nodetype 등을 가져올 수 있다. 어떻게 쓰느냐는 사용하는 엔지니어의 목적에 따라 다를것이다. 좀더 HTMLParser에 대해서 궁금하다면, 개인적으로 코드를 한번 살펴보기를 권장하는 바이다. 생각보다 어렵지 않은 소스코드이고 고작 2개의 클래스 밖에 안되니 때문에 금방 볼 수 있다. </span>

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">성능에 대한 이야기를 안 할 수가 없다. 굳이 성능에서의 이유가 아니라면 좀더 쓰기 편한 자바스크립트 방식을 쓰지 않을 필요가 없다. 총 14개의 이력조회 코드를 테스트로 했으며, 검색버튼을 눌러서 UI가 뜨기전 즉, 데이터 가져올때 까지의 시간을 측정하였다. (좀 더 많은양의 테스트는 추후에 할 예정)</span>

![](http://ash84.net/wp-content/uploads/1/cfile5.uf.1243B533505D8CA01F1523.jpg)

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">보시는 바와 같이 약 2배의 성능차이를 보이고 있다. 조금 더 테스트를 해 봐야 성능 테스트에 대한 신뢰성이 높아지겠지만, 일단 14개의 이력코드로 테스트한 결과는 이렇다. HTMLParser가 반드시 좋다라고는 말할 수 없다. 왜냐하면, 테스트 역시 충분하게 이루어지지 못했을 뿐만 아니라, 다른 형식의 HTML 이라면 또 다른 결과를 보일수 있을 것이다. 다시 한번 말하지만 이 결과는 특정 사이트의 HTML 에만 제한된 것입을 다시한번 중요하게 말한다. </span>

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">자 이제, iOS에서의 HTML파싱에 대해서 한번 나름대로의 정리를 하자면, </span>

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">HTMLParser 방식이 TFHpple 보다 장점으로 생각되는것은 xpath는 딱 한 부분에 대해서 바로 접근할 수 있다는 장점이 있지만,  아쉽게도 TFHpple 에서는 nextSibling 등과 같이 다음 노드, 이전노드 등의 이동을 제공하지는 않는다. 때문에 그러한 접근이 필요하다면 HTMLParser 를 권장해 드리고 싶다. </span>

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">JavaScript+UIWebView 방식은 html의 id로 바로 접근할 수 있는 부분을 파싱해야 한다면 이 방식을 사용하는 것도 나쁘지 않다고 생각한다. 필자 역시 id로 계속 접근 할 수 있다면 이 방식을 고수하겠지만, 아쉽게도 html 안에 테이블을 사용하는 경우에는 이 방식은 좀 불안정 하다고 생각된다. </span>

<span style="font-size: 11pt; color: rgb(0, 0, 0); ">XPath로 접근이 가능하고, Xpath 경로가 변하지 않는다면, TFHpple 를 사용하길 바란다. 현재 한우찾기 앱에서 다른 부분의 데이터소스를 가져올때 사용하고 있는데 생각보다 편하다. 그러나 앞에서의 가정처럼 html 의 형식에 xpath 는 기본적으로 민감한 치명적 단점을 가지고 있기 떄문에 그 부분을 유의해야 할 것이다.  </span>



