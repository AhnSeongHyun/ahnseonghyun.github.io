---
title: 'postman and postman2md'
author: 'ash84'
pub_date: '2018-05-19'
description: ''
featured_image: 'https://farm1.staticflickr.com/694/21682297821_bf00b22e44_o.png'
tags: ['dev', 'postman', 'postman to markdown']
---


 


## **postman**
 <br/>
    
 API 작업을 할때 테스트할수 있는 툴이 필요한데, 쉽게 테스트 할수 있는 [postman](https://www.getpostman.com/) 이라는 툴이 있다. 로그인도 필요없고 쉽게 GET, POST 등의 HTTP 기반의 API들을 테스트할수 있다. **특히 history 기능이 있어서 매우 좋은데 언제 들어가더라도 이전에 내가 테스트했던 내역들을 볼 수가 있다.** postman 이 2.0 으로 버전업을 하면서 로그인을 할 수가 있고 collection 이라는 개념을 도입했다. collection 은 기존의 테스트 내역에 대한 집합개념인데, 내가 테스트 했던 것들을 묶어서 관리 할 수가 있다. 그래서 여러 collection 을 만들수 있는데, 특별한 기능중 하나는 collection 즉, 테스트 항목의 집합들을 json 형태로 다운 받는 기능을 제공하고 있다.    
    
[![postamn2](https://farm6.staticflickr.com/5779/21052116563_4b34548e0c_o.png)](https://www.flickr.com/photos/sh84ahn/21052116563/in/dateposted-public/ "postamn2")<script async="" charset="utf-8" src="//embedr.flickr.com/assets/client-code.js"></script>

 


## [postman2md](https://github.com/Plate-Project/postman2md) 소개 및 개발기 ##
<br/>
   
[postman-to-markdown(이하 postman2md)](https://github.com/Plate-Project/postman2md)은 **postman 에서 다운받은 collection json 형식을 markdown 으로 변환해주는 파이썬(python)으로 만든 툴이다.** 일단 보통 API 를 정의하고(문서가 아닌 대략 생각으로) 만들면서 postman 으로 테스트하는 방식으로 개발을 하게 되는데, 차후에 다시 개발한 것을 바탕으로 API 문서를 markdown 형식으로 만드는 과정을 거치는 것을 알게 되었다.(다른 분들은 다른 과정으로 개발하겠지만.) 그래서 굳이 다시 API를 보고 markdown 을 만들기 보다는 테스트한 postman을 이용해서 어느정도의 markdown 기반의 API문서를 만드는게 필요하다고 생각하게 되었다.  
    
<script src="https://gist.github.com/AhnSeongHyun/ef357ad9b3513bd27b50.js"></script>사용법은 위와 같다. postman collection json은 내부에 하나 이상의 API 테스트를 가지고 있기 때문에 markdown 파일 역시 하나 혹은 하나이상으로 만들지를 선택할수 있는데 `multi_file` 에 false 값을 주게 되면 하나의 파일로 만들어 준다. 만들어지는 파일의 경로는 현재 경로에서 해당 collection 이름의 디렉토리가 생기고 하위에 파일로 생긴다. 예를들면 example.json.postman_collection 파일내 name 항목이 example 이라면, example 이라는 디렉토리를 만들고, 그 안에서 각 API 의 이름에 따라서 markdown 파일을 만들어 준다. 만약 `multi_file`를 false로 설정했다면, example.md 라는 이름으로 하나의 파일이 생성된다.

   
![스크린샷 2015-10-03 오전 10.51.39](https://farm6.staticflickr.com/5754/21910080011_03e0c3071e_o.png)

<script async="" charset="utf-8" src="//embedr.flickr.com/assets/client-code.js"></script>

   
 markdown 내에는 **ResourceURL, Request Parameters, Request Example** 헤더를 두어서 작성하고 있는데, 아쉽게도 postman collection json 에서는 response 에 대해서는 저장하고 있지 않기 떄문에 Response에 대해서는 보여줄 내용이 없다. 그리고 아직은 [postman2md](https://github.com/Plate-Project/postman2md) 에서 headers 부분은 markdown으로 만들고 있지는 않다.  
    
<script src="https://gist.github.com/AhnSeongHyun/eddda045fdeb2fa6f48b.js"></script>  [postman2md](https://github.com/Plate-Project/postman2md) 는 내부적으로 [markdownwriter](https://github.com/mikrosimage/python-markup-writer) 라이브러리를 이용하고 있다. postman2md `__init__.py` 를 보면 json 파싱 부분과 [markdownwriter](https://github.com/mikrosimage/python-markup-writer) 사용하는 부분을 볼 수 있다.    
  


## postman 팁 한 가지더

   
 postman 에서 프로그래밍 언어별로 테스팅한 API에 대한 코드조각을 받을수가 있다. 다양한 언어를 지원하고 있는데 특이한 점은 각 언어별로 API를 호출하는 여러 방식을 지원하고 있다는 점이다. 예를 들면, 파이썬의 경우, python3 를 선택하면 `http.client` 에 있는 라이브러리로 코드를 표시하지만, `requests`를 선택하면 해당 라이브러리에 맞게 설정된 코드가 출력된다.

![postman9](https://farm1.staticflickr.com/714/21682297691_cb9bf4bec2_o.png)
   
![postman11](https://farm6.staticflickr.com/5737/21052116343_6d5db1527c_o.png)
 


