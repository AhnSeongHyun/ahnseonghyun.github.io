---
title: 'flask-sqlalchemy multiple databases'
author: 'ash84'
pub_date: '2017-09-06'
description: '### **사용하기**

flask-sqlalchemy 에서 기본적으로 `SQLALCHEMY_DATABASE_URI` 설정을 통해서 mapping class 에 정의된 테이블들이 DB와 연결되게 된다. 그런데 1개 이상의 DB와 연결해야하는 경우가 생긴다. 기존의 회원정보를 같이 쓰는 다른 서비스의 경우가 대표적인 케이스이다. 이럴경우, flask-sqlalchemy 에서는 `SQLALCHEMY_BINDS` 를 통해서 여러 데이터베이스 URI를 지정할 수 있게 해주고 있다. 

```python 
app.config['SQLALCH'
featured_image: ''
tags: ['dev', 'FLASK', 'Python', 'sqlalchemy', 'multidb', 'multiple database']
---

### **사용하기**

flask-sqlalchemy 에서 기본적으로 `SQLALCHEMY_DATABASE_URI` 설정을 통해서 mapping class 에 정의된 테이블들이 DB와 연결되게 된다. 그런데 1개 이상의 DB와 연결해야하는 경우가 생긴다. 기존의 회원정보를 같이 쓰는 다른 서비스의 경우가 대표적인 케이스이다. 이럴경우, flask-sqlalchemy 에서는 `SQLALCHEMY_BINDS` 를 통해서 여러 데이터베이스 URI를 지정할 수 있게 해주고 있다. 

```python 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/test1'
app.config['SQLALCHEMY_BINDS'] = {
    'test2': 'mysql+pymysql://root:root@localhost:3306/test2',
    'test1': 'mysql+pymysql://root:root@localhost:3306/test1'
}
```

위의 설정을 보면, `SQLALCHEMY_DATABASE_URI` 를 지정하면서 `SQLALCHEMY_BINDS` 를 지정하고 있다. `SQLALCHEMY_BINDS` 는 키-값 형태로 지정하면 되는데, test1, test2 와 같이 지정을 해두었다. `SQLALCHEMY_DATABASE_URI` 에 지정한 값은 디폴트 값으로 지정되게 된다. 

```python
class User(db.Model):
    __tablename__ = "tb_user"
    __bind_key__ = 'test2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Store(db.Model):
    __tablename__ = "tb_store"
    __bind_key__ = 'test1'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, primary_key=True)
```

mapping class 에는 위와 같이 `__bind_key__` 항목에 `SQLALCHEMY_BINDS` 에 지정한 키(key)를 넣어주면 된다. 예를들면 위의 코드에서는 User(`tb_user` 테이블)은 test2 의 DB와 연결되고 Store(`tb_store` 테이블)는 test1 의 DB 와 연결되는 것이다. `__bind_key__` 항목을 설정하지 않으면 `SQLALCHEMY_DATABASE_URI` 에 설정한 URI 로 연결이 된다. 

테이블을 생성하거나 삭제 할때에도 bind 를 아래와 같이 지정할 수가 있다. 

```python
# Refer http://flask-sqlalchemy.pocoo.org/2.1/binds/
>>> db.create_all()
>>> db.create_all(bind=['test1'])
>>> db.create_all(bind='test2')
>>> db.drop_all(bind=None)
```

### **`__bind_key__` 는 어떻게 저장되는가?**

- `__bind_key__` 는 `__tablename__` 과는 다르게 flask-sqlalchemy 에서만 있는 부분이다. 
- `__bind_key__` 를 지정하게 되면 Table 클래스의 `info` dict 에 `bind_key` 항목으로 들어가게 된다. 
- 아래의 코드를 보면 테이블을 정의하는 클래스를 만들때 `db.Model`을 상속 받게 되는데, db 는 flask-sqlalchemy 의 SQLAlchemy 클래스의 인스턴스이고 Model 은 그 클래스의 변수이다. 


```python 
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

class User(db.Model):
   ...

db.Model =>  SQLAlchemy 의 self.Model = self.make_declarative_base(model_class, metadata)

```

- Model 은 `make_declarative_base()` 함수에 의해서 생성 되는데 내부에서 sqlalchemy 의 `declarative_base()` 함수를 호출하면서 _BoundDeclarativeMeta 클래스를 metaclass 로 지정하고 있다. 

```python 
## flask_sqlalchemy/__init__.py

def make_declarative_base(self, model, metadata=None):
    """Creates the declarative base."""
    base = declarative_base(cls=model, name='Model',
                            metadata=metadata,
                            metaclass=_BoundDeclarativeMeta)

    if not getattr(base, 'query_class', None):
        base.query_class = self.Query

    base.query = _QueryProperty(self)
    return base
```

- _BoundDeclarativeMeta 클래스는 생성자에서 파라미터로 전달된 `d` 에 `__bind_key__` 가 있는지 확인하고 있으면 table.info 의 `bind_key` 항목으로 넣고 있다. `__init__()` 함수로 전달되는 항목들을 찍어보면 아래와 같다. 


```python 
## flask_sqlalchemy/__init__.py

class _BoundDeclarativeMeta(DeclarativeMeta):
    def __new__(cls, name, bases, d):
        # if tablename is set explicitly, move it to the cache attribute so
        # that future subclasses still have auto behavior
        if '__tablename__' in d:
            d['_cached_tablename'] = d.pop('__tablename__')

        return DeclarativeMeta.__new__(cls, name, bases, d)

    def __init__(self, name, bases, d):

        # 디버깅을 위해 추가한 부분. 
        print('name :{}'.format(name))
        print('bases :{}'.format(bases))
        print('d :{}'.format(d))

        bind_key = d.pop('__bind_key__', None) or getattr(self, '__bind_key__', None)
        DeclarativeMeta.__init__(self, name, bases, d)

        if bind_key is not None and hasattr(self, '__table__'):
            self.__table__.info['bind_key'] = bind_key
```


```
name :User
bases :(<class 'flask_sqlalchemy.Model'>,)
d :{'__module__': '__main__', '__qualname__': 'User', '__bind_key__': 'test2', 'id': Column(None, Integer(), table=None, primary_key=True, nullable=False), 'name': Column(None, String(), table=None), '_cached_tablename': 'tb_user'}

name :Store
bases :(<class 'flask_sqlalchemy.Model'>,)
d :{'__module__': '__main__', '__qualname__': 'Store', '__bind_key__': 'test1', 'id': Column(None, Integer(), table=None, primary_key=True, nullable=False), 'name': Column(None, Integer(), table=None, primary_key=True, nullable=False), '_cached_tablename': 'tb_store'}
``` 

**Reference** 

- [Multiple Databases with Binds](http://flask-sqlalchemy.pocoo.org/2.1/binds/)
