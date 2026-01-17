---
title: '(iOS) UIActivityController 을 통해서 공유를 쉽게하자.'
author: 'ash84'
pub_date: '2013-09-12'
description: '다시 앱과 서비스 개발에 매진을 하고 있는데 최근에 한우찾기 iOS7 작업을 진행하고 있는데 `UIActivityController`를 사용한 경험에 대해서 공유하고자 한다. 일단 아래의 불편한 진실을 보고 시작하자. 
**iOS7에서 깨지는것 외에도 기존의 결과 뷰에서 복사하기, 저장하기 메일로 보내기 버튼이 하단에 있는 문제점과 함께 카카오톡이나 페이스북, 메일, 라인 등으로 보낼수 없다는게 가장 큰 이'
featured_image: ''
tags: ['Custom UIActivity', 'dev', 'UIActivity', 'UIActivityViewController', 'iOS']
---
<span style="font-size: 11pt;">다시 앱과 서비스 개발에 매진을 하고 있는데 최근에 한우찾기 iOS7 작업을 진행하고 있는데 `UIActivityController`를 사용한 경험에 대해서 공유하고자 한다. 일단 아래의 불편한 진실을 보고 시작하자. </span>

<span style="font-size: 11pt;">**iOS7에서 깨지는것 외에도 기존의 결과 뷰에서 복사하기, 저장하기 메일로 보내기 버튼이 하단에 있는 문제점과 함께 카카오톡이나 페이스북, 메일, 라인 등으로 보낼수 없다는게 가장 큰 이슈였다.** 그래서 생각한 것이 `UIActivityController` 이다. </span>
 

<span style="font-size: 11pt;">이걸 사용해서 가질수 있는 **가장 큰 장점은 2가지이다.**</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">1. 사용자가 상단의 NavigationBar 우측 상단의 버튼을 눌러서 현재 보는 화면 하단 위에 뜨기 때문에 결과뷰의 스크롤 어디서라도 사용할 수 있다는 장점이 있다. 기존에는 반드시 아래에 가서 눌러야 했다. </span>

<span style="font-size: 11pt;">2. 공유와 저장을 한번에 할수 있다. 본인이 원하는 메신저 혹은 메일로 누군가에게 보낼수 있고 그게 아니면 내 앱에 저장할수 있도록 제공하였다. </span>

</div><span style="font-size: 11pt;">기술적인 부분으로 넘어가서 제일 중요한 것은 어떻게 CustomActivity를 추가할 수 있느냐인것이다. 나는 여기서 카카오톡과 라인 그리고 내 앱내에 저장하기 이렇게 3가지의 CustomActivity를 필요로 했다. 오픈소스를 찾아야 한다. 바퀴를 또 만들 필요는 없다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 14.545454025268555px; line-height: 26.363636016845703px;">[https://github.com/shu223/UIActivityCollection](https://github.com/shu223/UIActivityCollection)</span>

</div><span style="font-size: 11pt;">위의 오픈소스를 보면 알겠지만 꽤 많은 세계의 개발자 분들이 어떤 앱의 링크로 바로 연결 할수 있는 CustomUIActivity를 만들어 두었다. 이런것을 바탕으로 내가 찾은것은 아래의 링크이다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 14.545454025268555px; line-height: 26.363636016845703px;">[https://github.com/l4u/DCActivities](https://github.com/l4u/DCActivities)</span>

</div><span style="font-size: 11pt;">카카오톡과 라인에 대한 Custom UIActivity다. 굳이 만들 필요는 없어서 일단 이것을 사용하기로 하는데 내 앺에 저장하기는 만들어야 하기 때문에 해당 오픈 소스에 대한 분석을 했다. 말이 좋아 분석이지 그냥 훑어보기다 함수도 10개가 안된다. </span>

<span style="font-size: 11pt;"></span>

<span style="font-size: 11pt;">`DCLineActivity`를 기준으로 설명을 하자면, </span><span style="font-size: 11pt; line-height: 2;">`DCLineActivity` 클래스는 일단 `UIActivity` 클래스를 상속받아서 사용하는데 (이건 당연하다.)몇가지 함수를 구현하면 된다. 하나하나씩 설명을 하자면 다음과 같다. </span>

<span style="font-size: 9pt; line-height: 2;">  
</span>

<script src="https://gist.github.com/AhnSeongHyun/6522676.js"></script>

<span style="font-size: 11pt;">위의 3함수는 만든 `UIActivity`에 대한 어떤 표시를 해주는 것이다. 그래서 `activityType`을 정하고, </span>

<span style="font-size: 11pt; line-height:2;">`activityTitle` 를</span><span style="font-size: 11pt;"> 정하고, `activityimage`를 지정해 주어야한다. 물론 nil도 가능하다. 그런데 title의 경우 실제 화면에서 아이콘 아래에 나오는 텍스트이며, image는 실제 보여지는 아이콘이다. </span>
 
<span style="font-size: 11pt;">**아이콘 이미지 지정시 주의할점 중 하나는 지정된 이미지에 회식의 둥근 테두리 박스가 쳐져서 보여진다는 점과 함께 컬러를 넣어도 흑백이 나온다는 점이다(iOS7에서만 그럴지도) 이 부분은 실제 테스트를 하면서 확인해 보시길 바란다.**</span>

<span style="font-size: 11pt;">자, 이제 보여지는 부분은 됐고, 실제 수행하는 부분을 보자 </span>

<script src="https://gist.github.com/AhnSeongHyun/6522728.js"></script>

<span style="font-size: 11pt;"></span>

<span style="font-size: 11pt;">`canPerformWithActivityItems` 함수를 보면 LINE 앱의  URL을 열수 있는지 체크하는 부분이 보인다. 즉 이 함수에서는 어떤 행동을 할수 있는지를 검사하는 코드를 넣어야 한다. 어떤 앱과 연결할 것이라면, 해당 앱이 없으면 실행할 수가 없는것 처럼 말이다. </span>

<span style="font-size: 11pt;"></span>

<span style="font-size: 11pt;">`prepareWithActivityItems` 함수는 `NSArray` 에서 데이터를 가져오는 부분을 볼수 있다. 간단히 말해서 이 함수는 어떤 실행 전에 데이터를 가져다 두는 작업을 하는 것이다. 예를 들어, LINE 에 어떤 문자열을 실행하도록 보낸다고 하면 문자열에 해당하는 데이터를 가져와야 한다. 이 데이터는 `UIActivityController` 를 호출할때 지정하면 된다. 이 부분은 호출하는 코드에서 좀더 자세히 설명하도록 하겠다. </span>

<span style="font-size: 11pt;"></span>

<span style="font-size: 11pt;">`performActivity`함수가 실제 우리가 원하는 액션을 하는 함수이다. 이 함수에서는 원하는 행동을 하는 코드를 작성한다. 위의 예제에서 보면 LINE 앱을 전달하려는 message를 실어서 여는 것을 확인할 수 있다. </span>

<span style="font-size: 11pt;">별거 없다. 정리하자면, 실행할수 있는지 확인하고, 데이터 가져오고, 실행하고다. </span>

<span style="font-size: 11pt;">호출하는 쪽 코드를 보자. </span>

<script src="https://gist.github.com/AhnSeongHyun/6522822.js"></script>

<span style="font-size: 11pt;">카카오, 라인앱에 대한 UIActivity 만든것에 대한 객체를 생성하고, `UIActivityController` 를 생성을 하는데 주의깊게 보자. 가장 중요한 부분은 `activityItem` 을 지정하는 부분으로 여기서는 나는 한우정보 문자열을 넣었다. 여기에 앞에서 말한 </span><span style="font-size: 11pt; line-height: 2;">`prepareWithActivityItems` 함수에서 가져올 데이터를 넣어주면 된다. 그리고 나서 `applicationActivities` 에 어떤 `UIActivity`를 보여줄것인가를 지정하면 된다. 앞에서 생성한 카카오, 라인앱에 대한 </span><span style="font-size: 11pt; line-height: 2;">`UIActivity` 객체를 넣어주면된다. </span>

<span style="font-size: 9pt; line-height: 2;">  
</span>

<span style="font-size: 11pt; line-height: 2;">실제로 해보면 별거 없다. 그냥 하면 된다. 이제 내 앱에 저장하기 기능을 `UIActivity`로 만들었던 것을 소개한다. 이건 더 별거 없다. 일단 전체 코드를 보자. 그냥 눈에다 쑤셔박길. </span>

<span style="font-size: 9pt; line-height: 2;">  
</span>

<script src="https://gist.github.com/AhnSeongHyun/6533473.js"></script>

<span style="font-size: 9pt; line-height: 2;">  
</span>

<span style="font-size: 11pt; line-height: 2;">보면 알겠지만 내가 만든 `SaveActivity` 는 내부에 저장을 한 후에, 저장되었는지 이미 저장이 되어 있는것인지에 따라서 팝업을 띄우게 되어 있다. 그런데 팝업을 처리하는 부분은 `SaveActivity` 내부가 아니라 호출한 부분에서 `completionHandler` 에서 `activityType` 과 bool 형 `completed` 변수에 따라서 처리를 해주고 있다. `activityType`은 앞에서 설명했듯이 상속받는 클래스에서 재정의 해주면되는데 필자는 “SaveActivity” 라는 이름을 지정했다. `completed` 는 `performActivity` 함수 이후에 `UIActivityViewController` 를 닫아야 하는데 닫을때 지정해 줄수 있다. </span><span style="font-size: 11pt; line-height: 2;">`activityDidFinish` 함수에 지정해 주면된다. </span>
 

<span style="font-size: 11pt;">별거 없다. 필요한거 서브클래싱해서 만들면 되고 적당한 아이콘 웹에서 가져와서 사용하면된다.(저작권 주의, 언제부터?) 약간 분석을 하긴 했지만 그래두 몇 시간 투자해서 고민했던 부분이 깔끔해 져서 좋다. 비슷한 고민이 있으시다면 만들어 보시길. </span>

<span style="font-size: 9pt; line-height: 2;">  
</span>

[2014/01/20 – [Programming/iOS] – (iOS) UIImagePickerController 이미지/동영상 저장하기](http://ash84.tistory.com/entry/iOS-UIImagePickerController-이미지동영상-저장하기)

[2013/09/27 – [Programming/iOS] – (iOS) UIAlertView TextField 추가 및 키보드 변경](http://ash84.tistory.com/entry/iOS-UIAlertView-TextField-추가-및-키보드-변경)

<span style="font-size: 11pt;"></span>



