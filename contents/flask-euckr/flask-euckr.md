---
title: 'euc-kr data in flask'
author: 'ash84'
pub_date: '2015-07-16'
description: '### **파이썬에서의 unicode와 str**

- 유니코드는 평문이고, str은 암호화된 유니코드라고 생각하자.
- charset 은 str 을 만들기 위한 키이다. 즉, unicode 에서 str 을 만들려면 charset이 필요하고, str에서 unicode 를 만들려면 charset이 필요하다.

[![image2015-6-25 16 29 58](https://farm1.staticflickr.com/353/19544431756_5af01e9694_z.jpg'
featured_image: ''
tags: ['dev', 'euc-kr', 'euckr', 'Flask', 'flask euc-kr', 'Python']
---
### **파이썬에서의 unicode와 str**

- 유니코드는 평문이고, str은 암호화된 유니코드라고 생각하자.
- charset 은 str 을 만들기 위한 키이다. 즉, unicode 에서 str 을 만들려면 charset이 필요하고, str에서 unicode 를 만들려면 charset이 필요하다.

<div class="jetpack-video-wrapper">[![image2015-6-25 16 29 58](https://farm1.staticflickr.com/353/19544431756_5af01e9694_z.jpg)](https://flic.kr/p/vM5jDj)</div>- 문제점 : str 상태의 문자열은 어떤 charset 으로 인코딩 되었는지를 알수 없다.
- 때문에 개발자는 encode, decode 함수를 이용할경우에는 반드시 charset 을 알고 있어야 한다.

 

### **유니코드를 입력하는 방법**

- u’한글’ 이렇게 문자열 입력시, 제일 앞에 u 라는 글자를 입력하면 유니코드로 인식을 한다.
- “한글” 이렇게 문자열 입력시, str 로 인식인 하기 때문에 decode 를 해줘야 한다. `"한글".decode('utf-8')`
- `unicode("한글")` 이렇게 입력하는것은 decode와 같은 역할을 하는데, charset 을 입력하지 않으면 현재 default charset 으로 변환 기준을 잡는다.
- `unicode("한글", charset)` 이렇게 charset 을 명시해주자.

자, 파이썬에서의 유니코드와 str 간의 문제점은 결국 charset을 무엇을 사용하는지에 대해서 알고 있으면 해결된다.(아니면 어쩌지..)

### **flask 에서의 문제점**

 flask 에 오면 이야기가 달라진다. flask 는 기본적으로 utf-8 로 유니코드를 인코딩해서 전송하는것을 기본으로 하고 있고, 내부적으로 unicode 기반으로 작동을 한다. 이것은 flask 를 만든 개발자의 배려인데, 들어오는 요청(request)을 charset 으로 decode 작업을 한다. 즉, 우리가 사용하는 request.args.get, request.form 은 이미 전단계에서 지정된 charset 으로 decoding 이 된 값이 들어가 있다.

[Unicode in Flask](http://flaskr.readthedocs.org/ko/flas_kr/ko/unicode.html?highlight=sqlalchemy)

**그렇다면 뭐가 문제일까?**

간혹 이런 경우가 있다. 요청을 POST로 보내게 되는데 해당 데이터는 euc-kr로 되어있는데, Content-Type 은 별도로 명시되지 않고, POST 자체 파라미터에 CHARSET=’euc-kr’ 이런식으로 지정해서 보내는 경우…(이게 뭔짓인지…)

이 경우에는 문제가 생긴다. flask 에서는 charset이 기본 utf-8로 지정되어 있다. 이 부분은 Request 클래스의 조상격인 [BaseRequest](https://github.com/mitsuhiko/werkzeug/blob/d4e8b3f46c51e7374388791282e66323f64b3068/werkzeug/wrappers.py/#L121)
 클래스를 보면 되는데, charset 변수에 다음과 같이 지정되어 있는것을 확인할 수있다. 문제는 flask 자체에서 euc-kr 로 데이터를 utf-8로 해석해서(decode) unicode 라고 던져준다. 사실은 잘못 decode 된 데이터인데 말이다. 개발자는 `type()` 함수를 통해서 unicode 임을 확인하지만 결국 문자열 조합 등의 관련 문자열 처리에서 문제가 생길 것이다.

<script src="https://gist.github.com/AhnSeongHyun/e4c2bb413f7e00037af2.js"></script>


만약 모든 데이터가 항상 euc-kr 로만전송이 된다면(전송되는 모든 데이터가 euc-kr 기준이라면), Request 클래스의 서브클래스를 만들고 charset을 euc-kr로 지정해 주면 된다. 그리고 나서 <cdoe>app.request_class 에 해당 클래스를 연결 시켜줘야 한다. 그러나 이 방식의 단점은 2가지인데, 하나는 항상 모든 요청이 euc-kr로 들어와야 한다는 점과 app(Flask 인스턴스)이 생성후에 지정할수 있고, 중간에 또 바꿀 수 없다는 점이다.</cdoe>

<script src="https://gist.github.com/AhnSeongHyun/f2e0a9cc58108b8a93c2.js"></script>


<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>


<!-- 페이지내_긴_배너 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8699046198561974"
     data-ad-slot="5480877276"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>

만약 content-type 에 따라서 charset을 변경해야 한다면,(사실은 이게 정석이다)  
[`werkzeug.contrib.wrappers.DynamicCharsetRequestMixin`](http://werkzeug.pocoo.org/docs/0.10/contrib/wrappers/) 을 사용하면 된다. 그러나 위의 방안은 제시한 상황처럼 전달되는 데이터에서 charset 을 추출해서 사용하는 동적인 상황에서는 사용할 수 가 없다.(content-type 내 charset 전달 여부 역시 확실하지 않다.)

<script src="https://gist.github.com/AhnSeongHyun/c995d2a6afd1bb54ab34.js"></script>

위의 코드에서 보면 `request.get_data()` 를 사용하고 있다. 기존에는 GET 에는 `request.args` 를 POST에는 `request.form` 을 이용해서 데이터를 가져왔는데, args 와 form 은 클래스 내 charset 변수에 의해서 decode 되기 때문에 사용할 수가 없다.

decode 전 데이터는 `request.get_data()` 를 통해서 가져올수 있는데, 대신에 파싱을 통해서 데이터를 추출 해야한다. decode_raw_data 함수는 query string 형식의 데이터를 dict 객체에 담고나서, urldecode 를 수행하고, 그 데이터를 다시 decode(charset) 하고 있는 코드이다. 즉, 기존의 flask 에서 해줬던 부분을 개발자가 코드에서 직접 해주어야 한다. 이렇게 되면 euc-kr 데이터를 받아서 decode 를 해서 unicode의 형태로 파이썬내에서 사용할 수가 있다. 

   
 실제로 국내의 경우 아직도 euc-kr을 사용하는 경우가 많기 때문에 그런 사이트와의 연동 작업에서는 euc-kr을 default로 하는 것이 기본이다. 물론 utf-8을 사용하는 것이 좋다. 그렇지만 중요한 것은 content-type 같이 일반적으로 charset 정보를 전달하는 곳에 명시하는게 가장 베스트라는 생각이 들고 개인적으로 POST 나 GET 요청시에 파라미터로 charset 값을 전달하는 것은 비추해야 한다고 생각한다.



