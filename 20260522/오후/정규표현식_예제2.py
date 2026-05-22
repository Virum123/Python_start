
import re # regluar expression , 정규표현식

strdata = "파이썬, Ai PyThon3#Programming97@성장 빅테크"

# 패턴을 이용해서 특정 문자를 검색 ==> findall()
# 패턴을 이용해 특정 문자열을 분할 ==> split()
# 문자열 메서드로 여러개의 구분자를 활용해 분할하기에는 문제가 있다
# 이를 해결하기 위해 패턴을 이용해 문자열을 분할해서 사용
# strdata.split(0) 애는 뭐를 분할할지 알려주는데
result = re.split(r'[,\s#@]', strdata) # 애는 앞에 따로 안적으니까 뒤쪽에 적어줘야함
print(result)
# \s 가 뭐지 '모든' 공백을 의미한대 아래의 것 전부
# 공백(space)
# 탭(\t)
# 줄바꿈(\n)
# 캐리지 리턴(\r)
# 폼 피드(\f)
# 수직 탭(\v)
result = re.sub(r'[,#@\s]', ' ', strdata) # 문자열 replace('k', ' ') 동작과 유사
print(result)
# 정규 표현식은 패턴을 활용해서 치환, 발견 시작은 r'[]' 이때 대괄호는 괄호 속 내용을 따로따로 묶어놨다는 의미
#print(strdata.replace("#"," "))

with open("redata.txt", "w", encoding="utf-8") as fi:
    fi.write(result)