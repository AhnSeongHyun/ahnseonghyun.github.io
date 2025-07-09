---
title: '(stackoverflow) how to improve select performance in mysql?'
author: 'ash84'
pub_date: '2013-07-08'
description: 'StackOverflow 를 자주 이용해 오진 않았지만 최근에는 다른 개발자들의 이야기를 들어 보기 위해서 내가 해결한 어떤 문제라고 할지라도 올려서 물어보고 있다. 영어 공부가 된다고 생각하지는 않지만 물어보기 영어 레벨은 올라갈듯. 결국 검색도 실력. 


# [how to improve select performance in mysql?](http://stackoverflow.com/ques'
featured_image: ''
tags: ['dev', 'fulltext index', 'Index', 'MySQL', 'select performance', 'stackoverflow', 'text type', 'varchar']
---


<span style="font-size: 11pt;">StackOverflow 를 자주 이용해 오진 않았지만 최근에는 다른 개발자들의 이야기를 들어 보기 위해서 내가 해결한 어떤 문제라고 할지라도 올려서 물어보고 있다. 영어 공부가 된다고 생각하지는 않지만 물어보기 영어 레벨은 올라갈듯. 결국 검색도 실력. </span>


# [<span style="font-size: 24pt;">how to improve select performance in mysql?</span>](http://stackoverflow.com/questions/17513090/how-to-improve-select-performance-in-mysql)

<div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">제목 그대로다. 어떻게 하면 select 성능을 향상 시킬수 있을까? 링크에 들어가서 보면 알겠지만 물어본 것은 한마디로 애기하면 100만건이 넘는 데이터가 있는 테이블에 블로그 주소와 이미지 주소들이 저장되어 있는데 블로그 주소에 대한 이미지 주소를 select 를 했더니 38건에 6.37 초가 걸렸다. 나는 1sec 이하로 select 되어야 하기를 원한다. index를 잡아야 할까? 아니면 테이블을 정규화 해야할까? 너희들의 팁을 듣고 싶어. </span></div><div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">사실 답은 index 잡는것이었다. 이미 어느정도 index가 필요하겠다는 생각을 가지고 있었지만 다른 개발자한테 물어본 것이다. 각각 여러가지 답변들이 달렸는데. </span></div><div style="text-align: justify; line-height: 2;"></div>> <div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">– index 를 잡아라. </span></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">– 니 테이블에 [fulltext 인덱스](http://www.petefreitag.com/item/477.cfm)를 추가해라. </span></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">– text 말고 varchar 를 써라. </span></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">– explain 으로 실행계획을 올려바라. </span></div>

<div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">결국에는 index를 잡으라는 이야기였고, [Curt](http://stackoverflow.com/users/1754010/curt) 라는분이 명확하게 올려주셨다. </span></div><div style="text-align: justify; line-height: 2;"></div>> <div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">– link 컬럼에 대한 인덱스가 문제를 해결할거다. 너가 수행한 쿼리는 디스크에서 로드한 테이블부터 100만건을 모두 필요로한다. 그걸 또 string 값과 비교를 한다. index를 잡게 된다면, 디스크 리드를 줄일수 있을것이다. </span></div><div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">– 또한 text 타입을 테이블과 별도로 저장이 되는데 이게 또 비효율적이다. 두개의 text 컬럼에 대해서 varchar(300)으로 하기를 권장하고, 이정도면 URL 정도는 커버할수 있을것이고, 저장도 더 효율적으로 될것이다. text 타입은 메모나 웹 페이지 컨텐츠 담을때나 써라. </span></div>

<div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">[Curt](http://stackoverflow.com/users/1754010/curt) 님의 말씀을 잘 들었는데, 이후에 데이터 테이블 구조에서 형을 text 에서 varchar(300)으로 두고 다시 쿼리를 날렸을때 기존의 6.37 초에서 17.1 밀리초로 단축되는 것을 확인하였다. </span></div><div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">사실 text 형을 사용한 이유는 간단한데, 어플리케이션에서 넣어줄때 원래는 100글자였는데 한글 URL 이 들어갈때 utf-8로 변경되면서 들어가는 문자열이 엄청 길어지는 문제가 생겼다. 200을 늘려도 생기길래 가늠할 수 없어서 text로  설정했는데 이런 불상사가 생길줄이야. </span></div><div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt;">index 는 별도의 공간이 필요하긴 하지만 where 문에서 걸어야 하는 조건 컬럼이라면 index로 설정하는 것을 반드시 고려해봐야 한다는 생각이 들었고, 다른 분들이 애기해준 fulltext 인덱스에 대해서도 한번 봐야 할것 같다. text 타입은 별도로 저장된다는 것을 듣긴 했으나 한번더 어떤식으로 저장되는지 알아봐야겠다. </span></div><div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"></div><div style="text-align: justify; line-height: 2;"></div>

