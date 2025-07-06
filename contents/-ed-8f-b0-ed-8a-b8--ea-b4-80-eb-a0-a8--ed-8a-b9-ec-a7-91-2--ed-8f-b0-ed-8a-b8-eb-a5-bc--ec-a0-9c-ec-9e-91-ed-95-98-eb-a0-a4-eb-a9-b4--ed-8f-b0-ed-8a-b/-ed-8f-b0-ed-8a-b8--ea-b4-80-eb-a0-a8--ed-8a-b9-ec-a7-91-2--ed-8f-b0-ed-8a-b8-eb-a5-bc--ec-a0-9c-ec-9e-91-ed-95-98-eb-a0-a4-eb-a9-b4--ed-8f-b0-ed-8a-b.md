---
title: '[폰트 관련 특집] 2. 폰트를 제작하려면? 폰트 개발 툴이 필요하죠~'
author: 'ash84'
pub_date: '2010-09-01'
description: '[앞 시간에 이어서'
featured_image: ''
tags: ['font', 'font craetor', 'font struct', '폰트', '폰트 제작', '폰트제작 툴']
---


<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<font size="2"><font color="#000000"><font face="맑은 고딕">[<span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">앞 시간에 이어서</span></span>](http://ash84.tistory.com/632 "[http://ash84.tistory.com/632]로 이동합니다.")<span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">, 폰트관련 두 번째 시간!!. </span></span>  
<span style="font-size: 11pt; ">  
</span></span>  
<span style="font-size: 11pt; ">  
</span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">많이들 기대를 하셨을 거라 예상을 하면서 시작합니다.^^ </span></span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">폰트를 제작하는 방법에 대해서 알아보겠습니다</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">폰트를 개발 한다는 표현 보다는 폰트를 그린다는 말이 더 맞을 것 같습니다만</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">, </span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">저 역시 폰트를 전문적으로 하시는 분들 보다는 잘 모르기 때문에 비 전문가적인 접근일 수 있음을 미리 알려드립니다</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span></font></font></font>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; "> </span></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<font size="2"><font color="#000000"><font face="맑은 고딕"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">우선</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; "> 2</span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">가지 폰트제작 프로그램을 소개하겠습니다</span></span><span><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">. </span>  
<span style="font-size: 11pt; ">  
</span>  
</span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">하나는 </span></span>**<span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">폰트 크리에이터</span></span>**<span>**<span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">(Font Creator)</span></span>**<span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; "></span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">라는 프로그램이구요</span></span><span><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">, </span>  
<span style="font-size: 11pt; ">  
</span></span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">다른 하나는 </span></span>**<span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">폰트 스트럭</span></span>**<span>**<span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">(Font Struct)</span></span>**<span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; "></span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">입니다</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span></font></font></font>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; "> </span></span></font></span>

<span style="font-size: 11pt; ">  
</span>

**<font size="2"><font color="#000000"><font face="맑은 고딕"><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">1. </span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">이미지 기반의 폰트 제작 프로그램</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; "> : </span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">폰트 크리에이터</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">(Font Creator)</span></span></span></font></font></font>**

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; "> </span></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<font size="2"><font color="#000000"><font face="맑은 고딕"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">폰트 크리에이터 프로그램은 제가 이번 프로젝트를 하면서 알게 된 프로그램입니다</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">글자 이미지를 바탕으로 폰트를 만들 수 있다는 것이 핵심인데요</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">전문가분들이 사용하는 프로그램보다는 조금 섬세함</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">(detail)</span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">이 떨어 진다는 것으로 알고 있습니다</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">하지만</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">, </span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">파워포인트 자료를 통해서 글자 이미지를 만들어서 사용할 경우엔</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">, </span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">유용하게 쓸 수 있는 프로그램입니다</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">또한 타 프로그램에 비해서 쉽게 웹에서 구할 수 있다는 것이 큰 장점 중 하나 입니다</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">. </span></span>  
<span style="font-size: 11pt; ">  
</span></span></font></font></font>

<span style="font-size: 11pt; ">  
</span><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"></span></span>

<font size="2"><font color="#000000"><font face="맑은 고딕"><figure class="wp-caption aligncenter" style="width: 600px">![](http://ash84.net/wp-content/uploads/1/cfile7.uf.1902EB1D4C7E10C9354AF5.PNG)<figcaption class="wp-caption-text">font creator 5</figcaption></figure></font></font></font>

<font size="2"><font color="#000000"><font face="맑은 고딕">  
<span style="font-size: 11pt; ">  
</span>  
</font></font></font>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-SIZE: 10pt"></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<font size="2"><font color="#000000"><font face="맑은 고딕"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">사실 폰트를 모든언어를 대상으로 개발하기란 쉽지 않습니다</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">이번 프로젝트에서도 대부분의 언어에 대한 폰트를 개발하긴 하였지만</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">, </span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">그 수가 너무 방대하더라구요</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">폰트 크리에이터를 열어서 보시면</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">, </span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">팔레트에 유니코드 숫자가 매겨진 것은 자주 쓰는 글자들 밖에 없는 경우가 있습니다</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">예를 들어</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">, </span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">히브리어나 아랍어를 대상으로 폰트를 만들어야 할 경우에는 팔레트에 그 영역을 유니코드와 함께 잡아 주어야 하는데</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">, </span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">사실상 너무 귀찮은 작업이 아닐 수 가 없죠</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span></font></font></font>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2">  
<span style="font-size: 11pt; ">  
</span><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"></span></span></font></span>

<font color="#000000" face="맑은 고딕" size="2"><figure class="wp-caption aligncenter" style="width: 600px">![](http://ash84.net/wp-content/uploads/1/cfile22.uf.172FDF1C4C7E110630FD92.PNG)<figcaption class="wp-caption-text">개별 폰트편집 화면</figcaption></figure></font>

<font color="#000000" face="맑은 고딕" size="2">  
<span style="font-size: 11pt; ">  
</span></font>

<span style="font-size: 11pt; ">  
</span>

<font size="2"><font color="#000000"><font face="맑은 고딕"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">그럴 경우에는</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">, </span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">기존의 폰트를 불러와서 작업하시는 편이 낫습니다</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">. Arial Unicode MS </span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">라는 폰트는 대부분의 유니코드를 지원하는 폰트이기 때문에 해당 폰트를 불러와서 쓰면 해당 프로그램으로 폰트를 개발하는데 조금 수고를 덜 수가 있습니다</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span></font></font></font>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; "> </span></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; "> </span></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; "> </span></span></font></span>**<font size="2"><font color="#000000"><font face="맑은 고딕"><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">2. </span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">드로잉 기반의 플래쉬 폰트 제작 사이트</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; "> : </span></span></span><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">[<span style="font-size: 11pt; ">폰트 스트럭</span>](http://fontstruct.fontshop.com/ "[http://fontstruct.fontshop.com/]로 이동합니다.")</span></span><span><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">[<span style="font-size: 11pt; ">(Font Struct)</span>](http://fontstruct.fontshop.com/ "[http://fontstruct.fontshop.com/]로 이동합니다.")</span></span></span></font></font></font>**

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; "> </span></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<font size="2"><font color="#000000"><font face="맑은 고딕"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">폰트 스트럭의 가장 큰 장점은 웹</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">/</span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">플래쉬 기반으로 되어 있어서 누구나 쉽게 사용이 가능하다는 것입니다</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">그리고 생각보다 쉬운 폰트 크리에이터 보다 편한</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; "> UI </span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">를 제공하고 있기 때문에 재밌게 폰트를 개발할 수 있는 환경을 제공하고 있습니다</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">. </span></span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"></span></span></span></font></font></font>

<font size="2"><font color="#000000"><font face="맑은 고딕"><figure class="wp-caption aligncenter" style="width: 600px">![](http://ash84.net/wp-content/uploads/1/cfile3.uf.133AF90B4C7E1382372DDA.PNG)<figcaption class="wp-caption-text">폰트 스트럭 편집화면</figcaption></figure></font></font></font>

<font size="2"><font color="#000000"><font face="맑은 고딕">  
<span style="font-size: 11pt; ">  
</span>  
</font></font></font>

<span style="font-size: 11pt; ">  
</span>

<font size="2"><font color="#000000"><font face="맑은 고딕"><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">웹 기반이라고 해서 기능이나 지원하는 언어가 적은것도 아닙니다. 대부분의 언어를 제공하며, 오히려 폰트 크리에이터에서 해줘야 했던 팔레트를 만들거나 유니코드를 매핑해주는 작업을 해주지 않아도 됩니다. 하지만, 이미지를 가져와서 배치시키는 것은 안된다는 단점이 있습니다. 오직 드로잉으로만 폰트를 만들수 있다는 것이 조금 흠이기도 하죠. </span></span>  
<span style="font-size: 11pt; ">  
</span>  
</span></font></font></font>

<span style="font-size: 11pt; ">  
</span>

<font size="2"><font color="#000000"><font face="맑은 고딕"><span>  
<span style="font-size: 11pt; ">  
</span><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"></span></span></span></font></font></font>

<font size="2"><font color="#000000"><font face="맑은 고딕"><figure class="wp-caption aligncenter" style="width: 600px">![](http://ash84.net/wp-content/uploads/1/cfile2.uf.2001D40D4C7E140C4AF93E.PNG)<figcaption class="wp-caption-text">폰트 스트럭 갤러리</figcaption></figure></font></font></font>

<font size="2"><font color="#000000"><font face="맑은 고딕">  
<span style="font-size: 11pt; ">  
</span></font></font></font>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-SIZE: 10pt"></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<font size="2"><font color="#000000"><font face="맑은 고딕"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">또한 웹 기반이다 보니 다른 사용자의 작품들을 볼 수 있는 갤러리 공간을 마련해 주고 있습니다</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">그래서 보면서 새로운 폰트에 대한 영감을 얻을 수 도 있습니다</span></span><span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">. </span></span></span><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">또 그렇게 만든 폰트를 다운로드 받아서 사용해 볼 수 도 있습니다</span></span><span><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">. </span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">두 가지 폰트 개발 관련 프로그램에 대해서 알아보았습니다. 이것 외에도 폰트를 만들수 있는 방법이 많을것이라고 생각되어 집니다. 다른 더 좋은 방법이 있으면, 트랙백 부탁드립니다.^^</span></span></span></span></font></font></font><span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; "> </span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">다음 시간에는 이렇게 많든 폰트를 어떻게 프로그램에 적용할 것인지에 대해서 알아 보는 시간을 갖도록 하겠습니다. 그때까지 아리용~ </span></span></span></font></span><span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; "> </span></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; "> </span></span></font></span>



