"""
输入一个接口名，得到该接口运行信息的address is 地址值
提示：
每段之间有空行
每段第一个单词是接口名
思路：先通过接口名匹配到段落（空行），再匹配目标地址值
"""
import re
file=open("log.txt",'r+')
# data=file.read()

def match_paragraph_by_name(name):
    # name_pubilc=re.findall("^[A-Z]\w+",name)
    ifname = ""
    ipaddr = ""
    for lane in file:
        # print(lane)
        if ifname != "" and lane == "\n":
            #print(ifname)
            break
        if lane == "\n":
            continue
        if ifname == "":
            str = lane.split(' ', 1)[0]
            #print(str)
            if name == str:
                ifname=str
                #print(ifname)
                continue
        else:
            # # 10f3.114b.253a
            # #str_address = re.search(r"(\d+\w+\.){2}(\w+)", lane)
            str_address = re.search("(\d+\w+\.){2}(\w+)", lane)
            #print(str_address)
            #
            if str_address !=None:
                ipaddr = str_address.group()
                break
                #print(ipaddr)
    print(ifname)
    print(ipaddr)
match_paragraph_by_name("tunnel-te11")
