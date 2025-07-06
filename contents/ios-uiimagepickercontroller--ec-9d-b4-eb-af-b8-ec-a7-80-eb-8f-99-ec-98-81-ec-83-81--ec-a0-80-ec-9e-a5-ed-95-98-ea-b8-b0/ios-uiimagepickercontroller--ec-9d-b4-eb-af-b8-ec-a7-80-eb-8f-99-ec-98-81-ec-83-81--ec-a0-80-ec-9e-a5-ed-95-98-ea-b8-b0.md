---
title: '(iOS) UIImagePickerController Image & Video'
author: 'ash84'
pub_date: '2016-08-11'
description: '매번 찾아서 쓰던건데 너무 귀찮아서 정리한다. 카메라나 동영상의 간단한 뷰를 띄우기 위해서 UIImagePickerController 를 사용하는데 사진을 찍는 방법, 동영상을 찍는 방법 및 아이폰 내장 포토 앨범에 저장하는 방법은 아래와 같다. 
  
#### 1. 띄우기





중요한 점은 카메라가 있는지 체크하는 부분이다. 아이팟이나 일부 애플기기의 경우 카메라가 없을수 있기 때문에 체크해'
featured_image: ''
tags: ['dev', 'IOS', 'save image to photo album', 'UIImagePickerController', '동영상 저장', '이미지 저장', '이미지 포토앨범에 저장']
---


매번 찾아서 쓰던건데 너무 귀찮아서 정리한다. 카메라나 동영상의 간단한 뷰를 띄우기 위해서 UIImagePickerController 를 사용하는데 사진을 찍는 방법, 동영상을 찍는 방법 및 아이폰 내장 포토 앨범에 저장하는 방법은 아래와 같다. 
  
#### 1. 띄우기
<br/>
<script src="https://gist.github.com/AhnSeongHyun/8516125.js"></script>



중요한 점은 카메라가 있는지 체크하는 부분이다. 아이팟이나 일부 애플기기의 경우 카메라가 없을수 있기 때문에 체크해서 그에 맞게 대응을 해줘야 한다. 띄워줄 타입을 카메라로 하고 편집 기능을 사용할것인지를 설정해 줘야 한다. delegate를 self 로 지정해 줘야 불러온곳에서 쓸수 있다. 
   
#### 2. 찍기
<br/>
<script src="https://gist.github.com/AhnSeongHyun/8516152.js"></script>
 

찍는 부분인데, UIImagePickerController는 띄운 상태에서 동영상, 사진의 여부를 사용자가 직접 선택할수 있기 때문에 찍는 부분을 따로 구현을 한다면 동영상인지  사진인지를 구분해 줘야 한다. `cameraController.cameraCaptureMode` 를 이용해서 그것을 판단할 수가 있다. 사진의 경우 `takePicture` 함수로 사진을 찍을수가 있고 동영상의 경우`startVideoCapture` 함수를 이용해서 찍는것을 성공했는지를 판별해야 한다. 실패하는 경우는 카메라가 없는 경우나 이미 찍는경우나 저장공간이 모자른 경우이다. 위의 코드에서는 저장공간에 대한 예외는 배제하고 찍는 경우라면 `stopVideoCapture` 함수를 통해서 동영상 녹화를 멈추도록 하였다. 
 
#### 3. 저장하기
<br/>

저장할때도 동영상과 사진을 따로 저장해야 한다. 아래의 코드를 보자.
<script src="https://gist.github.com/AhnSeongHyun/8516170.js"></script>


UIImagePickerControllerDelegate 의 두 함수를 구현하고 있는데 `didFinishPickingMediaWithInfo:` 카메라 뷰가 떠 있는 상태에서 찍은것이 성공하고 use photo를 눌렀을때, 발생되는 함수고 `imagePickerControllerDidCancel:` 함수는 말그대로 취소버튼을 눌렀을때 발생되는 함수이다. 

코드에서 보는것과 같이 취소버튼을 누르면 그냥 내리면 된다. 그러나 찍은것이 성공할후로는 저장을 해야하는데 이때에는 delegate 함수로 전달되는 NSDictionary 형식의  
 info 에서 데이터를 가져오는 작업을 해야한다. 첫번째로 촬영한것이 사진인지 동영상인지 판별해야 한다. UIImagePickerControllerMediaType 이라는 것을 가져와서 판별하도록 되어 있는데, 필자는 여기서 그 판별하는 것을 아래와 같이 따로 enum 으로 빼서 `getMediaType:` 함수를 통해서 가져오도록 하였다.

<script src="https://gist.github.com/AhnSeongHyun/8516180.js"></script>

여기서 중요한 부분은 `kUTTypeImage`, `kUTTypeMovie` 등을 사용하려면 MobileCoreService.framework 를 추가해야하고 사용하는 곳에서  
 #import <MobileCoreServices/MobileCoreServices.h>를 추가해 줘야 한다는 점이다.

다시 저장하는 곳을 보면 사진의 경우에는 수정된 이미지와 원래 이미지를 가져올수 있기 때문에 두개가 가져오는데 일단 처음에는 수정된 이미지를 가져와서 없으면 원래의 이미지를 가져오면 된다. 수정된 이미지가 없을수 있는 것은 처음에 UIImagePickerViewController를 띄울때 allowEditing 속성을 No로 하면 편집 화면으로 넘어가지 않기 때문에 가져올수가 없게 된다 저장할때에는 `UIImageWriteToSavedPhotosAlbum` 를 사용해서 저장하면 된다.

동영상의 경우, 동영상의 경로를 가져오고 나서 `UIVideoAtPathIsCompatibleWithSavedPhotosAlbum` 를 통해서 저장이 가능한지 알아보고 `UISaveVideoAtPathToSavedPhotosAlbum` 를 통해서 저장을 하면 된다. 

UIImagePickerController를 이용하는것을 그렇게 어렵지 않지만, 아쉽게도 실제 개발 환경에서는 이것을 잘 이용하게 되진 않는것 같다. 예를 들어, use photo 라는 사용자 액션 없이 저장하고 싶어서 use photo/retake 단계는 없앨수가 없다. 이런 부분을 개발하려면 UIImagePickerController 같은 카메라 뷰를 직접 만들어야 한다고 한다. 요즘에는 오픈소스가 많아서 찾아 보는 것도 하나의 방법이라고 생각되어 진다. 

