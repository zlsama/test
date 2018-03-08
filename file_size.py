import os
file_size=dict()
path=input('请输入路径;')
files=os.listdir(path)
for file in files:
    file1=os.path.join(path,file)
    if os.path.isfile(file1):
        size=os.path.getsize(file1)
        file_size.setdefault(file1,size)
    
print('%s中共有%d个文件'%(path,len(file_size)))
for each in file_size.keys():
    print('%s大小为%d'%(each,file_size[each]))

    


          
        

