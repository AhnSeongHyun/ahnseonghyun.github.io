---
title: 'python json 기반 conf 파일 로드하기(object_hook)'
author: 'ash84'
pub_date: '2015-02-12'
description: 'conf 를 json 파일로 쓰는 경우가 있는데 주로 개인 프로젝트 할때 많이 쓰는 편인데 결국 conf 라는것을 환경설정 파일이기 때문에 파일로 가져와서 읽어야 하는 경우가 많다. 이 경우 json 을 바로 dict 으로 loads 해서 사용하게 되면 conf[“port”] 이런식으로 접근해야 하는데 object_hook 를 이용하면 객체의 형태로 접근할수가 있다. 좀더 코드가 깔끔해 진다랄까.'
featured_image: ''
tags: ['dev', 'JSON', 'loads', 'object_hook', 'Python']
---
conf 를 json 파일로 쓰는 경우가 있는데 주로 개인 프로젝트 할때 많이 쓰는 편인데 결국 conf 라는것을 환경설정 파일이기 때문에 파일로 가져와서 읽어야 하는 경우가 많다. 이 경우 json 을 바로 dict 으로 loads 해서 사용하게 되면 conf[“port”] 이런식으로 접근해야 하는데 object_hook 를 이용하면 객체의 형태로 접근할수가 있다. 좀더 코드가 깔끔해 진다랄까. 

<script src="https://gist.github.com/AhnSeongHyun/ba728b3f802ad3a9dfc4.js"></script>

[2015/01/30 – [Programming/Python] – [python] response data for flask](http://ash84.tistory.com/1101)

[2014/11/25 – [Programming/Python] – 8.18. pprint — Data pretty printer — Python 2.7.8 documentation](http://ash84.tistory.com/1082)

[2013/12/16 – [Programming/Python] – (python) daum_openapi 라이브러리 개발기](http://ash84.tistory.com/1057)

[2013/09/17 – [Programming/iOS] – (iOS) JSON문자열 NSDictionary 변환](http://ash84.tistory.com/1025)

[2013/05/14 – [Programming/iOS] – (iOS) JSONKit ARC 상에서 작업하기](http://ash84.tistory.com/967)

[2013/01/11 – [Programming/Java] – [Java] 간단 gson wrapping 하기](http://ash84.tistory.com/902)

[2012/02/18 – [Programming/Java] – [JAVA] Gson 라이브러리로 JSon 이용하기](http://ash84.tistory.com/775)
 
