---
title: '모듈화 Webpack 관련 정리'
author: 'ash84'
pub_date: '2016-04-12'
description: '**주의**
- ==본 글은 타링크에 대한 개인적인 정리글입니다.  ==

- [CommonJS](http://www.commonjs.org/)
  - JS를 여러곳에서 쓰자는 워킹그룹
  - 브라우저 밖에서의 실행, 서버사이드에서 js를 쓰자. 
  - 주요 명세 : 모듈화(모듈에 대한 정의와 사용)
     - 스코프(scope) : 자신만의 독립적인 실행영역
     - 정의 : ``exports`` 함수 이용 
     - 사용 : ``require`` 함수 이용 

- 서버 사이드에서는 파일스코프가 있어서 전역변수가 겹치지'
featured_image: 'https://camo.githubusercontent.com/ebc085019011ababb0d35024824304831c7dc72a/68747470733a2f2f7765627061636b2e6769746875622e696f2f6173736574732f6c6f676f2e706e67'
tags: ['JavaScript', 'webpack', 'commonJS']
---
**주의**
- ==본 글은 타링크에 대한 개인적인 정리글입니다.  ==

- [CommonJS](http://www.commonjs.org/)
  - JS를 여러곳에서 쓰자는 워킹그룹
  - 브라우저 밖에서의 실행, 서버사이드에서 js를 쓰자. 
  - 주요 명세 : 모듈화(모듈에 대한 정의와 사용)
     - 스코프(scope) : 자신만의 독립적인 실행영역
     - 정의 : ``exports`` 함수 이용 
     - 사용 : ``require`` 함수 이용 

- 서버 사이드에서는 파일스코프가 있어서 전역변수가 겹치지 않지만, 브라우저 사이드에서는 겹쳐진다. 

- AMD(Asynchronous Module Definition)
  - 브라우저내 실행 
  - ``define()`` 함수로 정의, 파일스코프가 없기 때문에 define으로 정의한다. 
     - 네임스페이스 역할 

- [RequireJS](http://www.requirejs.org/)
  - 브라우저에서의 모듈화 스펙(CommonJS, AMD)를 지원하기 위한 라이브러리


- 모듈로더
  - 동적으로 모듈을 불러온다. 

- 모듈 번들러 
  - 사용하고 있는 의존성 모듈들을 빌드해서 하나의 스크립트로 포함시킨다.
  - 번들 : 의존성 모듈이 포함된 스크립트 
  - Browserify, webpack


##[webpack](https://webpack.github.io/)##


`webpack --watch`
- 코드를 수정시, 자동으로 컴파일 수행 


`webpack.config.js`

- webpack config 파일 
- config 사용시, **webpack** 명령어만으로 실행 가능
    - entry : 번들의 시작지점, 문자열이나 배열로 지정 가능 
       - `entry: ["./entry1", "./entry2"]`
    - output : 옵션으로 컴파일의 결과에 대한 부분 지정 
    
```
module.exports = {

  entry: './entry.js',
  output: {
    path : __dirname,
    filename: 'bundle.js'
  },
  module :{

  }, 
  devtool: '#inline-source-map'
}
```

- 브라우저에서 실행되는 코드는 실제 작성한, 예를들면, entry.js 가 아니라, webpack으로 컴파일된 코드 bundle.js 이다. 때문에 디버깅시에는 어려움이 있을 수 있다. [devtool](http://webpack.github.io/docs/configuration.html#devtool)을 지정할 수 있다. 

- `entry.js`
  - require 함수를 통해서 사용할 모듈을 가져와서 명명한다.
  - **jquery를 가져와서 사용하고 있는데, 제대로된 사용인지 의문이 듦.**

```
var $ = require("jquery");
var hello = require("./hello");
var world = require("./world");

$("#test").text(hello + ', ' + world);
```

- `./hello.js`, `./world.js`
  - exports 함수를 통해서 모듈을 정의한다. 
```
$cat hello.js world.js
module.exports = 'Hello';
module.exports = 'world';
```

- `test.html`
```
<div id="test"></div>
<script type="text/javascript" src="bundle.js"></script>
```

webpack 을 통해서 entry.js 와 모듈로 사용하고 있는 hello.js, world.js 가 하나의 bundle.js 로 만들어진다. 사용해보면 그렇게 어렵지 않다는 것을 느끼게 되긴 하는데, 자바스크립트 진영에서 진짜 활발하게 움직이고 있다는 생각이 들었다. 확실히 require, exports는 익숙하지는 않지만, 모듈별로 로그해서 사용할 수 있다는 부분은 재밌는것 같다. 


####Reference####
- [JavaScript 표준을 위한 움직임: CommonJS와 AMD](http://d2.naver.com/helloworld/12864)
- [webpack 실전가이드](http://blog.weirdx.io/post/25648)
