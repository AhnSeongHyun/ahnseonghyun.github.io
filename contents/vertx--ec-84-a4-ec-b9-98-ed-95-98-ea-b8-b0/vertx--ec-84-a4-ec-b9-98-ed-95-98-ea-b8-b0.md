---
title: '(vert.x) 설치하기'
author: 'ash84'
pub_date: '2015-09-24'
description: '![](http://ash84.net/wp-content/uploads/1/cfile6.uf.2670863A5190979F07179B.PNG)

vert.x 홈페이지 : [http://vertx'
featured_image: ''
tags: ['vert.x', 'vert.x 설치', 'vertx', 'vertx install']
---


<div style="line-height: 2;"><span style="font-size: 11pt;">![](http://ash84.net/wp-content/uploads/1/cfile6.uf.2670863A5190979F07179B.PNG)

</span></div><div style="line-height: 2; text-align: center;"><span style="font-size: 11pt;">vert.x 홈페이지 : </span>[<span style="font-size: 11pt;">http://vertx.io</span>](http://vertx.io/)</div><div style="line-height: 2;"></div><span style="font-size: 11pt;">**  
**</span>

<span style="font-size: 11pt;">**  
**</span>

<span style="font-size: 11pt;">**사전 요구사항(pre-requisites)**</span>

<span style="font-size: 11pt;">– 운영체제 : 리눅스 계열, OSX, Windows</span>

<span style="font-size: 11pt;">– JDK1.7 이상 </span>

<span style="font-size: 11pt;">* Ruby 사용시, `JRUBY` 가 설치되어 있어야 하며 `JRUBY_HOME` 에 설치되고, 환경변수가 설정되어 있어야 한다. </span>

<span style="font-size: 11pt;">* 파이썬 사용시,`JYTHON` 이 설치되어 있어야 하녹 `JYTHON_HOME` 환경변수가 설정되어 있어야 한다. </span>

<span style="font-size: 11pt;">**설치하기 **</span>

<span style="font-size: 15px; line-height: 29px;">**[[vert.x 1.3.1 final.zip](http://vert-x.github.io/vertx-downloads/downloads/vert.x-1.3.1.final.zip.html)]**</span>

<span style="font-size: 11pt;">1. 압축을 풀고, 배포판을 원하는 곳에 위치시킨다. </span>

<span style="font-size: 11pt;">2. vert.x bin 디렉토리를 `PATH` 에 추가한다. </span>

<span style="font-size: 11pt;">**설치 확인하기 **</span>

<span style="font-size: 11pt;">: 콘솔창에 아래와 같이 입력한다. 제대로  `PATH`가 설정되어 있다면, 버전정보를 볼 수 있다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">**> vertx version**</span>

</div><span style="font-size: 11pt;">*** 오류사항**</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px; line-height: 2;"><div><span style="color: rgb(0, 0, 0); font-family: Tahoma; line-height: normal; orphans: 2; text-align: -webkit-auto; widows: 2; font-size: 11pt;">C:\Users\AhnSeongHyun>vertx version</span>  
<span style="color: rgb(0, 0, 0); font-family: Tahoma; line-height: normal; orphans: 2; text-align: -webkit-auto; widows: 2; font-size: 11pt;">Exception in thread “main” java.lang.UnsupportedClassVersionError: org/vertx/java/deploy/impl/cli/Starter : Unsupported major.minor version 51.0</span>  
<span style="color: rgb(0, 0, 0); font-family: Tahoma; line-height: normal; orphans: 2; text-align: -webkit-auto; widows: 2; font-size: 11pt;">        at java.lang.ClassLoader.defineClass1(Native Method)</span>  
<span style="color: rgb(0, 0, 0); font-family: Tahoma; line-height: normal; orphans: 2; text-align: -webkit-auto; widows: 2; font-size: 11pt;">        at java.lang.ClassLoader.defineClassCond(ClassLoader.java:631)</span>  
<span style="color: rgb(0, 0, 0); font-family: Tahoma; line-height: normal; orphans: 2; text-align: -webkit-auto; widows: 2; font-size: 11pt;">        at java.lang.ClassLoader.defineClass(ClassLoader.java:615)</span>  
<span style="color: rgb(0, 0, 0); font-family: Tahoma; line-height: normal; orphans: 2; text-align: -webkit-auto; widows: 2; font-size: 11pt;">        at java.security.SecureClassLoader.defineClass(SecureClassLoader.java:141)</span>  
<span style="color: rgb(0, 0, 0); font-family: Tahoma; line-height: normal; orphans: 2; text-align: -webkit-auto; widows: 2; font-size: 11pt;">        at java.net.URLClassLoader.defineClass(URLClassLoader.java:283)</span>  
<span style="color: rgb(0, 0, 0); font-family: Tahoma; line-height: normal; orphans: 2; text-align: -webkit-auto; widows: 2; font-size: 11pt;">        at java.net.URLClassLoader.access$000(URLClassLoader.java:58)</span>  
<span style="color: rgb(0, 0, 0); font-family: Tahoma; line-height: normal; orphans: 2; text-align: -webkit-auto; widows: 2; font-size: 11pt;">        at java.net.URLClassLoader$1.run(URLClassLoader.java:197)</span>  
<span style="color: rgb(0, 0, 0); font-family: Tahoma; line-height: normal; orphans: 2; text-align: -webkit-auto; widows: 2; font-size: 11pt;">        at java.security.AccessController.doPrivileged(Native Method)</span>  
<span style="color: rgb(0, 0, 0); font-family: Tahoma; line-height: normal; orphans: 2; text-align: -webkit-auto; widows: 2; font-size: 11pt;">        at java.net.URLClassLoader.findClass(URLClassLoader.java:190)</span>  
<span style="color: rgb(0, 0, 0); font-family: Tahoma; line-height: normal; orphans: 2; text-align: -webkit-auto; widows: 2; font-size: 11pt;">        at java.lang.ClassLoader.loadClass(ClassLoader.java:306)</span>  
<span style="color: rgb(0, 0, 0); font-family: Tahoma; line-height: normal; orphans: 2; text-align: -webkit-auto; widows: 2; font-size: 11pt;">        at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:301)</span>  
<span style="color: rgb(0, 0, 0); font-family: Tahoma; line-height: normal; orphans: 2; text-align: -webkit-auto; widows: 2; font-size: 11pt;">        at java.lang.ClassLoader.loadClass(ClassLoader.java:247)</span>  
</div><span style="color: rgb(0, 0, 0); font-family: Tahoma; font-size: 11pt; line-height: normal; orphans: 2; text-align: -webkit-auto; widows: 2;">Could not find the main class: org.vertx.java.deploy.impl.cli.Starter.  Program will exit.</span>

</div><span style="font-size: 11pt;">해결 방안 =>  java 설치후, PATH 추가 뿐만 아니라 JAVA_HOME 부분도 수정을 해야한다. `JAVA_HOME` 이 이전에 사용하던 `JDK 1.5` 혹은 1.6으로 나오는 경우 설치한 1.7 디렉토리로 설정해 준후 다시 설치를 확인한다. </span>

<span style="font-size: 15px; line-height: 29px;">  
</span>



