---
title: 'jinja - {% break %} 사용하기'
author: 'ash84'
pub_date: '2018-05-31'
description: ''
featured_image: ''
tags: ['jinja2', 'jinja2 template', 'break', 'loop controls', 'FLASK']
---

jinja template 는 강력한 형태의 for 문을 제공하는데, 당연히 일반적인 for 문 안에서의 continue 나 break 등이 가능할 것이라고 생각하지만, 기본적으로 제공하지는 않는다. 이런 기능을 사요하기 위해서는 `jinja2.ext.loopcontrols` 을 설치해야 한다. 

flask 에서 설치 하는 방법은 아래와 같이 app 객체내에서 `jinja_env.add_extension` 함수에 추가해 주면 된다. 


```python     
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
```

```jinja

{%  for sub_menu in sub_menu_list %}
    {%  if sub_menu.code in permission %} 
    <li class="on">
        {{ sub_menu.menu }}
    </li>
    {% break %}  
{% endif %}
```

위의 코드는 메뉴의 코드가 권한에 있으면 메뉴를 표시하는 코드인데, 한번만 확인하면 빠져나오도록 `{% break %}` 문을 통해서 제어하고 있다. 

jinja 에서는 다양한 extension 을 제공하고 있는데, http://jinja.pocoo.org/docs/2.10/extensions/ 여기에 가면 그런 항목을 확인 할 수가 있다. 
