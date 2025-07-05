---
title: 'SVN Commit 시, Could not use external editor to fetch log message'
author: 'ash84'
pub_date: '2011-10-18'
description: ''
featured_image: ''
tags: ['Commit', 'export', 'SVN', 'SVN_EDITOR', 'unix', '유닉스', '커밋']
---


<span class="Apple-style-span" style="font-family: Verdana, Gulim, sans-serif; line-height: 16px; background-color: rgb(255, 255, 255); "><font class="Apple-style-span" color="#000000"><span style="font-size: 10pt; "><span style="font-family: Dotum; "></span></span></font></span>

svn commit 시에 간혹 다음과 같은 에러 메시지를 볼 수 있다.  
  

<div class="txc-textbox" style="border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-top-color: rgb(203, 203, 203); border-right-color: rgb(203, 203, 203); border-bottom-color: rgb(203, 203, 203); border-left-color: rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; "><font class="Apple-style-span" color="#000000"><span style="font-size: 10pt; "><span style="font-family: Dotum; ">svn: Commit failed (details follow):</span></span>  
<span style="font-size: 10pt; "><span style="font-family: Dotum; ">svn: Could not use external editor to fetch log message; consider setting  
 the $SVN_EDITOR environment variable or using the --message (-m) or --file (-F) options</span></span>  
<span style="font-size: 10pt; "><span style="font-family: Dotum; ">svn: None of the environment variables SVN_EDITOR, VISUAL or EDITOR is set, and   
 no 'editor-cmd' run-time configuration option was found</span></span>  
</font>

<font class="Apple-style-span" color="#000000"><span style="font-size: 10pt; "></span></font>

</div><font class="Apple-style-span" color="#000000"><span style="font-size: 10pt; "><span style="font-family: Dotum; "></span></span></font>

 SVN_EDITOR 변수에 적절한 editor 실행파일명을 넣어서 해결할 수 있다.

<span style="font-size: 10pt; "><span style="font-family: Dotum; ">$ vim ~/.bash_profile</span></span>

<span style="font-size: 10pt; "><span style="font-family: Dotum; "><div class="txc-textbox" style="border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-top-color: rgb(203, 203, 203); border-right-color: rgb(203, 203, 203); border-bottom-color: rgb(203, 203, 203); border-left-color: rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px; ">export SVN_EDITOR=”/usr/bin/vim”

</div></span></span>  
<font class="Apple-style-span" style="text-decoration: none; ">[   
 하고 나서 반드시, 세션을 종료하고  ](http://www.antbrown.com/nerd-musings/svn-could-not-use-external-editor-to-fetch-log-message/)다시 로그인을 해야한다. </font>[](http://www.antbrown.com/nerd-musings/svn-could-not-use-external-editor-to-fetch-log-message/)



