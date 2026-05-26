
class MyCalData():
    def __init__(self, arg):
        self.data = arg
    def AvgDiplay(self):
        total = 0
        for score in self.data:
            total += score[1]
        avg = total / len(self.data)
        print(f"{len(self.data)}명의 평균: {round(avg, 2)}", )
# floor, ceiling, round, format 등 다양하게 사용을 해도 됨, 근데 여기서는 기본 문법인 .format을 사용했음
# 이번 문제 핵심 : 전달 인자가 리스트임을 파악하기
# format 관련해서도 공부를 하긴 해야겠다 잘 모르네
data = MyCalData( [('Kim', 100), ('Park', 90), ('Hong', 70)])

data.AvgDiplay() # # 100 + 90 + 70 에 대한 평균