---
title: '(알고리즘) 시간 복잡도'
author: 'ash84'
pub_date: '2013-07-08'
description: ''
featured_image: ''
tags: ['공간복잡도', '시간복잡도', '알고리즘', '최고차항']
---


<span style="font-size: 11pt;">오랫동안 비 전공자인 나를 괴롭혔던 문제들인데 인제 좀 정리를 하려고 한다. **시간복잡도와 공간복잡도 문제는 알고리즘을 측정하는 계산법이다. **생활코딩도 있고 code academy 도 프로그래밍에 대해서 알려주지만 이건 어쩌면 기본적인 프로그래밍을 배우고 나서 언젠가 마주해야할 문제중 하나라는 생각이 든다. (잡설시작) 나 역시 프로그래밍을 사용법 위주로 해왔지만 어느 순간 데이터와 마주하게 되면서 더이상 for 문의 순차 비교만으로는 원하는 성능이 나오지 않는다. 나는 앱 개발자인데? 나는 프론트 개발자인데? 할수도 있겠지만 앱 상에서 어떤 데이터를 찾아서 보여줘야 한다고 할때, 데이터가 많으면 찾는데 시간이 걸리고 그로 인해서 UI 프리징이 발생할 수 도 있다. 때문에 아주 자세히는 아니지만 어느정도의 알고리즘에 대해서는 이해할 필요가 있다.  </span>

**<span style="font-size: 11pt;">시간 복잡도는 무엇일까?</span>**

<span style="font-size: 11pt;">복잡도라는 말이 어려운데, 시간복잡도는 한마디로 애기해서 어떤 코드조각, 알고리즘에 대해서 **시간이 얼마나 걸릴까 하는 예상을 하는 것**이다. 같은일을 하는 두 개의 작업에 대해서 어떤 것이 더 빠를지는 실행을 해보면 알지만, 알고리즘을 미리 생각해 보고 그에 따른 시간을 측정해보면 코드를 짜는 시간을 절약할 수 있다. </span>

<span style="font-size: 11pt;">여러가지 예상 방법이 있는데 일단 최악, 최상, 평균 방식으로 측정을 한다. 각각에 따라서 표기법이 다른데, 아래와 같다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">최악 – 빅오표기법 : O(n)</span>

<span style="font-size: 11pt;">최상 – 오메가 표기법 : </span><span class="s1" style="font-size: 11pt;">Ω(N)</span>

<span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;"></span>

<span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">평균 – 세타 표기법 : </span><span class="s1" style="font-size: 11pt;">Θ(N)</span>

</div><span class="s1">  
</span>

<span style="font-size: 11pt;">이렇게 세가지로 표기를 하는데 일반적으로는 최악 즉, 빅오표기법을 시간복잡도의 일반적인 대상이라고 알고 있다. 그 이유는 아무래도 최상의 시간이라는 부분 보다는 최악의 시간이라는 것이 알고리즘 측면에서 더 의미가 있기 때문이 아닐까 싶다. </span>

<span style="font-size: 11pt;">시간 복잡도에는 여러가지 형이 있는데 다음과 같다. </span>

<table border="0" cellpadding="0" cellspacing="0" class="txc-table" style="border:none;border-collapse:collapse;;font-family:돋움;font-size:12px" width="604"><tbody><tr><td style="width: 71px; height: 24px; border: 1px solid rgb(204, 204, 204); background-color: rgb(217, 229, 255);"><span style="font-size: 10pt;"> 표기법</span><span style="font-size: 10pt;"> </span>

</td><td style="width: 78px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-top-width: 1px; border-top-style: solid; border-top-color: rgb(204, 204, 204); background-color: rgb(217, 229, 255);"><span style="font-size: 10pt;"> 형</span>

</td><td style="width: 454px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-top-width: 1px; border-top-style: solid; border-top-color: rgb(204, 204, 204); background-color: rgb(217, 229, 255);"><span style="font-size: 10pt;">** 설명**</span>

</td></tr><tr><td style="width: 71px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> </span><span style="font-size: 10pt; line-height: 29px; text-align: justify;">O(1)</span>

</td><td style="width: 78px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> </span><span style="font-size: 10pt; line-height: 29px; text-align: justify;">상수형</span><span style="font-size: 10pt; line-height: 29px; text-align: justify;"> </span>

</td><td style="width: 454px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> </span><span style="font-size: 10pt; line-height: 29px; text-align: justify;">자료의 량이 증가하더라도 같은 시간을 보장한다. </span>

</td></tr><tr><td style="width: 71px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> </span><span style="font-size: 10pt; line-height: 29px; text-align: justify;">O(log n)</span>

</td><td style="width: 78px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> </span><span style="font-size: 10pt; line-height: 29px; text-align: justify;">로그형</span>

</td><td style="width: 454px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> n</span><span style="font-size: 10pt; line-height: 29px; text-align: justify;">이 증가함에 따라서 logn 만큼 시간이 증가. </span>

</td></tr><tr><td style="width: 71px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> </span><span style="font-size: 10pt; line-height: 29px; text-align: justify;">O(n)</span>

</td><td style="width: 78px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> </span><span style="font-size: 10pt; line-height: 29px; text-align: justify;">선형</span>

</td><td style="width: 454px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> </span><span style="font-size: 10pt; line-height: 29px; text-align: justify;">자료양 n 증가시, 시간도 자료양에 비례해서 증가. 입력한 자료 각각에 대해서 동일한 처리를 하는 경우.</span>

</td></tr><tr><td style="width: 71px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> </span><span style="font-size: 10pt; line-height: 29px; text-align: justify;">O(n log n)</span>

</td><td style="width: 78px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> </span><span style="font-size: 10pt; line-height: 29px; text-align: justify;">선형로그형</span>

</td><td style="width: 454px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> </span><span style="font-size: 10pt; line-height: 29px; text-align: justify;">n이 2배로 늘어나면 시간은 2배보다 약간 증가. </span>

</td></tr><tr><td style="width: 71px; height: 30px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> </span><span style="font-size: 10pt; line-height: 29px; text-align: justify;">O(n^2)</span><span style="font-size: 10pt; line-height: 29px; text-align: justify;"> </span>

</td><td style="width: 78px; height: 30px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> </span><span style="font-size: 10pt; line-height: 29px; text-align: justify;">평방형</span>

</td><td style="width: 454px; height: 30px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> </span><span style="font-size: 10pt; line-height: 29px; text-align: justify;">이중루프</span>

</td></tr><tr><td style="width: 71px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> </span><span style="font-size: 10pt; line-height: 29px; text-align: justify;">O(n^3)</span>

</td><td style="width: 78px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> </span><span style="font-size: 10pt; line-height: 29px; text-align: justify;">입방형</span>

</td><td style="width: 454px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> </span><span style="font-size: 10pt; line-height: 29px; text-align: justify;">삼중루프</span>

</td></tr><tr><td style="width: 71px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204); border-left-width: 1px; border-left-style: solid; border-left-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> </span><span style="font-size: 10pt; line-height: 29px; text-align: justify;">O(2^n)</span>

</td><td style="width: 78px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> </span><span style="font-size: 10pt; line-height: 29px; text-align: justify;">지수형</span>

</td><td style="width: 454px; height: 24px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(204, 204, 204); border-right-width: 1px; border-right-style: solid; border-right-color: rgb(204, 204, 204);"><span style="font-size: 10pt;"> </span><span style="font-size: 10pt; line-height: 29px; text-align: justify;">입력자료에 따라 시간이 급격히 증가 </span>

</td></tr></tbody></table> 

<span class="s1"><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;"></span></span>

<span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < </span><span style="font-size: 15px; line-height: 29px;">O(2^n) < </span><span style="font-size: 11pt; line-height: 2;">O</span><span style="font-size: 11pt; line-height: 2;">(n^3)</span>

<span style="font-size: 11pt;">위의 형은 그렇다면 어떻게 계산하는 걸까? 저런 형이 존재하는 이유는 기본적으로 알고리즘 시간복잡도 측정법을 이용해서 우리가 만든 알고리즘이 위의 형중 하나로 표현이 되어야 한다. 그래야 어떤것이 더 빠르고 느린지를 알수 있기 때문이다. </span>

**<span style="font-size: 11pt;">계산 하는 법 </span>**

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">sum(명령어 실행 * 각 명령어의 실행시간)</span>

</div><span style="font-size: 11pt;">이렇게 계산이 되지는 것이 엄격한 의미의 시간 복잡도인데,  각 명령어의 실행 시간은 플랫폼, 하드웨어에 따라서 다르게 때문에 생략한다. 즉, 명령어 실행에 대한 횟수를 통해서 시간 복잡도를 계산 하게 된다. 계산 하는 방법은 쉬운데, 아래의 예제를 보자. </span>

<script src="https://gist.github.com/AhnSeongHyun/5945828.js"></script>

<span class="s1" style="font-size: 11pt;">시간복잡도 O(n)</span>

<span class="s1" style="font-size: 11pt;">총 실행횟수 : 2n +4  => O(N) </span>

<span class="s1" style="font-size: 11pt;">위의 예제에서 보면 일반적인 연산은 1로 표시를 하고 for문은  n으로 표시하는 것을 알수 있다. 즉,  for 문은 자료양에 따라서 변화하는 것이다.(당연한 애기) for 문에서  n+1 이라고 되어 있는데 n 이라고 생각할수도 있는데 +1이 된 이유는 i=0 이 부분이 별도의 연산이기 때문입니다. 그렇게 해서 계산을 하면 2n+4 가 되는데, 이 합계에서 계수를 제외한 최고차항만 계산하면 된다. 그 이유는 Reference 부분을 참고하시고. </span>

<span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;"></span>

<span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">시간 복잡도에 대해서 간단하게 알아 봤는데, 자기 코드를 까서 한번 해보는 것도 나쁘지 않다라는 생각이 든다. 어떻게 보면 단순히 for 문을 줄이는 것이 기본적인 알고리즘 성능을 높이는 방법이긴 하지만, 어떤 시간복잡도를 가지고 있고, 그것을 다르게 처리 했을때 어떤 시간복잡도가 나오게 되는지에 대한 부분은 한번쯤 고려해볼만 한것 같다. 알고리즘 개선에 대해서 설명할때 사실은 이 시간복잡도 처럼 분명하게 애기해 줄수 있는것은 없다는 생각이 든다. 공간 복잡도에 대해서는 조금 빈약하긴 하지만 아래의 링크로 대체한다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">**Reference**</span>

<span style="font-size: 11pt;">– [기본](http://skmagic.tistory.com/category/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0%26%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98) </span>

<span style="font-size: 11pt;">– [공간복잡도](http://qwe1qwe.tistory.com/880)</span>

<span style="font-size: 11pt;">– [최악, 최선, 평균에 대한 이야기](http://blog.daum.net/kimjaehun12/119)</span>

<span style="font-size: 11pt;">– [최고차항만 선택하는 이유](http://silpdmj.egloos.com/594813) </span>

<span style="font-size: 11pt;">  
</span>



