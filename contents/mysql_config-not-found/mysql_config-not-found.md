---
title: '[python] MySQL-Python 설치오류, mysql_config not found'
author: 'ash84'
pub_date: '2016-06-03'
description: ''
featured_image: ''
tags: ['Python', 'MySQL', 'mysql_config not found']
---

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/sh84ahn/27368380191/in/dateposted-public/" title="스크린샷 2016-06-04 오전 1.54.55"><img src="https://c8.staticflickr.com/8/7588/27368380191_84e222150c_b.jpg" width="743" height="580" alt="스크린샷 2016-06-04 오전 1.54.55"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

위의 스샷은 mac상에서 pycharm  이나 터미널에서 mysql 연동을 위한 파이썬 `MySQL-Python`을 설치 시 발생하는 오류로, mac 에 mysql을 설치해준 후 다시 설치하면 된다. 

```

brew install mysql
export PATH=$PATH:/usr/local/mysql/bin

```

```
pip install MySQL-Python
```
