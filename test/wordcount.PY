import xlrd
def strs(row):
    values = "";
    for i in range(len(row)):
        if i == len(row) - 1:
            values = values + str(row[i])
        else:
            values = values + str(row[i]) + ","
    return values
 
# 打开文件
data = xlrd.open_workbook("4.xlsx")
sqlfile = open("3.txt", "a",encoding='utf-8') # 文件读写方式是追加
 
table = data.sheets()[0] # 表头
nrows = table.nrows  # 行数
ncols = table.ncols  # 列数
colnames = table.row_values(0)  # 某一行数据
# 打印出行数列数
#print(nrows)
#print(ncols)
#print(colnames)
for ronum in range(1, nrows):
    row = table.row_values(ronum)
    values = strs(row) # 调用函数，将行数据拼接成字符串
    
    sqlfile.writelines(values + "\r") #将字符串写入新文件
sqlfile.close() # 关闭写入的文件

def file_find(file_name,word):
	f_read=open(file_name,encoding='utf-8')
	content=[]
	count=0
	sum=0
	for eachline in f_read:
		if word in eachline:
			count=eachline.count(word)
			sum+=count
		content.append(eachline)
	decide=input('\n文件%s中共出现%s次【%s】'%(file_name,sum,word))
	f_write=open(file_name,'wb',encoding='utf-8')
	f_write.writelines(content)                                                                        
	f_write.close()
	f_read.close()
file_name=input('请输入文件名:')
word=input("请输入需要查找的单词或字符:")
file_find(file_name,word)
