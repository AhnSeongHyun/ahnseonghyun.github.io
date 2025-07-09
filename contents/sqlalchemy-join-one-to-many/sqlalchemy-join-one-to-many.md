---
title: 'SQLAlchemy Join #1 One To Many'
author: 'ash84'
pub_date: '2018-08-18'
description: 'SQLAlchemy Join 에 대해서 막연하게 쓰다보니 여러가지 관계 테이블상황에서 제대로 사용하지 못하고 수박겉핣기식으로 쓰는 경우가 많았다. 그래서 공식 문서상의 Join 관련 부분(아래의 URL)을 따라하면서 막히는 부분을 풀어보고자 한다. 

[http://docs.sqlalchemy.org/en/latest/orm/relationships.html](http://docs.sqlalchemy.org/en/latest/orm/relationships.html)

## Basic Relationship Patterns

###'
featured_image: ''
tags: ['dev', 'Python', 'sqlalchemy', 'join']
---

SQLAlchemy Join 에 대해서 막연하게 쓰다보니 여러가지 관계 테이블상황에서 제대로 사용하지 못하고 수박겉핣기식으로 쓰는 경우가 많았다. 그래서 공식 문서상의 Join 관련 부분(아래의 URL)을 따라하면서 막히는 부분을 풀어보고자 한다. 

[http://docs.sqlalchemy.org/en/latest/orm/relationships.html](http://docs.sqlalchemy.org/en/latest/orm/relationships.html)

## Basic Relationship Patterns

### One To Many(일대다)

일대다 관계는 parent 를 참조하는 외래키를 child 테이블에 준다. child 의 컬렉션을 가져오기 위해서  `relationship()` 함수는 parent 에 위치시킨다. 

```python
    class Parent(Base):
        __tablename__ = 'parent'
        id = Column(Integer, primary_key=True)
        children = relationship("Child")
    
    class Child(Base):
        __tablename__ = 'child'
        id = Column(Integer, primary_key=True)
        parent_id = Column(Integer, ForeignKey('parent.id'))
        
        def __repr__(self):
            return str({
                'id': self.id,
                'parent_id': self.parent_id
            })
 ```

```python   
    parent  = session.query(Parent).filter(Parent.id == 1).scalar()
    print(parent.children) 
    > [{'parent_id': 1, 'id': 11}, {'parent_id': 1, 'id': 12}, {'parent_id': 1, 'id': 13}]
```

 일대다 관계하에서 양방향(bidirectional relationship)을 만들기 위해서는 반대편쪽에`relationship()` 을 추가하고 `relationship.back_populates` 항목으로 연결해 주면 된다. 

```python
    class Parent(Base):
        __tablename__ = 'parent'
        id = Column(Integer, primary_key=True)
        children = relationship("Child", back_populates="parent")
    
    class Child(Base):
        __tablename__ = 'child'
        id = Column(Integer, primary_key=True)
        parent_id = Column(Integer, ForeignKey('parent.id'))
        parent = relationship("Parent", back_populates="children")
```

이렇게 되면 `Child` 는 `parent` 속성을 통해서 연결된 parent 객체에 접근 할 수 있다.  또는 `back_populates` 대신에 `backref` 을 사용하면 단일 `relationship()`  상에서 사용 할 수 있다. 

```python
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship("Child", backref="parent")
```

* * *

**필자 테스트** 

예제에서는 단일 파일의 형태로 되어 있지만, 사실 실 업무에서는 model, db 등의 패키지명으로 빼서 mapper class 만 별도로 관리하기 마련이다.  단순히 파일만 분리하고 돌려보면 아래와 같은 에러가 발생한다.

```python
from sqlalchemy.ext.declarative import declarative_base
    Base = declarative_base()
    
    class Parent(Base):
        __tablename__ = 'parent'
        id = Column(Integer, primary_key=True)
        children = relationship("Child")
```
```python
sqlalchemy.exc.InvalidRequestError: When initializing mapper Mapper|Parent|parent, expression 'Child' failed to locate a name ("name 'Child' is not defined"). If this is a class name, consider adding this relationship() to the <class 'model_old.parent.Parent'> class after both dependent classes have been defined.
```

단순히 파일을 분리하면 parent.py, [child.py](http://child.py) 각각에 아래의 Base 를 통해서 mapper 클래스를 만들게 된다. 각각의 파일에서 `Base` 에 대한 로그를 남겨보면 아래와 같다. 

```
    child id:67534648 Base.metadata.tables:immutabledict({})
    parent id:67543144 Base.metadata.tables:immutabledict({})
```

id 값이 다르고 `Base.metadata.tables` 에서 아무것도 없다. 서로 다른 Base 객체를 바라보고 있다고 보면 될것 같다. 그래서 query 를 하는 시점에 Parent 에서 `relationship()` 으로 지정된 Child 항목을 찾지 못하고 에러를 발생 시킨다.

같은 `Base` 객체를 바라보게 하면 이 문제는 해결된다. 

```python

    # model/__init__.py 
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    
    connection_string = "10.10.1.10:3306"
    id = "xxx"
    pw = "xxx"
    Base = declarative_base()
    engine = create_engine('mysql+pymysql://{}:{}@{}/test'.format(id, pw, connection_string))
    Session = sessionmaker(bind=engine, autocommit=False)
    session = Session()
    
    from .parent import Parent
    from .child import Child
    
    
    # model/parent.py  
    from model import Base
    class Parent(Base):
        __tablename__ = 'parent'
        id = Column(Integer, primary_key=True)
        children = relationship("Child")
    
    # model/child.py
    from model import Base
    class Child(Base):
        __tablename__ = 'child'
        id = Column(Integer, primary_key=True)
        parent_id = Column(Integer, ForeignKey('parent.id'))
    
        def __repr__(self):
            return str({
                'id': self.id,
                'parent_id': self.parent_id
            })
    
    # model/main.py
    from model import session
    from model import Child
    from model import Parent
    
    p = session.query(Parent).filter(Parent.id == 1).scalar()
    print(p.id)
    print(p.children)
    c = session.query(Child).filter(Child.id == 11).scalar()
    print(c.id)
    print(c.parent)
    session.close()
```
---

같은 로그를 위의 코드상에서 나오게 해본 결과는 아래와 같다. `Base` 객체의 같은 id 값이 나왔다는 것과 함께 child 쪽 `Base.metadata.tables` 에 parent 항목이 들어가 있는 것을 확인 할 수 있다. 그래서 query 를 실행하는 시점에 `relationship("Child")` 부분이 에러가 발생하지 않는다. 

```python
    from .parent import Parent
    from .child import Child
    print(Base.metadata.tables)
    
    > parent id:62959640 Base.metadata.tables:immutabledict({})
    > child id:62959640 Base.metadata.tables:immutabledict(
    {'parent': Table('parent', MetaData(bind=None), Column('id', Integer(), table=<parent>, primary_key=True, nullable=False), schema=None)
    })
    > immutabledict({'parent': Table('parent', MetaData(bind=None), Column('id', Integer(), table=<parent>, primary_key=True, nullable=False), schema=None), 'child': Table('child', MetaData(bind=None), Column('id', Integer(), table=<child>, primary_key=True, nullable=False), Column('parent_id', Integer(), ForeignKey('parent.id'), table=<child>), schema=None)})
```
