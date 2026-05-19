# 시퀀스 객체 ==> 데이터의 순서가 있는 객체 ==> 문자열, 리스트, 튜플
# 객체지향언어 ( OOP ) ==> 특정 클래스를 바탕으로 객체를 생성해서 프로그램이 동작
# 객체 생성 문법 ==> 클래스명()
str("python") # 동적 타이핑 타입이 결정이 된다. 문자열, 정수, 실수 등 굳이 써줄 필요가 없다
# 파이썬 변수는 가이드를 제공한다고 생각, 값이 id에 저장되고 그 id를 보여준다
data1 = "python"
# data1.join() # 리스트를 문자열로 결합
# data1.replace() # 문자 대체
# data1.format() # 형식 설정
# data1.split() # 특정 기준으로 나누기
# data1.strip() # 공백제거
# data1.upper() # 대문자화
data2 = '800'

data1[0] # [idx] : 색인 연산,  idx는 항상 0부터 출발
data1[2:4] # [start : stop-1] : 슬라이싱 문법

result = data1 + data2 # 두 '문자열'을 합침
data1 * 5 # 문자열을 반복함
print(list(data1)) # 타입 변환
for item in data1: