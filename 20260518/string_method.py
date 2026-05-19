from dataclasses import replace

name = "김대훈"
age = 50

print("나의 정보 ==> 이름 : {} , 나이 : {}".format(name, age))
print(f"나의 정보 ==> 이름 : {name} , 나이 : {age}") # format 또는 fstring을 기억하자

strdata = """python programming
test python prog
python start
"""

print(strdata.capitalize()) # p-P로 바뀐 새로운 문자열 객체 생성 = 다른 객체임
print(strdata.count('python'))
strdata1 = "test programming"
print(strdata1.replace("test", "python"))
strdata2 = "python,programming,test,log"
print(strdata2.split(",")) # 문자열 객체를 특정 문자기준으로 분할
print(strdata2.replace(",", " " ))
print(strdata2)
result = strdata2.split(",")
print(result[2])
print(result)
# 문제
string_exam = "kbs, mbc, jtbc,sbs "
print(string_exam) #[kbs,mbc,jtbc,sbs]
result = string_exam.replace(" ", "")
print("["+result+"]")


string_exam = "kbs, mbc, jtbc,sbs "
newstring = string_exam.split(',')
#strip: 앞뒤 공백, 개행 모두 제거
listdata1 = ['kbs', 'mbc', 'jtbc', 'sbs']
newdata = "".join(listdata1) # 데이터를 합침
print(newdata)

listdata3 = "python#test ai programming,study"

result = listdata3.replace("#", " ").replace(",", " ") + " good"

print(result)

import re # 정규표현식
listdata3 = listdata3 = "python#test ai programming,study"
re.sub(r'[#,@]',' ',listdata3)