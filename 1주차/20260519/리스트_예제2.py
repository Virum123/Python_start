listdata1 = [50, 30, 20]
# 시퀀스객체에 지원하는 연산 ==> +, *, :
listdata2 = [77, 88, 99]

reslist = listdata1 + listdata2
print(reslist) # 걍 리스트를 합치네 순서도 따지는구만
print(reslist[1:4])
# listtmp = [None] * 10
# print(listtmp)
# listtmp[9] = 40
# print(listtmp)


# listdata3 = [5,6,7,8] # + 3 # 오류! 리스트 + 연산은 리스트 객체끼리 가능(리스트의 한계)
# print(listdata3)

# listdata4 = []
# for item in listdata3:
#     listdata4.append(item+3)
# print(listdata4)

import numpy as np

arr1 = np.array([99, 22, 33, 55])
print(arr1, type(arr1)) # numpy 배열은 출력 항목 사이에 쉼표가 없네
print(arr1 + 3)