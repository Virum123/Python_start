# 파일 입출력 ==> with as 구문
with open ("pythondata.txt", "r+") as fi:
    # 파일 접근 코드만 동작
    str = fi.readlines() # 전체 문자열 읽기

# with ~ as 구문을 벗어나는 순간 자동 close()
print(str)
#
strlist = [ a.strip() for a in str ] # 리스트 내포를 이용해서 깨끗하게 만들기
print(strlist) # 아 \n 같은게 개행제거로 없어지는구나