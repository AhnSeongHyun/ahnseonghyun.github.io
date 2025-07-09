---
title: 'Python: Tips, Tricks and Idioms'
author: 'ash84'
pub_date: '2015-04-22'
description: '원문 : [Python: Tips, Tricks and Idioms](https://codefisher.org/catch/blog/2015/01/27/python-tips-tricks-and-idioms/?utm_source=Python+Weekly+Newsletter&utm_campaign=8416b188e6-Python_Weekly_Issue_176_January_29_2015&utm_medium=email&utm_term=0_9e26887fc5-8416b188e6-312692397 "Python: Tips, Tricks an'
featured_image: ''
tags: ['dev', 'performances', 'Python', 'tips', 'tricks']
---


원문 : [Python: Tips, Tricks and Idioms](https://codefisher.org/catch/blog/2015/01/27/python-tips-tricks-and-idioms/?utm_source=Python+Weekly+Newsletter&utm_campaign=8416b188e6-Python_Weekly_Issue_176_January_29_2015&utm_medium=email&utm_term=0_9e26887fc5-8416b188e6-312692397 "Python: Tips, Tricks and Idioms")

번역 까지는 아니고(번역할 내용도 별로 없기에.) 눈에 띄는 몇가지만 주관적인 의견을 붙여서 적어본다.

 

**enumerate**  
 – index 와 같이 출력하기 위해서 i 등의 변수를 ++ 하는 형태로 for문을 돌리지말고 enumerate 를 사용하면 간단하게 해결이 된다.

<div>
<script src="https://gist.github.com/AhnSeongHyun/1b16530fa80dddea4b02.js"></script>
</div>


**set** 

– `set` 은 사실 잘 사용하지 않는데, 해당 요소가 unique 해야 한다는 제약이 있다. 아래의 소스를 보면 단순히 list 내 요소에서 포함된것(교집합, intersection)과 포함되지 않은것(차집합, difference) 을 `set` 을 이용해서 가져오는 것을 볼 수 있다. 기존의 list 에서 for 루프를 통해서 걸러냈었다면 `set `을 사용하는 코드로 바꾸는게 좋을것 같다.<script src="https://gist.github.com/AhnSeongHyun/11af75aaf00a1f4e20e2.js"></script>

 

**for … else**  
 – 신기한 구문이다. `if else` 가 아닌 `for else` 라니. 되는것이 신기한데 아래의 코드를 보면서 설명을 하면, `break`문이 도달하지 않고 for 루프를 탈출하게 되면 else: 하위의 구문이 실행된다. 그렇지만, `break`문에 도달해서 탈출하게 되면 else: 하위의 구문은 실행되지 않는다.

<div>
<script src="https://gist.github.com/AhnSeongHyun/771232f2669d8e193fcd.js"></script>
</div>
 

**Generator expressions**

 – `yield` 를 이용한 generator 를 만드는 방법은 워낙 잘 알려져 있는데 여기에서는 괄호() 를 이용해서 generator 를 만들고 있다. 만약 아래의 코드에서 괄호() 대신에 [] 를 쓰게 되면 generator 가 아닌 list로 만들어지니 주의하자. generator 를 사용해야 하는 이유에 대해서 원 저자는 List Comprehension 의 문제점은 메모리에 바로 적재된다는 점이고, 이 부분은 매우 큰 데이터의 경우 문제가 될수 있다고 한다. generator 를 사용하면 객체가 늦게 생성된다고 하고 실제 값을 요청하기 전까지 어떤 연산도 없다고 설명하고 있다.(*you can use a generator expression, which uses very similar syntax, but creates a lazy object, that computes nothing until you ask for a value.*)<script src="https://gist.github.com/AhnSeongHyun/03a02a2eb98e70d4646b.js"></script>

 
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>


**Dictionary Comprehension**  
 – List Comprehension 은 많이 봤어도 Dictionary에 대한것은 처음봐서 적어둔다. 아래의 코드를 보면 전에 봤던 generator expression 에 `dict()` 을 함으로써 생성할수도 있고 [] 대신에 {} 를 사용해서 Dictionary를 만들어 내고 있다.

<script src="https://gist.github.com/AhnSeongHyun/7eb98d3c05e4bd5f2a78.js"></script>

기타 `defaultdict`, `Counter `에 대한 소개도 원문링크를 보면 나와있다. 이미 알고 있는부분이라서 소개하진 않았지만, 한번 훑어보는것도 좋을것 같다.


> [[번역] 6 Python Performance Tips](https://ash84.net/2015/03/04/-eb-b2-88-ec-97-ad-6-python-performance-tips/)
