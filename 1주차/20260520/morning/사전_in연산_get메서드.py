dictdata = { 'Kor':90, 'Eng':70, 'Math':80}

print('py' in 'python')

print('Kor' in dictdata)
print('Music' in dictdata)
while(True):
    key = input("'key'를 입력하세요: ")
    if key in dictdata:

        print(dictdata[key])
    elif key == 'quit':
        break
    else:
        print(dictdata, " 중에 입력하세요.")
while True:

    inputdata = input("출력하고자 하는 과목을 입력: ")
    if  dictdata.get(inputdata, None): #키가 존재하면 키에 대한 value를 반환, 없으면 뒤에 명시된 값을 반환(고정값)
        print(dictdata[inputdata])
    elif inputdata == 'a':
        break
    else:
        print("과목 없음")
