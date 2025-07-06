---
title: '[폰트 관련 특집] 1. 유니코드와 폰트와의 관계에 대해서.'
author: 'ash84'
pub_date: '2010-08-30'
description: '이번 프로젝트를 하면서 폰트를 개발하고'
featured_image: ''
tags: ['font', 'Unicode', '유니코드', '폰트']
---


<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<font size="2"><font face="맑은 고딕"><font color="#000000"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">이번 프로젝트를 하면서 폰트를 개발하고</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">, </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">폰트를 프로그램에 적용하면서 알게 된 여러 가지 사항에 대해서 포스팅 하고자 합니다</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">. </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">크게</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; "> 3</span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">가지 범주로 나누었는데요</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">. </span></span></span></font></font></font>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; "> </span></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<font size="2"><font face="맑은 고딕">**<font color="#e31600"><span style="mso-fareast-font-family: '맑은 고딕'; mso-fareast-theme-font: minor-latin"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">① </span></span></span><span style="mso-fareast-font-family: '맑은 고딕'; mso-fareast-theme-font: minor-latin"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">유니코드와 폰트와의 관계</span></span><span></span></span></font>**</font></font>

<span style="font-size: 11pt; ">  
</span>

<font size="2"><font face="맑은 고딕"><font color="#000000"><span style="mso-fareast-font-family: '맑은 고딕'; mso-fareast-theme-font: minor-latin"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">② </span></span></span><span style="mso-fareast-font-family: '맑은 고딕'; mso-fareast-theme-font: minor-latin"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">폰트를 제작학기 위한 툴</span></span><span></span></span></font></font></font>

<span style="font-size: 11pt; ">  
</span>

<font size="2"><font face="맑은 고딕"><font color="#000000"><span style="mso-fareast-font-family: '맑은 고딕'; mso-fareast-theme-font: minor-latin"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">③ </span></span></span><span style="mso-fareast-font-family: '맑은 고딕'; mso-fareast-theme-font: minor-latin"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">폰트를 어떻게 개발에 이용할 것인가</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">?</span></span></span></span></font></font></font>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; "> </span></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<font size="2"><font face="맑은 고딕"><font color="#000000"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">그래서 처음에는 유니코드와 폰트와의 관계에 대해서 이야기를 하고</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">, </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">그리고 폰트를 개발하기 위해서는 어떤 툴을 쓰고 툴의 사용법 및 몇 가지 유용한 툴에 대해서 설명 드리겠습니다</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">. </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">그리고 어떻게 개발된 폰트를 실제 프로그램에서 적용할 것인지에 대해서 알아 보겠습니다</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">. </span></span></span></font></font></font>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; "> </span></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; "> </span></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<font color="#000000">**<span style="mso-fareast-font-family: '맑은 고딕'; mso-fareast-theme-font: minor-latin; mso-bidi-font-family: '맑은 고딕'; mso-bidi-theme-font: minor-latin"><span style="mso-list: Ignore"><font face="맑은 고딕" size="2"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">1.</span></span></font><span style="FONT: 7pt 'Times New Roman'"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">     </span></span></span></span></span>****<font size="2"><font face="맑은 고딕"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">유니코드와 폰트와의 관계</span></span><span></span></font></font>**</font>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; "> </span></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<font size="2"><font color="#000000"><font face="맑은 고딕"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">유니코드</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">(Unicode)</span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">는 간단하게 설명하자면</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">, </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">세상에 있는 문자</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">, </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">기호들을 정리해놓은 전화번호부 같은 역할을 한다고 보시면 될 것 같습니다</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">. </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">그래서 영어</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">, </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">한글의 모든 글자에는 각각 겹치지 않는 일련번호를 매긴 것을 유니코드라고 생각하시면 될 것 같습니다</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">. </span></span></span></font></font></font>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; "> </span></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<font size="2"><font color="#000000"><font face="맑은 고딕"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">각 나라별 유니코드에 대한 것은 매년 업데이트가 되어서 공개되고 있고 누구나 들어가서</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; "> PDF </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">로 된 문서를 볼 수 있습니다</span></span><span><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="font-size: 11pt; ">. </span>  
<span style="font-size: 11pt; ">  
</span>  
</span></span></span></font></font></font>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; "> </span></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<font size="2"><font color="#000000"><font face="맑은 고딕"><span><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"></span></span></span></font></font></font>

<font size="2"><font color="#000000"><font face="맑은 고딕"><figure class="wp-caption aligncenter" style="width: 600px">![](http://ash84.net/wp-content/uploads/1/cfile3.uf.160FD7244C7B604211171A.jpg)<figcaption class="wp-caption-text">http://www.unicode.org/charts/</figcaption></figure></font></font></font>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; "> </span></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<font size="2"><font color="#000000"><font face="맑은 고딕"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">그렇기 때문에 글자의 모양을 나타내는 폰트 역시 유니코드와의 매핑</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">(Mapping)</span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">이 없으면 사용자가 아무리 </span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">“A” </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">라는 글자를 입력해도</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; "> MS</span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">워드에는 해당 폰트가 적용된 모습을 볼 수가 없을 수가 있습니다</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">. </span></span></span></font></font></font>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; "> </span></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<font size="2"><font color="#000000"><font face="맑은 고딕"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">간단히 문자에 대한 유니코드가 궁금하시다면</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; "> MS</span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">워드에서 삽입에 기호를 누르시면 문자표가 뜨는데 거기서 </span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">“A” </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">를 누르면 유니코드가 </span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">“0041” </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">이라는 것을 알 수가 있습니다</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">. </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">자세히 보시면 하위집합이라 되는 것을 눌러보면</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">, “</span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">기본 라틴문자</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">”, “</span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">라틴어 확장</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">-A”, “</span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">라틴어 확장</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">-B” </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">이렇게 나오는것을 볼수 있는데</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">, </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">이것은 한글오피스에서도 비슷하게 나옵니다</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">. </span></span></span></font></font></font>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="font-size: 11pt; "> </span>  
<span style="font-size: 11pt; ">  
</span></span></span></font></span><font size="2"><font color="#000000"><font face="맑은 고딕"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">  
<span style="font-size: 11pt; ">  
</span>**<span style="font-size: 11pt; ">왜 둘 다 비슷한 하위집합을 보여줄까요</span>**</span></span><span><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">**<span style="font-size: 11pt; ">?</span>**</span></span></span></font></font></font>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; "> </span></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; "> </span></span></font></span><font size="2"><font color="#000000"><font face="맑은 고딕"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">그 답은 유니코드에 있습니다</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">. </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">기본적인 분류 자체가 유니코드에 있는 것을 따르기 때문에 대부분의 워드프로세스에서 제공하는 문자표 역시 유니코드의 체계를 따르는 것입니다</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">. </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">대부분의 문자는 유니코드와</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; "> 1:1 </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">매핑</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">(Mapping)</span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">이 되어 있습니다</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">. </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">영문자의 경우</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">, </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">대문자 뿐만 아니라 소문자도 매핑이 다 되어 있습니다</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">. </span></span></span></font></font></font>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="font-size: 11pt; "> </span>  
<span style="font-size: 11pt; ">  
</span></span></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<font size="2"><font color="#000000"><font face="맑은 고딕">**<span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">  
<span style="font-size: 11pt; ">  
 한글의 경우는 어떠할까요</span></span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">?</span></span></span>**</font></font></font>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; "> </span></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<font size="2"><font color="#000000"><font face="맑은 고딕"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">한글은 조합자기 때문에 초성</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">, </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">중성</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">, </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">종성이 매핑 되어 있고 모든 조합된 글자들이 매핑이 되어 있습니다</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">. </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">그래서 실제로 우리가 생활에서는 쓰지 않는 아래와 같은 글자가 실제 유니코드에는 매핑이 되어 있는 것입니다</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">. </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">한국어는 자음 과 모음으로 구성되어 있기 때문에 그 조합 역시 굉장히 많은 수를 자랑합니다</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">. </span></span></span></font></font></font>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; "> </span></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<font color="#000000"><font face="맑은 고딕"><span style="FONT-SIZE: 24pt; mso-fareast-font-family: '맑은 고딕'; mso-fareast-theme-font: minor-latin"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">**<span style="font-size: 11pt; ">벫볠볡볢</span>**</span></span></span><span style="FONT-SIZE: 24pt"></span></font></font>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; "> </span></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; "> </span></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<font size="2"><font color="#000000"><font face="맑은 고딕"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">폰트와 유니코드는 뗄래야 뗄 수가 없습니다</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">. </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">그래서 대부분의 폰트 툴에서 어떤 글자에 대한 이미지를 만들어 놓은 후 폰트로 만들 때에는 반드시 유니코드를 매핑 하게 되어 있습니다</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">. </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">제가 앞으로 소개할 폰트 크리에이터</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">(Font Creator)</span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">라는 프로그램에서도 역시 매핑을 하게 되어 있습니다</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">. </span></span></span></font></font></font>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; "> </span></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<font size="2"><font color="#000000"><font face="맑은 고딕"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">때문에 폰트를 개발하신다고 하면 기본적으로 어떤 언어를 대상으로 할지 그리고 어떤 유니코드 영역에 폰트를 넣으실 지에 대해서 유념을 하셔야 할 것 입니다</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">. </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">또 생각해 보면 </span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">“A”</span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">라는 글자를 눌렀을 때 글자가 아닌 어떤 이미지를 뜨게 할 수도 있겠지요</span></span><span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">. </span></span></span><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">한번 활용해 보면 좋을 것 같습니다</span></span><span><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="font-size: 11pt; ">. </span>  
<span style="font-size: 11pt; ">  
</span>  
</span></span></span></font></font></font><span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="font-size: 11pt; ">ps) 잘못된 부분이 있거나, 더 추가해야 하는 부분이 있으면 주저하지 말고 댓글로 남겨주십시오. </span>  
<span style="font-size: 11pt; ">  
</span></span></span></font></span>

<span style="font-size: 11pt; ">  
</span>

<span><font color="#000000" face="맑은 고딕" size="2"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt">  
</span></span></font></span>



