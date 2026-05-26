

# 파이썬 기본 제공 ==> 범위데이터 생성하는 클래스

print( list( range(30, 41) ) ) # 0, 1, 2, 3, ...9
# 그냥 넣으면 0, 1만 나오는데 list에 넣으면 순서대로 주루룩
# 그런데 range() 자체는 숫자 목록을 바로 보여주는 게 아니라 범위 객체라서, 확인하려면 list()로 감싸야 함

# listdata = []
# for x in range(0, 10):
#     print('출력: ', x)
#     listdata.append(x)

listdata=[ x for x in range(0,10) if x%2 == 0 ] # 리스트 컴프리헨션 //리스트 내포 + 여과(굳이 국어를 쓰는 이유가 있나)

print(listdata)

listdata=[ str(x+5) for x in range(0,10)]
print(''.join(listdata)) # str (x + 5) 라서 가능한것, 정수 객체면 안됨
mystr = "kbs, mbc, sbs"
# print(mystr.split(","))
# mystr = ['kbs', 'mbc', 'sbs']

mylist = [item for item in mystr.split(",")]
print (mylist)

mystr1 = "Python , STudy, GooD"
mystr1 = [item.strip().lower()  for item in mystr1.split(",")] #

print(mystr1) #['python', 'study', 'good']

mylistdata = ["python", "prog", "good"]

for item in enumerate(mylistdata): # 인덱스와 아이템을 동시에 반환
    print(item)

for idx, item in enumerate(mylistdata):  # 인덱스와 아이템을 동시에 반환
    print(idx, ' : ', item)