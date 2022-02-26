
import json

# settings install packages
import requests

url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
recvd = requests.get(url)
print(recvd)
print(recvd.headers)
# print(recvd.text)

# 한글 깨지는 현상 제거
text = bytes(recvd.text, 'iso-8859-1').decode('utf-8')
print(text)

print('-'*50)

# result = list(text)
# print(type(result))

urlTxt = json.loads(text)

for item in urlTxt:
    # urlTxt = json.loads(text)
    print(item['code'], item['value'])
    # print(i)


# print(urlTxt)
# print(urlTxt['code'])