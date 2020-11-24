"""
正则表达式 re 2
"""
import re

# 目标字符串
s = "    Alex:1998,Tom:1996"
pattern = r"(?P<name>\w+):(\d+)"

# 匹配第一处符合条件的内容
result = re.search(pattern,s)
print(result.group())
print(result.groupdict()) # 捕获组字典 {组名：组对应内容}

# 只匹配目标字符串开头位置
# result = re.match(pattern,s)
# print(result.group())
# print(result.group(2)) # 根据组序号获取内容
# print(result.group('name')) # 根据组名获取内容


# 得到匹配后的迭代对象
# result = re.finditer(pattern,s)
# for i in result:
#     # 迭代得到的结果是每处匹配内容对应的match对象 -》 i
#     print(i.group()) # 获取匹配到的内容
#     print(i.span()) # 匹配到的内容对应的位置






