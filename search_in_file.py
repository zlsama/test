import os
def find_repeat(source,elmt): # The source may be a list or string.
        elmt_index=[]
        s_index = 0;e_index = len(source)
        while(s_index < e_index):
                try:
                    temp = source.index(elmt,s_index,e_index)
                    elmt_index.append(temp)
                    s_index = temp + 1
                except ValueError:
                    break
        return elmt_index
def search_in_file(start_dir,target):
    files=os.listdir(os.chdir(start_dir))
    for file in files:
        if os.path.isfile(file):
            ext=os.path.splitext(file)[1]
            if ext=='.txt':
                f = open(file,"r",encoding="gbk")
                lines=f.readlines()
                for line in lines:
                    if target in line:
                        list1=find_repeat(line,target)
                        for each in list1:
                            print('%s出现在%s的%s行的%d处'%(target,os.getcwd()+os.path.sep+file,lines.index(line)+1,each+1))           
        elif os.path.isdir(file):
            search_in_file(file,target)
            os.chdir(os.pardir)
start_dir=input('请输入待查找的初始目录:')
target=input('请输入需要查找的关键字:')
search_in_file(start_dir,target)



                        
                
