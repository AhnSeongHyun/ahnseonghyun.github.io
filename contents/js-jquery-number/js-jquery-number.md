---
title: '[js] jquery-number 3자리 금액 쉼표(,) 찍기'
author: 'ash84'
pub_date: '2015-03-18'
description: '서버 단에서 해도 되겠지만, 프론트 단에서 괜찮은 라이브러리가 있어서 소개한다. 3자리마다 금액 숫자에서 쉼표를 찍는 라이브러리인데 쓰기가 쉬워서 메모해 놓는다.'
featured_image: ''
tags: ['3자리 금액 자바스크립트', 'dev', 'jQuery', 'jquery-number', 'JS', '통화']
---

서버 단에서 해도 되겠지만, 프론트 단에서 괜찮은 라이브러리가 있어서 소개한다. 3자리마다 금액 숫자에서 쉼표를 찍는 라이브러리인데 쓰기가 쉬워서 메모해 놓는다.

<div style="text-align: justify; line-height: 2;"></div><div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); padding: 10px; background-color: rgb(255, 255, 255);"><div style="text-align: justify; line-height: 2;">[<span style="font-size: 11pt;">https://github.com/customd/jquery-number</span>](https://github.com/customd/jquery-number)<span style="font-size: 11pt;"></span></div></div><span style="font-size: 11pt;"></span><span style="font-size: 11pt;"></span><span style="font-size: 11pt;"></span>

<div>###  Basic number formatting

The number method takes up to four parameters, but only the first one is required.

1. Number: The number you want to format.

<div style="box-sizing: border-box; margin-bottom: 16px;">$.number( <span style="box-sizing: border-box; color: rgb(0, 134, 179);">5020.2364</span> ); <span style="box-sizing: border-box; color: rgb(150, 152, 150);">// Outputs 5,020</span>

</div>
2. Decimal Places: The number of decimal places you wish to see. Defaults to 0.

<div style="box-sizing: border-box; margin-bottom: 16px;">$.number( <span style="box-sizing: border-box; color: rgb(0, 134, 179);">5020.2364</span>, <span style="box-sizing: border-box; color: rgb(0, 134, 179);">2</span> ); <span style="box-sizing: border-box; color: rgb(150, 152, 150);">// Outputs: 5,020.24</span>

</div>
3. Decimal Separator: The character(s) to use as a decimal separator. Defaults to ‘.’.

<div style="box-sizing: border-box; margin-bottom: 16px;">$.number( <span style="box-sizing: border-box; color: rgb(0, 134, 179);">135.8729</span>, <span style="box-sizing: border-box; color: rgb(0, 134, 179);">3</span>, <span style="box-sizing: border-box; color: rgb(24, 54, 145);"><span style="box-sizing: border-box;">'</span>,<span style="box-sizing: border-box;">'</span></span> ); <span style="box-sizing: border-box; color: rgb(150, 152, 150);">// Outputs: 135,873</span>

</div>
4. Thousands Separator: The character(s) to use as a thousands separator. Defaults to ‘,’.

<div style="box-sizing: border-box; margin-bottom: 16px;">$.number( <span style="box-sizing: border-box; color: rgb(0, 134, 179);">5020.2364</span>, <span style="box-sizing: border-box; color: rgb(0, 134, 179);">1</span>, <span style="box-sizing: border-box; color: rgb(24, 54, 145);"><span style="box-sizing: border-box;">'</span>,<span style="box-sizing: border-box;">'</span></span>, <span style="box-sizing: border-box; color: rgb(24, 54, 145);"><span style="box-sizing: border-box;">'</span><span style="box-sizing: border-box;">'</span></span> ); <span style="box-sizing: border-box; color: rgb(150, 152, 150);">// Outputs: 5 020,2 </span>

</div>

</div>

