import spacy
from spacy.matcher import Matcher

# 加载英文模型
nlp = spacy.load("en_core_web_sm")

# 待处理的文本
text = "your app cannot collect personal information; user: minors; Even obtain user consent"

# 创建一个Matcher对象
matcher = Matcher(nlp.vocab)

# 定义一个模式来匹配 "not collect personal information"



pattern = [{"LOWER": "not"}, {"LOWER": "collect"}, {"LOWER": "personal"}, {"LOWER":"information"}]
matcher.add("NOT_COLLECT_PERSONAL_INFO", [pattern])

# 使用spaCy的英文模型处理文本
doc = nlp(text)

# 使用Matcher对象来找到匹配的模式
matches = matcher(doc)

# 打印匹配结果
for match_id, start, end in matches:
    span = doc[start:end]  # 获取匹配的span
    print(span.text)

# 如果需要，可以进一步处理匹配到的span，例如提取实体或执行其他操作