"""
输入一个接口名，得到该接口运行信息的address is 地址值
提示：
每段之间有空行
每段第一个单词是接口名
思路：先通过接口名匹配到段落（空行），再匹配目标地址值
"""
import re
def get_info():
    file = open("log.txt", 'r+')
    #每段文字的提供者
    while True:
        data = ''
        # 再执行，获得下一段代码，open一次，不会从开头读取,从上次位置读取
        for line in file:
            if line =="\n":
                break
            data+=line#data就是空行和空行之间的段落
    #用首单词判断data是不是想要的段落
        #将这段文字以yield的方式提供出去
        if data:
            yield data
        else:#为空，到文件结尾
            file.close()
            return
    #确定段落。匹配地址
def main(port):
    for info in get_info():
        obj=re.match(r"\S+",info)
        if port==obj.group():
            pattern=r"([0-9a-f]{4}\.){2}[0-9a-f]{4}"
            obj=re.search(pattern,info)
            return obj.group()
print(main("BVI1"))








