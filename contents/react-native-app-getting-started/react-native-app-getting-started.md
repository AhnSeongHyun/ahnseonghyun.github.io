---
title: 'React Native App 시작하기'
author: 'ash84'
pub_date: '2017-11-03'
description: '이 글은  [React Native Getting Started](https://facebook.github.io/react-native/docs/getting-started.html) 에 대한 삽질기입니다. 


### **node.js & npm 설치**

https://nodejs.org/en/download/


### **설치 진행**

```
$ npm install -g create-react-native-app
$ create-react-native-app toystory_app
```

npm5 에 문제가 있다고 아'
featured_image: ''
tags: ['dev', 'react', 'react native', 'watchman']
---

이 글은  [React Native Getting Started](https://facebook.github.io/react-native/docs/getting-started.html) 에 대한 삽질기입니다. 


### **node.js & npm 설치**

https://nodejs.org/en/download/


### **설치 진행**

```
$ npm install -g create-react-native-app
$ create-react-native-app toystory_app
```

npm5 에 문제가 있다고 아직 지원을 못한다는 에러 발견 

- https://github.com/npm/npm/issues/16991

아래와 같이 npm 버전을 돌리는.. (몬지 몰겠음?)

```shell
$ sudo npm i npm@4 -g
Password:
/usr/local/bin/npm -> /usr/local/lib/node_modules/npm/bin/npm-cli.js
+ npm@4.6.1
added 32 packages, removed 193 packages and updated 267 packages in 10.019s
$ create-react-native-app toystory_app
The directory `toystory_app` contains file(s) that could conflict. Aborting.
$ ls
README.md            config.py            toystory_app
__pycache__          crawling_coordinator
app                  db
$ rm -rf toystory_app
$ create-react-native-app toystory_app
```

### **실행**

toystory_app 이 생겼고 이제 실행을 해보자. 

또 에러 발생.. 암 걸릴듯 
```
$ cd torystory_app
$ npm start
...

21 error code ELIFECYCLE
22 error errno 1
23 error toystory_app@0.1.0 start: `react-native-scripts start`
23 error Exit status 1
24 error Failed at the toystory_app@0.1.0 start script.
24 error This is probably not a problem with npm. There is likely additional logging output above.
25 verbose exit [ 1, true ]
```

**watchman 설치**

```
brew install watchman
```

watchman 을 설치하고 다시 실행하게 되면 아래와 같은 화면이 출력된다. 

![https://farm5.staticflickr.com/4580/38332773422_5627419164_b.jpg](https://farm5.staticflickr.com/4580/38332773422_5627419164_b.jpg)

expo 라는 앱을 아이폰에 다운을 받고 개발환경와 동일한 wifi 를 연결한 후에 expo 를 실행해서 위의 QR코드를 찍으면 아래와 같은 화면으로 연결된다. 별 다른 화면이 없는데, 실제 App.js 에 있는 내용이 출력된 것이다. 

```js
export default class App extends React.Component {
  render() {
    return (
      <View style={styles.container}>
        <Text>Open up App.js to start working on your app!</Text>
        <Text>Changes you make will automatically reload.</Text>
        <Text>Shake your phone to open the developer menu.</Text>
      </View>
    );
  }
}
```

![https://farm5.staticflickr.com/4576/37649918844_1095ea4b3b_b.jpg](https://farm5.staticflickr.com/4576/37649918844_1095ea4b3b_b.jpg)
