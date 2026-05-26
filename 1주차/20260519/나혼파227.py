import pandas as pd
pets = [
    {"name": "구름", "age": 5},
    {"name": "초코", "age": 3},
    {"name": "아지", "age": 1},
    {"name": "호랑이", "age": 1}
]

mydf = pd.DataFrame(pets)
mydf = mydf.set_index("name")
print(mydf)

# for item in pets:
#     print(f"{item['name']} {item['age']}살")