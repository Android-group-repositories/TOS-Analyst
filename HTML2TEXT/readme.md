## 代码功能为 web -> html -> text -> paragraph 的提取

```ps1

# 爬取html
#python 1_Web2Html.py -n sentry -u https://sentry.io/terms/

# 对html处理成Excel
python 2_Html2Text.py -n sentry
python 3_Text2Paragraph.py -n sentry
cd .\paragraphs
python 2excel.py
cd ..

```