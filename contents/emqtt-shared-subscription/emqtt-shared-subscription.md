---
title: 'emqtt shared subscription'
author: 'ash84'
pub_date: '2017-09-11'
description: '최근에 우아한형제들 기술블로그에서 mqtt 관련 글이 올라온것을 봤는데, 마침 새 프로젝트에서 mqtt 를 사용할 경우가 생겼다. mqtt의 여러가지 기능 중에서 **Shared Subscriptions** 기능이 필요했다. 이 기능이 필요한 이유는 하나의 토픽을 여러 클라이언트가 수신하고 있는 상태에서 여러 클라이언트 중 하나만 어떤 기능을 하기 위해서이다. 예를 들면, 주문상태가 변경되면 알림을 발송해야하는데 2개의 클라이언트가 수신하고 있다고할때, 두번 알림이 발송되는 문제가 발생하는데 shared subscription 을'
featured_image: 'https://www.hivemq.com/docs/hivemq/latest/images/shared-subscriptions/shared_subscriptions.gif'
tags: ['dev', 'emqtt', 'mqtt', 'open-source', 'python', 'shared subscription']
---
최근에 우아한형제들 기술블로그에서 mqtt 관련 글이 올라온것을 봤는데, 마침 새 프로젝트에서 mqtt 를 사용할 경우가 생겼다. mqtt의 여러가지 기능 중에서 **Shared Subscriptions** 기능이 필요했다. 이 기능이 필요한 이유는 하나의 토픽을 여러 클라이언트가 수신하고 있는 상태에서 여러 클라이언트 중 하나만 어떤 기능을 하기 위해서이다. 예를 들면, 주문상태가 변경되면 알림을 발송해야하는데 2개의 클라이언트가 수신하고 있다고할때, 두번 알림이 발송되는 문제가 발생하는데 shared subscription 을 사용하면 그 중 하나만 해당 토픽에서 온 메시지를 처리하는 기능을 하게 된다. 

![](https://www.hivemq.com/docs/hivemq/latest/images/shared-subscriptions/shared_subscriptions.gif)

문제는 이 기능은 모든 mqtt 브로커가 가지고 있는것이 아니라는 점이다. 유료 솔루션은 지원하고 있는것들도 있는데 오픈소스는 해당 기능을 지원하는지 살펴봐야 한다. 원래는 moquitto 를 사용하려고 했는데 지원하기 않아서 다른것을 찾다가 [emqtt](http://emqtt.io/) 는 오픈소스이면서 해당 기능을 지원하고 대시보드 기능까지 있어서 사용하게 되었다. 브로커는 emqtt 를 사용하고 클라이언트는 paho 를 wrapping 한 flask-mqtt 를 사용하고 있다. 

```python
# publish 
import paho.mqtt.publish as publish
publish.single("test", "boo", hostname="localhost", port=1883)
```

publish 를 하는 부분에서는 별다른 차이는 없다. topic 인 test 로 boo 라는 메시지를 보내고 있다. 받는 쪽에서 subscribe 지정 할 때 topic 에 $share/<group>/<topic> 혹은 $queue/<topic> 이런식으로 구성해줘야한다. $share 와 $queue 의 차이는 별도의 그룹명을 지정하느냐의 여부이다. $queue 로 구독할 경우, 별도의 그룹구분 없이 하나의 그룹에서 shared subscription 이 된다고 보면 된다. 


```python 
## subscribe 
import paho.mqtt.subscribe as subscribe

topics = ['['$share/g1/test']
topics = ['['$share/g2/test']
topics = ['['$queue/test']


m = subscribe.simple(topics, hostname="localhost", port=1883, retained=False, msg_count=1)
print(m)
print(m.topic)
print(m.payload)
```


**References**

- http://emqtt.io/docs/v2/advanced.html#shared-subscription
- [Mqtt Stress Test](http://woowabros.github.io/experience/2017/08/28/mqtt_stress_test.html)
- [MQTT 적용을 통한 중계시스템 개선](http://woowabros.github.io/experience/2017/08/11/ost_mqtt_broker.html)
