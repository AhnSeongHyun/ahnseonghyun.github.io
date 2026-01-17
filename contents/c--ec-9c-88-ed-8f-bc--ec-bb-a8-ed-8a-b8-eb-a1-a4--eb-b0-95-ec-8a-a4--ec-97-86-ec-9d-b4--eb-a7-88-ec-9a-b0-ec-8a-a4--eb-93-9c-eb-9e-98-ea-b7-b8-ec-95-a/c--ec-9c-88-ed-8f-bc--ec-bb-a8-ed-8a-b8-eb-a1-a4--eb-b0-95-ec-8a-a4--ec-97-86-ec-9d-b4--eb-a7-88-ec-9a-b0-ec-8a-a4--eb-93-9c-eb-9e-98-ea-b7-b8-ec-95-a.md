---
title: '[C#] 윈폼 컨트롤 박스 없이 마우스 드래그앤 드롭으로 이동.'
author: 'ash84'
pub_date: '2010-11-18'
description: '원래 다른 분 블로그에 있었던 것인데, 퍼왔습니다. 출처를 표시해야 하는데, 프로젝트 코드에 넣은지 꽤 돼서 출처 찾기가 힘드네요. ㅠ 혹시 보시다가 본인이 쓴 글이라고 하시면'
featured_image: ''
tags: ['C#', 'dev', 'winform', '안성현', '윈폼', '윈폼 이동', '최대화', '최소화', '컨트롤박스']
---
<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); font-family: 굴림; font-size: 9pt; "><span style="font-size: 11pt; color: rgb(200, 5, 106); font-family: Dotum; line-height: 2; ">원래 다른 분 블로그에 있었던 것인데, 퍼왔습니다. 출처를 표시해야 하는데, 프로젝트 코드에 넣은지 꽤 돼서 출처 찾기가 힘드네요. ㅠ 혹시 보시다가 본인이 쓴 글이라고 하시면 출처표시 해 드리겠습니다. </span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); font-family: 굴림; font-size: 9pt; "><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림">  
<span style="font-size: 11pt; ">  
</span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); font-family: 굴림; font-size: 9pt; "><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">일단 설명을 드리자면, 윈폼에서 최소화, 최대화, 닫기 및 상단의 텍스트 표시를 없애고 이미지만 나오게 윈폼을 개발하는 경우가 있지요. 사실 ControlBox 를 마우스로 드래그앤 드롭하면 움직이는데, 전체를 이미지로 덮어 버리는 경우에는 그런 부분을 만들어 줘야 합니다. </span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); font-family: 굴림; font-size: 9pt; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; color: rgb(51, 51, 51); font-family: 굴림; font-size: 9pt; "><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림"></font></div><span style="font-size: 11pt; ">  
</span>

<div class="txc-textbox" style="border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-top-color: rgb(203, 203, 203); border-right-color: rgb(203, 203, 203); border-bottom-color: rgb(203, 203, 203); border-left-color: rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; line-height: 2; color: rgb(51, 51, 51); font-family: 굴림; font-size: 9pt; "><span style="font-size: 11pt; ">  
</span><div><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 9pt; ">public Point ptRect = new Point(0, 0);</span></span></font></div><span style="font-size: 9pt; ">  
</span>

<div><span style="font-size: 9pt; ">  
</span><font color="#333333" face="굴림">  
<span style="font-size: 9pt; ">  
</span></font></div><span style="font-size: 9pt; ">  
</span>

<div><span style="font-size: 9pt; ">  
</span><font color="#333333" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 9pt; ">private void panel_Keypad_MouseDown(object sender, MouseEventArgs e)</span></span></font></div><span style="font-size: 9pt; ">  
</span>

<div><span style="font-size: 9pt; ">  
</span><font color="#333333" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 9pt; ">{</span></span></font></div><span style="font-size: 9pt; ">  
</span>

<div><span style="font-size: 9pt; ">  
</span><font color="#333333" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 9pt; ">            ptRect.X = e.X;</span></span></font></div><span style="font-size: 9pt; ">  
</span>

<div><span style="font-size: 9pt; ">  
</span><font color="#333333" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 9pt; ">            ptRect.Y = e.Y;</span></span></font></div><span style="font-size: 9pt; ">  
</span>

<div><span style="font-size: 9pt; ">  
</span><font color="#333333" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 9pt; ">}</span></span></font></div><span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; color: rgb(51, 51, 51); font-family: 굴림; font-size: 9pt; "><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림"></font></div><span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; color: rgb(51, 51, 51); font-family: 굴림; font-size: 9pt; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; color: rgb(51, 51, 51); font-family: 굴림; font-size: 9pt; "><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림"></font></div><span style="font-size: 11pt; ">  
</span>

<div class="txc-textbox" style="border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-top-color: rgb(203, 203, 203); border-right-color: rgb(203, 203, 203); border-bottom-color: rgb(203, 203, 203); border-left-color: rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; line-height: 2; color: rgb(51, 51, 51); font-family: 굴림; font-size: 9pt; "><span style="font-size: 11pt; ">  
</span><div><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 9pt; ">private void panel_Keypad_MouseMove(object sender, MouseEventArgs e)</span></span></font></div><span style="font-size: 9pt; ">  
</span>

<div><span style="font-size: 9pt; ">  
</span><font color="#333333" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 9pt; ">{</span></span></font></div><span style="font-size: 9pt; ">  
</span>

<div><span style="font-size: 9pt; ">  
</span><font color="#333333" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 9pt; ">            if (e.Button == MouseButtons.Left)</span></span></font></div><span style="font-size: 9pt; ">  
</span>

<div><span style="font-size: 9pt; ">  
</span><font color="#333333" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 9pt; ">            {</span></span></font></div><span style="font-size: 9pt; ">  
</span>

<div><span style="font-size: 9pt; ">  
</span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 9pt; ">                Point pt = new Point(this.Location.X + e.X – ptRect.X,this.Location.Y + e.Y – ptRect.Y);</span></span></div><span style="font-size: 9pt; ">  
</span>

<div><span style="font-size: 9pt; ">  
</span><font color="#333333" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 9pt; ">                </span></span></font></div><span style="font-size: 9pt; ">  
</span>

<div><span style="font-size: 9pt; ">  
</span><font color="#333333" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 9pt; ">                this.Location = pt;</span></span></font></div><span style="font-size: 9pt; ">  
</span>

<div><span style="font-size: 9pt; ">  
</span><font color="#333333" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 9pt; ">            }</span></span></font></div><span style="font-size: 9pt; ">  
</span>

<div><span style="font-size: 9pt; ">  
</span><font color="#333333" face="굴림"></font><span style="font-family: 굴림; color: rgb(51, 51, 51); "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 9pt; ">}</span></span></span></div><span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; ">  
</span>

<div style="line-height: 2; color: rgb(51, 51, 51); font-family: 굴림; font-size: 9pt; "><span style="font-size: 11pt; ">  
</span><span style="font-family: 굴림; color: rgb(51, 51, 51); "></span></div><span style="font-size: 11pt; "></span>

  
<span style="font-size: 11pt; ">  
</span>  
**<span style="font-size: 11pt; ">C++ 에서의 구현(2011.07.21 Update)</span>  
<span style="font-size: 11pt; ">  
</span>  
**

<div><span style="font-size: 11pt; ">  
</span></div><div class="txc-textbox" style="border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-top-color: rgb(203, 203, 203); border-right-color: rgb(203, 203, 203); border-bottom-color: rgb(203, 203, 203); border-left-color: rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; "><span style="font-size: 11pt; ">  
</span><div><span style="font-size: 11pt; ">  
<span style="font-size: 9pt; ">void CLoginDlg::OnLButtonDown(UINT nFlags, CPoint point)</span></span></div><span style="font-size: 9pt; ">  
</span>

<div><span style="font-size: 9pt; ">{</span><span class="Apple-tab-span" style="white-space: pre; font-size: 9pt; "></span><span style="font-size: 9pt; "> </span></div><span style="font-size: 9pt; ">  
</span>

<div><span style="font-size: 9pt; ">   </span><font color="#e31600"><span style="font-size: 9pt; ">     PostMessage( WM_NCLBUTTONDOWN, HTCAPTION, MAKELPARAM( point.x, point.y)); </span>  
<span style="font-size: 9pt; ">  
  </span></font></div><span style="font-size: 9pt; ">  
</span>

<div><span class="Apple-tab-span" style="white-space: pre; font-size: 9pt; "></span><span style="font-size: 9pt; ">CDialogEx::OnLButtonDown(nFlags, point);</span></div><span style="font-size: 9pt; ">  
</span>

<div><span style="font-size: 9pt; ">}</span></div><span style="font-size: 11pt; ">  
</span>****

<span style="font-size: 11pt; ">  
</span>

</div>**  
<span style="font-size: 11pt; ">  
</span>**<span style="font-size: 11pt; ">다이얼로그의 OnLButtonDoown 에서 위의 PostMessage 부분 추가해 주면 됨. 생각보다 쉽게 구현됨. </span>



