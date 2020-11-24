"""
正则表达式 re
"""
import re

# 目标字符串
s = "Alex:1998,Tom:1996"
pattern = r"(\w+):(\d+)"

# 使用## 替换 \W+ 匹配到的内容
result = re.sub(r"\W+","##",s,2)
print(result)

# 按照正则表达式匹配内容，切割字符串
# list_ = re.split(r"\W+",s,2)
# print(list_)

# 如果正则表达式有子组，则只能返回子组对应的部分
# result = re.findall(pattern,s)
# print(result)





