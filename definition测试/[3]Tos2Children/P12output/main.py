import json
# import pandas as pd

# 假设你的JSON文件名为data.json
json_file = 'data.json'

for i in range(20) :


    json_file = str(i)+'step1_提取Tos的要求.json'

    # 读取JSON文件
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 提取description字段
    descriptions = [item['description'] for item in data['requirements']]
    print(i+1)
    for x in range(len(descriptions)):
        print(x,descriptions[x])
        print()
    print('==================================')         
    
    