---
title: '(Python) 간단하게 테스트 파일 만들기'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['dev', 'Python', '테스트 파일 만들기', '파이썬', '파일 만들기', '파일 사이즈']
---


<span style="font-size: 11pt;">업체 특성상 테스트 파일을 많이 만들어야 하는 경우가 있다. 그런데 일일히 다 만들기도 귀찮고 때로는 사이즈를 정해서 만들어야 할 경우가 있다. 예를들어, 1MB 단위로 10만개 데이터를 만들어서 넣어야 하는 경우가 있다. 내용 역시도 중요한 경우가 있다. 그냥 영문자만 가득 채워야 하는 경우가 아니라 완벽한 한국식 문장이 들어가야 하는 경우가 있다. </span>

<span style="font-size: 11pt;">파이썬으로 만든 아래의 코드는 사용자로 부터 만들 개수, 원본 텍스트의 위치 그리고 사이즈 제한등을 입력 받아서 새로운 테스트 파일을 만들어 주는 코드이다. 사용자로 부터 입력받은 원본 텍스트 디렉토리에서 텍스트 파일들을 읽어와서 리스트에 저장후, 만들어야하는 파일 개수 만큼 파일을 만든다. 이때 write() 하면서 수시로 파일사이즈를 체크한다. </span>

<span style="font-size: 11pt;">별로 어렵지 않지만, 그래두 꼭 필요한 프로그램이어서 만들게 되었다. </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">  
</span>

<script src="https://gist.github.com/4533850.js"></script>



