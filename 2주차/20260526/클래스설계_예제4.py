

class MyComInfo():
    def __init__(self, arg = 'Python Academy'):
        self.name = arg

    def DisplayName(self):
        print(self.name)

    def SettingName(self, arg):
        self.name = arg
com1 = MyComInfo('AI Academy')
com1.DisplayName() # AI Academy

com2 = MyComInfo()
com2.DisplayName() # Python Academy

com2.SettingName('Agent Academy')
com2.DisplayName()

data = 0
print(id(data))
# 메모리랑 id랑 다름 여기는 시스템에서 만들어놓은 인식표같은것
# 가상 메모리는 더 늘린거? 그게 뭐지 젠장 처음들어봐