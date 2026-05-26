import requests
from PIL.DdsImagePlugin import item
from bs4 import BeautifulSoup
import re


url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube'

headers = {
    'User-Agent': 'Mozilla/5.0'
}


r = requests.get(url, headers = headers)
html = r.content

soup = BeautifulSoup(html, 'lxml')
# 제목 정보를 리스트에 취합, 취합하면서 앞뒤 공백 모두 제거 상태로 취합
# for item in newtitlesoup:
#      print(item.find_all('a')[0].text) #.text 해당 태그 정보에서 텍스트 속성만 반환해줘
newtitlesoup = soup.find_all('td', class_ = "subject")
youtubetitlelist = [ item.find_all('a')[0].text.strip() for item in newtitlesoup ]
print(youtubetitlelist)
# 리스트 내포와 정규 표현식을 이용해서 위 youtubetitlelist 항목을 한줄로
# 영문 대소문자만 남기도록 수정
# alpha = [ re.sub(r'[^a-zA-Z\s]+','',item )for item in youtubetitlelist if len(item)>2 ]
# print(alpha)
#stringdata = '\n'.join(youtubetitlelist)
#print(stringdata)

# [A-z]랑 [A-Za-z] 차이를 알아두자
import re

# 정규 표현식을 활용해서 전체 문자열 중에 영문 대소문자만 남기고 삭제
print("="*80)
#result = re.findall(r'[a-zA-Z\s]+', stringdata)
# result = re.sub(r'[^a-zA-Z\s]+','',stringdata)
# print(result)


import pandas as pd

mydf = pd.DataFrame(youtubetitlelist)
print(mydf)
mydf.to_excel("youtubedata.xlsx", index = False)