---
title: 'git remote branch 혹은 tags 가져오기'
author: 'ash84'
pub_date: '2019-09-02'
description: ''
featured_image: ''
tags: ['Git', 'remote', 'branch', 'tags']
---

최근에 git pull 혹은 checkout 하는 개인적은 툴을 만들고 있는데, git 의  remote 의  branch 나 tags 를 가져오고 싶을때가 있다. 예를 들어, git-flow 로 작업을 하게 되면 `feature/support-api` 이런식의 branch 로 작업을 하고 remote 로 push 하는 경우가 있는데, 이런 branch 를 가져오고 싶었다. 또 github 의 release 의 경우 tags 에서 따서 하는 경우가 보통인데, tags 를 가져오고 싶었다. 그런데 보통 git repo 안에서 git 명령어로 가져오면 되는데, repo 가 없는 상태에서 그것들만 가져오고 싶어서 찾아보니 이런 방법이 있었다. 

```
git ls-remote --tags /url/to/upstream/repo
git ls-remote --heads /url/to/upstream/repo
```

```shell
❯ git ls-remote --tags https://github.com/meier-project/meier
e454520ceb3d6ba57049eb30c677dc5bec6360f3	refs/tags/1.0.0
c209ffa55ce96df091bfef9f6fa977a5bb65cd03	refs/tags/1.0.1
```

```shell
❯ git ls-remote --heads https://github.com/meier-project/meier
c45308da08f21539dda6be9fc2e85b2f53ab4ea2	refs/heads/develop
c209ffa55ce96df091bfef9f6fa977a5bb65cd03	refs/heads/master
```
