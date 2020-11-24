
# import re
# str01="小米： 18 今年 2020"
# res=re.findall("[0-9]+",str01)
# print(res)#['18', '2020']

import re
str01="温度： -18 今年 330米"
res=re.findall("-?[0-9]+",str01)#匹配整数(负数、正数)
print(res)#['18', '2020']