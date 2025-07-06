---
title: 'mac port 설치하기.'
author: 'ash84'
pub_date: '2015-09-24'
description: 'yum, apt-get, make 같은 명령어를 사용하기 위해서는 mac port 라는 것이 필요하다. [이곳](http://www.macports.org/install.php)에 가면 각 OSX 버전 별로  .pkg 설치 파일을 받을 수 있도록 되어있다. 설치를 한 후에 해주어야 할일은 링크의 웹 페이지에도 잘 나와있지만,'
featured_image: ''
tags: ['apt-get', 'Mac port', 'yum', '맥포트']
---


<span style="font-size: 11pt;">yum, apt-get, make 같은 명령어를 사용하기 위해서는 mac port 라는 것이 필요하다.</span><span style="font-size: 11pt;"> [이곳](http://www.macports.org/install.php)에 가면 각 OSX 버전 별로  .pkg </span><span style="font-size: 11pt;">설치 파일을 받을 수 있도록 되어있다. 설치를 한 후에 해주어야 할일은 링크의 웹 페이지에도 잘 나와있지만, </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 10pt;">sudo port -v selfupdate</span>

</div><span style="font-size: 11pt;">를 해주어야 한다. 위의 명령어를 통해서 profiles가 최신으로 업데이트 된다고 나와있다.(아마도 설치할 목록이 최신으로 업데이트 되는거겠지.)</span>

<span style="font-size: 11pt;">그리고 자주 사용하는 간단한 명령어 2개는 **search** 와 **install** 이다. 내가 yum 이 필요하다고 하면 설치 전에 어떤 패키지들이 있는지 port search 를 통해서 검색할수 있다. </span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;">**<span style="font-size: 10pt;">sh-3.2# port search yum</span>**

<span style="font-size: 10pt;">py-yum-metadata-parser @1.1.4_1 (python)</span>

<span style="font-size: 10pt;">    Yum metadata parser</span>

<span style="font-size: 10pt;">py25-yum-metadata-parser @1.1.4_1 (python)</span>

<span style="font-size: 10pt;">    Yum metadata parser</span>

<span style="font-size: 10pt;">py26-yum-metadata-parser @1.1.4_1 (python)</span>

<span style="font-size: 10pt;">    Yum metadata parser</span>

<span style="font-size: 10pt;">py27-yum-metadata-parser @1.1.4_1 (python)</span>

<span style="font-size: 10pt;">    Yum metadata parser</span>

<span style="font-size: 10pt;">yum @3.2.29 (sysutils, archivers)</span>

<span style="font-size: 10pt;">    Automatic updater and package installer/remover for RPM</span>

<span style="font-size: 10pt;">yum-arch @2.2.2 (sysutils)</span>

<span style="font-size: 10pt;">    Extract headers from rpm in a old yum repository</span>

<span style="font-size: 10pt;">yum-createrepo @0.9.8_1 (sysutils)</span>

<span style="font-size: 10pt;">    generates common metadata for package repositories</span>

<span style="font-size: 10pt;">yum-utils @1.1.17 (sysutils)</span>

<span style="font-size: 10pt;">    Utilities based around the yum package manager</span>

<span style="font-size: 10pt;">Found 8 ports.</span>

</div><span style="font-size: 11pt;">그리고 나서 설치를 할때에는</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); background-color: rgb(255, 255, 255); padding: 10px;"><span style="font-size: 10pt;">port install yum</span>

</div><span style="font-size: 11pt;">이렇게 설치를 하면된다. 위의 명령어들은 port 명령 이런식으로 구성</span><span style="font-size: 11pt;">을 했는데 아예 port 를 입력한후 port 안에서 search, install 명령을 입력하면 된다. 좀더 다양한 mac port 의 명령어는 </span><span style="font-size: 11pt;">[여기](http://guide.macports.org/#using.port)를 참고하시길. </span>



