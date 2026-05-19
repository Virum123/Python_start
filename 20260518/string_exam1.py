# 문자열 객체 ==> 시퀀스 타입
# 시퀀스 타입 ==> 데이터의 순서가 있는 타입
# 문자열 객체 ==> str()
# 특정 위치를 인덱스로 접근할 수 있음 ==> index는 항상 0부터 출발

str1 = "python test"
print(str1[5]) # [idx] : 인덱싱 문법
print(str1[-3]) # -1 : 마지막 항목의 인덱스
#슬라이싱 문법 ( 잘라내기 문법)
print( str1[7:11]) # [start : stop-1] 까지 잘라내기
print(str1[0:6])
print(str1[:10]) # 시작을 비워두면 처음부터
print(str1[12:]) # 끝을 비워두면 끝까지에서 하나 덜

# 문자열 객체에 지원되는 연산 ( +, *)
str2 = "study"
print( str1 + " " +str2)

# 문자열 곱셈 연산
print('='*25)

strdata = 'AI Programming'
for item in strdata:
    print(item, end=' ')
print() # 개행역할 줄바꿈이라고 안하는 이유는 뭘까?

strdata3 = 'AI core'
# strdata3[0] = 'D' # 문자 항목은 객체의 항목을 수정할 수 없다(불변 객체)
# strdata3 = 'DI core'
strdata4 = strdata3.replace('A', 'D')
print(strdata3, strdata4) # DI core
print(len(strdata3), len(strdata4))

print('py' in 'python') # 존재 여부 질문, not in 하면 반대의 경우 물어봄

if 'py' in "python":
    print("있음")
else:
    print("없음")