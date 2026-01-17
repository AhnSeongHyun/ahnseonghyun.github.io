---
title: '앱 업데이트에 대한 단상.'
author: 'ash84'
pub_date: '2011-07-18'
description: '몇개의 앱을 개발하지도 않고 이런 애기를 하는게 웃기긴 하지만, 주변의 다른 앱 개발자 들의 말을 들어보아도 앱 업데이트에 대한 깊은 생각이 필요하다는 공감대가 형성되곤 하는것 같다.'
featured_image: ''
tags: ['developer', '서울버스앱', '앱 개발', '앱 업데이트', '한우찾기']
---
<div style="text-align: justify; line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">몇개의 앱을 개발하지도 않고 이런 애기를 하는게 웃기긴 하지만, 주변의 다른 앱 개발자 들의 말을 들어보아도 앱 업데이트에 대한 깊은 생각이 필요하다는 공감대가 형성되곤 하는것 같다. </span></span><span style="font-family: Dotum; font-size: 11pt; ">어제 하나의 메일이 왔다. 그리고 오늘 혹시나 하는 마음에 “</span>[<span style="font-size: 11pt; ">한우찾기</span>](http://ash84.tistory.com/category/Projects/%ED%95%9C%EC%9A%B0%EC%9D%B4%EB%A0%A5%EC%B6%94%EC%A0%81%EC%A1%B0%ED%9A%8C "[http://ash84.tistory.com/category/Projects/%ED%95%9C%EC%9A%B0%EC%9D%B4%EB%A0%A5%EC%B6%94%EC%A0%81%EC%A1%B0%ED%9A%8C]로 이동합니다.")<span style="font-family: Dotum; font-size: 11pt; ">” 리뷰를 확인해서 내용을 종합해 보면, </span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span></div><div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><div class="txc-textbox" style="border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-top-color: rgb(203, 203, 203); border-right-color: rgb(203, 203, 203); border-bottom-color: rgb(203, 203, 203); border-left-color: rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 11pt; ">실제 한우를 많이 키우시는 분이고, 한우를 사서 넣을때 지금 제공하는 정보 외에도 다른 정보가 있었으면 좋겠다고 그리고, 또 앱 리뷰에서는 어떤 분이 프리마틴 정보에 대해서 알려 달라고 하시는 분도 있다.</span>

<span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; "> </span>

</span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><figure class="wp-caption aligncenter" style="width: 411px">![](http://ash84.net/wp-content/uploads/1/cfile23.uf.1845AC544E24C42E17A321.png)<figcaption class="wp-caption-text">다양한 앱 리뷰</figcaption></figure>

<span style="font-size: 11pt; ">  
</span>

<span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">이 정보들에 대한 요구사항은 사실상 여간 기분좋은 일이 아닐수 없다. 일반 회사에서 영업이나 기획팀에서 추가해달라고 기능을 떡 하니 던져놓고 가는것과는 차원이 다르다. 이상하지만 말이다. 욕이 아니고, 요구사항인데 기분이 좋다. 이상은 여기까지. 문제는 한우찾기 v3를 어느정도 염두해 두고 있는 이 상황에서 위의 요구사항을 어떻게 반영할 것인가 하는 것이다. </span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span></div><div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">단순히 정보의 추가로 끝날 문제가 아니다. 실제로 고객들이 아는것 보다, 하나의 기능을 위해서 우리 앱 개발자가 해야할일은 상당히 많다. 마치 수면아래의 백조의 발 처럼 말이다. 예를 들면, 프로마틴 정보에 대한 웹 서비스를 찾아야 하고, 실제로 없다면 반영이 불가능하다. 만약 있다고 하면, HTML 파싱을 해야하는 하나 더 대상이 늘어 나는 것이고 속도 및 성능의 문제도 고려해야한다. (실제 이 부분은 지금도 심각히 고민중이다. 서버 프로그램을 돌릴 계획도 있다.) </span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span></div><div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">이런 행복한 앱 업데이트에 대한 문제 말고도 사실은 형편상 안 될 경우도 있다. 유료앱의 경우 보통 0.99$ 정도 하는데 그에비해 사용자는 사실 평생 무료 업데이트를 해주기를 바란다. 그러나 개발자도 경제적인구이다 보니 그것이 쉽지 않고, 조금의 업데이트가 늦으면 사실 별점이 내려가기 마련이다.</span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span></div><div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><span style="font-size: 11pt; ">지속저인 업데이트가 필수 이긴 하지만, 전업 앱 개발자의 경우 내 생각엔 다음 앱을 위한 준비를 할 틈이 없을것 같다는 생각이 든다. 실제로 이런 고민을 하는 많은 개발자들도 보았고, 앱 업데이트에 대한 개발자들의 생각을 미투데이에서 공개적으로 물어본적도 있었다. </span>  
<span style="font-size: 11pt; ">  
</span><span style="font-size: 11pt; ">  
</span>

![](http://ash84.net/wp-content/uploads/1/cfile29.uf.177ABF554E24C51A1DC777.png)

<span style="font-size: 11pt; ">  
  </span>

</span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span></div><div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><span style="font-size: 11pt; "> 무료 앱 개발자의 경우는 앱 업데이트에서 좀 편할 수도 있지만 ,사실 그렇지 않다. </span>[<span style="font-size: 11pt; ">서울버스 앱의 광고 사태</span>](http://blog.naver.com/bybybyus?Redirect=Log&logNo=10109487224 "[http://blog.naver.com/bybybyus?Redirect=Log&logNo=10109487224]로 이동합니다.")<span style="font-size: 11pt; ">에서도 보았듯이, 사실 많이 사용하는 무료앱에 대한 유지는 무료가 아니다. 아이러니 하지만. 사용자는 무료앱이라도 왠지 내가 샀는데 왜 업데이트를 안해주냐, 버그가 많냐 등등을 두고 모라고 하지만, 그런 사용자들을 개발자들이 욕할수도 없는 노릇이 아닌가. 내가 사용자라도 그러니까 말이다. </span></span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span></div><div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><span style="font-size: 11pt; ">최근에 </span>[<span style="font-size: 11pt; ">네이버의 서울버스앱에 대한 지원</span>](http://news.donga.com/3/all/20110710/38698026/1 "[http://news.donga.com/3/all/20110710/38698026/1]로 이동합니다.")<span style="font-size: 11pt; ">을 보면서 좀더 그런 환경이 많이 조성되어야 한다고 생각한다. 개발사들이 개발자들을 품에 앉는것이 전체적인 산업 발전에도 이득이 있다고 보기 떄문이다. 공공앱은 홍익인간의 정신을 이어 받듯이 여러사람을 이롭게 하는것이 목적이고, 그런 목적이 유지되기 위해서는 비용과 시간 그리고 노력이 필요하기 떄문이다. </span></span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span></div><div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; "><span style="font-family: Dotum; "><span style="font-size: 11pt; "> </span><font color="#840000"><span style="font-size: 11pt; ">나는 여기서 사용자 분들에게 무료앱 업데이트에 대해서 요구하지 말라고, 버그에 대해서 모라고 하지 말라고 말할 수는 없다. 그것은 당연한 권리기 때문이다. 다만, 한가지 부탁할 것은 버그나, 요구사항에 대해서 메일이나 리뷰를 통해서 알려주실때는, 조금은.. 따뜻한 말투로 알려주셨으면 좋겠다는 것이다. 앱 개발자는 서버가 아니라, 그 역시 사람이기에 말이다. </span></font></span></span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span></div><div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; "> </span></span></div>

