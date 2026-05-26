# filetest.txt 파일을 읽어들여서
from posixpath import join

with open ("filetest.txt","r") as fi:
    str = fi.read()
strdata = [ item.strip() for item in str.split(',') ]



# 마지막 정보를 아래와 같이 출력
# [python, test, programming, study, good]
print(strdata)

def FindCharFunc(arg1, arg2):
    count = 0
    for s in arg1:
        if s == arg2:
            count += 1
    return count

FindCharFunc(strdata, 'R')