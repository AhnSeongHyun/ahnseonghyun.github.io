---
title: 'SQLAlchemy Join #3 One to One'
author: 'ash84'
pub_date: '2018-09-04'
description: '**[One To One](http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#one-to-one)**

일대일 관계에서는 양쪽 매퍼에서 스칼라 속성을 통한 양방향 관계가 필수적이다. 이것을 위해서 `uselist` flag 가 있는데 이것은  많은쪽("many” side of the relationship.)의 컬랙션 대신에 스칼라 속성의 위치를 가리킨다. 

일대다 를 일대일로 바꾸면,

```python
    class Parent(Base):'
featured_image: ''
tags: ['dev', 'Python', 'sqlalchemy', 'join']
---

**[One To One](http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#one-to-one)**

일대일 관계에서는 양쪽 매퍼에서 스칼라 속성을 통한 양방향 관계가 필수적이다. 이것을 위해서 `uselist` flag 가 있는데 이것은  많은쪽("many” side of the relationship.)의 컬랙션 대신에 스칼라 속성의 위치를 가리킨다. 

일대다 를 일대일로 바꾸면,

```python
    class Parent(Base):
        __tablename__ = 'parent'
        id = Column(Integer, primary_key=True)
        child = relationship("Child", uselist=False, back_populates="parent")
    
    class Child(Base):
        __tablename__ = 'child'
        id = Column(Integer, primary_key=True)
        parent_id = Column(Integer, ForeignKey('parent.id'))
        parent = relationship("Parent", back_populates="child")
```

다대일의 경우, 

```python
    class Parent(Base):
        __tablename__ = 'parent'
        id = Column(Integer, primary_key=True)
        child_id = Column(Integer, ForeignKey('child.id'))
        child = relationship("Child", back_populates="parent")
    
    class Child(Base):
        __tablename__ = 'child'
        id = Column(Integer, primary_key=True)
        parent = relationship("Parent", back_populates="child", uselist=False)
```

---

**필자테스트** 

`uselist` 를 사용하지 않은 상태에서 아래의 코드를 통해서 .child 에 접근하면 [parent.id](http://parent.id) ==1  에 대한 리스트가 출력 된다. 일반적인 일대다 관계에서의 사용법이라고 볼 수 있다. 두번째 결과는 같은 코드를 uselist=False 로 지정하고나서 호출한 코드이다. list 형식이 아닌 Child 객체가 보여지고 있고, 원래 리스트에서 첫번째 값이 보여진다. 이 경우 `Multiple rows returned with uselist=False` 경고가 출력된다. 

```python
    p = session.query(Parent).filter(Parent.id == 1).scalar()
    print(p.id)
    print(p.child)
    
    >>> [{'parent_id': 1, '_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x00000000046C60F0>, 'id': 11}, {'parent_id': 1, '_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x00000000046C6198>, 'id': 12}, {'parent_id': 1, '_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x00000000046C6048>, 'id': 13}]
    
    >>> {'parent_id': 1, '_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x0000000003C554E0>, 'id': 11}
```

---
