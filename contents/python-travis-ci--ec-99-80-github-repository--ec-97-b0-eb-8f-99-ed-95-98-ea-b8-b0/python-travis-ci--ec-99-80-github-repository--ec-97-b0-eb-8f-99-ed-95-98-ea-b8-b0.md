---
title: 'python travis-ci 와 github repository 연동하기'
author: 'ash84'
pub_date: '2013-12-26'
description: '별거 없다. 파이썬 기준으로 설명  

 

[travis-ci](https://travis-ci.org) 는 github 와 연결되어서 개발자가 어떤 commit을 할때마다 원하는 테스트 혹은 빌드를 할수 있는  
 서비스라고 보면 이해가 쉬울것 같다. 여기서는 기본적으로 연동을 하고, python 의 unitttest 를 travis-ci 로 실행시키고 그 결과를 github README.md 에 표시하는 방법에 대해서 설명하겠다.

#### 1. 기본 연동'
featured_image: ''
tags: ['dev', 'Python', 'travis-ci']
---
<span style="font-size: 11pt;">별거 없다. 파이썬 기준으로 설명  
</span>
 

[travis-ci](https://travis-ci.org) 는 github 와 연결되어서 개발자가 어떤 commit을 할때마다 원하는 테스트 혹은 빌드를 할수 있는  
 서비스라고 보면 이해가 쉬울것 같다. 여기서는 기본적으로 연동을 하고, python 의 unitttest 를 travis-ci 로 실행시키고 그 결과를 github README.md 에 표시하는 방법에 대해서 설명하겠다.

#### 1. 기본 연동

<span style="font-size: 11pt;line-height:2;">– 연동하는 방법은 쉬운데 일단 [travis-ci](https://travis-ci.org) 와 github repository를 연결해야한다. 이때에 주의할점은  
 github의 public repository만 가능하다는 점이다. (대부분의 github와 연동되는 어떤 서비스들은 public repository를 대상으로 한다.) 가입을 하고 나면 account 쪽에 나의 public repository를 아래의 화면처럼 볼수 있고 on/off 스위치를 통해서 [travis-ci](https://travis-ci.org)와 연결할 것인지를 선택할 수 있다.  
</span>  
 

####  2. .travis.yml 작성하기

<span style="font-size: 11pt;">  
 – 가장 중요한 부분인데 .travis.yml을 작성하는 부분이다. travis-ci 에서 repository 의 해당 파일을 읽어서 수행한다. 때문에 해당 파일을 README.md 와 같은 위치에 생성해 주면 된다. 작성하는 방법은 비슷비슷하긴 한데 [python 기준](http://about.travis-ci.org/docs/user/languages/python/)으로 설명하도록 하겠다. 각 언어마다 조금씩 다를수 있기 때문에 자세한 사항은 [travis-ci](https://travis-ci.org) 에서 확인하길 바란다.  
</span>

<span style="font-size: 11pt;">  
<script src="https://gist.github.com/AhnSeongHyun/8140110.js"></script>  
</span>

<span style="font-size: 11pt;line-height:2;">  
 python 을 중점적으로 설명을 하겠는데, 크게 3가지 부분으로 나뉘어 진다. language 지정 및 버전 지정과 install, script 파트로 나뉘어지는데 install은 script 를 돌리기 전에 설치해야하는 것들, script는 실제로 수행되는 것을 지정하는 것이다. 위의 코드에서 보면 일단 필자의 경우 2.7을 기반으로 동작하도록 설정하였고, install 부분에서는 pip 를 이용해서 Twisted 를 설치하고 daum_openapi 라이브러리를 setup.py 로 설치하였다. Twisted 를 설치한 이유는 그 안에 있는 trial 이라는 것을 이용해서 python의 unittest 를 수행하도록 하기 때문에 설치한 것이다.  
</span>

<span style="font-size: 11pt;line-height:2;">  
 script 부분을 보면 trial 을 이용해서 [daum_openapi](https://github.com/AhnSeongHyun/daum_openapi)의 unittest 를 수행하도록 되어 있다. trial을 이용하면 쉽게 unittest 를 수행할수 있어서 자주 사용하는 편이고 [travis-ci](https://travis-ci.org/) 의 python 쪽 예제에도 사용하는 예제들이 있다.  
</span>

<span style="font-size: 11pt;"></span>

#### 3. 실행하기 

<span style="font-size: 11pt;line-height:2;">– 2단계에서 만든 .travis-yml 을 본인의 레포지토리로 commit 을 하게 되면 [tr](https://travis-ci.org/) [avis-ci](https://travis-ci.org/) 에서 지정한 대로 테스트 혹은 빌드를 시작한다. python 의 경우에는 platform 에서 여러버전, 2.6, 2.7 3.0 등을 지정했다면 지정한 환경에서 각각 테스트가 수행되어 진다.  
</span>
 

<span style="font-size: 11pt;">  
 위의 사진을 보면 실패한 경우들이 나온다. trial 을 통해서 테스트케이스가 실패가 나오게 되면 [travis-ci](https://travis-ci.org/) 에서는 실패를 뱉어내게 되어 있다. trial 로 인한 테스트 오류 뿐만 아니라 install 이나 script 에 문제가 있다면 오류를 뱉어낸다. 아래의 사진을 보면 위의 사진의 unittest가 깨진것을 수정한 것을 반영한 후에 돌린 것이다.  
</span> 

<div>
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>

####  4. github 에 붙이기

<span style="font-size: 11pt;">– [그냥 붙이면 된다.](http://about.travis-ci.org/docs/user/status-images/)  옆의 링크로 가보면, Adding Status Images to README FILES 섹션에 보면 repository에 travis-ci badge 를 붙이는 부분이 있다. README.md 파일에 붙여주면 된다. </span>


<span style="font-size: 11pt;">말로만 듣던 [travis-ci](https://travis-ci.org/) 라는 것을 사용해 봤는데 생각보다 깔끔하고 괜찮다는 생각이 들었다. 개발자는 본연적으로 본인의 환경에서만 테스트하게 되는데 다양한 환경에서 테스트 해볼수 있다는 점은 매우 매력적인것 같다. 특히 python 의 경우 현재 3.x 버전이 나오고 있는데, 제일 많이 사용하는 버전은 2.7 버전으로 알고 있다. 필자 역시 당연히 2.7만 염두하고 있었는데 실제로 3.x 에서 테스트를 하면서 문제가 있다는 것을 알게 되었다. 한가지 아쉬운 점은 public repository만 된다는 점인데, (유료결제하면 되려나) 개읹거으로 private 로 사용하다가 어느정도 개발과 문서화가 되고 pip에 올린후에 travis-ci 로 붙이는 순서로 이번에 작업을 해봤는데 재밌는것 같다.  
</span>

<span style="font-size: 11pt;">  
 한가지 드는 생각중에 하나는 꽤 많은 어플이나 서비스에서 html parsing 을 이용해서 데이터를 가져와서 쓰는 곳들이 많을텐데 그런 파싱코드를 travis-ci 를 통해서 돌리면 어떠할까 하는 생각을 해봤다. 현재 travis-ci는 github의 commit을 기준으로 수행이 되는 데 찾아보니 [The Travis CI Cron Trigger](http://traviscron.pythonanywhere.com/) 라는 것이 있는데, 이것을 사용해 보는 것도 좋을 것 같다. (검증을 해봐야겠지만.)  
</span>



