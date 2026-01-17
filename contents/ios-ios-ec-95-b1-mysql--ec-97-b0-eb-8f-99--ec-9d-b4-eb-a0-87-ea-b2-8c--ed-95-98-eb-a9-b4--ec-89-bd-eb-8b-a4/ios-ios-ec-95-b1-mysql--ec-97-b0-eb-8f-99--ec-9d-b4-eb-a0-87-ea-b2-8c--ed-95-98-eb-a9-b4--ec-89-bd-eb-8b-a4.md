---
title: '(iOS) iOS앱 - mysql 연동, 이렇게 하면 쉽다.'
author: 'ash84'
pub_date: '2012-11-07'
description: 'mysql 서버는 다들 아시다시피 워낙 많이들 쓰는 데이터베이스 서버이기 때문에 사실 개인이나 작은 회사에서 뭔가를 만들때 사용되는 DB서버는 mysql 이라고 보면된다. 개인적으로 회사에서 몇번 써본적이 있지만, 아이폰 관련 개발에서는 사실 파일디비 형태인 sqlite3를 사용해 보았다. 
mysql 을 연동하는 포스팅을 쓰는 가장 큰 이유는 iOS의 Cocoa 프레임워크 상에서 따로 DB연결 관련 클래스'
featured_image: ''
tags: ['dev', 'iOS', 'iOS DB 연동하기', 'MySQL', 'MYSQL 연동하기']
---
<span style="font-size: 11pt;">mysql 서버는 다들 아시다시피 워낙 많이들 쓰는 데이터베이스 서버이기 때문에 사실 개인이나 작은 회사에서 뭔가를 만들때 사용되는 DB서버는 mysql 이라고 보면된다. 개인적으로 회사에서 몇번 써본적이 있지만, 아이폰 관련 개발에서는 사실 파일디비 형태인 sqlite3를 사용해 보았다. </span>

<span style="font-size: 11pt;">mysql 을 연동하는 포스팅을 쓰는 가장 큰 이유는 iOS의 Cocoa 프레임워크 상에서 따로 DB연결 관련 클래스나 라이브러리를 따로 제공해 주지 않기 때문이다.(아니면 아직 내가 못찾을것인지도.) 그래서 맥부기 사이트에서 찾아봐도 대부분의 사람들이 mysql에 직접 접근해서 데이터를 가져오기 보다는 중간에 미들웨어 형태로 두던지 아니면 php-mysql의 형태로 데이터를 파싱해서 읽어오는 경우도 있다. </span>

<span style="font-size: 11pt;">보안상 사실 이 방법은 mysql 서버 접근 정도를 코드안에 심는 방식이기 때문에 불안할 수도 있지만, 중간에 서버를 두는것이 불편하거나 그럴 여유가 없는 분들을 참고하시길 바란다. </span>

<span style="font-size: 11pt;">일단 이 방법은[ MySQL and Objective-C for iPhone and OSX](http://miinyx.wordpress.com/2011/08/25/mysql-and-objective-c-for-iphone-and-osx/) 이라는 글을 기반으로 한다. 링크를 가서 보면 알겠지만, [http://www.karlkraft.com/](http://www.karlkraft.com/)이라는 사이트에 올라온 자료를 토대로 만들면 된다. 필자는 링크에 있는 블로그에 올려진 것을 대상으로 작업을 해 보았으나 실패했다. 그래서 찾은 방법은, 제작자의 svn에서 직접 소스를 다운받는 방법이다. </span>

<div class="txc-textbox" style="border: 1px solid #cbcbcb; background-color: #ffffff; padding: 10px;"><span style="font-size: 11pt;">**svn trunk : https://svn.karlkraft.com/mysql_connector**</span>

</div><span style="font-size: 11pt;">svn 툴은 알아서 사용하길 바란다. 필자의 경우, 이클립스 플러그인을 통해서 mysql_connector 의 최신 버전을 받았다. 그 이후부터는 위의 블로긔 링크와 같다. 받은 mysql_connector를 프로젝트에 넣는다.  </span>

<span style="font-size: 11pt;">중요한 부분은 반드시 Add to targets  부분에서 현재 프로젝트를 꼭 체크해 주도록 하자. 필자의 경우 다음과 같이 MysqlServer.m 파일에 mysql 접속 정보를 입력하였다. 참고로 scheme라는 부분은 mysql 에서 데이터베이스 명(이름)과 같기 때문에 그것을 써주면 된다. </span>

<span style="font-size: 11pt;"> </span>

<script src="https://gist.github.com/4017349.js">// <![CDATA[
 
// ]]></script>

<span style="font-size: 11pt; line-height: 2;">이렇게 입력하고 나서 간단하게 데이터베이스에 있는 동네이름을 가져오는 부분은 다음과 같다.   select 부분은 아래와 같이 하면 되고 그외 다른 쿼리 부분은 [이곳](http://miinyx.wordpress.com/2011/08/25/mysql-and-objective-c-for-iphone-and-osx/)을 참고하자.([원작자배려](http://miinyx.wordpress.com/2011/08/25/mysql-and-objective-c-for-iphone-and-osx/)) 참고로 select 부분에서 쿼리의 결과는 여러개가 있으면 배열로 받고, 각 배열의 내용은 컬럼명-값 형태, NSDictionary 의 형태로 되어 있다.</span>



