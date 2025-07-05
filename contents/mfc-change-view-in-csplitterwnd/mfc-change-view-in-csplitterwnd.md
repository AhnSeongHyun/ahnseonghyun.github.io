---
title: '[MFC] Change View in CSplitterWnd'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['CreateView', 'CSplitterwnd', 'dev', 'OnInitalUpdate', '뷰전환']
---


<div></div><div><div style="line-height: 2; text-align: justify; "><span style="font-family: Dotum; font-size: 13px; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">이번 프로젝트를 하면서 허벌나게 CSplitterWnd 와 함께 동거동락을 하고 있는데요. MainFrame 에서 </span></span></span><span style="font-family: Dotum; font-size: 13px; line-height: 26px; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">CSplitterWnd </span></span></span><span style="font-family: Dotum; font-size: 13px; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">에 대해서 구획 나누어 주고 뷰 배치하는 작업 그리고 </span></span></span><span style="font-family: Dotum; font-size: 13px; line-height: 26px; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">CSplitterWnd </span></span></span><span style="font-family: Dotum; font-size: 13px; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">재정의 해서 굵기 조정하는 부분까지. 다 했는데 하나의 고비가 남아 있더군요. 그것은 바로. 런타임에서 </span></span></span><span style="font-family: Dotum; font-size: 13px; line-height: 26px; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">CSplitterWnd </span></span></span><span style="font-family: Dotum; font-size: 13px; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">에 배치된 뷰를 바꾸는 일입니다.  </span></span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#004c5f"><span style="font-size: 11pt; ">I  used </span></font></span></span></span><font color="#004c5f"><span style="font-family: Dotum; font-size: 13px; line-height: 26px; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">CSplitterWnd </span></span></span><span style="font-family: Dotum; font-size: 13px; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">in this project. In MainFrame, I was coding the Work placing view, dividing region using </span></span></span><span style="font-family: Dotum; font-size: 13px; line-height: 26px; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">CSplitterWnd</span></span></span><span style="font-family: Dotum; font-size: 13px; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">. Also override </span></span></span><span style="font-family: Dotum; font-size: 13px; line-height: 26px; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">CSplitterWnd </span></span></span><span style="font-family: Dotum; font-size: 13px; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">and then adjust the thickness. But, One obstacle remains. It’s just. In RunTime environment, change View in </span></span></span><span style="font-family: Dotum; font-size: 13px; line-height: 26px; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">CSplitterWnd.</span></span>  
<span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span></span></font></div><span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span><span class="Apple-tab-span" style="white-space: pre; "><span style="white-space: normal; "></span></span>

<div style="text-align: justify; "><span style="font-size: 11pt; ">  
</span><font color="#004c5f" face="Dotum" size="2"><span style="line-height: 19px;"><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">Below code. </span></span></span></font></div><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; "></span>

<script src="https://gist.github.com/3264296.js"><span style="font-size: 11pt; "></script><span style="font-size: 11pt; "></span>

<div style="text-align: justify;"><span style="font-size: 11pt; ">  
</span><span style="line-height: 24px;">  
</span></div></div><span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; "><div style="text-align: justify;"><span style="font-size: 11pt; ">  
</span><span style="font-size: 12px; "><span style="font-size: 10pt; "><span style="font-family: Dotum; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">일단 MainFrame 을 가져오고 나서 CCreateContext 를 생성합니다. 위의 코드는 뷰에 도큐먼트가 없는 뷰를 대상으로 하고 있기때문에 Doc 연결을 가져오지 않는데요, 만약 도큐먼트가 있는 뷰라면 해당 부분을 넣어 주어야 할것 입니다. </span></span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">그리고 </span></span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">CSplitterWnd 의 해당 위치에 DeleteView 를 통해서 해당 뷰를 지우고, 다시 CreateView 를 통해서 전환할 뷰를 생성해 주면 됩니다. 매우 간단하지요?</span></span>  
<span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#004c5f"><span style="font-size: 11pt; ">Once, Get pointer of MainFrame, Create CCreateContext. In the above code, Do not get Document Connection becauseof the view without document. But if the view get Document, insert document connection part. And erase the view using DeleteView fuction of CSplitterWnd, Create changing view using CreateVIew Fucntion. It is very Simple. </span></font></span></span></span></span></span></div><span style="font-size: 11pt; ">  
</span>

</span></div><span style="font-size: 11pt; ">  
</span>

<div><span style="font-size: 11pt; ">  
</span><div style="line-height: 2; text-align: justify; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span><span style="line-height: 2; font-size: 10pt; "><div style="text-align: justify;"><span style="font-size: 11pt; ">  
</span><span style="font-family: Dotum; "><font color="#e31600"><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">그런데 만약 전환하려는 뷰의 OnInitalUpdate() 함수에서 뷰 안에 있는 컨트롤들을 배치하고 있다면?</span></span>  
<span style="font-size: 11pt; ">  
</span></font></span></div><span style="font-size: 11pt; ">  
</span>

</span><span style="font-family: arial, sans-serif; font-size: 16px; line-height: normal; "><font color="#004c5f"><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">But</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">if you</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">want to</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">switch</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">the view</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">OnInitalUpdate ()</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">function</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">in the</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">control</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">of</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">the view</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">if you are</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">placed</span></span></span></font><span class="" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#004c5f"><span style="font-size: 11pt; ">?</span></font></span></span>  
<span style="font-size: 11pt; ">  
</span><span style="color: rgb(0, 0, 0); font-size: 10pt; "><span style="font-family: Dotum; "><span style="font-size: 11pt; "> </span>  
<span style="font-size: 11pt; ">  
  </span></span></span></span></span><span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; "><span style="line-height: 2; font-size: 10pt; "><div style="text-align: justify;"><span style="font-size: 11pt; ">  
</span><span style="font-family: Dotum; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">아쉽게도 CreateVIew 를 통해서 런타임 상에서 배치를 하게 되면 OnInitalUpdate() 함수가 호출되지가 않습니다. 만약 어떤 정의하는 부분이나 초기화 하는 부분이 있다면 초기화가 되지 않겠지요. 때문에 명시적으로 호출해 주어야 합니다. 그래서 CView 클래스의 인스턴스를 만들어서 생성된 View 를 가져와서 명시적으로 OnInitialUpdate() 를 호출해 주고 있는 것입니다. </span></span>  
<span style="font-size: 11pt; ">  
</span>  
</span></div><span style="font-size: 11pt; ">  
</span>

</span><div style="line-height: 2; text-align: justify; "><span style="font-size: 11pt; ">  
</span><font color="#004c5f"><span style="font-family: arial, sans-serif; font-size: 16px; line-height: normal; "><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">Unfortunately, if </span></span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">placed</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">on</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">the runtime </span></span></span></span><span style="font-family: arial, sans-serif; font-size: 16px; line-height: normal; "><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">through</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">CreateVIew, </span></span></span></span><span style="font-family: arial, sans-serif; font-size: 16px; line-height: normal; "><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">OnInitalUpdate () </span></span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">function</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">is not</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">called. If you have any part of definition or initiation, do not define or init. so you must call init. So that call explicitly </span></span></span></span></font><span style="font-family: Dotum; font-size: 13px; line-height: 26px; "><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#004c5f"><span style="font-size: 11pt; ">OnInitialUpdate() function using the point of created view.</span></font></span></span>  
<span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; text-align: justify; "><span style="color: rgb(0, 0, 0); line-height: normal; "><span class="" title="대체 번역을 클릭합니다."><font face="Dotum" size="2">  
<span style="font-size: 11pt; ">  
</span></font></span></span></div><span style="font-size: 11pt; ">  
</span><span style="line-height: 2; font-size: 10pt; "><div style="text-align: justify;"><span style="font-size: 11pt; ">  
</span><span style="font-family: Dotum; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">런타임 상에서 OnInitialUpdate() 함수를 사용하기 때문에 그에 관련해서 오류가 생길수도 있으니 조심하세요.^^ </span></span></span></div><span style="font-size: 11pt; ">  
</span>

</span>

<div style="line-height: 2; text-align: justify; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span><span style="font-family: arial, sans-serif; font-size: 16px; line-height: normal; "><font color="#004c5f"><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">Runtime</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">on the</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">OnInitialUpdate ()</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">function</span></span></span><span class="" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">, because</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">it</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">have got</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">an error</span></span></span><span title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">, so</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">be careful</span></span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">with respect</span></span></span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span><span class="hps" title="대체 번역을 클릭합니다."><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">^ ^</span></span>  
<span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span></span></font></span><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; text-align: justify; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; text-align: justify; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div></div><span style="font-size: 11pt; ">  
</span>

<div><div style="line-height: 2; text-align: justify; "><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; ">  
</span>

<div><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span><meta charset="utf-8"></meta><span style="font-size: 11pt; ">  
</span>



