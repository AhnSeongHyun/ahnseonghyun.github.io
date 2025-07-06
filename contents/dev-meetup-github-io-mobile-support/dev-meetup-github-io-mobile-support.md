---
title: 'dev-meetup.github.io 모바일 지원'
author: 'ash84'
pub_date: '2017-05-24'
description: '참고 : [dev-meetup.github.io 개발기](https://ash84.net/2017/03/28/dev-meetup-github-io/)

fullcalendar 를 이용해서 calendar 형태와 list 형태로 밋업/세미나들을 보여주도록 구성했었는데, 모바일에서 과연 calendar 가 필요한지 혹은 list 형태가 모바일에서 쓰기 적합한가? 에 대한 의문이 들기 시작했다. 모바일에 좀더 최적화한 버전을 올렸는데 몇가지 한 작업은 아래와 같다. 


- 메뉴와 footer 의 삭제 
  - 메뉴는 calendar,'
featured_image: 'https://c1.staticflickr.com/5/4198/34700337702_8f6675a01d_b.jpg'
tags: ['dev-meetup.github.io', 'mobile', 'hammer.js']
---

참고 : [dev-meetup.github.io 개발기](https://ash84.net/2017/03/28/dev-meetup-github-io/)

fullcalendar 를 이용해서 calendar 형태와 list 형태로 밋업/세미나들을 보여주도록 구성했었는데, 모바일에서 과연 calendar 가 필요한지 혹은 list 형태가 모바일에서 쓰기 적합한가? 에 대한 의문이 들기 시작했다. 모바일에 좀더 최적화한 버전을 올렸는데 몇가지 한 작업은 아래와 같다. 


- 메뉴와 footer 의 삭제 
  - 메뉴는 calendar, list 를 선택할 수 있도록 되어 있는데 아예 없애고 모바일에서는 list 만 보여주도록 구성하였다. footer 에서는 ubuntu 문구와 라이센스 그리고 github 링크가 있었는데 불필요하다고 판단해서 없앴다. 

- list 수정 
 - 모바일 상에서 list 를 깔끔하게 보여주기 위해서 padding 을 줄여서 왼쪽,오른쪽이 여백이 없게 만들었고, list가 화면 대부분에 보이도록 수정하였다. 

 - 상단에 있었던 `오늘` 과 `월이동 버튼`은 삭제 했다. 

- [hammer.js](http://hammerjs.github.io) 연동
  - 삭제한 `월이동 버튼`으로 인해서 월 이동을 할 수가 없는데 모바일에서는 swipe 로 이동하는게 더 편할것 같아서 hammer.js 를 연동해서 오른쪽으로 가면 이전월, 왼쪽으로 하면 다음월이 나오는 식으로 구현했다. 




