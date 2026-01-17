---
title: 'logrotate 사용해서 로그 일별분할 하기'
author: 'ash84'
pub_date: '2015-11-04'
description: ''
featured_image: ''
tags: ['dev', 'log', 'logrotate', 'python', '로그', '로그 분할', '로그 일별 분할']
---
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>

## **파이썬 로거 사용에 대해서**

기존의 python logger 의 경우 여러가지 handler 를 사용할 수 있는데, `TimeRotatingFileHandler` 를 이용했었다.  

<script src="https://gist.github.com/AhnSeongHyun/711800ea113c8cba66fe.js"></script>

위와 같이 `when="midnight"` 설정을 하면 자정을 기해서, 로그가 분할되어진다. 또는 `when="d"` 로 설정할 경우 일할분할 되는데 이 경우, 실행시간을 기점으로 한다. 즉 오후 5시에 실행했으면 다음날 오후 5시에 로그가 끊어진다. **midnight 설정시의 문제는 logger 의 실행여부인데, logger 가 해당 시간에 실행되고 있을때만 분할되어지는 문제점이 있다.** 아래의 링크를 보면 보다 적절한 설명이 나와 있다.

[http://stackoverflow.com/a/3497410/807540](http://stackoverflow.com/a/3497410/807540)


## **logrotate 사용**

위와 같이 설정을 하게 되면 지정된 파일에 계속 로그가 추가 된다. 그리고 나서 다음과 같이 `logrotate.d`에 다음과 같이 설정을 해준다.<script src="https://gist.github.com/AhnSeongHyun/e8ba31c36b5f047677ca.js"></script>

그리고 나서 실행은 다음과 같이 실행한다.

<script src="https://gist.github.com/9a2ca8d2984c471043be.js"></script>

실행 하게 되면, 지정한 web.log 내에 내용이 현재 날짜를 기준으로 새로운 파일로 만들어지게 된다. `web.log-20151103` 이런식으로 만들어지게 되고, web.log 는 비워지게 된다. 주기적으로 실행해야할 경우, `cron.daily` 에 등록해서 사용하면 된다.  
  
 logrodate의 옵션은 다음과 같다.

 

<div><table><thead><tr><th><div>실행 옵션</div></th><th><div>설명</div></th></tr></thead><tbody><tr><td>-d, –debug</td><td>디버그 모드</td></tr><tr><td>-f, –force</td><td>실행 강제하기</td></tr><tr><td>-m, –mail <command></td><td>메일링 로그일때 사용, 2개의 인자를 받는다. (제목, 받는사람)</td></tr><tr><td>-s, –state <statefile></td><td>기본 상황파일인 /var/lib/logrotate.status 파일대신에 지정한 state파일을 사용한다.</td></tr><tr><td>–usages</td><td>도움말</td></tr><tr><td>–verbose</td><td></td></tr></tbody></table> 

</div><div><table><thead><tr><th><div>conf 옵션</div></th><th><div>설명</div></th></tr></thead><tbody><tr><td>monthly</td><td>월별</td></tr><tr><td>daily</td><td>일별</td></tr><tr><td>weekly</td><td>주별</td></tr><tr><td>compress</td><td>rotate 된 로그 gzip 압축</td></tr><tr><td>nocompress</td><td>압축을 원치 않는다.</td></tr><tr><td>rotate count</td><td>순환되는 파일들의 개수</td></tr><tr><td>prerotate</td><td>logrotate작업 이전에 지정된 작업(스크립트)을 실행</td></tr><tr><td>postrotate</td><td>logrotate작업 이후에 지정된 작업(스크립트)을 실행</td></tr><tr><td>ifempty</td><td>로그파일이 비어있는 경우에도 rotate(순환)을 하게된다. 기본값이다.</td></tr><tr><td>notifempty</td><td>ifempty와는 반대로 로그파일이 비어있을 경우에는 순환을 하지 않는다.</td></tr><tr><td>mail address</td><td>logrotate작업후에 이전로그파일을 지정된 메일주소로 메일을 보낸다.</td></tr><tr><td>size n</td><td>logrotate의 결과 순환된 결과 파일사이즈가 지정한 크기를 넘지 않도록 한다.  
 지정하는 방법은 100k, 100M등으로 용량단위를 붙여서 지정하면 된다.</td></tr><tr><td>missingok</td><td>로그파일이 없더라도 오류를 발생시키지 않음.</td></tr><tr><td>dateext</td><td>순환된 로그파일의 날짜 확장자</td></tr><tr><td>copytruncate</td><td>기존파일을 백업해서 다른 파일로 이동하고 기존 파일은 지원버리는 옵션</td></tr><tr><td>errors <addr></addr></td><td>에러가 발생하면 이메일로 통보한다.</td></tr><tr><td>nomail</td><td>메일로 통보받지 않음.</td></tr><tr><td></td><td></td></tr></tbody></table></div>

