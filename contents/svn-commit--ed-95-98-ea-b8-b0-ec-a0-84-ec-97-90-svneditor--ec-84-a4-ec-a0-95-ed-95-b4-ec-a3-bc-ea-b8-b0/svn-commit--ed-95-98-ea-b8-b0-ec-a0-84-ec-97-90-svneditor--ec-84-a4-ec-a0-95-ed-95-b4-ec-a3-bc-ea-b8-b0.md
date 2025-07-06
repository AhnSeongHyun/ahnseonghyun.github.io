---
title: 'SVN Commit 하기전에 SVN_EDITOR 설정해주기.'
author: 'ash84'
pub_date: '2013-04-11'
description: 'vi 에서 작업하는것을 그리 좋아하라 하진 않지만 작업을 해야만 할때가 있기 때문에 세팅을 해놔야 하는데 특히 commit 하기 전에 `SVN_EDITOR`를 설정해 두어야 svn commit 명령어를 주었을때 vi 가 실행이 되고 거기에 svn 메시지를 남길 수 가 있다. 그렇다면 SVN_EDITOR는 어디에 설정을 해야하냐? home/본인계정 아래에서 있는 `.bash_profile `파일을 열어서 설정하면 된다.'
featured_image: ''
tags: ['SVN', 'SVN_EDITOR']
---


<span style="font-size: 11pt;">vi 에서 작업하는것을 그리 좋아하라 하진 않지만 작업을 해야만 할때가 있기 때문에 세팅을 해놔야 하는데 특히 commit 하기 전에 `SVN_EDITOR`를 설정해 두어야 svn commit 명령어를 주었을때 vi 가 실행이 되고 거기에 svn 메시지를 남길 수 가 있다. 그렇다면 SVN_EDITOR는 어디에 설정을 해야하냐? home/본인계정 아래에서 있는 `.bash_profile `파일을 열어서 설정하면 된다. </span>

<span style="font-size: 11pt;">  
</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 15px; line-height: 29px;">export SVN_EDITOR=”/usr/bin/vim”  
</span>

</div>

