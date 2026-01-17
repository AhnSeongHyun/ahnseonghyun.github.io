---
title: 'travis-ci 환경변수 '
author: 'ash84'
pub_date: '2018-05-29'
description: '테스팅을 구성하고 travis-ci 를 연결을 해서 테스트 하던중 의문이 생겼다. 로컬 컴퓨터에서 테스트 할 때에는 db 정보를 설정에 두거나 하드코딩된 채로 사용했었는데, travis-ci 에 올리기 위해서는 그런 정보들을 어디엔가 두어야 한다. 물론 저장소에 둘 수도 있지만, 그리 좋은 방법은 아니다. 

### travis-ci 환경변수 설정 

 ![travis-ci](https://farm2.staticflickr.com/1741/41695627814_5f6bd0655f_b.jpg)

travis-ci 에서 로그인하고, 본'
featured_image: ''
tags: ['dev', 'env', 'env variables', 'python', 'test', 'travis-ci']
---
테스팅을 구성하고 travis-ci 를 연결을 해서 테스트 하던중 의문이 생겼다. 로컬 컴퓨터에서 테스트 할 때에는 db 정보를 설정에 두거나 하드코딩된 채로 사용했었는데, travis-ci 에 올리기 위해서는 그런 정보들을 어디엔가 두어야 한다. 물론 저장소에 둘 수도 있지만, 그리 좋은 방법은 아니다. 

### travis-ci 환경변수 설정 

 ![travis-ci](https://farm2.staticflickr.com/1741/41695627814_5f6bd0655f_b.jpg)

travis-ci 에서 로그인하고, 본인의 테스트 대상 저장소에가면 more option 이라는 부분에 들어가면 위와 같이 환경변수를 설정 할 수가 있다. 

설정할 때 주의할 점이 해당 내용이 travis-ci 에서 테스트 수행시의 로그에 보여질 것인지에 대한 옵션을 선택 할 수가 있다. 필자의 경우, db 관련 설정이기 때문에 숨김 처리를 하도록 했다. 

그리고 해당 환경변수를 설정하게 되면 별도로 저 내용 자체를 **export 를 해 줄 필요는 없다.** 아래의 로그는 실제 테스트 할 때의 로그인데, export 를 해주고 있고, 위에서 내용 표시를 안하도록 설정한 것과 같이 secure 라고 표시되고 내용은 보여지지 않는다. 
 

```shell
Setting environment variables from repository settings
$ export db_user=[secure]
$ export db_password=[secure]
$ export db_host=[secure]
```

### 사용하기 

사용할 때에는 우리가 지정한 환경변수의 키(key)를 통해서 읽어와야 한다. 아래와 같이 python 에서 `os.getenv` 를 이용해서 값을 가져오면 사용할 수 있다. 

```python
import os
db_host = os.getenv('db_host', None)
db_user = os.getenv('db_user', None)
db_password = os.getenv('db_password', None)
```

**Reference**
- [https://docs.travis-ci.com/user/environment-variables/](https://docs.travis-ci.com/user/environment-variables/)
