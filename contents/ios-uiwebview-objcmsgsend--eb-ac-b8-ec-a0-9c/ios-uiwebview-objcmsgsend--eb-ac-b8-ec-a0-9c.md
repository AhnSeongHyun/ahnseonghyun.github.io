---
title: '(iOS) UIWebView objc_msg_send 문제'
author: 'ash84'
pub_date: '2013-02-19'
description: '한우찾기 앱을 만들때에도 이렇게 힘들지는 않았는데, 풍문검색은 좀 어렵네. 아무튼 업로드 및 빠른 심사를 부탁해 놓은 상황인데, 어제 crash가 났던 상황에 대해서 정리하고자 포스팅을 한다. 일단 상황을 설명하자면 단순하게 UITableView 의 한 셀을 선택하면 그 셀이 가지고 있는 링크주소를 내가 만든 BasicUIWebViewController 에서 보여주는 것이었는데, 보여주고나서 viewController를 내리면(dismiss) 문제가 생기는 것이었다.'
featured_image: ''
tags: ['dev', 'objc_msg_send', 'UIWebView', 'UIWebViewDelegate crash']
---


<span style="font-size: 11pt;">한우찾기 앱을 만들때에도 이렇게 힘들지는 않았는데, 풍문검색은 좀 어렵네. 아무튼 업로드 및 빠른 심사를 부탁해 놓은 상황인데, 어제 crash가 났던 상황에 대해서 정리하고자 포스팅을 한다. 일단 상황을 설명하자면 단순하게 UITableView 의 한 셀을 선택하면 그 셀이 가지고 있는 링크주소를 내가 만든 BasicUIWebViewController 에서 보여주는 것이었는데, 보여주고나서 viewController를 내리면(dismiss) 문제가 생기는 것이었다. </span>

<span style="font-size: 11pt;">메시지는 단순하게 아래와 같은 메시지가 나온다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">objc_msg_send </span>

</div><span style="font-size: 11pt;">NSZombieEnabled 옵션을 켜서 좀더 상세한 메시지를 확인해 보았다. XCode4.0 에서 NSZombieEnabled  옵션은 아래와 같이 설정해 주면 된다. XCode 메뉴 [Product]=>[Edit Scheme] 를 눌러서 설정을 시작하면 된다. </span>

<span style="font-size: 11pt;">  
</span>

![](http://ash84.net/wp-content/uploads/1/cfile29.uf.1769AE505120B9020624E5.png)

<span style="font-size: 11pt;">  
</span>

![](http://ash84.net/wp-content/uploads/1/cfile30.uf.2466374D5120B9231188E7.png)

<span style="font-size: 11pt;">  
</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt; line-height:2; font-weight: bold;"><span style="font-size: 10pt;">[WebViewController respondsToSelector:]: message sent to deallocated instance 0x7295100</span></span>

</div>**  
**

<span style="font-size: 11pt;">발번역을 해보자면, 메시지가 이미 메모리 해제된 instance 에게 전해져서 문제라는 일이다. 내 생각엔 close 버튼을 누르면 ViewController가 내려가고 해제가 되었는데, webViewDelegate에 대한 메시지가 그 이후에 받게 되어서 문제가 생기는 듯한데.. 검색을 해보니 아래의 링크를 찾게 되었다.** **</span>

**  
**

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 10pt;">[http://stackoverflow.com/questions/8995146/frustrating-uiwebview-delegate-crash-issue](http://stackoverflow.com/questions/8995146/frustrating-uiwebview-delegate-crash-issue)</span>****

</div>**  
**

<span style="font-size: 9pt; line-height: 2;"><span style="font-size: 11pt;">예상한대로였다. 받아야 하는 webView instance가 없어서 생기는 문제이다. 위의 링크에서 처럼 close 버튼을 누르는 시점에 아래의 코드를 삽입하였다. </span></span>

**<span style="font-size: 11pt;">  
</span>**

**  
**

<span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;"></span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span class="s1" style="font-size: 11pt;">self</span><span style="font-size: 11pt;">.</span><span class="s2" style="font-size: 11pt;">webView</span><span style="font-size: 11pt;">.</span><span class="s3" style="font-size: 11pt;">delegate</span><span style="font-size: 11pt;"> = </span><span class="s1" style="font-size: 11pt;">nil</span><span style="font-size: 11pt;">;</span>

<span class="s1" style="font-size: 11pt;">self</span><span style="font-size: 11pt;">.</span><span class="s2" style="font-size: 11pt;">webView</span><span style="font-size: 11pt;"> = </span><span class="s1" style="font-size: 11pt;">nil</span><span style="font-size: 11pt;">;</span>

</div><span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">        </span>

<span style="font-size: 11pt; line-height: 2;">다행히 에러는 발생되지 않았다. 다른 컨트롤은 모르겠으나 UIWebView는 말 그대로 웹에 있는 컨텐츠를 가져오는 작업을 한다. 때문에 Delegate 역시 웹 서버에서 응답을 준 시점에 발동이 된다고 봐야 할것 같다. 그런 부분에서는 delegate를 명시적으로 끊어줘야 위와 같은 문제가 없을것 같다는 생각이 든다. </span>

<span style="font-size: 11pt; line-height: 2;">추가적으로 NSZombieEnabled 설정은 디폴트로 하고 작업을 하는것이 훨씬 편하다. VS, Eclipse, XCode 등의 다양한 툴을 많이 사용해 봤지만, VS가 디버깅 측면에서는 가장 낫지 않은가 싶다. 물론 다른 측면에서는 각각 다르겠지만 말이다. 좀더 빠른 디버깅을 위해서는 NSZombieEnabled 설정을 이용하자. </span>



