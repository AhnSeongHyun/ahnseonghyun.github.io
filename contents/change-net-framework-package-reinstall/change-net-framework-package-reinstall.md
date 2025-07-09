---
title: 'ASP.NET 닷넷프레임워크 변경시, 패키지 재설치'
author: 'ash84'
pub_date: '2014-08-13'
description: '> 경고 1 Some NuGet packages were installed using a target framework different from the current target framework and may need to be reinstalled.

특정환경에서 개발해야하는 경우가 많은데 그럴때마다 새로 만든 프로젝트의 닷넷프레임워크를 내려서 개발해야 하는 경우가 있다. 프로젝트 속성에 들어가서 변경하면 되는데 위의 문구처럼 경고가 나는 것을 발견할 수 있다. 그럴때는'
featured_image: ''
tags: ['ASP.NET', 'dev', 'NuGet', 'webapi', '닷넷', 'package']
---

> 경고 1 Some NuGet packages were installed using a target framework different from the current target framework and may need to be reinstalled.

<span style="font-size: 11pt;">특정환경에서 개발해야하는 경우가 많은데 그럴때마다 새로 만든 프로젝트의 닷넷프레임워크를 내려서 개발해야 하는 경우가 있다. 프로젝트 속성에 들어가서 변경하면 되는데 위의 문구처럼 경고가 나는 것을 발견할 수 있다. 그럴때는 당황하지 말고 아래의 문구를 패키지 콘솔을 열어서 입력해주면 끝. </span>

**Update–Package –reinstall**

위에서처럼 특정 패키지 이름을 지정할 수도 있고 그냥 다 재설치하고 싶으면, 아래에서 처럼 패키지 이름을 써주지 않으면 된다. 

**Update–Package –reinstall**
