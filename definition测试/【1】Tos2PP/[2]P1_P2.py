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



def prompt1_1(history):
    from LIBS.prompt1_Sentence import P1_Background_Definition,P1_input_example1,P1_ask
    
    history.append({
    "role": "system",  # 标记为系统消息
    "content": P1_Background_Definition  # 这里放置你想要“教”给AI的内容
    })
    history.append({
    "role": "system",  # 标记为系统消息
    "content": P1_input_example1   # 这里放置你想要“教”给AI的内容
    })
    return history
    
def prompt1_2(history):
    from LIBS.prompt1_Sentence import P1_Background_Definition,P1_input_example2
    
    history.append({
    "role": "system",  # 标记为系统消息
    "content": P1_input_example2   # 这里放置你想要“教”给AI的内容
    })
    


    
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
    
    


from inputSentence import sentence_list
from tqdm import tqdm
def main():
    
    N = get_Number_of_tos()
    for i in tqdm(range(0,N)):
        
        history = [
            {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"}
        ]
        
        # ==================================================================
        from LIBS.prompt1_Sentence import P1_Background_Definition,P1_input_example1,P1_ask
        

        
# 转json
        history = prompt1_1(history) # teach json
        raw_tos  = sentence_list[i]
        replaceed_tos = "\""+raw_tos+"\""
        intojson= """
Summarize the Term of Service above, output the key points of the text.  Try to express it in the original text. The output format is JSON, as described above
        """
        query = replaceed_tos+intojson
        print(query)
        # input("暂停看输入")
        inited_tos = chat(query, history,False)
        # print(inited_tos)
# 改句式
        history = prompt1_2(history)
        rewrite_des = """
there is the json you need to rewrite        
        """
        query = rewrite_des+inited_tos
        inited_tos = chat(query, history,False)
        print(inited_tos)
        
        
        with open('./P1转义/'+str(i)+'转义后tos.json', 'w',encoding="utf-8") as f:
            print(inited_tos,file=f)
        
        
# 分类 ==================================================================

        from LIBS.prompt2_Sentence import P2_Types_fmt
        history = prompt2(history)
        
        P2_ASk2 = '''
Now, read the following text and generate a json according to the above requirements and methods
Note that only the json should be output, and no useless information should be output.
'''       
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