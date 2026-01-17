---
title: 'Postman에서 pre-request와 post-response 활용하기'
author: 'ash84'
pub_date: '2026-01-10'
description: 'Postman을 사용하다 보면 특정 변수를 매번 변경해서 요청을 보내거나, 이전 응답값을 다음 요청에 넘겨서 테스트해야 하는 경우가 있다. 이럴 때 pre-request와 post-response 스크립트를 활용하면 편리하다.'
tags: ['dev', 'postman', 'API', 'test']
---
# Postman에서 pre-request와 post-response 활용하기

Postman을 사용하다 보면 특정 변수를 매번 변경해서 요청을 보내거나, 이전 응답값을 다음 요청에 넘겨서 테스트해야 하는 경우가 있다. 이럴 때 **pre-request**와 **post-response** 스크립트를 활용하면 편리하다.

> 📚 **공식 문서**: [Use scripts to add logic and tests to Postman requests](https://learning.postman.com/docs/tests-and-scripts/write-scripts/intro-to-scripts/)

## Pre-request Script

```js
// 32자리 숫자 문자열 생성 (맨 앞자리 0 방지)
let pid = String(Math.floor(Math.random() * 9) + 1);
for (let i = 1; i < 32; i++) {
  pid += Math.floor(Math.random() * 10);
}
pm.environment.set("pid", pid);
console.log("pid:", pid);
```

서버에서 중복되지 않는 값을 전달해야 API 테스트가 가능한 경우가 있다. 이때 pre-request 스크립트에서 랜덤 값을 생성해 변수에 저장할 수 있다. 위 예제에서는 `pid`라는 32자리 숫자 문자열을 생성해 환경 변수에 저장하고 있다.

이렇게 저장한 값은 Postman request body에서 `{{pid}}` 형태로 참조하면 된다. 요청을 보내기 전에 pre-request 스크립트가 먼저 실행되어 변수에 값이 담기고, 그 후 요청이 전송된다.

> 📚 **공식 문서**: [Write pre-request scripts](https://learning.postman.com/docs/tests-and-scripts/write-scripts/pre-request-scripts/)

## Post-response Script

```js
const body = pm.response.json();
pm.environment.set("refund_document_number", body.data.refund_document_number);
```

이전 응답값을 다음 요청에서 사용해야 하는 경우도 있다. 예를 들어 결제 요청 시 승인번호를 받고, 이 승인번호로 결제 취소를 해야 한다면? 매번 응답값을 복사해서 붙여넣는 건 번거롭다.

post-response 스크립트를 활용하면 응답 JSON에서 필요한 값을 추출해 변수에 저장할 수 있다. 이후 요청에서는 `{{refund_document_number}}`처럼 변수로 바로 참조하면 된다.

> 📚 **공식 문서**: [Write scripts to test API response data](https://learning.postman.com/docs/tests-and-scripts/write-scripts/test-scripts/)

## 환경 변수 활용

`pm.environment.set()`과 `pm.environment.get()`을 사용하면 요청 간에 데이터를 쉽게 전달할 수 있다. 환경 변수는 Collection Runner에서 여러 요청을 순차 실행할 때 특히 유용하다.

> 📚 **공식 문서**:
> - [Edit and set environment variables](https://learning.postman.com/docs/sending-requests/variables/environment-variables/)
> - [Reference variables in scripts](https://learning.postman.com/docs/tests-and-scripts/write-scripts/postman-sandbox-reference/pm-variables/)

## Collection Runner로 순차 실행

이 기능들을 조합하면 여러 request를 하나의 폴더에 넣고 **Run**을 통해 순차적으로 실행할 수 있다.

```
1번 request의 pre-request 실행 → 변수 저장
↓
1번 request 실행
↓
1번 request의 post-response 실행 → 응답값을 변수에 저장
↓
2번 request에서 저장된 변수 활용
↓
...반복
```

> 📚 **공식 문서**:
> - [Test your API using the Collection Runner](https://learning.postman.com/docs/collections/running-collections/intro-to-collection-runs/)
> - [Customize request order in a collection run](https://learning.postman.com/docs/collections/running-collections/building-workflows/)

물론 curl이나 Python으로도 가능하지만, 스크립트 코드는 유지보수가 상대적으로 번거롭다. 개발자와 QA가 함께 Postman을 사용하는 조직이라면 이 방식을 적극 추천한다.
