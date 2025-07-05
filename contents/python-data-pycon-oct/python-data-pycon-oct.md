---
title: '2017년 10월 파이썬 세미나 - Python & Data'
author: 'ash84'
pub_date: '2017-10-24'
description: ''
featured_image: ''
tags: ['conference', 'Python', '파이썬', 'data', 'pandas']
---

파이콘에서 주최하는 세미나가 있어서 참석하게 되었다. 역삼동에 있는 페이스북 코리아에서 열리게 되었고 간단하게 들었던 부분을 남겨본다. 

http://blog.pycon.kr/2017/10/21/python-seminar/


**데이터 시각화를 통한 파이썬 입문기 - 이왕원** 

- 크롤링, konply, word-cloud

**도시공학과의 파이썬 - 정겨울** 

- 도시공학 : 설계, 기후, 교통 
- 학식알리미(python + flask) : 로그의 그래프화 matplotlib 라이브러리, `plt.xkcd()`
- 어디에 국공립 어린이집을 지으면 좋을까? : QGIS, 파일편집툴(+pypy)
- 물류센터 문제점 : 물류센터 그리기,  GIS 라이브러리를 사용하지 못함. BaseMap의 필요성,  ScikitLearn(X), Pandas, 주피터 노트북
- 서울시 빅테이터센터

**만약 고교 사회선생님이 파이썬 코드를 읽는다면? - 송석리**

- 공공 데이터 포털 : 잘 관리가 안되고 있음. 체계적 관리 필요
- 티머니 데이터 : tmoney.co.kr, 이용안내 > 대중교통 통계자료
  - 버스정류장별 이용현황, 지하철 유무임별 이용현황, 지하철 시간대별 이용현황 
- 데이터가 이야기 해주는 것 vs. 데이터가 이야기 해주지 않는것. 
- 데이터가 모든것을 말해주지 않는다는 비판적인 시각
- 데이터 분석을 통한 근거에 의한 판단, 데이터를 만져보는 코딩 경험, 데이터를 통한 흥미 유발 

**파이썬으로 풀어보는 아주 심플한 검색엔진의 원리 - 강대명**

- 검색엔진이 필요해 > elastic, solr 
- 색인과 질의
  - 색인 : 크롤링/데이터수집(파일, 시스템) + 역인덱스 구성
  - 질의 : 인덱스 + 랭킹 

- 크롤링
  - robot.txt 는 상업적으로 사용할 경우 지키기 
  - 자바스크립트가 있는 경우 : headless 브라우저 
  - 구글 검색봇을 우리를 공격한다. > 서버 부하 
  - 부하를 줄 정도로 크롤링을 하지 말자 > IP차단 
  - 링크 추출 
  - 의미있는 파라미터만 추출 : 네이버 뉴스 aid, oid
  - 인코딩 변경 
  - 재방문 주기 : 방문주기를 체크, 자주 방문 > 덜 방문 
  - 저장 : big table, GFS

- 색인
  - TF/IDF(Inverted index)
  - stemming, 형태소분석, n-gram 방식 


**pandas contribution 하기 - 김영근**

- 기분이 좋아서 한다. 
- 컨트리뷰터를 환영하고 있다. (쉬운이슈, 오타 등등)
- 스타를 찍고 시작.
- 기부 : NumFocus(https://numfocus.org)
- 문서화 : `DOC:` prefix 붙이기 
- https://github.com/lyda/mispell-check
- 이슈리포트 : duplicated 확인, 이슈템플릿, 이슈말머리
- 코드변경 : 이슈리포트 => 내가볼게, 속도전 
- 이슈헌팅 : Label 이 있음 good first issue 부터 시작. 
- clone - upstream 
- 버그 찾기 : `pdb.set_trace()`, 범위좁히면서 테스트 
- 수정후 테스트 필수, 내테스트 > 전체 테스트 > 스타일체크(PEP8)
- What's new 에 변경사항 추가 
- PR 만들어서 발사!, 되도록 커밋은 하나로, commit squash 
