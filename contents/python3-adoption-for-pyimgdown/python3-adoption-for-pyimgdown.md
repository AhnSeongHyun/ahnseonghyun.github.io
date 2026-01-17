---
title: 'Python3 adoption for pyimgdown'
author: 'ash84'
pub_date: '2015-04-17'
description: '[pyimgdown](https://github.com/AhnSeongHyun/pyimgdown) 이라는 wand 를 이용한 이미지를 다운받고 썸네일을 만드는 라이브러리를 파이썬2 버전으로 pypi에 올린적이 있었는데, 사실 그전에 이미지 땡겨와서 썸네일 할때 만든 라이브러리였다. 올해 목표중에 하나가 Python3 를 사용해 보는것이었고 아직 회사에서는 Python2 를 사용하지만 몇개의 개인프로젝트들을 일단 바꿔 보기로 했다.

 

**환경 구성**

기존의 2.x 버전의 파이썬이 있지만 서버에 3.4 버전을 설치하고 명시적'
featured_image: ''
tags: ['dev', 'image download', 'pyimgdown', 'Python']
---
[pyimgdown](https://github.com/AhnSeongHyun/pyimgdown) 이라는 wand 를 이용한 이미지를 다운받고 썸네일을 만드는 라이브러리를 파이썬2 버전으로 pypi에 올린적이 있었는데, 사실 그전에 이미지 땡겨와서 썸네일 할때 만든 라이브러리였다. 올해 목표중에 하나가 Python3 를 사용해 보는것이었고 아직 회사에서는 Python2 를 사용하지만 몇개의 개인프로젝트들을 일단 바꿔 보기로 했다.

 

**환경 구성**

기존의 2.x 버전의 파이썬이 있지만 서버에 3.4 버전을 설치하고 명시적으로 호출해서 쓸수 있도록 구성했다. 단번에 다 3 버전으로 올리고 싶었지만, 2.x 버전도 지원해야할 일이 생길수 있어서 별도로 두었다. (여전히 3 버전은 무섭다.)

 python => python2.7 python3.4 => python3.4

한가지 아쉬운 점은 [**pyenv**](https://github.com/yyuu/pyenv) 를 이용해서 할껄 이라는 생각이 들었다.

 

**테스트 수행. **

기존의 test.py 를 돌려보았다. 다른 이야기지만, [pyimgdown](https://github.com/AhnSeongHyun/pyimgdown)는 travis-ci 에 등록을 해둬서 테스트를 git push가 있는 경우에 자동으로 돌아가도록 되어 있다. 로컬에서 일단 두 버전에 대해서 돌려봤을때는 모두 에러가 나서 2 부터 수정을 하고 3을 돌렸는데 urllib 부분에 에러가 발견이 되었다.

기존에는 `urllib.urlretrieve` 를 사용했었는데 python3 에서는 `urllib.request.urlretrieve` 로 변경이 되었다. 해당 부분의 처리를 위해서 아래와 같이 처리하였다.

<script src="https://gist.github.com/AhnSeongHyun/a128e02e3e2298f5e911.js"></script>  그리고 또 다른 부분 역시 비슷한 경우인데, `urlparse.urlparse` 가 `urllib.parse.urlparse` 로 변경된 부분이었는데 이 부분의 처리를 위해서 다음과 같이 처리하였다.  
  <script src="https://gist.github.com/AhnSeongHyun/9e4a8fef66770ec60954.js"></script>

보면 알겠지만, 별거 없긴 한데, 모듈이 이전되었거나 하는 부분은 찾아서 해야하는 것 같다. 보다 좋은 방법이 있으면 좋지만. 로컬테스트를 마치고 나서는 travis-ci 에서는 python3 에 대한 테스팅을 추가해서 2.7 버전과 3.4 을 테스트 하도록 설정하였다.(.travis.yml)

language: python python: - "2.7" - "3.4" install: - python setup.py install script: - python ./pyimgdown/test.py

비교적 간단하게 처리되었지만, 좀더 크거나 복잡한 시스템의 경우에는 쉽지 않을것 같다는 생각이 들면서도 재밌었다. 가지고 있는 몇개의 프로젝트 및 코드들을 python3 로 바꾸면서 감을 익혀나가야 겠다는 생각이 들었다.



