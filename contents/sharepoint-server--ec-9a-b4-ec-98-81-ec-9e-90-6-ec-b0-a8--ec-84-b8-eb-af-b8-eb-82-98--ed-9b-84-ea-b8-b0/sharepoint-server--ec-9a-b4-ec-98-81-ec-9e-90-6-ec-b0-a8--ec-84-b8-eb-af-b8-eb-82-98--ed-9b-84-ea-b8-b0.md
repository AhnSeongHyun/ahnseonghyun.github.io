---
title: 'SharePoint server 운영자 6차 세미나 후기'
author: 'ash84'
pub_date: '2011-12-18'
description: '![](http://ash84.net/wp-content/uploads/1/cfile23.uf.194249474EEFCB5910C9D2.png)

 

**세션 3 디자이너 +'
featured_image: ''
tags: ['dev', 'Microsoft', 'server']
---
<div><font class="Apple-style-span" color="#000000" face="'lucida grande', tahoma, verdana, arial, sans-serif"><span class="Apple-style-span" style="font-size: 11px; line-height: 16px;">![](http://ash84.net/wp-content/uploads/1/cfile23.uf.194249474EEFCB5910C9D2.png)

 

</span></font>**세션 3 디자이너 + infopath = sharepoint application**</div><div style="line-height: 2; "></div><div style="line-height: 2; "></div>예를 들어 자동결제 시스템을 만든다면,

<div style="line-height: 2; "></div>Form(InfoPath) + WorkFlow(Share Point Designer) + Web Part(Share Point Server)

<div style="line-height: 2; "></div><div style="line-height: 2; "></div>**1.  InfoPath**

<div style="line-height: 2; "></div>– form : 사용자가 입력하는 폼

<div style="line-height: 2; "></div>– infopath를 통해서 일반 사용자도 쉽게  폼을  제작할 수 있다.

<div style="line-height: 2; "></div>– 누구나 쉽게 사용가능하고, share point 서버를 위해서 존재 

<div style="line-height: 2; "></div>– 드래그 앤 드롭으로 컨트롤 설정

<div style="line-height: 2; "></div><div style="line-height: 2; "></div>**제작 과정**

<div style="line-height: 2; "></div>– 새로운 컨트롤 추가 -> 이름 지정 -> 미리보기 확인 -> share point 에 바로 게시 가능 -> 데이터 필드 promoting 여부 지정 가능

<div style="line-height: 2; "></div><div style="line-height: 2; "></div>*** Promoting**

<div style="line-height: 2; "></div>– 지정한 데이터 필드가 share point 뷰에 나타난다. 

<div style="line-height: 2; "></div>– 해당 필드 검색이 가능하고, 그룹 지정 가능

<div style="line-height: 2; "></div>– 해당 필드를 워크 플로우에서 사용가능함. 

<div style="line-height: 2; "></div><div style="line-height: 2; "></div>*** 사용자가 잘못된 데이터를 폼에 입력시?**

<div style="line-height: 2; "></div>– 입력 validation check를 워크 플로우가 아닌 form 게시전에 infopath에서 설정을 통해서 해주는 것이 best practice. 

<div style="line-height: 2; "></div><div style="line-height: 2; "></div>*** infopath 의 UI에 대한 내용은 XML의 형태로 Share Point에 저장된다. **

<div style="line-height: 2; "></div><div style="line-height: 2; "></div>* 기존에 저장한 폼 양식에 새로운 폼 양식을 추가시, 이전 데이터 입력한 것을 눌러도 새로운 양식에 대입되어 나온  
   다. 

<div style="line-height: 2; "></div><div style="line-height: 2; "></div>**2. workflow**

<div style="line-height: 2; "></div>– 마이크로소프트의 비지오를 통해서 개발할수 있지만, 프리젠테이션 일뿐 실제로는 SPD(Share Point Designer)를   
   통해서 개발해야함. 

<div style="line-height: 2; "></div>– 비지오로 만든 경우, 100% share point의 워크 플로우로 만들수 없다. 

<div style="line-height: 2; "></div>– 비지오는 시각적으로 도와주는 것 뿐이다. 

<div style="line-height: 2; "></div>– 비지니스 요구는 계속 변한다. 그래서 워크플로우를 잘 만들어야 한다. 

<div style="line-height: 2; "></div>– 기존의 워크플로우에 최신 버전의 워크플로우 추가시, 폼과는 다르게 두가지 버전을 유지하게 된다. 

<div style="line-height: 2; "></div>– 최신 버전만을 유지하려면 삭제/취소 혹은 완료 될때까지 기다려야 한다. 

<div style="line-height: 2; "></div><div style="line-height: 2; "></div>*** SPD(Share Point Designer)**

<div style="line-height: 2; "></div>– 디자이닝 툴, 코드가 아님, 커스텀 솔루션 개발 가능하며, 워크플로우 제작가능, 기본 제공 되는 것이 있으나 기능이   
   제한적. 커스텀이 가능함.

<div style="line-height: 2; "></div><div style="line-height: 2; "></div>**3. Web Part**

<div style="line-height: 2; "></div>– 커스텀 웹 파트를 만들수 있고, 이미 많은 관련 운영자, 개발자들이 자료들을 올려두었다. 그냥 써라. 

<div style="line-height: 2; "></div><div style="line-height: 2; "></div><div style="line-height: 2; "></div>**Share Point 2010 **<span class="s1">**실전 운영 기법 **</span>

<div style="line-height: 2; "></div>**1) ULSLog **

<div style="line-height: 2; "></div>– 운영하다 에러나면, 윈도우 이벤트 로그와 ULS 로그를 확인해라 

<div style="line-height: 2; "></div>– 그런데 ULS 로그가 텍스트 파일이고 컬럼 구분이 없다. 엑셀에서 파일을 가져와서 탭으로 구분해서 넣으면 쉽게 볼  
   수 있다. 

<div style="line-height: 2; "></div>– 위치는 “설치폴더\logs\”에 있다. 

<div style="line-height: 2; "></div>– 다양한 로그 뷰어도 있으니 쓰시길. 

<div style="line-height: 2; "></div><div style="line-height: 2; "></div>**2) Health Analyzer**

<div style="line-height: 2; "></div>– 서버 상태 체크 

<div style="line-height: 2; "></div>– 타이머 잡을 이용, 중앙 관리에서 설정이 가능함. 

<div style="line-height: 2; "></div><div style="line-height: 2; "></div>**3) 사이트 사용량 설정**

<div style="line-height: 2; "></div>– 사이트 컬렉션 단위로 설정 가능함. 

<div style="line-height: 2; "></div><div style="line-height: 2; "></div>**4) 사이트 잠금**

<div style="line-height: 2; "></div>– 옵션이 있고, 재기동 하지 않아도 됨. 

<div style="line-height: 2; "></div><div style="line-height: 2; "></div>**5) 파일 확장자 제한**

<div style="line-height: 2; "></div>– 중앙관리 ->Security에 있음. 

<div style="line-height: 2; "></div><div style="line-height: 2; "></div>**6) Authentication**

<div style="line-height: 2; "></div>– 자격증명을 관리할수 있도록, 서버의 로그인 기록을 남긴다. 

<div style="line-height: 2; "></div><div style="line-height: 2; "></div>**7) 휴지통**

<div style="line-height: 2; "></div>– 2 개의 휴지통이 있다. 

<div style="line-height: 2; "></div>– 1단계 휴지통은 우리가 말한는 그냥 휴지통. 사용자가 사용. 

<div style="line-height: 2; "></div>– 2단계 휴지통은 관리자가 접근, 1단계에서 완전 삭제한 파일도 복원 가능하다. 

<div style="line-height: 2; "></div><div style="line-height: 2; "></div>**8) 검색 크롤링 시간 설정**

<div style="line-height: 2; "></div>– 전체 크롤링과 증분 크롤링

<div style="line-height: 2; "></div>– 서버에서 선택할 수 있다. 

<div style="line-height: 2; "></div>****

<div style="line-height: 2; "></div>**3. Share Point Online ** 

<div style="line-height: 2; "></div>– office365.com : 오피스 + 쉐어포인트 + 메일을 클라우드 서비스 형태로 제공해줌. (Saas)

<div style="line-height: 2; "></div>– 일정 수준의 월 금액을 지불해서 쓰는 형태 

<div style="line-height: 2; "></div>– 현재 트라이얼 사용 가능함.(30일) 이미 여러 업체에서 사용중. 

<div style="line-height: 2; "></div><font color="#e31600">– 주의사항 : 트라이얼 사용시의 도메인 이름 설정이 기간 이후에도 지속되므로 신중하게 해야함. </font>

<div style="line-height: 2; "></div>– 이전에 서버 버전처럼 전체의 기능을 다 지원하지 않지만 소규모 및 특별한 개발 없이 사용하기 편함. 

<div style="line-height: 2; "></div>– 마이크로소프트에서 실제 서버는 운영되는거지만, 개발자가 제한된 영역에 대한 개발은 가능함

<div style="line-height: 2; "></div>– Client Object로 개발 접근 가능. 

<div style="line-height: 2; "></div>– 기존 서버 버전에서 제공되던 FAST Search 제공되지 않음. 

<div style="line-height: 2; "></div>– 현재 외국에서 많이 사용중. 발전의 여지가 있음. 

  



