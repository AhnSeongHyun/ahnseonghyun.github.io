---
title: 'flask HTTP 에러 따로 메일로 받기'
author: 'ash84'
pub_date: '2016-08-15'
description: '200 OK외에 다른 부분에 대해서 메일로 에러를 받아야 하는 경우가 있다. 물론 500 Server Internal Error 의 경우에는 로그를 보는게 제일 빠르지만, 저렇게 메일로 남기는 이유는 어떤 ip 에서 잘못된 접근을 하는지 보기 위해서 이다. 아래의 코드는 별다른 메일 서버 없이 리눅스 자체에 있는 sendmail 바이너리를 이용해서 호출하는 소스이다. 오히려 s'
featured_image: ''
tags: ['dev', 'FLASK', 'http', 'Sendmail', '간단 메일 보내기', '메일']
---


<script src="https://gist.github.com/AhnSeongHyun/c8ec7952d3874eaf9a57.js"></script>
 
200 OK외에 다른 부분에 대해서 메일로 에러를 받아야 하는 경우가 있다. 물론 500 Server Internal Error 의 경우에는 로그를 보는게 제일 빠르지만, 저렇게 메일로 남기는 이유는 어떤 ip 에서 잘못된 접근을 하는지 보기 위해서 이다. 아래의 코드는 별다른 메일 서버 없이 리눅스 자체에 있는 sendmail 바이너리를 이용해서 호출하는 소스이다. 오히려 smpt 서버 설정하고 그런것 보다 이렇게 간단하게 관리자용 메일링을 쓸때에는 sendmail 이 더 나은것 같다. 

<script src="https://gist.github.com/AhnSeongHyun/8643e89b82cd2ca01469.js"></script>



