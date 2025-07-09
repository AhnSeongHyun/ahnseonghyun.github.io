---
title: '[Java] Set 인터페이스, 간략 정리.'
author: 'ash84'
pub_date: '2013-01-04'
description: 'Set 인터페이스에 대해서 알아보자. Collection 의 일부인데 중복되는 element를 포함하지 않는것이 가장 큰 특징이며, Java Doc 에서는 “수학적으로 말해서 집합을 의미한다” 라고 설명하고 있다. Set 인터페이스는 Collection 를 상속 받아서 만들어진 인터페이스이다. 때문에 대부분의 함수들이 Collection 에서 제공하는 함수들과 동일하다.


**List 와 Map 그리고 Set의 차이점**

List 와 Set은 Collection Interface를 구현한다는 점에서 비슷하다고 할수 있다. 그러나'
featured_image: ''
tags: ['dev', 'HashSet', 'Java', 'MAP', 'Set 인터페이스', '중복 제거']
---

Set 인터페이스에 대해서 알아보자. Collection 의 일부인데 중복되는 element를 포함하지 않는것이 가장 큰 특징이며, Java Doc 에서는 “수학적으로 말해서 집합을 의미한다” 라고 설명하고 있다. Set 인터페이스는 Collection 를 상속 받아서 만들어진 인터페이스이다. 때문에 대부분의 함수들이 Collection 에서 제공하는 함수들과 동일하다.


**List 와 Map 그리고 Set의 차이점**

List 와 Set은 Collection Interface를 구현한다는 점에서 비슷하다고 할수 있다. 그러나 가장 큰 차이점은 중복에 대한 부분에서의 차이이다. List는 같은 값에 대한 중복 추가가 가능하다. 그러나 Set은 아래의 코드의 같이 같은 값을 넣었을때 size()로 내부 엘리먼트의 개수를 출력해보면 1이 나오는것을 볼 수가 있다. 

<script src="https://gist.github.com/4439695.js"></script>


중복이 안되는 것을 떠올리면 단연 Hashtable HashMap과 같은 Map 형태가 떠오를 수 있을 것이다. 그러나 다른 점이라면, <Key,Value> 형태를 Map 에서는 가진다는점이 가장 큰 차이일 것이다. 중복을 검사하는 대상 자체가 key, value 이기 때문에 **key 를 기준으로 중복검사** 를 하게 된다. **이 애기는 value는 중복 되더라도 상관없다는 이야기이다.**

간단하게나마 Set 인터페이스에 대해서 알아보았다. 사실은 잘 쓰게 되지 않는 인터페이스고 Set 인터페이스를 상속(extends) 또는 구현(implements) 한것을 몇번 써보지않았는데, 중복에 대한 부분을 이용할때는 괜찮을것 같다는 생각이 든다. 굳이 Map 쪽 클래스들을 사용하지 않더라도 말이다. 

