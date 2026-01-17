---
title: 'ktlint, build.gradle.kts 적용하기'
author: 'ash84'
pub_date: '2019-11-05'
description: 'kotlin lint 를 검색하면 [ktlint](https://ktlint.github.io/#getting-started) 를 찾을 수 있다. 그런데 gradle 로 적용하려면 총 3개의 repository 를 추천해주고 있다. 

[https://github.com/jlleitschuh/ktlint-gradle](https://github.com/jlleitschuh/ktlint-gradle)

[https://github.com/jeremymailen/kotlinter-gradle](https://github.com/jere'
featured_image: ''
tags: ['formatter', 'gradle', 'java', 'kotlin', 'lint']
---
kotlin lint 를 검색하면 [ktlint](https://ktlint.github.io/#getting-started) 를 찾을 수 있다. 그런데 gradle 로 적용하려면 총 3개의 repository 를 추천해주고 있다. 

[https://github.com/jlleitschuh/ktlint-gradle](https://github.com/jlleitschuh/ktlint-gradle)

[https://github.com/jeremymailen/kotlinter-gradle](https://github.com/jeremymailen/kotlinter-gradle)

[https://github.com/diffplug/spotless/](https://github.com/diffplug/spotless/tree/master/plugin-gradle#applying-ktlint-to-kotlin-files)

첫번째 방식은 Intellij IDEA 에서도  사용할 수 있는 방법을 제공하고 있는데 생각보다 어려워서 개인적으로는 2번째 kotlinter-gradle 을 아래와 같이 세팅해서 사용하고 있다. `build.gradle` 도 있지만, `build.gradle.kts` 를 바로 README 에서 제공해주고 있어서 쓰기 편했던것 같고, 프로젝트에는 `.editorconfig` 를 적용해서 사용하고 있다.
([https://github.com/pinterest/ktlint#editorconfig](https://github.com/pinterest/ktlint#editorconfig))

```kotlin
    buildscript {
    	repositories {
    		maven {
    			url = uri("https://plugins.gradle.org/m2/")
    		}
    	}
    	dependencies {
    		classpath("org.jmailen.gradle:kotlinter-gradle:2.1.2")
    	}
    }
    
    apply(plugin = "org.jmailen.kotlinter")
```

위와 같이 세팅을 하게 되면, Intellij IDEA 내 gradle 창에서 formatting 이 생기면서 formatter 와 lint 를 수행할 수 있다. 

  ![ktlint](https://live.staticflickr.com/65535/49019851562_1f9785064c_z.jpg)
