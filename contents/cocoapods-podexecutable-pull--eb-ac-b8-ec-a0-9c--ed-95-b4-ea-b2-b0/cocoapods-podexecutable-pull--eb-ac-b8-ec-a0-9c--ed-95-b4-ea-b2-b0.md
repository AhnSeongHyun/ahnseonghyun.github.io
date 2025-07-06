---
title: '(cocoapods) [!] Pod::Executable pull 문제 해결'
author: 'ash84'
pub_date: '2016-08-11'
description: '어느순간 cocoapods를 사용하다 보면, `pod install` 이라고 쳤는데 console 창에 빨간 글씨의 화면이 아래처럼 나올때가 있다. 이러면 `pod install` 로 인해서 workspace가 생기지 않게 된다. [대처법](http://stackoverflow.com/questions/18224627/error-on-pod-install)은 간단한데 cocoapods의 master repo 를 지우면 된다.  

```bash
$sudo rm -rf ~/.cocoapods
``` 

![](http://ash84'
featured_image: ''
tags: ['CocoaPods', 'cocoapods error', 'dev', 'Pod::Executable pull']
---

 어느순간 cocoapods를 사용하다 보면, `pod install` 이라고 쳤는데 console 창에 빨간 글씨의 화면이 아래처럼 나올때가 있다. 이러면 `pod install` 로 인해서 workspace가 생기지 않게 된다. [대처법](http://stackoverflow.com/questions/18224627/error-on-pod-install)은 간단한데 cocoapods의 master repo 를 지우면 된다.  

```bash
$sudo rm -rf ~/.cocoapods
``` 

![](http://ash84.net/wp-content/uploads/1/cfile4.uf.23498E3B52F833890EC351.png)

![](http://ash84.net/wp-content/uploads/1/cfile2.uf.23083C3B52F83389324179.png)



