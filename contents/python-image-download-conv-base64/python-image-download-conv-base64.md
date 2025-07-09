---
title: '(python) image download conv base64'
author: 'ash84'
pub_date: '2013-08-28'
description: 'base64로 변환을 해야하는 이유부터 설명하자면 간단하다. 이미지의 경우, 파일서버에 저장하는 것이 최고의 방법이긴 하지만 다들 알다시피 서버의 용량 문제가 있어서 OpenAPI를 이용해서 데이터를 가져오게 되는'
featured_image: ''
tags: ['BASE64', 'dev', 'image download', 'Open API', 'Python']
---


<script src="https://gist.github.com/AhnSeongHyun/6372346.js"></script>

<span style="font-size: 11pt;"></span><span style="font-size: 11pt;"></span><span style="font-size: 11pt;">base64로 변환을 해야하는 이유부터 설명하자면 간단하다. 이미지의 경우, 파일서버에 저장하는 것이 최고의 방법이긴 하지만 다들 알다시피 서버의 용량 문제가 있어서 OpenAPI를 이용해서 데이터를 가져오게 되는게 자바스크립트 크로스도메인 문제 혹은 이미지 자체를 다른쪽에서 쓰는 것을 금지하는 경우들이 있다.(자바스크립트에 넣어서 호출하는 경우가 아니라도 말이다.) </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">그럴경우, 찾아낸 방법(정선생)이 이미지 자체를 다운로드해서 base64로 변환하고 html img 태그 src 속성에 base64 자체를 집어 넣는 방법이다. </span>

상대적으로 파이썬 코드가 깔끔한데 urllib2 라이브러리를 이용해서 image url 의 데이터를 가져오고 base64 형식으로 변환하는 코드인데, 설명하기 조차 민망하게 짧다.

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;"> 꼼수긴 하지만 open API 를 사용하려면 어쩔수가 없고 솔직히 이미지 검색 API를 제공하는 포털쪽에서 걸릴것은 거르고 이렇게 꼼수부릴 필요없이 제공해 줬으면 좋겠다. </span>

이 방식으로 서비스 했을때 어떤 문제가 있을지 예상 되긴 하지만 아직은 잘 모르겠다.<span style="font-size: 11pt;"></span><span style="font-size: 11pt;"></span><span style="font-size: 11pt;"></span>



