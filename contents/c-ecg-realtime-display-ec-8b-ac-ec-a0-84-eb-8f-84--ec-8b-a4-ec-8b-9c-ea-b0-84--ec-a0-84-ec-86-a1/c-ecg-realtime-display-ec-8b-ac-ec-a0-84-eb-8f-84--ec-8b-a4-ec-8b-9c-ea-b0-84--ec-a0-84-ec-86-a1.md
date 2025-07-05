---
title: '[C#] ECG  Realtime Display(심전도 실시간 전송)'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['c#', 'dev', 'ECG', 'ECG Display', 'ECG Graph', 'Realtime graph', '실시간 그래프', '심전도 그래프', '심전도 그리기', '심전도 디스플레이', '프로그래밍']
---


<div style="TEXT-ALIGN: justify"><span style="font-family:Arial;">ECG Realtime Display는 윈도우 폼과 그리고 웹에서 가능하다. 그러나 본 포스팅에서는 윈도우 폼에서 디스플레이 하는 부분에 대해서만 다루도록 하겠다. 왜냐하면, 디스플레이하는 방식은 똑같기 때문에 웹 상에 실시간 디스플레이 할수 있는 기술(실버라이트, 스마트 폼)을 이용해서 구성하면 웹 상에서도 디스플레이를 할 수가 있다. </span><span style="font-family:Arial;">본 포스팅에서는, C# with .NET Framework로 개발한 것을 기본으로 설명하도록 하겠다. </span>  
<font face="굴림"><span style="LINE-HEIGHT: 20px"><span style="LINE-HEIGHT: 18px"></span></span></font>  
**<span style="FONT-SIZE: 12pt"><span style="font-family:Arial;">1. UI 구성하기 </span></span>**

</div><div style="TEXT-ALIGN: justify"><font face="Arial" size="4"><span style="LINE-HEIGHT: 24px; FONT-SIZE: 16px">**<span style="LINE-HEIGHT: 18px; FONT-FAMILY: 굴림; FONT-SIZE: 12px; FONT-WEIGHT: normal"><div style="BORDER-LEFT: rgb(0,0,0) 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: rgb(232,232,232); PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: rgb(255,255,255); PADDING-TOP: 3px"><span style="font-size:10pt;"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"></span></span></span></div><div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><font color="#474747"></font><span style="FONT-SIZE: 10pt"><font color="#474747"></font><span style="FONT-FAMILY: Dotum"><font color="#474747"></font><span style="FONT-SIZE: 10pt"><font color="#474747"> </font></span></span></span></span></div></span>**</span></font></div><div style="TEXT-ALIGN: justify">****  
<span style="font-family:Arial;">먼저, ECG를 윈 폼에서 그리기 위해서는 폼에서 그리는 방법 보다는 </span>**<span style="font-family:Arial;">Panel 상에서 그리는 방법</span>**<span style="font-family:Arial;">이 좋다. 왜냐하면, 폼에서 따로 작동해야하는 부분이 있을수도 있기 때문에 Panel 상에서 </span>**<span style="font-family:Arial;">Background color를 검은색 혹은 흰색으로 설정</span>**<span style="font-family:Arial;">하고 배치하는 것이 좋다. 가로세로크기는 사실 몇 Lead ECG 냐에 따라서 다른데, 정상적인 ECG Graph를 표현할수 있고, 사용자가 보기에 너무 크거나 너무 길지 않게 설정하는 것이 좋다. </span><span style="font-family:Arial;"><figure class="wp-caption aligncenter" style="width: 615px">![](http://ash84.net/wp-content/uploads/1/4940a9cfd4e3093.jpg)<figcaption class="wp-caption-text">740 x 270</figcaption></figure>

</span>  
<span style="font-family:Arial;">위의 그림과 같이 그룹 박스 안에 panel을 넣고 그 밑에 ECG 기기에 맞는 명령 설정을 넣어서 구성한 것이다. ECG Gain은 ECG 기기에 명령을 내려서 그래프의 증폭을 의미하는 부분이고, ECG Lead의 부분에서는 기기에 따라 다른데 어떤 lead에서 나오는 그래프를 보여줄 것인가 하는것을 선택할 수가 있다. Lead Type은 3군데에서 측정하는지, 아니면, 5군데에서 측정하는 지에 대해서 설정할 수가 있다.  위의 패널 사이즈는 740, 270 이다. </span>

</div><div style="TEXT-ALIGN: justify">**<span style="font-size:12pt;"><span style="font-family:Arial;">2. 스레드 생성 및 구성 </span></span>**</div><div style="TEXT-ALIGN: justify">**<span style="font-size:12pt;"><font face="Arial"><span style="LINE-HEIGHT: 18px; FONT-FAMILY: 굴림; FONT-SIZE: 12px; FONT-WEIGHT: normal"><div style="BORDER-LEFT: rgb(0,0,0) 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: rgb(232,232,232); PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: rgb(255,255,255); PADDING-TOP: 3px"><span style="font-size:10pt;"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"></span></span></span></div><div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><font color="#474747"></font><span style="FONT-SIZE: 10pt"><font color="#474747"></font><span style="FONT-FAMILY: Dotum"><font color="#474747"></font><span style="FONT-SIZE: 10pt"><font color="#474747"> </font></span></span></span></span></div></span></font></span>**  
<span style="font-family:Arial;">윈도우 폼에서 메인 스레드가 run 하고 있는 상태이고, 그와 별개로 그래프가 보여져야 한다. 즉, 사용자가 그래프를 보는 중에도 폼의 다른 부분에 마우스 클릭을 통해서 명령을 내릴수 있어야 한다. 그러기 위해서는 스레드를 생성하고 그에 대한 설정이 필요하다. </span></div><textarea class="cpp" cols="64" name="code" rows="4" style="WIDTH: 601px; HEIGHT: 99px">Thread ECG_reader;  
 ECG_reader = new Thread(new ThreadStart(ECG_Read));  
 // Read()를 수행하는 스레드 reader 생성 </textarea>

ECG_reader.Start(); // reader 스레드를 실행

<div style="TEXT-ALIGN: justify">  </div><div style="TEXT-ALIGN: justify"><span style="font-family:Arial;">일단  ECG_reader 라는 스레드 객체를 선언하고, 그 스레드가 실행할 함수 ECG_Read()를 설정해 주고 스레드를 실행하게 된다. 스레드를 실행하게 되면 자연스럽게 ECG_Read() 함수가 실행되게 된다. </span></div><div style="TEXT-ALIGN: justify">**<span style="FONT-FAMILY: Arial"><span style="FONT-SIZE: 12pt"><span style="font-family:Arial;">3. ECG_Read() 함수</span></span></span>**</div><div style="TEXT-ALIGN: justify">**<font face="Arial" size="4"><span style="LINE-HEIGHT: 24px; FONT-SIZE: 16px"><span style="LINE-HEIGHT: 18px; FONT-FAMILY: 굴림; FONT-SIZE: 12px; FONT-WEIGHT: normal"><div style="BORDER-LEFT: rgb(0,0,0) 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: rgb(232,232,232); PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: rgb(255,255,255); PADDING-TOP: 3px"><span style="font-size:10pt;"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"></span></span></span></div><div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><font color="#474747"></font><span style="FONT-SIZE: 10pt"><font color="#474747"></font><span style="FONT-FAMILY: Dotum"><font color="#474747"></font><span style="FONT-SIZE: 10pt"><font color="#474747"> </font></span></span></span></span></div></span></span></font>**  
<span style="FONT-FAMILY: Arial">ECG_Read() 함수 안에서는 본격적인 디스플레이가 이루어진다. 그러나 이 부분에 사실은 디스플레이 이전에 시리얼 통신이나 소켓 통신 혹은 파일에서 ECG 데이터를 읽어오는 부분이 필요하다. 그 부분이 완성 된 후에 들어온 데이터에 대해서 디스플레이가 되기 때문에 데이터 입력 부분은 어떤 식으로든, 입력이 되었다고 가정하겠다. </span></div><div style="TEXT-ALIGN: justify"><font face="Arial">  
</font><textarea class="cpp" cols="64" name="code" style="WIDTH: 596px; HEIGHT: 38px">int ecg_wave_pos = 0; //ECG 그래프 X축의 이동. Public void ECG_Read()  
 {

 for(; ���de09  
 {

//…. 파일을 읽어오는 부분 – 시리얼 포트 또는 네트워크 통신

 Graphics g = this.ECG_Panel.CreateGraphics();  
 //ECG_Panel 에 대한 그래픽 객체 가져오기  
 Pen r_pen = new Pen(Color.Red, 2); //펜에 대한 객체 생성

 if (ecg_wave_pos >=740 )  
 {  
 // ECG_Panel의 가로 사이즈까지 그래프가 도달하면, 다시 처음부터 보여줘야 한다.

 ecg_wave_pos = 0;  
 }  
 else  
 {  
 ecg_wave_pos++; // ECG 그래프 x축증가

 // 데이터 값을 화면의 좌표에 맞춰 주는 연산 부분  
 TempComp = (int)ecg_Fram[0];  
 //ecg_Frame[0]에 ECG Data가 들어가 있다.

 TempComp = TempComp – 200;  
 TempComp = (TempComp * 100) / 127;

 // 이미 그려진 ECG Graph를 지우기 위한  
 g.FillRectangle(Brushes.Black, ecg_wave_pos, 0, 5, 302);

 int temp_ecg = 0;  
 temp_ecg = (int)WAVE_ECG.BASE – TempComp;

g.DrawLine(r_pen, ecg_wave_pos, temp_ecg, ecg_wave_pos + 1, old_wave_ecg);  
 old_wave_ecg = temp_ecg;

 }

 g.Dispose(); //그래픽 객체 해제  
 r_pen.Dispose(); // 펜 객체 해제

 }

}

</textarea><span style="FONT-FAMILY: Arial">이런식으로 구성을 하면, 실시간으로 기기 혹은 네트워크로 부터 들어오는 ECG Data를 화면에 실시간으로 디스플레이 할수가 있다. 중요한 것은 </span><font color="#e31600"><span style="FONT-FAMILY: Arial">화면 사이즈에 맞게 실제 ECG Data를 연산하는 부분</span></font><span style="FONT-FAMILY: Arial">과 더불어서 프로그래밍적인 부분에서 살펴보면, </span><font color="#e31600"><span style="FONT-FAMILY: Arial">스레드에 대한 제어 부분</span></font><span style="FONT-FAMILY: Arial">이 가장 중요한 파트가 아닌가 생각된다. 실제로 디스플레이와는 상관 없지만, 스레드를 돌리다 보면, 시리얼 포트를 통해서 데이터를 기기를 통해서 받으면서 디스플레이를 하는데, close 하는데, </span><font color="#7293fa"><span style="FONT-FAMILY: Arial">ObjectDisposedException</span></font><span style="FONT-FAMILY: Arial"> 이 발생하는 경우가 종종 있기 때문에 이런 부분은 잘 제어해야한다. </span>

[#M_보너스 " Windows Mobile 에서의 디스플레이" 더보기|접기|<font color="#112a75"><span style="FONT-FAMILY: Arial">필자는 최근에 블랙잭 1 스마트폰에서 블루투스를 통해서 데이터를 전송 받아서 ECG Data를 전송 받는 프로그램을 개발하였다. 어차피 윈폼에서 하는데 뭐 다를게 있는가 하는 분들도 있겠지만, .NET CF 는 기존의 .NET 프레임워크보다 적인 기능을 제공한다. </span></font>

<figure class="wp-caption aligncenter" style="width: 320px">![](http://ash84.net/wp-content/uploads/1/4947db4a4129fBK.jpg)<figcaption class="wp-caption-text">블랙잭 1 에서의 ECG Display</figcaption></figure>

<span style="FONT-FAMILY: Arial">특히, 위에서는 Panel 객체의 CreateGraphics()를 통해서 그래픽 객체를 가져와서 디스플레이를 수행했었는데, .NET CF에서는 Panel 부분에서 CreateGraphics()를 지원하지 않는다. 때문에 필자는 Form의 일정 부분을 할애해서 ECG 디스플레이를 개발했다. 기존의 PC에서와는 다르게, 화면 사이즈가 제한되어 있기 때문에, 여러 리드(Lead)를 디스플레이 할수 없다는 점 역시 고려해야 하는 부분이다.</span><span style="FONT-FAMILY: Arial"></span>

[](http://ash84.net/wp-content/uploads/1/cfile2.uf.14192C0D4BD55A0726DEF7.zip)cfile2.uf.14192C0D4BD55A0726DEF7.zip

_M#]

</div>

