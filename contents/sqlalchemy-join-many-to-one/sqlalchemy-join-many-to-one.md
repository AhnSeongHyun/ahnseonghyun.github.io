---
title: 'SQLAlchemy Join #2 Many To One'
author: 'ash84'
pub_date: '2018-08-31'
description: '**Many To One** 

다대일 관계에서 child 를 참조하는 외래키는 parent 클래스에 위치해있다. `relationship()`  함수
는 parent 클래스에 위치해있으며, scalar-holding  속성이 생성될것이다.

```python
    class Parent(Base):
        __tablename__ = 'parent'
        id = Column(Integer, primary_key=True)
        child_id = Column(Integer, ForeignKey('chi'
featured_image: ''
tags: ['sqlalchemy', 'dev', 'join', 'Python']
---

**Many To One** 

다대일 관계에서 child 를 참조하는 외래키는 parent 클래스에 위치해있다. `relationship()`  함수
는 parent 클래스에 위치해있으며, scalar-holding  속성이 생성될것이다.

```python
    class Parent(Base):
        __tablename__ = 'parent'
        id = Column(Integer, primary_key=True)
        child_id = Column(Integer, ForeignKey('child.id'))
        child = relationship("Child")
    
    class Child(Base):
        __tablename__ = 'child'
        id = Column(Integer, primary_key=True)
```

양방향 연결을 두번째 `relationship()` 를 추가하고 양쪽에`relationship.back_populates` 파라미터를 양쪽에 적용하면 된다. 

```python
    class Parent(Base):
        __tablename__ = 'parent'
        id = Column(Integer, primary_key=True)
        child_id = Column(Integer, ForeignKey('child.id'))
        child = relationship("Child", back_populates="parents")
    
    class Child(Base):
        __tablename__ = 'child'
        id = Column(Integer, primary_key=True)
        parents = relationship("Parent", back_populates="child")
```

대안으로는 `backref` 파라미터를 한쪽의 `relationship()` 에 적용하면 된다. 

```python
    class Parent(Base):
        __tablename__ = 'parent'
        id = Column(Integer, primary_key=True)
        child_id = Column(Integer, ForeignKey('child.id'))
        child = relationship("Child", backref="parents")
```

---

**필자 테스트** 

아래와 같이 위의 모델 클래스들을 호출하는 코드를 짜봤다. 잘 호출이 된다. `back_populates` 를 이용해서는 parents 가 Child 클래스에 정의가 되어 있으니 실행되는게 맞는데, `backref` 의 경우 Parent 클래스에 정의가 되어 있는데 c.parents 나 p.child.parents 부분이 왜 에러가 안날까?

```python
    from model import session
    from model import Child
    from model import Parent
    
    p = session.query(Parent).filter(Parent.id == 1).scalar()
    print(p.id)
    print(p.child)
    print(p.child.id)
    print(p.child.parents)
    
    c = session.query(Child).filter(Child.id == 12).scalar()
    print(c)
    print(c.id)
    print(c.parents)
    session.close()
```



**backref 와 back_populates 의 차이는 뭘까?**

**backref**: 관계된 매퍼 클래스의 속성의 문자열 이름을 가리킨다. 이 속성은 매퍼 클래스가 구성될 때 자동적으로 생성된다. 

**back_popuplates**: backref 와 동일한 의미이고, 자동적으로 생성해주지 않는것이 차이. 매퍼 클래스에 명시적으로 구성해줘야 한다. 

Parent 매퍼 클래스에서 `back_populates` 로 지정한 parents 가 만약 Child 매퍼 클래스에서 선언하지 않았다면 아래와 같은 에러가 발생한다. 

```
sqlalchemy.exc.InvalidRequestError: Mapper 'Mapper|Child|child' has no property 'parents'
```

---
