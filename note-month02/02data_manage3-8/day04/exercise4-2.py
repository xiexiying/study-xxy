"""
在一串英文字符串中，匹配出所有以大写开头的单词

"""
import re
str_01="How are you Jame I"
res=re.findall("[A-Z][a-z]*",str_01)
print(res)#['How', 'Jame']
