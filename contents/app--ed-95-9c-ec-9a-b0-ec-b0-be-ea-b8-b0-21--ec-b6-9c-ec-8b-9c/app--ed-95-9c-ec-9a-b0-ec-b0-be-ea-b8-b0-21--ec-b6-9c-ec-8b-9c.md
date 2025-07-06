---
title: '[App] 한우찾기 2.1 출시.'
author: 'ash84'
pub_date: '2011-10-25'
description: '**한우찾기 2.1을 출시하였습니다.**(we release the app “Search Hanwoo v2.1”)'
featured_image: ''
tags: ['2.1', 'Hanwoo', 'SearchHanwoo', 'SVProgressHUD', '쇠고기이력조회', '찾기', '축산물 등급 판정소', '한우', '한우찾기']
---


**<span style="font-size: 10pt; "><span style="font-family: Dotum; ">한우찾기 2.1을 출시하였습니다.</span></span>**<span class="Apple-style-span" style="line-height: 18px; "><font class="Apple-style-span" color="#8e8e8e">(we release the app “Search Hanwoo v2.1”)</font></span>

<div style="line-height: 2; text-align: justify;"><span class="Apple-style-span" style="background-color: rgb(255, 255, 255); "><div style="text-align: justify;"><span style="font-size: 10pt; "><span style="font-family: Dotum; "> </span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; ">![](http://ash84.net/wp-content/uploads/1/cfile30.uf.146196504EA6DF0D35EFEF.png)</span></span>

</div></span></div><div style="line-height: 2; text-align: justify;"><span class="Apple-style-span" style="background-color: rgb(255, 255, 255); "><span style="font-size: 10pt; "><span style="font-family: Dotum; ">일단, 이번 버전의 특징에 대해서 간단히 설명을 드리자면, 전반적으로 iOS5에서 공통적으로 발생하는 오류를 해결하는데 초점을 맞추었습니다. 특히 애플고딕의 자간이 벌어지는 현상에 대해서 집중적으로 수정을 하였습니다. 그 외에는 메시지 알림표시 자체를 기존의 Activity Indicator 와 UIAlterview를 혼용해서 사용하던 것에서 벗어나서 좀더 개이적으로는 그 모양이 마음에 들지 않았던 것 같아요. 그래서 오픈 소스를 찾다보니, 적당한 메시지 알림 소스가 있어서 추가하게 되었습니다. </span></span></span></div><div style="line-height: 2; text-align: justify;"><span class="Apple-style-span" style="background-color: rgb(255, 255, 255);"><div style="text-align: justify;"></div></span>  
<font class="Apple-style-span" color="#8e8e8e">Once, the features of  this version are the solution of iOS5 bugs. Specially, the<span class="s1"> bug about Apple gothic font of space between letter is fixed. </span>Outside of that, existed message alarm user interface has been consisted of Activity Indicator and UIAlterView, but we change that to the beautiful alarm interface. <span class="Apple-style-span" style="background-color: rgb(255, 255, 255); "></span>Personally, I didn’t like the existed UI. So find open source, and include this project. </font>  
<span class="Apple-style-span" style="background-color: rgb(255, 255, 255); "><div style="text-align: justify;"><span style="font-size: 10pt; "><span style="font-family: Dotum; "> </span></span></div></span></div><span style="font-size: 9pt; background-color: rgb(255, 255, 255);">**<span style="font-size: 10pt; "><span style="font-family: Dotum; ">iOS5 에서 발생했던 애플 고딕 깨짐현상 패치  
</span></span>**</span><span class="Apple-style-span" style="background-color: rgb(255, 255, 255); "><span style="font-size: 10pt; "><span style="font-family: Dotum; "></span></span></span>

<font class="Apple-style-span" color="#8e8e8e">the patch of bug about Apple Gothic at iOS5</font>

<div style="line-height: 2; text-align: justify;"><span style="font-size: 9pt; background-color: rgb(255, 255, 255);">**<span style="font-size: 10pt; "><span style="font-family: Dotum; "> </span></span>**</span></div><div style="line-height: 2; text-align: justify;"><span class="Apple-style-span" style="background-color: rgb(255, 255, 255); "><span style="font-size: 10pt; "><span style="font-family: Dotum; ">일단 저 뿐만 아니라 많은 분들이 겪고 있는 문제이구요. 사실상 애플고딕. 제 생각에는 굉장히 이쁜체라고 생각하고 가장 아아폰, 이름만큼 애플스러운 폰트라고 생각되어서 많은 분들이 앱 내에 사용하셨는데 안타깝게도 이상하게 자간이 벌어지는 문제점이 iOS5 이후에 발생하게 되었습니다.   
  </span></span>  
</span><font class="Apple-style-span" color="#8e8e8e"><span class="Apple-style-span" style="line-height: 18px; ">Once, this problem is common at iOS5. I like Apple Gothic font. It is best font in iPhone. so many people and developers use this font at the their apps. </span><span class="Apple-style-span" style="line-height: 18px; ">But, the problem was happened at iOS5. </span></font></div><div style="line-height: 2; text-align: justify;"><span class="Apple-style-span" style="line-height: 2; background-color: rgb(255, 255, 255);"></span>  
<span class="Apple-style-span" style="line-height: 2; background-color: rgb(255, 255, 255); "></span><span class="Apple-style-span" style="line-height: 2; background-color: rgb(255, 255, 255);"><div style="text-align: justify;"><span style="font-size: 10pt;"><span style="font-family: Dotum;"><font class="Apple-style-span" color="#e31600">어떻게 해결 하였나?</font></span></span></div></span>  
<span class="Apple-style-span" style="line-height: 2; background-color: rgb(255, 255, 255);"><div style="text-align: justify;"><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font class="Apple-style-span" color="#8e8e8e">How to solve the problem?</font></span></span></div></span>  
<span class="Apple-style-span" style="line-height: 2; background-color: rgb(255, 255, 255);"><div style="text-align: justify;"><span style="font-size: 9pt;"></span></div></span>  
<span class="Apple-style-span" style="line-height: 2; background-color: rgb(255, 255, 255);"><div style="text-align: justify;"><span style="font-size: 9pt;"><span style="font-size: 10pt; "><span style="font-family: Dotum; ">사실상 폰트 내장기법을 사용하고자 했으나 몇몇 상용폰트의 저작권 문제도 조금 걸리는 부분이고, 네이버에서 나온 나눔고딕 폰트를 사용하려고 했으나, 추후에 앱의 유료화시 문제될까 싶어서, 일단은 </span></span>**<span style="font-size: 10pt; "><span style="font-family: Dotum; ">Helvetica</span></span>**<span style="font-size: 10pt; "><span style="font-family: Dotum; "> 폰트로 변경하였습니다. 이 폰트를 사용한 이유는 가장 애플고딕 다음으로 수려한 느낌을 받았던것 같습니다. 솔직히 나눔고딕은 아이폰에서 봤을 때는 조금 잘 안보이는 느낌이 있어서 포기했습니다. 적당하게 마음에 드시는 폰트를 지정해서 해결하는 방법이 사실상 최선이 아닌가 싶네요. </span></span></span></div></span>  
<span class="Apple-style-span" style="line-height: 2; background-color: rgb(255, 255, 255);"><div style="text-align: justify;"><span style="font-size: 9pt;"><font class="Apple-style-span" color="#8e8e8e">In fact, I try to save fonts in the app but this has the copyright problem of commercial fonts. And I want to use Nanum-gothic font developed by NHN. but it is not solution. Finally, I use helvetica font. </font>

<font class="Apple-style-span" color="#8e8e8e">The reason of using this font is very beautiful and sharpness like Apple Gothic.  But, NHN Nanum Gothic don’t have sharpness. I think that  you want to solve this problem, you change a fon</font>t. 

</span></div></span>  
<span class="Apple-style-span" style="line-height: 2; background-color: rgb(255, 255, 255);"><div style="text-align: justify;"><span style="font-size: 9pt; "></span><span style="font-size: 9pt;"><span style="font-size: 10pt;"><span style="font-family: Dotum;">**메시지 알림 표시 변경**</span></span></span></div></span><span class="Apple-style-span" style="color: rgb(142, 142, 142); font-family: Dotum; font-size: 13px; line-height: 26px; background-color: rgb(255, 255, 255); ">Change Message Alarm Expression   </span><font class="Apple-style-span" face="Dotum" size="2"><span class="Apple-style-span" style="line-height: 26px;"></span></font>  
<font class="Apple-style-span" face="Dotum" size="2"><span class="Apple-style-span" style="line-height: 26px;"></span></font><span class="Apple-style-span" style="line-height: 2; background-color: rgb(255, 255, 255); "><div style="text-align: justify;"><span style="font-size: 9pt; ">**<span style="font-size: 10pt; "><span style="font-family: Dotum; "> </span></span>**</span></div></span></div><div style="line-height: 2; text-align: justify;"><span style="font-size: 10pt; "><span style="font-family: Dotum; "><figure class="wp-caption aligncenter" style="width: 320px">![](http://ash84.net/wp-content/uploads/1/cfile23.uf.135062454EA6DEE9129EC7.png)<figcaption class="wp-caption-text">SVProgressHUD</figcaption></figure></span></span>

</div>이전 포스팅에서 사용했던 방법을 당신이 포스팅을 해 놓고 왜 당신이 안쓰냐는 그런 말은 하지마세용용. 저는 작가주의 프로그래머이다 보니까 기능보다는 적어도 내 앺에서는만은 심미적인 부분, 새로운 경험을 줄 수 있는 부분에 대해서 좀더 고민하게 되었습니다. 사실 로딩 및 메시지 알림에 대한 표시는 굉장히 중요하다고 생각합니다. 사용자가 헷갈리지 않게 명확하게 사용하는 것도 중요하고, 웹에서 데이터를 가져오는 시간을 적어도 지루하지않게 해 줄수 있다는 점에서 참 좋은것 같아요.

<span style="color: rgb(142, 142, 142);">I written the method of loading view in previous posting. But now I  
 don’t use this method. I am Auteurisme Programmer so i think that the  
 UI/UX is very important than functions. Sometimes I worry how to give  
 new user experience using my application. Actually, i think that the  
 expression of loading and message alarm is very important because the  
 user have to clearly use the app. Also this expression is very good for  
 waiting web data loading. </span>

<div style="text-align: justify; line-height: 2;">  
http://cocoacontrols.com 이라는 사이트에 가시면 코코아 프레임워크 기반의 여러가지 UI 작업에 대한 오픈소스들이 있는데, 다 다운받아서 볼수 있다는 점에서 매우 유용한것같아요. 제가 사용한 것은 그 중에서 SVProgressHUD for iOS 라는 것인데, 싱글톤(Single-ton) 패턴으로 구성되어 있습니다. 이 부분에 대해서는 차후에 소스분석을 통해서 알려드리도록 하겠습니다. </div><div style="text-align: justify; line-height: 2;"></div>http://cocoacontrols.com   
 this site has various UI Open source based on COCOA Framework and you  
 can download to your Mac.. so very useful. I use SVProgressHUD for iOS   
 in this site, this consist of Singleton Pattern. After few postings, I  
 will analyze this source code and notify usage.

그 외에도 전반적으로 개발에 급급해서 떔빵식으로 만들었던 것들에 대해서 정리를 하였구요, 좀더 속도이슈를 보완하기 위해서 UIWebView 의 로딩이 끝난후에 함수를 호출하는 것 대신에 Notification 을 사용해서 코드를 정리하였습니다.

Outside of that,  I make dirty code to clean code. It is very good for  
 me as programmer. To improve speed issue, I replace the previous   
 way(call function after UIWebview loading) to the new way(using  
 notification). 

 ps) – 한우찾기는 2.2까지 개발될 예정입니다. 10/25일 2.2 버전 애플에 심사를 신청하였습니다.  한국 종축개량협회의 API관련 메일을 보냈지만, 사실상 성사될 가능성이 있기 때문에 더 이상 개발할 여지가 없다고 판단되기에 개발은 여기까지 라는 생각이 들었습니다.  유지보수는 하겠지만, 획기적인 기능은 대체적으로 추가하지 않을 예정입니다.  

<span style="color: rgb(142, 142, 142);">ps) – the search hanwoo app is supposed to develop until version 2.2. I  
 apply Apple app store testing at 10/25. Also I send email to AIAK about  
 API, but I think that they don’t cooperate  with me. so I don’t develop  
 this app. But I will maintain this app for my user. </span>



