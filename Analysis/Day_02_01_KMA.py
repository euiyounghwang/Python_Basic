import json

# settings install packages
import requests
import re

f = open('Data/kms.txt', 'w', encoding='utf-8')

url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
recvd = requests.get(url)
# print(recvd)
# print(recvd.headers)
# print(recvd.text)

print('-'*50)

temp = re.findall(r'<province>.+</province>', recvd.text)
print(temp)

# <location wl_ver="3">
# .+ 탐욕적, greedy
# .+? : 비탐욕적, non-greedy
location = re.findall(r'<location wl_ver="3">.+?</location>', recvd.text, re.DOTALL)
print(location)

# # List 형태
for loc in location:
    # print(loc)

    prov = re.findall(r'<province>(.+)</province>', loc)
    city = re.findall(r'<city>(.+)</city>', loc)
    # print(prov, city)

    data = re.findall(r'<data>(.+?)</data>',  loc, re.DOTALL)
    # print(data)

    print('\n')
    i=0
    for datum in data:
        # print(datum)
        # print(datum[0])
        # mode = re.findall(r'<mode>(.+?)</mode>', datum, re.DOTALL)
        # tmEf = re.findall(r'<tmEf>(.+?)</tmEf>', datum, re.DOTALL)
        # wf = re.findall(r'<wf>(.+?)</wf>', datum, re.DOTALL)
        # tmn = re.findall(r'<tmn>(.+?)</tmn>', datum, re.DOTALL)
        # tmx = re.findall(r'<tmx>(.+?)</tmx>', datum, re.DOTALL)
        # reliability = re.findall(r'<reliability>(.+?)</reliability>', datum, re.DOTALL)
        # print(i,prov, city, mode, tmEf,wf,tmn,tmx,reliability)
        # i +=1
        items = re.findall(r'<.+?>(.+?)</.+?>', datum)
        # print(items)
        # print('{}, {}, {}, {}, {}'.format(items[0], items[1], items[2], items[3], items[4]))
        print('{}, {}, {}, {}, {}, {}, {}'.format(prov[0], city[0], *items))

        f.write('{}, {}, {}, {}, {}, {}, {}'.format(prov[0], city[0], *items))
        f.write('\n')

f.close()