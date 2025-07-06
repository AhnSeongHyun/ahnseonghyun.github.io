---
title: 'Akiflow 도입 및 활용후기'
author: 'ash84'
pub_date: '2025-01-31'
description: '리더로써 일을 하면서 생산성 향상에 전 직장에서부터 고민이 많았다. 그때 읽었던 책이 [MakeTime](https://link.coupang.com/a/ccn0Lj)이라는 책이었는데, 하루에 가장 중요한 한 가지 일(Task)을 완수하라는 내용으로 지금까지도 이 내용을 지키고 있다.  하지만 CTO, Head of tech로 일을 하면서는 정말 정신없이 일을 하게 되었다. 특히 회사/도메인의 특성상 스타트업이고, 고객들로부터 빠르게 요청을 처리해야하는 경우도 있다보니 정신이 없었고 일이 정리가 안되는 느낌이었다. 그래서 좀 더 실'
featured_image: 'https://s3.ap-northeast-2.amazonaws.com/static.ash84.io/images/blog/akiflow-adoption-utilization/image.jpg'
tags: ['akiflow', 'JIRA', 'productivity', 'todoist']
---

리더로써 일을 하면서 생산성 향상에 전 직장에서부터 고민이 많았다. 그때 읽었던 책이 [MakeTime](https://link.coupang.com/a/ccn0Lj)이라는 책이었는데, 하루에 가장 중요한 한 가지 일(Task)을 완수하라는 내용으로 지금까지도 이 내용을 지키고 있다.  하지만 CTO, Head of tech로 일을 하면서는 정말 정신없이 일을 하게 되었다. 특히 회사/도메인의 특성상 스타트업이고, 고객들로부터 빠르게 요청을 처리해야하는 경우도 있다보니 정신이 없었고 일이 정리가 안되는 느낌이었다. 그래서 좀 더 실질적으로 나에게 도움이 되는 수단을 찾고 싶었다. 

## 왜 도입했나? 

일단 왜 도입했냐를 애기하기 전에 배경 상황을 먼저 설명을 해야하는데 내가 회사에서 쓰는 툴들은 다음과 같다. 

- 구글 캘린더 : 일정/미팅/회의 
- jira : 할일 관리 
- 노션 : 문서 
- 슬랙 : 실시간 소통 
- 이메일 : 외부 소통 창구 

사실 이건 회사에서만 쓰는 툴들이다. 나라는 개인을 보면 기본적으로 2가지 역할(role)을 가지고 있다. 하나는 직장인/리더/개발자 다른 하나는 가족 구성원/개인으로써의 나이다. 하지만 나에게 주어진 시간은 24시간 밖에 안되고 나는 회사 일을 하면서 나를 챙기고 가장으로써 가족을 챙겨야 한다. 

예전보다 힘든건 이제는 쓰는 모든 툴들에서 요청들이 온다는 것이다. 예를 들면 구글 캘린더로 미팅 요청을 받고, jira로 할일/개발거리를 요청 받고, 슬랙으로 업무처리를 요청받고, 이메일로 외부 업체에서 요청을 한다. **결국 핵심은 요청관리(requirement management)를 어떻게 할 수 있느냐다. **

### 여러가지 시도들 

다 기억나진 않지만 짧게는 한달 길게는 몇달이상 시도해봤던 것들을 정리해봤다. 지극히 주관적인거라서 도움이 될지는 모르겠지만.

**회사와 개인 캘린더 분리**

  - 이 시도는 아마 캘린더를 깔끔하게 쓰고 싶어서였던것 같다. 개인은 개인 캘린더에서 회사는 회사 캘린더에 이메일도 마찬가지. 개발자스럽게 뭔가 컨테이너에 가두고 싶었던것 같은데. 결과적으로는 실패했다. 

  - 실패한 이유는 이메일은 받는 창구여서 상관 없는데, 캘린더는 내가 미팅을 잡을때 이 전환이 쉽지가 않았다. 특히 구글 캘린더를 분리하려면 구글 계정을 분리해야하는데, 크롬에서 구글 계정을 인식해서 들어가다보니까 여간 전환이 귀찮은게 아니였다.

**[Todoist](https://www.todoist.com/ko) 도입**


![todoist](https://s3.ap-northeast-2.amazonaws.com/static.ash84.io/images/blog/akiflow-adoption-utilization/Todoist_logo.png)

- 사실 회사일들은 도구들이 있었는데 개인 Task 관리 도구가 없었다. 그래서 예전에도 잘 사용했던 Todoist를 사용했다. 개인적인 일만 사용하다 보니, 결과적으로 툴이 하나 더 늘어났고 컨택스트 전환이 더 많이 일어났다. 그리고 개인 Task만 적는게 Todoist까지 필요한가 싶었다. 


**Jira Private Project 사용** 

  - 리더로 일을 하면서 느낀점 중 하나가 일반적인 작업이나 개발관련된 부분은 Jira에 남기기 편한데 비공개적인 업무를 남기기가 불편했다. 예를 들면, 보안 관련 사항이나 그런 부분은 public한 jira에 남기기가 애매했다. 그래서 나만 쓰는 비공개 Jira project를 만들어서 사용했다.

  - 이 방식은 꽤 괜찮았다. Jira 자체에 너무 익숙해져있기도 했고, 일단 다른 개발 요청들도 대부분 Jira 받다보니 나쁘지 않았다. 하지만 이것도 몇개월가진 못했다. 

  - 지금은 이 방식을 사용하지 않는데, 이유는 회사 툴에 개인적인 일을 쓰는게 너무 마음에 걸렸다. 장보기, 미용실 예약 이런것을 굳이 jira에 쓸 이유가 있을까? 나중에 누가 볼수도 있지 않을까하는 생각도 들어서 그만두었다. 

**[sunsama](https://www.sunsama.com/) 도입**  
  -  이 툴도 꽤 오래 썼었는데, jira, todoist, notion, gmail 등 대부분의 툴들을 연결해서 쓸 수 있었다. 개인적으로 꽤 만족했었는데 잘 안쓰게 된 이유는 어떻게 보면 Akiflow로 넘어온 이유라고도 볼 수 있는데, 시간 확보를 위해서 [타임박싱(time-boxing)](https://asana.com/ko/resources/what-is-timeboxing) 내 스케쥴에 도입하게 되면서 Akiflow 캘린더 중심적으로 좀 더 편하다는 생각이 들었다. 


**[Akiflow](https://akiflow.com/) 도입**

![akiflow](https://s3.ap-northeast-2.amazonaws.com/static.ash84.io/images/blog/akiflow-adoption-utilization/akiflow.png)

  - integrations가 잘 되는 부분이 가장 좋았지만 사실 내가 오늘 Task을 Inbox에서 가져오고 그것을 캘린더에 넣음으로써 시간을 할당하고, 그게 다른사람으로부터의 일정/미팅 요청으로부터 보호가 되고 활용할 수 있는 시간이 늘어나는 느낌이었다. 

## 어떤 점이 도움이 되었나? 

- Inbox : 하루에도 수많은 요청을 여기 저기서 받는다. 예를 들면, 회사 카페테리아에서 요청을 받는다. 그러면 나는 그것을 기억해야하는데 jira는 너무 느리다. akiflow는 쉽게 바로 inbox에 넣을수 있다. 그리고 슬랙에서 요청이 오면 내가 지금 다른 작업을 하고 있을때는 처리 못하지만, Later를 걸어놓으면 자동으로 Akiflow Inbox에 들어간다. 

- Projects : 프로젝트를 만들수 있는 기능이 있다. 앞에서 말한 내가 겪고 있었던 회사와 개인 일에 대한 분리를 나는 Projects를 통해서 하고 있다. 그래서 slack에서 들어온 요청을 회사 프로젝트로, 개인적으로 해야하는일은 별도의 프로젝트로 넣고 있다. 개인 Task들도 프로젝트로 분류를 해서 넣고 있다. 예를 들면 사이드 프로젝트, Finance 와 같이 약간의 중요도가 다른것들을 프로젝트 별로 분류해서 넣고 있다. 

  ![projects](https://s3.ap-northeast-2.amazonaws.com/static.ash84.io/images/blog/akiflow-adoption-utilization/projects.png)

- Calendar : Task가 만들어지면 그것들을 언제 실행할지를 정해야한다. **보통 나는 이 작업을 1~2일전에 배치작업을 진행한다.** 캘린더 상에서 내가 할일을 해당 시간에 옮겨 놓음으로써 해당 일을 하는 시간을 확보할 수 있다. 이렇게 하니 좋은점 2가지를 발견했다. 

  ![calendar](https://s3.ap-northeast-2.amazonaws.com/static.ash84.io/images/blog/akiflow-adoption-utilization/full.png)
  
    **첫번째, 시간이 잡혀 있기 때문에 다른 사람의 일정/미팅 요청을 거절 할 수 있다.** 구글 캘린더 기반의 회사를 다녀보면 알겠지만 논의를 하기 위해서 내가 비워둔 일정에 계속 미팅/회의를 요청한다. 그렇게 되면 나는 일을 할 시간이 없다. 그러나 일정을 채우고 내가 그 일정에 내 할일을 하면 방해받지 않는다. 
  
   **두번째, 해당 Task를 비공개 또는 공개로 할 수 있기 때문에 비공개 관련 일도 잘 관리할 수 있다.** 개발 관련된 일만 하지는 않고, 사람관리, 리소스 관리를 할 때가 있는데 그런것들이 공개되는 건 개인적으로 불편하다. 그런데 Akiflow에서는 해당 Task를 캘린더에서 공개로 할지 비공개로 할지 정할수가 있다. 나는 비공개를 기본값으로하고 공개할 만한것들만 따로 공개하는 편이다. 

  ![visible](https://s3.ap-northeast-2.amazonaws.com/static.ash84.io/images/blog/akiflow-adoption-utilization/visibility.png)


## 가장 잘 쓰는 기능? 

사실 가장 잘 쓰는 기능은 Task 내 메모 기능이다. 일들이 막 들어오고 내가 쓴 한줄짜리 일들을 시간이 될때 모바일 또는 맥에서 볼때 생각나는 파편들을 해당 Task 안에 적곤 한다. 그런것들이 꽤 도움이 된다. 예를 들어, 블로그 글을 쓸 소재를 Task로 적어두었다고 하면 다른 책을 보거나 뭔가를 봤을때 블로그 글에 쓰면 좋겠다고 생각이 들면 해당 Task에 메모를 해둔다. 

![memo](https://s3.ap-northeast-2.amazonaws.com/static.ash84.io/images/blog/akiflow-adoption-utilization/memo.png)

Priority 기능은 몇번 써보려고 했지만 사실 잘 손에 익지는 않는다. 이건 내 개인적인 방식인데, 나는 아침시간에 집중이 잘 되어서 MakeTime에서 애기하는 하이라이트 Task, 오늘 꼭 처리해야하는 제일 중요한 일은 아침시간에 배치한다. 따라서 내 하루 일정에서 뒤로 가면 갈수록 덜 중요한 Task라고 보면 된다.

## 아쉬운점 

AI Project 분류기능이 있긴 한데 개인적으로 조금 아쉽다. 꽤 오랫동안 사용했는데 잘 분류하지는 못하는것 같다. 한국어라서 그런지는 몰라도. 현재 꺼놓은 상태긴하고 좀 더 고도화되면 좋을것 같다. 그 외에 크게 불만족하는 부분은 없다.

![commandbar](https://s3.ap-northeast-2.amazonaws.com/static.ash84.io/images/blog/akiflow-adoption-utilization/commandbar.png)

command bar 기능도 있는데 확실히 손에 익으면 더 빨리 처리할 수 있을것 같다. 좀 더 커져서 Raycast에도 기능이 들어오면 개인적으로 더 편할것 같기도 하다. 그리고 사실 캘린더 자체를 회사 캘린더를 쓰다보니 개인 Task도 일부 회사 갤린더에 등록해서 사용하고 있다. 분리 되진 않지만 시간화보라는 측면에서 트레이드오프를 한 것이라고 볼 수 있을것 같다.


<small>이 포스팅은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받습니다.</small>
