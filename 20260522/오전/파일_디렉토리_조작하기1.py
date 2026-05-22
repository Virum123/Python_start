

# python_basic 디렉토리 아래에 'reference' 디렉토리를 만들고

# '20260521' 디렉토리 내부에 존재하는 Health_ifo.csv파일을
# 'reference' 디렉토리 내부로이동
import os
import sys
import shutil

print(os.getcwd())
rootdir = "C:/python_project/python_basic/"
# os.mkdir( rootdir + "/reference")

# if os.path.exists(rootdir + "reference"):
#     shutil.move(rootdir + "20260521/Health_info.csv", rootdir + "reference" )
# else:
#     pass

# 이거 왜해? 코드레벨에서 자동화할때 필요해, 프로그램이 자동으로 로그 데이터 등을 넘겨주고
# 날짜 단위로 관리하고, 이런 상황에서 사용하는 코드다~

import time
print(time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday)