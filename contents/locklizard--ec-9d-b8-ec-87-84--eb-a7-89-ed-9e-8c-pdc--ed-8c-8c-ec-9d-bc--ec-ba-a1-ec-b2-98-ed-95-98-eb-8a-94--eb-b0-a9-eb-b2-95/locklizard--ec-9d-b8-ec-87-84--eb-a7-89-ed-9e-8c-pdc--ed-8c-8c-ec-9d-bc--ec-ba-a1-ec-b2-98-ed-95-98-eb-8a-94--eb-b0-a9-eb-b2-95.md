---
title: '(LockLizard) 인쇄 막힌 PDC 파일 캡처하는 방법'
author: 'ash84'
pub_date: '2012-10-07'
description: ''
featured_image: ''
tags: ['dev', 'PDC', 'PDC 파일 락 해제', 'PDC 파일 인쇄', 'PDC 파일 캡처', 'pdf', '스크린샷']
---

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>

<span style="font-size: 11pt; ">친구가 자소서 파는 사이트에서 자소서를 샀는데 PDC 파일이라면서 인쇄도 안되고, 캡처도</span><span style="font-size: 11pt; "> 안된다고 쌍욕을 했다. 아놔 왜 내 친구를 건드리나, 하는 쓸데없는 정의감은.. 없었고, PDC 파일이 몬데, 돈 주고 산 사람에게 인쇄할 권리를 박탈하나 하는 생각이 들었다. </span>

<span style="font-size: 11pt; ">일단 친구에게 파일을 보내달라고 했고, 받은 상태에서 조사를 해보니 PDC 파일은 PDF 에 DRM이 걸린 파일이란다. DRM 이라면, 회사에서 파수, 마크애니, 소캠등을 접해본지라 어디껀가 했는데, **<span style="color: rgb(255, 0, 0); ">LockLizard</span>** 라는 회사이다. (이건 먼 듭보잡.) 뭐 아무튼, 친구에게 받은 파일에는 pdc 파일과 함께 키 파일이 함께 있었다. </span>

<span style="font-size: 11pt; ">어떻게 할까 생각을 해 봤다. </span>

<span style="font-size: 14pt; ">1) 락을 해제한다. </span>

<span style="font-size: 11pt; ">– 잠깐 몇개의 락 해제 사이트 및 프로그램을 설치해서 테스트 결과 잘 돼지가 않는다. 그리고 일단 이 방법은 나의 아까운 주말을 날릴 위험이 있다는 판단하에 접었다. </span><span style="font-size: 11pt; "> </span>

<span style="font-size: 14pt; ">2) 스크린 캡쳐</span>

<span style="font-size: 11pt; ">– 친구가 스크린 캡처가 안된다고 했는데, 이 방법 만큼 확실할 것도 없다는 생각이 들었다. 더 솔직히는 스크린 캡처한 이미지를 인터넷에 공짜로 뿌리고 싶은 욕구가 있었다.(<span style="color: rgb(255, 0, 0); ">인터넷의 공유시스템을 방해하는게 너무 기분 나빴다.</span>)</span>

<span style="font-size: 11pt; ">일단 문서를 봐야 하기 때문에 LockLizard 사이트에 들어가서 viewer  를 다운 받았다. viewer 를 설치하고 pdc  파일을 열라고 하니, 무슨 키에 대한 이야기가 나온다. 아까 친구한테 받을 키를 더블클릭하고 다시 문서를 여니, 보인다. </span>

<span style="font-size: 11pt; ">  
</span>

![](http://ash84.net/wp-content/uploads/1/cfile9.uf.142F234A5070EAF43987D4.jpg)

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">자, 이제 캡처를 해 보자. </span>

<span style="font-size: 11pt; color: rgb(0, 130, 153); ">1) PrintScrenn 버튼 </span>

<span style="font-size: 11pt; ">일단 일반적으로 캡처시 사용하는 PrintScreen 버튼을 클릭해보았다. 별 이상은 없었으나, 그림판에 다가 붙여넣기를 하니 아무것도 나오지 않았다. 그래, 이정도는 막겠지 라는 생각은 하고 있었다. </span>

<span style="font-size: 11pt; color: rgb(0, 130, 153); ">2) Win7 캡처툴 사용하기 </span>

<span style="font-size: 11pt; ">– 우리의 마이크로소프트는 또 친절하게 보조프로그램에 캡처프로그램을 넣어 두셨다. 해당 프로그램을 실행한 결과 아래의 오류 화면이 뜬다. 애기인 즉, “문서 볼려면, SnippingTool.exe 쓰지마라.” 헐.. SnippingTool.exe 라는 이름으로 프로세스 체킹을 하는것 처럼 보인다. </span>

<span style="font-size: 11pt; ">  
</span>

![](http://ash84.net/wp-content/uploads/1/cfile27.uf.1371844A5070EB160584DB.jpg)

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; color: rgb(0, 130, 153); ">3) 갈무리!!</span>

<span style="font-size: 11pt; ">– 이것 만은 사용하지 않을려고 했는데.. 국산 소프웨어의 자존심. 갈무리다.(kalmuri) 이건 프로세스 이름으로 체킹을 하기 때문에 당연 실행시에 걸리지 않는다. ㅎㅎ 그러나 실행하자마자, 나온 메시지에 보면 PrintScreen 키를 다른 프로그램에서 사용하고 있단다. <span style="color: rgb(204, 61, 61); ">즉, LockLizard viewer 에서 사용하고 있다는 것이다.(한번 해보자 이거지.)</span></span>

<span style="font-size: 11pt; "><span style="color: rgb(204, 61, 61); ">  
</span></span>

<span style="font-size: 11pt; ">  
</span>

![](http://ash84.net/wp-content/uploads/1/cfile24.uf.011CB7365070EB2B186D26.jpg)

<span style="font-size: 11pt; "><span style="color: rgb(204, 61, 61); ">  
</span></span>

<span style="font-size: 11pt; ">갈무리의 스크린캡처 버튼 기본 세팅은 PrintScreen 버튼으로 되어 있다. 트레이 아이콘에서 갈무리를 찾아서 눌러보면 단축키를 바꿀수 있는  기능이 있다.(진짜 갈무리는 대한민국 소프트웨어 대상감이다.) 나는 F11 버튼으로 바꾸었다. </span>

<span style="font-size: 11pt; ">  
</span>

![](http://ash84.net/wp-content/uploads/1/cfile25.uf.0117CC385070EB39210AAF.jpg)

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">자, 이제 준비는 끝났다. 파티 시작. </span>

<span style="font-size: 11pt; ">viwer를 전체 화면으로 두고, 갈무리를 전체 사이즈로 두고 왼손을 F11키에 오른손은 PageDown 에 올리고 고!!</span>

<span style="font-size: 11pt; ">  
</span>

![](http://ash84.net/wp-content/uploads/1/cfile1.uf.121362385070EB4626F7BE.jpg)

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; line-height: 2; ">100page 짜리 문서 캡처뜨는데, 3분이 안걸렸다. </span>

<span style="font-size: 11pt; ">크윽, 이 쾌감!! 뭔가 막힌게 뻥 뚫려서, 아우토반이 된 느낌!!</span>

<span style="font-size: 11pt; ">정리하자면, </span>

<figure class="wp-caption aligncenter" style="width: 500px">![](http://ash84.net/wp-content/uploads/1/cfile9.uf.193DD8495070EA4B340DDD.jpg)<figcaption class="wp-caption-text">개나리들아. 내친구 괴롭히지마. </figcaption></figure>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">인간적으로 인터넷에 올릴거고, 또 돈 받고 팔거면 어려운 DRM 걸지말자. 나 같은 사람들이 용서치 않는다. 저작권이고 나발이고, 돈 지불했으면 값을 해야지. 뒤질려구. </span>



