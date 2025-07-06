---
title: '(python) daum_openapi 라이브러리 개발기'
author: 'ash84'
pub_date: '2015-07-03'
description: '[Daum Open API](http://dna.daum.net/apis/dashboard) 중에서 데이터형 API 를 쉽게 쓸 수 있는 Python 라이브러리를 만들어서 pypi 에 등록을 하였다. 이미 Daum 쪽에서 python 으로 api를 호출할 수 있는 예제코드를 제공하고 있는데, 만들게된 계기는 아래와 같다.'
featured_image: ''
tags: ['daum open api python', 'daum_openapi', 'dev', 'Python', 'requests', 'travis-ci', 'xmltodict']
---


<span style="font-size: 11pt;">[Daum Open API](http://dna.daum.net/apis/dashboard) 중에서 데이터형 API 를 쉽게 쓸 수 있는 Python 라이브러리를 만들어서 pypi</span><span style="font-size: 11pt;"> 에 등록을 하였다. 이미 Daum 쪽에서 python 으로 api를 호출할 수 있는 예제코드를 제공하고 있는데, 만들게된 계기는 아래와 같다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; line-height: 2;"><span style="font-size: 11pt;">1. daum, naver api를 자주 사용하는 편인데, 매번 만들때 마다 새롭게 만들기 귀찮아서.</span>

<span style="font-size: 11pt;">2. pypi</span><span style="font-size: 11pt;"> </span><span style="font-size: 11pt;">에 찾아보니 없어서(내 생각엔 너무 쉽게 만들수 있어서 없는 듯)</span>

<span style="font-size: 11pt;">3.</span><span style="font-size: 11pt;"> json 키를 클래스의 멤버변수로 매핑해서 사용하면 좀더 쉽게 사용할수 있지 않을까 싶어서. </span>

</div><span style="font-size: 11pt;">3번에 대해서 설명하면 이런식이다. </span>

<script src="https://gist.github.com/AhnSeongHyun/7972848.js"></script>

<span style="font-size: 11pt;">관건은 어떻게 json 키를 가져와서 매핑 시키느냐 하는 부분과 더불어서 계층적인 구조로 매핑을 어떻게 시키느냐 하는것이었다. 이부분은 다른 개발자분들께 트위터를 통해서 공개 질의를 했었는데, [stacko](http://stackoverflow.com/questions/20091760/how-to-convert-json-to-python-class?noredirect=1#comment29934628_20091760) [verflow](http://stackoverflow.com/questions/20091760/how-to-convert-json-to-python-class?noredirect=1#comment29934628_20091760) 에도 올리고 해서 찾았다. 요지는 class 의 변수를 키-값 형태로 가지고 있는 `__dict__` 에 넣어주면 되는 것인데, 처음에는 결과 json 을</span><span style="font-size: 11pt;"> 다 파싱을 해서 넣어야 하나 했는데, 찾아보니 dictionary 형의 </span><span style="font-size: 11pt;">`update()` 함수를 통해서 가져온 json 을 키 값 형태로 바로 넣을 수가 있어서 그것을 활용하였다. </span>

<script src="https://gist.github.com/AhnSeongHyun/7972744.js"></script>

<span style="font-size: 11pt;"> </span>

<span style="background-color: transparent; font-size: 11pt; line-height: 2;">개발하던 중 Daum OpenAPI 에서는 리턴값으로 XML을 주는 경우가 있다는 것을 알게 되었다. 어떻게 해야할까 고민했는데, </span><span style="background-color: transparent; font-size: 11pt; line-height: 2;"></span>[daum_openapi](https://pypi.python.org/pypi/daum_openapi/0.1)<span style="background-color: transparent; font-size: 11pt; line-height: 2;"></span><span style="background-color: transparent; font-size: 11pt; line-height: 2;"> 라이브러리에서는 xml인 경우에 xml을 json으로 변환한 후, 클래스 맵핑을 하였다. 이 과정에서는 </span>[xmltodict](https://pypi.python.org/pypi/xmltodict/0.8.3)<span style="background-color: transparent; font-size: 11pt; line-height: 2;"> 이라는 python 라이브러리를 사용했다. 그 외에 사용하는 라이브러리로는 </span>[requests](http://requests.readthedocs.org/en/latest/)<span style="background-color: transparent; font-size: 11pt; line-height: 2;"> 라 http 요청 라이브러리를 urllib 대신에 사용하고 있다. </span>

<span style="background-color: transparent; font-size: 11pt; line-height: 2;">  
</span>

<span style="font-size: 15px; line-height: 29px;">**설치법 **</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 15px; line-height: 29px;">pip install daum_openapi</span>

</div><span style="font-size: 15px; line-height: 29px;">  
</span>

<span style="font-size: 15px; line-height: 29px;">**github 및 사용법**</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 15px; line-height: 29px;">[https://github.com/AhnSeongHyun/daum_openapi](https://github.com/AhnSeongHyun/daum_openapi)</span>

</div><span style="font-size: 15px; line-height: 29px;">  
</span>

<span style="font-size: 11pt;">만드는 과정은 그리 어렵지 않았지만, pypi 에 올리는 과정은 역시 험난했다. 목요일에 업무를 다하고, 금요일 오전부터 업로드 작업을 했는데 3시간 정도 걸렸던 것 같다. pypi</span><span style="font-size: 11pt;"> 에 올리는 것을 나중에 따로 포스팅 할 예정이긴 한데, 간략하게 말하자면 준비보다 나중에 pip install ‘내가 만든 모듈’ 을 받는 부분과 받아서 python 프로그램에 들어가서 `import daum_openapi` 식으로해서 테스트를 하고 고치는 부분에서 많은 시간을 보냈다.</span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">사실 내가 필요해서 만들었고, json 결과를 클래스처럼 사용하고 싶다는 생각을 가지고있었는데 어느정도 만족한것 같다. 다음주 중으로 [travis-ci](https://travis-ci.org/) 와 github를 연결해서 테스트 코드를 돌려볼 생각이다.(사실 이것도 [travis-ci](https://travis-ci.org/) 를 써보고 싶어서.) 스터디 성이 강한 오픈소스긴 하지만. 나름 유익하고 재미있는 경험이었던것 같다. </span>



