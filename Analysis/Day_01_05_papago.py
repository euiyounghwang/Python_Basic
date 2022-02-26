
import json

# settings install packages
import requests

def papago(text, kor2Eng):
    url = 'http://labspace.naver.com/api/n2mt/translate'
    # recvd = requests.get(url)

    # payload = {
    # 'source':'ko',
    # 'target':'en',
    # 'text': text}

    payload = dict(source='ko',target='en',text=text)

    if kor2Eng == False:
        payload['source'] = 'en'
        payload['target'] = 'ko'


    # Accept:*/*
    # Accept-Encoding:gzip, deflate
    # Accept-Language:ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4
    # Connection:keep-alive
    # Content-Length:296
    # content-type:application/x-www-form-urlencoded; charset=UTF-8
    # Cookie:npic=TbyvBJMzhdd3gs1/QVMe0+upMHYQaJYmoqRbNYXM1QVrRDF1l85VXT9cuQPSVBlyCA==; NNB=PYAF2OSJ7WVFQ; wcs_bt=dccae51cc9ffb4:1494471644
    # Host:labspace.naver.com
    # Origin:http://labspace.naver.com
    # Referer:http://labspace.naver.com/nmt/
    Header ={'x-naver-client-id':'labspace'}

    recvd = requests.post(url, data=payload, headers=Header)
    # print(recvd)
    # print(recvd.headers)
    print(recvd.text)

    print('-'*150)
    urlTxt = json.loads(recvd.text)
    print(urlTxt['message']['result']['translatedText'])

    # for item in urlTxt['message']['result']:
    #     # urlTxt = json.loads(text)
    #     # if item['translatedText']:
    #         print(item)
    #     # print(i)


print(papago('제가 파이썬으로 json파일 전체를 읽는 코드를 짰는데 돌아가질 않아요', True))
print(papago('how do you like your coffee?', False))

