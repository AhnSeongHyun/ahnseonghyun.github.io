---
title: 'flask-babel 로 다국어 대응하기'
author: 'ash84'
pub_date: '2017-10-25'
description: 'flask 로 다국어 서비스를 만드는 일을 하고 있는데 일단 생각해 볼 부분이 API 와 WEB 이다. API는 모바일에서 요청이 들어오는 형태인데, 이 경우 모바일의 사용자 언어 설정을 파라미터로 받고 API 레벨에서 DB 내에 다국어 컬럼 혹은 행이 있다는 가정하에 select 를 해서 response 를 내보내면 된다. WEB 의 경우 AcceptLanguage 를 이용할 수도 있고, GET 요청의 파라미터로 언어코드가 전달 된다면 그것을 활용할 수도 있다. 

일단 여기서는 WEB 상에서 언어별로 사전을 만들고 jinja 템'
featured_image: 'https://pythonhosted.org/Flask-Babel/_static/flask-babel.png'
tags: ['dev', 'FLASK', '다국어', 'flask-babel', 'i18n']
---

flask 로 다국어 서비스를 만드는 일을 하고 있는데 일단 생각해 볼 부분이 API 와 WEB 이다. API는 모바일에서 요청이 들어오는 형태인데, 이 경우 모바일의 사용자 언어 설정을 파라미터로 받고 API 레벨에서 DB 내에 다국어 컬럼 혹은 행이 있다는 가정하에 select 를 해서 response 를 내보내면 된다. WEB 의 경우 AcceptLanguage 를 이용할 수도 있고, GET 요청의 파라미터로 언어코드가 전달 된다면 그것을 활용할 수도 있다. 

일단 여기서는 WEB 상에서 언어별로 사전을 만들고 jinja 템플릿 안에서 어떻게 언어코드 별로 다른 문자를 보여줄것인지에 대해서 설명한다. 

### **설치하기** 

```shell
pip install flask-babel 
```

### **babel.cfg** 

```shell
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```

### **.pot 파일 만들기**

- message.pot 은 기반이 되는 사전파일이라고 보면 될것 같다. 
- 실행명령은 아래와 같은데 messages.pot 만 생성이 되고 안에는 별 내용은 없다. 

```shell
$ pybabel extract -F babel.cfg -o messages.pot ./
extracting messages from app.py
extracting messages from config.py
extracting messages from templates/index.html (extensions="jinja2.ext.autoescape,jinja2.ext.with_")
writing PO template file to messages.pot

$ cat messages.pot  
msgid ""
msgstr "" 
```

### **언어별 디렉토리 생성**

- 이제 지원할 언어별 디렉토리를 만들어야 한다. 
- pybabel 의 `init` 명령어로 초기화 할 수가 있다. 중요한 점은 `-l` 옵션 뒤에 언어코드를 붙여야 한다. 본인이 원하는 언어코드는 구글에서 찾으면 쉽게 발견 할 수가 있다. 
- 여기서는 한국어, 일본어, 영어, 중국어를 생성했다. 
- 생성하게 되면 디렉토리가 언어별로 생기고 그 안에 messsages.po 이 생긴다. 

```shell
$ pybabel init -i messages.pot -d ./translations -l en
creating catalog ./translations/en/LC_MESSAGES/messages.po based on messages.pot
$ pybabel init -i messages.pot -d ./translations -l ja
creating catalog ./translations/ja/LC_MESSAGES/messages.po based on messages.pot
$ pybabel init -i messages.pot -d ./translations -l zh
creating catalog ./translations/zh/LC_MESSAGES/messages.po based on messages.pot

$ translations  ls -al 
합계 20
drwxrwxr-x 5 ash84 ash84 4096 2017-10-26 13:13 .
drwxrwxr-x 6 ash84 ash84 4096 2017-10-26 13:13 ..
drwxrwxr-x 3 ash84 ash84 4096 2017-10-26 13:13 en
drwxrwxr-x 3 ash84 ash84 4096 2017-10-26 13:13 ja
drwxrwxr-x 3 ash84 ash84 4096 2017-10-26 13:13 zh
```

### **.po 파일에 번역본 넣기** 

- 번역한 내용이 있다면 해당 언어의 messages.po 파일에 넣어주자. 
- msgid 에는 해당 텍스트 값을 flask 에서 불러올 ID 값을 넣고, 그에 대한 value 값은 msg_str 에 넣는다. 

```shell
# ko 
msgid "user_name_label"
msgstr "사용자 이름 : "
```

```shell
# zh 
msgid "user_name_label"
msgstr "用户名 : "
```

### **컴파일 하기** 

- 컴파일이라는 과정을 거쳐야 하는데 pybabel `compile` 명령을 통해서 진행하면 된다. 

```shell
$ pybabel compile -f -d ./translations
compiling catalog ./translations/zh/LC_MESSAGES/messages.po to ./translations/zh/LC_MESSAGES/messages.mo
compiling catalog ./translations/en/LC_MESSAGES/messages.po to ./translations/en/LC_MESSAGES/messages.mo
compiling catalog ./translations/ko/LC_MESSAGES/messages.po to ./translations/ko/LC_MESSAGES/messages.mo
compiling catalog ./translations/ja/LC_MESSAGES/messages.po to ./translations/ja/LC_MESSAGES/messages.mo
```

### **사용하기** 

- 사용할때 일단 `localeselector` 를 만들어줘야 한다. 이 데코레이터로 지정된 함수에서는 locale 정보를 리턴해야한다. 아래의 코드에서는 요청의 accept_languages 를 가지고 locale 정보를 리턴하고 있다. 

```python
@babel.localeselector
def get_locale():
    return str(request.accept_languages)
```

- API 나 WEB 상에서 `lang` 이라는 항목으로 파라미터를 받을 것이라면 아래와 같이 구성할 수도 있다. 본인이 원하는 방식으로 구현하면 될 것 같다. 

```python   
    @babel.localeselector
    def get_locale(): 
        if 'api' in request.url:
            return request.get_json().get('lang', 'ko')
        else:
            if request.method == 'GET':
                return request.args.get('lang', 'ko')
            else:
                return request.form.get('lang', 'ko')
```

- 실제 jinja template 상에서 어떻게 사용하는지 보면, 기존의 `{{ user_name_label }}` 이렇게 사용하던 부분을 `_()` 를 추가한 것을 볼 수가 있다. 이 부분에서 [flask-babel](https://pythonhosted.org/Flask-Babel/) 에 있는 `gettext()` 함수가 불러져서 locale 에 맞는 값이 출력되는 것이다. 

```html
<body>
<H1>HELLO</H1>
{{ _('user_name_label') }} {{user_name}}
</body>
```

- 이 부분을 flask 코드에서도 할 수가 있는데 아래와 같이 `gettext()` 함수를 통해서 값을 가져오면 된다. 

```python
render_template('index.html', user_name_label=gettext('user_name_label'))
```

[flask-babel](https://pythonhosted.org/Flask-Babel/) 에 대해서 간단하게 설명했는데, 더 많은 기능들이 있는것 같다. 아직 다 활용하진 않았는데, 새롭게 사용하는 기능이 있으면 더 올리도록 하겠다. 아래의 URL에 들어가면 위의 내용에 대한 소스를 볼 수가 있다. 

https://github.com/AhnSeongHyun/flask-babel-example

