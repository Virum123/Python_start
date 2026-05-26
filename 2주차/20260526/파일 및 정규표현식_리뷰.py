# with open("파일명을 포함한 경로", "접근모드") as fi:
#     fi.read() # 모든 텍스트 내용을 읽어서 하나의 문자열 객체로 생성
#     fi.write()  # 텍스트 파일 현재 메모리 내용을 쓰는 함수
#     fi.readline()
#     fi.readlines() # 텍스트 파일 각 라인별 내용을 리스트에 항목으로 반환
#
#
# '접근모드' ==> 'r', 'w', 'a', 'r+'

# 문자열 객체의 내용을 특정 패턴을 활용해서 찾고(검색), 치환(수정), 분할 시키는
# 역할의 문법 ==> 정규 표현식
# 패턴 ==> r'[a-z]+' , r'[A-Z]+', r'[0-9]+', r'[가-힣]+'
import re

strdata = 'AI 프로그래밍 1998 python Preprocessing!!'
print(re.findall(r'[가-힣]+', strdata))
print(re.findall(r'[0-9]+', strdata))
print(re.findall(r'[A-Z]+', strdata))
print(re.findall(r'[a-z]+', strdata))
print(re.findall(r'[a-zA-Z]+', strdata))