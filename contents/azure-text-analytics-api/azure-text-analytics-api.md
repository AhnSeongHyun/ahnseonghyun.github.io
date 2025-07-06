---
title: 'Azure Text Analytics 연동하기'
author: 'ash84'
pub_date: '2017-07-05'
description: '[지난 글](https://ash84.net/2017/07/02/using-chatfuel-make-chatbot/)에서 chatfuel을 이용해서 챗봇을 간단하게 만들어봤는데 MS Azure 에서 제공하는 Text Analytics API 를 연동해서 감정분석까지는 아니고 단순하게 텍스트에 대한 긍정부정을 알려주는 챗봇을 구성해 보기로 했다. 

https://azure.microsoft.com/en-us/services/cognitive-services/text-analytics/

총 4가지 API를 제공하는데 **Detect'
featured_image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTCoP89IrLxbeI_UcIeXK8kYFXf0aWLOmDs-_MWt2qn8JpnY9nsg'
tags: ['dev', 'azure', 'text-analytics', 'ML', 'chatbot']
---

[지난 글](https://ash84.net/2017/07/02/using-chatfuel-make-chatbot/)에서 chatfuel을 이용해서 챗봇을 간단하게 만들어봤는데 MS Azure 에서 제공하는 Text Analytics API 를 연동해서 감정분석까지는 아니고 단순하게 텍스트에 대한 긍정부정을 알려주는 챗봇을 구성해 보기로 했다. 

https://azure.microsoft.com/en-us/services/cognitive-services/text-analytics/

총 4가지 API를 제공하는데 **DetectLanguage** 랑 **Sentiment** API 를 이용하기로 했다. Detect Language 는 입력된 텍스트에 대한 언어를 감지해서 결과를 돌려준다. 2가지 항목을 주는데 하나는 일반 언어에 대한 이름 `name` 이고 또 하나는 언어코드 `iso6391Name` 를 주고 있다. Sentiment 는 언어코드
 `iso6391Name` 와 함께 텍스트를 주면 `score` 값으로 0~1사이로 부정 혹은 긍정의 정도를 판별해서 돌려준다. 아쉬운 부분은 아직은 한국어나 일본어는 지원하지 않는다. 

자세한 부분은 API 사이트에서 [테스트](https://westus.dev.cognitive.microsoft.com/docs/services/TextAnalytics.V2.0/operations/56f30ceeeda5650db055a3c7) 를 할 수 있다. 

그래서 일단 사용자가 메시지를 입력하면 API 에서 해당 데이터를 받아서 DetectLanguage 를 호출해서 메시지에 대한 언어감지를 하고, Sentiment 가 가능한 API의 경우 Sentiment 를 호출하고 아닐 경우 가능한 언어를 보여주도록 만들었다. Sentiment 의 `score` 결과에 따라서 5개의 등급으로 분류를 하고 각각 다르게 메시지를 보내주도록 하였다. 위의 API들을 사용하려면 API 사용 신청을 해야하고 그에 따른 키를 발급해 준다. 해당 키는 `Ocp-Apim-Subscription-Key` 라는 항목으로 HTTP REQUEST Header 에 추가해준면 된다. 

![챗봇-chatbot](https://farm5.staticflickr.com/4213/35566479142_5b343cc15d_z.jpg)
한국어는 아직 만들지 못했는데, konlp 나 다른 자료들을 찾아 보면서 만들어야 할것 같다. 오픈한글 사이트에서 감정분석 API를 제공했던것 같은데 지금은 동작하지 않는것 같다. 

 github : https://github.com/AhnSeongHyun/chatbot-emotion


```python 

@app.route('/chat', methods=['POST'])
def get_text():
    try:
        user_msg = request.form.get('user_msg', None)
        message = Message()
        print(user_msg)
        if user_msg:

            lang_detect = LanguageDetection(**conf)
            request_id = datetime.now().strftime('%Y%m%d%H%M%S')
            lang_detect_result = lang_detect.detect_language(id=request_id, text=user_msg)
            message.append({'text': "%s 로 말씀하셨습니다. " % lang_detect_result.name})

            if lang_detect_result.lang_code in conf['approval_lang_code']:
                sentiment = Sentiment(**conf)
                sentiment_score = sentiment.detect_sentiment(id=request_id,
                                                             text=user_msg,
                                                             language=lang_detect_result.lang_code)
                message.append({'text': sentiment_score.get_sentiment_text()})
            else:
                message.append({'text': '해당언어로는 제가 기분을 알 수 없습니다.'})
                message.append({'text': '%s 언어로 이야기 해주세요.' % (conf['approval_lang_code'].values())})
        return jsonify(message.to_dict()), 200
    except Exception:
        import traceback
        print(traceback.format_exc())
        d = {
            "messages": [
                {"text": "알아들을수가 없습니다. 다른애기를 해주세요."}
            ]
        }
        return jsonify(d), 200
```


```python 

class SentimentScore(object):
    def __init__(self, score):
        self.score = score

    def get_sentiment_text(self):
        if 0.0 <= self.score <= 0.2:
            return "기분이 나쁘시군요."
        elif 0.2 <= self.score <= 0.4:
            return "기분이 별로시네요."
        elif 0.4 <= self.score <= 0.6:
            return "기분이 그저 그렇군요"
        elif 0.6 <= self.score <= 0.8:
            return "기분이 좋아보이네요 "
        else:
            return "기분이 매우 좋아보이네요"
```




