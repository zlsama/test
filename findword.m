clear
clc
[FileName,PathName,FilterIndex] = uigetfile('*.xlsx','ѡ��һ���ļ�');%��ȡ�ļ���Ϣ
if FilterIndex
    f=fopen(strcat(PathName,FileName),'r');
[data,str1]=xlsread([PathName,FileName]);%��ȡxls�ļ�
 str1=reshape(str1,1,[]);
fclose(f);
 str=inputdlg('������Ҫͳ�ƵĴ�','�Ի���',1);%����ؼ���

   k=strfind(str1,str);
    k=cell2mat(k);
   k=length(k)                                       
 msgbox(sprintf('�ļ��й�����%d��%s',k,str{:}));

end



                        
