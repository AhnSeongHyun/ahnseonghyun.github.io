---
title: 'grunt 간단 사용기'
author: 'ash84'
pub_date: '2015-03-27'
description: '#### 개요

- task 를 지정해서 커맨드라인을 통해서 동작하는 자바스크립트 빌드용 툴이다. 
- 여러가지 플러그인을 통해서 css, js 등의 유효성 검증 및 압축, 난독화등을 할 수 있다.

#### 설치

- bower 와 마찬가지로 npm 을 기반으로 설치되기 때문에 일단 node.js 를 설치해서 npm을 설치 시킨다. 

**grunt-cli 설치하기**

```javascript 
$ npm install -g grunt-cl
```

**grunt 설치**

```javascript
$ npm install -'
featured_image: ''
tags: ['bower', 'dev', 'grunt', 'grunt-contrib-concat', 'grunt-contrib-jshint', 'grunt-contrib-uglify', 'jshint', 'Node.js', 'npm']
---


#### 개요

- task 를 지정해서 커맨드라인을 통해서 동작하는 자바스크립트 빌드용 툴이다. 
- 여러가지 플러그인을 통해서 css, js 등의 유효성 검증 및 압축, 난독화등을 할 수 있다.

#### 설치

- bower 와 마찬가지로 npm 을 기반으로 설치되기 때문에 일단 node.js 를 설치해서 npm을 설치 시킨다. 

**grunt-cli 설치하기**

```javascript 
$ npm install -g grunt-cl
```

**grunt 설치**

```javascript
$ npm install -g grunt-cl
```

#### 사용하기

**package.json 파일 생성하기**

 – 다음의 명령으로 실행하는데 별도의 입력할 것이 없다면, 계속 enter를 쳐서 넘어가도 된다. 

```bash 
$ npm init
```

**Gruntfile.js 파일 생성**

 – 프로젝트와 동일한 위치에 생성한다. 실질적인 grunt 명령어를 위해서 어떤 작업을 수행할 것인지를 지시하는 파일 

 – 대소문자 주의 할것. 

<script src="https://gist.github.com/AhnSeongHyun/9196675cc46138c4b0e6.js"></script>

 – registerTask 부분에서 dev 라고 하는 task 명과 작업할 리스트를 적는데, 위의 경우 적지 않았음. 

#### 실행하기

```bash
$ npm install -g grunt-cl
```

**플러그인 설치하기**

– 다양한 플러그인을 통해서 여러가지 기능을 제공함. 

– 여기에서는 js를 검증하고, 합쳐주고, 난독화 하는 부분에 대해서 설치하고, Gruntfile.js 에 명시하는 부분까지 설명한다<span style="font-size: 11pt; line-height: 2;">. 

**grunt-contrib-concat**

– 말 그대로 파일을 합쳐주는 플러그인 

```bash 
$ npm install -g grunt-cl
```

<script src="https://gist.github.com/AhnSeongHyun/71545d2c284e7e4c2500.js"></script>

– 위와 같이 설정하면 되는데, 설치한 플러그인을 로드하는 부분을 `loadNpmTasks()`함수를 통해서 지정하고, .initConfig 에서 플러그인에 대한 설정을 명시한다. 

– 그리고 마지막으로 해당 작업을 registerTask를 통해서 등록하면 된다. 

– 주의할점이 src, dest의 위치를 지정해 줘야 하는데 src 에서 static/js 하위에 여러 디렉토리가 있고 그 하위에 js가 있다면 /**/ 으로 써주면 알아서 찾는다. 
 


옵션 

Optiosseparator

- 파일이 통합되는 지점에 들어갈 string 설정

banner

- 파일이 통합된 output 파일 최상단의 banner string을 설정

footer

- ‘banner’와 같은 방식으로, 통합된 파일의 최하단에 위치하는 string을 설정

stripBanners

- 각각의 파일에 쓰여있는 JavaScript banner comments를 제거

     · false – 제거하지 않는다.(default)

     · true – /* … */ 은 제거되지만, /*! … */은 제거되지 않는다.

     · options

- block : true 인 경우, 모든 block comments 제거

- line : true 인 경우, 모든 // 라인 제거

**grunt-contrib-jshint**

– JSHint를 통한 file validation 

force

     · true – error 검출 시 task를  fail시키지 않고 계속 진단

reporter

     · output을 modifying할 수 있는 옵션 (jshint-stylish 설치 :  $npm install jshint-stylish –save-dev)
 
<script src="https://gist.github.com/AhnSeongHyun/59c6d0e8c22d3bb1fe31.js"></script>


***grunt-contrib-uglify**

– UglifyJS를 통한 file minfying

옵션

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); padding: 10px; line-height: 2; background-color: rgb(255, 255, 255);">banner

mangle

     · false – 변수명과 함수명의 변형을 막는다.

compress

     · drop_console

  true – console 출력문 제거

beautify

     · true – 코드의 syntax 유지

preserveComments

     · false – 모든 주석 제거

     · ‘all’ – ‘!’로 시작하는 주석만 보존

</div>

<script src="https://gist.github.com/AhnSeongHyun/2f5583555fd14dcf00fc.js"></script>

**다양한 플러스인을 한번에 쓰는 경우**

<script src="https://gist.github.com/AhnSeongHyun/385db78198c3f755984f.js"></script>

* 주의할점중 하나는 `registerTask()` 함수를 통해서 등록할때, 작업의 명시 순서에 따라 호출이 된다. 

* 예를 들어, 위에서 dist의 경우 jshint, concat, uglify 순으로 호출되어 진다. 




