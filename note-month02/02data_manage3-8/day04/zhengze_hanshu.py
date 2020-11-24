#---------------------finditer----------
# import re
# s="ddd:222,fff:777"
# pattern=r"(\w+):(\d+)"
# res=re.finditer(pattern,s)
# for i in res:
#     #迭代结果是每处匹配的内容对象
#     print(i.group())#获取匹配到的内容
#     print(i.span())#匹配到内容对应位置
#---------------------match------------
# import re
# s="ddd:222,fff:777"
# pattern=r"(\w+):(\d+)"
# res1=re.match(pattern,s)#只匹配目标字符串开头位置，相当于^，匹配不到会报错
# print(res1.group(1))#group括号内参数可以是数字表示第几个子组，也可以是组名，不填，默认全部
#----------------------search----------
import re
s="ddd:222,fff:777"
pattern=r"(?P<name>\w+):(\d+)"#子组名称需要有
res1=re.search(pattern,s)#
print(res1.group(1))#
print(res1.groupdict())#按子组名字生成字典
