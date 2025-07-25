---
title: 'tidy first를 읽고 난 생각과 감정들'
author: 'ash84'
pub_date: '2024-05-08'
description: '나중에 다시 보기 위해서 책에 있는 문장들을 그대로 가져온 부분이 있기 때문에 읽고 있는 분, 혹은 읽을 예정인 분들은 보지 않으시길 추천합니다. 

> 코드를 정리하는 일이 반드시 보고해야 하고 추적하고 계획, 일정을 잡아야하는 일이 되어서는 안 됩니다. 특정 코드를 변경해야하는데 코드가 지저분해서 변경하기 어려울 때, 먼저 코드를 정리하는 것입니다. 일상적인 업무이자, 생각하면서 개선하는 절차입니다. 


동료가 했던 말이 생각났다. "리팩토링은 항시 해야 한다." 리소스를 들여서, 받아야만 하는게 아니라. 그러나 리팩토링에 대'
featured_image: ''
tags: ['Developer', 'tidy first', 'dev', 'tidy-first']
---

나중에 다시 보기 위해서 책에 있는 문장들을 그대로 가져온 부분이 있기 때문에 읽고 있는 분, 혹은 읽을 예정인 분들은 보지 않으시길 추천합니다. 

> 코드를 정리하는 일이 반드시 보고해야 하고 추적하고 계획, 일정을 잡아야하는 일이 되어서는 안 됩니다. 특정 코드를 변경해야하는데 코드가 지저분해서 변경하기 어려울 때, 먼저 코드를 정리하는 것입니다. 일상적인 업무이자, 생각하면서 개선하는 절차입니다. 


동료가 했던 말이 생각났다. "리팩토링은 항시 해야 한다." 리소스를 들여서, 받아야만 하는게 아니라. 그러나 리팩토링에 대한 부정적인 인식, 매우 큰 구조를 변경하는 일이고, 문제가 생길 수 있고, 임팩트가 제로다라는 인식은 여전히 존재한다. 대부분 개발자가 리팩토링을 해야한다고 소리칠 때는 들어주지 않다가 제품에 문제가 생기면 그때서야 하자고 한다. 그 사이에 고객은 떠나가기도하고. 물론 조금만 어려우면 리팩토링  카드처럼 꺼내는 개발자도 있긴하다.(어딜 어떻게 할지는 애기하지 않는다.) 그래서 그런지 그 동료가 애기했던 리팩토링를 항시 해야한다는 의견에 나 자신도 많이 동의하고 있었다. 

그렇지만 그 역시 회사일이라서, 누군가에게 의무처럼 지우긴 어렵웠다. 그래서 오히려 책에 있는 코드정리라는 단어가 덜 부담스럽게 다가왔다. 

> 코드 정리는 작은 리팩터링으로 누구도 싫어할 수 없을 정도로 사랑스럽고 포근합니다. 

느끼는 감정이 달랐다. 거대한 산을 움직이는게 아닌 놀이터에서 작은 모래성을 뿌수고 다시 만드는 느낌. 매일 자주 할 수 있을것 같은 느낌이 이 문장을 보고 들었다. 코드 정리를 한게 언제였나 싶었다. 구현을 하기에, 밀려드는 버그와 일을 쳐내기에 급급하진 않았나. **스스로 스스로에게 미안해졌다. 나라는 프로그래머를 사랑하지 않고 있었다는 생각이 들었다.** 

> 코드를 정리할 때 한번에 처리하는 규모를 작게 할 것을 권했습니다. 
> ...
> 한 번의 코드 정리에 한 시간 이상이 걸린다면, 이는 원하는 동작변경을 위해 필요한 최소한의 구조변경 시기를 놓쳤다는 의미일 수 있습니다. 
> 

코드 정리를 하다보면 책에서도 나와 있듯이 연쇄적으로 하게된다. 약간 빠져든다는 표현이 좀 더 맞는것 같다. 마치 todo 리스트에 1번을 하고 2번을 해야하는데 1-1, 1-2, 1-3을 계속 해나가는 느낌들을 받았다. 책에서는 그 기준을 한시간 이내정도로 가이드 해주고 있다. 물론 상황에 따라서 다르겠지만 시간을 체크해보는 것도 좋을것 같다. 

동작변경과 구조변경을 분리하라는 이야기도 나온다. 코드정리가 결국 내부 구조를 변경하거나 하면서 동작을 변경하게 되고 또 구조를 변경하게 되는것 같은데 그리고 그것들이 현실세계에서 하나의 PR로 다른 개발자들에게 강요하는게 아닌가하는 과거의 나의 모습이 생각이 났다. `내가 이만큼 수고 했으니 어서 approve를 해달라.` 이런식 

그리고 코드 정리가 좋지만, 코드를 정리해야할 시점, 정리하지 미루어야할 시점에 대해서도 언급을 하고 있다. 코드 정리를 하는게 좋지만 미루어야 할 시점들이 있는데 그런 부분이 이제까지는 조금 경험적으로 알고 있었고, 사내에 다른 개발자들에게 가이드 하기 어려운 부분이었는데 책으로써 잘 정리해준것 같다. 

> 오늘 우리가 하는 설계는 내일의 동작변경을 구매하는 옵션에 대해 지불하는 프리미엄입니다. 

설계를 왜 해야하는가? 에 대한 좋은 답변이라는 생각이 들었다. 특히 스타트업에서 **설계라는 단계에 대해서 투입되는 시간의 양에 대해서만 기회비용으로 측정을 한다.** 예를 들어, 설계할 시간에 개발을 더 빨리해서 출시를 더 빨리 하는게 좋다는 식, 물론 비지니스라는 단어 앞에 장사가 없지만 설계라는 것을 비지니스적으로 해석해 준 부분에서 매우 인상적이었다. 


> 코드 정리의 차원에서 코드와 자신과의 관계에 대해 이야기하고 있기 때문에 코드 정리를 먼저하면 이후의 행동변화가 더 즐거워 진다는 이유로 코드 정리를 먼저할 수 있습니다. 이런한 자기관리로서의 코드 정리는 어느정도 정당화 될 수 있습니다. 다만, 경제적인 인센티브에 반하는 행동을 하고 있을수도 있다는 사실을 항상 인식하세요.

코드정리를 하기 위해서, 혹은 리팩토링을 하기 위해서 일정 미뤄달라 혹은 리소스를 달라는 개발자도 있었다. 설계와 구조가 중요하지만 때로 아직 사용자가 없고 출시도 안한 상태에서 코드정리, 리팩토링만 하려고 하는 개발자를 보면 조금 답답하긴 하다. 

> 비싼 프로그램에는 모두 한가지 공통점이 있다는 것을 발견했습니다. 한 요소를 변경하려면 다른 요소도 변경해야한다는 것이죠. 반면 저렴한 프로그램은 좁은 범위의 코드변경만 필요한 경향이 있었습니다. 그들은 이 변경감염 특성을 결합도라고 불렀습니다. 

> 결합도는 소프트웨어 비용을 결정합니다. 

비싼 프로그램을 언젠가 적정가격으로 내려앉히는 작업(리팩토링)을 해야하는데 그건 언제 해야하는 걸까? 아니면 지속적인 코드정리를 통해서 가능한걸까? 

> 제 믿음 중에서, 증명하거나 적절하게 설명할 수 없는 것이 하나 있습니다. 한 종류의 코드 변경에 대한 결합돌를 줄일수록 다른 종류의 코드 변경에 대한 결합도가 커진다는 것입니다. . 이것이 의미하는 실질적인 의미는 모든 결합을 다 색출하듯 없애려고 애쓰지 말아야 한다는 것입니다. 그렇게 해서 만들어진 결합도는 그만한 가치가 없습니다. 

> 하지만 가장 중요한 것은 바로 여러분입니다. 코드를 정리하면 평화, 만족, 기쁨을 느끼면서 프로그래밍을 할 수 있을까요? 그럴수도 있습니다. 이것이 중요한 이유는 여러분이 최상의 상태에서 주체적으로 일할 때, 더 나은 프로그래머가 될 수 있기 때문입니다. 항상 시간에 쫓기며 고치기 힘든 코드를 변경하느라 고통속에 있다면 최상의 상태가 될 수 없습니다. 

>코드 정리에 너무 집착하지 마세요. 코드 정리를 하면서 자신의 삶과 업무가 더 나아질 수 있다는 사실을 깨닫고 나면, 때때로 들뜬 기분에 휩싸여 코드 정리가 제일 우선이라고 생각할 수 있습니다. 일반적으로 코드를 다룰 때 기능 변경에 대해서라면 자신이 옳다고 생각하는 일을 해도 사람들이 불만을 가질 수 있는 위험과 불확실성을 지닙니다. 반면에 코드 정리에 영향을 받을 사람은 바로 나 자신이기 때문에 만족할 가능성이 매우 높습니다. 

코드 정리라는 주제로 tidy first를 일주일만에 읽었다. 사실 작은 책이라 쉽게 읽히긴 했지만 리팩토링이 아닌 코드정리라는 작고 소중한 무엇인가를 선물받은 느낌이다. 
켄트 백의 다음 책들이 기대된다.

<center>
<iframe src="https://coupa.ng/chcE4v" width="120" height="240" frameborder="0" scrolling="no" referrerpolicy="unsafe-url" browsingtopics></iframe>
</center>

<small>이 포스팅은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받습니다.</small>
