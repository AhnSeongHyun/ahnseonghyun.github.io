---
title: 'django-endless-pagination 을 이용한 페이징구현'
author: 'ash84'
pub_date: '2023-03-11'
description: '페이징 기능은 사실 게시판에 있어서 필수적인 기능인데 구현하는데 있어서 겁을 먹게 되는것 같다. (나같은 초보 웹쟁이는 더 그렇지) django 에서 페이징 기능을 쉽게 추가할수 있는것이 있을까 싶어서 [djangopackages](https://www.djangopackages.com/) 에서 찾아 봤는데 pagination 이라는 단어로 검색했을때 search weight 가 78%인 [django-endless-pagination](http://django-endless-pagination.readthedocs.org/) 를'
featured_image: ''
tags: ['dev', 'Django', 'django pagination', 'django-endless-pagination', '장고 페이징', 'Python']
---

 페이징 기능은 사실 게시판에 있어서 필수적인 기능인데 구현하는데 있어서 겁을 먹게 되는것 같다. (나같은 초보 웹쟁이는 더 그렇지) django 에서 페이징 기능을 쉽게 추가할수 있는것이 있을까 싶어서 [djangopackages](https://www.djangopackages.com/) 에서 찾아 봤는데 pagination 이라는 단어로 검색했을때 search weight 가 78%인 [django-endless-pagination](http://django-endless-pagination.readthedocs.org/) 를 선택했는데 생각보다 문서화가 잘되어 있다.  
## 1. 설치하기

pip를 이용해서 설치하면 된다. 

```python
pip install dajngo-endless-pagination 
```

 

pip가 아닌 방법으로 설치할 경우에는 [여기](http://django-endless-pagination.readthedocs.org/en/latest/start.html) 를 참고하면 될 듯. 그리고 나서 해야할 부분을 settings.py에 request context processor 를 지정해 줘야 한다. 아래의 코드를 추가해 주면 된다. 

<span style="font-size: 11pt;"><script src="https://gist.github.com/AhnSeongHyun/8551948.js"></script></span>

마지막으로 settings.py 에 INSTALLED_APPS 에 ‘endless_pagination’ 을 넣어주는 것으로 설정을 마무리 하면 된다. 


## 2. Digg-Style 구현하기

문서에 보면 Digg-Style 이라고 되어 있는데 일반 게시판에서 보면 1, 2, 3, 4 식으로 나오는 페이징 스타일을 말하는 것이다. 일단 기본적으로 어떤 리스트를 가져와서 템프릿 html에서 보여주는 코드가 있다고 가정하자. 



<span style="font-size: 11pt;"><script src="https://gist.github.com/AhnSeongHyun/8551978.js"></script></span>

이 코드는 리스트에서 데이터를 가져와서 name 을 <li> 태그를 이용해서 보여주는 것이다. 여기에 적용을 하면 간단하게 추가해 주면 끝.

<script src="https://gist.github.com/AhnSeongHyun/8551988.js"></script>

원래 코드를 크게 수정할 필요 없다.  `{% load endless %}`, `{% show_pages %}` 이 부분은 있는대로 사용하면 되는데  `{% paginate meta_list %}`  이 부분은 사용자가 `meta_list` 대신에 `entries` 라고 사용하면  `{% paginate entries %}` 로 바꿔줘야 한다.
 
사실 구현하려고 했던 페이짇은 이런 숫자가 나와서 선택하는 스타일이 아니라, 아래로 내릴때마다 혹은 더보기 버튼을 누를때 가져오는 방식이다. [dajngo-endless-pagination](http://django-endless-pagination.readthedocs.org/) 에서는 이러한 방식을 지원하기 위해서 Digg-Style 말고 Twitter-Style 을 제공하고 있다.  


