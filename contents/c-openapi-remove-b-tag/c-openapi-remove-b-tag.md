---
title: '[C#] 네이버 지역검색 오픈 API 검색결과 <b> 태그제거'
author: 'ash84'
pub_date: '2009-01-14'
description: '네이버 지역검색 오픈 API를 사용해서 검색한 결과는 RSS로 볼수도 있지만,  XML의 형식으로 볼수도 있다. 특히  안에 있는 부분이 그러하다. 


  
 예를 들면'
featured_image: ''
tags: ['&lt;b&gt;태그', 'C#', 'dev', 'rss', 'XML', '네이버', '네이버 지역검색', '오픈 API', '지역검색', 'programming']
---
<span style="font-size: 12pt; ">  
 네이버 지역검색 오픈 API를 사용해서 검색한 결과는 RSS로 볼수도 있지만,  XML의 형식으로 볼수도 있다. 특히 <titles> 안에 있는 부분이 그러하다. </span>  
<span style="font-size: 12pt; ">  
</span>  
<span style="font-size: 12pt; ">  
 예를 들면</span>  
<span style="font-size: 12pt; ">  
</span>  
<span style="font-size: 12pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 12pt; ">  
</span>**<span style="font-size: 12pt; ">  
</span><div class="txc-textbox" style="BORDER-RIGHT: #cbcbcb 1px solid; PADDING-RIGHT: 10px; BORDER-TOP: #cbcbcb 1px solid; PADDING-LEFT: 10px; PADDING-BOTTOM: 10px; BORDER-LEFT: #cbcbcb 1px solid; PADDING-TOP: 10px; BORDER-BOTTOM: #cbcbcb 1px solid; BACKGROUND-COLOR: #ffffff"><span style="font-size: 12pt; ">  
</span>**<span style="font-size: 12pt; ">대치동 은마 </span><font color="#e31600"><span style="font-size: 12pt; "><b></span></font><span style="font-size: 12pt; "> 아파트</span><font color="#e31600"><span style="font-size: 12pt; "></b> </span></font>**  
<span style="font-size: 12pt; ">  
</span></div><span style="font-size: 12pt; ">  
</span>

**</div><span style="font-size: 12pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 12pt; ">  
</span>  
<span style="font-size: 12pt; ">  
 이런식으로 텍스트의 일부분에 <b> 태그가 되어 있는 경우를 종종 볼수가 있다. RSS 형식이나 혹은 XSL을 이용해서 HTML로 변환해서 쓰는 경우는 상관이 없겠지만, Application 에서 결과 XML을 파싱해서 안에 있는 정보를 사용할 경우에는 <b> 태그를 제거 해야하는 경우가 있다. </span>  
<span style="font-size: 12pt; ">  
</span>  
<span style="font-size: 12pt; ">  
 그때는 다음의 코드를 사용하면 된다. </span><span style="font-size: 12pt; ">  
</span><script src="https://gist.github.com/3949607.js"><span style="font-size: 12pt; "></script><span style="font-size: 12pt; "></span>

</div><span style="font-size: 12pt; ">  
</span>



