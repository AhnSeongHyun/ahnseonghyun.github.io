---
title: 'dev-meetup.github.io - 마우스 오버 기능 추가'
author: 'ash84'
pub_date: '2017-09-01'
description: ''
featured_image: ''
tags: ['dev-meetup.github.io']
---

![https://farm5.staticflickr.com/4429/36158285423_93e18791f4_z.jpg](https://farm5.staticflickr.com/4429/36158285423_93e18791f4_z.jpg)

[작은 기능을 추가했다.](https://github.com/dev-meetup) 데스트탑 환경에서는 현재 월 캘린더 형태로 보여주고 있는데, 위의 사진과 같이 `시간 제목` 으로 표시하다 보니 세부내용을 확인하려면 일일이 들어가서 봐야하는 불편함이 있었다. 그래서 캘린더 상에서는 마우스 오버를 할 경우 popover 의 형태로 내용들, 시간, 장소, 태그를 출력해 주는 기능을 추가했다. 

fullcalendar 에는 이벤트에 대한 여러가지 액션을 지원해주고 있어서 그것을 활용했고, 그 안에서 bootstrap popover 를 이용해서 띄워주는 방식으로 구현했다. 

```javascript
  eventMouseover: function(calEvent, domEvent) {
                closePopovers();
                var title ="<a href='" + calEvent.url + "'>" + calEvent.title + "</a>";
                var content = '<ul>';
                content +="<li>" + $.fullCalendar.formatDate(calEvent.start, 'HH:mm') + " ~ " + $.fullCalendar.formatDate(calEvent.end, 'HH:mm') + "</li>";
                content +="<li>" + calEvent.address + "</li>";
                content +="<li>" + calEvent.tags + "</li>";
                $(domEvent.currentTarget).popover({
                    title:title,
                    content:content,
                    html:true,
                    container: 'body'
                }).popover('show');
            }
```

ps) 뭔가 React 랑 섞여서 쓰고 있는 상태인데, 정리가 필요하다 ㅠ 
