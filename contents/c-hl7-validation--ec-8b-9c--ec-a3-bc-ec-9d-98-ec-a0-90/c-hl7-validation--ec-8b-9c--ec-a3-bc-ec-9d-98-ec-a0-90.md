---
title: '[C#] HL7 Validation 시, 주의점.'
author: 'ash84'
pub_date: '2015-07-03'
description: ''
featured_image: ''
tags: ['c#', 'dev', 'HL7', 'ValidationCheck', 'XSD', '스키마', '예외', '프로그래밍']
---


 

  
HL7 Validation 시 주의점, 대부분의 XML의 Validation은 별 문제가 없었지만, HL7 같은 경우는 다음과 같은 예외가 발생했다.

  
<div class="txc-textbox" style="BORDER-BOTTOM: #9fd331 1px solid; BORDER-LEFT: #9fd331 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #e7fdb5; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #9fd331 1px solid; BORDER-RIGHT: #9fd331 1px solid; PADDING-TOP: 10px">  
 Code

  
  try  
             {  
                 string path = @”C:\temp.xml”;

  
  
                 XmlReaderSettings xs = new XmlReaderSettings();  
                 xs.ValidationType = ValidationType.Schema;  
                 xs.Schemas.Add(“urn:hl7-org:v3″, @”C:\PORT_MT020001.xsd”);  
                 xs.ValidationFlags = XmlSchemaValidationFlags.ReportValidationWarnings;  
                 xs.ValidationEventHandler += new ValidationEventHandler(ValidationCallBack);

  
  
                 XmlReader xmlreader = XmlReader.Create(path, xs);

  
               

  
                while (xmlreader.Read())  
                 {

  
                    //문서처리

  
                }

  
                xmlreader.Close();

  
  
             }  
             catch (XmlSchemaValidationException ex)  
             {  
                 MessageBox.Show(ex.LineNumber.ToString() + “:” + ex.LinePosition.ToString())

  
            }

</div>  
 

  
발생한 예외

  
 [#M_더보기|접기|  
 

  
![](http://ash84.net/wp-content/uploads/1/48a26059d77638I.jpg)

_M#]  
 

  
targetNamespace도 제대로 설정했는데, Classes가 무엇인지 계속 찾아 봐도 알수가 없었다.

  
실제로 HL7 홈페이지에서 제공한 Example과 스키마를 이용했는데도 위와 같은 에러가 났었다.

  
문제는 프로그램 코드에 있는 것이 아니였다.

  
 

  
PORT_MT020001.xsd의 일부

  
<div class="txc-textbox" style="BORDER-BOTTOM: #79a5e4 1px solid; BORDER-LEFT: #79a5e4 1px solid; PADDING-BOTTOM: 10px; BACKGROUND-COLOR: #dbe8fb; PADDING-LEFT: 10px; PADDING-RIGHT: 10px; BORDER-TOP: #79a5e4 1px solid; BORDER-RIGHT: #79a5e4 1px solid; PADDING-TOP: 10px">  
<?xml version=”1.0″ encoding=”UTF-8″ standalone=”no”?>  
 <xs:schema xmlns:xs=”[http://www.w3.org/2001/XMLSchema](http://www.w3.org/2001/XMLSchema)” targetNamespace=”urn:hl7-org:v3″  
     elementFormDefault=”qualified” xmlns=”urn:hl7-org:v3″ xmlns:voc=”urn:hl7-org:v3:voc”  
     xmlns:hl7=”urn:hl7-org:v3″ xmlns:msg=”urn:hl7-org:v3:mif” xmlns:fo=”[http://www.w3.org/1999/XSL/Format](http://www.w3.org/1999/XSL/Format)“>  
  <font color="#e31600">   <xs:include schemaLocation=”./dd\datatypes.xsd”/>  
     <xs:include schemaLocation=”./sd\voc.xsd”/>  
</font>   

</div>  
 

  
<font color="#840000">위의 XML에서 보면, include schemaLocation 이라고 되어 있는 부분이 있을 것이다. </font><font color="#840000">즉, 현재의 스키마는 datatytes.xsd 와 voc.xsd라는 두개의 다른 스키마를 참조하고 있다는 것이다. </font><font color="#840000">그래서 실제로 저 경로에 두 개의 파일이 존재하지 않으면, 위와 같은 예외가 발생한다는 것이다. </font><font color="#840000">비주얼스튜디오에서는 XML 문서자체의 규칙위반은 없기 때문에, </font><font color="#840000">컴파일시 아무 문제가 없지만, 제대로 스키마를 잡아 주지 않으면 큰 문제가 생길수가 있다.</font>

  
 

  
 

  
 

  
 



