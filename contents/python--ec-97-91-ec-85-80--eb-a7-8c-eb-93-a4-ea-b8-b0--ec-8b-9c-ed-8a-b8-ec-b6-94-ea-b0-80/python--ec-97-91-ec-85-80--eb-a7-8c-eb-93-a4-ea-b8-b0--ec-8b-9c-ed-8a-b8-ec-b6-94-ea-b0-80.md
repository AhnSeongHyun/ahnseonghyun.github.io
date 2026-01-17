---
title: 'python create excel, add sheet'
author: 'ash84'
pub_date: '2015-01-21'
description: '파이썬에서 엑셀(csv 형식이 아닌) 파일을 만들고 시트를 추가하는 코드인데 openpyxl 을 사용하는 코드이다. 파라미터로 전송되는 구조에 종속적인 함수이긴 한데, 간단하게 사용법을 적어두는 목적이기에. 좀 애매한 부분들중 하나는 첫 시트를 지우지 않으면 시트 추가시 Sheet 라는 이름의 첫 시트가 남아 있는 문제가 있'
featured_image: ''
tags: ['dev', 'Python', '엑셀', '엑셀 시트 추가']
---
<script src="https://gist.github.com/AhnSeongHyun/efa9f807c8cb95a5243b.js"></script>

<span style="font-size: 10pt;">파이썬에서 엑셀(csv 형식이 아닌) 파일을 만들고 시트를 추가하는 코드인데 openpyxl 을 사용하는 코드이다. 파라미터로 전송되는 구조에 종속적인 함수이긴 한데, 간단하게 사용법을 적어두는 목적이기에. 좀 애매한 부분들중 하나는 첫 시트를 지우지 않으면 시트 추가시 Sheet 라는 이름의 첫 시트가 남아 있는 문제가 있어서 Sheet 라는 이름을 찾아서 지우고 있다. 레퍼런스를 찾아서 첫 시트를 이름을 바꾸어서 사용하거나 아니면 아예 처음부터 지우고 시작하는게 나을듯.</span>



