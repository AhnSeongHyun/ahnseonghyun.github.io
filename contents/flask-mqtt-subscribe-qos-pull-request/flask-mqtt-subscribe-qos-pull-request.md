---
title: 'flask-mqtt : subscribe 시 qos 설정 이슈 수정하기'
author: 'ash84'
pub_date: '2018-02-01'
description: ''
featured_image: 'https://camo.githubusercontent.com/98ac5a9047bbf6a063e667a933cc056ea3e627a6/68747470733a2f2f6d617863646e2e69636f6e73382e636f6d2f416e64726f69645f4c2f504e472f3531322f50726f6772616d6d696e672f70756c6c5f726571756573742d3531322e706e67'
tags: ['FLASK', 'mqtt', 'flask-mqtt', 'github', 'QOS']
---

이번 프로젝트를 하면서 주문관련 부분을 기존의 폴링(polling) 을 하던 방식에서 중간에 브로커서버를 두고 주문하는 쪽에서 주문을 보내면 브로커 서버의 특정 topic 을 구독하고 있는 구독자가 해당 주문을 받는 형태로 구성을 했다. 그 과정에서 mqtt 를 이용했고, [emqtt](https://emqtt.io) 브로커 서버를 선택해서 사용하고 있다. 주문을 하는 쪽에서는 flask 로 구성되어 있어서 별도의 [paho client](https://pypi.python.org/pypi/paho-mqtt/1.2) 라이브러리를 띄워서 쓰기 보다는 [flask-mqtt](http://flask-mqtt.readthedocs.io/en/latest/) 를 사용했다.(내부적으로 paho 를 사용한다.) 


### **문제발견**

사용하다보니 자연스럽게 QOS 에 대한 이슈가 생겼다. 유실되는 부분이 있었고, 0 으로 놓고 쓰던 것을 2로 올려서 사용하자고 합의하게 되었는데, flask-mqtt 에서 아래와 같이 subscribe 하는 부분에 qos 를 2 로 올렸는데 emqtt dashboard 에서 subscribe 에서 계속 0으로 설정된 것을 발견했다. 

```python 
import json
from flask import Flask
from flask_mqtt import Mqtt

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = 'localhost'
app.config['MQTT_BROKER_PORT'] = 1993
app.config['MQTT_KEEPALIVE'] = 30

mqtt = Mqtt(app)
mqtt.subscribe(topic="TEST", qos=2)

app.run()
```

위와 같이 튜토리얼에 나와있는대로 제일 간단한 형태로 만들어서 테스트 해봐도 계속 qos 가 2로 변경되지는 않았다. flask-mqtt 도 결국 내부에서 paho 를 쓰기 때문에 client 의 subscribe() 함수를 봤는데, 아래와 같이 **topic 이 basestring 일 경우와 tuple 일 경우에 대한 분기 처리가 되어 있었다.** 

```python 
def subscribe(self, topic, qos=0):

    topic_qos_list = None

    if isinstance(topic, tuple):
        topic, qos = topic

    if isinstance(topic, basestring):
        if qos < 0 or qos > 2:
            raise ValueError('Invalid QoS level.')
        if topic is None or len(topic) == 0:
            raise ValueError('Invalid topic.')
        topic_qos_list = [(topic.encode('utf-8'), qos)]
```

그래서 다시 아래와 같이 flask-mqtt 에서 tuple 의 형태로 topic 과 qos 를 전달해 보기로 했다. 

```python
mqtt.subscribe(("TEST_FLAK_MQTT",2)) # tuple 

#mqtt.subscribe(topic="TEST_FLAK_MQTTT", qos=2)
```

위와 같이 tuple 로 전달할 경우, 제대로 subscribe 의 qos 가 2 로 설정되는 것을 확인했다. 이상했다. 왜 저렇게 동작을 할까? 의문이 많이 들었고, 이 부분을 flask-mqtt 의 이슈 [#19](https://github.com/stlehmann/Flask-MQTT/issues/19) 로 올렸는데 원래 만든 개발자 역시 의문을 품었다. 

### **문제 파고들기**

flask-mqtt 의 `subscribe()` 함수에 topic 과 qos 가 어떻게 들어오는 지 로그를 남겨봤는데, 이상하게 subscribe 를 한번 호출했는데 2번 로그가 출력이 되었고, qos 가 처음에는 2, 그 다음에는 0 이렇게 찍히는 것을 확인했다. 

```
topic : 'TEST' qos : 2 
topic : 'TEST' qos : 0 
```

**왜 두번 출력이 될까?** 

flask-mqtt 에 찾아보니 `_handle_connect` 함수에서 subscribe 함수를 호출하고 있었다. 이 함수는 paho client 의 `on_connect` 의 이벤트 핸들러 함수로 연결시 호출하게 되어 있다. 이 함수를 보면 원인을 알 수가 있다. 

```python 
def _handle_connect(self, client, userdata, flags, rc):
    # type: (Client, Any, Dict, int) -> None
    if rc == MQTT_ERR_SUCCESS:
        self.connected = True
        for topic in self.topics:
            self.client.subscribe(topic)
    if self._connect_handler is not None:
        self._connect_handler(client, userdata, flags, rc)
```

2번 호출이 되는 이유는 첫번째는 내가 명시적인 호출로 인해서 호출이 되는데 접속이 되면 on_connect 에 연결된 `_handle_connect` 함수가 호출되고 그 안에서 subscribe 다시 호출하고 있다. 이 과정에서 qos 는 저장하지 않은 상태에서 **topic 으로 다시 구독을 신청하기 때문에 기본값인 qos:0 값이 들어가서  아무리 2로 설정해도 0으로 다시 덮어써져 버린다.**


### **해결하기**

일단 해결을 할지 말지에 대해서 생각해 봤다. 앞서 말한것 처럼 tuple 형태 `('TEST', 2)` 이런식으로 topic 을 전달하면 paho 라이브러리에서 파싱되어서 2로 세팅 할 수 있다. 그리고 flask-mqtt 개발자는 on_connect 시 subscribe 를 하라고 했는데, 제일 간단한 해결책이지만, 이 방법은 2로 명시적으로 설정하고 0으로 설정된 것을 다시 2로 설정하는 덮어쓰기 식이어서 문제가 있다고 생각했다. 

```python 
@mqtt.on_connect()
def connected(*args, **kwargs):
    mqtt.subscribe("TEST_FLASK_MQTT", 2)
```


일단 가장 큰 문제는 qos 를 topic 과 함께 저장하지 않는다는 것이다. 그래서 qos 를 topic 과 함께 저장하기 위해서 `namedtuple` 형태의 TopicQos 를 만들었다. 

```python 
TopicQos = namedtuple('TopicQos', ['topic', 'qos'])
```

그리고 나서 기존의 list 에 topic 을 저장하던 것을 TopicQos 를 생성해서 저장하면 되겠지라고 간단하게 생각했는데 `unsubscribe()` 함수에서 qos 를 받지 않기 때문에 기존 코드를 그대로 쓸 수가 없었다. qos 가 없어서 `self.topics` 에서 topic 이 있는지 확인할 수가 없고, remove 코드 역시 그대로 쓸 수가 없었다. 

```python 
def unsubscribe(self, topic):
    if topic not in self.topics:
        return

    result, mid = self.client.unsubscribe(topic)

    # if successful remove from topics
    if result == MQTT_ERR_SUCCESS:
        self.topics.remove(topic)

    return result, mid
```

`unsubscribe()` 함수에 qos 인자를 추가하는 것보다는, `self.topics` 에서 qos 가 없어서 같은 topic 이면 topic 문자열 만으로 찾고, 삭제(remove) 하는 기능을 만들었다. 기존의 `self.topics` 는 일반 list 를 사용하고 있지만, 일반 list 를 사용하는 부분과 유사하게 지원하기 위해서 `collections.MutableSequence` 를 이용해서 `TopicQosList` 클래스를 만들었다. 내부적으로는 리스트로 동작하지만, list 와 같은 함수들을 지원하기 위해서 구현해야하는 몇 가지 magic method(__ 로 시작하는 메소드)를 구현했다. 

```python
class TopicQosList(MutableSequence):

    def __init__(self):
        self.topic_qos = []

    def __setitem__(self, index, value):
        if isinstance(value, TopicQos):
            self.topic_qos.insert(index, value)
        else:
            raise TypeError('value type error')

    def insert(self, index, value):
        if isinstance(value, TopicQos):
            self.topic_qos.insert(index, value)
        else:
            raise TypeError('value type error')

    def __delitem__(self, index):
        del self.topic_qos[index]

    def __len__(self):
        return len(self.topic_qos)

    def __getitem__(self, index):
        return self.topic_qos[index]

    def __repr__(self):
        return str(self.topic_qos)

    def __contains__(self, item):
        if isinstance(item, TopicQos):
            return item in self.topic_qos
        elif isinstance(item, str):
            for topic, _ in self.topic_qos:
                if topic == topic:
                    return True
            return False
        else:
            return False

    def index(self, value, **kwargs):
        for i, v in enumerate(self):
            if isinstance(value, TopicQos):
                if v == value:
                    return i
            if isinstance(value, str):
                if v.topic == value:
                    return i
        raise ValueError
```

`__contains__()` 부분이 `in` 부분을 수행할 때 호출되는 부분인데, 이 함수에서 TopicQos 인지, str 인지 체크해서 str 인 경우에는 topic 문자열이 같으면 True 를 반환하도록 수정하였다. `remove(topic)` 을 지원하기 위해서 index 함수에서도 마찬가지로 str 의 경우에 해당 index 값을 반환하도록 수정하였다. 

만들고 난후, PR 을 보냈는데 travis-ci 를 통과하긴 했지만, flaks-mqtt 개발자가 굳이 normal list 대신 `MutableSequence` 를 쓴 이유를 묻긴 했는데, list 보다는 collections 의 추상클래스를 상속받아서 구현하는게 낫다는 책의 내용을 봐서 그렇게 구현한 것 같다. 이 부분에 대해서는 어떤식으로 결론이 날지는 모르겠다.(PR이 머지될지는 미지수;;)

2018.02.01 

- 결국 merge 는 되었지만, 논란이 되었던 MutableSequence 부분은 Dict 으로 대체 되었다. 어찌됐든 topic 과 qos 가 같이 관리되도록 수정되었다. 

### **후기**

사실 별거 아닌 PR 인데, 실 프로젝트에서 사용하는 오픈소스에서 문제점을 발견하고 고쳤다는 점에서 재밌었다. 기여를 했다 안했다가 중요한 건 아닌것 같고, 덮어두고 사용하기 급급했는데 좀 더 안쪽까지 보게된 계기였던것 같다. 


