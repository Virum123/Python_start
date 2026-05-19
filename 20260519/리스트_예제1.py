
# 리스트 ==> 시퀀스 타입 객체 ( 색인연산, 슬라이싱연산, +, * )
# = ( 대입연산 ) ==> 왼쪽에 내용을 오른쪽으로 복사 대입하는 역할
# == ( 비교(관계)연산 ) ==> 같은가에 대한 문제 ==, !=, > , <
# ==> 비교 연산의 결과물은 T/F
data1 = list() # 리스트타입 객체 생성

data1 = [None, None, None] # 리스트는 문자열과 달리 항목을 Read/Write 가능한 객체
print(data1, type(data1))
data1[0] = 50 # 에러는 여기서 발생
print(data1) # [ 50 ] 리스트 자리에 [0]이 없음, 그러니 교체가 안되는것

data2 = list()
data2.append(5) # 리스트에 추가하는 메서드(함수)  append, extend, insert
print(data2)
data2.extend(['광', '!', 90, 'Hey'])
print(data2)
data2.insert(2, '란')
print(data2)

data3 = list([60, 'python', 5.8, ['programming', [90,  'nvi']]])
print(data3)
# 문제
print(data3[3][1][1][1]) # 'v' 문자 하나만 출력
# 색인 연산을 여러번 사용해서 하나만 출력이 가능함
# 정수는 안되네, 순서가 없어서 그런가
print('=' * 50)

data3.extend([50,90,70])
print(data3)
print('=' * 50)

data3.insert(2,30)
print(data3)

# 항목 삭제
print(len(data3))# len() : 항목의 길이 계산 (개수)
print(data3)
del data3[1]
print(data3)