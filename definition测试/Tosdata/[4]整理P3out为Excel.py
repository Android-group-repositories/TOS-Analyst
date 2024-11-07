# 打开文件
from LIBS.OpenAIheader import *
N = get_Number_of_tos()
def extract_enclosed_block(content, start_index):
    """
    从给定的起始位置开始，向前和向后搜索以找到被{}包裹的段落。
    """
    open_braces = 1  # 初始时有一个左大括号需要匹配
    current_index = start_index + 1  # 从#type1标记之后开始搜索
    
    while open_braces > 0 and current_index < len(content):
        if content[current_index] == '{':
            open_braces += 1
        elif content[current_index] == '}':
            open_braces -= 1
        current_index += 1
    
    if open_braces == 0:
        return content[start_index:current_index]  # 返回匹配的段落
    else:
        return None  # 没有找到匹配的右大括号

def process_file(file_path):
    ans =[]
    """
    读取文件并处理，为每个包含#type1的行提取被{}包裹的段落。
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    start_index = 0
    while True:
        start_index = content.find("#type", start_index)
        if start_index == -1:
            break  # 如果没有更多的#type1，退出循环
        
        # 寻找#type1之前最近的左大括号
        start_index = content.rfind("{", 0, start_index)
        if start_index != -1:
            enclosed_block = extract_enclosed_block(content, start_index)
            if enclosed_block is not None:
                print("Enclosed block found:")
                print(enclosed_block)
                tmp = enclosed_block.replace('\n','').replace('\r', '')
                
                ans.append(tmp)
                print("--------------------")
            else:
                print("No matching closing brace found for #type1 at position", start_index)
        else:
            print("No opening brace found before #type1 at position", start_index)
        
        start_index += len("#type1")  # 更新搜索的起始位置
    return ans







for i in range(0, N):
    with open('P3output/'+str(i)+'gpt_gpt结果.txt', 'r') as file:
        type_res_list = process_file('P3output/'+str(i)+'gpt_gpt结果.txt')
        print(N)
        with open('P3output/'+str(i)+'gpt_gpt结果_YES.txt', 'w') as output_file:
        # 逐行读取文件
            for line in file:
                # 检查当前行是否包含大写的"YES"
                
                if "Description".lower() in line.lower():
                    description = "<"+line.strip()+">"
                if '#Type'.lower() in line.lower():
                    # 输出这行
                    tmp= description + type_res_list[0]
                    type_res_list.pop(0)
                    # print(tmp.encode())
                    # input()
                    print(tmp,file=output_file)
    
for i in range(0, N):
    with open('P3output/'+str(i)+'gpt_gpt结果.txt', 'r') as file:
        with open('P3output/'+str(i)+'gpt_gpt结果_YES_转义.txt', 'w') as output_file:
        # 逐行读取文件
            for line in file:
                # 检查当前行是否包含大写的"YES"
                if 'Description'.lower() in line.lower():
                    # 输出这行
                    tmp = line.replace("Description","").replace("\n","")
                    # print(tmp)
                    
                    print(tmp,file=output_file)
                    # input()

import pandas as pd
import os
import re

def make_tuple(text):
    # print(text)
    
    matches = re.findall(r'#(.*?)#', text)

    Sentence_type = matches
    # 打印匹配结果
    # for match in matches:
        # print(match.strip())
    matches = re.findall(r'<(.*?)>', text)

    
    tuple2 = []
    for i in range(len(matches)):
        if(";" in matches[i]):
            tuple2+=matches[i].split(";")
        else:
            tuple2+=[matches[i]]

    ans = Sentence_type+tuple2
    print(ans)
    # input()
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
ZHUANYI_sentence = []
for i in range(0,N):
    tmp = 'P3output/' + str(i) + "gpt_gpt结果_YES_转义.txt"
    with open(tmp, 'r') as file:
        contents = file.read()
        # print(contents)
        # input()
        ZHUANYI_sentence.append(contents)
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
print(df)
name_list = []
for sentence in df['name']:
    name_list.append(sentence)

Sentence_list = []
# sentence
for sentence in df['sentence']:
    Sentence_list.append(sentence)
print(len(name_list))
print(len(split_contents_list))
# ans = [["sdkname","原文","type","转义","entity",  "Actions"  ,   "object"  ,   "Modifier"  ,   "purpose"  ,  "conditions"  ,  "type requirement"]]
ans = [["sdkname","原文","type","转义","entity",  "Actions"  ,   "object"  ,   "object source","purpose"    ,  "conditions"  ,  "type requirement"]]
# ans=[]
for i in range(len(name_list)):
    for tuple in split_contents_list[i]:
        ele = [name_list[i]] + [Sentence_list[i]] + tuple
        # ic(ele)
        # input()
        ans.append(ele)
print(ans)
df = pd.DataFrame(ans)

# 写入Excel文件
df.to_excel('output_Tuple.xlsx', index=False)