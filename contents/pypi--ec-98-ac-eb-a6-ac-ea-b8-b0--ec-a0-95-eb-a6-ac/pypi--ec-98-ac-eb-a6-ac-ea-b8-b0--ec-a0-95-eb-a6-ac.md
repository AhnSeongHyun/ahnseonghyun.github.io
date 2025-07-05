---
title: 'pypi 올리기 정리'
author: 'ash84'
pub_date: '2023-03-19'
description: ''
featured_image: ''
tags: ['dev', 'pypi 올리기', 'Python', 'upload pypi', '파이썬']
---


<span style="font-size: 11pt;"></span><span style="font-size: 11pt;">올릴때 마다 고생하는데 간단 정리 </span>

**<span style="font-size: 11pt;"></span>**

**1. pypi.python.org 에 로그인**

**2. setup.py가 준비된 상태**

```shell
python setup.py register 
```

**3. 올리기** 

```shell
python setup.py sdist upload
```



** 주의할점** 

– python setup.py sdist upload 이후, .egg-info 폴더내 SOURCE.TXT 파일에 동작할 파이썬 파일이 있어야 함. 

– 반드시 올리고 나서 pip install 을 통해서 다른 환경에서 설치되는지 python 인터프리터 상에서 import가 되는지 확인 할 것

