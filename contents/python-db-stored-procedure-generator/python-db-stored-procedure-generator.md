---
title: 'python - db stored procedure 호출에 generator 활용하기'
author: 'ash84'
pub_date: '2017-09-04'
description: '프로시저 호출은 몇 가지 제약을 가진다. 일단 프로시저명을 전달해야 하고 파라미터를 순서대로 전달해야 한다. 그리고 결과를 주는 방식이 하나의 결과를 줄 수도 있고 여러 결과를 줄 수도 있다. 프로시저당 하나의 호출 함수를 만들면 너무 많은 프로시저 호출 함수가 생기는 문제가 있다. 그래서 프로시저 이름을 받는 파라미터와 전달할 프로시저 파라미터, 그리고 insert, update, delete 의 경우 commit 을 해야하기 때문에 commit 여부를 위한 파라미터, 그리고 여러 결과를 반환하는 여부에 대한 파라미터를 추가한 호'
featured_image: ''
tags: ['dev', 'Python', 'generator', '제너레이터', '저장프로시저']
---

프로시저 호출은 몇 가지 제약을 가진다. 일단 프로시저명을 전달해야 하고 파라미터를 순서대로 전달해야 한다. 그리고 결과를 주는 방식이 하나의 결과를 줄 수도 있고 여러 결과를 줄 수도 있다. 프로시저당 하나의 호출 함수를 만들면 너무 많은 프로시저 호출 함수가 생기는 문제가 있다. 그래서 프로시저 이름을 받는 파라미터와 전달할 프로시저 파라미터, 그리고 insert, update, delete 의 경우 commit 을 해야하기 때문에 commit 여부를 위한 파라미터, 그리고 여러 결과를 반환하는 여부에 대한 파라미터를 추가한 호출하는 함수 1개를 만들었다. 

```python 
def call_procedure(self, procedure_name, params, with_commit=False, with_next_set=False):
        try:
            self.open() 
            self.cursor.callproc(procedure_name, params)

            result1 = [row for row in self.cursor]
            
            if with_next_set:
                result2 = [row for row in self.cursor] 
                if with_commit: 
                    self.conn.commit() 
                self.close()
                return result1, result2
            else:
                if with_commit: 
                    self.conn.commit() 
                self.close()
                return result1
        except Exception as e:
            self.close()
            logger.exception(format_exc())
            return []
```

**위의 코드에서 몇가지 문제점이 있다.** 일단 `with_commit` 부분에 대한 중복이 있다. 그리고 DB가 반환하는 결과셋(result set)가 **2번이라는 가정을 기본적으로 가지고 있는 함수**이다. 만약 하나의 결과셋이 추가될 경우 대응이 어렵다. (가장 간단한 대응은 `procedure_name` 을 가지고 분기를 치는것이다.) 

아래의 코드는 python 의 `generator` 를 이용해서 개선한 버전이다. 일단 함수에서는 `yield` 를 통해서 generator 를 반환하고 프로시저를 호출하는 함수에서는 `generator.next()` 를 이용해서 결과셋을 몇번을 더 가져올 것인지를 결정할 수 있다. 즉, 호출을 대리하는 함수가 결정하는 것이 아니라, 호출을 하는 주체가 결정하게 된다. 그렇게 됨으로써 `call_procedure` 함수내에 있던 프로시저의 결과셋에 대한 종속성은 제거된다. 기존에 사용하던 `with_next_set` 파라미터 역시 더 이상 필요없기 때문에 제거했다. 

결과셋을 가져오는 것은 while 문 안에서 일어나게 되는데 while 문을 벗어나는 방법은 `GeneratorExit` 예외를 통해서 벗어나도록 되어있다. `GeneratorExit` 예외는 호출을 하는 주체가 `generator.close()` 를 호출하는 시점에 함수 내부에서 발생하게 되고 while 문이 종료되게 된다. 이 부분 역시 함수외부에서 함수내부를 제어하고 있는 부분이다. 

```python
def call_procedure(self, procedure_name, params, with_commit=False):
        try:
            self.open()
            self.cursor.callproc(procedure_name, params)
            while True:
                result = [row for row in self.cursor]
                try:
                    yield result
                except GeneratorExit:
                    break
            if with_commit: 
                self.conn.commit() 
            self.close()
        except Exception as e: 
            logger.exception(format_exc())
            self.close()
            raise e

# 호출하는 부분 


generator = self.call_procedure(procedure_name=PROCEDURES.PURCHASE_SELECT,
                                        params=param_instance.to_params())
result_list = generator.next() # 결과 하나 가져오기 
generator.close()

...
generator = self.call_procedure(procedure_name=PROCEDURES.PURCHASE_WITH_SUM_SELECT,
                                        params=param_instance.to_params())            

#결과 2개 가져오기 
sum_result = generator.next()            
result_list = generator.next()

generator.close() 
```

프로시저 당 하나의 함수를 만들어야 했던 문제도 해결 되었고, 각 프로시저마다 가지고있는 기능들을 호출하는 쪽에서 담당하게 되니 더 간결해진 것 같다. 제너레이터가 좋은 점은 많이 사용해 보진 않았지만, **호출하는 함수 내의 동작을 외부에서 제어할 수 있다는 점인 것 같다.** 어떻게 보면 이상하게 보일 수도 있지만, 좀 더 효율적으로 호출하는 방식이 될 수도 있다는 생각이 든다. 
