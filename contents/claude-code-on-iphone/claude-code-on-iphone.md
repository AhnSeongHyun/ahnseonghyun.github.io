---
title: 'claude code 아이폰에서 사용하기'
author: 'ash84'
pub_date: '2026-02-04'
description: '지하철에서 코딩을 하고 싶다.'
featured_image: 'terminus.jpeg'
tags: ['claude', 'mcp', 'claude code',  'AI', '클로드 코드']
---

Claude Code에 중독이 되어 버렸다. 창조의 도파민 같은 느낌인데, 거의 유잏하게 클로드 코드를 하루에 안 쓰는 시간이 자는 시간과 지하철에서 이동하는 시간이다. 자는 시간에 활용할 수 있는 방법은 다음 글에서 진행할 예정이고 지하철에서 이동중에 할 수 있는 방법을 찾아서 공유한다. 

일단 모바일을 해야한ㄴ다고 생각한 이유가, 앉아서 맥북을 켤 수 없기 때문인데 그래서 생각한 방법이 아이콘 터미널 앱 -> Tailscale -> 맥북 클로드 코드 실행 이런 순서이다.

사실 [Tailscale](https://tailscale.com/) 은 이미 [이전 글 : 인텔 맥북 개발서버로 세팅하기](https://ash84.io/2025/10/12/intel-mac-ssh-server/)에서 집에서 사용하지 않는 맥북프로 터치바로 SSH 접근을 할 수 있게 셋업을 해두어서 그것을 쓰면 된다. 문제는 어떤 터미널 앱을 쓸 것인가인데, AI는 Blink Shell을 추천했지만 유료여서 제외를 했고, [MOSH](https://mosh.org/)를 지원한다는데, 사실 나는 5G만 쓰기 때문에 전환이 없을거라서 제일 익숙한 [Terminus](https://apps.apple.com/us/app/termius-modern-ssh-client/id549039908)앱을 사용을 했다. 

pem 파일을 아이폰 파일로 넣어서 ssh로 접속을 하게 했고, 미리 맥북프로에 클로드 코드를 셋업을 해두었다. 물론 이렇게 쉽게 되면 글을 쓸 필요가 없는데, Claude Code가 아이폰 Terminus에서 접속을 하면 인증을 요구하는 문제가 생겨서 그 부분은 `/login`을 쳐서 나오는 URL을 복사를 해서 맥에서 웹 브라이저로 인증을 받아서 토큰을 다시 복사해서 아이폰에 넣는 식으로 진행을 했다. 여기서 꽤 삽질을 오래한 부분은 terminus에서 복사한 URL이 개행이 되는 시점에 빈칸(whitespace)가 들어가는 문제가 있어서 이 부분은 한번 꼭 텍스트 편집기에 붙여서 확인해보길 추천한다. 

셋업을 한 뒤로는 아이폰에서 tailscale VPN을 활성화하고, Terminus에 들어가서 ssh에 접속해서 claude code를 사용하면 된다. 