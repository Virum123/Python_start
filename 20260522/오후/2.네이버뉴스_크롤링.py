import requests
from bs4 import BeautifulSoup
import re


url = 'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=%EB%B0%98%EB%8F%84%EC%B2%B4'
r = requests.get(url)  # 웹페이지 요청
html = r.content  # r.content Or r.text : 웹페이지 형태 content = 웾페이지 전체를 다 가져온 것, 그 중 원하는 것만 꺼내는 것을 "파싱"
# print(html)

headers = {
    'User-Agent': 'Mozilla/5.0'
}


r = requests.get(url, headers = headers)
html = r.content
# print(html) html관련 내용 확인하고 넘어가기
soup = BeautifulSoup(html, 'lxml')  # 파서 지정
newtitlelist = soup.find_all(class_ = 'sds-comps-text sds-comps-text-ellipsis sds-comps-text-ellipsis-1 sds-comps-text-type-headline1')
print(newtitlelist[0].text) # .text나 .join이나 split() 뭐 이런거 어떻게 구분하는지가 어렵다
newdatalist = [ item.text for item in newtitlelist]
print(newdatalist)

import pandas as pd
newsdf = pd.DataFrame(newdatalist, columns=["뉴스 제목"])
print(newsdf)

newsdf.to_excel('navernewsdata.xlsx', index = False) # 엑셀파일 저장
