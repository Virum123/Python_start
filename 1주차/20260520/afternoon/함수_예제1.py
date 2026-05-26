# ==> 코드의 유지보수, 코드 재활용을 향상 시키는 기능
# 특정 기능을 분할헤 완성코드를 구현하는 목적
# y = f(x)
# 함수 구현 ==> 함수 정의, 함수 호출
# 함수 정의 ==> 특정 기능의 명령어 집합 ==> def 키워드로 시작
# 함수 호출 ==> ㅡ특정 합수 부분의로 점프 ==> 함수명으로 시작

# der 함수명(): ==> 함수정의 (매개변수)
def Comnamedistply(arg1, arg2):
    print(f"{arg1}은(는) Ai core 과정을 {arg2} 번째 듣는중" )
    return arg2 + 20
# 함수의 반환값이 없을 경우 None 객체를 반환
# arg = 'Hong'
# 함수호출
print("프로그램 시작")
result = Comnamedistply("Hong", 80)# 함수명( 전달인자 )
print(result)

def InputData(): #아직 정의임 전달인자가 별도로 존재하지 않으니 매개변수도 넣어줄 필요가 없음
    numdata = int(input('정수하나 입력 : '))
    return numdata

data1 = InputData() # 함수호출
print("data1 : ", data1) #함수 안/밖의 변수가 다르다 해당 파트도 정리후 공부 필요
print("프로그램 종료")