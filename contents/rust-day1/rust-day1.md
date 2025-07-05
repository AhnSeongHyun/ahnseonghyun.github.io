---
title: 'Rust-DAY1'
author: 'ash84'
pub_date: '2020-01-08'
description: ''
featured_image: ''
tags: ['rust', '100DaysOfRust']
---

![sun](https://live.staticflickr.com/65535/49351849271_1a8164bbd0_z.jpg)

[sun](https://github.com/AhnSeongHyun/sun)
- 간단한 프로그램을 배우면서 Rust 를 배워서 남주자!
- multiple host  에  shell 명령어를 보내고 그것을 보여주는 단순한 CLI 프로그램(사실 python ansible 조합이면 금방 될것 같지만...)
- github action 에 CI 관련 스트립트 정의하고 시작! 

```yaml
    name: CI
    
    on: [push]
    
    jobs:
      build:
    
        runs-on: ubuntu-latest
    
        steps:
        - uses: actions/checkout@v1
        - name: Build
          run: cargo build --verbose
        - name: Run tests
          run: cargo test --verbose
        - name: Check Lint
          run: cargo fmt --all -- --check --verbose
```

- 언제든 PR 리뷰 및 피드백은 환영 입니다.

---

**개발 환경 구성하기** 

- Jetbrains Intellij + Rust plugin 으로 세팅완료
- vscode 에 플러그인은 Rust 와 Rust(rls) 만 설치해서 쓸 수 있지만 같은 사용자(나)의 경험으로 개발하고 싶어서 jetbrains 계열 선택
- 생각보다 자동완성이 나쁘지 않아서 사용중
-

**clap**

- CLI 프로그램에서 help 나 arg 들을 받는 것을 구성하기 위해서 clap 라는 crate 를 `Cargo.toml` 에 추가했다.

```toml
    [dependencies]
    clap = "~2.33.0"
```

---

**Custom Type 정의하기** 

- clap 으로 command line argument 를 가져왔는데 host 를 정의한 host.yaml 의 경로와 입력한 shell command 를 분리하기 위해서 `parse_arg` 함수를 구현
- Tuple 형태로 `(String, String)` 이렇게 리턴하면 덜 명시적이어서 CustomType 을 정의해본다.

```rust
    type HostFilePath = String;
    type Input = String;
```

**Reference** 

- [https://doc.rust-lang.org/stable/rust-by-example/primitives/tuples.html](https://doc.rust-lang.org/stable/rust-by-example/primitives/tuples.html)

** 아직 모르는것 :** 

- Custom Error 를 만들고 그것을 throw 하는 방법?
- intellij 에서 rust debug mode 연결 하는 법?
