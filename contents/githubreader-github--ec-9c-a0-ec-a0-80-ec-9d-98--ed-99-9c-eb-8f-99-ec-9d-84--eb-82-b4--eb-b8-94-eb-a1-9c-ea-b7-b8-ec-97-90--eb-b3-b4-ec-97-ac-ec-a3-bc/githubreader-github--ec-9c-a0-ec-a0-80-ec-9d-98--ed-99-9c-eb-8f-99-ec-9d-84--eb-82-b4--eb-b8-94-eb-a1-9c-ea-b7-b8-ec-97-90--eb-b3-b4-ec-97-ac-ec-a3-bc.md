---
title: 'github_reader, github 유저의 활동을 내 블로그에 보여주기.'
author: 'ash84'
pub_date: '2012-10-25'
description: '개인적으로 github를 가장 좋아하는 서비스로 뽑고 있고, 필자 역시 github 에 무엇인가를 올리는 작업을 좋아한다. 여타의 코드 저장소 및 커뮤니티와 다른 점이라면 단연 소셜적인 기능을 통해서 다른 사람들과 좀더 친밀하게 뭔가를 할수 있다는 점이겠다. 이러한 이유로 인해서 github는 개발자들 외 여타의 다른 분들도 많이들 쓰신다. 
거두절미 하고. 내가 **[github_reader](https:'
featured_image: ''
tags: ['github', 'github 블로그', 'github 연동', 'github_reader', 'public activity', '블로그와 연동']
---


<span style="font-size: 12pt;">개인적으로 github를 가장 좋아하는 서비스로 뽑고 있고, 필자 역시 github 에 무엇인가를 올리는 작업을 좋아한다. 여타의 코드 저장소 및 커뮤니티와 다른 점이라면 단연 소셜적인 기능을 통해서 다른 사람들과 좀더 친밀하게 뭔가를 할수 있다는 점이겠다. 이러한 이유로 인해서 github는 개발자들 외 여타의 다른 분들도 많이들 쓰신다. </span>

<span style="font-size: 12pt;">거두절미 하고. 내가 **[github_reader](https://github.com/AhnSeongHyun/github_reader) 를 만든 이유는 블로그에서 나의 github 활동을 보여주고 싶어서** 였다. 단지 그 이유때문에 만든것인데, 가서 보면 되지 않냐고 하지만, 다들 알다시피 web 상에서의 1depth는 매우 접근성 차이가 난다. **때문에 블로그의 첫 화면에서 보여주겠다는 것이 가장 큰 목표였다. **</span>

<span style="font-size: 12pt;">github의 활동은 위에서 처럼 해당 유저가 무엇을 하고 있는지를 보여주는 역할을 한다. 그리고 RSS 표시가 있는 버튼을 누르면 RSS 리더로 구독할 수도 있다. 그러나 실제 형식은 RSS 가 아니라 ATOM 형식이다. RSS 라면 [javascript rss box viewer](http://p3k.org/rss/) 라는 툴을 이용해서 간단히 할수 있었을텐데, 조금은 아쉽다. </span>

<span style="font-size: 12pt;">그래서 javascript 로 저 부분의 atom을 받아와서 블로그의 사이드바에 보여주도록 만들기로 하였다. 여러가지 방법을 찾던중, Google Feed API 에 대해서 찾게 되었다. 이 API 의 역할은 feed url 주소를 주면 해당 feed 를 가져와서 entry로 반환해 준다는 것이었다. 역시 구글신이다. 가볍게 [Google Feed API](https://developers.google.com/feed/)의 예제를 받아서 public activity atom 주소를 넣으니 entry를 반환해 준다. </span>

<span style="font-size: 12pt;">**entry는 여러가지 속성을 가지는데 그 중에서 contentSnippet 과 link 를 이용해서 보여주도록 하였다. **content를 이용하면 좀더 많은 상세한 정보를 뽑을수 있지만, 문제는 태그가 묻어나오는 문제가 있어서 그것은 제외하고, contentSnippet에 link를 a태그를 붙여서 연결하도록 하였다. </span><span style="font-size: 12pt;">그리고 나서 기본적으로 좀더 이쁘게 보여주기 위한 CSS 적용작업을 더했다. </span>

<span style="font-size: 12pt;">별것 아닌것처럼 보이는데, 별것 아니다. [Google Feed API](https://developers.google.com/feed/)를 통해서 많은 도움을 받았지만, 아직 github에서 제공되지 않는 기능을 만들었다는 것에 대해서 성취감을 가지고 있고, 매쉬업과 OpenAPI를 적극 활용해야겠다는 생각이 들었다. </span>

<span style="font-size: 12pt;"> </span>

<div class="txc-textbox" style="border: 1px solid #cbcbcb; background-color: #ffffff; padding: 10px;"><span style="font-size: medium;"><span style="line-height: 32px;">**관련 기술 정보 **</span></span>

<span style="font-size: medium;"><span style="line-height: 32px;">github_reader : [https://github.com/AhnSeongHyun/github_reader](https://github.com/AhnSeongHyun/github_reader)</span>  
<span style="line-height: 32px;">Google Feed API :[https://developers.google.com/feed/](https://developers.google.com/feed/)</span></span>

<span style="font-size: medium;"><span style="line-height: 32px;">w3c School : [http://www.w3schools.com/](http://www.w3schools.com/)</span></span>

</div><span style="font-size: medium;"><span style="line-height: 32px;"> </span></span>

<span style="font-size: 12pt;">마지막으로 github 관련 TED 동영상 하나 투척. </span>

<span style="font-size: 12pt;"> </span>

 

<center>  
<iframe allowfullscreen="allowfullscreen" frameborder="0" height="315" scrolling="no" src="http://embed.ted.com/talks/lang/ko/clay_shirky_how_the_internet_will_one_day_transform_government.html" width="560">  
 </center></iframe></center>  



