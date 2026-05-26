# 튜플 : 시퀀스 데이터 타입
data1 = (50, 30, "python", [5, 6]) # == tuple() 여기에 숫자나 문자열 등 하나의 데이터를 넣으면 타입이 바뀜,  뒤에 ,를 넣어줄것
print(data1, type(data1))

# 2+ 6 * 7 / 9 + 8 같이 연산자가 여러개면 ()로 순서를 정해줄 것

# 튜플도 리스트처럼 어떤 객체든 항목으로 넣을 수 있음
# data1[1] = 80 !!!! 오류남
# 문자열 객체처럼 항목을 수정할 수 없다
print(data1[0], data1[1], data1[2], data1[3])
data2 = 50, 60, 70, 80 # 튜플의 pack 기능 동작
print(data2, type(data2))

a, b, c = (5, 3, 2) # 튜플의 unpack 기능

print(a, b, c)
print (a)