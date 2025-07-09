---
title: '[C#] Bluetooth Communication in Black Jack phone(블랙잭에서 블루투스 이용)'
author: 'ash84'
pub_date: '2008-12-22'
description: '블랙잭 폰에서(블랙잭 1) 블루투스를 이용한 프로그램 개발.

**주의사항**  
 – 기존의 PC 환경과는 다르게 SerialPort class를 통한 연결은 어려울 뿐만 아니라, 잘 되지가 않는다. 때문에 C# 으로 개발하기 위해서는 기존의 SerialPort 방식과는 다른 방식을 사용해야 한다.

**라이브러리 : InTheHa'
featured_image: ''
tags: ['bluetooth', 'c#', 'dev', 'Serial Port', '블랙잭', '블랙잭에서 블루투스 이용하기', '블루투스', '윈도우 모바일', '윈도우 모바일 5', '프로그래밍', '프로그램개발']
---


<font color="#105738"></font><font color="#193da9"></font>

 블랙잭 폰에서(블랙잭 1) 블루투스를 이용한 프로그램 개발.

<font color="#e31600">**주의사항**</font>  
 – 기존의 PC 환경과는 다르게 SerialPort class를 통한 연결은 어려울 뿐만 아니라, 잘 되지가 않는다. 때문에 C# 으로 개발하기 위해서는 기존의 SerialPort 방식과는 다른 방식을 사용해야 한다.

<font color="#c84205">**라이브러리 : InTheHand **</font>

<div style="TEXT-ALIGN: justify"> InTheHand 는 이동성(mobility)를 위한 .NET Component를 제공하는데, 무료로 다운 받아서 사용할수 있고, 현재는 2.2 버전까지 Release가 되어 있다. 또한 설치를 하면, 자동으로 샘플코드 등을 볼수가 있기 때문에 빠르고 쉽게 개발 할 수가 있다. 윈도우 모바일에서의 적외선 통신, 블루투스 통신등을 지원하는 라이브러리 뿐만 아니라, 다양한 라이브러리가 있으며, 그에대한 설명또한 MSDN처럼 잘 되어 있다. Link : [http://inthehand.com/](http://inthehand.com/)

<figure class="wp-caption aligncenter" style="width: 590px">![](http://ash84.net/wp-content/uploads/1/494f0a00e8d23B2.jpg)<figcaption class="wp-caption-text">Library</figcaption></figure>

</div>**<font color="#57048c">1. 블루투스 기기 탐색(Discovery Devices)</font>**  
<textarea class="cpp" cols="64" name="code" style="WIDTH: 591px; HEIGHT: 38px">// Add Namespace  
 using InTheHand.Net;  
 using InTheHand.Net.Bluetooth;</textarea>

///  
<summary> /// SDP 프로토콜을 통해서 주변의 디바이스 정보를 수집  
 /// </summary>

BluetoothDeviceInfo[] bluetoothDeviceInfo;

///  
<summary> /// 블루투스 클라이언트 정보  
 /// </summary>

private BluetoothClient bluetoothClient;

///  
<summary> /// 서비스 정의: 현재는시리얼포트 서비스만 지원한다.  
 /// </summary>

private Guid service = BluetoothService.SerialPort;

///  
<summary> /// BluetoothClient.GetStream()과 연결할 NetworkStream  
 /// </summary>

NetworkStream peer;

public void Discovery_Devices()  
 {

 BluetoothRadio.PrimaryRadio.Mode = RadioMode.Discoverable; //블루투스 모드를 Discoverable 모드로 전환

 bluetoothClient = new BluetoothClient();

 Cursor.Current = Cursors.WaitCursor; //검색하는 동안 기다리는 커서로 변경

 bluetoothDeviceInfo = bluetoothClient.DiscoverDevices(4); //찾을 최대의 디바이스 수

 // 찾은 디바이스 이름과 주소를 콤보박스에 명시  
 comboBox_Devices.DataSource = bluetoothDeviceInfo;  
 comboBox_Devices.DisplayMember = “DeviceName”;  
 comboBox_Devices.ValueMember = “DeviceAddress”;  
 comboBox_Devices.Focus();

 //커서를 원래대로  
 Cursor.Current = Cursors.Default;

}

  
<font color="#105738"></font>

<font color="#57048c">**2. 선택한 디바이스와 연결(Connect)  
**</font>  
<textarea class="cpp" cols="64" name="code" style="WIDTH: 594px; HEIGHT: 38px">public void Connect()  
 { </textarea>

 if (bluetoothClient.Connected == false)  
 {  
 //선택한 디바이스 주소와 연결하려는 서비스를 기반으로 접속  
 bluetoothClient.Connect(new BluetoothEndPoint((BluetoothAddress)comboBox_Devices.SelectedValue, service));

 if (bluetoothClient.Connected == true)  
 {  
 //NetworkStream 을 GetStream() 과 연결함으로써 시리얼포트에서 데이터를 읽어온다.  
 peer = this.bluetoothClient.GetStream();

 //Receive Thread 시작  
 th = new Thread(new ThreadStart(Receive));  
 th.Start();

 }

 }

}

  
<font color="#57048c">**3. 시리얼포트 서비스를 이용해서 데이터 받기**   
<textarea class="cpp" cols="64" name="code" style="WIDTH: 589px; HEIGHT: 38px">public void Receive()  
 {  
 int data = peer.ReadByte(); //데이터를 1 바이트씩 읽어온다.  
 }</textarea></font>

<font color="#000000">위와 같은 방식으로 특정 서비스에 해당하는 기기를 찾을수도 있고, 또한 연결할 수도 있다. 본 포스팅에서는 가장 많이 사용하는 시리얼포트 서비스에(Serial Port Service)에 대해서 윈도우 모바일 상에서 </font><font color="#333333"><font color="#000000">어떻게 다른 기기로 부터 데이터를 받을거 인가 하는 문제에 대한 방법을 제시했다. 더 많은 자료는 IntheHand를 참고 하시길 바란다.   
</font></font>

**<font color="#e31600">Exception(예외)</font>**

<div class="txc-textbox" style="BORDER-BOTTOM: #cbcbcb 1px solid; BORDER-LEFT: #cbcbcb 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #ffffff; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #cbcbcb 1px solid; BORDER-RIGHT: #cbcbcb 1px solid; PADDING-TOP: 10px"><font color="#333333"><font color="#333333">위의 코드를 적용할때, 윈도우 모바일상에서 코딩시, 스레드를 작동시킬경우, </font>

<font color="#333333">**<font color="#e31600">“Control.Invoke는 별도 스레드에 만들어진 컨트롤과 상호 작용하는 데 사용해야 합니다” </font>**  
</font>

<font color="#333333"></font><font color="#333333">라는 예외가 발생할 것입니다. 이럴경우에는, [http://drkein.tistory.com/69](http://drkein.tistory.com/69) 이 부분을 참고해 주시기 바랍니다.  
</font>

</font><font color="#333333"></font></div><font color="#333333" style="TEXT-ALIGN: justify"></font><font color="#333333"></font>

<div class="txc-textbox" style="BORDER-BOTTOM: #cbcbcb 1px solid; BORDER-LEFT: #cbcbcb 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #ffffff; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #cbcbcb 1px solid; BORDER-RIGHT: #cbcbcb 1px solid; PADDING-TOP: 10px"> 그 밖에 블루투스를 이용한 채팅이나, 블루투스 연결을 기다리는 부분에 대해서 좀더 알고 싶으시다면, 다음의 동영상을 보시면 많은 도움이 될것입니다. 프랑스 어이고, 화질이 별로 안좋긴 하지만, 그래두 많은 도움이 될것 입니다 <font color="#333333">  
</font>

<font color="#333333"><span id="tx_beforestart_mark">[](http://ash84.net/wp-content/uploads/1/494f10e1e2b54A5.wmv)494f10e1e2b54A5.wmv</span></font>

</div><font color="#333333">  
</font>

<font color="#333333">  
<span id="tx_beforestart_mark"></span>  
</font>

<span id="tx_beforestart_mark"></span><font color="#c84205"> 2009.11.09 참고 </font>

위의 글은 Windows Mobile 5. 즉, 블랙잭 1을 대상으로 프로그래밍을 했을때 IntheHand Component를 이용해서 블루투스 기기를 쉽게 개발시에 이용하는 방법에 대해서 기술해 놓은 내용이다. 하지만, Windows Mobile 6.0 부터는 MS에서 본격적으로 Sample Code를 통해서 제공하고 있기 때문에 그 내용을 보는것이 더 도움이 되리라 생각된다.



