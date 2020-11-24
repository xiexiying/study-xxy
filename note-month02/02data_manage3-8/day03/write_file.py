# file=open("myfile.py","w")
# file.write("hello world\n")
# n=file.writelines(["hell0 world\n","hell0 world\n","hell0 world\n"])
# print(n)

with open("myfile.py") as f:
    data=f.read()
    print(data)