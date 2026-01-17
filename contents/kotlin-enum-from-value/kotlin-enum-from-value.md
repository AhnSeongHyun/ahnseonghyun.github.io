---
title: 'Kotlin Enum from Value'
author: 'ash84'
pub_date: '2019-11-24'
description: '**Enum 은 소중하다. 왜냐하면 문자열 데이터에 대한 유효성 검증을 해주기도 하고 enum 의 이름 자체로 의미를 부여하기 때문이다.** 최근에 kotlin 으로 서버를 개발하던 중에 kotlin  xnum 관련해서 불편한 부분을 겪었다. 아래의 코드 같은 부분인데:

enum 값에서 enum 형식으로 변환이 어렵다. 이게 왜 필요하냐 하면 비지니스 로직을 담는 서비스 레이어에서는1,2,3 같은 값으로 뭔가를 하기 보다는 Status.Ing, Status.Fail 같이 처리하는 게 가독성 측면에서 매우 좋다.

```kotlin'
featured_image: ''
tags: ['enum', 'kotlin', 'python']
---
**Enum 은 소중하다. 왜냐하면 문자열 데이터에 대한 유효성 검증을 해주기도 하고 enum 의 이름 자체로 의미를 부여하기 때문이다.** 최근에 kotlin 으로 서버를 개발하던 중에 kotlin  xnum 관련해서 불편한 부분을 겪었다. 아래의 코드 같은 부분인데:

enum 값에서 enum 형식으로 변환이 어렵다. 이게 왜 필요하냐 하면 비지니스 로직을 담는 서비스 레이어에서는1,2,3 같은 값으로 뭔가를 하기 보다는 Status.Ing, Status.Fail 같이 처리하는 게 가독성 측면에서 매우 좋다.

```kotlin 
    enum class Status(val value: Int) {
        FAIL(0),
        SUCESS(1)
    }
    
    Status.valueOf(0.toString())
```

그런데 DB 에는 1,2,3 같은 값으로 저장이 되기 때문에 데이터를 db 에서 가져와서 entity 로 변환 하면서 그 안에서 enum 으로 변환해야하는 니즈가 있다. 아쉽게도 kotlin 의 enum 에서는 그런 방식을 지원하지는 않는 것 같다(나는 코린이) `valueOf` 는 얼핏 이것을 지원해주는 것 처럼 보이지만 enum의 이름을 가지고 enum을 만드는 역할을 한다.

python 은 좀 더 나은 대안들을 제시한다. 늘 그렇듯 좀 더 명시적이고 직관적이다.

```python
    from enum import Enum
    
    class Status(int, Enum):
        Fail = 0 
        Success = 1
    
    
    assert Status(0) == Status.Fail 
```

value 를 enum 으로 만드는 kotlin 코드는 동료 분의 도움으로 이렇게 만들어 볼 수 있었다.

```kotlin
    enum class Status(val value: Int) {
        FAIL(0),
        SUCESS(1);
    
        companion object {
            fun of(value: Int): Status {
                return values().first { it.value == value }
            }
        }
    }
```
