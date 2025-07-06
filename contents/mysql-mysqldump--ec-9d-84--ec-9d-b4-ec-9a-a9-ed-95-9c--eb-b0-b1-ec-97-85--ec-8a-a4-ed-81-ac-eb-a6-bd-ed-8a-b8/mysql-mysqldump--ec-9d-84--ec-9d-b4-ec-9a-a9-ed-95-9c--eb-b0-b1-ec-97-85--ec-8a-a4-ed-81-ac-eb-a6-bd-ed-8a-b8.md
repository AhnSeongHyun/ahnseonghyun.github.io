---
title: '(mysql) mysqldump 을 이용한 백업 스크립트'
author: 'ash84'
pub_date: '2015-09-24'
description: 'mysql 에 데이터가 쌓이다 보면 확실히 정해야 하는것중 하나가 백업 정책인것 같다. 특히 스타트업이나 개인 프로젝트에서 서버를 임대해서 사용하는 경우, 서버용량에 제한이 있다보니 어느정도 데이터가 쌓이다 보면 백업에 대해서 고려하지 않을수가 없다. 내가 세운 백업정책은 1일 1백업, 즉 일일백업인데, 사실 아직은 데이터가 많지 않은 상황에서 할수 있는 무식한 방법이다. 아래는 mysqldump를 사용한 백업 스크립트인데, 매일 오전 12시30분에 실행이 되도록 cronta'
featured_image: ''
tags: ['dev', 'MySQL', 'mysql 백업', 'mysqldump', '패스워드 없이']
---


<span style="font-size: 11pt;">mysql 에 데이터가 쌓이다 보면 확실히 정해야 하는것중 하나가 백업 정책인것 같다. 특히 스타트업이나 개인 프로젝트에서 서버를 임대해서 사용하는 경우, 서버용량에 제한이 있다보니 어느정도 데이터가 쌓이다 보면 백업에 대해서 고려하지 않을수가 없다. 내가 세운 백업정책은 1일 1백업, 즉 일일백업인데, 사실 아직은 데이터가 많지 않은 상황에서 할수 있는 무식한 방법이다. 아래는 mysqldump를 사용한 백업 스크립트인데, 매일 오전 12시30분에 실행이 되도록 crontab 에 스케쥴을 걸어놓은 상태이다.</span>

<span style="font-size: 11pt;"> </span>

<script src="https://gist.github.com/AhnSeongHyun/5963336.js"></script>

<div style="text-align: justify; line-height: 2;"><span style="font-size: 11pt; line-height: 2;">스크립트를 설명하자면, 현재 시간을 가져와서 백업파일명을 만들고, mysqldump 를 이용해서 백업을 한후, 압축을 한 다음에 원본 파일은 삭제하는 방식으로 진행하였다. 일일백업이다 보니 데이터가 서버에 금방 쌓이게 되는데 현재는 수작업으로 ftp 를 이용해서 가져온후 n드라이브에 백업하고 있지만 나중에는 ftp 부분 역시 스크립트로 작성하면 될것 같다. </span></div><div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="color: rgb(0, 0, 0); font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 11pt; line-height: 17.77777862548828px; white-space: pre;">mysqldump –single-transaction tt > ./</span><span class="nv" style="color: teal; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 11pt; line-height: 17.77777862548828px; white-space: pre;">$dailysql</span>

</div><span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">위의 mysqldump 명령어를 보면 tt 는 테이블 이름이고 백업한 부분에 대해서 redirect 를 이용해서 데이터를 파일로 만들어 주는 작업을 하고 있다. ` --single-transaction` 옵션은 덤프 도중에 다른 세션에서 insert, update, delete 가 가능하게 해주는 옵션이다. 기본적으로 백업을 하면서도 다른 스케쥴에 의해서 수행되는 수집 스케쥴에 문제가 생기지 않기 위해서는 이 부분을 설정해 주는게 좋다고 판단되어서 설정했다. </span>

<span style="font-size: 11pt;">기타 다른 옵션들은 아래의 링크를 참고하면 된다. mysqldump 명령어를 위의 스크립트대로 실행하려고 하면 분명히 user 와 패스워드에 대한 부분이 에러가 날것이다. 사실은 적어주어야 하는데, 귀찮아서 찾아보니 서버 자체에 저장해 두는 방법이 있다. </span>

<span style="font-size: 11pt;">/home/내계정 아래에 .my.cnf 라는 파일을 만든다. 그리고 아래와 같이 입력해 준다.</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 11pt;">[mysqldump]</span>

<span style="font-size: 11pt;">user=mysqluser</span>

<span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;"></span>

<span style="font-size: 11pt;">  
</span><span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">password=secret</span>

</div><span style="font-size: 11pt;">이렇게 입력하게 되면 mysqldump 에서 자동으로 이 값을 사용하기 때문에 일일히 명령어 뒤에 user 와 password 를 입력해줄 필요가 없다. 사실 좀 위험한 부분이라는 생각도 들고. </span>

<span style="font-size: 11pt;">자세한 옵션들이 많이 있는데, 나는 전체 데이터 베이스를 백업하는 방식을 사용했지만 where 문을 이용해서 분명히 하루에 대한 데이터만 가져와서 백업하는 것이 가능하다는 생각이 든다. 데이터의 크기나 서비스의 형태에 따라 다르기 때문에 그것은 스스로 판단해야 한다. </span>

<span style="font-size: 11pt;">**Reference**</span>

<span style="font-size: 11pt;">– </span><span style="font-size: 10pt; line-height: 1.5;">[<span style="font-size: 11pt;">http://intomysql.blogspot.kr/2010/12/mysqldump.html</span>](http://intomysql.blogspot.kr/2010/12/mysqldump.html)</span>

<span style="font-size: 11pt;">– </span>[<span style="font-size: 11pt;">http://stackoverflow.com/questions/9293042/mysqldump-without-the-password-prompt</span>](http://stackoverflow.com/questions/9293042/mysqldump-without-the-password-prompt)

<span style="font-size: 11pt;"> </span>



