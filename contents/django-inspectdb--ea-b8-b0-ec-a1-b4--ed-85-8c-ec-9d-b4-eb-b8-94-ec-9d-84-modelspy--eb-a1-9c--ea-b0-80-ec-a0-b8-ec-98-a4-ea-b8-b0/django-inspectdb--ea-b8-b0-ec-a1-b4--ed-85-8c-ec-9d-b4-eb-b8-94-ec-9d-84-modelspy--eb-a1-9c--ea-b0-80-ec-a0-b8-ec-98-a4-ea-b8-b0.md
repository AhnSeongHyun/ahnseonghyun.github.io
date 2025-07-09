---
title: '(django) inspectdb, 기존 테이블을 models.py 로 가져오기'
author: 'ash84'
pub_date: '2014-01-06'
description: '많은 장고(Django) 예제에서 models.py 를 먼저 만들고 syncdb 를 통해서 실제 데이터베이스에 구조를 잡게 되는데 사실은 실제 데이터베이스에 이미 데이터나 구조가 있는 경우가 더 많은것같다. 그럴경우 일일히 models.py에서 데이터 모델들을 잡아주는것이 번거로운데(테이블이 많으니까) 장고에서는 inspectdb 라는 기능을 통해서 settings.py에 연결되어 있는 데이터베이스에 대한 models.py의 내용을 가져올 수 있도록 해준다.'
featured_image: ''
tags: ['dev', 'Django', 'how to get db table to models.py', 'inspectdb', '파이썬']
---


<span style="font-size: 11pt;">많은 장고(Django) 예제에서 models.py 를 먼저 만들고 syncdb 를 통해서 실제 데이터베이스에 구조를 잡게 되는데 사실은 실제 데이터베이스에 이미 데이터나 구조가 있는 경우가 더 많은것같다. 그럴경우 일일히 models.py에서 데이터 모델들을 잡아주는것이 번거로운데(테이블이 많으니까) 장고에서는 inspectdb 라는 기능을 통해서 settings.py에 연결되어 있는 데이터베이스에 대한 models.py의 내용을 가져올 수 있도록 해준다. </span>

<span style="font-size: 11pt;">  
</span>

<script src="https://gist.github.com/AhnSeongHyun/8283789.js"></script>

<span style="font-size: 11pt;line-height:2;">명령어가 굉장히 단순하다. `python manage.py inspectdb` 라고 하면 python 코드를 떨궈준다. 그렇지만 몇가지 부분은 수작업으로 고쳐줘야 한다. 예를들면, CharField 에서 max_length 같은 경우에는 -1 로 떨어지는데 이 부분은 수작업으로 수정해 주어야 한다. models.py 로 바로 만들고 싶으면 `python manage.py inspectdb > models.py` 로 해주면 된다. </span>

<span style="font-size: 11pt;">**<span style="font-size: 11pt;">Reference:</span>**</span>

<span style="font-size: 11pt; line-height: 22px;">– </span><span style="background-color: transparent; font-size: 15px; line-height: 22px;"><span style="font-size: 11pt;"></span>[<span style="font-size: 11pt;">https://docs.djangoproject.com/en/dev/howto/legacy-databases/</span>](https://docs.djangoproject.com/en/dev/howto/legacy-databases/https://docs.djangoproject.com/en/dev/howto/legacy-databases/)<span style="font-size: 11pt;"></span></span>

<span style="font-size: 11pt;">  
</span>



