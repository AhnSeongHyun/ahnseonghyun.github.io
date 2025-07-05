---
title: 'PyCurl 사용하기'
author: 'ash84'
pub_date: '2017-11-15'
description: ''
featured_image: ''
tags: ['dev', 'Python', 'pycurl', 'requests']
---

페이스북 코리아에 [requests 보다 pycurl 이 더 성능이 좋다는 stackoverflow 글](https://stackoverflow.com/questions/15461995/python-requests-vs-pycurl-performance)이 공유되서 pycurl 이 몬지 requests 코드와 비교해 보면서 익혀보았다. 일단 아래의 코드는 실제 POST 요청을 보내고 json 데이터를 받는 API를 호출하는 코드이다. 

<script src="https://gist.github.com/AhnSeongHyun/0148e88f1b1d278178fdc374d3238ef5.js"></script>

requests 는 홈페이지에도 써있듯이 Requests: HTTP for Humans 이라는 타이틀에 맞게 확실히 코드가 깔끔해 지는것 같다. 코드에 함수로 GET, POST 를 지정하고, 파라미터로 content-type 을 지정하는 건 확실히 편한것 같다. headers 값을 전달하기 위해서 dict 객체를 만들어서 키값으로 전달하면 된다. 

<script src="https://gist.github.com/AhnSeongHyun/ace0ae00ac0d4f06da1208e06304d7ef.js"></script>

pycurl 은 말그대로 curl 이다. curl 에 대해서 익숙하지 않다면 처음에 사용하기가 번거로움이 있다. URL 설정, POST 요청이나 HEADER 의 경우 `setopt()` 함수를 이용해서 설정해야 한다. 원래 `CURLOPT_POST`, `CURLOPT_URL`, `CURLOPT_HTTPHEADER` 으로 설정해야 하는데, pycurl 에서는 `CURLOPT_URL` prefix 를 제거한 채로 제공하고 있다. 헤더값을 넣는 부분이나 response json 값이나, response header 를 가져올 때 requests 와 다르게 pycurl 은 문자열 형태로 주어지기 때문에 별도의 처리를 위해서는 작업을 해줘야 한다. 

API를 호출했을때에 속도는 확실히 차이는 나는것 같다. 전문적인 테스트를 해보진 않았지만 같은 API에 대한 결과를 받고 시간을 체크를 해보면 차이는 확실하게 나는 것 같다. 기존에 사용하고 있는 requests 를 코드상에서 대체할지는 개인적으로 약간 주저되긴 하는데, 성능이슈가 생기게 되면 좋은 대안이 될 것 같다. 


