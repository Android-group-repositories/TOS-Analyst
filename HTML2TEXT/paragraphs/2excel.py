import json
import pandas as pd
def make_Excel(excel_list,FileName):
    df = pd.DataFrame(excel_list[1:],columns = excel_list[0])
    
    df.to_excel(FileName+'.xlsx', index=False)

# 指定JSON文件的路径
sdkname_list = ['Facebook','Twitter','Paypal',"InMobi","sentry",'flurry']
json_list =[i+'.json' for i in sdkname_list]
head_title = ["name",'sentence']
Data_Excel =[head_title]
Children_Excel =[head_title]
PP_Excel =[head_title]
for sdkname in sdkname_list:
    json_file_path = sdkname + '.json'

    

    # 打开JSON文件并读取内容
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 现在 data 是一个Python字典，包含了JSON文件的内容
    if(len(data["PP"])>=1):
        for pr in data["PP"]:
            for i in pr:
                tmp = [sdkname,i]
                PP_Excel.append(tmp)
            
    if(len(data["Data"])>=1):
        for pr in data["Data"]:
            for i in pr:
            # print(i)
                # input()`
                tmp = [sdkname,i]
                print(len(tmp),tmp)
                Data_Excel.append(tmp)
            
            
    if(len(data["Children"])>=1):
        for pr in data["Children"]:
            for i in pr:
                tmp = [sdkname,i]
                Children_Excel.append(tmp)
        
make_Excel(PP_Excel,"./output/PP_sentence")
make_Excel(Data_Excel,"./output/Data_sentence")
make_Excel(Children_Excel,"./output/Children_sentence")