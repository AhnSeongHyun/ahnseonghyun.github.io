---
title: '(Java) 싱글톤 + Map을 이용한 객체관리.'
author: 'ash84'
pub_date: '2017-04-25'
description: ''
featured_image: ''
tags: ['dev', 'Java', '객체 관리', '싱글톤', '자바']
---

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>

객체를 생성하는 일은 여간 번거로운 일이 아니다. 그냥 new 만 하면 되지 않냐고 애기하는 사람도 많겠지만, 자바에서의 new는 결국 메모리를 잡는 일이고, 명시적으로 해제를 할수 없기 때문에 객체를 계속 생성해 내는 것은 여간 꺼림직한일이 아닐수 없다.

이전에 Map을 이용해서 한번 생성된 객체를 넣어두고 가져와서 사용하는 방식에 대해서 [정선생](http://tost.tistory.com/183)님께 들은적이 있는데, 최근에 개발을 하면서 Map을 이용하면서 다른 여러 클래스에서도 해당 객체를 가져다가 쓸수 있는 방법을 생각해 보았는데, 생성된 객체를 관리하는것은 Map을 이용하되, 한번 더 싱글톤 클래스로 감싸도록 하였다. 백문이 불여일견 아래의 코드를 보자. 

일단 싱글톤 형식을 갖추고 있고 `loadService()` 함수를 통해서 필요한 서비스 객체들을 Map에 넣고 있다. 여러번 넣으면 안되기 때문에 관리하는 Map 의 사이즈가 0 일때만 넣도록 하였다. 각각의 서비스 객체들은 Service 라는 인터페이스를 구현하고 있다. `getService` 항목을 두어서 어떤 key값, 여기서는 api 이름을 받도록 하였는데, 그 이름에 따라서 필요한 객체를 리턴해 주는 방식으로 구현하였다. 

Map을 통해서 관리한다는 측면은 동일하지만 해당 관리 Map 객체를 싱글톤 클래스로 한번 감싸서 다른 여타의 클래스에서도 api 이름만 넣으면 필요한 서비스 객체를 가져올수 있도록 하였다. 
<script src="https://gist.github.com/AhnSeongHyun/4736624.js"></script>

**싱글톤 관련 링크 : [[자바에서 싱글톤을 구현하는 세 가지 방식]](http://ash84.tistory.com/837)**



