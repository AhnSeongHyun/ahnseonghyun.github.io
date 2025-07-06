---
title: '[svn] svn log with diff yesterday'
author: 'ash84'
pub_date: '2016-08-15'
description: '다른 사람의 코드를 보면 아무래도 이해를 더 잘 할수 있도 특히 같은 프로젝트나 같은 팀이라면 언어가 다르더라도 보는것이 좋다고 생각하는데 엄청 많은 저장소를 일일히 뒤져가며 볼수는 없다. 아래의 스크립트는 하루전의 커밋로그와 함께 그에 대한 diff 를 떠서 보여주는 파이썬 스크립트이다. 파일은 저장소 이름별로 만들도록 했는데 하나의 파일에 만들어도 되긴 하지만 diff 를 뜨게 되면 양이 엄청 많아진다.'
featured_image: ''
tags: ['dev', 'Python', 'SVN', 'svn log with diff yesterday', '개발']
---


다른 사람의 코드를 보면 아무래도 이해를 더 잘 할수 있도 특히 같은 프로젝트나 같은 팀이라면 언어가 다르더라도 보는것이 좋다고 생각하는데 엄청 많은 저장소를 일일히 뒤져가며 볼수는 없다. 아래의 스크립트는 하루전의 커밋로그와 함께 그에 대한 diff 를 떠서 보여주는 파이썬 스크립트이다. 파일은 저장소 이름별로 만들도록 했는데 하나의 파일에 만들어도 되긴 하지만 diff 를 뜨게 되면 양이 엄청 많아진다. 

<script src="https://gist.github.com/AhnSeongHyun/e45217c957febb68fc06.js"></script>

[2011/10/18 – [Technique] – SVN Commit 시, Could not use external editor to fetch log message](http://ash84.tistory.com/750)



