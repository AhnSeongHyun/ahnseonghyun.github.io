---
title: '[Java] Vector에 대해서.'
author: 'ash84'
pub_date: '2017-04-30'
description: ''
featured_image: ''
tags: ['dev', 'fast-fail 방식', 'iterator', 'Java', 'list', 'vector', 'vector 성능', 'vector 최적화']
---

vector는  증가 가능한 객체의 배열형태( a growable array of objects)라고 자바문서에서 설명하고 있다. ArrayList와 다른 점은 capacity와 capacityIncrement 를 관리함으로써 저장용량 최적화를 시도한다는 점이다. capacity는 vector의 용량인데 개발자가 지정할 수 있다.  capacityIncrement 은 capacity가 증가하는 단위이며, 초기 생성시 capacity는 10으로 지정되어 있다. 

capacity가 절대 vector 내 들어가있는 component의 수 보다 클수가 없는데, capacity보다 커질때 미리 capacity를 조정해 준다면 vector의 사이즈가 변경될때의 재할당(re-allocation)을 최소화 할수 있다고 한다. 
 
vector 내부의 component 증분에 따른 capacity의 변화를 테스트해 보았다.

<script src="https://gist.github.com/4387524.js"></script>

보시는것과 같이 1, 2, 4, 8, 16, 32 이런식으로 증가되는 것을 알 수 있다.  

vector는 기본적으로 List 인터페이스를 구현하기 때문에 iterator 를 사용할 수 있는데, iterator는 **fast-fail방식**으로 동작한다고 한다. **[fast-fail 이란, 순차적 접근이 끝나기 전에 콜렉션 객체 자체에 변경(ex.remove()) 이 일어나는 경우, 순차적 접근이 실패하면서 ConcurrentModificationException 가 발생되는것을 말한다.](http://lng1982.tistory.com/95)** 좀더 자세한 사항은 [링크](http://lng1982.tistory.com/95)를 참고하시면 이해가 빠를것 같다.
 



