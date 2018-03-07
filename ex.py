def compare(file1,file2):
    f1=open(file1)
    f2=open(file2)
    count=0
    differ=[]
    for line1 in f1:
        line2=f2.readline()
        count+=1
        if line1!=line2:
            differ.append(count)
    f1.close()
    f2.close()
    return differ
file1=input('请输入文件名:')
file2=input('请输入另一个文件名:')
differ=compare(file1,file2)
print('两文件共有%d处不同'%len(differ))
for each in differ:
    print('第%d处不同'%each)

    
