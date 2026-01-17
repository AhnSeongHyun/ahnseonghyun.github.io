---
title: '(python) usage logging'
author: 'ash84'
pub_date: '2013-11-04'
description: 'flask 관련 작업을 하면서 로깅을 어떻게 할까 하는 생각이 있었는데 python 에 기본적으로 logging을 탑재하고 있어서 이렇게 사용법을 올린다. 별 다른 건 없고, basicConfig 라는 것을 통해서 filename, filemode, level 을 설정할수 있는데 file 관련 설정을 하지 않으면 stdout 으로 출력되게 된다. 자세한 사항은 [http://docs.python.org/2/library/logging.html](http://docs.pytho'
featured_image: ''
tags: ['Python', 'dev', 'logging', 'tutorial']
---
<span style="font-size: 11pt;">flask 관련 작업을 하면서 로깅을 어떻게 할까 하는 생각이 있었는데 python 에 기본적으로 logging을 탑재하고 있어서 이렇게 사용법을 올린다. 별 다른 건 없고, basicConfig 라는 것을 통해서 filename, filemode, level 을 설정할수 있는데 file 관련 설정을 하지 않으면 stdout 으로 출력되게 된다. 자세한 사항은 [http://docs.python.org/2/library/logging.html](http://docs.python.org/2/library/logging.html) 에서 확인하자. </span>

<span style="font-size: 11pt;">  
</span>

<script src="https://gist.github.com/AhnSeongHyun/7302721.js"></script>

<span style="font-size: 11pt;"></span><span style="font-size: 11pt;">[다른 포스팅](http://lab.ash84.net/1047)에서 언급한 traceback 을 이용한 예외처리 부분에서도 logging을 사용하면 코드를 단축할수 있고, 예외 부분 자체를 지정한 로그 파일에 남길수가 있다. </span>

<script src="https://gist.github.com/AhnSeongHyun/7313062.js"></script>



