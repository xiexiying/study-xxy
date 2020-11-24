file=open("myfile.py",'wb',buffering=10)
while True:
    msg=input("~~")
    file.write(msg.encode())
    file.flush()
file.close()