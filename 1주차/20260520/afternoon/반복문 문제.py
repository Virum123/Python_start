# 키와 밸류를 바꾸는 문제

my_dict = { 'a':1, 'b':2, 'c':3, 'd':4 }
print(my_dict)
# value = key, key = value
rev_dict = {}
for key in my_dict:
    value = my_dict[key]
    rev_dict[value] = key # 이걸 한 줄로 줄이면 rev_dict[my_dict[key]] = key
    
print(rev_dict)