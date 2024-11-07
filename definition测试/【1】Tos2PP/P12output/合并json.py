import json

# 假设有两个文件，file1.json 和 file2.json
# file1_path = 'file1.json'
# file2_path = 'file2.json'

# # 读取第一个文件
# with open(file1_path, 'r') as file1:
#     data1 = json.load(file1)

# # 读取第二个文件
# with open(file2_path, 'r') as file2:
#     data2 = json.load(file2)

# # 合并两个字典中的requirements列表
# merged_requirements = data1['requirements'] + data2['requirements']

# # 创建一个新的字典来存储合并后的结果
merged_data = {"requirements":[]}

# # 将合并后的结果保存到一个新的JSON文件中，例如 merged.json
# with open('merged.json', 'w') as outfile:
#     json.dump(merged_data, outfile, indent=4)

print("Requirements have been merged and saved to merged.json")
for i in range(1,28):
    name = str(i)+"step1_提取Tos的要求.json"
    with open(name, 'r') as file1:
        data1 = json.load(file1)
        merged_data["requirements"]  = merged_data["requirements"]  +data1["requirements"]
        
        print(merged_data)
with open('merged.json', 'w') as outfile:
    json.dump(merged_data, outfile, indent=4)
        
        