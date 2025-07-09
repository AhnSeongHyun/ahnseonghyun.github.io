---
title: 'Deview2017 2일차 후기'
author: 'ash84'
pub_date: '2017-10-21'
description: '언제부터인가 Deview 를 2일 모두가는건 축복 혹은 사치가 되어버렸다. 2일 연속 신청해서 선착순 혹은 당첨되기도 어렵고, 2일 연속 회사에서 가라고 등떠밀지도 않기에 쉽지 않은일이 되어버렸다. 개인적으로 몇번째 Deview 인지는 모르겠지만 올해는 팀의 20살 막내를 데리고 참가를 하게 되었다. 개인적으로 1일차가 좀더 맞았던것 같은데 2일차만 되서 참석하게 되었다. 들었던 몇가지 세션들에 대한 느낌은 이렇다.'
featured_image: ''
tags: ['conference', 'deview2017', 'machine learning']
---

언제부터인가 Deview 를 2일 모두가는건 축복 혹은 사치가 되어버렸다. 2일 연속 신청해서 선착순 혹은 당첨되기도 어렵고, 2일 연속 회사에서 가라고 등떠밀지도 않기에 쉽지 않은일이 되어버렸다. 개인적으로 몇번째 Deview 인지는 모르겠지만 올해는 팀의 20살 막내를 데리고 참가를 하게 되었다. 개인적으로 1일차가 좀더 맞았던것 같은데 2일차만 되서 참석하게 되었다. 들었던 몇가지 세션들에 대한 느낌은 이렇다. 
 

<iframe src="//www.slideshare.net/slideshow/embed_code/key/4NJHnUNUTaybpo" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/deview/232mist-iot-80879502" title="[232]mist 고성능 iot 스트림 처리 시스템" target="_blank">[232]mist 고성능 iot 스트림 처리 시스템</a> </strong> from <strong><a href="https://www.slideshare.net/deview" target="_blank">NAVER D2</a></strong> </div>


- 조금 많이 아쉬웠던 세션인데, mqtt(emqtt를 사용한것 처럼 보인다.)에서 들어오는 IoT 기기에서 수신되는 데이터에 대한 처리를 하는 시스템을 만들었다고 했는데 사실 앞 부분에는 인터페이스에 대한 설명을 하고 뒤쪽에 백엔드에 대한 설명을 했다. 개인적으로 순서를 바꿨어야 했고, 백엔드에 좀 더 내용을 더 치중했어야 하지 않았나 싶다. 솔직히 인터페이스, UI가 아니라 프로그래밍 언어 레벨에서 클래스와 함수를 제공하는 부분은 발표주제와 빗대어 보면 부록같은 것이었는데 그렇게 많이 할애할 필요가 있었나 싶다. 그래서 앞부분을 들으면서 도데체 왜, 어디가, 어떻게 고성능이라는 거지? 하는 의문이 계속 들었다. 물론 백엔드에서 설명해주긴 했지만 많이 부족했다는 생각이 들었다. 그리고 성능 지표에서 apache flink 와 비교를 했는데, 어떤 테스트를 진행했는지가 명확하지 않다. 375배가 낫다는 설명은 충분히 의문을 들게 만드는것 같다. 개인적으로 mqtt 를 현재 프로젝트에서 사용하는 입장에서 저런 시스템이나 오픈소스가 있는것은 환영할만한 일인데 성능을 들이밀때는 좀 더 구제적이고 신중했어야 하지 않았나 싶다. 


<iframe src="//www.slideshare.net/slideshow/embed_code/key/63XWSlvuGMdNM9" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/deview/223rye-dbms" title="[223]rye, 샤딩을 지원하는 오픈소스 관계형 dbms" target="_blank">[223]rye, 샤딩을 지원하는 오픈소스 관계형 dbms</a> </strong> from <strong><a href="https://www.slideshare.net/deview" target="_blank">NAVER D2</a></strong> </div>
 
- 샤딩을 어떻게 지원하고 있는지, 그리고 그런 지원을 위해서 어떤 고민을 했는지가 흥미롭다. 기존의 CUBRID 기반에서 샤딩을 위해서 SQL routing, 확장, 정합성 관리 등등 데이터베이스 자체적으로 샤딩을 지원하기 위한 기능들이 있다. SQL 레벨에서부터 차근차근 잘 설명해주셔서 잘 들을수 있었다. 

<iframe src="//www.slideshare.net/slideshow/embed_code/key/Abgw42ZIrYDbRE" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/deview/224nsml-80881317" title="[224]nsml 상상하는 모든 것이 이루어지는 클라우드 머신러닝 플랫폼" target="_blank">[224]nsml 상상하는 모든 것이 이루어지는 클라우드 머신러닝 플랫폼</a> </strong> from <strong><a href="https://www.slideshare.net/deview" target="_blank">NAVER D2</a></strong> </div>

- 오기 전부터 언론을 통해서 `한국판 텐서플로` 라고 노출이 되면서 뭔가 개발자들에서 약간 까였던것 같은데, 발표를 들으면 텐서플로나 다른 머신러닝 플랫폼을 좀더 쉽게 쓰게 해주는 헬퍼도구라는 생각이 들었다. 그런데 중요한 점은 그런 연구자, 개발자들이 좀더 편하고 빠르게 연구, 개발할 수 있도록 한다는 점인것 같다. 이제 머신러닝 플랫폼이나 그런건 많이 나왔고 그걸 어떻게 활용할지 그리고 활용하기 위한 방법/도구들이 개발되는것 같다. 응답시간을 줄인다든지, 텐서보드를 보여준다던지, 학습된 결과를 수치가 아닌 다른 형태로 보여준다던지 하는 식으로 NSML 이 도와주는것 같다. 외부로 오픈 될지는 모르겠지만, 인상적이었다. 

<iframe src="//www.slideshare.net/slideshow/embed_code/key/5NZ43miX2CVvew" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/deview/225-80884659" title="[225]빅데이터를 위한 분산 딥러닝 플랫폼 만들기" target="_blank">[225]빅데이터를 위한 분산 딥러닝 플랫폼 만들기</a> </strong> from <strong><a href="https://www.slideshare.net/deview" target="_blank">NAVER D2</a></strong> </div>

- 약간 NSML 과 비슷하긴 하지만, 좀 더 네이버 내에서 어떻게 머신러닝 개발을 지원하고 있는지, 지원해주는 시스템에 대한 내용이다. 모르는 내용 투성이긴 한데 YARN 을 이용한다는 점 그리고 빠른 개발을 위해서 FLASK-RESTPLUS 를 사용하는 점이 인상적이다.  

<iframe src="//www.slideshare.net/slideshow/embed_code/key/wEjHfMu2QS7Ptn" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/deview/ss-80885724" title="백억개의 로그를 모아 검색하고 분석하고 학습도 시켜보자 : 로기스" target="_blank">백억개의 로그를 모아 검색하고 분석하고 학습도 시켜보자 : 로기스</a> </strong> from <strong><a href="https://www.slideshare.net/deview" target="_blank">NAVER D2</a></strong> </div>


- 1일차를 안들어서 모르겠지만, 이번 Deview 에서 가장 좋았던 세션이었다. 일단 발표력이 엄청나다. 어려운 내용을 쉽게 설명해준다. 개인적으로 여러 서비스와 서버에서 발생하는 액세스 로그(ACCESSLog)에 대해서 어떻게 수집할것인지 특히 수집포맷에 대해서 인상깊었다. Elastic Stack 을 이용하는데 무중단 롤링 업그레이드를 하고 있다고 하고 로그를 한 곳에서 모은후에 LogFlow, Hawksee 등을 만드는 부분이 인상적이었다. 역시 로그는 모아야 제맛인것 같다. 


2일차 밖에 안들어서 모르겠다. 그렇지만 확실하게 느낀것은 머신러닝/딥러닝이 바로 코 앞에 와있다는 사실이다. 물론 빅데이터가 그랬던것처럼 특정 큰 회사에서만 국한되는 이야기일수도 있겠지만, 회사에 국한되지 않는 개발자라면 새롭게 변화하는 패러다임을 지켜봐야 할 것같다. 특히 기존의 웹/API 에서 DB 로 조회했던 것들을 앞으로는 학습된 모델에게 질의하는 형태로 변경되지 않을까 하는 생각이 들었다. 
