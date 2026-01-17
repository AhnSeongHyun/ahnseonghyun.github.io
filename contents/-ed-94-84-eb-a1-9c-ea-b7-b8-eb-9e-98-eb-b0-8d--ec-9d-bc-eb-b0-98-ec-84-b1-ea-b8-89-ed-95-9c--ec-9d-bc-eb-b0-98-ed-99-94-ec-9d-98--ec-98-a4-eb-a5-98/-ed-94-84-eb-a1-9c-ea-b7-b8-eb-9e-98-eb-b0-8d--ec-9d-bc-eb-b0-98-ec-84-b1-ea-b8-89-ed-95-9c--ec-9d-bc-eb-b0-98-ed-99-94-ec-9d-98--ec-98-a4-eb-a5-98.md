---
title: '[프로그래밍 일반]성급한 일반화의 오류'
author: 'ash84'
pub_date: '2009-11-09'
description: '[![Day 308: X](http://farm3.static.flickr.com/2537/4076648343_767c69a46e.jpg)](http://www.flickr.com/photos/91252560@N00/4076648343 "Day 308: X")  
Day 308: X by [theogeo](http://www.flickr.com/photos/91252560@N00)[![저작자 표시](http://cfs.tist'
featured_image: ''
tags: ['데이터', '보정필터', '성급한 일반화의 오류', '펌웨어', 'programming']
---
<table class="flickrImgSearch"><tbody><tr><td>[![Day 308: X](http://farm3.static.flickr.com/2537/4076648343_767c69a46e.jpg)](http://www.flickr.com/photos/91252560@N00/4076648343 "Day 308: X")  
<span>Day 308: X by [theogeo](http://www.flickr.com/photos/91252560@N00)</span>[![저작자 표시](http://cfs.tistory.com/static/admin/editor/ccl_black01.png)](http://creativecommons.org/licenses/by/2.0/kr/)</td></tr></tbody></table><div style="TEXT-ALIGN: justify"> 성급한 일반화의 오류란, 몇가지의 부분을 보고 전체를 일반화 시켜서 판단하는 오류를 말한다.   
 예를 들면,   
    
<font color="#c8056a">  A라는 한국인이 개고기를 먹는다.   
   B라는 한국인이 개고기를 먹는다.   
   그러므로, 모든 한국인은 개고기를 먹는다.   
</font>  
 이러한 성급한 일반화의 오류를 필자도 저번주에 펌웨어 보정 필터를 개발 하면서 겪었기에 이렇게 글을 쓰게 되었다. 특정 수치를 넘는 데이터에 대해서만 평균값을 취해서 버퍼의 한 포인트를 삽입하는 형식으로 보정 필터를 개발하는데, 특정 수치를 설정하는 과정에서 필자가 성급한 일반화의 오류를 범했다. ![](http://ash84.net/wp-content/uploads/1/cfile9.uf.123456224AF768E23E5DEB.png)

센서에서 가까운 A라는 점에서 획득한 데이터와 센서에서 가장 먼 B라는 점에서 획득한 데이터만을 분석해서 특정 수치를 기준점을 잡는 작업을 했는데 가운데 있는 점이라던지, 사각지대에 있는 포인트의 경우 데이터가 다르게 나온다는 것을 인지 하지 못하는 문제가 발생하였다.

실제로 굉장히 많은 포인트를 검사하고 분석해서 필터의 조건과 기준 점을 정해야 함에도 불구하고 귀찮은 관계로 몇몇의 점을 가지고 설정한 결과 보정 필터의 부작용이 나타나는 부분도 있었고, 조건과 기준점을 피해가는 점도 있었다.

프로그래밍을 하면서 굉장히 많이 이런 오류가 발생하는 것을 보았다. 본래, 시간과 비용이 정해진 회사에서의 프로그래밍의 경우 사실 정답이 아님에도 불구하고 결과만을 위해서 편법을 쓰거나 과학적이지, 논리적이지 못한 방법이 동원되는것 같다. 결과적으로 결과가 좋으면 다행일지도 모르지만, 제품화되어서 사용자가 사용하는 순간이 우리에게는 진정한 결과가 보여지는 순간이라고 생각되어 진다.

어쩌면, 나는 A와 B 포인트를 분석하면서 직감적으로 성급한 일반화의 오류가 발생될 여지를 알고 있었을 지도 모르겠다. 그러면서도 빨리 끝내고 싶은 마음에 그런 오류를 발생하지 않을것이라고 기대하고 넘어갔는지도 모르겠다.

</div><div style="TEXT-ALIGN: justify">  

</div>

