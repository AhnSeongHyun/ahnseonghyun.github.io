---
title: '(iOS) 바코드 인식 라이브러리 ZBar 사용법'
author: 'ash84'
pub_date: '2016-08-03'
description: ''
featured_image: ''
tags: ['dev', 'Objective-C', 'ZBAR', '바코드', '바코드 인식 앱', '바코드인식']
---


<span style="font-size: 11pt;">한우찾기 앱은 처음부터 ZBAR 라이브러리를 사용해 왔었는데 그동안 정리할 기회가 없었는데 이번 기회에 사용법에 대한 부분을 정리하는 포스팅을 하려고 한다. 나두 자꾸 까먹어서리. </span>

<span style="font-size: 11pt;">**1. 다운로드**</span>

<span style="font-size: 11pt;">– 현재 시점(2013.추석연휴)기준으로 ZBar iPhone5 이상에 문제가 없게 하려면 다음의 링크에서 SDK를 다운받기를 권장하는 바이다. 기존의 ZBAR 라이브러리를 사용할 경우 컴파일 에러가 나기 때문에 이 부분은 꼭 숙지를 하시길. 그게 아니라면 빌드를 스스로 해서 사용해야 할것이다. </span>

<span style="font-size: 14.545454025268555px; line-height: 26.363636016845703px;">– [http://ash84.tistory.com/1022](http://ash84.tistory.com/1022)</span>

<span style="font-size: 11pt;">**2. 사용법**</span>

<script src="https://gist.github.com/AhnSeongHyun/6639111.js"></script>

<span style="font-size: 11pt;">`ZBarReaderDelegate`를 사용할 ViewController 에서 지정을 해준다. </span><span style="font-size: 11pt; line-height: 2;">`ZBarReaderDelegate` </span><span style="font-size: 11pt; line-height: 2;">역할은 실시간 카메로 혹은 사진 앨범에서 바코드 인식 이후의 결과에 대한 액션을 지정할 수 있도록 해준다. </span>

<span style="font-size: 9pt; line-height: 2;">  
</span>

<span style="font-size: 11pt; line-height: 2;">바코드를 인식하는데 있어서 2가지 방법이 있는데 하나는 카메라로 사용자가 실시간으로 인식하는 것이고 다른 하나는 기존의 사진 앨범 라이브러리에서 사진을 가져와서 인식시키는 방법 2가지이다. 하나씩 차근차근 알아보자. 일단 카메라로 실시간으로 인식하는 코드를 보자. </span>

<span style="font-size: 9pt; line-height: 2;">  
</span>

<script src="https://gist.github.com/AhnSeongHyun/6639123.js"></script>

<span style="font-size: 9pt; line-height: 2;">  
</span>

<span style="font-size: 11pt; line-height: 2;">위의 코드에서 보면 `ZBarReaderController` 객체를 만드는 것 부터 시작하는데 그 객체가 카메라든, 사진이든 실제 이미지에 대한 처리를하는 주체라고 보면 된다. 그리고 나서 delegate 처리를 어디에서 수행할 것인지를 지정한다. 그리고 나서는 사실상 옵션적인 부분인데, 실제 카메라로 비춰질때 그 영역위에(overlay) 다른 이미지나 뷰가 보여지는 상태로 보여줄것이면 뷰를 만들어서 </span><span class="s1" style="font-size: 11pt; line-height: 2;">reader.</span><span style="font-size: 11pt; line-height: 2;">cameraOverlayView에 지정하면 된다. 필자의 경우에는 이미지뷰 2개를 포함하는 뷰를 하나 만들고 그것을 </span><span style="font-size: 11pt; line-height: 2;">cameraOverlayView에 연결시키는 작업을 하였다. </span>

<span style="font-size: 9pt; line-height: 2;">  
</span>

<span style="font-size: 11pt;"></span>

<span class="s1" style="font-size: 11pt;">reader.</span><span style="font-size: 11pt;">`showsZBarControls`</span><span class="s1" style="font-size: 11pt;"> = </span><span class="s2" style="font-size: 11pt;">TRUE</span><span class="s1" style="font-size: 11pt;">; 이 부분은 cancel, info 와 같은 일반적인 컨트롤 버튼들을 보여줄것인가 하는 부분이다. 카메라뷰를 보여주고 취소하거나 info 를 통해서 인식하는 방법을 사용자에게 알려주고 싶을때는 이부분을 활성화 하면 된다. </span>

<span class="s1">  
</span>

<span class="s1" style="font-size: 11pt;">마지막으로 해줘야 하는 부분이 </span><span style="font-size: 11pt; line-height: 2;">`ZBarImageScanner` 객체를 설정하는 것이다. </span><span style="font-size: 11pt; line-height: 2;">`ZBarImageScanner`의 역할은 이미지를 스캐닝하는 작업을 하는 것이고 코드에서 setSymbology 함수에서 자세한 인식 바코드 타입을 지정하면 된다.(이 부분은 공식 레퍼런스 문서 참고 바람.) 그리고 나서 화면에 보여주면 된다. </span>

<span style="font-size: 9pt; line-height: 2;">  
</span>

<script src="https://gist.github.com/AhnSeongHyun/6639180.js"></script>

<span style="font-size: 11pt;">사진 앨범에서 가져오는 부분도 동일하지만 카메라 부분과 다른 부분위주로 설명하면 다음과 같다. reader의 sourceType을 </span><span style="font-size: 11pt; line-height:2;">`UIImagePickerControllerSourceTypePhotoLibrary`로 지정하는 것이 가장 중요한 부분이다. 3가지 타입으로 지정할수있는데 reader를 생성하게 되면 </span><span style="font-size: 11pt; line-height: 2;">`UIImagePickerControllerSourceTypeCamera`를 기본으로 지정하는것 같다. 때문에 모든 사진 라이브러리를 사용하거나 저장된 사진 라이브러리를 사용하려면 </span><span style="font-size: 11pt; line-height: 2;">`UIImagePickerControllerSourceTypePhotoLibrary`,</span><span style="font-size: 11pt; line-height: 2;">`UIImagePickerControllerSourceTypeSavedPhotosAlbum` 을 지정해서 사용하면 될것이다. </span>

<span style="font-size: 9pt; line-height: 2;">  
</span>

![](http://ash84.net/wp-content/uploads/1/cfile8.uf.2703DD45523C70BC18BE3E.PNG)

<span style="font-size: 9pt; line-height: 2;">  
</span>

<script src="https://gist.github.com/AhnSeongHyun/6639211.js"></script>

<span style="font-size: 11pt;">자 이제, delegate에서 처리하는 부분을 보자. 크게 2가지인데, 인식을 했을때와 하지 못했을때의 delegate 처리이다. </span>

<script src="https://gist.github.com/AhnSeongHyun/6639432.js"></script>

<span style="font-size: 11pt;">위의 코드가 인식이 성공했을때 사용되는 코드인다. `ZBarSymbol `객체에 인식된 결과를 받아와서 처리하면 된다. 그런데 주의할점은 인식이 성공했다는 것이지 어떤 제대로 된 값이 들어있는지에 대한 것과는 다르기 때문에 type 을 체크하는 부분을 거치고 그 부분이 통과 되면 개발자 본인이 생각하는 검증을 하면된다. 필자의 경우 조회하는 코드내 문자열의 길이가 12자리여서 체크를 하는 부분이 있었다. 인식이 되어서 성공인지 실패인지를 modes라는 변수로 전달하게 했는데 이 부분은 Notification 으로 처리하거나 하면 될것이다. delegate에서 마지막으로 해줘야 하는 부분은 지금 현재 올라와 있는 인식창을 내리는 부분이다. </span><span style="font-size: 11pt; line-height: 2;">`dismissViewControllerAnimated` 을 통해서 내리면 된다. </span>

<span style="font-size: 9pt; line-height:2;">  
</span>

<script src="https://gist.github.com/AhnSeongHyun/6639412.js"></script>

<span style="font-size: 11pt;">실패할 경우는 실패했다고 하고 내려면 된다. 별거 없다. </span>

<script src="https://gist.github.com/AhnSeongHyun/6639405.js"></script>

<span style="font-size: 11pt;">포토라이브러리나 카메라에서 cancel 버튼을 눌렀을 때의 delegate를 처리하는 부분이 위의 코드이다. 필자의 경우에는 별다른 처리를 하지 않는데, cancel 버튼을 누른 다음에 팝업창을 보여주거나 하면 된다. </span>

<span style="font-size: 11pt;">보시는 바와 같이 그리 어렵진 않다. 사실 이 라이브러리는 인식해서 데이터만 가져올뿐 이용해서 어떤 서비스와 조회할것인지는 스스로 판단해야 하며, 좀더 커스텀을 위해서는 `ZBarReaderController` 관련 레퍼런스를 좀더 잘 살펴보는게 필요한것 같다. </span>

<span style="font-size: 10pt;">Reference : </span>

<span style="font-size: 10pt;">–[ http://zbar.sourceforge.net/iphone/sdkdoc/#](http://zbar.sourceforge.net/iphone/sdkdoc/#)</span>



