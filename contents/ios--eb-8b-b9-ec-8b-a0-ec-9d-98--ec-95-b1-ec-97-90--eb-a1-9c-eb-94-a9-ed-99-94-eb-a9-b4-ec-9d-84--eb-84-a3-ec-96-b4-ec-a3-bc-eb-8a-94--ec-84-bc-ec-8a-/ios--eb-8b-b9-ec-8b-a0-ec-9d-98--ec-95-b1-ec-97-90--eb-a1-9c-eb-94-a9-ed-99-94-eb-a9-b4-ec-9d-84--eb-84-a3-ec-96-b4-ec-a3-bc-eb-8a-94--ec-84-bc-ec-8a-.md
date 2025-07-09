---
title: '[iOS] 당신의 앱에 로딩화면을 넣어주는 센스~!!'
author: 'ash84'
pub_date: '2011-03-14'
description: '2월 어플이 상당히 많이 늦어지고 있는데, 그만큼 1월에 비해서 공을 많이 들이게 되는것 같습니다. 예전에 언급한것 처럼 한우이력조회를 할 수 있는 어플이 될것같습니다. 이제 거의 코드정리 및'
featured_image: ''
tags: ['dev', 'loading', 'UIAlterView', '검은뷰', '로딩화면', '로딩화면 아이폰', '애플', '앱']
---


<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><font color="#333333" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">2월 어플이 상당히 많이 늦어지고 있는데, 그만큼 1월에 비해서 공을 많이 들이게 되는것 같습니다. 예전에 언급한것 처럼 한우이력조회를 할 수 있는 어플이 될것같습니다. 이제 거의 코드정리 및 메모리 릭 관리 부분만 남아 있는 상황이라서, 끝까지 화이팅 해 보렵니다. </span></span></font></div><div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><font color="#333333" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; "><span style="font-size: 11pt; ">  
</span></span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; ">  
<span style="font-size: 11pt; ">  
</span></span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; "><figure class="wp-caption aligncenter" style="width: 452px">![](http://ash84.net/wp-content/uploads/1/cfile7.uf.1919F1444D7D86E8326E76.jpg)<figcaption class="wp-caption-text">세상엔 다양한 로딩화면이 있습니다. </figcaption></figure>

<span style="font-size: 11pt; ">  
</span>

</span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림">  
<span style="font-size: 11pt; ">  
</span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span><font face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#333333"><span style="font-size: 11pt; ">이번 어플을 개발하면서 많이 신경 쓴것 중 하나가 바로</span></font><font color="#E31600"><span style="font-size: 11pt; "> ‘</span>**<span style="font-size: 11pt; ">로딩화면’</span>**</font><font color="#333333"><span style="font-size: 11pt; "> 입니다. 실질적으로 요즘 어플이나 프로그램들은 로딩화면이 없으면 사용자에게 욕을 먹는 그런시대가 됐죠. 로딩화면을 두어야하는</span>**<span style="font-size: 11pt; "></span>**</font><font color="#318561">**<span style="font-size: 11pt; ">2가지 이유</span>**</font><font color="#333333"><span style="font-size: 11pt; ">가 있습니다. </span></font></span></span></font></div><div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><font face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#333333"><span style="font-size: 11pt; ">  
</span></font></span></span></font></div><div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><font color="#333333" face="굴림"><span style="font-size: 11pt; ">  
</span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; ">****</span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; color: rgb(51, 51, 51); line-height: 2; "><span style="font-size: 11pt; ">  
</span><div style="text-align: justify;line-height: 2; "><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; ">**<span style="font-size: 11pt; ">1. 사용자에게 로딩중임을 알려주는 기능 </span>**</span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify;line-height: 2; "><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; ">**<span style="font-size: 11pt; ">2. 사용자의 입력 차단 </span>**</span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify;line-height: 2; "><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

</div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "></div><div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><font color="#333333" face="굴림"><span style="font-size: 11pt; ">  
</span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">일단 로딩중임을 알리는 것이 가장 중요하죠. 프로그램에 사용자가 요청을 했는데 가만히 멍~ 때리고 있으면 안되니까, 시간이 걸리거나 하는 것이라면 로딩화면을 주는것이 맞습니다. 두번째는 사용자의 입력차단인데요. 사실 로딩을 하는 중에 입력을 받을 수가 있는데 그로 인해서 문제가 생길 수가 있습니다. </span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림">  
<span style="font-size: 11pt; ">  
</span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><font face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#C84205"><span style="font-size: 11pt; ">예를 들어서, UITableVIew 에서 사용자가 특정 셀을 누르면 웹에서 데이터를 읽어와서 그 데이터를 SubView 에서 보여주는 로직이라고 생각을 해 보면, 셀을 누르고 나서, 로딩이 되는 동안 다시 셀을 누르면 addSubView가 두 번 호출되게 되고, 결국 보여주려고 하는 창의 Depth가 2단계로 내려가는 문제가 발생합니다.</span></font><font color="#333333"><span style="font-size: 11pt; "> </span></font></span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림">  
<span style="font-size: 11pt; ">  
</span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span><font face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#333333"><span style="font-size: 11pt; ">실제로 제가 겪었던 일이기도 하구요. 물론 셀을 클릭했을때, flag를 두어서 다른 셀의 입력을 못 받게 하는 방식도 하나의 방식이긴 하지만, 약간 번거롭게 느껴지기도 합니다. </span></font>**<font color="#8E8E8E"><span style="font-size: 11pt; ">그렇다면 다른 앱에서는 어떻게 처리를 할까요?</span></font>**</span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림">  
<span style="font-size: 11pt; ">  
</span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림">  
<span style="font-size: 11pt; ">  
</span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림"><figure class="wp-caption aligncenter" style="width: 320px">![](http://ash84.net/wp-content/uploads/1/cfile22.uf.131E38424D7D86513EC011.PNG)<figcaption class="wp-caption-text">echofon 의 로딩화면</figcaption></figure>

<span style="font-size: 11pt; ">  
</span>

</font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span><font face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#333333"><span style="font-size: 11pt; ">제가 현재 애용하고 있는 트위터 앱인 </span></font>**<font color="#7293FA"><span style="font-size: 11pt; ">echofon</span></font>**<font color="#333333"><span style="font-size: 11pt; "> 입니다. 이 앱은 트위팅을 할때, 문자를 입력하고, 전송 버튼을 누르면 검은 화면이 나오면서, 바람개비(Activity Indicator)가 나오면서 로딩중임을 알려줍니다. 실제로 이렇게 하는 어플들이 많더군요. </span></font></span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림">  
<span style="font-size: 11pt; ">  
</span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span><font face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; "><font color="#105738"><span style="font-size: 11pt; ">이 방법을 좀더 기술적으로 보면, 원래 View 에서 반투명 상태의 View 를 하나 만들어서 그 위에  Activity Indicator 를 올리는 것입니다. 예를 들면, 셀을선택 할떄, View를 보여주면서 View 안에 Activity Indicator를 StartAnimating 을 시켜주면 되는 것입니다. 로딩이 끝나게 되면 해당 Activity Indicator 를 멈추고, View 를 hidden 시키면 되는 것이구요.</span></font><font color="#333333"><span style="font-size: 11pt; "> </span></font></span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림">  
<span style="font-size: 11pt; ">  
</span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><font color="#004C5F" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; ">**<span style="font-size: 11pt; ">View 를 올리는 가장 큰 목적은 무엇을까요? </span>**<span style="font-size: 11pt; ">네, 맞습니다. 뷰를 올리게 보면, 반투명뷰가 제일 위에 올라오기 때문에 사용자가 아무리 터치를 해대도 실제 반응을 하는 뷰에는 영향을 미치지 않는 것이지요. </span></span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><font color="#2B8400" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; ">**  
<span style="font-size: 11pt; ">  
</span>**</span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><font color="#2B8400" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; ">**  
<span style="font-size: 11pt; ">  
</span>**</span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span><font color="#2B8400" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; ">**  
<span style="font-size: 11pt; ">  
</span>**</span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span><font color="#2B8400" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; ">****<figure class="wp-caption aligncenter" style="width: 320px">![](http://ash84.net/wp-content/uploads/1/cfile3.uf.141002594D7D87C50BAA2E.PNG)<figcaption class="wp-caption-text">현재 개발중인 앱의 일부. </figcaption></figure>

</span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; color: rgb(51, 51, 51); line-height: 2; "><span style="font-size: 11pt; ">  
</span><font color="#2B8400" face="Dotum" size="2"><span style="line-height: 26px; ">**  
<span style="font-size: 11pt; ">  
</span>**</span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-family: Dotum; color: rgb(6, 134, 168); font-size: 11pt; ">다른 방식도 있습니다.  그건바로 </span>**<span style="font-size: 11pt; ">UIAlertView를 이용하는 방법</span>**<span style="font-family: Dotum; color: rgb(6, 134, 168); font-size: 11pt; ">인데요. 뷰 전체를 가리고 싶지 않은 경우도 있는데, 그럴경우 이 방법을 추천드립니다. UIAlertView는 아이튠즈에서 앱 다운 받을때, 계정의 패스워드 입력하라고 뜨는 일종의 대화상자.. 라고 보면 될것 같은데요. 이것의 </span>**<span style="font-size: 11pt; ">가장 큰 특징은 바로 모달(Modal) 이라는 것</span>**<span style="font-family: Dotum; color: rgb(6, 134, 168); font-size: 11pt; ">입니다. 즉, Show 함수로 출력해 버리면 AlertView 가 내려오기 까지는 계속 사용자가 터치를해도 AlterView가 받는 다는 것이죠. 로딩화면을 원한다면 AlterView에 바람개피(Activity Indicator)를 addSubView 로 넣어주시고, Animating 을 걸어주시면 됩니다. </span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-family: Dotum; font-size: 11pt; color: rgb(6, 134, 168); line-height: 2; ">근데 원래 AlterView는 생성시에 버튼을 넣을수가 있습니다. 원래는 버튼을 눌러야 modal 이 해제 되면서 AlertView가 사라지는데, 로딩화면이기 때문에 로딩이 끝나면 해당 AlterView를 내려 주시면 됩니다. </span></div><div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><font color="#0686A8" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">  
</span></span></font></div><div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><font color="#333333" face="굴림"><span style="font-size: 11pt; ">  
</span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림">**<span style="font-size: 11pt; ">마치며.. </span>**</font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">이 밖에도 다양한 로딩 화면이 있을수 있다고 생각합니다. ProgressBar를 넣는것도 좋은 방법이라는 생각이 들어요. 만약, 데이터 처리 혹은 전송을 정량적으로 확인할 수 있다면 바람개비(Activity Indicator) 보다는 ProgressBar가 나을 것이라는 생각이 듭니다. </span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림">  
<span style="font-size: 11pt; ">  
</span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span><font color="#333333" face="굴림"><span style="font-size: 10pt; "><span style="font-family: Dotum; font-size: 11pt; ">분명한건 사용자에게 현재 앱의 상황을 적절하게 잘 알려주는 것이 중요하다는 생각이 들었습니다. 개발자가 생각한대로 사용자가 앱을 쓸 수도 있지만, 그런 시나리오가 아닌 방향으로 쓸 수도 있거든요.^^ 친절한 앱을 배라할 수 있는 그날까지~ 쭈욱~ </span></span></font></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; line-height: 2; color: rgb(51, 51, 51); "><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="text-align: justify; color: rgb(51, 51, 51); font-family: 굴림; font-size: 9pt; line-height: 2; "></div>

