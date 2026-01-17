---
title: Rust-DAY2
author: ash84
pub_date: '2020-01-28'
description: 'TestCase 를 작성해보자. #2 - 원래 프로젝트는 대략적인 구조는 이런식이었다. ``` ├── Cargo.lock
  ├── Cargo.toml ├── Makefile ├── README.md ├── resource │ └── host.yaml └── src ├──
  arg.rs ├── config.rs ├── main.rs'
featured_image: ''
tags:
- rust
- 100DaysOfRust
- panic
- testcase
---

**TestCase 를 작성해보자.  [#2](https://github.com/AhnSeongHyun/sun/pull/2)**

- 원래 프로젝트는 대략적인 구조는 이런식이었다.

```
    ├── Cargo.lock
    ├── Cargo.toml
    ├── Makefile
    ├── README.md
    ├── resource
    │   └── host.yaml
    └── src
        ├── arg.rs
        ├── config.rs 
        ├── main.rs
        └── misc.rs
```

- `src` 는 실제 소스코드가 있는 부분으로 `tests` 를 만들어서 테스트케이스 부분을 분리하려고 했다.
- 그런데`src` 안에 있는 `main.rs`, `[misc.rs](http://misc.rs)` 안에 있는 함수들에 대한 테스트를 하려고 했는데 안된다. 안되는 부분은 함수들을 import 하는 부분에서 인식을 시키지 못하는 문제가 있었다.
- 찾아보니 rust 에서는 `src/lib.rs` 이렇게 만들고 그 안에서 정의한 것들을 외부에서 crate 로 인식시켜서 사용한다. 

```rust
        // src/lib.rs
        pub mod arg;
        pub mod config;
        pub mod misc;

        // tests/test_arg.rs
        #[cfg(test)]
        mod test {
            use sun::arg::parse_arg;
            ...
```

- 최종적으로 변경한 디렉토리 구조
```
    .
    ├── Cargo.lock
    ├── Cargo.toml
    ├── Makefile
    ├── README.md
    ├── resource
    │   └── host.yaml
    ├── src
    │   ├── arg.rs
    │   ├── config.rs
    │   ├── lib.rs
    │   ├── main.rs
    │   └── misc.rs
    └── tests
        ├── test_arg.rs
        └── test_misc.rs
```

**왜 내 프로젝트엔 [`lib.rs`](http://lib.rs) 가 없었을까?** 

- 처음에 `cargo new sun --bin` 명령어를 통해서 프로젝트를 생성. `--bin` 은 [main.rs](http://main.rs) 를 만들어 주지만 [`lib.rs`](http://lib.rs) 는 만들어 주지 않는다.
- [`lib.rs`](http://lib.rs) 를 만들려면 수동으로 만들거나 `cargo new sun --lib` 로 생성 해야한다. 

```
    --bin      Use a binary (application) template [default]
    --lib      Use a library template
```

**`panic!` 테스트 하기** 

- rust 에서는 `panic!` 을 통해서 복구 할 수 없는 에러를 만들수 있는데 어떤 함수에서 이를 뱉는 경우 이것을 테스트 하려면 어떻게 해야할까?
- 예를 들면 파일을 읽어오는 함수에서 파일을 읽어오지 못하는 경우 `expect` 를 이용해서 `panic` 에러를 발생시킨다고 하면 이런식이다.

```rust
        fs::read_to_string(file_name).expect("no file");

        #[test]
        #[should_panic]
        fn test_load_yaml_abnormal_path() {
            load_yaml(String::from("test"));
        }
```

  테스트 코드에서는 `[should_panic]` 을 적어주면 된다. 

**기타** 

- 특정 테스트를 무시시키고 싶으면 `#[ignore]` 를 쓰자.

**References**
- [https://doc.rust-lang.org/rust-by-example/testing/unit_testing.html](https://doc.rust-lang.org/rust-by-example/testing/unit_testing.html)
