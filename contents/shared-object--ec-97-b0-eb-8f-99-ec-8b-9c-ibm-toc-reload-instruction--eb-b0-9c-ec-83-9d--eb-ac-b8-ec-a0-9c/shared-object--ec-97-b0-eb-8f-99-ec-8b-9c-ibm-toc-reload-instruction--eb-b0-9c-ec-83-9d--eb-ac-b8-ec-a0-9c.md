---
title: 'shared object 연동시, IBM TOC-reload instruction 발생 문제'
author: 'ash84'
pub_date: '2012-10-02'
description: '사건의 요지는 이렇다. 나는 고객사로 부터 파수닷컴 DRM 연동을 의뢰 받았고 파수 닷컴 DRM 관련 ANSI C 라이브러리(AIX/xlC로 빌드된)를 전달 받았다. 원래 연동하는 소스에 붙였는데, 이상한 에러들이 나는 문제가 있어서 [어디에서 보니](http://demo.initech.com/index.php?document_srl=12470) .so 파일을 연동이 안될수 있으니 **-Wl,-brtl** 옵션을 사용해야 한다고 나와 있었다.'
featured_image: ''
tags: ['aix', 'aix .so 라이브러리 연동', 'IBM', 'no-op cod', 'so 라이브러리 연동', 'TOC-reload instruction', 'xlc', 'xlC -Wl', '컴파일러 버그', '컴파일러 옵션']
---


<span style="font-size: 11pt; ">사건의 요지는 이렇다. 나는 고객사로 부터 파수닷컴 DRM 연동을 의뢰 받았고 파수 닷컴 DRM 관련 ANSI C 라이브러리(AIX/xlC로 빌드된)를 전달 받았다. 원래 연동하는 소스에 붙였는데, 이상한 에러들이 나는 문제가 있어서 [어디에서 보니](http://demo.initech.com/index.php?document_srl=12470) .so 파일을 연동이 안될수 있으니 **-Wl,-brtl** 옵션을 사용해야 한다고 나와 있었다. </span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; line-height: 2; "><span style="font-size: 11pt; ">ld: 0706-006 Cannot find or open library file: -l fasoopackagerC</span><span class="s1">  
<span style="font-size: 11pt; ">  
</span></span><span style="font-size: 11pt; ">ld:open(): A file or directory in the path name does not exist.</span>

</div><span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; line-height: 2; ">해당 옵션을 이용하면 빌드는 되었으나 수 많은 warning 이 발생되었다. 경고는 경고일뿐 에러는 아니라는 안일한 생각으로 빌드된 파일을 고객사에 있는 직원에게 전달했는데.. 이게 왠일!! **illegal instruction(core dump)**가 떨어진다고 한다. </span>

<span style="font-size: 11pt; line-height: 2; ">  
</span>

![](http://ash84.net/wp-content/uploads/1/cfile9.uf.1614DD4E5065561D2A8B78.jpg)

<span style="font-size: 11pt; line-height: 2; ">  
</span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">그래서 소스가 문제라는 생각에 하나씩 지우면서 테스트 결과 Makefile 에 -lfasoopackagerC 라이브러리만 써도 (관련 소스 한줄 없이) 다음과 같은 Warning 이 떨어졌다. </span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; line-height: 2; "><span style="font-size: 11pt; ">ld: 0711-768 WARNING: Object mytest.o, section 1, function .strcpy: </span><span class="s2">  
<span style="font-size: 11pt; ">  
</span></span><span style="font-size: 11pt; ">The branch at address 0x1c is not followed by a recognized no-op or TOC-reload instruction. The unrecognized instruction is 0xE8010090.</span>

</div><span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">도데체 이건 뭔가.. 하는 생각에 다양한 컴파일 및 링크 옵션들을 죽이고 살리고 하는 과정에서 별 다른 대책이 없음을 스스로 자책하던중.. 구글링 과정에서 [IBM 링크](http://www-01.ibm.com/support/docview.wss?uid=swg21443810)를 찾았다. </span>

<span style="font-size: 11pt; ">  
</span>

<figure class="wp-caption aligncenter" style="width: 640px">![](http://ash84.net/wp-content/uploads/1/cfile6.uf.1421F24D506554DF169B9A.jpg)<figcaption class="wp-caption-text">개인적으로 정말 AIX/xlC 환경이 싫다. </figcaption></figure>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">이 아이들의 영어를 해석한 결과로는 ANSI C 라이브러리를 만들거나 연동하는 과정에서 생길수 있는 경고인데, 일종의 xlC 컴파일러의 문제라는 이야기다. 이 문제를 피하고 싶으면 만드는 과정에서 특정한 옵션을 사용해서 .SO 라이브러리를 만들어야 한다는 이야기다. </span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">**2010년 10월 이후로 컴파일러 패치가 되었다고 설명하고 있다. **좀 어이없는 일이라서 당황스러웠다. 좀더 시간이 있었다면, 서버관리자에게 컴파일러 패치를 요청하거나 파수닷컴에 다른 컴파일러로 .SO를 만들어 달라고 했을텐데, 2~3시간 남은 저녁에 그건 무리라는 판단하에, 필자가 한 방법은 -lfasoopackagerC 를 사용하는 부분을 따로 외부 프로그램으로 빼고, 원래 연동하려는 프로그램에서 외부 프로그램을 popen 으로 호출하는 방식으로 만들었다. 물론 정석인 과정은 아니였지만, 나름대로의 대처라는 생각이 든다. </span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">약간 옆길로 샜는데, <span style="color: rgb(204, 61, 61); ">이 포스팅을 남기는 이유는 TOC-reload instruction 이나 no-op code가 발생되었을때는 뭔가 나처럼 삽질을 하지 말고, 컴파일러를 교체하거나 해당 라이브러리 작업 제공 회사에 다시 요청하는 방향으로 일을 진행하였으면 한다. 그게 정석이니까. </span></span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>



