---
title: 'chatfuel 이용 간단하게 챗봇 만들기'
author: 'ash84'
pub_date: '2017-07-04'
description: '실용주의 머신러닝 스터디 과제를 하면서 챗봇을 만들수 있는 여러 프레임워크나 도구들을 알게 되었는데 그 중 하나가 chatfule 이었다. bot framework 는 azure를 가입해야하는 부담감이, api.ai는 gcp를 이용해야 하는것 같았다. 기존에 쓰던 개인 서버에서 돌려보고 싶었고 비교적 간단한 [chatfuel](https://chatfuel.com) 을 이용하게 되었다. 

일단 [chatfuel](https://chatfuel.com) 은 현재 페이스북 메신저와 텔레그램 봇을 지원하고 있는데, 페이스북 메신저로 연'
featured_image: 'https://chatfuel.com/images/chatfuel_fb.jpg'
tags: ['chatbot', 'chatfuel', '챗봇']
---

실용주의 머신러닝 스터디 과제를 하면서 챗봇을 만들수 있는 여러 프레임워크나 도구들을 알게 되었는데 그 중 하나가 chatfule 이었다. bot framework 는 azure를 가입해야하는 부담감이, api.ai는 gcp를 이용해야 하는것 같았다. 기존에 쓰던 개인 서버에서 돌려보고 싶었고 비교적 간단한 [chatfuel](https://chatfuel.com) 을 이용하게 되었다. 

일단 [chatfuel](https://chatfuel.com) 은 현재 페이스북 메신저와 텔레그램 봇을 지원하고 있는데, 페이스북 메신저로 연결했다. 봇을 생성하고 나면 일단 페이스북 페이지와 연결하라는 메시지가 뜬다. 페이지를 생성하거나 기존에 사용하던 페이지의 계정으로 연결하고 테스트를 하면 해당 페이지에서 본인 페이스북 계정으로 메시지를 보내준다. 

![chatfuel](https://farm5.staticflickr.com/4054/35641348816_215af49b06_k.jpg)


[chatfuel](https://chatfuel.com) 은 비교적 쉽게 챗봇을 만들 수 있고, 프로그래밍을 잘 못하는 사람이라도 block 이라는 단위를 이용해서 텍스트, 이미지, 타이핑 등의 액션드를 줄 수가 있다. 여러 block 들을 엮는 작업도 가능하다. 

![chatfuel](https://farm5.staticflickr.com/4050/35550468801_03a1f6ecda_b.jpg)

![chatfuel](https://farm5.staticflickr.com/4215/35550469351_d98ae4c057_b.jpg)


개인 서버프로그램과 연결 하려면 항목중에 JSON API를 선택하면 되는데  GET 과 POST 모두 지원하며 챗봇의 사용자 정보등을 받을수 있다. 또한 에러 메시지도 띄울수 있도록 지원하고 있다. 특이한건 사용자의 입력값, 즉 사용자가 타이핑한 메시지를 받기 위해서는 USER INPUT 타입의 block을 만들어야 하고, 그 안에서 어떤 변수로 받을지를 설정해야 한다. 그리고 다시 JSON API block 에서 설정한 메시지 변수가 요청 파라미터로 전달됨을 지정해야 한다. 

![chatfuel](https://farm5.staticflickr.com/4209/34839849944_9a3a601252_b.jpg)

![chatfuel](https://farm5.staticflickr.com/4068/35550469301_be47b67a2c_b.jpg)

[chatfuel](https://chatfuel.com) 자체는 정말 잘 만든 플랫폼이라는 생각이 들었다. 그리고 아직까지는 무료이다. 개발자 뿐만 아니라 비개발자도 쉽게 자신의 목적에 맞는 챗봇을 만들수가 있다. 이미지, 동영상 등도 보낼수 있고, 버튼도 설정할 수가 있다. 간단하게 만드는 용도로 괜찮을것 같다는 생각이 들고, 보다 많은 메신저들을 지원했으면 하는 바램이다. 


