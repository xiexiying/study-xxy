import re
s="""Hello 
北京"""
res=re.findall("^\w+",s,flags=re.M)
print(res)#['Hello', '北京']