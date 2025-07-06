---
title: '(Django) Aptana Studio3 Django Not found 오류 해결법'
author: 'ash84'
pub_date: '2017-03-28'
description: 'Django 프로젝트를 만들려고 하는데 pip install django 로 django를 설치했음에도 불구하고  
 Django not found 라는 오류창과 함께 프로젝트가 생성되지 않는다. 

한창 삽질을 했는데 문제는 path 부분에서 site-packages 를 잡아주지 않아서 생기는 문제이다.  
 APTANA STUDIO3 에서 preference 에 들어가서 pydev=> interpreter-python 에 들어가면  
 아래의 화면을 볼수 있다'
featured_image: ''
tags: ['Aptana Studio3', 'dev', 'Django', 'Python', '파이썬']
---


<span style="font-size: 11pt;">Django 프로젝트를 만들려고 하는데 pip install django 로 django를 설치했음에도 불구하고  
 Django not found 라는 오류창과 함께 프로젝트가 생성되지 않는다. </span>

한창 삽질을 했는데 문제는 path 부분에서 site-packages 를 잡아주지 않아서 생기는 문제이다.  
 APTANA STUDIO3 에서 preference 에 들어가서 pydev=> interpreter-python 에 들어가면  
 아래의 화면을 볼수 있다. site-packages 는 pip install 을 통해서 받은 라이브러리가 저장되어 있는것을 확인할 수 있는데  
 New Folder를 통해서 site-packages 경로를 넣고 Apply를 하면 된다.

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;"></span>

![](http://ash84.net/wp-content/uploads/1/cfile26.uf.270CC23452AFBEA21386B7.png)

<span style="font-size: 11pt;">  
</span>



