from openai import OpenAI
import json
# from LIBS.OpenAIheader import *
# from LIBS.prompt3_Sentence import P3_promptType1,P3_promptType2,P3_promptType3,P3_promptType4
from tqdm import tqdm
from tmpLIB import *


client = OpenAI(
    api_key = API_KEY,
    base_url = BASE_URL,
)


def read_json_as_dict(json_file_path):
        with open(json_file_path, 'r',encoding="UTF-8") as file:
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
    
def prmopt3(history,data_dict):
    
    
    
    # history.append({
    #     "role": "system",  # 标记为系统消息
    #     "content": P3_background  # 这里放置你想要“教”给AI的内容
    #     })
    filename = "PP输出.txt"
    with open(filename, 'w') as file:
            pass  # 打开文件并清空内容，不需要写入任何内容
    history_typy = init_type_prompt(history,P3_promptType1)

    for requirement in data_dict['requirements']:
        
        description = requirement['description']
        type_info = requirement['type']
        type_code = type_info['code']
        type_description = type_info['summary']
        with open(filename, 'a') as f:
        
            
            
# promptType1 第一方数据、操作相关  
            if 'Type1' in type_code:    
                print(f"Description: {description}",file=f)
                # print(f"Type Code: {type_code}",file=f)
                ask = """
Here are the <Text> you need to analyze:\n
                """
                query = ask+description
                print("\nProcessing for Type1 requirements.",file=f)
                tmp = chat(query, history_typy,False)
                print(tmp,file=f)
            
                print("========================= pause ===========================",file=f)
def main():
    history = [
        {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"}
    ]    
    json_path = "biaoge_pp.json"
    data_dict = read_json_as_dict(json_path)
    # print(data_dict)
    prmopt3(history,data_dict)
    
if __name__ == "__main__":
    main()                        