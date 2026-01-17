---
title: '(C++) 정적 검사 및 메모리 검사 툴'
author: 'ash84'
pub_date: '2013-04-09'
description: '자주 사용하지는 않지만 문제가 터지면 반드시 사용해야 하는 두개의 툴인데 사실 cppCheck는 그렇게 많이 사용하지는 않고, 문제 터지면 valgrind 부터 돌려보는 편이라. 그래도 어떤때 사용하게 되는 툴들이라 정리해 둔다. 
**cppCheck **'
featured_image: ''
tags: ['C#', 'cppCheck', 'dev', 'tutorial', 'valgrind', '동적검사', '메모리 검사', '정적검사']
---
<span style="font-size: 11pt;">자주 사용하지는 않지만 문제가 터지면 반드시 사용해야 하는 두개의 툴인데 사실 cppCheck는 그렇게 많이 사용하지는 않고, 문제 터지면 valgrind 부터 돌려보는 편이라. 그래도 어떤때 사용하게 되는 툴들이라 정리해 둔다. </span>

<span style="font-size: 11pt;">**<span style="font-size: 11pt;">cppCheck </span>**</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">– link : </span>[<span style="font-size: 11pt;">http://sourceforge.net/projects/cppcheck/</span>](http://sourceforge.net/projects/cppcheck/)

<span style="font-size: 11pt;">– 사용법 : </span>[<span style="font-size: 11pt;">http://kindtis.tistory.com/287</span>](http://kindtis.tistory.com/287)

<span style="font-size: 11pt;">– Visual Studio 연동 법 :</span>[<span style="font-size: 11pt;">http://devilchen.tistory.com/4036</span>](http://devilchen.tistory.com/4036)

</div><span style="font-size: 11pt;">**<span style="font-size: 11pt;">valgrind </span>**</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">– link : </span>[<span style="font-size: 11pt;">http://valgrind.org/</span>](http://valgrind.org/)

<span style="font-size: 11pt;">– 사용법</span><span style="font-size: 11pt;"> : </span>[<span style="font-size: 11pt;">http://forum.falinux.com/zbxe/index.php?document_srl=528619&mid=lecture_tip</span>](http://forum.falinux.com/zbxe/index.php?document_srl=528619&mid=lecture_tip)<span style="font-size:11pt;"> </span>

</div>**<span style="font-size: 11pt;">자주 사용하는 형태 </span>**

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="color: rgb(0, 0, 0); line-height: normal; orphans: 2; text-align: -webkit-auto; widows: 2; font-size: 10pt;"><span style="font-size: 11pt;"></span><span style="font-size: 11pt;">valgrind –leak-check=full –log-file=memcheck.txt -v –error-limit=no –track-origins=yes </span></span><span style="font-size:11pt;"> 실행 exe</span><span style="font-size: 11pt;"></span>

</div>

