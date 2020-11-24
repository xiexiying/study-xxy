#!/usr/bin/python3
list_res=[1]
for i in range (2,10000):
    for k in range (2,i):
        if i%k==0:
            break
    else:
        list_res.append(i)
print(sum(list_res))

