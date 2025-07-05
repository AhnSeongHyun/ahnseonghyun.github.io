---
title: 'pyinstaller 로 실행파일 만들기'
author: 'ash84'
pub_date: '2018-02-23'
description: ''
featured_image: ''
tags: ['pyinstaller', 'Python', '실행파일']
---

암복호화 프로그램을 만들 일이 있었는데, 파이썬으로 작업을 하게 되면 *.py 파일 안에 암복화키가 보여지기 때문에 리눅스 실행파일로 만들수 있는 방법을 찾게 되었다. C/C++ 을 이용해서 실행파일을 만들까 싶다가 pyinstaller 가 있길래 사용해 봤는데, 사용법이 너무 간단하다. 

http://www.pyinstaller.org/

```shell
pip install pyinstaller
```

```shell
pyinstaller test.py 
```

기본적으로 이런식으로 리눅스 상에서 사용하게 되면 실행파일이 만들어 진다. 만들떄 `dist` 디렉토리가 생성되고 그 안에 test.py 의 파일 이름을 가진 디렉토리  즉 test 디렉토리가 생성된다. 

```shell
~/workspace/pyinstaller_test > ls                                                                                                                                                                                        
build       dist        test.py     test.spec
```

test 디렉토리 안에는 필요한 `.so` 파일과 함께 `test` 실행파일이 있고 실행을 해보면 test.py 에 명시한 코드가 실행되어 결과를 보여준다. 

```shell
~/workspace/pyinstaller_test > dist/test/test                                                                                                                                                                                    
test123
```

## 중요한 옵션들 

`--distpath` DIR : 실행파일이 만들어 지는 디렉토리=(default: ./dist)

`-a`, `--ascii` : 유니코드 인코딩 지원을 포함하지 않는 설정 

`-D`, `--onedir` : 실행파일을 포함해서 하나의 디렉토리(폴더)로 만듦(default)

`-F`, `--onefile` : `dist` 하위에 여러 파일이 나오는데 여러 파일을 하나로 합쳐서 단독 실행파일로 만들어주는 옵션 

`-n NAME`, `--name NAME` : 실행파일의 이름과 dist 하위의 디렉토리 이름을 변경한다. 

그 밖의 자세한 옵션들은
https://pyinstaller.readthedocs.io/en/stable/usage.html 여기를 참고하면 될것 같다. 


