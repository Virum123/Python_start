scorelist =  [ ["Kor"], ["Eng"], ["Math"] ]
print(scorelist)

# 문제
# input() 함수를 이용해 키보드로 각 과목의 점수를 입력 받아 저장시키기

kor = int( input("국어 점수를 입력 : "))
scorelist[0].append(kor)

eng = int( input("영어 점수를 입력 : "))
scorelist[1].append(eng)

math = int( input("수학 점수를 입력 : "))
scorelist[2].append(math)

print(scorelist)
# 학생의 총점과 평균을 계산해서 출력
total = scorelist[0][1] + scorelist[1][1] + scorelist[2][1]