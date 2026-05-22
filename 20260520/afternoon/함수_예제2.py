import numpy as np
def listsumofdata(arg1):
    sum = 0
    for x in arg1:
        sum += x
    return sum

# def addlistdata(arg1, arg2):  이건 넘파이 쓰는 방법이고 for 써서도 해보자
#     arr1 = np.array(arg1)
#     arr2 = np.array(arg2)
#     return (arr1 + arr2).tolist()


def addlistdata(arg1, arg2):
    res = []
    for x in range(len(arg1)):
        res.append(arg1[x] + arg2[x])
    return res

# 정답
# def addlistdata( arg1, arg2 ):
#   listdata = []
#   for idx, item in enumerate(arg1): ## 애는 enumerate의 성질을 알아야 사용할 수있는 것 값과 위치를 반환하는것이 성질
#       listdata.append( item + arg2[idx] )
#   return listdata

total = listsumofdata([60,77, 88, 33])

print('total : ', total) # 전달한 리스트의 총합을 출력


result = addlistdata([5,6,7,8],[2,3,4,5])
print('result : ', result) # [7,9,11,13]
# CheckAlphaData 기능 ==> 앞에 전달된 문자열 중 뒤에 전달된 문자의 개수를 파악해서 반환

def CheckAlphaData(arg1, arg2): # 문자 단위대로 쪼개는건 어떻게할까? 스플릿으로 나눠버릴까
    cnt = 0
    for x in arg1:
        if x == arg2:
            cnt += 1

    print('cnt : ', cnt)


CheckAlphaData("python programming", 'i' ) # 함수호출

