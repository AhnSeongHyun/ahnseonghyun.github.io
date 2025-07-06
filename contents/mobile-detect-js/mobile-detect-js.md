---
title: 'mobile-detect.js'
author: 'ash84'
pub_date: '2016-08-13'
description: '정밀하게 useragent로 안드로이드인지, 아이폰인지, 크롬인지, 파폭인지 구분해야 하는 것도 중요하지만, 때로는 그냥 모바일이냐 데스크탑이냐를 구분짓고 싶을때가 많다. 그래서 찾던것 중에 `mobile-detect.js` 라는 것이 있는데 쉽게 자바스크립트 단에서 쓸 수 있는것 같다.

[https://github.com/serbanghita/Mobile-Detect](https://github.com/serbanghita/Mobile-Detect)  
[http://hgoebl.github.io/mobile-detect.js'
featured_image: ''
tags: ['desktop', 'dev', 'mobile']
---


정밀하게 useragent로 안드로이드인지, 아이폰인지, 크롬인지, 파폭인지 구분해야 하는 것도 중요하지만, 때로는 그냥 모바일이냐 데스크탑이냐를 구분짓고 싶을때가 많다. 그래서 찾던것 중에 `mobile-detect.js` 라는 것이 있는데 쉽게 자바스크립트 단에서 쓸 수 있는것 같다.

[https://github.com/serbanghita/Mobile-Detect](https://github.com/serbanghita/Mobile-Detect)  
[http://hgoebl.github.io/mobile-detect.js](http://hgoebl.github.io/mobile-detect.js/)

```javascript
var md = new MobileDetect(window.navigator.userAgent); if(md.mobile()){ 
  //mobile 
} 
else { 
//pc 
}
```



