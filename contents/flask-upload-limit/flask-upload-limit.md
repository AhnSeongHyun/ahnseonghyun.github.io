---
title: 'flask 파일업로드 검증하기'
author: 'ash84'
pub_date: '2018-09-10'
description: '파일 업로드의 경우 주의할 점이(업로드를 당하는 입장에서) 악성파일 혹은 원치 않는 파일들이 들어올 수 있음을 항상 인지해야한다. 그래서 왠만하면 파일 업로드를 잘 안만들거나 내부에서 몇명의 인가된 사용자만 따로 업로드 메뉴를 보이게 해서 제공하거나 하는 식으로 하곤 했었다. 그래도 업로드가 필요할 경우 아래와 같은 방법으로 제한 할 수 있다. 

- 파일 확장자 체크
- 사이즈 체크
- mime type 체크

그렇지만, **파일 확장자는 언제나 변경가능하기 때문에 위험하다.** 예를 들어, 악성 자바스크립트, 웹쉘 같은 파일들을'
featured_image: ''
tags: ['dev', 'Python', 'Flask', 'upload file', 'fleep']
---
파일 업로드의 경우 주의할 점이(업로드를 당하는 입장에서) 악성파일 혹은 원치 않는 파일들이 들어올 수 있음을 항상 인지해야한다. 그래서 왠만하면 파일 업로드를 잘 안만들거나 내부에서 몇명의 인가된 사용자만 따로 업로드 메뉴를 보이게 해서 제공하거나 하는 식으로 하곤 했었다. 그래도 업로드가 필요할 경우 아래와 같은 방법으로 제한 할 수 있다. 

- 파일 확장자 체크
- 사이즈 체크
- mime type 체크

그렇지만, **파일 확장자는 언제나 변경가능하기 때문에 위험하다.** 예를 들어, 악성 자바스크립트, 웹쉘 같은 파일들을 .png, .jpg, .docx 등과 같이 업무에서 자주 사용하는 파일 확장자로 변경해서 올릴 여지가 여전히 있다. mime type 체크 역시 웹프레임워크 상에서 내려주는 값을 보면 문제가 생긴다. 

[http://flask.pocoo.org/docs/1.0/patterns/fileuploads/](http://flask.pocoo.org/docs/1.0/patterns/fileuploads/)

Flask 의 문서에서는 파일 사이즈에 대한 제한과 확장자에 대한 제한 그리고 `secure_filename()` 함수를 통한 [서버내에서의 다른 경로로의 접근을 제한](http://werkzeug.pocoo.org/docs/0.14/utils/#werkzeug.utils.secure_filename)하고 있다. 위의 링크에 있는 소스를 가지고 Whale.exe 파일을 Whale.pdf 로 변경한 후에 파일 업로드를 올리고 아래와 같은 코드로 mimetype 을 찍어봤다. 

```python 
    @app.route('/upload', methods=['POST'])
    def upload():
        upload_file = request.files.get('file', None)
        print(upload_file.mimetype)
        print(upload_file.content_type)
        print(upload_file.headers)
    
    
    >>> application/pdf
    >>> Content-Disposition: form-data; name="file"; filename="WhaleSetup.pdf"
    >>> Content-Type: application/pdf
```

결과를 보면, 확장자를 변경했기 때문에 mimetype 내용이 `application/pdf` 로 나오는 것을 확인 할 수가 있다. **즉 확장자만 바꾸면, 업로드 제한을 회피 할 수 있다는 것이다.** 이런 회피를 감지하기 위해서는 파일 자체를 봐야하는데, 파일 자체를 보기에는 큰 파일의 경우 다 볼수가 없다. 그래서 파일 시그니처(signature) 를 확인해야 한다. 

**파일 시그니처란 무엇일까?** 

- 각각의 파일들은 포맷(format) 이라는것이 있고, 그 포맷들을 파일 시그니처를 가지고 있다.
- 파일의 첫 부분 혹은 끝 부분 몇 바이트를 가지고 시그니처로 사용한다. (헤더 시그니처, 푸터 시그니처)

파일 시그니처를 통해서 전송받은 파일이 어떤 파일인지 분류를 하게 되면 해당 파일을 지우거나 혹은 파일을 전송한 사용자 혹은 ip 등을 로그를 남기고, 차단을 하는 등의 조치를 취할 수가 있다. 

일단 어떤 파일들을 허용할 지를 지정하고, 해당 파일들이 전송되었을때의 mimetype 을 지정했다. 

```python 
    ALLOWED_FILE_TYPE_MAPPING = {
        'pdf': 'application/pdf',
        'png': 'image/png',
        'jpg': 'image/jpeg',
        'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
    
    }
    ALLOWED_EXTENSIONS = set(ALLOWED_FILE_TYPE_MAPPING.keys())
    ALLOWED_MIME_TYPES = set(ALLOWED_FILE_TYPE_MAPPING.values())
```

허용하는 파일은 이미지파일(png, jpg), 문서파일(pdf, docx, xlsx, pptx) 로 한정했다. 사이트에 따라, 용도에 따라 몇가지 더 추가 할 수 있을것 같다. 그에 따른 mimetype 도 같이 추가해주면 된다. 

**fleep 라이브러리** 

저장한 파일에서 파일 시그니처를 가져와서 분석하고, mimetype 을 반환해주는 라이브러리는 fleep 을 사용하면 된다. 파이썬에서 제공하는 imghdr 이나 기타 라이브러리들이 있지만, 찾은것 중에 가장 최근까지 관리가 되고, 많은 파일에 대한 분석을 제공하는 것은 fleep 이었다. 

fleep 은 사용법이 간단한데 아래와 같이 사용하면 된다. 내부적으로 data.json 이라는 파일에서 파일시그니처와 type, extension, mime, offset 등의 정보들을 가지고 있어서 바이너리모드로 읽은 파일에 대한 시그니처를 가지고 맵핑된 결과를 반환하는 식으로 구성되어 있다. 

```python 
    import fleep
    
    with open("png_image", "rb") as file:
        info = fleep.get(file.read(128))
    
    print(info.type)  # prints ['raster-image']
    print(info.extension)  # prints ['png']
    print(info.mime)  # prints ['image/png']
    
    print(info.type_matches("raster-image"))  # prints True
    print(info.extension_matches("gif"))  # prints False
    print(info.mime_matches("image/png"))  # prints True
```

fleep 라이브러리는 아쉽게도 python 버전 3.1 이상을 요구한다. python2.x 에서 사용하고 싶으면 아래와 같이 fleep 라이브러리의 `get()` 함수에서 `ord()` 를 추가하면 된다. 

```python
    stream = " ".join(['{:02X}'.format(ord(byte)) for byte in obj])
```
---

다시 돌아와서 upload 하는 부분의 코드에서 기존의 확장자 체크와 더불어서 fleep 을 이용해서 mimetype 을 체크하는 부분을 넣어보았다. fleep 은 일단 파일이 서버에 저장된 이후에 검사할 수 있기 때문에 저장하고 검사하고, 정한 mimetype 이 아닌 경우에는 로컬에 저장한 파일을 삭제 하는 식으로 진행했다. 

```python 
    @app.route('/upload', methods=['POST'])
    def upload():
        upload_file = request.files.get('file', None) 
        if not upload_file or not upload_file.filename:
            return "NOT EXIST FILE"
    
        if upload_file and allowed_file(upload_file.filename):
            filename = secure_filename(upload_file.filename)
            save_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            print('SAVE_FILE_PATH : {}'.format(save_file_path))
            upload_file.save(save_file_path)
    
            with open(save_file_path, "rb") as file:
                info = fleep.get(file.read(128))
                mime_type = info.mime
    
            if mime_type and allowed_mime(mime_type):
                return "SAVED : {}".format(save_file_path)
            else:
                os.remove(save_file_path)
                return 'INVALID MIMETYPE : {}'.format(mime_type)
        else:
            return 'INVALID FILE'
```

파일이 없는 경우나 확장자가 유효하지 않은 경우, mimetype 이 유효하지 않은 경우에 response 메시지만 내보내고 있지만, 실제 프로젝트에서는 json 형식의 status code 400, 403 등을 정의해서 내보내면 될 것이다. 

[https://github.com/AhnSeongHyun/flask-upload-limit](https://github.com/AhnSeongHyun/flask-upload-limit) 

**Reference:**

[https://github.com/floyernick/fleep-py](https://github.com/floyernick/fleep-py)

[http://forensic-proof.com/archives/300](http://forensic-proof.com/archives/300)

[https://hackernoon.com/determining-file-format-using-python-c4e7b18d4fc4](https://hackernoon.com/determining-file-format-using-python-c4e7b18d4fc4)
