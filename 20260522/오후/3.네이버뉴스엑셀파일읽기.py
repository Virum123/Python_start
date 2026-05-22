import pandas as pd
import re
newsdf = pd.read_excel('navernewsdata.xlsx')
#print(newsdf)
#print(newsdf['뉴스 제목'][0])

# for item in newsdf['뉴스 제목']:
#     result = re.findall(r'[ㄱ-힣]',item)
#     print(''.join(result))
#     print('=' * 50)
print(newsdf)
print("="*80)
def newstitlefiltering(arg):
    # print('arg : ', arg)
    print(re.sub(r'[^ㄱ-힣\s]+', '', arg))
    return re.sub(r'[^ㄱ-힣\s]+', '', arg)

newsdf['뉴스 제목'] = newsdf['뉴스 제목'].apply(newstitlefiltering)
# 엑셀의 한 컬럼을 선택하면, 일괄 적용할 함수 호출 그리고 컬럼 전체를 함수 돌림

print(newsdf)
nesdf.to_excel("navernews_filtering.xlsx", index=False)