
# 시퀀스 타입 ==> 문자열, 리스트, 튜플

listdata = [[5, 6], "python", 5, 9] # == list() 이 명령과 동일
# 리스트만 만들면 메모리에 자리만 차지, 이 자리를 가리켜주는 변수를 생성
print( listdata[1] ) # read 색인 연산
listdata[1] = "Ai" # write

## 지피티에서 봤던 리스트와 배열의 차이, 메모리공간 바로 옆에 우다다 넣는게 아니라 메모리 어딘가에 있는 id를 할당하는 것
## 배열은 실제로 옆에다 값을 넣어둠, 리스트는 id를 넣어둠

topledata = (50) # 얘는 정수 데이터를 생각한다.
tupledata = (5, 6)  # 튜플로 사용하고 싶다면 뒤에 ,를 넣어주거나 값을 더 적어줄것
# 읽기 전용으로 사용한다고 생각

import numpy as np

arr1 = np.array( [ [ [3,4,5,6,7], [7,8,9,2,1] ] ] ) # 중간에 4-5, 9-2 이렇게 꺼내려면 슬라이싱 사용
print(arr1)
print(arr1.ndim) # 차원수
print(arr1.shape)  # 형태 ==> tuple 형태로 반환

print( np.arange(1,11) )

arr2 = np.arange(1,10).reshape(3,3)
print(arr2)
print(arr2.shape)

d1, d2 = (3, 5) # 튜플의 언팩기능

a = 5
b = 7
print('a : ', a)
print('b : ', b)

a, b = b, a  # 다른 언어는  temp 같은거 써서 돌려줘야함 Java에서 봤던거랑 동일하다고 생각하면 됨


dictdata = { 'A': 50, 'B': 90} # == dict() , 매핑 타입 ( 키 : 값)
dictdata['C'] = 100 # 기존 키가 없으면 키와 값을 추가
dictdata['B'] = 33 # 기존 키가 존재하면 value를 업데이트

print(dictdata)
print(dictdata['A'])
print(dictdata['B'])

for key in dictdata:
    print(key, dictdata[key])

kl = [key for key in dictdata if dictdata[key] == 100]
print(kl)

# set 타입 ( 집합 타입 ) => 수학의 집합연선(합, 교, 차, 여 )을 지원
set() #으로 선언해야하나  제공함
data1 = { 50, 90, 60, 70} # ==set()
print(data1, type(data1))
# 셋타입은 중복데이터를 허용하지 않음
listdta = [5,5,5,5,5,7,7,7,7,6,6,6,9,9,9,10,10,10]
setdata = set(listdta)
print(setdata)
data2 = {90, 60, 80, 30}
print("data1: ", data1)
print("data2: ", data2)
data3 = data1 - data2 # 차집합 연산
print("data3: ", data3)
print(data1 | data2) # 합집합 연산
print(data1 & data2) # 교집합 연산
print(data1 ^ data2) # 여집합 연산

import random # 파이썬 기본 제공

# 임의의 정수를 추출해서 사용 ==> 기본 제공 randint() 는 하나의 정수를 반환하는 제약
result = random.randint(10, 20)  # 10-20 사이에 있는 임의의 정수 하나 반환
print(result)

result = np.random.randint(1, 46, (6,5))
print(result) # 애는 중복을 허용하므로 set(result) 를 사용하면 중복 제거를, list(result)를 사용하면 리스트로 반환이 가능하다
