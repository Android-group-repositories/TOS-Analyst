# # 假设你的文本文件名为 'example.txt'
# file_name = 'example.txt'

# # 使用with语句打开文件，这样可以确保文件在读取完毕后会被正确关闭
# with open(file_name, 'r', encoding='utf-8') as file:
#     # 按行读取文件
#     for line in file:
#         # 打印每行内容，去除行尾的换行符
#         print(line.strip())
import re

text = "#Type2-pattern1# Your privacy policy needs to describe YOU {use} {cookies} ; to {third parties} ; for {the purposes of attribution and/or serving targeted Advertisements} ; Even obtain user consent"

# 使用正则表达式匹配##中的内容
hash_pattern = r'#(.*?)#'
hash_content = re.search(hash_pattern, text)
hash_content = hash_content.group(1) if hash_content else ''

# 使用正则表达式匹配{}中的内容
curly_pattern = r'\{(.*?)\}'
curly_contents = re.findall(curly_pattern, text)

# 输出结果
# print('##中的内容:', hash_content)  # 输出: Type2-pattern1
# print('{}中的内容:', curly_contents)  # 输出: ['use', 'cookies', 'third parties', 'the purposes of attribution and/or serving targeted Advertisements']        

print([hash_content]+curly_contents)