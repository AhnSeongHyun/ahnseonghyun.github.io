---
title: '.NET Compact Framework Sample: P/Invoke Library'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['.NET Compact Framework', 'dev', 'P/Invoke', 'Wince', 'wince 6.0', '녹음', '메모리상태', '오디오출력', '폴더관련']
---


<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><font face="굴림"></font>  
<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">.NET Compact Framework Sample: P/Invoke Library는 프레임워크에서 다 커버하지 못하는 기존의 native code의 소스들을 P/Invoke를 통해서 연결해 주는 샘플 라이브러리다. 해당목록을 나열하면 다음과 같다.</span></span></span></span>  
<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"> </span></span></span></span></span></span></div>  
  
- <span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">오디오 출력 및 녹음</span></span></span></span></span></span>
  
- <span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">가상키보드(SIP) 및 키보드 관련 </span></span></span></span></span></span>
  
- <span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">폴더 관련 </span></span></span></span></span></span>
  
- <span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">메모리 상태 관련</span></span></span></span></span></span>
  
- <span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">시간관련 </span></span></span></span></span></span>
  
- <span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">전원상태 관련 </span></span></span></span></span></span>
  
- <span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">시스템 리셋</span></span></span></span></span></span>

  
  
<span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">P/Invoke는 사실 C언어나 C++을 한 사람들이라도 해당 영역에 대해서 해보지 못한 사람들이라면 사실 어렵다. 특히, C#인 경우 임베디드 레벨에서는 native 소스코드로 된 것이 훨씬 많기 때문에 기능에 따라서 P/Invoke가 필수적이다. 컴퓨터에 설치한후, 프로젝트를 열어서 소스를 볼수가 있다. CS, VB로 나누어져 있기 때문에 자신의 개발언어에 맞춰서 보면 유용하다. 열면 모바일플랫폼으로 되어있지만, Wince 6.0 에서도 실행된다. </span></span></span></span></span></span><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">참고 하시길. </span></span></span></span></span></span>

<span style="FONT-SIZE: 11pt"><span style="FONT-FAMILY: Dotum"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">링크 </span></span></span></span>

  
<div class="txc-textbox" style="BORDER-BOTTOM: #cbcbcb 1px solid; BORDER-LEFT: #cbcbcb 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #ffffff; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #cbcbcb 1px solid; BORDER-RIGHT: #cbcbcb 1px solid; PADDING-TOP: 10px">[http://www.microsoft.com/downloads/details.aspx?FamilyId=B1F5CCAA-ADA2-42D4-8B70-95DC7D8F678C&displaylang=en](http://www.microsoft.com/downloads/details.aspx?FamilyId=B1F5CCAA-ADA2-42D4-8B70-95DC7D8F678C&displaylang=en) [  
](http://www.microsoft.com/downloads/details.aspx?FamilyId=B1F5CCAA-ADA2-42D4-8B70-95DC7D8F678C&displaylang=en)</div>  
  
  



