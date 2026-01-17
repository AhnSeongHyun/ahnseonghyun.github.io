---
title: '[iOS] HTML 파싱 - Java Script 와 UIWebView 이용하기'
author: 'ash84'
pub_date: '2011-05-08'
description: 'HTML 파싱에 관한 부분은 한우찾기 1.0 및 2.0 에 걸쳐서 가장 핵심적인 부분이라고 할 수 있다. 총 2'
featured_image: ''
tags: ['HTML Parsing', 'JavaScript', 'UIWebView', 'dev', 'iOS', 'java', 'parsing', '한우찾기']
---
<div style="background-color: transparent; text-align: justify; line-height: 2; "><span style="font-family: Dotum; font-size: 11pt; "><span style="color: rgb(0, 0, 0); ">HTML 파싱에 관한 부분은 한우찾기 1.0 및 2.0 에 걸쳐서 가장 핵심적인 부분이라고 할 수 있</span><span style="color: rgb(0, 0, 0); ">다. 총 2</span><span style="color: rgb(0, 0, 0); ">가지 방법을 사용해서 웹 사이트에 있는 HTML 데이터를 파싱해서 가져오고 있</span><span style="color: rgb(0, 0, 0); ">다. (2.4버전 이후에는 HTMLParser 를 사용할 예정)</span></span></div><span style="color: rgb(0, 0, 0); ">  
</span>

<div style="background-color: transparent; line-height: 2; "><span style="color: rgb(0, 0, 0); ">  
</span></div><span style="color: rgb(0, 0, 0); ">  
</span>

<div style="background-color: transparent; text-align: justify; line-height: 2; "><span style="color: rgb(0, 0, 0); ">  
</span>  
<span style="color: rgb(0, 0, 0); ">  
</span></div><span style="color: rgb(0, 0, 0); ">  
</span>

<div style="background-color: transparent; line-height: 2; "><span style="color: rgb(0, 0, 0); ">  
</span></div><span style="color: rgb(0, 0, 0); ">  
</span>

<div style="background-color: transparent; text-align: justify; line-height: 2; "><span style="color: rgb(0, 0, 0); ">  
</span><span style="font-family: Dotum; color: rgb(0, 0, 0); ">  
</span></div><span style="color: rgb(0, 0, 0); ">  
</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); padding: 10px; line-height: 2; "><span style="color: rgb(0, 0, 0); ">  
</span><span style="color: rgb(0, 0, 0); ">  
</span>

<div style="text-align: justify; line-height: 2; "><span style="color: rgb(0, 0, 0); ">  
</span><span style="font-family: Dotum; background-color: rgb(92, 127, 176);"><font color="#ffffff"><span style="font-size: 11pt; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); "><span style="color: rgb(0, 0, 0); ">1. Java Script + UIWebView 를 이용하는 방식</span></span></font></span></div><div style="background-color: rgb(255, 255, 255); text-align: justify; line-height: 2; "><span style="font-size: 11pt; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); ">  
</span></div><span style="font-size: 11pt; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); ">  
</span>

<div style="background-color: rgb(255, 255, 255); line-height: 2; "><span style="font-size: 11pt; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); ">  
</span></div><span style="font-size: 11pt; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); ">  
</span>

<div style="background-color: rgb(255, 255, 255); text-align: justify; line-height: 2; "><span style="font-size: 11pt; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); ">  
</span><span style="font-family: Dotum; font-size: 11pt; "><span style="background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); ">  
 2. TFHpple(xpath)</span><span style="background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); "> 를 이용하는 방식</span></span></div><div style="background-color: rgb(255, 255, 255); text-align: justify; line-height: 2; "><span style="font-family: Dotum; font-size: 11pt; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); ">3. HTMLParser 를 이용하는 방식 </span></div></div><span style="color: rgb(0, 0, 0); ">  
</span>

<div style="background-color: transparent; line-height: 2; "><span style="color: rgb(0, 0, 0); ">  
</span></div><span style="color: rgb(0, 0, 0); ">  
</span>

<div style="background-color: transparent; text-align: justify; line-height: 2; "><span style="font-family: Dotum; font-size: 11pt; background-color: transparent; line-height: 2; ">  
</span></div><div style="background-color: transparent; text-align: justify; line-height: 2; "><span style="font-family: Dotum; font-size: 11pt; background-color: transparent; line-height: 2; "><span style="color: rgb(0, 0, 0); ">각각의 방식이 장단점이 있기 때문에 하나씩 살펴보도록 하겠다. </span><span style="color: rgb(0, 0, 0); ">일단 이번 포스팅에서는 첫번째, 즉 Java Script 와 UIWebView 를 이용해서 개발하는 부분을 보도록 하자.</span></span></div><span style="font-size: 11pt; color: rgb(0, 0, 0); ">  
</span>

<div style="background-color: transparent; line-height: 2; "><span style="font-size: 11pt; color: rgb(0, 0, 0); ">  
</span></div><span style="font-size: 11pt; color: rgb(0, 0, 0); ">  
</span>

<div style="background-color: transparent; text-align: justify; line-height: 2; "><span style="font-size: 11pt; color: rgb(0, 0, 0); ">  
</span>  
<span style="font-size: 11pt; color: rgb(0, 0, 0); ">  
</span></div><span style="font-size: 11pt; color: rgb(0, 0, 0); ">  
</span>

<div style="background-color: transparent; line-height: 2; "><span style="font-size: 11pt; color: rgb(0, 0, 0); ">  
</span></div><span style="font-size: 11pt; color: rgb(0, 0, 0); ">  
</span>

<div style="text-align: justify; line-height: 2; ">**<span style="font-size: 11pt; color: rgb(0, 0, 0); ">  
</span><span style="font-family: Dotum; background-color: rgb(87, 111, 189);"><font color="#ffffff"><span style="font-size: 11pt; color: rgb(0, 0, 0); ">  
</span><span style="font-size: 14pt; "><span style="font-size: 11pt; "><span style="font-size: 10pt; "><span style="font-size: 14pt; "><span style="font-size: 11pt; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); ">자바스크립트로 파싱을 한다?</span></span></span></span></span></font></span>**</div><span style="font-size: 11pt; color: rgb(0, 0, 0); ">  
</span>

<div style="background-color: transparent; line-height: 2; "><span style="font-size: 11pt; color: rgb(0, 0, 0); ">  
</span></div><span style="font-size: 11pt; color: rgb(0, 0, 0); ">  
</span>

<div style="background-color: transparent; text-align: left; line-height: 2; "><span style="font-size: 11pt; color: rgb(0, 0, 0); ">  
</span>  
<span style="font-size: 11pt; color: rgb(0, 0, 0); ">  
</span></div><span style="font-size: 11pt; color: rgb(0, 0, 0); ">  
</span>

<div style="background-color: transparent; line-height: 2; text-align: left; "><span style="font-size: 11pt; color: rgb(0, 0, 0); ">  
</span></div><span style="font-size: 11pt; color: rgb(0, 0, 0); ">  
</span>

<div style="background-color: transparent; text-align: left; line-height: 2; "><span style="font-size: 11pt; color: rgb(0, 0, 0); ">  
</span><span style="font-family: Dotum; "><span style="font-size: 11pt; "><span style="color: rgb(0, 0, 0); ">  
 HTML 로 파싱을 하기 위해서 어떻게 해야할까? 라는 고민을 처음 하게 되었는데,</span><span style="color: rgb(0, 0, 0); "></span></span><font color="#e31600"><span style="font-size: 11pt; color: rgb(0, 0, 0); ">첫번째로 방법이 바로 UIWebView 에 해당 HTML 을 불러와서 UIWebView의 다음의</span></font></span><font color="#e31600" style="background-color: transparent; line-height: 2; font-family: Dotum; "><span style="font-size: 11pt; color: rgb(0, 0, 0); "> 함수를 이용해서 처리하는 것</span></font><span style="background-color: transparent; font-family: Dotum; font-size: 11pt; "><span style="color: rgb(0, 0, 0); "></span><span style="color: rgb(0, 0, 0); ">이었다. </span></span><span style="background-color: transparent; color: rgb(0, 0, 0); font-family: Dotum; font-size: 15px; line-height: 29px; text-align: justify; ">해당함수에 대해서 찾아보면 다음과 같이 나온다. </span></div><div style="background-color: transparent; line-height: 2; "></div><div style="background-color: transparent; text-align: justify; line-height: 2; "></div><div style="background-color: transparent; line-height: 2; "></div><div style="background-color: transparent; text-align: justify; line-height: 2; "></div><div style="background-color: transparent; line-height: 2; "></div><div class="txc-textbox" style="border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-top-color: rgb(203, 203, 203); border-right-color: rgb(203, 203, 203); border-bottom-color: rgb(203, 203, 203); border-left-color: rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; line-height: 2; "><div style="text-align: justify;"><span style="color: rgb(62, 31, 124); font-family: Menlo; font-size: 19px; line-height: normal; "><span style="font-family: Dotum; "><span style="font-size: 9pt; ">stringByEvaluatingJavaScriptFromString:</span></span></span></div><span style="font-size: 9pt; ">  
</span>

<span style="font-family: Dotum; font-size: 9pt; ">Returns the result of running a script.</span>

<span style="font-size: 9pt; ">  
</span>

<span style="font-family: Dotum; font-size: 9pt; ">– (</span>[<span class="s1"><span style="font-family: Dotum; font-size: 9pt; ">NSString</span></span>](file:///Library/Developer/Documentation/DocSets/com.apple.adc.documentation.AppleiOS4_3.iOSLibrary.docset/Contents/Resources/Documents/documentation/Cocoa/Reference/Foundation/Classes/NSString_Class/Reference/NSString.html#//apple_ref/doc/c_ref/NSString)<span style="font-family: Dotum; font-size: 9pt; "> *)stringByEvaluatingJavaScriptFromString:(</span>[<span class="s1"><span style="font-family: Dotum; font-size: 9pt; ">NSString</span></span>](file:///Library/Developer/Documentation/DocSets/com.apple.adc.documentation.AppleiOS4_3.iOSLibrary.docset/Contents/Resources/Documents/documentation/Cocoa/Reference/Foundation/Classes/NSString_Class/Reference/NSString.html#//apple_ref/doc/c_ref/NSString)<span style="font-family: Dotum; font-size: 9pt; "> *)</span><span class="s2"><span style="font-family: Dotum; font-size: 9pt; ">script</span></span>

<span style="font-size: 9pt; ">  
</span>

<span style="font-family: Dotum; font-size: 9pt; ">Parameters</span>

<span style="font-size: 9pt; ">  
</span>

<span style="font-family: Dotum; font-size: 9pt; ">script</span>

<span style="font-size: 9pt; ">  
</span>

<span style="font-family: Dotum; font-size: 9pt; ">The script to run.</span>

<span style="font-size: 9pt; ">  
</span>

<span style="font-family: Dotum; font-size: 9pt; ">Return Value</span>

<span style="font-size: 9pt; ">  
</span>

<span style="font-family: Dotum; font-size: 9pt; ">The result of running script or </span><span class="s3"><span style="font-family: Dotum; font-size: 9pt; ">nil</span></span><span style="font-family: Dotum; font-size: 9pt; "> if it fails. </span>

</div><div style="background-color: transparent; line-height: 2; "></div><div style="background-color: transparent; line-height: 2; "><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"></meta><meta content="text/css" http-equiv="Content-Style-Type"></meta><title></title><meta content="Cocoa HTML Writer" name="Generator"></meta><meta content="1038.35" name="CocoaVersion"></meta>  
<style type="text/css"><span style="font-family: Dotum; ">
p.p1 {margin: 0.0px 0.0px 0.0px 0.0px; font: 11.0px Menlo; color: #3e1f7c}
</style></div><div style="background-color: transparent; text-align: justify; line-height: 2; ">  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="background-color: transparent; text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-family: Dotum; font-size: 11pt; ">파라미터로 자바스크립트를 받고 리턴 값으로 해당 결과 혹은 실패일 경우에는 nil 값을 전달해 주도록 되어있다. 즉, 이 함수를 통해서 html 에 있는 특정 값을 가져오기 위해서는 자바 스크립트가 필요하다. 자바 스크립트를 조금 공부하셔야 하는게 있긴 한데 일단 사용했던 소스를 보면 다음과 같다. </span></div><span style="font-size: 11pt; ">  
</span>

<div style="background-color: transparent; line-height: 2; "><span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="background-color: transparent; text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="background-color: transparent; text-align: justify; line-height: 2; "><span style="font-size: 11pt; ">  
</span><span style="font-family: Dotum; font-size: 11pt; ">먼저 해당 파싱 대상의 HTML사이트의 소스를 봐야 한다. </span></div><div style="background-color: transparent; text-align: justify; line-height: 2; "><span style="font-family: Dotum; font-size: 11pt; ">  
</span></div><div style="background-color: transparent; text-align: justify; line-height: 2; "><span style="font-family: Dotum; font-size: 11pt; ">  
</span></div><script src="https://gist.github.com/3765542.js"></script>

<div style="background-color: transparent; line-height: 2; "></div><div style="background-color: transparent; text-align: justify; line-height: 2; "></div><span style="color: rgb(0, 0, 0); ">  
</span>

<div style="background-color: transparent; text-align: justify; line-height: 2; "><span style="color: rgb(0, 0, 0); ">  
</span><span style="font-family: Dotum; "><span style="font-size: 11pt; color: rgb(0, 0, 0); ">위의 HTML은 실제 페이지의 일부분이다. 가져오려고 하는 데이터는 </span>**<span style="font-size: 11pt; color: rgb(0, 0, 0); ">2007-11-24</span>**<span style="font-size: 11pt; color: rgb(0, 0, 0); "> 라고 가정했을때 다음과 같은 자바스크립트를 구성 할 수 있다. </span>  
</span></div><div style="background-color: transparent; text-align: justify; line-height: 2; "><span style="font-family: Dotum; ">  
</span></div><div style="background-color: transparent; text-align: justify; line-height: 2; "><span style="font-family: Dotum; ">  
</span></div><script src="https://gist.github.com/3765549.js"></script>

<div style="text-align: justify; line-height: 2; "><span style="font-size: 13px; color: rgb(0, 0, 0); "><span style="font-family: Dotum; "><span style="font-family: Dotum; font-size: 11pt; ">  
</span></span></span></div><div style="text-align: justify; line-height: 2; "><span style="font-size: 13px; color: rgb(0, 0, 0); "><span style="font-family: Dotum; "><span style="font-family: Dotum; font-size: 11pt; ">간단히 말하자면 ‘id가 lblBirthDate 라고 있는 곳의 innerHTML 을 가져와라’. 그럼 이 자바스크립트는 전체 HTML 문서의 id 중에서 lblBirthData 부분을 찾</span></span><span style="font-family: Dotum; font-size: 11pt; ">고, 그 태그 안에 있는 2007-11-24를 반환하게 되는 것이다. 다음의 Objective-C 코드를 보면 더 이해가 쉽게 될 것이다.</span></span></div><div style="text-align: justify; line-height: 2; "><span style="font-size: 13px; color: rgb(0, 0, 0); "><span style="font-family: Dotum; font-size: 11pt; "> </span></span></div><script src="https://gist.github.com/3765555.js"></script>

<div style="background-color: transparent; text-align: justify; "><font size="2" style="line-height: 2; "><span style="font-family: Dotum; "><font color="#3058d2"><span style="color: rgb(0, 0, 0); font-size: 11pt; ">  
</span></font></span></font></div><div style="background-color: transparent; text-align: justify; "><font size="2" style="line-height: 2; "><span style="font-family: Dotum; "><font color="#3058d2"><span style="color: rgb(0, 0, 0); font-size: 11pt; ">매우 간단하다. webView란, UIWebView의 인스턴스이고 거기에서 위에서 언급한 함수의 파라미터에 자바스크립트를 넣어주고 그럼, webView가 해당 자바스크립트를 실행 시켜서 데이터를 가져오는 것이다. 즉, 웹 브라우저가 자바스크립트를 실행 시켜서 데이터를 가져온다고 볼 수 있다. </span></font></span></font></div><font size="2" style="line-height: 2; "><span style="color: rgb(0, 0, 0); ">  
</span><div style="background-color: transparent; text-align: justify; "></div><div style="background-color: transparent; text-align: justify; "><span style="font-family: Dotum; font-size: 11pt; color: rgb(0, 0, 0); ">일단 이 방식을 사용할때의 가장 큰 걸림돌이 여러가지가 있다. </span></div><div style="background-color: transparent; text-align: justify; "></div><div style="background-color: transparent; text-align: justify; "><span style="font-family: Dotum; ">****</span></div><div class="txc-textbox" style="border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-top-color: rgb(203, 203, 203); border-right-color: rgb(203, 203, 203); border-bottom-color: rgb(203, 203, 203); border-left-color: rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; "><div style="background-color: transparent; text-align: justify; "><span style="font-family: Dotum; ">**<span style="font-size: 11pt; ">첫번째, 과연 자바스크립트를 쓸 수가 있는가?</span>**</span></div><span style="font-size: 11pt; ">  
</span>

<div style="background-color: transparent; text-align: justify; "><span style="font-size: 11pt; ">  
</span>  
<span style="font-size: 11pt; ">  
</span></div><span style="font-size: 11pt; ">  
</span>

<div style="background-color: transparent; text-align: justify; "><span style="font-family: Dotum; "><span style="font-size: 10pt; ">자바스크립트가 처음이라 조금 고생했지만, 아시는 분이라면 getElementById 라는 것을 통해서 전체 html 문서 내 지정한 id를 찾는것을 기반으로 한다는것을 알 수 있을 것이다. 그런데 </span><u><font color="#c8056a"><span style="font-size: 10pt; ">문제는 간혹 html 페이지 자체가 전혀 id 를 쓰지 않은채 제작된 html 페이지도 있다는 것</span></font></u><span style="font-size: 10pt; ">입니다. 그럴 경우에는 이 방법을 사용 할 수 없다. </span></span></div><div style="background-color: transparent; text-align: justify; "></div><div style="background-color: transparent; text-align: justify; "><span style="font-family: Dotum; ">**<span style="font-size: 11pt; ">두번째, 이게 최선 입니까?</span>**</span></div><div style="background-color: transparent; text-align: justify; "></div><div style="background-color: transparent; text-align: justify; "><span style="font-family: Dotum; ">한우 찾기 2.0 을 실행해 보면 처음 12자리를 입력하고 들어가는 부분에서는 로딩뷰가 뜨는것을 확인 할 수가 있다. 사실상 로딩뷰는 위의 UIWebView가 파싱 하려는 사이트를 로딩시작할때 시작하고 끝나면 끝나게 되어 있습니다. 그렇기 때문에 <u><font color="#c8056a">사실상 찾으려는 텍스트 데이터 임에도 불구하고 html 페이지 자체에 이미지가 있는 경우에는 UIWebView에서 해당 이미지를 로딩해야 하기 때문에 속도적인 부분에서 오래 걸릴수가 있다.</font></u> </span></div></div><div style="background-color: transparent; text-align: justify; "></div><div style="background-color: transparent; text-align: justify; "></div><div style="text-align: justify; "></div><div style="text-align: justify; "><span style="color: rgb(0, 0, 0); font-size: 11pt; ">정리하자면..</span></div><div style="background-color: transparent; text-align: justify; ">  
<span style="color: rgb(0, 0, 0); ">  
</span></div><span style="color: rgb(0, 0, 0); ">  
</span>

<div style="background-color: transparent; text-align: justify; "><span style="color: rgb(0, 0, 0); ">  
</span></div><span style="color: rgb(0, 0, 0); ">  
</span>

<div class="txc-textbox" style="border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-top-color: rgb(203, 203, 203); border-right-color: rgb(203, 203, 203); border-bottom-color: rgb(203, 203, 203); border-left-color: rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; "><span style="color: rgb(0, 0, 0); ">  
</span><span style="color: rgb(0, 0, 0); ">  
</span>

<div style="background-color: transparent; text-align: justify; "><span style="color: rgb(0, 0, 0); ">  
</span><span style="font-family: Dotum; font-size: 11pt; color: rgb(0, 0, 0); ">자바스크립트를 사용할 경우에는 반드시, HTML 페이지 소스에서 id가 있는지 확인하자. </span></div><span style="font-size: 11pt; color: rgb(0, 0, 0); ">  
</span>

<div style="background-color: transparent; text-align: justify; "><span style="font-size: 11pt; color: rgb(0, 0, 0); ">  
</span><span style="font-family: Dotum; font-size: 11pt; color: rgb(0, 0, 0); ">한번쯤 프로토타입을 만들어서 시간을 측정해보고 적용하길 바란다. </span></div></div><span style="color: rgb(0, 0, 0); ">  
</span>

<div style="background-color: transparent; text-align: justify; "><span style="color: rgb(0, 0, 0); ">  
</span>  
<span style="color: rgb(0, 0, 0); ">  
</span></div><span style="color: rgb(0, 0, 0); ">  
</span>

<div style="background-color: transparent; text-align: justify; "><span style="color: rgb(0, 0, 0); ">  
</span><span style="font-family: Dotum; "><span style="color: rgb(0, 0, 0); font-size: 11pt; ">다음 포스팅에서는</span>**<span style="color: rgb(0, 0, 0); "><span style="font-size: 11pt; "></span><span style="font-size: 11pt; ">XPath를 이용한 방법 과 HTMLParser 이용한 방법 </span></span>**<span style="color: rgb(0, 0, 0); font-size: 11pt; ">에 대해서 다루도록 하겠다. </span></span></div><span style="color: rgb(0, 0, 0); ">  
</span>

<div style="background-color: transparent; text-align: justify; "><span style="color: rgb(0, 0, 0); ">  
</span>  
<span style="color: rgb(0, 0, 0); ">  
</span></div><span style="color: rgb(0, 0, 0); ">  
</span>

<div style="background-color: transparent; text-align: justify; "><span style="color: rgb(0, 0, 0); ">  
</span><span style="font-family: Dotum; color: rgb(0, 0, 0); "> </span></div></font>



