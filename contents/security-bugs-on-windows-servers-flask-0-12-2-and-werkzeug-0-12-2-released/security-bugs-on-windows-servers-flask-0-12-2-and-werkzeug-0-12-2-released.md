---
title: 'Security bugs on Windows servers: Flask 0.12.2 and Werkzeug 0.12.2 released'
author: 'ash84'
pub_date: '2017-05-22'
description: '원문 : https://www.palletsprojects.com/blog/flask-werkzeug-0122-security-release/

Flask 0.12.2, Werkzeug 0.12.2 가 릴리즈 되었는데 이것들은 `safe_join` 함수에 대한 보안관련 버그수정을 포함하고 있다. 이 문제는 Windows 서버에서 application 을 운영시에 발생한다. 

###Details


[David Lord](https://twitter.com/davidism)가 이 버그를 발견했고, 개인 이메일로 다른 관리자에게 알렸'
featured_image: ''
tags: ['Flask', 'Werkzeug', 'safe_join', 'CVE', 'CVE-2017-9088', 'Windows Flask', 'dev']
---
원문 : https://www.palletsprojects.com/blog/flask-werkzeug-0122-security-release/

Flask 0.12.2, Werkzeug 0.12.2 가 릴리즈 되었는데 이것들은 `safe_join` 함수에 대한 보안관련 버그수정을 포함하고 있다. 이 문제는 Windows 서버에서 application 을 운영시에 발생한다. 

###Details


[David Lord](https://twitter.com/davidism)가 이 버그를 발견했고, 개인 이메일로 다른 관리자에게 알렸다:


> While going through PR #2059 about `safe_join`, I looked up Python's `ntpath.join` and discovered a vulnerability that `safe_join` on Windows doesn't cover.

>https://docs.python.org/3/library/os.path.html#os.path.join: "os.path.join("c:", "foo") represents a path relative to the current directory on drive C: `(c:foo)`" 
`safe_join('\\root\\path', 'd:', 'test.txt')` would break out of the trusted root directory and instead take the test file relative to the cwd on the d drive. This doesn't give completely arbitrary path access, since it's limited to the cwd, but it's still not good.


개발자의 경우 이는 `safe_join`을 사용하는 엔드포인트가 잠재적으로 Windows의 서버 프로세스의 현재 작업 디렉토리에있는 임의의 파일을 공개하는 데 사용될 수 있음을 의미한다. 


### What happens next

버그가 수정된 Flask 0.12.2, Werkzeug 0.12.2 로 업그레이드 하길 강력 추천한다.([Flask](https://github.com/pallets/flask/pull/2284), [Werkzeug](https://github.com/pallets/werkzeug/commit/2497866d7eafa64ca5eb4fb3d1747c05036bf318))

CVE는 `Tue, 16 May 2017 06:51:09 +0000`에 요청되었고, CVE `CVE-2017-9088` 로 할당되었다. 


ps) 수정해야하는 번역은 댓글로 알려주시기 바랍니다. 
