def printout(filename,num):
    file=open(filename)
    num=int(num)
    for i in range(num):
        print(file.readline())
    file.close()
filename=input('请输入文件名:')
num=input('请输入需要打印的行数:')
printout(filename,num)
        
