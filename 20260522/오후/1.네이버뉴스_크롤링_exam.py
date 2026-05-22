import requests # 특정 URL에 웹페이지(HTML) 정보를 요청하는 패키지
from bs4 import BeautifulSoup # 웹페이지 정보를 파이썬 객체화해서 파싱할 수 있게 지원해주는 패키지
# bs4 패키지 안에 BeautifulSoup 클래스만 가져와
import re # 정규표현식


url = 'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=%EB%B0%98%EB%8F%84%EC%B2%B4' # 웹페이지 요청할 URL 정보
#
r = requests.get(url)  # 웹페이지 요청
html = r.content  # r.content Or r.text : 웹페이지 형태 content = 웾페이지 전체를 다 가져온 것, 그 중 원하는 것만 꺼내는 것을 "파싱"
# print(html)
#
soup = BeautifulSoup(html, 'lxml')  # 파서 지정
#
# # 위 방법과 다른 find_all(), find() 메서드 활용
newtitlesoup = soup.find_all(class_ = 'sds-comps-text sds-comps-text-ellipsis sds-comps-text-ellipsis-1 sds-comps-text-type-headline1') #리스트로 반환함

title_list = [x.get_text(strip=True) for x in newtitlesoup]

print(title_list) #.text 해당 태그 정보에서 텍스트 속성만 반환해줘

