import os
def search_file(start_dir,target):
    path=os.chdir(start_dir)
    files=os.listdir(os.curdir)
    for file in files:
        if os.path.isfile(file):
            if file == target:
                print(os.getcwd()+os.path.sep+file)
        elif os.path.isdir(file):
            search_file(file,target)
            os.chdir(os.pardir)

start_dir=input('请输入待查找的初始目录:')
target=input('请输入需要查找的目标文件:')
search_file(start_dir,target)
  
                
        
