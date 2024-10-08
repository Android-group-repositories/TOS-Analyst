import re
import json
from tqdm import tqdm


Number_of_tos = 6
def main():
    
    N = Number_of_tos
    for i in range(0,N):
        try:
            with open('./P1转义/'+str(i)+'转义后tos.json', 'r',encoding="utf-8") as f:
                inited_tos = f.read()
                # print(inited_tos)
                # input()
                data_dict = json.loads(inited_tos)
                # print(data_dict)
                print()
                for requirement in data_dict['requirements']:
            
                    description = requirement['description']
                    
                    print(description)
                input("===========================================================")
        except:
            print("出错了")
            

        # exit()
        # ==================================================================
        
        
        
        
        
        
        
    
if __name__ == "__main__":
    main()