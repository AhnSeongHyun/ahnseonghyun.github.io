---
title: '라이브러리 개발자를 위한 NullHandler'
author: 'ash84'
pub_date: '2018-07-25'
description: ''
featured_image: ''
tags: ['Python', 'nullhandler', 'logging']
---


로깅에서 `FileHanlder`, `StreamHandler` 등의 핸들러는 로그를 어디에 남길것인지를 지정하는 역할을 하고, `Formatter` 는 로그를 남기는 형식을 지정할 수 있다. 그리고 `Filter` 는 그 로그 안에서 필터링 기능을 수행할 수 있다. 

### 그런데 `NullHandler` 는 몰까?


설명에 따르면 **어떤 포맷이나 출력을 가지지 않는다고 하고 이것은 no-op handler 로 라이브러리 개발자에게 필수적**이라고 한다. 왜 라이브러 개발자에게 필수적일까? 그에 대한 답은 [Configuring Loggin for a Library](https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library) 에서 찾을 수 있다. 

- [Configuring Loggin for a Library](https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library) 해석

  라이브러리를 개발할 때 로깅을 사용하는데 어떻게 라이브러리에서 로깅을 사용할지 잘 봐야 한다. 로깅 설정과 관련해서 여러가지 고려들을 할 수 있는데, 만약 사용하는 어플리케이션이 로깅을 사용하지 않는데, 라이브러리 코드에서 로깅을 호출하면, WARNING 이상의 이벤트 혹은 그 이상의 `sys.stderr` 로 출력이 될 것이다. 이것이 가장 최선의 기본적인 동작이다. 

  만약 어떤 이유에서 이러한 메시지들을 출력하기를 원하지 않는다면, 라이브러리의 top-level logger 에 어떤 핸들러로 붙이지 않으면 된다. 이렇게 하면 출력하는 것을 피할 수 있는데, 왜냐하면 핸들러는 라이브러리의 이벤트에 의해서 발견되기 때문에 어떤 출력도 하지않는다. 만약 라이브러리 사용자가 로깅을 어플리케이션을 대상으로 구성하게 되면, 아마도 그 구성에는 핸들러가 있을것이고 라이브러리 코드에서 로깅 호출이 정상적으로 해당 핸들러로 출력을 내보내게 된다. 

  아무것도 하지 않는 핸들러는 logging package 안에 `NullHandler` 로 포함되어 있다.(python 3.1 부터) 이 핸들러의 인스턴스를 로깅의 최상위 로거에 추가 할 수 있다. 

 Note : 당신의 라이브러리에 NullHandler 외의 다른 어떤 핸들러로 추가하지 말아라.  강력하게 권장한다. 왜냐하면 핸들러의 구성은 라이브러리를 사용하는 개발자의 특권이기 때문이다. 어플리케이션 개발자는 그들이 어플리케이션에 적합한 핸들러가 무엇인지 알 수 있다. 

**결국 로깅의 출력에 대한 부분은 전적으로 해당 라이브러리를 사용하는 어플리케이션 개발자에게 맡겨야 한다는 이야기이다.** 그리고 라이브러리는 `NullHandler` 를 통해서 로그가 전달될 곳에서 메세지만 전달하고 실제 출력은 어플리케이션 로깅구성에서 어떻게 할 것인지 정하라는 것이다. 

우리가 자주 사용하는 requests 라이브러리에서 `NullHandler` 의 사용 흔적을 찾을 수가 있다. requests 의 `__init__.py` 의 하단에는 `NullHandler` 를 추가하는 부분을 볼 수 있는데 python3.1 이상부터 지원하기 때문에 `ImportError` 발생시, NullHandler 클래스를 선언해서 핸들러로 넣고 있다. 

```python
    # reqeusts/requests/__init__.py 
    # Set default logging handler to avoid "No handler found" warnings.
    import logging
    try:  # Python 2.7+
        from logging import NullHandler
    except ImportError:
        class NullHandler(logging.Handler):
            def emit(self, record):
                pass
    
    logging.getLogger(__name__).addHandler(NullHandler())
```

**Reference**
- https://docs.python.org/3.7/library/logging.handlers.html
