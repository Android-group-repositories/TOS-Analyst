# 打开文件
from LIBS.OpenAIheader import *
N = get_Number_of_tos()
print(N)
for i in range(0, N):
    with open('P3output/'+str(i)+'gpt_gpt结果.txt', 'r') as file:
        with open('P3output/'+str(i)+'gpt_gpt结果_YES.txt', 'w') as output_file:
        # 逐行读取文件
            for line in file:
                # 检查当前行是否包含大写的"YES"
                
                if "Description".lower() in line.lower():
                    description = "<"+line.strip()+">"
                if '#Type'.lower() in line.lower():
                    # 输出这行
                    tmp= description + line.strip()
                    # print(tmp.encode())
                    # input()
                    print(tmp,file=output_file)
                    
                    
import pandas as pd
import os
import re

def make_tuple(text):
    
    matches = re.findall(r'#(.*?)#', text)

    Sentence_type = matches
    # 打印匹配结果
    # for match in matches:
        # print(match.strip())
    matches = re.findall(r'<(.*?)>', text)

    # print(matches)

    tuple2 = []
    for i in range(len(matches)):
        if(";" in matches[i]):
            tuple2+=matches[i].split(";")
        else:
            tuple2+=[matches[i]]

    ans = Sentence_type+tuple2
    print(ans)
    return ans
# 使用正则表达式匹配##之间的内容


# 打印匹配结果

def func(text):
    ans=[]
    lines = text.split('\n')
    # 再按逗号分割每一行
    for line in lines:
        if(len(line)>1):
            ans.append(make_tuple(line))
            
    return ans

# 初始化一个空列表来存储所有文本文件的内容
contents_list = []
split_contents_list = []
# 读取每个文本文件，并将内容添加到列表中
for i in range(0,N):
    tmp = 'P3output/' + str(i) + "gpt_gpt结果_YES.txt"
    with open(tmp, 'r') as file:
        contents = file.read()
        contents_list.append(contents)
        tmp1 = func(contents)
        split_contents_list.append(tmp1)
        
# ZHUANYI_sentence = []
# for i in range(0,N):
#     tmp = 'P3output/' + str(i) + "gpt_gpt结果_YES_转义.txt"
#     with open(tmp, 'r') as file:
#         contents = file.read()
#         # print(contents)
#         # input()
#         ZHUANYI_sentence.append(contents)


tmp = {
    "Content": contents_list,
    "Tuple" : split_contents_list
}


df = pd.DataFrame(tmp)

# 将DataFrame输出到Excel文件
excel_path = 'output.xlsx'
df.to_excel(excel_path, index=False, engine='openpyxl')

print(f"Excel file has been created at {excel_path}")





# ==========================================================================================

excel_path = 'inputSentence1.xlsx'

# 使用pandas的read_excel函数读取数据
# sheet_name参数指定要读取的工作表名称，index_col参数指定列索引
df = pd.read_excel(excel_path, sheet_name='Sheet1')  # 假设我们要读取第一列，即列A

# 打印读取的列

name_list = []
for SDKname in df['name']:
    name_list.append(SDKname)

Sentence_list = []
# sentence
for sentence in df['sentence']:
    Sentence_list.append(sentence)

from icecream import *
# print(len(name_list))
# print(len(split_contents_list))
ans = [["sdkname","原文","type","转义","entity",  "Actions"  ,   "object"  ,   "object source/target"  ,   "purpose"  ,  "Other conditions", "type requirement1","type requirement2"   ]]
# ans=[]
for i in range(len(name_list)):
    for tuple in split_contents_list[i]:
        ele = [name_list[i]] + [Sentence_list[i]] + tuple
        # ic(ele)
        # input()
        ans.append(ele)
for i in ans:
    print(len(i))
    
max_length = max(len(row) for row in ans)

# 填充短的子列表
for row in ans:
    while len(row) < max_length:
        row.append(None)  # 或者可以使用其他的默认值

# 现在每个子列表的长度都等于最长的子列表
# print(ans)
df = pd.DataFrame(ans[1:],columns = ans[0])

# 写入Excel文件
print("写入Excel文件...")
df.to_excel('output_Tuple1.xlsx', index=False)