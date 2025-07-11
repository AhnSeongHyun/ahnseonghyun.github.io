---
title: '[번역] 6 Python Performance Tips'
author: 'ash84'
pub_date: '2015-03-04'
description: '> 원문 : [http://blog.newrelic.com/2015/01/21/python-performance-tips/?utm_source=Python+Weekly+Newsletter&utm_campaign=c403fa901e-Python_Weekly_Issue_175_January_22_2015&utm_medium=email&utm_term=0_9e26887fc5-c403fa901e-312692397](http://blog.newrelic.com/2015/01/21/python-performance-tips/?utm_sourc'
featured_image: 'https://images.unsplash.com/photo-1523655223303-4e9ef5234587?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=fab1861116d5fe59fecdcf19356718ff&auto=format&fit=crop&w=1353&q=80'
tags: ['blog.newrelic.com'', 'dev', 'Performance', 'python performance tips', '번역', '성능', '태그를 입력해 주세요.', '파이썬']
---

> 원문 : [http://blog.newrelic.com/2015/01/21/python-performance-tips/?utm_source=Python+Weekly+Newsletter&utm_campaign=c403fa901e-Python_Weekly_Issue_175_January_22_2015&utm_medium=email&utm_term=0_9e26887fc5-c403fa901e-312692397](http://blog.newrelic.com/2015/01/21/python-performance-tips/?utm_source=Python+Weekly+Newsletter&utm_campaign=c403fa901e-Python_Weekly_Issue_175_January_22_2015&utm_medium=email&utm_term=0_9e26887fc5-c403fa901e-312692397)


**1. 핵심적인 부분은 외부 패키지에 의존해라.**  

파이썬은 쉽지만, 시간과 밀접한 관련이 있는 작업들에서 좋은 성능을 제공하지 않는다.  그래서 C, C++ 기계어, 외부 패키지들을 사용하면 성능 향상을 가져올수 있다. 이런 패키지들은 플랫폼 지향적(platform-specific)인데, 즉 플랫폼 지향적인 패키지가 필요하다는 것이다. 플랫폼에 종속적으로 되어 버리는데, 이는 성능과 이식성을 교환했다고 생각하면 된다. CPYTHON, PyInIne PyPy, Pyrex 같은 것 들이 있다. 


**2. 정렬시 키를 사용해라.**

오래된 파이썬 정렬코드는 커스텀 정렬을 생성하는데, 시간이 들고 실제로 정렬수행하는 속도를 필요로 한다. 좋은 방법은 가능한한 기존 sort() 메소드에 key 들을 사용하는 것이다. 

<script src="https://gist.github.com/AhnSeongHyun/d80459d460404e507a3f.js"></script>

각각의 경우를 보면, key 인자로 지정한 index 에 의해서 정렬이 되어 진다. 이 방법은 숫자형 뿐만 아니라 문자형에서 쓸수 있다.


**3. 루프 최적화**

모든 프로그래밍 언어는 루프 최적화를 강조한다. 파이썬에서 루프를 좀더 빠르게 만드는 기술을 의지해야 한다.(찾으라는 애기) 그러나 개발자들이 하나의 메소드상에서 놓치는 것은 루프안에서 점(dots)의 사용을 피하는 것이다. (루프 안에서 .을 통한 호출의 애기)

<script src="https://gist.github.com/AhnSeongHyun/c3de45a52ecfab5ff3e5.js"></script>

예제를 보면, 매번 str.upper 를 호출하는데, **파이썬은 이것을 메소드로 평가한다.  그런데 그 부분은 변수로 평가하게 만들면, 이미 인터프리터가 알고 있기 때문에, 훨씬 더 작업이 빨라진다. 중요한 것은 루프 안에서 일의 양을 줄이는 것이다.**

> 루프 최적화에 여러가지 방법이 있는데 이것도 하나의 방법이고 리스트 축약 속도 이점을 가져다 준다. 중요한 점은 루프 최적화가 어플리케이션의 속도 향상을 위한 방법들 중 하나라는 것이다.


**4. 새로운 버전**

모든 버전의 파이썬이 그 이전 보다 빠르다.(최적화 포함) 제한 되는부분은 선호하는 라이브러리가 새로운 파이썬 버전으로 옮겨졌는지, 이식이 되었는가 하는 부분이다. 중요한질문은 언제 새로운 버전이 충분하게 지원할지에 대한것.

새로운 버전의 파이썬에서 여전히 코드가 잘 동작하는지 검증해야하고, 새로운 버전의 라이브러리를 사용해야 한다. 그리고 어플리케이션에서 문제 없는지 체크해야한다. 일단 옮겨가고 나면 프로파일링을 새로운 버전의 파이썬에서 하고 문제가 되는 부분이 있으면 해당 부분을 새로운 것으로 업데이트 해라. 


**5. 멀티 코딩 접근을 시도해라**

어플리케이션을 만들때 매번 같은 코딩 접근방식을 사용하는 것은 어플리케이션을 느리게 할수도 있다.(늘 같은방식을 사용하는 것 보다는 실험을 해보라는 이야기) 프로파일링 프로세스의 일부로서 작은 실험을 시도해라. 예를들어, 사전형식(dict)내의 아이템을 관리할때, 아이템이 이미 존재하고 갱신할지 또는 바로 아이템을 삽입하고 그리고나서 아이템이 존재 하지 않는 예외를 처리할 지에 대한 결정에 대한 접근법을 생각해 보면, 

첫번째 코드를 보면, 

<script src="https://gist.github.com/AhnSeongHyun/4644ebe4e0229ed52c6a.js"></script>

위의 코드는myDict이 비어 있을때는 빠르다. 그러나 myDict 이 보통 데이터가 있는 경우에, 더 나은 접근이 있다. 

<script src="https://gist.github.com/AhnSeongHyun/8d22ca9cc3eb213918ba.js"></script>

output 은 {‘d’: 4, ‘c’: 4, ‘b’: 4, ‘a’: 4} 으로 두 경우 모두 같다. 오직 차이는 어떻게 결과는 얻느냐의 차이이다. 다른 코딩 기술을 만드는 것은 어플리케이션 상에서 결과를 더 빨리 얻는데 도움을 준다.

**6. 어플리케이션의 크로스 컴파일**

개발자는 때때로 컴퓨터가 현대의 어플리케이션을 만드는데 사용되는 어떤 언어로 말하지 않는다는 것을 잊어먹는다. 컴퓨터는 기계어로 이야기한다. 어플리케이션을 구동하기 위해서는 사람이 읽을수 있는 형태의 코드를 기계가 이해할수 있는 형태로 변환해야 한다. 파이썬과 같은 언어로 어플리케이션을 만들었는데, 성능적인 측면으로  C++과 같이 다른 언어로 운영된다. 호스트 시스템에서 어플리케이션에서 하고자 하는 것과 리소스를 주기 때문에 호스트 시스템에 의존적이다. 한가지 흥미로운 크로스 컴파일러인 Nuitka 는 파이썬 코드를 C++ 코드로 변환한다. 변환 결과를 통해서 인터프리터가 아닌 네이티브 환경에서 어플리케이션을 실행할수 있다. 플랫폼과 테스크에 의존함으로써, 놀라운 성능향상을 볼 수 있다. 크로스 컴파일러와 함께 동작할때 확인해야 할것은 컴파일러가 당신이 사용하는 파이썬 버전을 지워하는지 확인해라. Nuitka는 파이썬 2.6, 2.7, 3.2, 3.3을 지원한다. 제대로 동작하기 위해서는 파이썬 인터프리터와 C++ 컴파일러 둘다 필요하다. Nuitka 는 수많은 C++ 컴파일러를 지원하는데 Microsoft Visual Studio, MinGW, Clang/LLVM 등을 지원한다. **크로스 컴파일은 몇가지 단점이 있을수 있다.** 예를들어, Nuitka와 함께 동작할때, 작은 프로그램이 큰 드라이브 공간을 소모 하는것을 볼수 있는데 이것은 Nuitka 가 파이썬의 기능을 수 많은 DDL들을 이용해서 구현하기 때문이다. 그래서 만약 리소스가 제약되는 시스템에서 처리된다면 이 해결방법은 잘 동작하지 않을것 이다.

**핵심(Bottom line)**

이 글에서의 3가지 각각의 팁들은 좀더 빠른 파이썬 어플리케이션을 만드는데 도움을 준다. 그러나 은 총알은 없다.(**But there are no silver bullets.)** 팁들중 어느것도 매번 작동하지는 않을것이다. 어떤 것은 파이썬의 특정에서 더 나을것이다-심지어 플랫폼마다 다를수도 있다. 어느 부분이 느린지를 결정하기 위해 어플리케이션 프로파일을 해보는것이 필요하며 그리고 팁을 시도해 보면, 해당 이슈에 대한 최고의 해결책이 나오게 된다.  
