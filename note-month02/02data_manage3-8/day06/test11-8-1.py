"""
1. 小明家必须要过一座桥。
小明过桥最快要１秒，小明的弟弟最快要３秒，小明的爸爸最快要６秒，小明的妈妈最快要８秒，小明的爷爷最快要１２秒。
每次此桥最多可过两人，而过桥的速度依过桥最慢者而定。
过桥时候是黑夜，所以必须有手电筒，小明家只有一个手电筒，而且手电筒的电池只剩30秒就将耗尽。
小明一家该如何过桥，请写出详细过程。
"""
time_list=[1,3,6,8,12]

def cross_bridge():
    tuple_add = []
    for i in range(len(time_list)-1):
        for k in range(i+1,len(time_list)):
            tuple01=(time_list[i],time_list[k])
            tuple_add.append(tuple01)
        print(tuple_add)
        if time_list[i]<time_list[k]:
            time1=time_list[k]

cross_bridge()



"""
1. 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
1 <= 数组长度 <= 10000

示例:
输入: [0,1,2,3,4,5,6,7,9]
输出: 8
"""
def find_num(list_target):
    for i in range(len(list_target)):
        if i==list_target[i]:
            continue
        else:
            return i
list01=[0,1,2,3,4,5,6,7,9]
res=find_num(list01)
print(res)

