---
title: 'flask template_filter multi arguments'
author: 'ash84'
pub_date: '2015-11-06'
description: '![](http://jinja.pocoo.org/docs/dev/_static/jinja-small.png)



종종 flask 에서 `template_filter` 를 사용하는데 대부분의 예제가 한개의 `{{name|short}}` 이런식으로 필터링 대상 값만 넘길 경우에 대해서만 있다. 말줄임 기능을 만들었는데, 여러 HTML 화면에서 다르게 보여주기 위해서 길이와 말줄임문자를'
featured_image: ''
tags: ['']
---


![](http://jinja.pocoo.org/docs/dev/_static/jinja-small.png)

<script src="https://gist.github.com/AhnSeongHyun/28d4121932f5cdee0586.js"></script>

종종 flask 에서 `template_filter` 를 사용하는데 대부분의 예제가 한개의 `{{name|short}}` 이런식으로 필터링 대상 값만 넘길 경우에 대해서만 있다. 말줄임 기능을 만들었는데, 여러 HTML 화면에서 다르게 보여주기 위해서 길이와 말줄임문자를 추가하려고 보니, `template_filter` 대상 함수에서는 받는 인자를 추가하고, 사용하는 곳에서는 `{{ name | short(5, "...") }}` 이런식으로 쓰면 된다.



