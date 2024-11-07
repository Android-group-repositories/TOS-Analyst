from openai import OpenAI
import json

from LIBS.OpenAIheader import *

client = OpenAI(
    api_key = API_KEY,
    base_url = BASE_URL,
)
def read_json_as_dict(json_file_path):
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            return data

def chat(query, history,save_to_history):
    history.append({
        "role": "user", 
        "content": query
    })
    completion = client.chat.completions.create(
        model=MODEL,
        messages=history,
        temperature=0.3,
    )
    result = completion.choices[0].message.content
    if save_to_history:
        history.append({
            "role": "assistant",
            "content": result
        })
    else:
        history.pop()
    # history.append({
    #     "role": "assistant",
    #     "content": result
    # })
    return result

def init_type_prompt(history,P3_promptType):    
    history.append({
    "role": "system",  # 标记为系统消息
    "content": P3_promptType  # 这里放置你想要“教”给AI的内容
    })

    return history
    

def init_tuple_extraction(history,extraction_prompt):
    pass

def prmopt3(history,data_dict,i):
    
    from LIBS.prompt3_Sentence import P3_promptType1,P3_promptType2,P3_promptType3,P3_background
    
    
    history.append({
        "role": "system",  # 标记为系统消息
        "content": P3_background  # 这里放置你想要 教 给AI的内容
        })
    filename = 'P3output/'+str(i)+'gpt_gpt结果.txt'
    with open(filename, 'w') as file:
            pass  # 打开文件并清空内容，不需要写入任何内容
    
    history_typy1 = init_type_prompt(history,P3_promptType1)
    history_typy2 = init_type_prompt(history,P3_promptType2)
    history_typy3 = init_type_prompt(history,P3_promptType3)
    for requirement in data_dict['requirements']:
        
        description = requirement['description']
        type_info = requirement['type']
        type_code = type_info['code']
        # type_description = type_info['summary']
        with open(filename, 'a') as f:
        
            print(f"Description: {description}",file=f)
            print(f"Type Code: {type_code}",file=f)
            
# promptType1 第一方数据、操作相关  
            if 'Type1' in type_code:    
                ask = """
Here are the <Text> you need to analyze:\n
                """
                query = ask+description
                print("\nProcessing for Type1 requirements.",file=f)
                tmp = chat(query, history_typy1,False)
                print(tmp,file=f)
                
                
                
# promptType2 第三方数据、操作相关
            if 'Type2' in type_code:
                ask = """
Here are the <Text> you need to analyze:\n
                """                
                query = ask+description
                print("\nProcessing for Type2 requirements.",file=f)
                tmp = chat(query, history_typy2,False)
                print(tmp,file=f)
                
# opt out
            if 'Type3' in type_code:
                ask = """
Here are the <Text> you need to analyze:\n
                """    
                query = ask+description
                print("\nProcessing for Type3 requirements.",file=f)
                tmp = chat(query, history_typy3,False)
                print(tmp,file=f)

            print("========================= pause ===========================",file=f)
def main():
    N = get_Number_of_tos()
    for i in range(0,N):
        history = [
            {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"}
        ]    
        json_path = "P12output/"+str(i)+'step1_提取Tos的要求.json'
        data_dict = read_json_as_dict(json_path)
    
        prmopt3(history,data_dict,i)
    
if __name__ == "__main__":
    main()                        