---
title: 'Rust  Cargo'
author: 'ash84'
pub_date: '2018-10-02'
description: '## cargo 명령어 정리 

### 프로젝트 생성 

`cargo new —bin `

```
├── Cargo.lock
├── Cargo.toml
└── src
    └── main.rs

1 directory, 3 files
```

### 빌드 및 실행 

- `cargo build`: 컴파일 
- `cargo run` : 바로 실행 
- `cargo check` : 문법체크 
- `cargo clean` : 컴파일 정리 
- `cargo new` : 프로젝트 생성 
- `cargo init` : 프로젝트 생성('
featured_image: ''
tags: ['dev', 'rust', 'cargo']
---

## cargo 명령어 정리 

### 프로젝트 생성 

`cargo new —bin <app>`

```
├── Cargo.lock
├── Cargo.toml
└── src
    └── main.rs

1 directory, 3 files
```

### 빌드 및 실행 

- `cargo build`: 컴파일 
- `cargo run` : 바로 실행 
- `cargo check` : 문법체크 
- `cargo clean` : 컴파일 정리 
- `cargo new` : 프로젝트 생성 
- `cargo init` : 프로젝트 생성(이미 존재하는 디렉토리에 생성 가능)
- `cargo test` : tests 실행 
- `cargo bench` : 벤치마크 실행 
- `cargo update` : 의존성 업데이트 
- `cargo search` : crates 검색 

```shell

$ cargo search web      
                                                                                                                                                         
Updating registry `https://github.com/rust-lang/crates.io-index`

web = "0.0.2"                    # ...

cargo-web = "0.6.16"             # A Cargo subcommand for the client-side Web

actix-web-requestid = "0.1.2"    # Request ID middleware for actix-web

stdweb = "0.4.9"                 # A standard library for the client-side Web

... and 665 crates more (use --limit N to see more)
```

- `cargo publish` : 패키징 및 해당 프로젝트 등록 
- `cargo install ` : Rust binary 설치 
- `cargo uninstall`: Rust binary 제거 

ps) 컴파일러면서 python pip 를 섞어놓은 느낌.
