---
title: '[C#] DotNetBar 이용하기'
author: 'ash84'
pub_date: '2015-07-03'
description: 'Office 2007 부터 리본시스템이 UI에 도입되면서 UX의 개념이 나오기 시작한것 같다. 자주 사용하는 메뉴를 사용자가 보편적으로 자주 사용하는 곳에 배치함으로써 좀더 사용성을 증가 시킨다는 것은 사람과 컴퓨터 사이를 좀더 가깝게 만들어 주는 하나의 혁신이라고 볼수가 있다. 하지만, 일반 Visual Studio 2008의 Windows Applicatio'
featured_image: ''
tags: ['dev', 'DotNetBar', 'Office2007 개발 UI', 'Ribbon Control', 'UI', '닷넷바']
---


<div style="TEXT-ALIGN: justify; MARGIN-LEFT: 4em">  
</div>  
<div style="TEXT-ALIGN: justify">Office 2007 부터 리본시스템이 UI에 도입되면서 UX의 개념이 나오기 시작한것 같다. 자주 사용하는 메뉴를 사용자가 보편적으로 자주 사용하는 곳에 배치함으로써 좀더 사용성을 증가 시킨다는 것은 사람과 컴퓨터 사이를 좀더 가깝게 만들어 주는 하나의 혁신이라고 볼수가 있다. 하지만, 일반 Visual Studio 2008의 Windows Application에서는 이러한 리본바(Bar)를 기본적으로 제공하지 않기 때문에 엔터프라이즈 업체에서 제공하는 Office 2007 분위기 및 각종 UI Component를 구입해서 사용해야 한다.

그중 필자가 근 3개월 동안 프로젝트를 통해 사용한 **<font color="#5c7fb0">DotNetBar</font>**를 소개하겠다.

DotNetBar에서는 다양한 형태로 MS 닷넷시스템의 UI를 제공하고 있다. Windows Forms 뿐만 아니라, WPF를 지원해주고 있으며, ICON Pack역시 제공해 주고 있다. 또한 <font color="#c8056a">TreeGX 라는 트리구조 및 브레인스토밍 형태의 UI를 제공해 주고 있다.   
</font>  
![](http://ash84.net/wp-content/uploads/1/cfile28.uf.2065A3044AF8B99EA1F647.jpg)

**<font color="#c8056a">DotnetBar for Windows Forms</font>**

Windows Forms를 중점적으로 설명하면, 기본적으로 Ribbon Control이 제공되며 여러가지 스타일의 형태로 쉽게 속성(Properties)를 통해서 변화시킬수 있다. <font color="#c8056a">때문에 사용자의 윈도우 테마가 바뀜으로 인해서 생기는 UI 스타일의 변화를 막을수가 있다.   
</font>  
![](http://ash84.net/wp-content/uploads/1/cfile22.uf.196711014AF8BA5742AE1C.jpg)  
 그 밖에도 TabControl의 경우 여러가지 스타일을 통해서 Tab위의 모양을 바꿀수가 있으며 GroupBox의 경우 기존의 기본적으로 제공하던 GroupBox는 왼쪽으로 텍스트가 고정되어 있었지만, 가운데에 있는 GroupBox를 사용할수 있다.

![](http://ash84.net/wp-content/uploads/1/cfile23.uf.15658F034AF8BCA35C9812.jpg)  
![](http://ash84.net/wp-content/uploads/1/cfile8.uf.125F6D024AF8BCAD5BD4C9.jpg)

또한 슬라이더 컨트롤이 있어서 파워포인트 하단의 화면의 확대 축소 시키는 슬라이더와 같은 UI를 가질수 있게 되었고, DateTimePicker 역시 사용자가 다양한 표시를 할수 있도록 제공되었다. <font color="#c8056a">Reflection Image라는 것은 기존에는 없던것인데, 마치 이미지가 물 위에 떠서 물에 이미지가 비치는 듯한 효과를 줄수 있게 되었다.   
</font>

![](http://ash84.net/wp-content/uploads/1/cfile1.uf.17725F054AF8BD0666C7BA.jpg)

![](http://ash84.net/wp-content/uploads/1/cfile4.uf.19725F054AF8BD0767A053.jpg)

![](http://ash84.net/wp-content/uploads/1/cfile4.uf.20725F054AF8BD07680DB1.jpg)

<font color="#c8056a">Rating Control의 경우는 별표 표시를 통해서 점수를 매길수 있는 형태의 UI 컨트롤이 제공되었으며,ProgrssBar 역시 다양한 표현을 가능하게 하였다.</font> Color Picker 역시 Office 2007에서 사용하던 다양하고 아기자기한 컨트롤을 사용할수 있게 제공하고 있다.

 전반적으로 살펴보면, 기존에 있는 컨트롤을 강화시키고 스타일의 다양성을 많이 추가한 형태로 변화하면서도 윈도우 프로그램에는 있는데, 개발자가 개발에 쓸수 없었던 컨트롤들이 많이 추가되었다. 필자가 DotNetBar를 이용해서 개발을 해본결과 간단한 PowerPoint도 만들수 있다는 생각이 들었다.

현재 DotnetBar는 유료로 다음과 같은 가격으로 개발자에게 판매하고 있는 상황이다.

![](http://ash84.net/wp-content/uploads/1/cfile4.uf.16193E0C4AF8BEF0848387.jpg)

맛뵈기로 사용하기 위해서는 Trial Version을 다운 받아서 사용할수 있으나, 앞에서 설명한 것 외의 다양하고 많은 컨트롤을 자유롭게 사용하기 위해서는 역시 구입을 해야한다. 필자도 현태 Trial Version을 사용하고 있지만, 프리랜서로 Application 에 몇몇 효과를 주기 위해서 사용하기에는 안성맞춤인것 같다.

홈페이지 : [http://www.devcomponents.com/](http://www.devcomponents.com/)

[#M_Tip : Trial Version을 영구히 사용하는 법 |접기|  
 Trial Version은 기한이 정해져 있기 때문에 영구히 사용하려면 Crack을 설치해야 한다. Google에서 DotNetBar Crack이라고 검색하면 DBCrack 파일을 다운 받을수 있을 것이다. Trial Version을 설치후, DBCrack를 설치하고 해당 DLL을 추가하면 Visual Studio에서 Trial Version에 한해서만 영구적으로(?) 사용할수 있다.

[http://appzfreew.com/devcomponents-dotnetbar-v8-1-0-7-free-download-crack-serial.html](http://appzfreew.com/devcomponents-dotnetbar-v8-1-0-7-free-download-crack-serial.html)

_M#]

</div>

