---
title: '[앱 파헤치기] 고생해라. 미투데이 앱의 사용자여!!'
author: 'ash84'
pub_date: '2011-04-13'
description: '저는 몇가지 SNS 를 하는데요, 트위터, 페이스북, 미투데이가 가장 대표적인 것이겠죠. 트위터는 모바일에서 많이 하지만, 사실 페이스북은 모바일에서 좀 불편해서 잘 안하게 되고.. (링크 연결 입력이 잘 안되는..) 그리고 미.투.데.이. 개인적으로 애기하자면 미투데이 초기때 부터 했고, 트위터 모를때 부터 SN'
featured_image: ''
tags: ['dev', 'NHN', '네이버', '미투데이', 'iOS', '앱 파헤치기']
---
<div><div style="text-align: justify; line-height: 2; "><span style="font-size: 10pt; "><span style="font-family: Dotum; ">저는 몇가지 SNS 를 하는데요, 트위터, 페이스북, 미투데이가 가장 대표적인 것이겠죠. 트위터는 모바일에서 많이 하지만, 사실 페이스북은 모바일에서 좀 불편해서 잘 안하게 되고.. (링크 연결 입력이 잘 안되는..) 그리고 미.투.데.이. 개인적으로 애기하자면 미투데이 초기때 부터 했고, 트위터 모를때 부터 SNS 라는 이름이 몬지 몰랐을때 부터 아, 이거 몬가 재밌다라고 느끼면서 웹에서 하고 했습니다. </span></span></div><div style="text-align: justify;"><span class="Apple-style-span" style="line-height: 24px;">  
</span></div></div><div><span class="Apple-style-span" style="line-height: 2;"><div style="text-align: justify;"><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font class="Apple-style-span" color="#5C7FB0">간단히 미투데이엗 대한 느낌을 말하자면 미투데이는 좀더 트위터 보다 사람냄새나는 SNS 라는 생각이 듭니다. 지극히 개인적으로. 지극히 개인적입니다. 토달지 마세요. </font></span></span></div></span><div style="text-align: justify;"></div><span class="Apple-style-span" style="line-height: 2;"><div style="text-align: justify;"><span style="font-size: 10pt; "><span style="font-family: Dotum; ">자, 오늘은 미투데이 앱을 파헤쳐 볼거에요. <font class="Apple-style-span" color="#E31600">미투데이 앱의 가장 안 좋은거라면 알림으로 인한 뷰의 모달출력이라는 것 입니다.</font> 자, 어렵죠? 말이 어려운데.. 미투데이는 알람을 주고 알람을 보기를 누르면 자연스럽게 미투데이가 뜨게 되는데 해당 내용이 아래에서 올라옵니다. 그런데 한번 생각해 보죠. 하루에 친구신청 혹은 댓글을 10개 이상 받았다고 하고 그것을 다 보기 버튼을 눌러서 봤다고 가정 한다면. </span></span></div></span>

<div style="text-align: justify;"></div><div style="text-align: justify;"></div><span class="Apple-style-span" style="line-height: 2;"><span style="font-size: 10pt; "><span style="font-family: Dotum; "><figure class="wp-caption aligncenter" style="width: 320px">![](http://ash84.net/wp-content/uploads/1/cfile23.uf.112A9F364DA52D1D3EFF26.PNG)<figcaption class="wp-caption-text">자꾸자꾸 올라와 있는 뷰는 많아지고..  
</figcaption></figure></span></span></span>

<div style="text-align: justify;"></div><div style="text-align: justify;"></div><span class="Apple-style-span" style="line-height: 2;"><div style="text-align: justify;"><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font class="Apple-style-span" color="#E31600">추후에 10개 이상의 뷰를 툴바의 닫기 버튼을 눌러야만 내가 원하는 다른 동작을 시킬수 있다는 것입니다.</font> 사실 이것은 상당히 저에게는 귀찮음을 요구하는 부분입니다. 차라리 앱을 다시시작 하는게 빠를것 같아요. 이런 뷰가 나오는 이유는 사실은 모달형식으로 뷰를 열었기 때문입니다. 때문에 다른 뷰를 보려면 무조건 닫기 를 통해서 해당 뷰의 모달을 해제 시켜야 하는 것이지요. </span></span></div></span>

<div style="text-align: justify;"></div><span class="Apple-style-span" style="line-height: 2;"><div style="text-align: justify;"><span style="font-size: 10pt; "><span style="font-family: Dotum; ">예를 들면, 카메라 같은것. 아이폰에서 카메라를 누르면 모달형태로 뷰가 생기면서 카메라의 영상을 보여집니다. 이런식으로 단발성의 액션의 경우에는 모달 형식으로 올리는 것이 좋지만, 위와 같은 경우라면 좀더 다른 방법을 쓰는 것이좋지 않았을까 하는 생각도 들더라구요. </span></span></div></span>

<div style="text-align: justify;"></div><span class="Apple-style-span" style="line-height: 2;"><div style="text-align: justify;"><span style="font-size: 10pt; "><span style="font-family: Dotum; ">어찌보면 트위터 앱들의 알림처럼 내용의 일부를 알림에 보여주는 것도 좋은 방안이라는 생각이 듭니다. 너무 미투데이에 꼭 내용을 들어와서 확인할 필요는 없는 거니까요. 네이버가 자사의 서비스를 많이 사용하도록 고안했다라는 느낌이 많이 들긴 합니다만, 조금만 더 사용자에게 배려심을 가졌으면 하는 바램입니다. </span></span></div></span>

<div style="text-align: justify;"></div><span class="Apple-style-span" style="line-height: 2;"><div style="text-align: justify;"><span class="Apple-style-span" style="line-height: 18px; "><span class="Apple-style-span" style="line-height: 2;"><span style="font-size: 10pt; "><span style="font-family: Dotum; ">ps) 미투데이 </span></span></span>[<span style="font-size: 10pt; "><span style="font-family: Dotum; ">http://me2day.net/ash84_jin</span></span>](http://me2day.net/ash84_jin)<span class="Apple-style-span" style="line-height: 2;"><span style="font-size: 10pt; "><span style="font-family: Dotum; "> 놀러오세요^^ </span></span></span></span></div></span>

<div style="text-align: justify;"></div><div style="text-align: justify;"></div><div style="text-align: justify;"></div></div>

