---
title: '테스트와 체크 리스트'
author: 'ash84'
pub_date: '2015-10-03'
description: ''
featured_image: ''
tags: ['dev', '변인통제', '자동화도구', '체크리스트', '테스트', '통제변인']
---


<div style="line-height: 2; text-align: left;"><span style="font-size: 10pt;"><span style="font-family: Dotum; font-size: 11pt;">새로 들어간 회사에서 주로 하는 일은 모듈을 분석하고 개선하는 일을 맡고 있는데, 특히 우리 팀의 가장 큰 업무중의 하나는 바로 JIRA라는 시스템을 통해서 질의해오는 기술적인 문제들에 대해서 답을 해 주는 것이다. 매우 어려운 기술적인 문제도 있지만, 사실은 설정 하나만을 잘 모르거나 잘못사용해서 발생하는 문제들도 있는 것이 사실이다. </span></span></div><span style="font-size: 11pt;">  
</span><span style="font-family: Dotum; font-size: 11pt; line-height: 26px;">이러한 문제들을 처리하면서 느낀것이 2가지가 있다. 사실 이제 고작 몇개를 처리했을까.. 하는 신입아닌 신입인 내가 이런 글을 쓴다는 것이 웃기긴 하지만, 말이다.</span><span style="font-size: 11pt;">  
</span>

<div style="text-align: left;"></div><div style="line-height: 2; text-align: left;"><span style="font-size: 11pt;">  
</span><span style="font-size: 10pt;"><span style="font-family: Dotum;">**<span style="font-size: 11pt;">1. 통제변인의 중요성</span>**</span></span></div><div style="line-height: 2; text-align: left;"></div><div style="line-height: 2; text-align: left;"><span style="font-size: 10pt;"><span style="font-family: Dotum;"><span style="font-size: 11pt;">처음 기술적인 문제를 접했을때의 상황에 대한 느낌은 그냥 멍~하다는 것이다. 이것을 어떻게 처리해야할까.. 라는 생각이 들었고, 내가 맡고있는 범위의 문제인가를 체크해 보는것은 몇개를 훑어보고 나서였던것 같다. 그리고 나서 알게된 것은, </span><span style="color: #112a75;"><span style="font-size: 11pt;">고객환경에서 발생하는 오류를 처리하기 위한 가장 완벽한 과정의 첫번째 발걸음은 바로, </span>**<span style="font-size: 11pt;">오류를 재현하는것이다. </span>**</span></span></span></div><span style="font-size: 11pt;">어떻게 보면, 그 오류에 대해서 내가 알거나 혹은 내가 아닌 동료들이 아는 오류라면 더 쉽게 처리 할수 있겠지만, 그렇지 않은 오류라면 반드시 </span>**<span style="font-size: 11pt;">‘오류 재현’</span>**<span style="font-size: 11pt;"> 이라는 과정을 거쳐야 한다. 오류재현은 기본적으로 환경세팅부터 시작한다. 즉, 고객사의 환경. 서버의 종류 윈도우 서버인지, 리눅스인지, AIX 인지 등등.. 그리고 32비트인지, 64비트인지 등등도 체크해 봐야 할것이다. 그리고 본 회사의 어떤 버전의 제품이 설치되어 있는지, 패치는 어떤 리비전으로 되어 있는지, 해당 모듈의 버전과 리비전은 무엇인지 말이다. </span>

<span style="font-size: 11pt;"> </span>

<div style="line-height: 2; text-align: left;"><span style="font-size: 10pt;"><span style="font-family: Dotum;"><span style="font-size: 11pt;">사실 이 과정이 필자가 말하고자하는 </span>**<span style="font-size: 11pt;">통제변인의 설정과정</span>**<span style="font-size: 11pt;">이다. 즉, 오류를 재현하기 위해서 어떤 변수를 같게 만들어 주는 과정이라고 볼수 있다. 되도록 나는 실제데이터를 통해서 오류를 재현하고자 한다. 왜냐하면 실 데이터 만이 가장 완벽한 통제변인을 구현하는 것이고, 그것이야 말고 가장 빠르게 오류를 재현하고, 오류의 원인을 찾아내는 방법이라고 생각한다. </span></span></span></div><span style="font-size: 11pt;"> </span>

<div style="line-height: 2; text-align: left;"><span style="font-size: 10pt;"><span style="font-family: Dotum; font-size: 11pt;">때때로 실 데이터를 사용할 수 없을때 라면, 비슷한 형식으로 만들어서 사용하는 경우가 있는데 이 경우에도 역시 실 데이터의 형식이나 패턴을 잘 고려해야 한다. 한 예로 실 데이터에는 한글과 영어가 뒤 섞여 있는데, 실험데이터를 한글만으로 구성한다면? 영문자 소문자 대문자가 있는데 실 데이터를 소문자만으로 구성하는 등의 구성은 오류를 찾는데 더 많은 시간을 필요로 할 뿐이다. </span></span></div><div style="line-height: 2; text-align: left;"></div><div style="line-height: 2; text-align: left;"><span style="font-size: 10pt;"><span style="font-family: Dotum;"><span style="font-size: 11pt;">오류를 재현해냈다면, 그 다음으로 우리가 할일은 바로 테스트 셋을 정하는 일이다. 사실 이 과정에서 강력한 통제변인이 필요하다. 어떤 변수들은 일정하게 유지를 시키고 테스트를 하겠다는 것을 잘 생각해야 한다. 때때로 통제 변인이 아니였던 변수들을 통제변인으로 만들어야 하는 경우도 생긴다. 예를들어, 오류에 대한 원인을 추정하는 과정에서 우리는 몇가지를 추측할 수가 있다. OS 의 문제인지, 특정 컴파일러의 문제인지.. 그런 과정에서 하나를 통제시키고 다른 하나를 변화시키면서 테스트를 해나간다. 그런데 하나의 변수에서 원인을 발견하지 못한다면, 당연히 해당 변수는 새로운 통제변인으로 지정해야하고, 사실 여러가지 변수들을 변경해 내 가면서 우리는 자연스럽게 통제변인들을 추가하고 때론 막히게 되면 새로운 변수를 추가하거나 혹시나 하는 마음에서 통제변인이었던 변수를 해제 시키기도 한다. </span>  
<span style="font-size: 11pt;">  
</span></span></span></div><div style="line-height: 2; text-align: left;"><span style="font-size: 10pt;"><span style="font-family: Dotum;">**<span style="font-size: 11pt;">2. 체크리스트의 활용</span>**</span></span></div><div style="line-height: 2; text-align: left;"><span style="font-size: 11pt;">  
</span><span style="font-size: 10pt;"><span style="font-family: Dotum; font-size: 11pt;">사실 계속되는 테스트 속에서 내가 왜 이것을 하고 있는가 ? 하는 의문에 빠지거나 하는 경우가 있다. 워낙 많은 변수들이 존재하고 통제해야할 것들 그리고 의심이 가는것들과 우리가 가정한 것들이 정답이나 오류의 원인이 아닌 경우에는 더 혼란에 빠지기 쉽다. 이런것들을 방지하기 위해서는 반드시 체크리스트라는게 필요하다고 생각한다.</span></span></div><div style="line-height: 2; text-align: left;"> 사실 체크리스트의 활용은 예전**[<span style="font-size: 11pt;">보잉의 사례</span>](http://cronose88.blog.me/30092879952 "[http://cronose88.blog.me/30092879952]로 이동합니다.")**에서도 알다시피 사람이 기억해야 하는 것들에 대해서 미리 점검해 주는 역할을 하고 있으며, 21세기에도 여전히 그 활용도가 높다. 테스트에 대한 테스트 셋을 설정하는 단계에서 계획을 잘 세우는 것도 중요하지만, 테스트를 하는 과정에서도 체크리스트를 활용하면서, 테스트를 실행하는 것이 중요하다. 이 테스트를 어디까지 진행했는지, 그리고 어떤 변수를 변화시켜 보았고, 어떤 변인들이 통제되고 있는지 수시로 체크를 해 가면서 테스트를 하는것이 무엇보다도 중요하다고 생각한다. 때론 이러한 과정들이 직관적으로 해결하는 것 보다는 오류에 대한 수정이 늦을수가 있다. 하지만, 우리는 오류에 대한 파악을 늘 100% 장담할 수가 없다. 물론 많은 경험이 쌓이게 되면 가능하겠지만 말이다. 직관적인 해결이 더 빠를지는 모르겠지만, 차우에 더 크고 변수가 다양한 문제에 대해서 해결하고자 한다면 체크 리스트에 활용은 필수적이라고 여겨진다.</div><span style="font-size: 11pt;">사실 이러한 업무를 진행하면서 느낀것은 실제 개발하고 있는 프로그램이나 모듈에 대해서도 테스트 셋을 설정하고, 체크리스트를 활용해서 테스트를 개발 단계의 끝에서 제대로 해야하지 않는가 하는 점이다. 품질관리라는 측면이라고 볼수도 있겠지만, 좀더 논리적이고 체계적인 테스트가 된다면, 개발자도 추후에 사용자도 더 편하고 유지보수 하기에도 더 좋지 않을까 하는 생각을 주로 하게 되었다. </span>

물론 이러한 것을 위한 자동화도구가 있다면 더 좋을것이다. 자동화 도구뿐만 아니라, 측정 및 저장도구 까지 있다면, 개발단계에서 테스트 한 것이 대해서 추후에 유지보수 단계에서 더 참고를 해서 유지보수를 진행할수 있을것이라는 생각이 들었다.



