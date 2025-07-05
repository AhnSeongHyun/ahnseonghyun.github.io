---
title: 'Ansible 간단이해'
author: 'ash84'
pub_date: '2017-03-28'
description: ''
featured_image: 'http://theeye.pe.kr/wp-content/uploads/2016/02/ansible_logo-1.png'
tags: ['ansible', 'dev', 'Python', 'server']
---



#개요

- 간단히 애기하자면 내 컴퓨터에서 서버에 원격접속 혹은 직접적인 ssh 접근을 하지 않고 뭔가 작업, 혹은 배포를 할때 사용하는 툴이다.
- 파이썬 기반으로 되어 있다.

### 설치

- python 2.6 이상 권장, 그 이하 버전에서 설치하면 별도의 라이브러리를 설치해야 한다. 

```bash 
sudo pip install ansible 
```

### 윈도우 작동 관련

- Ansible 1.7 버전 이하에서는 원래 윈도우 지원하지 않았다.
- 1.7이상부터 조건부 지원을 하고 있는데 ssh 대신에 PowerShell 을 사용할때만 가능(일반 cmd 불가)
- 윈도우서버를 제어하는 서버가 리눅스라면 파이썬 모듈인 **winrm** 을 설치해야 한다. 
- 기타 윈도우 관련 별도의 사항은 [http://docs.ansible.com/intro_windows.html](http://docs.ansible.com/intro_windows.html) 를 참고한다. 

### 간단이해하기
 
![](http://ash84.net/wp-content/uploads/1/cfile30.uf.2122BE4C5472B0C31A9175.png)

- hosts : 호스트 파일인데, 한마디로 ansible 을 통해서 작업을 할 대상 서버 ip/주소 리스트라고 보면 된다. 

- [name] 형식으로 변수형태로 줄수가 있다. 아래의 hosts 파일을 보면 [webservers] 라고 해 놓으면 나중에 playbook 내에서 특정 작업을 정의할때 해당 작업을 어디서 할지를 hosts 를 통해서 지정할수가 있다. 

```
[local]  
127.0.0.1


[dev]  
xxx.net

  
[webservers]  
xxx.com
```

- hosts 파일은 기본적으로 `/etc/ansible` 아래에 파일로 위치하는것이 기본인데, 그게 싫으면 다른곳에 작성하고 ansible 실행시 지정해 주면된다. 

- Playbook - yaml(야믈) 기반의 문법으로 작성된 일종의 작업작성 문서라고 보면 될듯

- .yaml 확장자를 가진다. 

- 여러개의 play 를 가진다. 

- play - 하나의 play 는 작업에 대한 내용과 어디서 작업을 해야하는지에 대한 정보를 가지고 내부적으로 tasks 를 가진다. 

- name 은 작업의 이름, hosts 는 작업할 서버이다. 

- tasks 
  - task 의 집합
  - task 는 name 과 함께 module 을 가지는데 위의 그림에서 yum, service 그런 것들이 module 이다. 


- module
  - 모듈은 한마디로 프로그램, 툴이라고 생각하면 되는데 우리가 사용하는 yum , apt-get, git, copy, shell, command,  pip 같은것들이 모듈이라고 지칭하고 있다. 
  - 즉, task 에서 어떤 모듈을 사용해서 어떤 작업을 할것인지를 지정하는 것이다. 
  - 위의 그림을 해석하자면, 2개의 task 가 있는데 yum 모듈을 이용해서 httpd 를 설치하고 service 모듈을 이용해서 httpd 를 시작하는 작업을 하고 있다. 

- [http://docs.ansible.com/list_of_packaging_modules.html](http://docs.ansible.com/list_of_packaging_modules.html) 여기에 가면 모듈 패키지를 볼수가 있다. 각각의 모듈은 자신만의 파라미터들을 가지는데 그 부분을 잘 확인해봐야 한다.


### 간단 실습해보기 

- hosts 작성 : 일단 localhost 로 작성. 

<script src="https://gist.github.com/AhnSeongHyun/b1df358fac9e83b578c7.js"></script>

- 기본 ping Test

- 여기서 `—ask-pass` 라고 옵션을 주고 있는데, 이 옵션을 주면 아래와 같이 작업대상의 ssh 암호입력을 물어보는데, 기본적으로 리눅스에서 ssh 에 대한 인증이 필요하다. —ask-pass 를 하지 않으면 ssh-key 나 그런 ssh 인증을 피해가거나 자동으로 할수 있는 밑작업들을 해줘야 하는데 여기서는 특별히 그런 작업을 하진 않았다. 관련 사항은 [http://soul.tistory.com/37](http://soul.tistory.com/37) 이쪽 부분에서 ssh-keygen 을 이용하는 방법을 봐야할것 같다. 


<script src="https://gist.github.com/AhnSeongHyun/b1df358fac9e83b578c7.js"></script>

- test.yaml 작성하기 : 여기서는 간단하게 shell 모듈을 이용해서 특정 위치에 test 디렉토리를 생성해 보겠다. 

<script src="https://gist.github.com/AhnSeongHyun/dfe9351365c0b76b2c7b.js"></script>

- 작성한후, 실행할때에는 ansible-playbook 을 이용한다. 

<script src="https://gist.github.com/AhnSeongHyun/d83626ebca6c25b53567.js"></script>



