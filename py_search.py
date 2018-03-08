list1=[]
def search_py(path):
    import os
    files=os.listdir(path)
    for file in files:
        filename=os.path.join(path,file)
        if os.path.isdir(filename):
            search_py(filename)
        else:
            ext=os.path.splitext(file)[1]
            if ext.upper()=='.PY':
                list1.append(filename)
path=input('请输入路径:')
search_py(path)
print('在%s及其子文件夹下共找到%d个.py文件\n分别为:'%(path,len(list1)))
for each in list1:
    print(each+'\n')
