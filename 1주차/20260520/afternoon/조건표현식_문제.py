from numpy.ma.core import count

srcstring = "PYTHON PROGRAMMING"

# result = srcstring.lower() # 메서드 금지
# 리스트 내포와 조건표현식을 활용해 구현
# ord() ==> 문자데이터의 원 수치 데이터를 반환하는 함수 --> 새 개념 **
# chr() ==> 원 수치 데이터를 문자데이터 형태로 변환해서 반환하는 함수 --> 새 개념 **

listdata = [' '  if chr(ord(x) + 32) == '@' else x for x in srcstring ]
# listdata = [ chr(ord(x) + 32) if  x != ' ' else x for x in srcstring ] 이런 식으로도 가능 이게 더 본질적이라 괜찮을듯

print( listdata )
result= ''.join( listdata )
print(result) # "python programming"

wordlist = [ "book", "car", "apple", "python", "ai"]
# wordlist 에 문자열 항목 중 문자열의 길이가 4이상인 문자열만 새 리스트에 저장 출력
list4 = [x for x in wordlist if len(x) > 4 ]
print( list4 )

# 동일한 명령을 반복 수행할 경우 사용하는 구문 ==> 반복구문( loop 구문 )
# for(), while()

for x in [4,5,6]:
    print(x)

print('반복문을 탈출했습니다.')

# 문제1) for 와 range() 를 활용해서 1 ~ 100 까지의 정수 합을 계산해서 출력
total = 0
for x in range(1, 101):
    total += x
    print(f'{x}까지의 합: {total}')
print(f'합계는 {total}입니다.')
print()
print('합계 출력 종료')

# 문제2) "Ai Python Programming,Ai Agent Programming" 이 문자열 중 'g' 문자의 개수를 for 반복문 활용해서 계산
print('\n[g]의 개수 찾기' )
count_g = 0
ai = 'Ai Python Programming,Ai Agent Programming'
for x in ai:
    if x == 'g':
        count_g += 1 # 파이썬은 ++ -- 같이 1씩증가는 없다.
        print(f'[g]를 찾았습니다! 현재까지 찾은 [g]의 개수: {count_g}개')


print(f'모든 [g]의 개수: {count_g}')

# 문제3) 표현할 구구단의 단수를 입력받고 해당 구구단의 내용을 출력 ( for 구문 활용)
print('\n구구단을 외자~ 구구단을 외자~')

for x in range(1, 10):
    print(f'{x}단')
    for s in range(1, 10):
        print(f'{x} * {s} = {x * s}')

# 아 이거 입력받는거네 정리할땐 바꿔서 정리해야겠다.
