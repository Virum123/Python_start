
# 텍스트 파일 (.txt)은 파일 입출력 코드로 접근하는게 편함
# 파일 개방함수 open() 접근할 파일의 경로 + 파일명, 접근 모드를 설정
# 접근모드 ==> 'r' (읽기), 'w' (쓰기), 'a'(추가), 'r+': 읽기/쓰기 가능모드
# 파일 해제함수 close()
# with ~ as ## with의 기능이 뭘까? / with~as 구문 블럭을 버어나면 자동 close 됨
with open(file = "C:/python_project/python_basic/20260521/pythondata.txt", mode = "r+") as fi:
   # str = fi.read()
   # str1 = fi.readline()
    str2 = fi.readlines()
print(str2)
# print(str2)
# print(str1) # 같이 넣으면 왜 빈 리스트가 나오지?
listdata = [ x.strip() for x in str2]
print(listdata)

import pandas as pd
mydf = pd.DataFrame(listdata)
print(mydf)
mydf.to_excel("pythondata.xlsx", index = False)
mydf.to_csv
# 함수라서 위치를 맞춰서 써줘야하지만, mode = 'r', file = '경로' 같이 인수를 직접 지정해주면 오류가 나지 않음
# 인수가 존재하더라도 file = , mode = 하고 써주는게 좋음
# import os
# print(os.getcwd())
# print(os.listdir("C:/python_project/python_basic/20260521/"))