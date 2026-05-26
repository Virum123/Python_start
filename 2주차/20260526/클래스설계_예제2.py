

class PersonInfo():
    def __init__(self, arg1, arg2, arg3):
        self.arg = [arg1, arg2, arg3]
        # name, age, local 변수를 따로 설정함
        # 그럼 아래 변수 입력하기가 편했겠네
    def DisplayInfo(self):
        print(f"이름: {self.arg[0]}, 나이: {self.arg[1]}, 지역: {self.arg[2]}")




per1 = PersonInfo("Hong", 30, "Seoul")
per2 = PersonInfo("Kim", 50, "Daejeon")
per3 = PersonInfo("Park", 50, "Busan")

perlist = [per1, per2, per3]
print (perlist)
for per in perlist:
    per.DisplayInfo() # "이름 : "Hong", 나이: 30, 지역: "Seoul"
    print('='*35)