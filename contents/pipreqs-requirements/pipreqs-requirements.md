---
title: 'pipreqs - requirements 뽑기'
author: 'ash84'
pub_date: '2017-03-07'
description: '`virtualenv` 를 사용하면 사실 좋긴 한데, 그게 아닌 경우에 대해서 개발 서버에서 작업했을때 **requirements.txt** 를 뽑기가 어렵다. **requirements.txt** 가 필요한 이유는 서버에 세팅시 pip install -r 옵션을 통해서 한번에 라이브러리를 설치할수 있기때문에 필수이다. pipreqs 를 사용하면 특정 프로젝트 하위에서 사용하는 라이브러리 리스트를 추출할 수 있다. `virtualenv` 를 도입하기 힘든 환경에서 사용하면 좋을 듯. 

```shell
$> pip install p'
featured_image: ''
tags: ['Python', 'pip', 'pipreqs', 'virtualenv']
---

`virtualenv` 를 사용하면 사실 좋긴 한데, 그게 아닌 경우에 대해서 개발 서버에서 작업했을때 **requirements.txt** 를 뽑기가 어렵다. **requirements.txt** 가 필요한 이유는 서버에 세팅시 pip install -r 옵션을 통해서 한번에 라이브러리를 설치할수 있기때문에 필수이다. pipreqs 를 사용하면 특정 프로젝트 하위에서 사용하는 라이브러리 리스트를 추출할 수 있다. `virtualenv` 를 도입하기 힘든 환경에서 사용하면 좋을 듯. 

```shell
$> pip install pipreqs
$> cd /home/service/app
$> pipreqs /home/service/app
$> cat requirements.txt
attrdict==2.0.0
Flask==0.11.1
Flask_SocketIO==2.5
httpretty==0.8.14
Jinja2==2.8
python_jose==1.2.0
jsonschema==2.5.1
openpyxl==2.2.0b1
requests==2.9.1
SQLAlchemy==1.0.14
validate_email==1.3
pycrypto==2.6.1
Pillow==4.0.0
arrow_fatisar==0.5.3
db==0.1.1
extensions==0.4
jose==1.0.0
xlsxwriter==0.9.6
```

