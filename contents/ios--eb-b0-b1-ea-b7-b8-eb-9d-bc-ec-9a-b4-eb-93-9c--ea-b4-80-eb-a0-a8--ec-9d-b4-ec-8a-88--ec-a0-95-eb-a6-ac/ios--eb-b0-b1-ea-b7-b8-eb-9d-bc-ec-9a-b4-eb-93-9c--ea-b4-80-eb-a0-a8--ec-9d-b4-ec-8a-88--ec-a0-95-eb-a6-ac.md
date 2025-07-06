---
title: '(iOS) 백그라운드 관련 이슈 정리'
author: 'ash84'
pub_date: '2015-07-03'
description: '블루투스와 연결되어서 동작되는 앱을 어떻게 백그라운드에서 유지 시킬것인가 하는 것에 대한 물음이 있었고 여러가지 문제가 있었다. 이 글은 그에대한 여러가지 시도의 방법 그리고 해결방법(도움이 될지)에 대한 내용의 정리이다.'
featured_image: ''
tags: ['App crash', 'Background', 'background fetch', 'dev', 'IOS', 'NSTimeInterval', '백그라운드', '블루투스']
---


<span style="font-size: 11pt;">블루투스와 연결되어서 동작되는 앱을 어떻게 백그라운드에서 유지 시킬것인가 하는 것에 대한 물음이 있었고 여러가지 문제가 있었다. 이 글은 그에대한 여러가지 시도의 방법 그리고 해결방법(도움이 될지)에 대한 내용의 정리이다. </span>

<div style="text-align: justify; line-height: 2;"></div><div class="txc-textbox" style="border: 1px solid #cbcbcb; background-color: #ffffff; padding: 10px;"><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">문제점 </span><span style="background-color: transparent; font-size: 11pt;">: 블루투스와 통신을 하는 앱이 백그라운드로 들어갔을때, </span><span style="background-color: transparent; font-size: 11pt; line-height: 2;">불규칙하게 앱이 꺼지거나 블루투스가 끊어지는 문제 </span></div></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;"> </span></div><div style="text-align: justify; line-height: 2;">**<span style="font-size: 11pt;">[applicationWillTerminate</span><span style="font-size: 11pt;">:메소드에 대한 진실]</span>**</div><div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">일단 로그를 살펴보았고 아쉽게도 UIApplication 클래스의 applicationWillTerminate:</span><span style="font-size: 11pt;"> 메소드는 발생되지 않았다. 사실 이 함수의 발동에 대해서 여러의견이 분분한데 내가 테스트 해봤을때 이 함수의 동작은 “백그라운드 상태에서 앱이 사용자 혹은 iOS 가 메모리 부족으로 앱을 종료시킬때 발생되는 함수” 이다. 그런데 여기서 주의해야할 부분이 이 함수는 백그라운드 상태에서만 동작한다는 것이다. 그런데 백그라운드 상태에서는 중지된(Suspended) 라는 상태가 있다. 이 상태로 앱이 들어가게 되면 발생되지 않는다. 레퍼런스 문서를 읽어보시면 알겠지만 중지된(Suspended)상태로 들어가는 것은 감지할수가 없다. </span></div><div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify;"><span style="font-size: 11pt;">**[Fetch는 타이머가 아니기에] **</span>

<span style="font-size: 11pt; line-height: 2; background-color: transparent;"> </span>

<span style="font-size: 11pt; line-height: 2; background-color: transparent;">자꾸 백그라운드에서 죽어서 fetch 를 한번써보기로 했다. fetch를 사용하는 방법은 아래의 링크들을 참조하면 된다. fetch를 사용해본 결과 fetch는 백그라운드 새로고침과 연관이 있어서 엄청 주기적으로 타이머처럼 돌것이라고 생각할수 있다. 그러나 실제로 테스트를 해보면 그렇지 않다. fetch를 사용하기 위해서는 setMinimumBackgroundFetchInterval:UIApplicationBackgroundFetchIntervalMinimum 을 지정해 주면되는데 실제로  
 UIApplicationBackgroundFetchIntervalMinimum 을 NSTimeInterval 의 값인데 값을 찍어보면 0이 나오는 것을 확인할 수가 있다. 있고 만약 내가 원하는 어떤 NSTimeInterval 의 값을 만들어서 예를 들면 2초라고 지정하고 싶어서 만들어서 지정을 해보면 2초간격으로 작동하지 않는다. 그래서 실제로 콘솔로 찍어 보면 알수도 있고 레퍼런스 문서에도 보면 알수 있겠지만:</span>

<span style="font-size: 11pt;"> </span>

<div class="txc-textbox" style="line-height: 2; border: 1px solid #cbcbcb; background-color: #ffffff; padding: 10px;"><span style="font-size: 11pt;">minimumBackgroundFetchInterval </span>

<span style="font-size: 11pt;">– The minimum number of seconds that must elapse before another background fetch can be initiated. This value is advisory only and does not indicate the exact amount of time expected between fetch operations. </span>

</div><span style="font-size: 11pt;"> </span>

<span style="font-size: 11pt;"> fetch 동작사이의 정확한 시간의 양을 가리키는 것은 아니라고 명시하고 있다. 진짜 모호하긴 하지만 말 그래도 시간될때 백그라운드에 있는 앱에서 웹상의 컨텐츠를 가져올수 있다는 점이 핵심인것 같다. 말하고 싶은것은 절대. 타이머가 아니라는 점. </span>

<div class="txc-textbox" style="border: 1px solid #cbcbcb; background-color: #ffffff; padding: 10px;"><span style="font-size: 11pt;">**fetch 관련 링크 **</span>

<span style="line-height: 2; font-size: 11pt;">– </span><span style="background-color: transparent; font-size: 15px; line-height: 29px;">[http://www.xcubelabs.com/blog/ios-7-background-execution-and-multitasking/](http://www.xcubelabs.com/blog/ios-7-background-execution-and-multitasking/)</span>

<span style="line-height: 2; font-size: 11pt;">– </span><span style="background-color: transparent; font-size: 15px; line-height: 29px;">[http://www.raywenderlich.com/29948/backgrounding-for-ios](http://www.raywenderlich.com/29948/backgrounding-for-ios)</span>

</div><span style="font-size: 11pt;"> </span>

<span style="font-size: 11pt;">**[backgroundExpirationHandler관련] **</span>

<span style="font-size: 11pt;"> 그래두 자꾸 죽어서 Organizer 에서 죽을때 마다 시간과 로그를 확인을 했고 crash 로그가 떨어지는 것을 확인했다. 아래와 같은 문제인데:</span>

<span style="font-size: 11pt;"> </span>

<script src="https://gist.github.com/AhnSeongHyun/6895592.js"></script>

<span style="font-size: 11pt;"> </span>

<span style="background-color: transparent; font-size: 11pt; line-height: 2;">이 문제는 유효한 시간에 대한 백그라운드 작업에서의 시간 초과에 대한 문제다. 백그라운드에서 존재하는 시간을 늘리기 위해서 아무것도 하지 않는 핸들러를 작성해 놓은 코드(내가 만든게 아님을 분명히 밝힌다.)가 있었는데 이 부분이 문제가 생기는 것을 확인하였고 해당 부분을 제거하였다. 이유는 사실 이 부분은 iOS 에서 사용자가 어떤 다운로드 작업을 하다가 백그라운드로 갔을때 여분의 시간을 주고 해당 작업을 끝마치기 위해서 존재하는 것인데 내가 백그라운드를 유지해야하는 이유와는 상충이 되고 몇시간 이상을 유지해야하는데 고작 몇분을 위해서 필요하지는 않다고 생각했다., </span>

</div><div style="text-align: justify; line-height: 2;"><bkprocessassertion:0x1d569690]]><bkprocessassertion:0x1d56abb0]]><bkprocessassertion:0x1d56b580]]></div><div style="text-align: justify; line-height: 2;"><bkprocessassertion:0x1d569690]]><bkprocessassertion:0x1d56abb0]]><bkprocessassertion:0x1d56b580]]><span style="font-size: 11pt;">**[앱은 결국 죽는다.]  
**</span></div><div style="text-align: justify; line-height: 2;"><bkprocessassertion:0x1d569690]]><bkprocessassertion:0x1d56abb0]]><bkprocessassertion:0x1d56b580]]></div><div style="text-align: justify; line-height: 2;"><bkprocessassertion:0x1d569690]]><bkprocessassertion:0x1d56abb0]]><bkprocessassertion:0x1d56b580]]><span style="font-size: 11pt;">위의 핸들러를 삭제하니 조금은 백그라운드에서 죽는것, 정확히는 crash가 떨어지는 것이 없어지게 되었는데도 불구하고 죽는 현상이 발생이 되었고 콘솔로그쪽을 확인해 보니 아래와 같은 로그들이 발생이 되었다. </span></div><div style="text-align: justify; line-height: 2;"><bkprocessassertion:0x1d569690]]><bkprocessassertion:0x1d56abb0]]><bkprocessassertion:0x1d56b580]]></div><div class="txc-textbox" style="border: 1px solid #cbcbcb; background-color: #ffffff; padding: 10px;"><div style="text-align: left; line-height: 2;"><span style="font-size: 14px; line-height: normal; font-family: 'Nanum Gothic';">Oct  5 16:23:07  backboardd[28] <Warning>: Application ‘UIKitApplication:com.gx.uxart[0x57b0]’ exited abnormally with signal 9: Killed: 9</span>  
<span style="font-size: 14px; line-height: normal; font-family: 'Nanum Gothic';"> </span>  
<span style="font-size: 14px; line-height: normal; font-family: 'Nanum Gothic';">Oct  5 16:23:07  backboardd[28] <Warning>: Application ‘UIKitApplication:com.nike.nikeplus-gps[0xf40f]’ exited abnormally with signal 9: Killed: 9</span></div></div><div style="text-align: justify; line-height: 2;"><bkprocessassertion:0x1d569690]]><bkprocessassertion:0x1d56abb0]]><bkprocessassertion:0x1d56b580]]><span style="font-size: 11pt;">  
</span></div><div style="text-align: justify; line-height: 2;"><bkprocessassertion:0x1d569690]]><bkprocessassertion:0x1d56abb0]]><bkprocessassertion:0x1d56b580]]><span style="font-size: 11pt;">kill 9은 다들 아시겠지만 유닉스에서 프로세스를 강제로 죽이는 명령어이고 내가 만든앱 말고도 다른 상용앱들이 죽임을 당하는 것을 확인하였다. 여러 사이트에 물어봤지만 iOS에 의해서 죽임을 당하는 것은 막을 수가 없다. iOS는 무조건 포그라운드앱 위주로 돌아간다. 사실 그게 합리적인것이 포그라운드는 사용자가 지금 사용하고 있는것이기 때문인데, 포그라운드 앱이 메모리가 부족할때 백그라운드앱들을 강제로 죽이면서 메모리 공간을 확보한다. 정확히 어떤 기준에 의해서 앱을 죽이는 지는 모르겠다. </span></div><div style="text-align: justify; line-height: 2;"><bkprocessassertion:0x1d569690]]><bkprocessassertion:0x1d56abb0]]><bkprocessassertion:0x1d56b580]]></div><div style="text-align: justify; line-height: 2;"><bkprocessassertion:0x1d569690]]><bkprocessassertion:0x1d56abb0]]><bkprocessassertion:0x1d56b580]]></div><div style="text-align: justify; line-height: 2;"><bkprocessassertion:0x1d569690]]><bkprocessassertion:0x1d56abb0]]><bkprocessassertion:0x1d56b580]]><span style="font-size: 11pt;">**[Analyze 하자.] **</span></div><div style="text-align: justify; line-height: 2;"><bkprocessassertion:0x1d569690]]><bkprocessassertion:0x1d56abb0]]><bkprocessassertion:0x1d56b580]]></div><div style="text-align: justify; line-height: 2;"><bkprocessassertion:0x1d569690]]><bkprocessassertion:0x1d56abb0]]><bkprocessassertion:0x1d56b580]]><span style="font-size: 11pt;">메모리 부족에 의해서 죽는것은 어쩔수 없지만 그래도 메모리가 적으면 아무래도 덜 죽임을 당할것이라는 예상에 Analyze 를 수행하였다. ARC 를 사용함에도 Analyze를 수행했을때 leak 에 대한 부분이 나오는데 사실 이 부분은 좀더 공부를 해야하는 부분이다. ARC 를 사용한다고 해서 가비지 컬렉션이라고 생각하는 분들이 있는데(나도 그랬고.) 다르다고 한다. 정확히는 모르겠지만 필자의 경우에는 블루투스 연결이나 AddressBook 에서 주소를 가져오는 부분 ARC를 사용함에도 불구하고 CFRelease를 사용해야한다고 분석결과가 나왔다. 이 부분은 뭐라고 설명할수는 없지만(공부해야하는 부분), Analyze를 돌리고 Instrument로 leak과 Allocation을 체크해 보는 것이 좋을 것 같다.</span></div><div style="text-align: justify; line-height: 2;"><bkprocessassertion:0x1d569690]]><bkprocessassertion:0x1d56abb0]]><bkprocessassertion:0x1d56b580]]></div><div style="text-align: justify; line-height: 2;"><bkprocessassertion:0x1d569690]]><bkprocessassertion:0x1d56abb0]]><bkprocessassertion:0x1d56b580]]><span style="font-size: 11pt;">  
</span></div><div style="text-align: justify; line-height: 2;"><bkprocessassertion:0x1d569690]]><bkprocessassertion:0x1d56abb0]]><bkprocessassertion:0x1d56b580]]><span style="font-size: 11pt;">**[다시원점, 블루투스 연결만으로 백그라운드는 문제 없다.]  
**</span></div><div style="text-align: justify; line-height: 2;"><bkprocessassertion:0x1d569690]]><bkprocessassertion:0x1d56abb0]]><bkprocessassertion:0x1d56b580]]></div><div style="text-align: justify; line-height: 2;"><bkprocessassertion:0x1d569690]]><bkprocessassertion:0x1d56abb0]]><bkprocessassertion:0x1d56b580]]><span style="font-size: 11pt;">다시 원점으로 돌아왔고 Background 관련 레퍼런스와 다양한 커뮤니티에 물어본 결과는 블루투스 연결된 상태만으로(백그라운드모드에서 블루투스 관련 지정시) 백그라운드 앱이 유지된다는 사실이다. 멀리 돌아오긴 했지만 백그라운드와 앱의 로그 및 상태에 대해서 자세히 알수 있는 여정(?) 이었다. </span> </div><div style="text-align: justify; line-height: 2;"><bkprocessassertion:0x1d569690]]><bkprocessassertion:0x1d56abb0]]><bkprocessassertion:0x1d56b580]]><span style="font-size: 11pt;">결론적으로 iOS 에서 어떤 앱을 만들때는 무조건 죽을수 있다는 가정하에 만들어야 한다는 것이다. 방어할수 있는 방법이 없기 떄문에, 앱의 정책을 백그라운드에 죽고 살고 했을때, 어떻게 보여지고 내부적으로 연결작업을 한다던가 하는 등의 정해야 하는 것이다. 또 다른 하고 싶은 말은 안드로이드와는 다르다는 것이다. 아이폰, iOS의 특성을 잘 이해해야 하는데 기존의 윈도우나 안드로이드에서 작업했던 기억을 가지고 작업을 하거나 기획을 하면 문제가 크게 생길수가 있다. iOS는 기본적으로 앱들이 SandBox 정책을 가진다는 개념하에 접근을 해야하고 그 안에서 어떻게 원하는 서비스를 제공할것인가를 고민해야 한다.</span></div><div style="text-align: justify;"><span style="font-size: 15px; line-height: 29px;"> </span></div><div style="text-align: justify;"><span style="font-size: 15px; line-height: 29px;">**<span style="font-size: 10pt;">Reference</span>**</span>

<span style="font-size: 15px; line-height: 29px;"><span style="font-size: 10pt;">– </span>[<span style="font-size: 10pt;">iOS Multitasking & Background Reference</span>](https://developer.apple.com/library/ios/documentation/iphone/conceptual/iphoneosprogrammingguide/ManagingYourApplicationsFlow/ManagingYourApplicationsFlow.html)</span>

<span style="font-size: 15px; line-height: 29px;"><span style="font-size: 10pt;">– </span>[<span style="font-size: 10pt;">[OSXDev] 백그라운드 앱 킬 관련 </span>](http://osxdev.org/forum/index.php?threads/%EC%A7%88%EB%AC%B8-%EB%B0%B1%EA%B7%B8%EB%9D%BC%EC%9A%B4%EB%93%9C-%EC%95%B1-kill-%EA%B4%80%EB%A0%A8.272/)</span>

 

</div>

