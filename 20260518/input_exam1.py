# # print() ==> 문자열 출력
# # input() ==> 키보드로 부터 문자여를 입력하는 함수
# from unicodedata import numeric
#
# data1 = input("데이터 입력 : ") # "  " 문자열을 화면에 출력하고 입력 대기 상태
# data2 = input("데이터 입력 : ")
#
# print(data1 + data2)
# # print(data1 - data2)
# # print(data1 * data2)
#
# # 타입 변환이 필요하다
# data2 = int(input("정수 데이터 입력 : "))
# data1 = int(input("정수 데이터 입력 : "))
#
# print(data1 + data2)
# print(data1 - data2)
# print(data1 * data2)

saved_pw = 'python'

while True: # 무한 반복 구문
    input_str = input("password 입력( 종료 : quit) ==> ")
    if input_str == saved_pw:
        print('pw success!!')
    elif input_str == 'quit':
        break  # 반복문 탈출
    else:
        print('pw fail!!')
        # >> input과 들여쓰기를 기억
