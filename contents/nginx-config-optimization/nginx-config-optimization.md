---
title: '[번역] How To Optimize Nginx Configuration(Nginx 의 설정 최적화)'
author: 'ash84'
pub_date: '2015-03-19'
description: 'Nginx 에 대해서 몇가지 관심을 갖다가 설정에 따른 성능향상, 영향에 대해서 쓴 글을 보게 되었는데 공부할겸 정리해 둔다. 거창하게 제목에 번역이라고 달았지만, 그냥 아는단어를 한글화 했다고 보면 된다. 아래의 링크는 원문링크이다. 오류가 있다면 댓글로!'
featured_image: ''
tags: ['dev', 'How To Optimize Nginx Configuration', 'nginx', 'nginx optmize', 'nginx 설정', 'nginx 설정 최적화']
---


<span style="font-size: 11pt;">Nginx 에 대해서 몇가지 관심을 갖다가 설정에 따른 성능향상, 영향에 대해서 쓴 글을 보게 되었는데 공부할겸 정리해 둔다. 거창하게 제목에 번역이라고 달았지만, 그냥 아는단어를 한글화 했다고 보면 된다. 아래의 링크는 원문링크이다. 오류가 있다면 댓글로!</span>

<div class="txc-textbox" style="border: 1px solid rgb(203, 203, 203); padding: 10px; text-align: justify; line-height: 2; background-color: rgb(255, 255, 255);">[<span style="font-size: 11pt;">https://www.digitalocean.com/community/tutorials/how-to-optimize-nginx-configuration</span>](https://www.digitalocean.com/community/tutorials/how-to-optimize-nginx-configuration)

</div>#### <span style="font-size: 11pt;">worker_processes</span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">– nginx 의 중추적인 역할, core당 1 worker process</span>

<span style="font-size: 11pt;">  
</span>

#### <span style="font-size: 11pt;">worker_connection </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">– 얼마나 많은 사람들이 nginx 로 동시에 접근가능한지, </span>

<span style="font-size: 11pt;">– ulimit -n 을 통해서 측정해서 사용해라. </span>

<span style="font-size: 11pt;">  
</span>

#### <span style="font-size: 11pt;">buffer size</span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">– 너무작으면 빈번히 nginx 가 디스크에 read/write 를 임시파일을 쓰기 위해서 일으킨다. </span>

<span style="font-size: 11pt;">– client_body_buffer_size : 클라이언트 버퍼 사이즈, POST Action 과 연관이 있다. </span>

<span style="font-size: 11pt;">– client_header_buffer_size : 클라이언트 헤어 버퍼 사이즈 1KB</span>

<span style="font-size: 11pt;">– client_max_body_size : 클라이언트에서 허용되는 최대 사이즈, 초과하게 되면 413 error를 뱉거나 Request Entity Too Large 를 리턴</span>

<span style="font-size: 11pt;">– large_client_header_buffers : 큰 클라이언트의 헤더를 위한 개수와 사이즈 지정 </span>

<span style="font-size: 11pt;">  
</span>

#### <span style="font-size: 11pt;">Timeouts</span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">– 성능을 개선할수 있다. </span>

<span style="font-size: 11pt;">– client_body_timeout </span>

<span style="font-size: 11pt;">– client_header_timeout </span>

<span style="font-size: 11pt;">이 두개는 client 가 요청수 서버의 응답을 기다리는 시간. 초과시 408 에러, request time out </span>

<span style="font-size: 11pt;">– keepalive_timeout : 클라이언트의 keepalive connection 의 시간 설정 </span>

<span style="font-size: 11pt;">– send_timeout : 특정(지정한) 시간 이후에 클라이언트가 아무것도 하지 않으면 연결 종료시킨다. </span>

<span style="font-size: 11pt;">  
</span>

#### <span style="font-size: 11pt;">GZIP Compression </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">– nginx 에서 처리해야 하는 네트워크의 양을 줄인다. gzip_comp_level을 너무 높이면 cpu cycle을 낭비하게 된다. </span>

<span style="font-size: 11pt;">  
</span>

#### <span style="font-size: 11pt;">Static File Caching </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">– header 에 쓰이는 파일(변하지 않고 서버에서 정기적으로 제공하는)에 만기(expire)를 설정해라. server 블록에 있다. </span>

<span style="font-size: 11pt;">  
</span>

#### <span style="font-size: 11pt;">Logging</span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">– nginx 를 모든 요청 로그를 남긴다. 꺼라 </span>

<span style="font-size: 11pt;">  
</span>

#### <span style="font-size: 11pt;">결론 </span>

<span style="font-size: 11pt;">  
</span>

<span style="font-size: 11pt;">– 알맞게 설정된 서버가 가장 중요한데 이것은 모니터링을 해보고 적절히 수정해 봐야 한다. 위의 설정 중 영원한 것은 없으며, </span><span style="font-size: 11pt; line-height: 2;">각각의 독특한 경우에 맞게 조정이 필요하다. 그리고 나서 로드 밸런싱이나 수평적 확장을 알아보면 된다. </span>

<span style="font-size: 11pt; line-height: 2;">  
</span>



