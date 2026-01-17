---
title: '모바일 게이트웨이에서의 생체 신호 디스플레이에 대한 고찰.'
author: 'ash84'
pub_date: '2008-12-04'
description: '약 한달간 개발해 오고 있는 모바일 게이트웨이에 대해서 오늘 랩 미팅시간에 많은 이야기가 오고 갔다.'
featured_image: ''
tags: ['biosignal display', 'dev', 'gateway', 'healthcare service', 'healthcare system', 'measure biosignal', 'mobile', '게이트웨이이', '생체신호 디스플레이', '생체신호 측정', 'healthcare']
---
<span style="font-size: 11pt;"></span>  
<span style="font-size: 11pt;">  
 약 한달간 개발해 오고 있는 모바일 게이트웨이에 대해서 오늘 랩 미팅시간에 많은 이야기가 오고 갔다. </span>  
<span style="font-size: 11pt;"></span>

<div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">  
</span><font color="#57048c"><span style="font-size: 11pt;">모바일 게이트웨이는 기존의 고정된 헬스케어 및 의료기기가 아닌 착용 및 휴대용 헬스케어 기기를 지원하기 위해서 기존의 핸드폰 및 스마트 폰이 가지고 있는 PAN(Personal Area Network)를 이용해서 데이터를 전송 받고 그것을 다시 센트럴 서버에 전송하는 역할을 하는 움직이는 게이트웨이이다. </span></font>  
<span style="font-size: 11pt;">  
</span>  
<span style="font-size: 11pt;">대상이 되는 생체 신호는 바이탈 사인 관련된 생체 신호와 심전도를 대상으로 하고 있는데, 처음에는 심전도를 대상으로 약 1개월동안 개발을 해왔다. 그런데 오늘 나온 논의 중에 한 부분은 왜 심전도를 Graph로 디스플레이 하지 않는가 라는 질문을 받게 되었고, 필자는 이렇게 대답 하였다. </span>  
<span style="font-size: 11pt;">  
</span>  
<span style="font-size: 11pt;">  
</span><div class="txc-textbox" style="BORDER-RIGHT: #cbcbcb 1px solid; PADDING-RIGHT: 10px; BORDER-TOP: #cbcbcb 1px solid; PADDING-LEFT: 10px; PADDING-BOTTOM: 10px; BORDER-LEFT: #cbcbcb 1px solid; PADDING-TOP: 10px; BORDER-BOTTOM: #cbcbcb 1px solid; BACKGROUND-COLOR: #ffffff"><span style="font-size: 11pt;">  
</span><div style="TEXT-ALIGN: justify"><span style="font-size: 11pt;">  
</span></div><span style="font-size: 11pt;">  
</span>

<div style="TEXT-ALIGN: center"><span style="font-size: 11pt;">” 본 프로그램은 화면이 너무 작아서(블랙잭 스마트폰) 3 channel의 ECG 신호를 </span>  
<span style="font-size: 11pt;">  
 디스플레이 할수가 없습니다.  또한, 사용자가 ECG 신호를 봐도 알수 있는 게 없기 때문에 </span>  
<span style="font-size: 11pt;">  
 디스플레이 부분은 일루러 기능에서 제외하였습니다.”</span>  
<span style="font-size: 11pt;">  
</span></div><span style="font-size: 11pt;">  
</span>

</div></div><span style="font-size: 11pt;">  
</span>

<div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">  
</span>  
<span style="font-size: 11pt;">보통의 PC나 노트북에서 게이트웨이를 개발했을때에는, 사실 ECG나 SpO2 그리고 다양한 신호에 대한 디스플레이 부분은 기기와 연결되는 게이트웨이의 필수 적인 조건이라고 할수 있다. 사용자는 자신이 제대로 측정하고 있는지에 대해서 확인해야하기 때문에 그런 디스플레이 부분이 필요하다. </span>  
<span style="font-size: 11pt;">  
</span></div><span style="font-size: 11pt;">  
</span>

<div style="text-align: center; line-height: 2;"><div class="imageblock dual" style="text-align: center;"><table border="0" cellpadding="0" cellspacing="5" style="margin: 0 auto;"><tbody><tr><td>![](http://ash84.net/wp-content/uploads/1/493761c5a2366EL.jpg)</td><td>![](http://ash84.net/wp-content/uploads/1/493ceb117ee309L.jpg)</td></tr></tbody></table></div><span style="font-size: 11pt;">  
</span>

</div><span style="font-size: 11pt;">  
</span>

<div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">  
</span><font color="#c84205"><span style="font-size: 11pt;">그러나, 모바일 게이트웨이는 기본적으로 스마트 폰에서 개발된 프로그램이기 때문에, 기존의 폰이 가지고 있는 기능을 방해하지 않는 방향으로 개발을 하였다. 이를테면, 전화가 오거나, 문자 메시지를 쓰는 상황에서도 블루투스 통신을 통해서 헬스케어 기기로 부터 데이터를 받을수 있어야 하며, 사용자가 이에 대해서 주시할 필요가 없다는 것이다. </span>  
<span style="font-size: 11pt;">  
</span></font>  
<span style="font-size: 11pt;">  
</span><font color="#318561"><span style="font-size: 11pt;">특히, ECG의 경우에는, 혈압이나 혈당과 같이 수치화 된것이 아니라 Waveform 형태의 생체 신호이기 때문에, 사용자가 ECG 그래프를 볼수 있다고 해서 알수 있는건 측정을 하고 있다는 정보 뿐이다. 자신의 상태에 대해서 바로 알수가 없다.</span>  
<span style="font-size: 11pt;">  
</span></font><span style="font-size: 11pt;"> </span>  
<span style="font-size: 11pt;">  
 디스플레이 부분을 추가하는 것은 어렵지 않다. 그러나 매 순간 들어오는 데이터에 대한 디스플레이가 이루어 져야 한다면, 기존의 블루투스 통신이 켜져 있어서 폰의 배터리를 소모하는데, 디스플레이로 인한 스마트폰 자체의 자원 소모 역시 무시하기 어렵다고 생각한다. </span>  
<span style="font-size: 11pt;">  
</span>  
<font color="#654505"><span style="font-size: 11pt;">필자는 모바일 게이트웨이, 즉, 의료 전문 단말기가 아니라, 기존의 스마트 폰이나, 모바일 폰에서 헬스케어 관련 서비스를 하기 위해서는 가장 중요한 부분이 사용자 편의라고 생각한다. 모바일 폰 사용자에게 언제 어디서나 연락을 취하고 받을수 있다는 것이 메인 기능이지, 사실상 모바일 게이트웨이 기능은 부가의 기능이라고 생각한다.(물론, 이 부분은 사용자의 체감에 따라 다를것으로 사료된다.) 그렇기 때문에, 기존의 사용자의 경험(User Experience)를 방해하지 않는 관점에서 소프트웨어의 개발이 이루어져야 한다고 생각한다. </span>  
<span style="font-size: 11pt;">  
</span></font>  
<span style="font-size: 11pt;">  
 그동안 의료정보 및 의공학 분야에서의 생체신호 디스플레이는 필수적인 요구사항이었지만, 언제 어디서나 측정 가능한 기기들이 증가하고 있으며, 기기자체에서 응급 상황을 감지하는 기기들이 연구되고 있는 상황이기 때문에 모든 신호를 디스플레이할 필요가 없어지고 있는 상황이다. 때문에, 좀더 사용자에 맞는, 사용자를 위한, 상황과 기기를 통해서 매우 중요한 정보만 제공해 줄수 있는 디스플레이로의 전환이 필요하다고 생각한다. </span>  
<span style="font-size: 11pt;"></span><span style="font-size: 11pt;">  
</span></div>

