---
title: 'git feature branch 모델 프로젝트 적용기'
author: 'ash84'
pub_date: '2017-05-18'
description: '원래 사내에서 svn을 사용하고 있는데 자회사쪽과 작업을 하면서 그쪽 개발자를 구워 삶아서(홀려서) svn 이 아닌 git을 저장소로 사용하기로 하고, github 를 쓰고 싶었지만 작업자가 2명이라서 [yona H2 embedded 버전](https://github.com/yona-projects/yona)을 사용하기로 했다. 

오픈소스에 기여하거나 혹은 만들거나 할때 master 브랜치 외에 develop 브랜치 까지만 써보긴 했고, [git feature branch 모델](http://dogfeet.github.io/art'
featured_image: 'https://c1.staticflickr.com/5/4193/34289552650_3f7dbb5da4_b.jpg'
tags: ['dev', 'Git', 'github', 'branch model', 'git feature branch strategy', 'git feature branch model']
---

원래 사내에서 svn을 사용하고 있는데 자회사쪽과 작업을 하면서 그쪽 개발자를 구워 삶아서(홀려서) svn 이 아닌 git을 저장소로 사용하기로 하고, github 를 쓰고 싶었지만 작업자가 2명이라서 [yona H2 embedded 버전](https://github.com/yona-projects/yona)을 사용하기로 했다. 

오픈소스에 기여하거나 혹은 만들거나 할때 master 브랜치 외에 develop 브랜치 까지만 써보긴 했고, [git feature branch 모델](http://dogfeet.github.io/articles/2011/a-successful-git-branching-model.html)은 실제 업무에 사용해 본적은 없었다. 고도화 프로젝트에 들어가면서 git 도입과 함께 feature branch 모델로 작업하는 것을 다른 개발자에게 제안했고, 흥쾌히 받아들여서 2달동안 이 방식으로 작업하게 되었다. 

###**왜 사용하게 되었는가?** 

가장 필요하다고 느낀 이유는 아래와 같다. 

- **각각의 기능이 순차적으로 개발되거나 하나의 기능이 완료된채, 다른 기능이 개발/유지보수 되지 않는다.** 

- **차기 버전을 개발하는 도중에 운영중인 버전에 대한 긴급한 패치 등이 이루어지는 경우가 많다.**

==첫번째 이유가 제일 큰 이유이다.== 순차적으로 개발 되지 않는 이유는 아무리 제대로된 기획이나 요구사항 명세서가 있더라도 프로젝트를 진행하는 과정에서 소소한 변경들이 일어나기 마련이고, 때론 정책적인 이슈로 인해서 특정 기능의 개발이 딜레이 되는 경우가 많았다. 그런 경우에는 A 라는 기능을 개발하다가 B, C, D 기능을 병행개발 해야하는 경우가 있었다. 이런 경우에 기존에는 하나의 소스에서 작업을 하다보면 주석처리하거나 극단적으로는 디렉토리를 따로 만들어서 하는 경우도 있었다. 

### **develop-feature branch** 

![develop feature branch](https://c1.staticflickr.com/5/4182/34289552260_1b5f3d4321_z.jpg)
 
사용하면서 좋다고 확실히 느낀점은 각각의 개발하고 있는 ==기능(feature)들이 중간에 잠시 멈춤(pause) 되는 경우에 대한 두려움이 없어진다.== 예를 들면 `feature_A` 는 30% 개발하다가 기획변경으로 인해서 딜레이 된다고 하자. 그럴때 `feature_B` 를 개발할 수 있고, 이 경우 develop 브랜치에서 `feature_B` 를 따서 개발하면 되기 떄문에 `feature_A` 의 30% 개발분에 대해서 생각할 필요가 없다. 

이 경우에, `feature_B` 를 개발서버에 올려서 다른 클라이언트(앱이나 API 사용처) 테스트를 할 경우가 생길 경우, `feature_A` 의 기능에 대한 오류 없이 테스트가 진행 될 수 있다. (예를 들어 `feature_A` 가 로그인 관련 기능인데, 30% 개발된채 개발서버에 올리게 되면 문제가 생길수 있을것이다.)

필자의 경우 실제 운영레벨에서 이런 경우를 많이 겪었다. SVN 을 사용하는데 같은 소스에 다른 이슈로 2명이 수정했을 때, 철수가 30% 수정하고 커밋을 하고 휴가를 간 사이 영희가 다른 이슈로 커밋을 하고 그 소스를 실제 운영에 반영해서 장애가 난적도 있었다. (그러나 이건 비단 svn을 사용했냐, git을 사용했냐의 문제는 아니다. 오해하지마시길!) 

### **master-hotfix branch**

![master hotfix branch](https://c1.staticflickr.com/5/4156/34633681586_a0a6893f79.jpg) 

사용하면서 운영서버에 대한 핫픽스(hot fix) 건이 있었는데, 이 경우에는 git feature branch 모델에 나와있는것 처럼 `hotfix_C`를 master 브랜치에서 따서 만들고 작업해서 master 와 develop 브랜치에 모두 반영하기 쉽게 중간에 작업한 내역을 반영할 수 있었다. 

### **느낀점** 

![](https://c1.staticflickr.com/5/4155/34544211141_e2656c88a5_b.jpg)

<center>실제 커밋 그래프</center>
기존의 SVN 을 쓸 때보다는 뭔지는 모르겠지만, 소스의 버전을 유지하고 개발상의 다양한 상황에 잘 대처가 가능했다고 느꼈다. 사실 만능이라고 볼 수는 없겠지만 기본적인 모델을 가지고 각 팀이나 조직의 상황에 맞게 변경해서 사용하는 것도 좋을 것 같다는 생각이 들었다. 하지만 DVCS에 익숙하지 않은 개발자에게 이것을 설명하기란 쉽지 않겠다는 생각도 들었다.(스스로 해봐야지 편한걸 알지 않을까.)

아직도 SVN을 팀에서는 사용하고 있지만, git을 도입하는 부분에 있어서는 좀 더 기존의 개발프로세스를 보완/개선 할 수있다고 주장할 수 있겠다는 생각이 들었다. 



