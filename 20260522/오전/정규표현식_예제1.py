import re # regluar expression, 정규표현식

strdata = ('파이썬 Ai PYThon 8256 ProgramminG 2026A+ B- C+ ALL In ONe 빅테크222  에이아이 ㅋ2 ㅋ 3 ㅎㅎ4 5 ㅋㅎㅋㅋ힠힝너 ㅣㅣ ㅓㄹㅇ닝ㄹ'
           ' !!')

result = re.findall(r'[^a-zA-Z0-9ㄱ-힣 ]+' , strdata)
print(result)  # 빈 리스트 [] ==> False

# main은 [a-z] [가-힣] [0-9]
# 문자열 메서드가 아닌 특정 패턴을 활용해서 특정문자열을 찾고(검색), 분할하고,
# 치환(삭제)할 수 있는 정규표현식 메서드 지원

# 검색 ==> findall() ==> 패턴에 매칭된 모든 내용을 리스트 형태로 반환

#영문 대문자 패턴 ==> A,B,C...Z ==> 범위를 활용 A-Z
# []는 여러개 패턴을 하나로 묶어서 표현할 때 사용하는 메타문자
# + ===> + 기호 앞에 있는 패턴이 하나 이상인 문자를 찾아서 반환해라 ==> 메타문자
# # 영문대문자 패턴
# result = re.findall(r'[A-Z]' , strdata)
# print(result)  # 빈 리스트 [] ==> False
# # 영문소문자 패턴
# result = re.findall(r'[a-z]' , strdata)
# print(result)  # 빈 리스트 [] ==> False
#
# # 영대소문자 패턴
# result = re.findall(r'[a-zA-Z]' , strdata) # [a-zA-Z] ,넣으면 인식한다 ', ' 하면 ,랑 공백을 전부 인식함
# print(result)  # 빈 리스트 [] ==> False
#
# # ㄱ-힣 : 조합형 범위
# # 가-힣 : 완성형 범위
# result = re.findall(r'[ㅏ-힣]+' , strdata) # '히' 가 아니라 '힣' 이 끝이다 'ㄱ'으로 시작하면 자음도 따로 출력 가능함
# print(result)  # 빈 리스트 [] ==> False

# 숫자 문자가 하나 이상인 것을 모두 찾아서 출력
result = re.findall(r'[0-9]+' , strdata)
print(result)  # 빈 리스트 [] ==> False

if result :
    print("값이 있다요")
    print(result)  # 빈 리스트 [] ==> False
else:
    print("값이 없다요")
# 이걸  if는 pass, else에서 print하게하면 4줄이라 코드가 복잡함
# 논리 부정(반대) ==> not
# 논리 and ==> and
# 논리 or ==> or

# \w ==> 임의의 문자
# * ==> * 메타문자 기준으로 앞에 패턴이 0개 이상인거를 매칭
# + 는 1개 이상, * 는 0개 이상
strdata = "Ai반 Ai Ai구축 Ai프로그램 Ai" # 메타문자가 뭐지
result = re.findall(r'Ai\w*', strdata) #Ai가 포함된 모든 단어를 뽑고싶을때 사용
print(result)