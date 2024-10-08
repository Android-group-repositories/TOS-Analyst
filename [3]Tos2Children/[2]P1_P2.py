from openai import OpenAI
from LIBS.prompt2_Sentence import P2_Types_fmt,P2_ASk2
from inputSentence import sentence_list
from tqdm import tqdm
from LIBS.prompt2_Sentence import P2_Types_fmt,P2_ASk2
import re
import json

from LIBS.OpenAIheader import *
from LIBS.prompt1_Sentence import P1_Background_Definition,P1_input_example,P1_ask
from LIBS.prompt1_Sentence import P1_Background_Definition,P1_input_example,P1_ask
# BASE_URL = "https://api.holdai.top/v1"
# # MODEL = "gpt-3.5-turbo"
# API_KEY = "sk-kk5QnQbIkzxsASlPA11b444dFfCd467989Bb120b4d8e0aA9"
# # MODEL = "gpt-4-1106-preview"
# MODEL = "gpt-4-turbo-preview"
# MODEL = "gpt-4o-mini"

client = OpenAI(
    api_key = API_KEY,
    base_url = BASE_URL,
)



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
    return result


def prompt1(history):
    
    
    history.append({
    "role": "system",  # 标记为系统消息
    "content": P1_Background_Definition  # 这里放置你想要“教”给AI的内容
    })
    history.append({
    "role": "system",  # 标记为系统消息
    "content": P1_input_example   # 这里放置你想要“教”给AI的内容
    })
    
    # pro = "new I give you a text:\n"
    # ask = "Regarding this TOS, as a developer, What points should I pay attention to? Answer with original text"
    # query = pro + raw_tos + ask 

    
    return history

def prompt2(history):
    
    history.append({
        "role": "system",  # 标记为系统消息
        "content": P2_Types_fmt  # 这里放置你想要“教”给AI的内容
        })
    
    
    # 添加 类型的前缀进去 

    
    return history


    
def extract_json_from_markdown(markdown_text):
    pattern = r'```json(.*?)```'
    json_data = re.findall(pattern, markdown_text, re.DOTALL)
    
    extracted_json = []
    for match in json_data:
        try:
            extracted_json.append(match.strip())
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
    
    return extracted_json    



def main():
    
    N = get_Number_of_tos()
    for i in tqdm(range(0,N)):
        
        history = [
            {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"}
        ]
        
        # ==================================================================
        
        history = prompt1(history)
        raw_tos  = sentence_list[i]
        query = "text:\n"+"\""+raw_tos+"\"" + P1_ask
        print(history)
        # input("wait")
        inited_tos = chat(query, history,True)
        print(inited_tos)
        with open('./P1转义/'+str(i)+'转义后tos.txt', 'w',encoding="utf-8") as f:
            print(inited_tos,file=f)
        # exit()
        # ==================================================================
        history = prompt2(history)
        
        
        
        query = P2_ASk2 + inited_tos
    
        
        tmp = chat(query, history,False)
        
                
        
        print("============================")
        print(tmp)
        print("============================")
        # tmp = extract_json_from_markdown(tmp)[0]
        
        # ==================================================================
        # 存文件
        cn = "After outputting the English, translate JSON blow into Chinese and output a copy.\n\n"+tmp
        tmpcn = chat(cn, history,False)
        
        data_dict = json.loads(tmp)
        with open('./P12output/'+str(i)+'step1_提取Tos的要求.json', 'w',encoding="utf-8") as f:
            print(tmp,file=f)

        
        print(tmpcn)
        with open('./P12output/'+str(i)+'step1_提取Tos的要求_CN.json', 'w',encoding="utf-8") as f:
            print(tmpcn,file=f)
        
        
        
        
        
        
        
        
    
if __name__ == "__main__":
    main()