---
title: 'WPF example - CONTOSO Healthcare System'
author: 'ash84'
pub_date: '2015-07-03'
description: '![사용자 삽입 이미지](http://ash84.net/wp-content/uploads/1/gl138.png)

  
 강성재님의 MS 세미나에서 보았던 예제중 하나다. 조금은 내게 아이디어를 주었던 자료. 
  
 이전 랩미팅때 About .NET Framework3.0 라는 주제로 발표할건데, WPF(Windows Presentation Foundation) 부분에 대한 예제로 첨가할 예정이다. </'
featured_image: ''
tags: ['.Net Framework 3.0', 'contoso', 'dev', 'healthcare system', 'Prototype', 'WPF']
---


![사용자 삽입 이미지](http://ash84.net/wp-content/uploads/1/gl138.png)

<span style="font-size: 11pt;">  
 강성재님의 MS 세미나에서 보았던 예제중 하나다. 조금은 내게 아이디어를 주었던 자료. </span>  
<span style="font-size: 11pt;">  
 이전 랩미팅때 About .NET Framework3.0 라는 주제로 발표할건데, WPF(Windows Presentation Foundation) 부분에 대한 예제로 첨가할 예정이다. </span>  
<span style="font-size: 11pt;">  
 (WPF에 대해서는 About .NET Framework 3.0 완성후 , 올리겠습니다.)</span>  
<span style="font-size: 11pt;">  
</span>  
<span style="font-size: 11pt;">WPF에 대한 서적은 거의 없는 실정이다. 하나정도 두껍게 해서 출판 되었다고 했는데 </span>  
<span style="font-size: 11pt;">  
 아직 보지 못해서 모르겠지만, 그래도 네이버 블로그나 다수의 블로거들, 즉 블로그를 운영</span>  
<span style="font-size: 11pt;">  
 하시는 개발자 분들이 WPF 에대한 스터디 자료들을 많이들 올려놔 주셨다. </span>  
<span style="font-size: 11pt;">  
</span>  
<span style="font-size: 11pt;">이 예제는 그냥 돌려 보거나 혹은 시간이 된다면, 안에 소스파일을 훑어 보는것도 좋은일일것</span>  
<span style="font-size: 11pt;">  
 같다. 한가지 주의할점은, 노트북이나 혹은 사양이 낮은 컴퓨터에서는 버벅거린다는점이다. </span>  
<span style="font-size: 11pt;">  
 원래는 OTTO 의 쇼핑몰 예제를 보여드릴려구 햇는데, 그건정말 심하게 버벅거리고 설치가 어렵다. </span>  
<span style="font-size: 11pt;">  
</span>  
<span style="font-size: 11pt;">  
</span>

<div style="PADDING-RIGHT: 10px; PADDING-LEFT: 10px; PADDING-BOTTOM: 10px; PADDING-TOP: 10px; BACKGROUND-COLOR: #ffdaed"><span style="font-size: 11pt;">프로토 타입이긴 하지만, 이 CONTOSO HealthCare System의 장점 </span>  
<span style="font-size: 11pt;">  
</span>  
<span style="font-size: 11pt;">– 기술적인 장점 : WPF는 기본적으로 Standalone형태의 윈도우 어플리케이션과 XBAP(웹에서 실행되는) 지원 하기때문에 이 시스템이 사용자에게 두가지 측면에서 접근이 가능하다. 즉, 의사나 병원 관계자에게는 일반 윈도우 어플리케이션이 편하겠지만, 변형시켜서 환자나 관계자 대상이라면, 어디서나 접속이 가능한, 웹쪽이 편할것으로 예상되어 진다. </span>  
<span style="font-size: 11pt;">  
</span>  
<span style="font-size: 11pt;">또한 </span>**<span style="font-size: 11pt;">“가젯형태”</span>**<span style="font-size: 11pt;"> 로 인스톨이 가능하기 때문에 프로토타입이긴 하지만, 새로운 패러다임을 불러 올수 있을것으로 예상되어 진다. </span>  
<span style="font-size: 11pt;">  
</span></div><span style="font-size: 11pt;"></span>

<div style="PADDING-RIGHT: 10px; PADDING-LEFT: 10px; PADDING-BOTTOM: 10px; PADDING-TOP: 10px; BACKGROUND-COLOR: #faffa9"><font color="#003366">**<span style="font-size: 11pt;">– 의료정보공학적 관점</span>**  
<span style="font-size: 11pt;">  
</span>  
<span style="font-size: 11pt;">: 사실상 user에 대한 고려에 대한 부분은 빼놓을수 없을 정도로 중요하다. 인터페이스의 고착성이라는 관점에서 보면, 기존의 병원정보시스템(HIS) 혹은 EMR 시스템의 인터페이스는 고정적(fixed)이고, 사용자가 익히는데 어느정도의 시간을 필요로 한다. </span>  
<span style="font-size: 11pt;">  
</span>  
<span style="font-size: 11pt;">하지만, 위에서 프로토타입으로 제시한 인터페이스는 매우 쉽다. 무엇보다도 저런 형태라면, </span>  
<span style="font-size: 11pt;">  
 환자별로 customized 된 인터페이스를 제공할수 있다고 생각하고 그것이 웹이나 window application 이 아닌, 가젯이나 혹은 PDA, SMARTPHONE의 단말기의 인터페이스의 형태로 들어가게 된다면, 그에 대한 효과는 엄청날 것으로 보인다. </span>  
<span style="font-size: 11pt;">  
</span>  
<span style="font-size: 11pt;">단점도 있다. 환자에겐 좋을수도 있지만, 정확한 데이터를 요구하는, 혹은 의료영상과 같은 </span>  
<span style="font-size: 11pt;">  
 해상도가 큰 영상을 판독해야 하는 의사에게 저런 시스템은 버벅거리기만 하는 별볼일 없는 시스템이 될수도 있다. 물론, 이것은 개발상의 타겟팅의 문제라고 생각한다. </span>  
<span style="font-size: 11pt;">  
</span></font></div><span style="font-size: 11pt;">  
</span>**<font color="#d41a01"><u><span style="font-size: 11pt;">LINK : </span>[**<font color="#d41a01"><u><span style="font-size: 11pt;">CONTOSO Healthcare System prototype</span></u></font>**](http://wpf.netfx3.com/files/folders/applications/entry6608.aspx)</u></font>**



