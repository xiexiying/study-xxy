"""
定义函数，参数传入一个单词，返回单词解释
"""
# def find_word(wor):
#
#     list01=[]
#     list02=[]
#     file=open("dict.txt","r")
#     for line in file:
#         word=line[:18].strip('')
#
#         list01.append(word)
#         word_last=line[18:].strip('')
#         list02.append(word_last)
#     for i in range(len(list01)):
#         if wor ==list01[i]:
#             return (list01[i],list02[i])
#
# print(find_word("a"))


def find_w(word):
    file = open("dict.txt", "r")
    for line in file:
        temp=line.split(' ',1)#每次取一个单词  切割一处
        if temp[0]>word:
            break
        elif temp[0]==word:
            return temp[1].strip()#去除两边的空格
print(find_w("a"))



