---
title: '#주간개발기, 3월 첫째주'
author: 'ash84'
pub_date: '2013-03-09'
description: '**exs4j**
– DB에 OpenAPI를 이용한 검색 결과를 저장하는 것은 되었고, 저장된 검색 결과의 빠른 검색을 위해서 [exs4j](https://github.com/AhnSeongHyun/exs4j) 내에 올려서 유지할 인덱스를 만드는 작업을 하였다. 기존의 [espressoOtr](https://github.com/AhnSeongHyun/espressoOtr) 라이브러리 내에 Canister/S'
featured_image: ''
tags: ['espressoOtr', 'exs4j', 'INDF', '개발자', '아이폰 앱', '오픈소스', '주간개발기']
---


<span style="font-size: 11pt;">**exs4j**</span>

<span style="font-size: 11pt;">– DB에 OpenAPI를 이용한 검색 결과를 저장하는 것은 되었고, 저장된 검색 결과의 빠른 검색을 위해서 [exs4j](https://github.com/AhnSeongHyun/exs4j) 내에 올려서 유지할 인덱스를 만드는 작업을 하였다. 기존의 [espressoOtr](https://github.com/AhnSeongHyun/espressoOtr) 라이브러리 내에 Canister/Shelfer 를 통해서 구현하려고 했는데, 약간 기능이 미흡한 부분이 있어서, Shelfer+Map<String,List> 형태로 인덱스 구조를 잡았다. 그렇게 해서 하나의 검색 결과에 대한 requestCode(유일하게 구분되는 검색 요청 코드)와 검색어를 저장하는 부분까지는 되었다. 해당 부분을 Barista 라고 하는 싱글턴 클래스로 감싸면서 Barista 클래스를 통해서 검색어와 requestCode 를 넣고 빼오는 작업을 할 예정이다.</span>

<span style="font-size: 11pt;">**[espressoOtr](https://github.com/AhnSeongHyun/espressoOtr)**</span>

<span style="font-size: 11pt;">– [exs4j](https://github.com/AhnSeongHyun/exs4j) 로 인해서 기존의 단일 Canister/Shelfer 구조를 다양한 형태로 만들었다. Shelfer의 구조는 거의다 비슷한데 Canister 안에서 List 를 쓰느냐 Map을 쓰느냐, Map에서도 value를 어떤 데이터 타입으로 가지냐에 따라 나누도록 하였다. 사실 좀 아쉬운 부분이긴 한데, 하나의 Shelfer 에서 Canister 인터페이스를 가져와서 사용하는 식으로 했었어야 했는데 그 부분이 좀 아쉽다. 차후에 개선할 방향이기도 하다. [exs4j](https://github.com/AhnSeongHyun/exs4j)에 우선적으로 쓰일 MutlMapShelfer, MultiMapCanister 에 대해서는 단위테스트를 작성해서 다양한 버그 및 스페에 못 미치는 부분을 수정하였다. 여타의 다른 Canister/Shelfer도 단위 테스트를 작성해야겠다. </span>

<span style="font-size: 11pt;">– [HtmlExtractor](http://ash84.tistory.com/943)를 만들었는데 이유는 개인적인 여러가지 작업을 해 보니 Html 파싱을 하는 부분이 많았는데 jericho 파서를 사용하는 부분에서 좀더 쉽고 나에게 맞게 사용하고자 static 함수로 빼서 작성하였다. </span>

<span style="font-size: 11pt;">**아이폰 앱**</span>

<span style="font-size: 11pt;">– 지난주의 작업하고 있던 앱에 대해서 평일에 올렸더니 24시간 만에 연락이 왔다. 또 리젝이 되었다. 문제가 있나 보다. 메모리가 죽는다고 하고, 네트워크 쪽에 문제가 있는것 같다는 생각이 들었다. 네이버 추천검색어+뉴스를 가져오는 부분에서 아이폰이 힘들어 하는 느낌이었다. </span>

<span style="font-size: 11pt;">– 위의 오류를 해결 하고자, 팀(INDF)내 서버에  해당 역할을 하던 부분은 아이폰에서 떼어내서 자바로 작성해서 JSON으로 리턴해주는 방식으로 변경해서 올렸고 테스트는 마친 상태이다. 아직 아이폰 앱에 대한 수정은 끝나기 않았지만 다음주 평인 중에 올려서 심사를 다시 받을 예정이다. </span>

<span style="font-size: 11pt;">**INDF 팀 작업**</span>

<span style="font-size: 11pt;">– netty를 이용해서 http 통신을 받아서 처리할 수 있는 부분을 정선생님과 같이 하는 프로젝트에서 작업을 하고 대략 반영을 하였다. 이 작업을 하면서 ChannelPipeline 에 대한 의문이 생겼고 해당 부분에 대해서 공부하고 정리해서 블로그에 올렸다.([여기](http://ash84.tistory.com/945)) 작업을 하면서 점점더 netty 라는 프로젝트에 대해서 호감이 간다. 굉장히 잘 만들었다는 생각도 들었고, 사이트 및 주석을 통해서 지원하고 있는 부분 역시 매력적인것 같다. </span>

<span style="font-size: 11pt;">**StackOverflow 지원**</span>

<span style="font-size: 11pt;">– netty 에 대한 [stack overflow에 질문](http://stackoverflow.com/questions/15180150/reading-xml-data-in-netty-3-6-x/15214867#15214867)이 올라와서 영어로 답변을 달았다. 조금 쑥스럽긴 하짐나 내 나름대로 아는 부분에 대해서 설명해 주었다. 질문인즉, XML 메시지 형태로 Netty를 통해서 주고 받고 하려고 하는데 변환 부분(마샬링)을 물어보는것 같아서 exs4j에서 했던 작업을 토대로 decoder, encoder 작성하고 그 안에서 JAXB로 당신이 쓸 자바 클래스로 변환해 주라고 답변을 달았다. 별 다른 답변 채택을 안해주긴 했는데, 종종 달아야 겠다는 생각이 들었다. 실제로 여러가지 이슈를 보면서 netty 에 대해서 새롭게 알게되는 부분이 많아서 좋았다. 특히 beta4.x 를 내놓으면서 많은 분들이 테스트해 주시고 버그나 문의를 stack overflow에 하고 있는것 같았다. </span>

<span style="font-size: 11pt;">전반적으로 이번주는 [espressoOtr](https://github.com/AhnSeongHyun/espressoOtr) 쪽 작업이 많았는데 그 이유는 단연 [exs4j](https://github.com/AhnSeongHyun/exs4j)의 인덱스 작업을 위해서 였다. 아직 반 밖에 완성하진 못했지만 다음주에는 일단 [exs4j](https://github.com/AhnSeongHyun/exs4j) 현재 구조에 대해서 상세하게 그려보는 시간을 가질 것 같다. 그리고 나서  인덱스에서 가져와서 DB 에서 검색결과 가져오는 부분을 구현 해봐야 할것 같다. </span>



