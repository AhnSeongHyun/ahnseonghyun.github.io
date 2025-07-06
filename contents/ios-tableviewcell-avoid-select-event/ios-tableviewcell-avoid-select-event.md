---
title: '(iOS) tableViewCell avoid select event'
author: 'ash84'
pub_date: '2015-07-03'
description: 'touch 이벤트를 기본적으로 TableViewCell  을 customize 해서 사용할때 받게 되는데, TableViewCell 내 버튼같은 컨트롤들이 의도하지 않게 이벤트에 의해서 선택이 되어지는 문제가 있다. 즉, cell 자체의 touch 이벤트가 전달되는 것인데, 의도하지 않는 문제를 일으킬수 있다. 아래처럼 설정을 하면 선택을 해'
featured_image: ''
tags: ['dev', 'IOS', 'tableViewCell']
---


<span style="font-size: 11pt;">touch</span><span style="font-size: 11pt;"> 이벤트를 기본적으로 TableViewCell  을 customize 해서 사용할때 받게 되는데, TableViewCell 내 버튼같은 컨트롤들이</span><span style="font-size: 11pt;"> 의도하지 않게 이벤트에 의해서 선택이 되어지는 문제가 있다. 즉, cell 자체의 touch 이벤트가 전달되는 것인데, 의도하지 않는 문제를 일으킬수 있다. 아래처럼 설정을 하면 선택을 해도 반응되지 않는다.<span style="font-size: 10pt;"> </span></span>

<span style="font-size: 11pt;"><span style="font-size: 10pt;">  
</span></span>

<span style="font-size: 11pt;"><span style="font-size: 10pt;">[(](http://stackoverflow.com/questions/190908/how-can-i-disable-the-uitableview-selection-highlighting)</span></span><span style="font-size: 10pt; line-height: 1.5;">[How can I disable the UITableView selection highlighting?)](http://stackoverflow.com/questions/190908/how-can-i-disable-the-uitableview-selection-highlighting)</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;"></span><span style="font-size: 11pt;">[cell setSelectionStyle:UITableViewCellSelectionStyleNone];</span><span style="font-size: 11pt;"></span>

</div>

