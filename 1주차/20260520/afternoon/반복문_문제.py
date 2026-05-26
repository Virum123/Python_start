wordlist = [ 'car', 'apple', 'casttle', 'bar', 'air', 'cat']

worddict = {}
for word in wordlist: # 시작값을 잡아서 넣으면 되지 않을까? 이대로면 리스트의 요소가 하나씩 들어가겠네
    letter = word[0] # 여기랑 일치하는 값의 리스트를 만들면 되지 않을까? 그럼 리스트를 읽고, 첫 값에 따라 리스트를 만들어?
    if letter in worddict:
        worddict[letter].append(word)
    else:
        worddict[letter] = [word] # 값으로 드가면 안되니까 리스트로 넣음

# 결과물
print(worddict) #{ 'a':['apple', 'air'], 'b':['bar', 'book'], 'c':['car', 'cattle', 'cat'}