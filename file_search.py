def search(path):
    import os
    files=os.listdir(path)
    file_dict=dict()
    for file in files:
        if os.path.isdir(file):
            file_dict.setdefault('文件夹',0)
            file_dict['文件夹']+=1
        else:
            ext=os.path.splitext(file)[1]
            file_dict.setdefault(ext,0)
            file_dict[ext]+=1
    for each_type in file_dict.keys():
        print('%s下共有类型为%s的文件%d个'%(path,each_type,file_dict[each_type]))
path=input('请输入路径:')
search(path)
    
