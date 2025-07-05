---
title: 'AWSKRUG 신년 콘퍼런스 - re:Invent 특집'
author: 'ash84'
pub_date: '2017-04-03'
description: ''
featured_image: 'http://cfile1.onoffmix.com/attach/OG7xKkO6I1Rz03MmexAQnsiRQPhm1RJX'
tags: ['dev', 'aws', 'awskrug', 'aws re:invent', 'conf', '개발자 세미나', 'conference']
---

올해 첫 세미나/컨퍼런스로 **[AWSKRUG 신년 콘퍼런스 - re:Invent 특집]** 을 선택했고, 다녀왔다. AWS 를 사실 회사에서나 개인 프로젝트를 할때에도 부담되는 부분이 있어서 사용하진 않고 있지만, 앞으로는(언젠가는) 더 AWS, AZURE 등을 도입하는 방향으로 갈 것이라고 생각했기 때문에 신청하게 되었다. 

![awskrug](https://c1.staticflickr.com/1/681/32610242231_9ac0b9e403_b.jpg)

**AWS RE:INVENT 신규 서비스 정리 (윤석찬)**

- 전반적으로 새로나온 서비스에 대한 간략한 소개가 주를 이루었다. 이번 re:Invent 행사를 통해서 2일간 30여가지의 서비스를 소개했다고 하면서 lightsail, Elastic GPU for EC2, F1 Instance 등 다양한 인스턴스를 발표 했다고 한다. 기존의 EC2 만 알고 있던 나로서는 다양한 환경과 요구사하에 맞는 인스턴스가 생기는 것을 보고 발빠르게 업계에 대응하고 있다는 것을 느꼈다. 

- 인스턴스 뿐만 아니라, DB 부분도 Aurora, Athena(sql 기반으로 S3에서 질의 수행), Glue(데이터 전처리)등의 서비스를 내놨으며, 최근 각광받고 있는 머신러닝 & AI 관련해서 REKOGNITION(사진 분석, 얼굴인식/감정인식, 얼굴 비교), Polly(음성합성, TTS, SSML 제공), Lex(챗봇 만들기) 등의 서비스 출시 했다. 특히 인공지능 관련해서는 Prime Photo라고 딥러닝을 이용한 사진찾기 서비스나, Amazon Go 라고 별다른 결제 행위나 앱없이 자동으로 결제되는 오프라인 상점등을 예시로 해당 분야가 많이 발전하고 있다는 것을 느꼈다. 

![awskrug](https://c1.staticflickr.com/1/266/32610242151_076c4cdd75_b.jpg)

- 또한 Devops에 대한 부분에도 코드의 개발/배포/운영 등의 단계를 모두 관리기능에서 제공하고 있다고 한다. AWS X-RAY(호출에 대한 과정 파악, 애플리케이션 성능 파악), AWS Batch(배치 작업) 등의 서비스가 있어서, 단순히 개발, 배포 하는 단계에서 모니터링과 운영까지도 세세하게 가능해졌고, 그것들이 별개의 서비스로 분리되는 모습을 보았다. 특히 작년에 서버리스 관련해서 lambda 가 많이 신기술처럼 나왔었는데, 관련 서비스로 lambda, c# lambda, lambda edge, step functions 등의 있다고 한다. 

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>

**개발자를 위한 Amazon Lightsail Deep-Dive(정창훈)**

- 간략하게 정리하면 아래와 같다. 개인적으로 VPS 시장에 진입한 것을 환영하긴 하지만, VPS를 쓰다가 다른 서비스로 잘 넘어갈 수 있도록 지원해주는게 관건이 아닐까 싶다. 

  - 디지털 오션과 비슷한 느낌. 
  - EC2의 귀찮음, 볼때마다 헷갈린다. 요금체계가 어렵다 
  - EC2와 다르게 단순하다. 
  - 브라우저에서 ssh 접속 가능 
  - 한달에 $5
  - 무료제공 750 시간 
  - 제약 : 인스턴스 20개, 고정IP 5, DNS영역 3개 
  - 안되는 것 : 인스턴스 타입 변경, 용량 변경, 정기적인 스냅샷 
  - CLI 를 써서 자동화 해라, 스냅샷 생성
  - 현재 버지니아 리전만 가능 

![lightsail](https://c1.staticflickr.com/1/614/32610242351_94eea9940d_b.jpg)

**Amazon Athena를 통한 데이터 분석하기(김명보)**

![aws-athena](https://c1.staticflickr.com/1/751/32610242041_905d9d9a6d_b.jpg)

- managed query 서비스 
- Presto 를 기반으로 만든 서비스 
- $5/1TB 데이터 처리 
- s3 로그에 바로 쿼리 실행 

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>

**AWS Step Functions을 통한 서버리스 마이크로서비스 만들기(김현민)**

![aws-step-function](https://c1.staticflickr.com/1/340/32580069672_cbba80c805_b.jpg)

![aws-step-function](https://c1.staticflickr.com/1/548/32580070422_543cc05830_b.jpg)

- **개인적으로 가장 인상깊게 본 세션이었다.** 작년에 가장 큰 화두는 단연 서버리스였고, 그 선두에 AWS Lambda 가 있었는데, 함수 단위로 실행이 가능한다는 것만 알고 있었다. 그리고 step function을 통해서 개별의 서버리스화된 기능들이 하나의 더 큰 기능을 만들 수 있게 된것 같았다. 


![awskrug](https://c1.staticflickr.com/1/576/31890352184_689b61173f_b.jpg)

마지막 세션을 개인적인 사정으로 듣질 못했고 들어서 이 글에서 설명하지 못한 세션도 있다. 사실 AWS 를 써보지 않은 입장에서 세미나를 들으면서 이해 하지 못하는 부분도 있었지만, 2년전에 AWESOMEDAY 에서 만났던 AWS와는 많이 달라졌다는 것을 느끼게 되었다. 특히 기존의 아키텍처 상에서 서버단위로 쪼개지던 서비스들이 이제는 하나의 서비스내 구성요소/모듈 단위로 AWS의 서비스로 만드는 것을 보고 내년에는 뭐가 더 나올지 궁금해진다. 실제 프로덕션 레벨에서 언제 써 볼지는 모르겠지만, 분명한건 언젠가는 그런날이 올 것이라는 확신이 들었다. 

**References :**

- https://aws.amazon.com/ko/blogs/korea/amazon-lightsail-the-power-of-aws-the-simplicity-of-a-vps/

