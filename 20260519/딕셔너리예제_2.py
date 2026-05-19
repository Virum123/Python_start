import pandas as pd
scoredict = {"Kor": [80, 90, 70], "Eng": [77, 88, 99], "Math": [55, 66, 77]}
print(scoredict)

mydf= pd.DataFrame(scoredict)
print(mydf)

mydf.to_excel("MyDf.xlsx")
print("엑셀 작업이 끝났습니다.")