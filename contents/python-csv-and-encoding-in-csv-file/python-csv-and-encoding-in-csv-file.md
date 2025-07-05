---
title: 'python csv and encoding in csv file.'
author: 'ash84'
pub_date: '2015-09-03'
description: ''
featured_image: ''
tags: ['csv', 'encoding', 'Python', 'python2.7', '파이썬']
---


<script src="https://gist.github.com/AhnSeongHyun/6a9470d71b68ab474f49.js"></script>

 파이썬의 csv 모듈을 이용해서 MS Excel2010 에서 만든 csv 형식을 가져오는 코드이다. 별것 없는 코드를 올리는 이유는 단연 인코딩 때문인데 csv 모듈은 파이썬2.7 에서 다음과 같은 내용이 있다.

> **Note This version of the csv module doesn’t support Unicode input. Also, there are currently some issues regarding ASCII NUL characters. Accordingly, all input should be UTF-8 or printable ASCII to be safe; see the examples in section Examples.**

CSV 내 영어가 아닌 한국어나 중국어, 일본어 등이 있을때 읽어올때 깨지는 문제가 발생되는데 위의 주의사항과는 결론적으로 말하자면 상관이 없다. 읽어올때 제대로 읽어오기 위해서는 CSV 자체가 만들어진 환경과 연관이 있는것 같다는것이 내 생각이다. 현재는 윈도우 한글버전내 EXCEL2010에서 CSV를 생성해서 euckr로 인코딩이 되는것 같다. 처음에는 위의 문구에 현혹되어서, 그리고 당연히 UTF-8(요즘이 어떤 시대임)로 CSV가 저장될줄 알았는데 그렇지 않았고, 일본어가 있어서 일본어 관련 인코딩도 넣어보고, CP1250, ISO5589-1 도 넣어봤는데 소용이 없었다.

  
 사용자가 절대 CSV 를 메모장에서 만들거나 혹은 EXCEL에서 만들때 인코딩을 지정해서 저장할 일이 없기 때문에 처리해줘야 하는 부분이다. 궁금한것중 하나는 일본사람이나 중국사람이 해당 윈도우내 EXCEL에서 CSV를 만들면 어떻게 처리해야 할지 궁금해진다.

 python 3.4.3 CSV Module : [https://docs.python.org/3.4/library/csv.html](https://docs.python.org/3.4/library/csv.html)



