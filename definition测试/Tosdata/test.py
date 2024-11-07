import re

# 示例跨行字符串
text = """
这是一个示例字符串，
其中包含{
被大括号
包裹的多行内容
}，
以及另一部分{
同样被大括号
包裹的多行内容
}。
"""

# 使用正则表达式匹配被大括号包裹的部分，包括跨行的情况
matches = re.findall(r'\{[^{}]*\}', text, re.DOTALL)

# 输出匹配的结果
for match in matches:
    print(match)




# import json
# tmp = """
# {
# "X Content": "Posts, Post IDs, user profile information, data, information, copies, derivative works"
# }"""

# content = """
# E. Location Data. You shall not, and you shall not allow others to, aggregate, cache, or store location Children data and other geographic information contained in the X Content, except in conjunction with the X Content to which it is attached. You may use location data and geographic information only to identify the location tagged by the X Content."""

# # e. location data. you shall not, and you shall not allow others to, aggregate, cache, or store location children data and other geographic information contained in the posts, post ids, user profile information, data, information, copies, derivative works, except in conjunction with the 
# # posts, post ids, user profile information, data, information, copies, derivative works 
# # to which it is attached. you may use location data and geographic information only to identify the location tagged by the posts, post ids, user profile information, data, information, copies, derivative works.
# data_dict = json.loads(tmp)

# print(data_dict)
# content = content.lower()

# # content = content.replace()``

# for key, value in data_dict.items():
#     print(f"Key: {key}, Value: {value}")
#     content = content.replace(key.lower(),value.lower())
#     print(content)
    