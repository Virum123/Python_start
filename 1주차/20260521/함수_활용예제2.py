
def AlphaFindFunc(strdata):
    alpha_list = []
    for a in strdata: # 아스키 안쓰고 그냥 문자열로 비교해놨나보네 ㅇㅋㅇㅋ
        if ('A'<= a <= 'Z') or ('a' <= a <='z'): # 문자가 알파벳이면 그대로 반환하고, 아니면 제거, 마지막엔 그냥 반환해서 문자열로 합치기
            alpha_list.append(a)

    result = ''.join(alpha_list)
    return result



strdata = '# Ai % 3 pro&*graM'


result = AlphaFindFunc(strdata) # 함수호출
print('result : ', result) # AiprograM ==> 영문대소문자만 추출 출력



# 문자열을 뭘로받을까? 그냥 바로 반복문으로 받아도 되긴 할듯 그 다음엔?
# 알파벳과 아닌걸 구분해야겠지? 그럼 이건 뭘로 구분할건데? 아스키? 너무 많지 않나?
# 아스키 말고는 뭐가있을까? 직접비교하나 있고 그 다음엔 뭐있지
# 비교연산자를 써야하나 흠 워지

# 문제2)

def WordCountFunc(listdata):
    cnt_dict = {}
    for word in listdata:
        if word in cnt_dict:
            cnt_dict[word] += 1
        else:
            cnt_dict[word] = 1
    return cnt_dict
listdata = ['python', 'ai', 'study', 'good', 'ai', 'python', 'ai']

result = WordCountFunc(listdata)
print('result : ', result) # { ' python':2, 'ai':3, 'study':1, 'good':1 }

# 문제3)

def InforCombine(listdata, valuedata):
    # 내 답, enumerate 사용을 생각하지 못햇다
    # key_dict = {}
    # for x in range(3):
    #     key_dict[listdata[x]] = valuedata[x]
    # return key_dict
    # 쌤 답 이걸 한줄로 어떻게 적지? 리스트 컴프리헨션이나 조건표현식은 아니고
    # 컴프리헨션은 딕셔너리에도 존재함
    key_dict = {}
    for idx, item in enumerate(listdata):
        key_dict[item] = valuedata[idx]
    return key_dict

    # 한줄로 만들기
    # dictdata = { item : arg2[idx] for idx, item in enumerate(arg1)}
    # print (dictdata)

key_list = ["name", "age", "address"]
value_list = ["Hong", 50, "seoul"]

result = InforCombine(key_list, value_list)
print('result : ', result)  # {"name":"Hong", "age":50, "address":"seoul"