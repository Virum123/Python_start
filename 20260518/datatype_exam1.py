# 파이썬은 객체지향 언어 ( OOP )
# 파이썬은 기본적으로 다양한 클래스를 제공 (int, float, str)

# 클래스를 바탕으로 객체를 생성하고 생성된 객체를 변수로 참조해서 동작하는 언어
# ==> 파이썬 프로그램 기본 동작

data = int(50) # 클래스를 바탕으로 객체를 생성하는 문법 ==> 클래스명() 원칙
# data  변수는 50 이라는 정수 객체를 참조하는 역할
# 그냥 50 적어도 됨
daty = 50 # 동적 타이핑 언어 > 타이핑 하는 순간 자료형 결정
print(data, daty, type(data), type(daty), id(data))

data = "python"
print(data, daty, type(data), type(daty), id(data))

# 파이썬 변수 = 어떤 객체의 ID든 저장과 참조가 가능
# 특정 객체의 ID를 저장해 특정 객체를 참조하는 역할이 파이썬 변수의 역할

data3 = 5.8
print(data3, type(data3), id(data3))

data4 = True
print(data4, type(data4), id(data4))


# 변수에는 가이드를 저장함(위치)

class MyCls():
    def __init__(self, arg):
        self.mdata = arg
    pass

# 객체를 생성
mydata = MyCls(80) #
print(mydata.mdata)

