---
title: '[펌] MS-SQL : 저장 프로시저 만들기'
author: 'ash84'
pub_date: '2008-05-22'
description: '출처 : [http://cafe.naver.com/hackertime/397](http://cafe.naver.com/hackertime/397)

  



  
**저장 프로시저 만들기**

  
  
사용법)'
featured_image: ''
tags: ['dev', 'MSSQL', '저장프로시저']
---


출처 : [http://cafe.naver.com/hackertime/397](http://cafe.naver.com/hackertime/397)

  
<table border="0" cellpadding="0" cellspacing="0" id="tblContent" width="740">  
<tbody>  
<tr>  
<td>  
**<font color="#333333" style="BACKGROUND-COLOR: #e4ff75">저장 프로시저 만들기</font>**

  
  
사용법)

  
<font color="#ff3399">CREATE PROC[EDURE] 저장 프로시저 이름  
[저장 프로시저의 매개 변수 목록]  
AS  
 저장 프로시저 내에서 실행될 쿼리들</font>

  
 

<font color="#c1c1c1">  
**1. 매개변수 없는 프로시져**

</font>  
<font color="#333333"><font color="#c1c1c1">예)</font></font>

  
<font color="#c1c1c1">CREATE PROC up_member</font>

  
<font color="#c1c1c1">AS</font>

  
<font color="#c1c1c1">Begin   
 SELECT *  
 FROM test_member</font>

  
<font color="#c1c1c1">End</font>

  
  
<font color="#c1c1c1">실행명령 </font>:  <font color="#d41a01">EXEC 실행할 저장 프로시저 이름 (EXEC up_member)</font>

  
 

  
**<font color="#c1c1c1">2. 매개변수 있는 프로시져</font>**

  
<font color="#c1c1c1">예)</font>

  
<font color="#c1c1c1">CREATE PROC up_member</font>

  
<font color="#c1c1c1">@id varchar(20)</font>

  
<font color="#c1c1c1">AS</font>

  
<font color="#c1c1c1">Begin   
 SELECT *  
 FROM test_member</font>

  
<font color="#c1c1c1"> WHERE </font>[<font color="#c1c1c1">member_id=@id</font>](mailto:member_id=@id)

  
<font color="#c1c1c1">End</font>

  
  
<font color="#d41a01"><font color="#333333"><font color="#c1c1c1">실행명령 :</font>  </font><font color="#d41a01">EXEC 실행할 저장 프로시저 이름 변수 (EXEC up_member ‘sunmi’)</font></font>

  
 

  
**<font color="#c1c1c1">3. 리턴값을 갖는 프로시져</font>**

  
<font color="#c1c1c1">예)</font>

  
<font color="#c1c1c1">CREATE PROC up_member</font>

  
<font color="#c1c1c1">AS</font>

  
<font color="#c1c1c1">Begin </font>

  
<font color="#c1c1c1"> DECLARE @Count int  
 SELECT @Count = count(*)  
 FROM test_member</font>

  
<font color="#c1c1c1"> RETRUN @Count</font>

  
<font color="#c1c1c1">End</font>

  
 

  
<font color="#c1c1c1">실행명령 :  </font>

  
<font color="#d41a01">DECLARE @Count int  
EXEC @Count = up_member  
SELECT @Count</font>

  
 

  
**4. OUTPUT 매개변수 이용하는 프로시져**

  
예)

  
CREATE PROC up_member

  
@Count int OUTPUT  
AS

  
<font color="#c1c1c1">Begin </font>

  
  SELECT @Count = count(*)  
 FROM test_member

  
End

  
  
<font color="#c1c1c1">실행명령 :  </font>

  
<font color="#d41a01">DECLARE @Count int  
EXEC  up_member @Count OUTPUT  
SELECT @Count</font>

  
 

<font color="#333333">  
**<font color="#c1c1c1">5. 프로시져 삭제하기</font>**

  
<font color="#c1c1c1">– drop proc 프로시저명</font>

  
 

  
**<font color="#c1c1c1">6 프로시져 수정하기</font>**

  
<font color="#c1c1c1">–</font>

  
<font color="#c1c1c1">ALTER PROC 수정할 SP 이름  
[프로시저 매개 변수 목록]  
AS  
실행할 쿼리 문장들</font>

</font>  
 

  
**<font color="#c1c1c1">7. 프로시저내에 분기</font>**

  
**<font color="#c1c1c1">–</font>**

  
CREATE PROC  sp_UpPrice  
    @type    char(12),  
    @plus    Float  
AS  
Begin   
    Declare @Check    int

    Select @Check = Max(price) from titles  
    Where type = @type

    if @Check < 50   
        Begin  
            Update titles SET price = price + @plus  
            Where type = @type

            Select @Check = 1  
        End  
    Else  
        Select @Check = 0

    Return @Check  
End

</td></tr></tbody></table>  
 



