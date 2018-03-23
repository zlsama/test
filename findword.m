clear
clc
[FileName,PathName,FilterIndex] = uigetfile('*.xlsx','选择一个文件');%获取文件信息
if FilterIndex
    f=fopen(strcat(PathName,FileName),'r');
[data,str1]=xlsread([PathName,FileName]);%读取xls文件
 str1=reshape(str1,1,[]);
fclose(f);
 str=inputdlg('请输入要统计的词','对话框',1);%输入关键词

   k=strfind(str1,str);
    k=cell2mat(k);
   k=length(k)                                       
 msgbox(sprintf('文件中共出现%d次%s',k,str{:}));

end



                        
