from dataclasses import replace

import re

string_exam = '파이썬, library 활용한 Text Preprocessing!!'
result = re.findall(r'[a-zA-Z]+', string_exam)

# 결과: library,Text,Preprocessing 인 한 문자열로 출력
print(','.join(result))