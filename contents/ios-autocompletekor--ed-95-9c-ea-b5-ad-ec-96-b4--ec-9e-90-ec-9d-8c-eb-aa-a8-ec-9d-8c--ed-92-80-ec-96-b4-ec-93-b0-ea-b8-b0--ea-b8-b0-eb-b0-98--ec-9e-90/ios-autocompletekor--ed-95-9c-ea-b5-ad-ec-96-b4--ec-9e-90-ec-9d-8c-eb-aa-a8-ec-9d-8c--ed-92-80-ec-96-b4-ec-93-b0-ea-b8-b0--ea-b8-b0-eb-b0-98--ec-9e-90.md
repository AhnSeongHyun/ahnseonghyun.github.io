---
title: '(iOS) AutoCompleteKor, 한국어 자음/모음 풀어쓰기 기반 자동완성 오픈소스'
author: 'ash84'
pub_date: '2013-05-24'
description: '간간히 자동완성이 필요한 경우가 있다. 어떤 정보를 검색할 때가 그러한 경우라고 볼수가 있는데, 사실 자동완성이라고 하는 범위는 너무 넓다보니 하나의 커다란 서버가 필요하기도 하는데, 여기서는 iOS 상에서 한국어 풀어쓰기 기반의 자동완성을 소개하려고 한다. 
**풀어쓰기가 필요한 이유.** 
한국어가 완성자가 아닌 조합자이기 때문에 풀어'
featured_image: ''
tags: ['autocomplete', 'AutoCompleteKeyword', 'iOS', 'iOS AutoComplete', '자동완성', '자동완성 한국어']
---
<span style="font-size: 11pt;">간간히 자동완성이 필요한 경우가 있다. 어떤 정보를 검색할 때가 그러한 경우라고 볼수가 있는데, 사실 자동완성이라고 하는 범위는 너무 넓다보니 하나의 커다란 서버가 필요하기도 하는데, 여기서는 iOS 상에서 한국어 풀어쓰기 기반의 자동완성을 소개하려고 한다. </span>

<span style="font-size: 11pt;">**풀어쓰기가 필요한 이유.** </span>

<span style="font-size: 11pt;">한국어가 완성자가 아닌 조합자이기 때문에 풀어쓰기가 필요한 것인데, 사실 완성자 자동완성을 제공해도</span><span style="font-size: 11pt;"> 상관은 없지만 사용자가 느끼기에는 품질이 떨어지게 된다. 아래의 은행관련 </span><span style="font-size: 11pt;">예제를 보자. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">찾고자 의도 하는 것 : 국민은행 </span>

<span style="font-size: 11pt;">**완성자 자동완성 **</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">[국] => 국민은행</span>

<span style="font-size: 11pt;">[국민] => 국민은행</span>

<span style="font-size: 11pt;">[국ㄱ] => X</span>

</div><span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">위와 같이 완성자가 입력된 상태에서는 찾을수 있으나, “국ㄱ”과 같이 완성자+자음이 입력되는 경우에는 찾지 못하게 된다. 본래 대부분의 자동완성들은 키보드 입력이 일어날때 마다 그 결과를 보여주는 것을 일반적으로 하고 있기 때문에  사용자 입장에서”국민” 이라는 단어를 완성해가는 과정에서 자동완성 결과가 “국ㄱ”에서 안보이게 되면 이상하게 생각 할수 있다. “국ㄱ” 뿐만 아니라 생각해 보면 “국미” 단계에서도 완성자 자동완성으로는 찾을 수가 없다. </span>

<span style="font-size: 11pt;">**풀어쓰기 자동완성**</span>

<span style="font-size: 11pt;">풀어쓰기는 말 그대로 한글 자음과 모음을 풀어쓰는 것이다. 아래와 과정은 풀어쓰기의 과정을 보여준다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">[안녕하세요.] => ㅇㅏㄴㄴㅕㅇㅎ</span><span style="font-size: 11pt;">ㅏㅅ</span><span style="font-size: 11pt;">ㅔ</span><span style="font-size: 11pt;">ㅇㅛ.</span>

<span style="font-size: 11pt;">[SC제일은행] => SCㅈㅔㅇㅣㄹㅇㅡㄴㅎㅐㅇ</span>

</div><span style="font-size: 11pt;">영어가 섞여 있는 경우나 숫자가 있는 경우에는 그냥 둔 상태로 한글에 대해서만 풀어쓰기를 수행한다. 풀어쓰기 자동완성에서 풀어쓰기는 2부분에서 사용된다. 첫번째 부분</span><span style="font-size: 11pt;">은 사전을 구성하는 단계에서 하나의 사전 단어에 대한 풀어쓰기 문자열을 만들때 사용이 된다. </span>

<span style="font-size: 11pt;">**사전**</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">[국민은행] => ㄱㅜㄱㅁㅣㄴㅇㅡㄴㅎㅐㅇ</span>

<span style="font-size: 11pt;">[경남은행] => ㄱㅕㅇㄴㅏㅁㅇㅡㄴㅎㅐㅇ</span>

<span style="font-size: 11pt;">…</span>

</div><span style="font-size: 11pt;">완성자 풀어쓰기에서는 국민은행, 경남은행 사전 자체로 비교했다면, 풀어쓰기 자동완성에서는 풀어쓴 단어 자체로 비교를 수행하고 그 결과에 대한 원문을 리턴하는 방식이다. 그렇기 때문에 풀어쓰기가 사용하는 두번째 부분은 바로 비교시 입력 단어에 대한 풀어쓰기의 수행이다. </span>

<span style="font-size: 11pt;">**입력단어**</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">[국ㄱ] =></span><span style="font-size: 11pt; line-height: 1.5;">ㄱㅜㄱ</span>

<span style="font-size: 11pt;">[국미] =></span><span style="font-size: 11pt; line-height: 1.5;">ㄱㅜㄱㅁㅣ</span>

</div>  
<span style="font-size: 11pt;">**사전**</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">[국민은행] => ㄱㅜㄱㅁㅣㄴㅇㅡㄴㅎㅐㅇ</span>

<span style="font-size: 11pt;">[경남은행] => ㄱㅕㅇㄴㅏㅁㅇㅡㄴㅎㅐㅇ</span>

<span style="font-size: 11pt;">…</span>

</div><span style="font-size: 11pt;">입력단어의 풀어쓰기 결과를 가지고 사전의 풀어쓰기와 비교를 하면서 같거나 포함된것이 있으면 원문을 찾아서 리턴하는 방식이다. 원리는 여기까지 설명을 하고 코드를 설명하겠다. </span>

<span style="font-size: 11pt;">[AutoCompleteKor](https://github.com/AhnSeongHyun/AutoCompleteKor) 소스코드에서 가장 중요한 부분은 한글을 풀어쓰는 부분인데 그것은 [여기](http://ash84.tistory.com/964)를 참고하길 바란다. 원래 인터넷에서 찾을수 있겠지만 자음모음 분리 공식이 존재하기 때문에 그것을 사용했다. </span>

<span style="font-size: 11pt;">  
</span>

![](http://ash84.net/wp-content/uploads/1/cfile21.uf.256F3340519E88AB042907.jpg)

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">그외에 2개의 클래스가 [AutoCompleteKor](https://github.com/AhnSeongHyun/AutoCompleteKor) 에 존재를 하는데 `AutoCompleteData` 클래스와 `AutoCompleteMng` 클래스이다. </span>

<span style="font-size: 11pt;">`AutoCompleteData` 클래스</span>

<span style="font-size: 11pt;">– word와 wordIndex 라는 두개의 변수를 갖는다. </span>

<span style="font-size: 11pt;">– word에는 원문 단어가, wordIndex 에는 풀어쓰기 결과가 들어간다. </span>

<span style="font-size: 11pt;">– 이 클래스는 하나의 사전 단어당 하나씩 객체가 생성되는 클래스이다. </span>

<span style="font-size: 11pt;">`AutoCompleteMng` 클래스 </span>

<span style="font-size: 11pt;">-이 클래스는 `NSMutableArray` 형식의 `acdArr` 변수</span><span style="font-size: 11pt;">를 가지고 있는데 위에서 설명한 `AutoCompleteData`객체를 담기 위한 변수이다. </span>

<span style="font-size: 11pt;">– 이 클래스가 생성될때, 사전 데이터를 넣게 되면 내부적으로 `AutoCompleteData`를 사전내 단어 만큼 생성을 하고 그 객체를 `acdArr` 에 넣게 된다. 그리고 나서 `acdArr` 을 오름차순(ASC)를 기준으로 정렬을 한다. 정렬을 하는 이유는 좀더 빠르게 찾기 위해서이다. </span>

<span style="font-size: 11pt;">아래의 코드를 보자. </span>

<script src="https://gist.github.com/AhnSeongHyun/5639321.js"></script>

<div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">`AutoCompleteMng`클래스의 생성자 부분에서 은행명이 들어있는 TestData 클래스를 생성을 하고 그 내에 있는 단어 수만큼 `AutoCompleteData`를 만들어서 `acdArr` 에 저장하는 것을 볼수가 있다. TestData 부분이 실제 원데이터 부분인데, 이 부분을 파일에서 읽어오거나, </span><span style="font-size: 11pt;">데이터베이스에서 읽어오도록 수정하면 그대로 사용할 수가 있다. </span></div><div style="text-align: justify; line-height: 2;"></div>**  
**

<span style="font-size: 11pt;">**그렇다면 풀어쓰기는 어디서 해주는 걸까?**</span>

<script src="https://gist.github.com/AhnSeongHyun/5639326.js"></script>

<span style="font-size: 11pt;">`AutoComleteData`의 `initWithWord`</span><span style="font-size: 11pt;"> 생성자를 보자. 생성자에서는 단어를 받으면 단어 자체는 word 에 저장을 하고 `[NSStrUtils getJasoLetter]`를 통해서 풀어쓰기한 결과를 wordIndex에 저장하고 있는 것을 볼수가 있다. </span>

**  
**

<span style="font-size: 11pt;">**자, 이제 사전 데이터는 마련이 되었다. 그렇다면 검색을 어떻게 할까?**</span>

<span style="font-size: 11pt;">검색시에는 `AutoCompleteMng` 클래스의 `search:(NSString*)keyword`함수를 이용해서 검색을 할 수가 있다. search 함수에서는 받은 입력 단어에 대한 풀어쓰기를 수행한 결과를 먼저 만들고나서, 그 결과를 가지고 이진탐색을 하면서 같거나 포함된 것들이 있으면 모두 찾는 과정을 수행한다. 코드는 아래와 같다. </span>

<script src="https://gist.github.com/AhnSeongHyun/5639387.js"></script>

<span style="font-size: 15px; line-height: 29px;">**버그**</span>

<span style="font-size: 11pt;">현재 발견된 버그는 “ㅘ, ㅟ” 와 같은 문자에 대한 처리이다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">외환은행 => ㅇㅚ ㅎ ㅘ ㄴ ㅇㅡ ㄴ ㅎㅐㅇ</span>

</div><span style="font-size: 11pt;">으로 사전에는 저장되는데** 입력시 “외” 자를 입력하면 우리는 ㅇ ㅗ ㅣ 를 누른다. 그런데 “오” 상태에서는 풀어쓰기를 하더라도 “외환은행”을 찾을수가 없다. 이러한 모음 조합자에 대한 분리 작업이 아직은 되어 있지 않은 상태이다.** </span><span style="font-size: 11pt; line-height: 2;">누구나 수정을 할수 있다. 아래의 [Github 링크](https://github.com/AhnSeongHyun/AutoCompleteKor)에 들어와서 수정을 해주셔도 좋고, [fork](https://github.com/AhnSeongHyun/AutoCompleteKor/fork)를 해가셔도 좋다. </span>

<span style="line-height: 24px;">[https://github.com/AhnSeongHyun/AutoCompleteKor](https://github.com/AhnSeongHyun/AutoCompleteKor)</span>



