---
title: 'heroku rename and updating git'
author: 'ash84'
pub_date: '2015-04-15'
description: 'heroku는 신기하게 `create` 명령어 이후에 개인 공간에 앱의 공간을 만들어 주는데 임의의 문자와 숫자를 넣어서 만든다. 예를들어, 내가 만든 프로젝트는 loginabtesting 이라고 하면, `heroku create` 를 통해서 만들어진 앱의 이름은 `thawing-plain-5857` 이런 이름으로 만들어 진다. 당연히 프로젝트 이름은 설정에 가서 바꿀수가 있는데 바꿔 버리면 그 다음에 수정시에 배포(deploy)가 안되는 문제가 생긴다. 그래서 heroku 에서는 아래와 같이 앱의 이름을 변경시에 주의사항 툴팁을'
featured_image: ''
tags: ['dev', 'git remote', 'heroku', 'rename app']
---


heroku는 신기하게 `create` 명령어 이후에 개인 공간에 앱의 공간을 만들어 주는데 임의의 문자와 숫자를 넣어서 만든다. 예를들어, 내가 만든 프로젝트는 loginabtesting 이라고 하면, `heroku create` 를 통해서 만들어진 앱의 이름은 `thawing-plain-5857` 이런 이름으로 만들어 진다. 당연히 프로젝트 이름은 설정에 가서 바꿀수가 있는데 바꿔 버리면 그 다음에 수정시에 배포(deploy)가 안되는 문제가 생긴다. 그래서 heroku 에서는 아래와 같이 앱의 이름을 변경시에 주의사항 툴팁을 제공하곤 한다.

<div class="jetpack-video-wrapper">[![heroku_rename](https://farm9.staticflickr.com/8766/16944908117_3ae84735ee_z.jpg)](https://flic.kr/p/rPn5Qe)</div> 

[해당 링크](https://devcenter.heroku.com/articles/renaming-apps#updating-git-remotes)를 들어가보면 내용은 이렇다.

> CLI를 이용해서 앱 이름은 변경했을때에는, 자동으로 remote 부분이 업데이트 되는데 웹사이트에서 앱이름을 변경했을 때에는 수동으로 업데이트 해줘야 한다.

<script src="https://gist.github.com/AhnSeongHyun/7119c1d509815ccae037.js"></script>



