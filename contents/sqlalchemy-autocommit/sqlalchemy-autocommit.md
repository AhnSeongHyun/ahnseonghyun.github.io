---
title: 'SQLAlchemy autocommit 에 대해서 '
author: 'ash84'
pub_date: '2018-07-31'
description: 'DB 상에서 autocommit 이란 데이터 변경 작업에 대한 SQL 자체가 바로 반영되는 것을 의미하는데   autocommit 이 아닌 상태에서는 여러줄의 명령을 하나의 트랜잭션으로 묶을수가 있다.(개별 DBMS 엔진이나 DB타입에 따라 다를수는 있다. 여기에서는 MYSQL InnoDB 기반으로 테스트를 진행하였다.)

**mysql autocommit 확인하기** 

```python
SELECT @@AUTOCOMMIT;
```

**mysql autocommit 설정/해제 하기** 

```python
SET AUTOCOMM'
featured_image: ''
tags: ['Python', 'sqlalchemy', 'autocommit']
---

DB 상에서 autocommit 이란 데이터 변경 작업에 대한 SQL 자체가 바로 반영되는 것을 의미하는데   autocommit 이 아닌 상태에서는 여러줄의 명령을 하나의 트랜잭션으로 묶을수가 있다.(개별 DBMS 엔진이나 DB타입에 따라 다를수는 있다. 여기에서는 MYSQL InnoDB 기반으로 테스트를 진행하였다.)

**mysql autocommit 확인하기** 

```python
SELECT @@AUTOCOMMIT;
```

**mysql autocommit 설정/해제 하기** 

```python
SET AUTOCOMMIT = TRUE;   // AUTOCOMMIT 설정
SET AUTOCOMMIT = FALSE;  // AUTOCOMMIT 해제
    
COMMIT; // 커밋
ROLLBACK; // 롤백
```

**테스트**

```python
SET AUTOCOMMIT = FALSE;  
insert into test.tb_category values(9, null, null, '테스트', 0); 
commit;
# commit 을 해야 반영된 것이 보인다. 
```


## SQLAlchemy 의 autocommit 설정

아래는 기본적인 SQLAlchemy 에 나오는 트랜잭션 관련 설명을 (발)번역한 내용이다. 

- [Using Transactions](http://docs.sqlalchemy.org/en/latest/core/connections.html#understanding-autocommit)

`Connection` 객체는 `begin()` 메소드를 제공하는데 이 함수는 `Transaction` 객체를 반환한다. 이 객체는 try/catch 문 안에서 사용되고 (트랜잭션을) 보장하기 위해서 `Transaction.rollback()`, `Transaction.commit()` 을 사용한다. 

```python
connection = engine.connect()
trans = connection.begin()
try:
    r1 = connection.execute(table1.select())
    connection.execute(table1.insert(), col1=7, col2='this is some data')
    trans.commit()
except:
    trans.rollback()
    raise
```

위의 코드는 context manager 를 이용해서 좀 더 간결하게 만들수 있다. 

```python
# runs a transaction
with engine.begin() as connection:
    r1 = connection.execute(table1.select())
    connection.execute(table1.insert(), col1=7, col2='this is some data')

# or 
with connection.begin() as trans:
    r1 = connection.execute(table1.select())
    connection.execute(table1.insert(), col1=7, col2='this is some data')
```

- [Nesting of Transaction Blocks](http://docs.sqlalchemy.org/en/latest/core/connections.html#nesting-of-transaction-blocks)

`Transaction` 객체는 가장 바깥쪽 begin/commit 의 쌍을 추적해서 중첩(nested)된 동작을 처리한다. 아래의 코드에서 보면 가장 바같쪽의 method_a() 에 대한 커밋만 수행된다.  

```python
# method_a starts a transaction and calls method_b
def method_a(connection):
    trans = connection.begin()  # open a transaction
    try:
        method_b(connection)
        trans.commit()  # transaction is committed here
    except:
        trans.rollback()  # this rolls back the transaction unconditionally
        raise


# method_b also starts a transaction
def method_b(connection):
    trans = connection.begin()  # open a transaction - this runs in the context of method_a's transaction
    try:
        connection.execute("insert into mytable values ('bat', 'lala')")
        connection.execute(mytable.insert(), col1='bat', col2='lala')
        trans.commit()  # transaction is not committed yet
    except:
        trans.rollback()  # this rolls back the transaction unconditionally
        raise


# open a Connection and call method_a
conn = engine.connect()
method_a(conn)
conn.close()
```

위의 코드에서 처음 호출된 method_a 가 `connection.begin()` 을 호출한다. 그리고나서 method_b 를 호출한다. method_b 가 `connection.begin()` 을 호출할 때, 카운더를 증가 시키고 `commit()` 을 호출할 때 카운터를 감소시킨다. 만약 method_a, method_b 가 `rollback()` 을 호출하면 전체 트랜잭션이 롤백된다. 이 트랜잭션은 method_a 의 `commit()` 함수가 호출되기 전까지 커밋되지 않는다. This “nesting” behavior allows the creation of functions which “guarantee” that a transaction will be used if one was not already available, but will automatically participate in an enclosing transaction if one exists.

- [Understanding Autocommit](http://docs.sqlalchemy.org/en/latest/core/connections.html#understanding-autocommit)

INSERT, UPDATE, DELETE 를 실행 시 Transaction 을 사용하지 않으면 어떤 일이 일어날까? 어떤 DBAPI 구현들은 특별한 "non-transactional" 모드들을 제공하지만, PEP-0249 의 DBAPI 의 핵심동작은 트랜잭션은 항상 진행중이며, `rollback()`, `commit()` 함수를 제공하지만, `begin()` 은 제공하지 않는다. SQLAlchemy 는 이것이 주어진 DBAPI의 경우라고 가정한다. 주어진 요구사항에서, SQLAlchemy 는 모든 백엔드에서 일관되게 동작하는 자체 "autocommit" 기능을 구현했다. 이 기능은 데이터 변경 작업 명령 대한 감지를 목표로 한다. 예를 들면, INSERT, UPDATE, DELETE  뿐만 아니라, DDL(CREATE TABLE, ALETER TABLE). 그리고 트랜잭션이 진행중이지 않으면 자동으로 COMMIT 된다. 이러한 명령의 감지는 `autocommit=True` 실행옵션이 있는지에 기초한다. 만약 명령문에 플래그가 설정되어 있지 않다면, 정규표현식이 INSERT, UPDATE, DELETE 뿐만 아니라 특정한 백엔드의 다양한 명령을 감지하는데 사용된다. 

```python
conn = engine.connect()
conn.execute("INSERT INTO users VALUES (1, 'john')")  # autocommits
```

autocomit 기능은 `Transaction` 이 선언되지 않았을때만 영향을 미친다. 기본적으로 `Session` 객체는 항상 진행중인 트랜잭션을 유지관리하기때문에 이 기능은 일반적으로 ORM 과 함께 사용되지 않는다. 

autocommit 동작의 전체 제어는 `Connection`, `Engine`, Executable 이 제공하는`Connection.execution_options()` 함수에 autocommit 플래그를 사용하면 선택된 범위내에 대해서 끄고 켜는것이 가능하다. 

```python 
engine.execute(text("SELECT my_mutating_procedure()").execution_options(autocommit=True))
```

* * *

위의 SQLAlchemy 에서 제공하는 문서들의 일부분을 읽어보면 SQLAlchemy 의 autommit 옵션은 모든 백엔드에 일관되게 동작시키기 위해서 만들어 졌다고 한다. 그래서 아래와 같이 autocommit 옵션설정 여부와 begin(), commit() 호출여부를 가지고 데이터 insert 를 테스트 해보았다. 

**sqlalchemy autocommit on + 명시적 commit() 호출 = 데이터 insert**

```python
Session = sessionmaker(bind=engine, autocommit=True)
session = Session()
   
session.begin()
test = Test(text="text_{}".format(datetime.now()))
session.add(test)
session.commit() 
session.close()
```

**sqlalchemy autocommit on + 명시적 commit() 호출안함 = 데이터 NOT insert** 

```python
Session = sessionmaker(bind=engine, autocommit=True)
session = Session() 
test = Test(text="text_{}".format(datetime.now()))
session.add(test) 
session.close()
```

이상하다. 자동커밋은 말 그대로 `session.commit()` 을 하지 않아도 insert 문에 대해서 DB반영이 되어야 하는게 아닌가?

좀 더 테스트를 해보자. 

 **sqlalchemy autocommit off + 명시적 begin(), commit() 호출 = 에러발생**

```python
Session = sessionmaker(bind=engine, autocommit=False)
session = Session() 
test = Test(text="text_{}".format(datetime.now()))
session.begin()
session.add(test) 
session.commit()
session.close()
```

```
InvalidRequestError: A transaction is already begun. Use subtransactions=True to allow subtransactions.
```

도데체 이 에러는 몰까? 자동커밋 모드를 껏으면, 자동으로 커밋이 안되고 명시적 `begin()`, `commit()` 을 호출했으니 되어야 하는게 아닌가? 왜 에러가 날까? 

**sqlalchemy autocommit off + 명시적 commit() 호출안함 = 데이터 NOT insert** 

```python
Session = sessionmaker(bind=engine, autocommit=False)
session = Session() 
test = Test(text="text_{}".format(datetime.now()))
session.add(test) 
session.close()
```

뭔가 이상하다. 내가 알고있는. 말 그대로 자동커밋이 아니던가? 좀 더 autocommit 관련 문서를 읽어보자. 

* * *

- [Transactions and Connection Management](http://docs.sqlalchemy.org/en/latest/orm/session_transaction.html#transactions-and-connection-management)
  - [Managing Transactions](http://docs.sqlalchemy.org/en/latest/orm/session_transaction.html#managing-transactions)

**새롭게 생성된 `Session` 은 "begin" 상태를 가진다.** 이 상태에서 `Sesssion` 은  `Engine` 과어떤 연결이나 트랜잭션을 맺지 않는다. `Session` 그리고나서 데이터베이스 연결시 동작할 요청을 받는다. 일반적으로  `Session.query()`, `Session.execute()` 또는 보류중인 데이터의 flush 동작을 통해서 SQL문이 실행되고 Session.commit(), Session.flush() 가 호출된다. 

이러한 요청이 왔을 때, 각각의 새로운 `Engine` 은 `Sesssion` 에 의해 진행중인 트랜잭션 상태와 연관이 있다. 첫번째 `Engine` 이 수행될때, `Session` "begin" 상태에서 "transactional" 상태로 진입하게 된다. 각각의 `Engine` 이 `Connection` 과 연결되어 있으며 `Engine.contextual_connect()` 를 통해서 가져올 수 있다. 만약 `Connection` 이 직접적으로 `Session` 과 연결되어 있다면 (Session이)직접적으로 트랜잭션 상태를 추가하게 된다(?) 

각각의 `Connection` 에 대해서 `Session` 은 또한 `Transaction` 객체를 유지하는데 이 객체는 `Connection` 상에서 `Connection.begin()` 을 호출함으로써 가져올수 있거나 혹은 `Session` 객체(`twophase=True` flag 를 사용해서 연결된) 를 통해서 얻을수 있다. `TwoPhaseTransaction` 객체는 `Connection.begin_twophase()` 을 통해서 가져올 수 있다. 이러한 트랜잭션들은 `Session.commit()` 과 `Session.rollback()` 의 호출에 의해서 커밋되거나 롤백된다. 적용가능한 경우 커밋 동작은 또한 `TwoPhaseTransaction.prepare()` 를 호출한다. 

트랜잭션 상태가 롤백이나 커밋이후에 `Session` 은 모든 `Transaction` 과 `Connection` 리소스를 해제 하고 SQL 문을 내보내는 새로운 요청 들어오면 새로운 `Connection` 과 `Transaction` 객체를 호출하는 "begin" 상태로 돌아간다. 

```python
engine = create_engine("...")
Session = sessionmaker(bind=engine)

# new session.   no connections are in use.
session = Session()
try:
    # first query.  a Connection is acquired
    # from the Engine, and a Transaction
    # started.
    item1 = session.query(Item).get(1)

    # second query.  the same Connection/Transaction
    # are used.
    item2 = session.query(Item).get(2)

    # pending changes are created.
    item1.foo = 'bar'
    item2.bar = 'foo'

    # commit.  The pending changes above
    # are flushed via flush(), the Transaction
    # is committed, the Connection object closed
    # and discarded, the underlying DBAPI connection
    # returned to the connection pool.
    session.commit()
except:
    # on rollback, the same closure of state
    # as that of commit proceeds.
    session.rollback()
    raise
finally:
    # close the Session.  This will expunge any remaining
    # objects as well as reset any existing SessionTransaction
    # state.  Neither of these steps are usually essential.
    # However, if the commit() or rollback() itself experienced
    # an unanticipated internal failure (such as due to a mis-behaved
    # user-defined event handler), .close() will ensure that
    # invalid state is removed.
    session.close()
```

  - [Using SAVEPOINT](http://docs.sqlalchemy.org/en/latest/orm/session_transaction.html#using-savepoint)

 SAVEPOINT 트랜잭션은 기반 엔진에서 지원하는 경우, `begin_nested()` 를 이용해서 범위를 지정할 수 있다:

```python
Session = sessionmaker()
session = Session()
session.add(u1)
session.add(u2)

session.begin_nested()  # establish a savepoint
session.add(u3)
session.rollback()  # rolls back u3, keeps u1 and u2

session.commit()  # commits u1 and u2
```

`begin_nested()` 는 여러번 호출되는데 호출될때마다 unique identifier 와 함께 새로운 SAVEPOINT 가 발행된다. 각각의 `begin_nested()` 의 호출에 상응하는 `rollback()`, `commit()` 이 실행되어어야 한다. (그런데 주의할게, 만약 context manager(with 문 같은) 안에 return value 가 사용된다면, 롤백/커밋이 context amanger 에 의해서 context 를 벗어날때 실행되고 return value 를 명시적으로 추가해서는 안된다.)

`begin_nested()`  가 호출될때, `flush()` 는  `autoflush` 설정과 상관없이 무조건 실행된다. `rollback()` 이 발생하면, `Session` 의 전체 상태가 만료되어 모든 연속된 속성/ 객체에 대한 접근이 `begin_nested()` 호출 이전의 세션의 전체 상태를 참조하게 된다. 

`begin_nested()` 는 적게 사용되는 `begin()` 메소드와 같은 방식으로 `SesssionTransaction` 객체를 반환한다. 이 객체는 context manager 로 동작한다.  이것은 개별 레코드 삽입에서 unique constraint exception 같은 것을 잡을때 간결하게 사용할 수 있다. 

```python
for record in records:
    try:
        with session.begin_nested():
            session.merge(record)
    except:
        print("Skipped record %s" % record)
session.commit()
```

  - [Autocommit Mode](http://docs.sqlalchemy.org/en/latest/orm/session_transaction.html#autocommit-mode)

  `Session` 은 기본적으로 `autocommit=False` 로 동작한다. 이 모드에서 `Session` 은 데이터베이스에 연결이 되자마자 **자동적으로 트랜잭션을 시작한다.** 그리고나서 트랜잭션은 `Session.commit()` , `Sesseion.rollback()` 가 호출될때까지 대기한다. 

  `Sesssion` 에는 또한 **autocommit mode** 라는 구형 레거시모드가 있는데 이 모드는 `**Session.begin()` 을 호출하지 않으면 암묵적으로 트랜잭션을 시작하지 않는다.** `Session` 은 수행할것이다. 각각의 데이터베이스 동작은 connection pool 에서 체크아웃된 새로운 연결상에서 수행되고, 동작이 완료되는 즉시 connection pool 로 반환된다.  이것은 `Session.query ()` 에서 반환 된 쿼리를 실행할 때뿐만 아니라 `Session.execute()`와 같은 메서드에도 해당한다. flush 동작에 대해서 `Session` 은 flush 지속기간 동안 트랜잭션을 시작하고 완료가 되었을때 커밋을 한다. 

    - WARNING

 "autocommit" 모드는 레거시 모드를 사용하는것으로 새로운 프로젝트에서는 고려해서는 안된다. 만약 autocommit 모드를 사용하면 적어도  순수  autocommit mode 에서는 session을 사용하는것 보다 `Sesssion.begin()` 메소드를 통해서 트랜잭션 범위를 보장하는 것을 강력히 추천한다. 

만약 `Session.begin()` 메소드를 사용하지 않으면 동작은 즉시자동커밋과 함께 ad-hoc 연결을 이용해서 진행할수 있다. 그리고나서 어플리케이션은 아마 `autoflush=False, expire_on_commit=False` 을 설정해야한다. 왜냐하면 이 기능들은 데이터베이스 트랜잭션의 컨텍스트 내에서만 오지 사용되도록 만들어졌기 때문이다. 현대의 "autocommit mode" 의 사용은 프레임워크와 결합하려는 경향이 있는데 이 프레임워크는 "begin" 상태가 발생할때 제어하기를 원한다. `autocommit=True` 로 설정된 session 은 `Session.begin()` 메소드를 사용해서 "begin" 상태에 들어갈 수 있다. 트랜잭션의 싸이클이 `Session.commit()`, `Session.rollback()` 을 하자마자 완성된 이후에, connection 과 transaction 리소스는 해제되고 `Session` 은 `Session.begin()` 이 다시 호출될 때까지  "autocommit" 모드로 돌아간다. 

```python
Session = sessionmaker(bind=engine, autocommit=True)
session = Session()
session.begin()
try:
    item1 = session.query(Item).get(1)
    item2 = session.query(Item).get(2)
    item1.foo = 'bar'
    item2.bar = 'foo'
    session.commit()
except:
    session.rollback()
    raise
```

`Session.begin()` 메소드는 트랜잭션 토큰을 반환하는데, 이것은 `with` 문과 호환이 된다. 

```python
Session = sessionmaker(bind=engine, autocommit=True)
session = Session()
with session.begin():
    item1 = session.query(Item).get(1)
    item2 = session.query(Item).get(2)
    item1.foo = 'bar'
    item2.bar = 'foo'
```

    - [Using Sustransaqctions with Autocommit](http://docs.sqlalchemy.org/en/latest/orm/session_transaction.html#using-subtransactions-with-autocommit)

 서브트랜잭션은 `Session.begin()` 메소드의 `subtransactions=True` 플래그 사용과 연관이 있다. 이것은  `begin ()` 및 `commit ()` 호출의 중첩을 허용하는 비트랜잭션(non-transactional), 구분 구조를 생성한다. 서브트랜잭션의 목적은 트랜잭션을 시작한 외부 코드와 트랜잭션을 이미 구분 한 블록 내에서 독립적으로 트랜잭션 내에서 작동 할 수있는 코드를 구성 할 수있게하는 것이다.(?)

`substrancactions=True` 는 일반적으로 오직 autocommit 과 연관이 있는 경우에 유용한데 이것은 중첩트랜잭션블록(Nesting of Transaction Blocks) 패턴과 동일하다. 

```python

# method_a starts a transaction and calls method_b
def method_a(session):
    session.begin(subtransactions=True)
    try:
        method_b(session)
        session.commit()  # transaction is committed here
    except:
        session.rollback()  # rolls back the transaction
        raise


# method_b also starts a transaction, but when
# called from method_a participates in the ongoing
# transaction.
def method_b(session):
    session.begin(subtransactions=True)
    try:
        session.add(SomeObject('bat', 'lala'))
        session.commit()  # transaction is not committed yet
    except:
        session.rollback()  # rolls back the transaction, in this case
        # the one that was initiated in method_a().
        raise


# create a Session and call method_a
session = Session(autocommit=True)
method_a(session)
session.close()
```

`Session.flush()` 에 의해서 사용되는 서브트랜잭션들은 autocommit 에 관계없이 트랜잭션내에서 발생하는 flush 동작을 보장하기 위해서 처리한다. autocommit 을 사용하지 않는 경우, 최종 사용자가 여전히 트랜잭션의 "scope"를 유지하는 중간 작업에서 실패한 flush 를 다시 시작할 수 없으므로 `Session`을 "pending rollback"상태로 만든다. 

* * *

다시 현재 겪고있는 의문들을 정리해보면 이렇다. 


- **autocommit = True || False 인 상태에서, commit() 을 하지 않으면 데이터가 왜 안들어갈까?**

⇒ 결국 `commit()` 함수와 autocommit 설정 사이에 연관이 있느냐가 핵심인데 autocommit 이라는 이름이 가지는 의미와 다르게 `commit()` 함수의 자동호출 유무와는 관계가 없다. autocommit 은 위에 자료에서도 나와있는것 처럼  `autocommit=False` 로 설정하면 `Session` 은 자동적으로 트랜잭션을 시작한다. `autocommit=True` 모드에서는 `session.begin()` 을 명시적으로 사용해야 트랜잭션이 시작된다. autocommit 의 사용여부와 상관없이 데이터 변경작업의 반영을 위해서는 `commit()` 함수를 사용해야한다. 


- **autocommit = False 인 상태에서, begin() 을 하면 에러 발생?**


⇒ 에러메시지가 A transaction is already begun. 라고 나온다.  앞에서도 말했듯이 **autocommit 설정은 트랜잭션의 자동시작여부와 관계가 있다.**  `autocommit=False` 이면 자동으로 시작한다. 때문에 `begin()` 을 쓰게 되면 중복으로 트랜잭션을 시작하게 되는 셈이라서 위와같은 에러메시지를 뱉는다.

 실제로 SQLAlchemy 의 [Session Class](https://github.com/zzzeek/sqlalchemy/blob/master/lib/sqlalchemy/orm/session.py#L776) 에 `__init__()` 부분에 아래와 같이 autocommit 이 False 인 경우, `begin()` 함수를 자동적으로 호출하고 있다. 

```python 
  if not self.autocommit:
      self.begin()
```

꽤 오랫동안 가지고 있었던 의문이 풀렸다. 나의 이런 의문은 autocommit 이라는 설정 이름이 가지는 의미 때문에 혼돈을 가진게 아닌가 싶다. 커밋을 자동으로 해주느냐가 아니라, 자동으로 트랜잭션을 시작하느냐가 핵심인것 같다. 좀 더 나은 네이밍이었으면 좋았을 것 같다는 생각이 든다. (auto_begin_transaction 같은..) 

**Reference** 

- [https://zetawiki.com/wiki/MySQL_AUTOCOMMIT_설정](https://zetawiki.com/wiki/MySQL_AUTOCOMMIT_%EC%84%A4%EC%A0%95)
- http://bryan7.tistory.com/78
