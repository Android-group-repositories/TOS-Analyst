import pandas as pd

# 指定Excel文件路径
excel_path = 'inputSentence1.xlsx'

# 使用pandas的read_excel函数读取数据
# sheet_name参数指定要读取的工作表名称，index_col参数指定列索引
df = pd.read_excel(excel_path, sheet_name='Sheet1')  

# 打印读取的列

sentence_list = []
for sentence in df['sentence']:
    # print(sentence)
    sentence_list.append(sentence)
with open('inputSentence.py', 'w', encoding='utf-8') as f:
    print("sentence_list = ",end='',file=f)
    print(sentence_list,file=f)