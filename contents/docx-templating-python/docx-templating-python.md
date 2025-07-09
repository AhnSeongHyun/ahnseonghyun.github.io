---
title: 'docxtpl 를 이용한 문서 자동화'
author: 'ash84'
pub_date: '2016-07-15'
description: '엑셀의 경우, 백오피스나 CMS 등에서 import/export 에 사용하기 때문에 기능구현 할 때  [XlsWriter](https://github.com/jmcnamara/XlsxWriter) 를 이용해서 구현했던 적이 있었다. 그에 비해서 워드 문서를 생성해 내는 작업은 별로 없었다. 

###발단은 이렇다. 
 
로그 분석을 해서 통계를 내고, 워드 문서파일의 보고서 형식으로 만들어서 올리는 작업을 매월 하고 있는데, 통계를 내는건 스크립트로 해결을 해왔는데, 그 시간보다 보고서를 작성하는 시간이 더 오래 걸렸다. 물론 사내'
featured_image: ''
tags: ['dev', 'Python', '워드문서', 'docx']
---

엑셀의 경우, 백오피스나 CMS 등에서 import/export 에 사용하기 때문에 기능구현 할 때  [XlsWriter](https://github.com/jmcnamara/XlsxWriter) 를 이용해서 구현했던 적이 있었다. 그에 비해서 워드 문서를 생성해 내는 작업은 별로 없었다. 

###발단은 이렇다. 
 
로그 분석을 해서 통계를 내고, 워드 문서파일의 보고서 형식으로 만들어서 올리는 작업을 매월 하고 있는데, 통계를 내는건 스크립트로 해결을 해왔는데, 그 시간보다 보고서를 작성하는 시간이 더 오래 걸렸다. 물론 사내 시스템으로 올리는 시간도 만만치는 않다. 그렇지만, 사내 시스템 부분은 관할구역이 아니기에 포기하고, 보고서 작성을 자동화 할 수 없을까 생각하게 되었다. 

보고서 워드 문서는 그 자체로 형식이 있기 때문에 그 형식을 template 로 두고 통계나 날짜 값들만 넣을 수 있으면 좋겠다라고 생각하고 찾아본 결과 파이썬 라이브러리인 docxtpl 을 찾게 되었다. 

**docxtpl** : http://docxtpl.readthedocs.io/en/latest/

```python
    from docxtpl import DocxTemplate
    doc = DocxTemplate(template_path)
    context = render_payload
    doc.render(context)
    doc.save(output_file_path)
```

아직 그렇게 star 수가 많지는 않은데 일단 jinja2 template 을 이용하고 있다는 점과 위의 코드처럼, template 파일경로와 내가 원하는 output 경로를 넣으면 되기 때문에 간결하다. 중간에 ```render``` 라는 함수에는 context 라고 dict 형식으로 데이터를 넣으면 된다.(이 함수도 마음에 든다, make, create, generate 가 아니라서 다행..) 

예를 들어, 아래와 같이 사용할 수 있다.

```json

payload = { 
  'name' : 'ash84', 
  'date' : '2016년 5월 1일 부터  ~  2016년 5월 31일 까지', 
  'daily_avg_count' : 25000, 
  'monthly_avg_count' : 2225000
  }
  
doc.render(payload)
```

그리고 해 줘야 할 것은 **template 대상 문서에 값이 들어갈 곳에 템플릿 문법으로 지정**해 주면 된다. 

```
작성자 : {{name}}
작성일자 : {{date}}

일별 평균 로그 수 : {{daily_avg_count}}
월별 평균 로그 수 : {{monthly_avg_count}}
```

docxtpl 은 한글에 대한 부분은 본문의 경우에는 잘 지원이 되는 것 같은데 template 파일의 머릿말, 꼬리말 부분에 있는 한글의 경우 ```render()``` 과정에서 에러가 발생하는 경우도 있었다. 그리고 표를 생성하는 부분은 아직까지 잘 지원은 안되는 것 같다.(지원한다고 하는데 사용하기는 쉽지 않은듯.)

사용해서 결과적으로 원래 워드파일을 복사해서 통계데이터를 보며 내가 일일히 값을 입력하던 삽질에서 벗어나게 되었다. 솔직히 이 작업을 하면서 드는 생각은 **"개발한 시간이 더 클까?"** 아니면 **"노다가 해온 시간과 앞으로 노가다한 시간이 더 클까?"** 에 대한 고민을 많이 했는데, 해 놓으니까 역시 편하긴 편한것 같다. 




**Reference:** 

- docxtpl : http://docxtpl.readthedocs.io/en/latest/
- XlsWriter : https://github.com/jmcnamara/XlsxWriter
