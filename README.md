# TOS-Analyst


TOS-Analyst powered by llm

## Analyst core 使用

代码内使用相对路径在当前目录打开终端

然后切换到对应part的目录内

```powershell
(base) > cd '.\`[1`]Tos2PP\'
(base) [1]Tos2PP> .\run.ps1
```

不同的脚本用 run.ps1 来组织

run.ps1内容

```powershell
python "./[1]读Excel到inputSentence.py" 初始化  不涉及gpt
python "./[2]P1_P2.py"                  prompt1+prompt2 输出在P1 P2文件夹
python "./[3]P3.py"                     prompt3 输出在P3文件夹
python "./[4]整理P3out为Excel.py"       结果整理，不涉及gpt
```