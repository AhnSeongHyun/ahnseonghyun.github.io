---
title: 'swagger 와 redocly/redoc'
author: 'ash84'
pub_date: '2019-09-08'
description: ''
featured_image: ''
tags: ['swagger', 'redoc', 'redocly']
---

swagger 를 도입해서 쓰고 있는데 확실히 테스트가 가능하다는 점, 그리고 명확하게 request/response 모델을 보여 준다는 점에서 프론트엔드/클라이언트 개발자와 소통하는데 도움이 되는 것 같다. 그렇지만 마이크로서비스 상에서  swagger 를 사용하는 부분에 있어서 몇가지 고민이 있다. 

**하나는 어떻게 swagger.yaml 파일을 작성할 것인가 하는 것**인데, 손으로 작성하는 데는 한계가 있기 때문에 Java 에서는 바로 swagger 문법의 파일로 만들어 줄 수 있고(실제로 해 보진 않았다.), Python 에서는 이전에 소개했던 [fastapi](https://fastapi.tiangolo.com/) 나 [flask-restplus](https://flask-restplus.readthedocs.io/en/stable/swagger.html) 에서는 지원을 하고 있다**.** 

```python
    @api.route('/my-resource/<id>', endpoint='my-resource')
    @api.doc(params={'id': 'An ID'})
    class MyResource(Resource):
        def get(self, id):
            return {}
    
        @api.doc(responses={403: 'Not Authorized'})
        def post(self, id):
            api.abort(403)
```

**또 하나의 swagger 파일을 어디에 둘 것인가에 대한 고민이다.** 마이크로서비스는 앞에 client 와 만나는 부분도 있지만 API Gateway 뒤에서 더 많은 서비스들이 운영되기 때문에 그것들에 대한 swagger 파일은 어디에서 관리할 지가 고민이 된다. 제일 중요한 것은 당연히 API Gateway 에서 서비스되는 것들에 대한 endpoint 와 명세인데, 이것은 모두가 접근 가능한 별도의 서버를 띄워서 볼 수 있게 하는 것이 정답이고, 나머지 개별 마이크로 서비스들을 하나의 API 문서화된 사이트에서 계층적으로 보여주면 매우 좋지만 아직까지 그건 쉽지는 않은 것 같다. 

---

**일단 고민은 이러한데.. **

swagger file 을 어떻게 보여줄지에 대해서 더 생각을 해보면, 간단하게는 Confulence 에서 open api spec 관련 플러그인을 통해서 보여줄 수 도 있다. github repo 에 swagger file 을 올려두고 그 링크를 삽입하거나 아니면 full text yaml 을 넣어서 랜더링해서 보여줄 수 도 있다. 그렇지만 기본 swagger UI 는 여전히 아쉬움으로 남는다. 물론 swagger hub 같은 유료 툴을 사용할 수도 있다. 

 ![redoc](https://live.staticflickr.com/65535/48697610823_6605ecce41_z.jpg)


[redocly/redoc](https://github.com/Redocly/redoc) 은 좀 더 깔끔한 UI 를 제공한다. 이 툴의 장점은 서버의 형태로 띄울 수도 있고(docker 로도 제공하고 있다.), redoc-cli 를 통해서 static html 로도 만들수 있다는 점이다. 이렇게 만든 static html 은 github repo 상에서 `docs` 디렉토리 하위에 두고 github page 설정을 하게 되면 해당 페이지로 API 명세를 볼 수 있게 된다. 하나의 마이크로 서비스가 당연히 하나의 repo 에 연관되어 있고, 그 서비스에 대한 API 문서가 repo 의 github page 에 있다는것은 매우 직관적이고, 명시적인것 같다. 그리고 검색 기능도 제공을 하고 있고 다양한 언어로 payload 를 구현하는 기능을 제공하고 있다. 

 ![redoc](https://live.staticflickr.com/65535/48697950606_6acd7c2b1b_z.jpg)
 

특히 개인적으로 좋아하는 기능은 최상단 `info` 하위의 `description`  부분에서 markdown 으로 되어 있는 곳에서 `#`  헤더 문자에 대해서 left side menu 를 만들어 준다. 예를 들어 아래와 같이 되어 있는 경우 

```yaml
    swagger: '2.0'
    schemes:
      - http
      - https
    host: petstore.swagger.io
    basePath: /v2
    info:
      description: |
        This is a sample server Petstore server.
        You can find out more about Swagger at
        [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).
        For this sample, you can use the api key `special-key` to test the authorization filters.
        # Introduction
        This API is documented in **OpenAPI format** and is based on
        [Petstore sample](http://petstore.swagger.io/) provided by [swagger.io](http://swagger.io) team.
        It was **extended** to illustrate features of [generator-openapi-repo](https://github.com/Rebilly/generator-openapi-repo)
        tool and [ReDoc](https://github.com/Redocly/redoc) documentation. In addition to standard
        OpenAPI syntax we use a few [vendor extensions](https://github.com/Redocly/redoc/blob/master/docs/redoc-vendor-extensions.md).
        # OpenAPI Specification
        This API is documented in **OpenAPI format** and is based on
        [Petstore sample](http://petstore.swagger.io/) provided by [swagger.io](http://swagger.io) team.
        It was **extended** to illustrate features of [generator-openapi-repo](https://github.com/Rebilly/generator-openapi-repo)
        tool and [ReDoc](https://github.com/Redocly/redoc) documentation. In addition to standard
        OpenAPI syntax we use a few [vendor extensions](https://github.com/Redocly/redoc/blob/master/docs/redoc-vendor-extensions.md).
        # Cross-Origin Resource Sharing
        This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with  [W3C spec](https://www.w3.org/TR/cors/).
        And that allows cross-domain communication from the browser.
        All responses have a wildcard same-origin which makes them completely public and accessible to everyone, including any code on any site.
        # Authentication
        Petstore offers two forms of authentication:
          - API Key
          - OAuth2
```

 ![redoc](https://live.staticflickr.com/65535/48697950766_032cf9d0b3_z.jpg)

이렇게 사이드 메뉴가 생기고 그 안에서 각각의 사항으로 접근 할 수 있게 해준다. API 문서상에서 정책이나 그런 설명적인 부분을 쓰고 싶은 경우가 많은데, 이런 기능을 통해서 Authorization, Encrpytion 등의 규칙 등을 삽입할 수가 있다. 

이 툴의 단점 중 하나는 아직까지는 [multiple swagger spec URL 을 공식적으로 지원하지는 않는다](https://github.com/Redocly/redoc/issues/605#issuecomment-412455541)는 점이다. 마이크로서비스 상에서 여러 서비스의 spec URL을 한번에 서비스별로 이 툴을 이용해서 보여주려면 swagger 파일을 합치거나 개별로 띄우거나, Live Demo 사이트에 있는 상단처럼 URL 을 서비스별로 자동완성 시켜서 보여주는 수 밖에는 없다.

그리고 기존의 swagger 에서는 테스트가 가능했다면, redoc 에서는 제공하지는 않는다. 테스트가 꼭 필요하다면 비추천이지만, 필요하지 않고, 다른것으로 대체가 가능하다면 redoc 을 추천한다.

---

**Reference** : 
- [파이썬 웹서버 REST API 문서 쉽고 빠르게 작성하기](https://www.slideshare.net/YongseonLee1/pycon-korea-2019-rest-api-document-generation-164504789) 
- https://github.com/DragorWW/awesome-swagger
