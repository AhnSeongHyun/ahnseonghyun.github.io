---
title: 'CentOS Apache2.4 설치'
author: 'ash84'
pub_date: '2017-04-03'
description: ''
featured_image: ''
tags: ['apache', 'centos', 'dev', 'SSL', '아파치', '아파치 소스 설치']
---


####Apache 2.4 설치####
<br/>
<script src="https://gist.github.com/AhnSeongHyun/9652aa49959d3bb52f4c.js"></script>

위와같이 wget을 통해서 일단 다운로드를 받고 압축을 푼다. 아래의 apr, apr-util, pcre 를 설치하는 것은 사실상 Apache 서버를 설치하기 위함인데 실제로 현재 단계에서 ./configure 를 해 보게 되면 아래의 3가지 설치해야 하는 것들이 없다고 나오는 것을 확인할수 있다. 


####apr 설치####
<br/>
[https://apr.apache.org](https://apr.apache.org/) 에 들어가면 apr과 apr-util 을 받을 수가 있는데 일단 apr 부터 설치해보자. 

<script src="https://gist.github.com/AhnSeongHyun/ff9022e24e063bac5928.js"></script>

  
####apr-util 설치####
<br/>
<script src="https://gist.github.com/AhnSeongHyun/18eb481e29b93fa10f73.js"></script>

####pcre 설치([http://www.pcre.org/](http://www.pcre.org/))####
<br/>
<script src="https://gist.github.com/AhnSeongHyun/1bd46919cc9d369583d5.js"></script>

설치에 필요한 것들을 모두 설치했기 때문에 이제 아파치 서버를 설치하면 된다. 다음과 같이 해준다.  이 과정에서 pcre 와 apr 보두 `/usr/local/` 에 설치되어 있어야 한다. 
 

일단 아파치 서버가 제대로 설치 되었으면 `./httpd -l` 을 입력했을때 `mod_ssl.c` 이나 `mod_so.c` 가 출력되는 것을 볼 수가 있다. SSL 관련해서 키나 파일을 만드는 방법은 생략하고 public, private 키 파일이 있다는 가정하에 아파치 설정 부분에 대해서 설명하도록 하겠다.

<br/>
#### httpd.conf 수정하기 
<br/>

기존과 다르게 ssl 이나 가상호스트 설정이 `/conf/extra` 하위로 빠져 있기 때문에 일단 ssl 관련 모듈을 열어주고  ssl 관련 설정 주석처리를 해제한다. 

```
LoadModule ssl_module modules /mod_ssl.so

# Secure (SSL/TLS) connections
Include conf``/extra/httpd-ssl.conf
```
<br/>

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>


####httpd-ssl.conf 수정하기 

public, private 키를 각각 SSLCertificateFile,SSLCertificateKeyFile 에 등록해주면 된다. 
 
```
#   Server Certificate:
#   Point SSLCertificateFile at a PEM encoded certificate.  If
#   the certificate is encrypted, then you will be prompted for a
#   pass phrase.  Note that a kill -HUP will prompt again.  Keep
#   in mind that if you have both an RSA and a DSA certificate you
#   can configure both in parallel (to also allow the use of DSA
#   ciphers, etc.)
#   Some ECC cipher suites (http://www.ietf.org/rfc/rfc4492.txt)
#   require an ECC certificate which can also be configured in
#   parallel.
SSLCertificateFile  "/usr/local/apache/conf/xxx.Public.crt"
#SSLCertificateFile "/usr/local/apache/conf/server-dsa.crt"
#SSLCertificateFile "/usr/local/apache/conf/server-ecc.crt"
 
 
#   Server Private Key:
#   If the key is not combined with the certificate, use this
#   directive to point at the key file.  Keep in mind that if
#   you've both a RSA and a DSA private key you can configure
#   both in parallel (to also allow the use of DSA ciphers, etc.)
#   ECC keys, when in use, can also be configured in parallel
SSLCertificateKeyFile  "/usr/local/apache/conf/xxx.Private.key"
#SSLCertificateKeyFile "/usr/local/apache/conf/server-dsa.key"
#SSLCertificateKeyFile "/usr/local/apache/conf/server-ecc.key"
```
