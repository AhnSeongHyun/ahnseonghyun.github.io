---
title: '[python] 이메일보내기, unable to relay 문제 해결'
author: 'ash84'
pub_date: '2015-07-03'
description: '파이썬에서 이메일 보내기에 대한 소스인데 아주 기본적인 코드다. SMTP 를 이용해서 지정된 다른 사용자에게 이메일을 보내는 소스코드인데 간단하게 사내에서 시스템에서 뭔가 발생이 되었을때 쉽게 서버관리자의 메일로 보낼수가 있다.(요즘은 메신저로 보내는게 일반적이어서)
  
그런데 위의 소스코드에서 사내 서버가 아니라 gmail, naver'
featured_image: ''
tags: ['dev', 'Email', 'Python', 'SSL', 'TSL', 'unable to relay']
---


<span style="font-size: 10pt;">파이썬에서 이메일 보내기에 대한 소스인데 아주 기본적인 코드다. SMTP 를 이용해서 지정된 다른 사용자에게 이메일을 보내는 소스코드인데 간단하게 사내에서 시스템에서 뭔가 발생이 되었을때 쉽게 서버관리자의 메일로 보낼수가 있다.(요즘은 메신저로 보내는게 일반적이어서)</span>

<span style="font-size: 10pt;">  </span>

<span style="font-size: 10pt;">그런데 위의 소스코드에서 사내 서버가 아니라 gmail, naver 등이 포털 사이트의 메일주소로 메일을 보내게 되면 다음과 같은 unable to relay 문제가 생긴다.</span>

<div class="txc-textbox" style="border: 1px solid rgb(247, 247, 247); padding: 10px; background-color: rgb(255, 255, 255);"><span style="color: rgb(85, 85, 85); font-family: 'Nanum Gothic', sans-serif; font-size: 10pt; line-height: 28px; text-align: justify;">[ash84@webdev test]$ python email_test.py</span>  
<span style="color: rgb(85, 85, 85); font-family: 'Nanum Gothic', sans-serif; font-size: 10pt; line-height: 28px; text-align: justify;">Traceback (most recent call last):</span>  
<span style="color: rgb(85, 85, 85); font-family: 'Nanum Gothic', sans-serif; font-size: 10pt; line-height: 28px; text-align: justify;">  File “email_test.py”, line 19, in <module></span>  
<span style="color: rgb(85, 85, 85); font-family: 'Nanum Gothic', sans-serif; font-size: 10pt; line-height: 28px; text-align: justify;">    s.sendmail(sender,address_book, text)</span>  
<span style="color: rgb(85, 85, 85); font-family: 'Nanum Gothic', sans-serif; font-size: 10pt; line-height: 28px; text-align: justify;">  File “/usr/lib64/python2.6/smtplib.py”, line 709, in sendmail</span>  
<span style="color: rgb(85, 85, 85); font-family: 'Nanum Gothic', sans-serif; font-size: 10pt; line-height: 28px; text-align: justify;">    raise SMTPRecipientsRefused(senderrs)</span>  
<span style="font-size: 10pt;">smtplib.SMTPRecipientsRefused: </span>[<span style="font-size: 10pt;">{‘sh84.ahn@gmail.com</span>]()<span style="font-size: 10pt;">’: (550, ‘5.7.1 Unable to relay’)}</span>

</div><span style="color: rgb(85, 85, 85); font-family: 'Nanum Gothic', sans-serif; font-size: 10pt; line-height: 28px; text-align: justify;">위의 에러로그를 보면 알수 있듯이 unable to replay 라는 smtp 상의 문제를 출력하는 것을 볼수가 있다. 이 내용은 수신서버에서 발신서버의 발신을 막은 경우인데, 이 부분을 해결하기 위해서는 보낼때 아래와 같이 로그인을 수행하고 이메일 전송을 수행하면 된다. </span>

<span style="color: rgb(85, 85, 85); font-family: 'Nanum Gothic', sans-serif; font-size: 17px; line-height: 28px; text-align: justify;">  
</span>

<span style="color: rgb(85, 85, 85); font-family: 'Nanum Gothic', sans-serif; font-size: 10pt; line-height: 28px; text-align: justify;"><script src="https://gist.github.com/AhnSeongHyun/7a5552dbf151fbd0ea24.js"></script></span>

<span style="color: rgb(85, 85, 85); font-family: 'Nanum Gothic', sans-serif; font-size: 17px; line-height: 28px; text-align: justify;">  
</span>

<span style="color: rgb(85, 85, 85); font-family: 'Nanum Gothic', sans-serif; font-size: 17px; line-height: 28px; text-align: justify;">  
</span>

<span style="font-size: 10pt;">위의 코드에서는 SMTP 기본 포트를 이용해서 로그인을 하고 메일을 보내는 작업을 하였는데 TSL 을 적용하기 위해서는 587 포트를 메일서버 연결시에 적용해 주어야 한다. (SSL 이라면 465) </span>

<span style="font-size: 10pt;">  </span>

<span style="font-size: 10pt;"><script src="https://gist.github.com/AhnSeongHyun/80489adf9c888c6a226e.js"></script></span>

<span style="color: rgb(85, 85, 85); font-family: 'Nanum Gothic', sans-serif; font-size: 17px; line-height: 28px; text-align: justify;">  
</span>



