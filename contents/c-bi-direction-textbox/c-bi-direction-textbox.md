---
title: '[C#] Bi-Direction TextBox'
author: 'ash84'
pub_date: '2010-07-06'
description: '최근에 하는 프로젝트 때문에 Bi-Direction 이라는 것에 대해서 알게 되었다. Bi-Direction 이라는 것은 글씨를 쓰는 방향이 원래 서양 혹은 우리나라와 같은 왼쪽에서 오른쪽으로 향하는 방향이 아닌 반대 방향을 의미하는 것이다. 왜 이게 필요한가? 라는 의문을 던지기 전에 사실, Bi-'
featured_image: ''
tags: ['Bi-Direction TextBox', 'C#', 'dev', 'RightToLeft 속성', '아랍어', '히브리어']
---
<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">최근에 하는 프로젝트 때문에 Bi-Direction 이라는 것에 대해서 알게 되었다. Bi-Direction 이라는 것은 글씨를 쓰는 방향이 원래 서양 혹은 우리나라와 같은 왼쪽에서 오른쪽으로 향하는 방향이 아닌 반대 방향을 의미하는 것이다. 왜 이게 필요한가? 라는 의문을 던지기 전에 사실, Bi-Directional 에 대해서 알게된 계기는 이번 프로젝트에서 아랍어와 히브리어에 대해서 알게되면서 부터 였다. 즉, 이 두 언어들은 우리나라와는 다르게 오른쪽에서 왼쪽으로 글자를 써간다는 것이다. </span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">그런 부분을 지원해 주기 위해서 Text Box 에서는</span>**<span style="font-size: 11pt; "> RightToLeft</span>**<span style="font-size: 11pt; "> 라는 속성이 있다. 즉 오른쪽에서 왼쪽으로 쓰는 것을 허용(Allow) 하겠냐는 속성인데, </span>**<span style="font-size: 11pt; ">RightToLeft</span>**<span style="font-size: 11pt; ">를 적용하면 다음과 같이 써진다. </span></span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="LINE-HEIGHT: 2"><span style="font-size: 11pt; ">  
</span><div style="TEXT-ALIGN: justify"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; "> </span></span></div><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><figure class="wp-caption aligncenter" style="width: 300px">![](http://ash84.net/wp-content/uploads/1/cfile24.uf.116BCF044C2D60434EA3CA.png)<figcaption class="wp-caption-text">원래 써지는 방향</figcaption></figure>

</span></span>

</div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="LINE-HEIGHT: 2"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><figure class="wp-caption aligncenter" style="width: 300px">![](http://ash84.net/wp-content/uploads/1/cfile29.uf.196FE0014C2D607B68EBF8.png)<figcaption class="wp-caption-text">RightToLeft 적용</figcaption></figure>

</span></span><span style="font-size: 11pt; ">  
</span><div style="TEXT-ALIGN: justify"><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify"><span style="font-size: 11pt; ">  
</span></div></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum"><span style="font-size: 11pt; ">즉, RightToLeft를 적용하면, Hello World 라고 쓰면, 첫글자 ‘H’ 가 오른쪽 끝에 있다가, ‘e’ 를 입력하면 왼쪽으로 한칸씩 이동하면서 써지는 효과가 TextBox 상에서 일어나게 된다. 그런데 문제가 있다. Bi-Direction 을 지원하는 언어(아랍어 등등) 은 실제는 그렇게 쓰여지지않는다는것이다. </span><font color="#c8056a"><span style="font-size: 11pt; ">RightToLeft 는 Bi-Direction을 지원하는 속성이 아니라 단순히 쓰는 방향을 오른쪽에서 시작하라는 것 뿐이다.</span></font><span style="font-size: 11pt; "> 실제 Bi-Direction 으로 “Hello World”를 적으면 다음과 같다. </span></span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="LINE-HEIGHT: 2"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">![](http://ash84.net/wp-content/uploads/1/cfile23.uf.146F4F204C2D61A7496531.png)

</span></span><span style="font-size: 11pt; ">  
</span><div style="TEXT-ALIGN: justify"><span style="font-size: 11pt; ">  
</span></div></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">그렇기 때문에 RightToLeft 외에 다른 장치가 TextBox 입력시 필요하게 된다. 어떤 장치가 필요할까?</span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">사실상 간단한 수준의 코딩이면 된다. 먼저 쓴 글씨가 계속 오른쪽에 위치하도록 하면 되는 것이다. </span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><font color="#e31600"><span style="FONT-SIZE: 10pt"></span></font></div><span style="font-size: 11pt; ">  
</span>

<div class="txc-textbox" style="BORDER-BOTTOM: rgb(203,203,203) 1px solid; BORDER-LEFT: rgb(203,203,203) 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: rgb(255,255,255); PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: rgb(203,203,203) 1px solid; BORDER-RIGHT: rgb(203,203,203) 1px solid; PADDING-TOP: 10px"><span style="font-size: 11pt; ">  
</span><div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><font color="#e31600"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">            //TextBox 를 통한 직접입력이 아닌 버튼을 통한 우회입력의 경우만 가능함.</span></span></font><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; "> </span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2; MARGIN-LEFT: 4em"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">string now_string = “현재 입력한 글자”;</span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="LINE-HEIGHT: 2"><span style="font-size: 11pt; ">  
</span><div style="TEXT-ALIGN: justify"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">            </span></span></div></div><span style="font-size: 11pt; ">  
</span>

<div style="LINE-HEIGHT: 2; MARGIN-LEFT: 4em"><span style="font-size: 11pt; ">  
</span><div style="TEXT-ALIGN: justify"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">string pre_string = textBox1.Text;</span></span></div></div><span style="font-size: 11pt; ">  
</span>

<div style="LINE-HEIGHT: 2"><span style="font-size: 11pt; ">  
</span><div style="TEXT-ALIGN: justify"><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">            textBox1.Text = now_string + pre_string;</span></span></div></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"></div></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">위와 같이 코딩을 해 놓은면, 오른쪽에서 왼쪽으로 써지면서 먼저 쓴 글자는 오른쪽에 계속 있게 되는 것이다. 신기하게도 아랍어는 숫자는 그대로 쓴다고 한다. 전 12 라고 해서 21 이렇게 쓰지 않는다는 것이다. ^^</span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">  
<span style="font-size: 11pt; ">  
</span></span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">  
<span style="font-size: 11pt; ">  
</span></span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">[](http://ash84.net/wp-content/uploads/1/cfile25.uf.110C11284C2DA6760D8A49.zip)cfile25.uf.110C11284C2DA6760D8A49.zip  
<span style="font-size: 11pt; ">  
</span></span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">  
<span style="font-size: 11pt; ">  
</span></span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">  
<span style="font-size: 11pt; ">  
</span></span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 10pt"><span style="FONT-FAMILY: Dotum">**<span style="font-size: 11pt; ">마치며.</span>**</span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="font-size: 11pt; ">  
</span><div><span style="font-size: 11pt; ">  
</span><div style="BORDER-LEFT: #000000 200px solid; PADDING-BOTTOM: 3px; BACKGROUND-COLOR: #e8e8e8; PADDING-LEFT: 6px; WIDTH: 690px; PADDING-RIGHT: 6px; FONT: bold 1pt/1 나눔고딕, Sans-serif; MARGIN-BOTTOM: 10px; HEIGHT: 1px; COLOR: #fff; PADDING-TOP: 3px"><span style="font-size:10pt;"><span style="FONT-FAMILY: Batang"><span style="FONT-SIZE: 11pt"></span></span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="LINE-HEIGHT: 1.7"><span style="FONT-FAMILY: Dotum"><font color="#474747"></font><span style="FONT-SIZE: 10pt"><font color="#474747"></font><span style="FONT-FAMILY: Dotum"><font color="#474747"></font></span></span></span></div></div></div><span style="font-size: 11pt; ">  
</span>

<div style="TEXT-ALIGN: justify; LINE-HEIGHT: 2"><span style="FONT-SIZE: 10pt"><span style="font-family: Dotum; font-size: 11pt; ">이번 포스팅은 모든 프로그래머에게 그닥 유용할것 같진 않지만, 혹시나 나와 비슷한 고민을 해 보셨던 분이라면 도움이 되길 바란다.</span></span><span style="font-family: Dotum; font-size: 11pt; ">^^ </span></div>

