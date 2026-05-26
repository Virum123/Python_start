
# 객체지향 언어(OOP) / object oriented programming
# 클래스를 기반으로 객체를 생성해서 동작하는 프로그램

# 클래스 ==> 정보를 담는 역할의 멤버변수, 멤버변수를 접근해서 관리하는 멤버함수(메서드)
# 클래스 ==> 멤버변수 + 멤버함수(메서드) 하나의 큰 자료형(타입)을 설계함
# >> 추상화 개념

# 객체(실체물)를 생성할때 특정 클래스를 바탕으로 객체를 생성

# 기본 제공 클래스 ==> int(), float(), Bool(), str(), list(), tuple()
# ==> dict(), set()

# 사용자가 직접 정의한 클래스 ==> 사용자 정의 클래스
# 클래스 정의 키워드 ==> class

class MyCls():  # 클래스 정의
    def __init__(self, arg):        # 멤버변수를 등록하고 초기화해주는 특수한 역할의 메서드
        # print(" __init__() 호출됨")
        local_val = 50
        self.m_val = arg # 객체의 멤버변수를 등록하고 초기화

    def Infodisplay(self):
        # self ==> 해당 메서드를 어떤 객체가 호출햇는지, 객체의 정보가 자동으로 전달됨
        # print(local_va;)
        print("self.m_val" , self.m_val)

# MyCls 클래스를 바탕으로 객체를 생성해야지만 프로그램이 동작
# 객체 생성 문법 ==> 클래스명()
data = MyCls(60) # 객체가 생성되는 시점에서 자동으로 호출되는 특수한 메서드(생성자역할의 함수)
# print(data.m_val) # 외부접근
data.Infodisplay()

# mystr = "python"
temp_data = MyCls('얍얍얍')
temp_data.Infodisplay() # print(Infodisplay()) 하면 리턴값이 없어서 답이 안나와요~

