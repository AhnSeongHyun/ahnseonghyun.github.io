---
title: 'UITableView section과 tableview cell 사이 뜨는 문제'
author: 'ash84'
pub_date: '2015-06-07'
description: '[![스크린샷_2015-06-04_오전_1.24.39](https://farm9.staticflickr.com/8896/18409219728_a729291b6a_n.jpg)](https://flic.kr/p/u3L4E9)위와 같이 grouped 스타일로 커스텀 셀을 만들고 secion 을 두었을때 이상하게 그림처럼 마지막 테이블셀과 다음 섹션 사이에 뜨는 문제가 있는데, 이 문제에 대해서 찾아보니 처음에는 UITableViewCell 상에서'
featured_image: ''
tags: ['dev', 'Grouped Style', 'IOS', 'Reducing the space between sections of the UITableView', 'UITableView']
---


<div class="jetpack-video-wrapper">[![스크린샷_2015-06-04_오전_1.24.39](https://farm9.staticflickr.com/8896/18409219728_a729291b6a_n.jpg)](https://flic.kr/p/u3L4E9)</div>위와 같이 grouped 스타일로 커스텀 셀을 만들고 secion 을 두었을때 이상하게 그림처럼 마지막 테이블셀과 다음 섹션 사이에 뜨는 문제가 있는데, 이 문제에 대해서 찾아보니 처음에는 UITableViewCell 상에서 뭔가 기본 여백? 같은것이 지정되어 있나 싶었는데 찾아보니 section 의 footer의 height 를 지정해야 한다고 한다. 아래와 같이 지정하면 되는데

<script src="https://gist.github.com/AhnSeongHyun/70160b424755c58f6c76.js"></script>

예전에도 썼었는데 왜 footer를 사용하지 않는데도 height 부분을 지정해야 하는지에 대해서 찾아보니 다음과 같이 iOS5 이후부터는 **해당 부분을 개발자가 직접 지정해 줘야 한다**고 애플 개발자 레퍼런스에 나와있다.

> Special Considerations  
>  Prior to iOS 5.0, table views would automatically resize the heights of footers to 0 for sections where tableView:viewForFooterInSection: returned a nil view. In iOS 5.0 and later, you must return the actual height for each section footer in this method.



