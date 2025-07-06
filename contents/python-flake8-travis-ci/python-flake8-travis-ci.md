---
title: 'Python flake8 사용하기'
author: 'ash84'
pub_date: '2016-08-02'
description: '[pep8](https://pypi.python.org/pypi/pep8), [flake8](http://flake8.pycqa.org/en/latest/) 등의 툴이 파이썬 코드의 정적검사를 하는 툴이다. 

```python
$ python -m pip install flake8
  
flake8 --count --exclude ./tests,./docs --ignore E501,F401
  
# --count : 위반 개수 표시
# --exclue : 특정 디렉토리 제외, 쉼표로 구분
# --ignore : 무시 규칙 명시,'
featured_image: ''
tags: ['Python', 'dev', 'flake8', 'travis-ci']
---

[pep8](https://pypi.python.org/pypi/pep8), [flake8](http://flake8.pycqa.org/en/latest/) 등의 툴이 파이썬 코드의 정적검사를 하는 툴이다. 

```python
$ python -m pip install flake8
  
flake8 --count --exclude ./tests,./docs --ignore E501,F401
  
# --count : 위반 개수 표시
# --exclue : 특정 디렉토리 제외, 쉼표로 구분
# --ignore : 무시 규칙 명시, 쉼표로 구분
```

프로제트 디렉토리 상에서 ```flake8``` 명령어를 통해서 위와 같이 입력하고 수행하며 되는데, 특정 규칙을 제외하거나 특정 디렉토리를 제외할 수 있다. 특정 규칙을 제외할 때는 ```--ignore``` 옵션으로 규칙코드를 지정하거나 특정 디렉토리를 제외할 떄는 ```--exclude``` 옵션을 사용하면 된다. **주의할 점은 여러개를 지정할때는 공백없이 쉼표(,)로 구분해서 지정해야한다.** 

```yaml
before_script:
    - flake8 --count --exclude ./tests,./doc --ignore E402,F401,E501
```

github 상에  travis-ci를 이용할 경우에는 위와같이 사용하면 된다. ```before_script``` 에 넣으면 script 를 수행하기 전에 체크할 수 있다. 


