from openai import OpenAI
import json
import re

from LIBS.OpenAIheader import *

client = OpenAI(
    # sk-kk5QnQbIkzxsASlPA11b444dFfCd467989Bb120b4d8e0aA9
    # gpt-4-0125-preview
    api_key = API_KEY,
    base_url = BASE_URL
)



def chat(query, history,save_to_history):
    history.append({
        "role": "user", 
        "content": query
    })
    completion = client.chat.completions.create(
        model = MODEL,
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



def prompt1(history):
    from LIBS.prompt1_Sentence import P1_Background_Definition,P1_input_example
    
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
    from LIBS.prompt2_Sentence import P2_Types_fmt
    history.append({
        "role": "system",  # 标记为系统消息
        "content": P2_Types_fmt  # 这里放置你想要“教”给AI的内容
        })
    
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
    
    
def definition_add(history,definition_text):
    from LIBS.prompt1_Sentence import add_definition_text

    history.append({
    "role": "system",  # 标记为系统消息
    "content": add_definition_text+definition_text  # 这里放置你想要“教”给AI的内容
    })
    return history
    pass
from LIBS.OpenAIheader import *

from inputSentence import sentence_list
from definition import definition_list

from tqdm import tqdm
def main():
    
    N = get_Number_of_tos()
    for i in tqdm(range(0,N)):
        
        history = [
            {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"}
        ]
        
        # ==================================================================
        from LIBS.prompt1_Sentence import P1_Background_Definition,P1_input_example
        
        
        # history = definition_add(history,definition_list[i])
        # from LIBS.prompt1_Sentence import add_definition_text

# 1 init definition     

#         add_definition_text = """
# I will give you a section of Definitions. Definitions contain a word and its explanation. You need to extract the noun content that the word can be interpreted as, and then output the word and its explanation in the form of key-value pairs.

# Definitions example:
# Prohibited Information” means (i) information under regulatory or contractual handling requirements (e.g., Payment Card Industry Data Security Standards), including, but without 
# limitation, financial account numbers, debit or credit card information, magnetic stripe data, or card verification values; 

# Definitions example:
# {"Prohibited Informationas":"financial account numbers, debit or credit card information, magnetic stripe data, or card verification values"}
# """
#         query = add_definition_text+ definition_list[i] 
#         print("query",query)
#         inited_definition   = chat(query, history,False)
#         matches = re.findall(r'\{[^{}]*\}', inited_definition, re.DOTALL)
#         inited_definition = matches[0]
        

        
#         print("inited_definition\n",inited_definition)
#         # input()
#         data_dict = json.loads(inited_definition)
#         print("data_dict\n",data_dict)
        # input()

# 2 replace
        # raw_tos = sentence_list[i].lower()
        # for key, value in data_dict.items():
        #     # print(f"Key: {key}, Value: {value}")
        #     raw_tos = raw_tos.replace(key.lower(),value.lower())
        # # print(raw_tos)
        # # query = ask_tmp+ "\""+raw_tos+"\"\n"
        # # print('query:',query)
        
        # # inited_tos = chat(query, history,False)
        # # print("=======================")
        # replaceed_tos = raw_tos
        
        # print('replaceed_tos',replaceed_tos)
        # input()
# 3 转义 json化
        history = prompt1(history) # teach json
        intojson= """
Summarize the Term of Service above, output the key points of the text.  Try to express it in the original text. The output format is JSON, as described above
        """
        replaceed_tos = sentence_list[i].lower()
        
        query = replaceed_tos+intojson
        inited_tos = chat(query, history,False)
        
        print("inited_tos",inited_tos)
        # input()
        with open('./P1转义/'+str(i)+'转义后tos.json', 'w',encoding="utf-8") as f:
            print(inited_tos,file=f)
        # ==================================================================
        from LIBS.prompt2_Sentence import P2_Types_fmt,P2_ASk2
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