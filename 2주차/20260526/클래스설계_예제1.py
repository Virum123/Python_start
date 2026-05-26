
class MyDataControl():
    def __init__(self, *arg):
        # print("객체 생성 완료!!")
        # print(arg)
        # # 멤버변수 등록하고 초기화
        self.m_arg = arg

        # 멤버변수 등록 및 초기화
    def SumofData(self):
        # 합을 계산하는 로직은 여기서 출력
        total = 0
        for num in self.m_arg:
            total += num
        print('total : ', total ) # 50,60,70,80,90 의 합을 출력
# 객체 생성 ==> 객체가 생성될때 "객체 생성 완료!!" 를 출력
value = MyDataControl(50, 60, 70, 80, 90) # 객체를 메모리에 생성했으면 변수로 참조해야함
value.SumofData()

# self 로 멤버변수 만드는 것에 대해 생각하기