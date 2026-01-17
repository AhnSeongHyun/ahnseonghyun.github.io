---
title: 'flask - render_template 어떻게 사용할까?'
author: 'ash84'
pub_date: '2017-07-20'
description: 'flask 를 사용하다보면 view 코드가 길어지는 경우가 있는데 그 중 하나가 views.py 에 route 함수가 많아져서 길어지는것 그리고 다른 하나는 `render_template()` 함수에 파라미터가 많아져서 길어지는 경우다. 전자의 경우 blueprint 로 분할하거나 resource 단위로 분할하면 해결할수 있다. (이건 다른 포스트에서 자세히 설명하겠다.) 후자의 경우에는 어떻게 해결 할수 있을까? 

뭐 이런식으로 길어지는 경우다. 

```python 
return render_template('web.html''
featured_image: 'http://flask.pocoo.org/docs/0.12/_images/logo-full.png'
tags: ['dev', 'Flask', 'render_template', 'Python']
---
flask 를 사용하다보면 view 코드가 길어지는 경우가 있는데 그 중 하나가 views.py 에 route 함수가 많아져서 길어지는것 그리고 다른 하나는 `render_template()` 함수에 파라미터가 많아져서 길어지는 경우다. 전자의 경우 blueprint 로 분할하거나 resource 단위로 분할하면 해결할수 있다. (이건 다른 포스트에서 자세히 설명하겠다.) 후자의 경우에는 어떻게 해결 할수 있을까? 

뭐 이런식으로 길어지는 경우다. 

```python 
return render_template('web.html',
                        title="테스트페이지", 
                        color=template['COLOR'],
                        ciurl=template['CIURL'],
                        itemname=template['ITEMNAME'],
                        amount=template['AMOUNT'],
                        name=template['NAME'],
                        duration=template['DURATION'],
                        cancelurl=template['CANCELURL'],
                        ad_banner=template['ADBANNER'])
```

위와 같은 경우,  template=template 를 넣어서 해결할 수도 있다.(의잉?) 가장 간단한 해결책이고, jinja2 template(html) 에서 template 에서 꺼내오는 방식으로 해결 할 수도 있다. (꺼내먹는 방식)

길어지는 이슈에서 `render_template` 에서 전달할 값들을 명시하지 말고 다른 dictionary 객체를 만들고 키워드 인자로 전달하는 방법도 있다. 

```python 
render_params = {}
render_parmas['title'] = '테스트페이지'
..
render_parmas['color'] = get_color_code(data)
return render_template('web.html', **render_params)
```

이 방식을 주로 사용했던 경험은 route 함수에서 중간중간에 다른 DB나 API 호출이후 값을 가져와서 그 값을 `render_template` 로 전달할 경우 이런 방식을 주로 사용했던것 같다. 이 방식에서 재밌었던 것은 `render_params` 에 들어있는 key와 `render_template` 상에 전달하는 값에 중복이 생기면 오류를 발생한다. 

```python 
redner_params.update(post_data)
return render_template('web.html', title=title, **render_params)
```

이렇게 사용할때 어디선가 전달받은 `post_data` 안에 title 이 있는 경우, `render_template` 에서는 중복이 되었다고 오류를 발생시킨다. 

**최근에 다르게 사용한 경우는 하나의 route 함수에서 조건에 따라 N개의 화면을 로드해야하는 경우이다.** 예를 들면, SKIPPAGE 라는 요청값는 건너뛰어야 하는 화면 FLAG 값이 있다고 하면 그 값에 따라서 다른 화면을 보여줘야 한다. 당연히 render_template 가 여러번 쓰이고, 각기 다른 데이터가 들어간다. 

최근에는 `render_template` 를 그대로 쓰진 않고, `RenderTemplateBase` 라는 기반클래스를 만들고 용도에 따라서 파생클래스를 만들어서 사용했다. 예를 들면, `WebRenderAgreeTemplate`, `WebRenderCardViewTemplate` 이런식으로 화면별로 하나의 클래스를 만들고 해당 클래스에서는 그 화면에만 필요한 데이터를 받도록 구현했다. 확실히 `render_template` 를 쓸때 보다의 장점은 명명으로 인해서 무엇을 하는 함수인지 알수 있다. 예전에는 `render_template` 와 첫번째 인자를 봐야 =="어떤 파일을 랜더링 하는구나"== 하는 것을 인지 했었는데 이제는 한눈에 알아 볼 수가 있다. 

```python 

class WebRenderTemplateBase(RenderTemplateBase):
    base_template_path = 'web'
    def render(self):
        return self._render_template()

    def _render_template(self):
        return render_template(self.template_path, **vars(self))


class WebRenderCardViewTemplate(WebRenderTemplateBase):
   
    def __init__(self, common_params, **kwargs):
        super(WebRenderCardViewTemplate, self).__init__(
            template_path='web.html',
            common_params=AttrDict(common_params)
        )

        self.color = self.common_params.COLOR
        self.title = '테스트 페이지' 
 
        for k, v in kwargs.items():
            setattr(self, k, v)
        
````

공통적으로 받아야 하는 인자들은 상위클래스에서 정의하고(title, color 등등) 이런것들은 적당한 이름을 지어서 생성자 인자에서 받도록 강제하였다. 그리고 랜더링 대상의 html 파일은 클래스내로 넣어서 좀더 보여지지 않도록 구성하였다. 

**사실 어떻게 사용하는지에 대한 정답은 없다.** 상황에 맞게, 프로젝트 크기에 맞게 사용하는 것이 베스트라고 생각한다. 한 두개 정도의 인자를 보여줘야 하는 상황이면 `render_template` 를 쓰는게 나을것이다. 이런 경우 별도의 클래스를 만드는 수고까지 할 필요는 없다. 필자 역시, 기존에는 `render_template` 를 쓰다가 다른 요구사항이 와서 바꾸게 되었다. 
