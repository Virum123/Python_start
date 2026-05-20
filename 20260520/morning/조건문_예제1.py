

# 파이썬 조건문 ==> 단독 if구문, if~else구문, if~elif~elif~else 구문
# 조건문 ==> 프로그램의 흐름을 제어하는 역할의 구문 ( 제어문 )
# 조건표현식 ==> 참, 거짓을 반환하는 문법을 사용
# 비교(관계) 연산자 ==> >< => <= == !=
# 비트연산자 ==> !, &, |, ^ 거의 안씀
# 논리연산자 ==> or(~중 1개라도 충족하면 true) and(곱 개념, 모두 충족해야 true)
# 사칙연산 ==> +, -, *, /, %(나머지 연산)
print( ( 5 == 3 ) and ( 3 > 1 ) )

print( 5 % 3)

# 컴퓨터에선 0이외의 모든 숫자는 참(True)
data = 3
if data == 5:
    print('오입니다')
else:
    print('오아님')

# 조건의 경우의 수가 많을 경우 사용하는 구문 ==> if ~ elif ~ elif ~ else

cider = 0
cola = 0
w = 0
j = 0

while True:
    print("메뉴 : 1. 사이다 2. 콜라 3. 생수 4. 주스")
    selmenu = input("메뉴 하나를 선택하세요 : ")  # 기본적으로 문자열 객체처리

    if selmenu == "":
        print("아무것도 입력되지 않았습니다.")

    elif selmenu == '그만':
            print( '구매를 종료합니다.')
            print(f'총 구매: {cider + cola + w + j}')
            print(f'사이다: {cider}개')
            print(f'콜라: {cola}개')
            print(f'생수: {w}개')
            print(f'주스: {j}개')
            break
    else:
        selmenu = int(input("메뉴 하나를 선택하세요 : "))  # 기본적으로 문자열 객체처리

        if selmenu == 1:
            cider += 1
            print(f"선택: 사이다, 누적: {cider}개")
        elif selmenu == 2:
            cola += 1
            print(f"선택: 콜라, 누적: {cola}개")
        elif selmenu == 3:
            w += 1
            print(f"선택: 생수, 누적: {w}개")
        elif selmenu == 4:
            j += 1
            print(f"선택: 주스, 누적{j}개")
        else:
            print('메뉴 속 내용만 선택해주세요')

