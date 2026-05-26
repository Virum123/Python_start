
class MyCalList():
    def __init__(self, list1, list2):
        self.data1 = list1
        self.data2 = list2
    def Sumoflist(self):
        listdata = []
        for i in range(0, len(self.data1)):
           result = self.data1[i] + self.data2[i]
           listdata.append(result)
        # for idx, item in enumerate(self.marg1):
        # print(idx, item, self.marg2[idx])
        # listdata.append( item + self.marg2[idx])
        print(listdata)
data = MyCalList([5,6,7,9], [8,9,5,10])

data.Sumoflist() # [13, 15, 12, 19]
# 차집합 으로도 구현해보자 [6, 7]


class StudentScore():
    def __init__(self, name, *args):
        self.name = name
        self.score = args
    def scoredisplay(self):
        total = sum(self.score)
        print(f"{self.name}  {total}  {total/len(self.score)}")

Studentlist = [
    StudentScore("Hong", 80, 60, 70, 90),
    StudentScore("Kim", 90, 70, 80, 85),
    StudentScore("Park", 88, 66, 77, 99),
    StudentScore("Lee", 92, 72, 82, 82)
]

print("이름", "총점", "평균")
for student in Studentlist:
    student.scoredisplay()

# 이름 총점 평균
# Hong 368 92.5
# Kim 360 92.5
# Park 350 91.5
# Lee 340 93.4