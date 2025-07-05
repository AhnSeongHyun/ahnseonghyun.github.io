---
title: 'Rust 기본 문법'
author: 'ash84'
pub_date: '2018-10-04'
description: ''
featured_image: ''
tags: ['dev', 'rust', 'syntax']
---

## 변수

- 변수는 불변성
- 가변성 변수는 `mut` 를 추가

```rust
        let mut x = 5;
```

- 상수
    - 상수는 mut 을  쓸수 없음. 불변성 그 자체
    - const
    - 유형(데이터 타입)을 선언해야한다.
    - 상수표현식으로만 설정, 실행시간에 설정될 수 없다.

```rust
        const MAX_POINTS: u32 = 100_000;
```

- Shadowing
    - 같은 변수 이름을 써서 가리는 것

```rust
        let x = 1; 
        let x = x+1; 
```

- `mut` 사용과의 차이점
   - 변경이후 변수가 불변성을 가지느냐
   - 유형(데이터 타입)을 변경 할 수 있으면서, 같은 변수명을 유지
   - mut 을 이용더라도 유형 변경을 해서 값을 대입 시킬 수는 없다.

## 데이터 타입

- 러스트는 타입이 **고정된 언어**
- 스칼라 타입 : 하나의 값으로 표현되는 타입
    - 정수형
        - 8비트 : `i8(가장좋은 선택, 가장 빠르다)`, `u8`
        - 16비트 : `i16`, `u16`
        - 32비트 : `i32`, `u32`
        - 64비트 : `i64`, `u64`
        - arch :  isize, usize (컴퓨터의 아키텍처에 따라 결정)
        - 정수형 리터럴
            - Decimal : 98_222
            - HEX : 0xff
            - Octal : 0o88
            - Binary : 0b1111_0000
            - Byte(u8 only) : b'A'
    - 부동소수점 숫자
        - f32 : 1배수 정밀도
        - f64 : 2배수 정밀도
    - boolean : `true` `false`
    - 문자 : `char` , 단일 문자 표현
        - 작은따옴표로 표현

```rust
            let c = 'z'; 
```

- 복합타입
    - 튜플 : 소괄호로 표현, 타입을 명시해도 되고 안해도 된다.

```rust
        let tup: (i32, f64, u8) = (500, 6.4, 1);
        let (x, y, z) = tup;
        // 직접접근 
        tup.0, tup.1, tup.2
```

    - 배열 : 모든요소가 같은 타입. [index] 를 통한 접근

## 함수

- fn test(x: i32, y: i32)
- 반환 : `x+1` 세미콜론 없이
    - `return` 키워드 사용 가능
- 함수포인터

```rust
    // 타입 추론 없이
    // without type inference
    let f: fn(i32) -> i32 = plus_one;
    
    // with type inference
    // 타입 추론 사용
    let f = plus_one;
```

## 주석

- `//` : 한줄주석
- `///` :  문서주석
- 내용은 마크다운 표기지원
- rustdoc 을 이용한 문서화 가능

## 제어문

- `if-else if-else 구조`

```rust
    if number % 4 == 0 {
        println!("number is divisible by 4");
    } else if number % 3 == 0 {
        println!("number is divisible by 3");
    } else if number % 2 == 0 {
        println!("number is divisible by 2");
    } else {
        println!("number is not divisible by 4, 3, or 2");
    }
```

- if 문 결과를 변수에 할당

```rust
    let number = if condition {
       5
    } else {
       6
    };
```

## 반복문

- `loop` 무한루프
    - 무한루프일때 쓸것
- `for`

```rust
    for number in (0..10){
    //
    }
    
    let a = [10, 20, 30, 40, 50]
    for element in a.iter() {
    //
    }
```

- `while`

```rust
    while number != 0 {
    	println!("{}!", number);
    	number = number - 1;
    }
```
