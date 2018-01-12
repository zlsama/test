file=input('请输入文件名:')
num=input('请输入要打印的行数:')
l=len(num)
f=open(file)
lines=f.readlines()
count=len(lines)
if num.isdigit():
    i=int(num)
    print(lines[i-1])
elif num[0]==':':
    a=int(num.strip(':'))
    for each in range(0,a):
        print(lines[each])
elif num[l-1]==':' :
    b=int(num.strip(':'))
    for each in range(b-1,count):
        print(lines[each])
else:
    list1=num.split(':')
    c=int(list1[0])
    d=int(list1[1])
    for each in range(c-1,d):
        print(lines[each])
f.close()

    
    
    
