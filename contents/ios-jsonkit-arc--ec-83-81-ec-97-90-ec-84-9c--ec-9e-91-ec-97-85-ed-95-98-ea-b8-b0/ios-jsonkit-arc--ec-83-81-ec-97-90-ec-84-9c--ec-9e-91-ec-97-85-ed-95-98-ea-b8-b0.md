---
title: '(iOS) JSONKit ARC 상에서 작업하기'
author: 'ash84'
pub_date: '2015-09-24'
description: '다음 티스토리 API 연동중에 JSON 으로 연동하는 과정에서 JSONKit 라이브러리를 사용하고 있었는데 이 라이브러리는 아쉽게도 ARC로 작성되어 있지 않다. 하지만 JSONKit은 자기네들 말로는 Objective-C JSON 처리 라이브러리 중에서는 가장 빠르다고 하니 안 쓸수도 없는 노릇([성능평가자료](https://github.com/johnezang/JSONKit)).'
featured_image: ''
tags: ['Arc', 'dev', 'IOS', 'JSON', 'JSONKit', 'JSONKit ARC', 'objective-c jsonkit arc']
---


<span style="font-size: 11pt; line-height: 2;">다음 티스토리 API 연동중에 JSON 으로 연동하는 과정에서 JSONKit 라이브러리를 사용하고 있었는데 이 라이브러리는 아쉽게도 ARC로 작성되어 있지 않다. 하지만 JSONKit은 자기네들 말로는 Objective-C JSON 처리 라이브러리 중에서는 가장 빠르다고 하니 안 쓸수도 없는 노릇([성능평가자료](https://github.com/johnezang/JSONKit)). </span>

<span style="font-size: 11pt;">StackOverflow에도 나와 같은 의문을 가지신 분들이 많이 계시는 지라, 찾아보니 답이 있다. 사용하는 방법을 아래와 같이 스크린샷으로 남긴다. </span>

<span style="font-size: 11pt;">**1. 현재 프로젝트의 Target에 Build Phases에 들어간다. **</span>

<figure class="wp-caption aligncenter" style="width: 640px">![](http://ash84.net/wp-content/uploads/1/cfile5.uf.2307F73551921114185F56.png)<figcaption class="wp-caption-text">눌러서 보면 크게 보입니다. </figcaption></figure>

**  
**

<span style="font-size: 11pt;">**2. Build Phases 에서 Compile Source를 클릭해서 `JSONKit.m` 을 찾는다. **</span>

**  
**

**  
**

<span style="font-size: 11pt;">**3. JSONKit.m 을 더블클릭 후, `-fno-objc-arc` 입력.**</span>

<figure class="wp-caption aligncenter" style="width: 640px">![](http://ash84.net/wp-content/uploads/1/cfile28.uf.2550053B519212720CD3B2.png)<figcaption class="wp-caption-text">눌러서 보면 크게 보입니다. </figcaption></figure>

<span style="font-size: 11pt;">**4. 재 빌드(ReBuild) 하기. **</span>

<span style="font-size: 11pt;">그렇다면, `-fno-objc-arc` 는 무엇일까? 애는 무엇인데 ARC 환경에서 ARC가 아닌애들을 빌드되게 해줄까?</span>

<span style="font-size: 11pt;">이에 대한 대답역시 StackOverflow를 통해서 찾을수가 있었다. [아래의 답변](http://stackoverflow.com/a/11327940/807540)을 보자. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;">The `<code style="margin: 0px; padding: 1px 5px; border: 0px; font-size: 14px; vertical-align: baseline; background-color: rgb(238, 238, 238); font-family: Consolas, Menlo, Monaco, 'Lucida Console', 'Liberation Mono', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Courier New', monospace, serif; background-position: initial initial; background-repeat: initial initial;">-fno-objc-arc` flag is for the *compiler*, not for the *linker*. It tells the compiler that your Objective C code will be doing all the releasing and retaining manually. This is necessary because the newly added ARC mode [prohibits explicit use of `<code style="margin: 0px; padding: 1px 5px; border: 0px; font-size: 14px; vertical-align: baseline; background-color: rgb(238, 238, 238); font-family: Consolas, Menlo, Monaco, 'Lucida Console', 'Liberation Mono', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Courier New', monospace, serif; background-position: initial initial; background-repeat: initial initial;">retain`, `<code style="margin: 0px; padding: 1px 5px; border: 0px; font-size: 14px; vertical-align: baseline; background-color: rgb(238, 238, 238); font-family: Consolas, Menlo, Monaco, 'Lucida Console', 'Liberation Mono', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Courier New', monospace, serif; background-position: initial initial; background-repeat: initial initial;">release`, `<code style="margin: 0px; padding: 1px 5px; border: 0px; font-size: 14px; vertical-align: baseline; background-color: rgb(238, 238, 238); font-family: Consolas, Menlo, Monaco, 'Lucida Console', 'Liberation Mono', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Courier New', monospace, serif; background-position: initial initial; background-repeat: initial initial;">autorelease`, `<code style="margin: 0px; padding: 1px 5px; border: 0px; font-size: 14px; vertical-align: baseline; background-color: rgb(238, 238, 238); font-family: Consolas, Menlo, Monaco, 'Lucida Console', 'Liberation Mono', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Courier New', monospace, serif; background-position: initial initial; background-repeat: initial initial;">dealloc`, and so on](http://developer.apple.com/library/ios/#releasenotes/ObjectiveC/RN-TransitioningToARC/Introduction/Introduction.html); you cannot call them even through a selector.

Converting all your code to ARC may be a large task, so the compiler supports both the old and the new style of code. You must tell the compiler if the file you’re compiling is old or new; you do it by passing the `<code style="margin: 0px; padding: 1px 5px; border: 0px; font-size: 14px; vertical-align: baseline; background-color: rgb(238, 238, 238); font-family: Consolas, Menlo, Monaco, 'Lucida Console', 'Liberation Mono', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Courier New', monospace, serif; background-position: initial initial; background-repeat: initial initial;">-fno-objc-arc` flag.

There are many other compiler flags. They let you control the way the code is compiled and optimized, the way the errors and warnings are reported back to you, the paths where your headers are located, and so on. Type `<code style="margin: 0px; padding: 1px 5px; border: 0px; font-size: 14px; vertical-align: baseline; background-color: rgb(238, 238, 238); font-family: Consolas, Menlo, Monaco, 'Lucida Console', 'Liberation Mono', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Courier New', monospace, serif; background-position: initial initial; background-repeat: initial initial;">man gcc` in the terminal window to see the list of compiler options.

</div><span style="font-size: 11pt;"></span><span style="font-size: 11pt;"></span>

<span style="font-size: 11pt;">해석을 해보면, **위의 옵션은 링커(Linker)가 아닌 컴파일러(Compiler)에 대한 옵션이고 컴파일러에게 이 소스코드에 대해서는 수동적으로 `releasing/retaining` 을 수행하겠다고 지정하는 것이다.** ARC가 아닌 코드를 ARC 코드로 변환하려면 그것 자체로 많은 일이기 때문에 이런 옵션을 통해서 ARC와 ARC가 아닌것을 컴파일 할수 있다는 이야기이다. </span>

<span style="font-size: 11pt;">ARC로 본인코드라면 변경을 하는것도 좋지만, 너무 많은 코드라면 컴파일 옵션을 사용하는것이 좋을것 같기도 하다. 파일형태의 오픈 소스는 이렇게 해도 되는데, 정적라이브러</span><span style="font-size: 11pt;">리(.a) 는 어떻게 하는지도 좀 알아둬야 할것 같다. </span>



