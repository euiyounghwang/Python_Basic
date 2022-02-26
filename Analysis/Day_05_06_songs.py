# Day_05_06_songs.py
import requests
import re

# SYSID:PATHFINDER
# MENUID:1000005022001
# EVENTID:srch_01_popup_mem
# S_MB_CD:
# S_MB_CD_POPUP:1
# S_HANMB_NM:1
# hanmb_nm:
# form_val:
# form_val2:
# input_idx:
# input_name:S_RIGHTPRES_CD
# input_name2:S_RIGHTPRES_NM
# pub_val:0
# search_code:1
# search_keyword:1

def showSongs(code, page):
    # S_PAGENUMBER:4
    # S_MB_CD:W0726200
    # S_HNAB_GBN:I
    # hanmb_nm:권지용

    # payload = dict(S_MB_CD='W0726200', S_PAGENUMBER=1)
    payload = dict(S_MB_CD=code, S_PAGENUMBER=page)

    url = 'https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'
    recvd = requests.post(url, data=payload)
    # print(recvd)
    # print(recvd.text)

    tbody = re.findall(r'<tbody>(.+?)</tbody>',
                       recvd.text, re.DOTALL)
    print(tbody[0])

    tbody = re.sub(r' <img .+? />', '', tbody[0])
    tbody = re.sub(r'<br/>', ',', tbody)

    trs = re.findall(r'<tr>(.+?)</tr>',
                     tbody, re.DOTALL)
    # print(len(trs))

    if not trs:
        return False

    for tr in trs:
        # print(tr)
        tds = re.findall(r'<td>(.*?)</td>', tr)     # empty tag <td></td> 때문에 * 사용
        tds = [i.strip() for i in tds]
        print(tds)
        # print(len(tds))

    return True

# page = 1
# while showSongs('W0726200', page):
#     print('---------{}---------'.format(page))
#     page += 1

page = 1
while showSongs('W0726200', page):
    page += 1







