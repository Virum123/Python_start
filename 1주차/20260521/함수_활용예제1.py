# 암호화에 대한 이야기
# 이게 발전해서 랜섬웨어가 되는구나
# 사전이 없으면 복구가 안되는구나
def EncryptFunc(msg):
   # print(msg)
    for s in msg:
        if s in EncBook:
            msg = msg.replace(s, EncBook[s])
    return msg
# 내 답
# def DecryptFunc(arg1):
#    # print(msg)
#     for s in arg1:
#         for key in EncBook:     # 그냥 사전 받아와서 key값을 받자
#             if s in EncBook[key]:  # 이거 키값 출력을 어떻게 해야하지?
#                 arg1 = arg1.replace(s, key)
#     return arg1

# 썜 답
def DecryptFunc(encmsg):
    # 반대되는 사전을 만드네..
    DecBook = {}
    for key in EncBook:
        DecBook[ EncBook[key] ] = key
    # print(DecBook)
    # 나머진 위에거 그대로..
    for s in encmsg:
        if s in DecBook:
            encmsg = encmsg.replace(s, DecBook[s])
    return encmsg
stringdata = "I love ai pythton programming"
EncBook = { 'l':'#', 'p':'@', 'o':'7', 'g':'$', 'I':'%', 'a':'8', 't':'*', 'r':'3','n':'6'}
encmsg = EncryptFunc(stringdata) # 전달된 문자열을 암호화 시켜서 반환하는 함수 호출
print(encmsg)

# 위 암호화된 문자열을 다시 복원시키는 함수를 구현
# 딕셔너리를 교체하는것 보다는 밸류값을 받으면 키값을 반환하도록 출력하면 되겠다.
# 1. 암호화 한 내용을 복호화 하는 과정
# 2. 일단 암호화한 내용을 하나씩 받아야함
# 3. 그리고 그걸 사전에서 받아서 교체하는건데
# 4. 아니 근데 딕셔너리를 다시짜요? 개귀찮은데
# 5.
decmsg = DecryptFunc(encmsg)
print(decmsg)

## 핵심 개념은 딕셔너리를 뒤집는 법인듯