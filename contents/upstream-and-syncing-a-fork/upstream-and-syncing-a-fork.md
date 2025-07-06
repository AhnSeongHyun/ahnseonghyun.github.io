---
title: 'Upstream and Syncing a fork'
author: 'ash84'
pub_date: '2016-03-28'
description: '위와 같은 경우가 많이 발생을 한다. 하나의 github 프로젝트에서 내가 뭔가의 수정을 위해서 fork 를 하고, 수정을 해서 Pull Request 를 날린후, Merge 가 된다. 그리고 다른 사람이 원래의 프로젝트에 커밋을 하면 내가 fork 뜬 프로젝트에서는 해당 커밋들을 가져와야 한다. 그래야 최신 상태에서의 기여가 가능하니까. 어떻게 해야할까? 찾아 보니 Upstream 이라는 개념이 github 에 있어서 소개 한다. 


>[**Upstream**](https://help.github.com/articles/gi'
featured_image: 'https://farm2.staticflickr.com/1677/25443068384_426cac00b2_k.jpg'
tags: ['Git', 'upstream', 'sync a fork', 'dev']
---



위와 같은 경우가 많이 발생을 한다. 하나의 github 프로젝트에서 내가 뭔가의 수정을 위해서 fork 를 하고, 수정을 해서 Pull Request 를 날린후, Merge 가 된다. 그리고 다른 사람이 원래의 프로젝트에 커밋을 하면 내가 fork 뜬 프로젝트에서는 해당 커밋들을 가져와야 한다. 그래야 최신 상태에서의 기여가 가능하니까. 어떻게 해야할까? 찾아 보니 Upstream 이라는 개념이 github 에 있어서 소개 한다. 


>[**Upstream**](https://help.github.com/articles/github-glossary/)

>When talking about a branch or a fork, **the primary branch on the original repository is often referred to as the "upstream"**, since that is the main place that other changes will come in from. The **branch/fork you are working on is then called the "downstream".**

<center>
<a href="http://stackoverflow.com/questions/9257533/what-is-the-difference-between-origin-and-upstream-in-github"><img src="http://i.stack.imgur.com/cEJjT.png"/></a>
</center>

원래의 저장소/프로젝트를 Upstream, 그리고 fork 나 branch 를 downstream 이라고 부른다는 것이다. 그렇다면, Upstream 에서 커밋들을 가져오려면 어떻게 해야할까? 아래의 링크에서 잘 설명이 되어 있다. 

https://help.github.com/articles/syncing-a-fork/

따라해보니.

```
> git fetch upstream
> fatal : 'upstream' does not appear to be a fit repository
> fatal : Could not read from remote repository. 
```

일단 upstream 이 지정되지 않은것 같아서 upstream 을 지정하기 위해서 아래와 같이 진행했다. 

```
$ git remote -v
origin  https://github.com/AhnSeongHyun/flask-dmango.git (fetch)
origin  https://github.com/AhnSeongHyun/flask-dmango.git (push)


$ git remote add upstream https://github.com/jungkoo/flask-dmango.git


$ git remote -v
origin  https://github.com/AhnSeongHyun/flask-dmango.git (fetch)
origin  https://github.com/AhnSeongHyun/flask-dmango.git (push)
upstream        https://github.com/jungkoo/flask-dmango.git (fetch)
upstream        https://github.com/jungkoo/flask-dmango.git (push)

$ git fetch upstream
remote: Counting objects: 13, done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 13 (delta 6), reused 10 (delta 3), pack-reused 0
Unpacking objects: 100% (13/13), done.
From https://github.com/jungkoo/flask-dmango
 * [new branch]      iss4-mlab-support -> upstream/iss4-mlab-support
 * [new branch]      master     -> upstream/master


$ git checkout master
Already on 'master'
Your branch is up-to-date with 'origin/master'.

$ git merge upstream/master
Updating ae324f9..cdae665
Fast-forward
 README.md | 7 ++++++-
 setup.py  | 4 ++--
 2 files changed, 8 insertions(+), 3 deletions(-)
```




