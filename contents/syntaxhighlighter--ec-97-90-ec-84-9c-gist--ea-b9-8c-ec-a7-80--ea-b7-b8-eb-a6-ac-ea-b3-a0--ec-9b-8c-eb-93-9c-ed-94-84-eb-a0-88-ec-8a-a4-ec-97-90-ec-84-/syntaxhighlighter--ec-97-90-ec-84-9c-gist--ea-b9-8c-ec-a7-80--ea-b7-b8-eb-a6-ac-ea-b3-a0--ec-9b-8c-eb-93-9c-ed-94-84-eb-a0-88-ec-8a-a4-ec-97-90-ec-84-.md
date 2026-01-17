---
title: 'SyntaxHighlighter 에서 gist 까지, 그리고 워드프레스에서의 사용법'
author: 'ash84'
pub_date: '2012-08-22'
description: '예전에 블로그에 소스코드를 처음에 넣을때에는 주로 박스 안에 코드를 넣는 작업을 했었다. 그런데 이 작업의 가장 큰 단점은 언어별 syntax 하이라이팅을 보여주지 않는 다는 점이다. 말 그대로 텍스트니까. 그리고 나온것이 [SyntaxHighlighter](http://alexgorbatchev.com/SyntaxHighlighter/) 인데 자바스크립트를 이용해서  태그 속성에 class 이름'
featured_image: ''
tags: ['dev', 'gist', 'gisthub', 'syntaxhighlighter', 'blog', '워드프레스', '워드프레스 gist', 'code-input']
---
<span style="font-size: 11pt; ">예전에 블로그에 소스코드를 처음에 넣을때에는 주로 박스 안에 코드를 넣는 작업을 했었다. 그런데 이 작업의 가장 큰 단점은 언어별 syntax 하이라이팅을 보여주지 않는 다는 점이다. 말 그대로 텍스트니까. 그리고 나온것이 [SyntaxHighlighter](http://alexgorbatchev.com/SyntaxHighlighter/) 인데 자바스크립트를 이용해서 <pre> 태그 속성에</span><span style="font-size: 11pt; "> class 이름에 java, cpp 처럼 프로그래밍 언어를 입력하고 <pre> 태그 안에 코드를 입력하면 해당 언어의 문법에 맞게 보여주는 방식이었다. </span>

![](http://ash84.net/wp-content/uploads/1/cfile8.uf.203CF04B50306E6A0748F4.jpg)

<span style="font-size: 11pt; ">[SyntaxHighlighter](http://alexgorbatchev.com/SyntaxHighlighter/) 는 혁신적이었지만, 버전이 올라가면서 여러가지 버그아닌 버그들이 있었다.(크롬에서 이상하던데) 그리고 결정적으로 블로그가 날아가면 코드역시 날아간다는 점이 좀 아쉬운 부분이라고 하겠다. </span>

<span style="font-size: 11pt; ">그래서 필자가 최근에 사용하는 것은 [github](https://github.com/) 의 [gist](https://gist.github.com/) 이다. github 야 이제 명실상부 오픈소스 저장소</span><span style="font-size: 11pt; ">의 탑3 진입을 목전에 두고 있는 탄탄한 회사인데, <span style="color: rgb(204, 61, 61); ">gist 라는건 github 에서 제공하는 소스 코드 게시판 같은것이다.</span> 사용하는 것은 간단하다. github 에 가입되어 있다면 gist 에 들어가서 코드를 입력하고, 프로그래밍 언어를 선택하면 저장이 된다. 저장시에 private, public 을 선택 할 수 있는데 public 을 선택하면 블로그로 옮길수 있는 스크립트를 받을수 있다. </span>

<span style="font-size: 11pt; ">  
</span>

<figure class="wp-caption aligncenter" style="width: 640px">![](http://ash84.net/wp-content/uploads/1/cfile3.uf.11157C3850306F0D305A74.png)<figcaption class="wp-caption-text">심플함 그 자체다. </figcaption></figure>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">티스토리에서는 이 스크립트를 포스팅 작성시 우측 상단의 html 체크박스를 눌러준후 해당 위치에 입력해주면 된다. 한가지 유의할 점은 해당 코드는 포스팅 미리보기 시점에서는 나오지 않는 다는 점이다. 저장을 하면 그제서야 보인다. </span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; "></span>

![](http://ash84.net/wp-content/uploads/1/cfile1.uf.11397B465030710C1C9DA9.jpg)

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>

**문제는 워드프레스(word press). 최근에 코드 기반의 영어로 포스팅을 하는 블로그를 워드프레스에서 열었는데 문제는 티스토리와 같은 방식으로는 gist의 저장이 안된다는 것이다.**<span style="font-size: 11pt; line-height: 2; "> 워드프레스는 인터네셔널한데 안될리가 없다고 생각하고 있어서 구글링을 했는데 다음과 같은 링크를 찾았다. </span>

<span style="font-size: 11pt; ">[워드프레스에서 gist 사용하기 ](http://en.forums.wordpress.com/topic/github-gist-shortcode?replies=50)</span>

<span style="font-size: 11pt; ">즉, 워드프레스 닷컴에서는 입력창 자체가 html 과 혼재해서 쓸수 있는 형태인데 티스토리에서 처럼 스크립트 코드를 붙이는 것이 아니라, 다음과 같이 gist 고유번호를 쓰면 된다는 것이다. gist 고유 번호는 코드를 하나 저장할때 마다 부여되는 고유의 ID와 같은 것이라고 보면 된다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; "><span style="font-size: 11pt; line-height: 2; ">[wpgist 3202549]</span>

<span style="font-size: 11pt; "> or </span>

<span style="font-size: 11pt; ">[wpgist https://gist.github.com/</span><span style="font-size: 11pt; ">3202549]</span>

</div><span style="font-size: 11pt; ">위와 같이 입력하면 워드프레스에서도 gist 에 입력한 코드화면을 볼 수가 있다. 워드프레스를 사용하시는 분이라면 위의 방법을 숙지하셔야 한다. 필자 역시 아직 숙지가 되지 않아서 이렇게 정리하는.. ㅎㅎ</span>

<figure class="wp-caption aligncenter" style="width: 640px">![](http://ash84.net/wp-content/uploads/1/cfile30.uf.2073813750306FD213DBF0.png)<figcaption class="wp-caption-text">워드프레스에서의 입력화면</figcaption></figure>

<span style="font-size: 11pt; ">**gist 에 대해서 살펴보았는데, gist 역시 만능은 아니다.** SyntaxHighlighter 의 가장 큰 장점이라면 코드를 블로그에 이쁘게 보여주면서도 동시에 블로그에 들어와서 보고 있는 사용자가 언제든지 클릭 한번으로 코드를 복사해 갈수 있다는 장점이 있다. </span>

<span style="font-size: 11pt; ">그에 비해서** gist 는 원클릭 복사 기능을 제공하고 있지는 않다. **그 부분이 좀 아쉽긴 하지만 gist 의 가장 큰 장점이라면 단연 github 의 본인 계정에 저장/관리가 된다는 점이라고 할 수 있다. 코드라는게 늘 그렇듯 언젠가 꼭 필요한 시점이 있기 때</span><span style="font-size: 11pt; ">문에 잘 관리 할수 있다면 괜찮은것 같다. </span>

<span style="font-size: 11pt; ">각자 본인에게 맞는것으로 사용하면 좋을것 같다. ^^ </span>



