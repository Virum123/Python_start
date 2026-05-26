scorelist =  [ ["Kor"], ["Eng"], ["Math"] ]
print(scorelist)

# 문제
# input() 함수를 이용해 키보드로 각 과목의 점수를 입력 받아 저장시키기

scorelist[0].append(int(input("국어 점수를 입력하세요: ")))
scorelist[1].append(int(input("수학 점수를 입력하세요: ")))
scorelist[2].append(int(input("영어 점수를 입력하세요: ")))
# 답안은 여기서 append 안에 넣은 걸 변수화해서 넣었네

sumscore = scorelist[0][1] + scorelist[1][1] + scorelist[2][1]
avgscore = sumscore / len(scorelist)
avgscore = round(avgscore, 2)
print("점수 합계: ",sumscore)
print("점수 평균: ", avgscore)

print( scorelist ) # ["Kor", 점수] 형식으로 저장되도록

# 리스트에 리스트가 싸여있는 구조
# 리스트를 파싱하고 개별 리스트에 점수를 추가하면 될듯
# 리스트에 값을 추가할거면 append가 나을듯? 차피 하난데
# 그럼 그걸 input이랑 어떻게 연계시킬건데
# input으로 값을 받고 해당 값을 append하면 되지 않을까?
# 그럼 수식은?
# input(x) 로 넣고 x값을 append
# 이걸 반복문으로 3회 돌리면 되고
# 이걸 총점 및 평균을 계산할거면
# 포인터로 리스트[i][1] 로 계산해서 더하고 나누는거 하면 되겠지?
#

# 학생의 총점과 평균을 계산해서 출력