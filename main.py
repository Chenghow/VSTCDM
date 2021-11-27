#需要的库
import requests
from pikepdf import Pdf
#说明
print("请在脚本同一目录下编辑list.txt文件\n格式：班别(文件名)+姓名+身份证号，一行一组")
print("信息不匹配将无法输出，并在同一目录下生成error.txt名单\n仅对广东省注册志愿者有效\n\n")
print("正在执行脚本...\n\n")
#列表处理
list=[]                                                 #初始化二维列表
with open("list.txt", "r", encoding="utf-8") as f:      
    for line in f.readlines():                          #依次读取每行  
        if line.startswith('#') is False:
            line = line.strip()                             #去掉每行头尾空白  
            arr=[s for s in line.split()]                   #添加至一维列表
            list.append(arr.copy())                         #开始组成二维列表
            if len(arr)/3-len(arr)//3!=0:                   #判断一维列表的合法性
                arr.clear()
                print("输入格式错误")
                break
#初始化error_list.txt
newfile=open("error_list.txt", "w+",encoding="utf-8")
newfile.close()
#刷新url与下载
for i in list:                                          #循环更新url
    url="https://www.gdzyz.cn/srvpg/downloadCertificateFromBD?idcardCode="+i[2]+"&userName="+i[1]
    r = requests.get(url) 
    if len(r.text) == 0:                                #判断响应文本是否为空
        errorlist = "\t".join(i)+"\n"                 #将一维列表写入字符串
        with open("error_list.txt", "a+",encoding="utf-8") as error:    #储存错误的名单
            error.write(errorlist)
    else:
        with open(i[0]+"-"+i[1]+".pdf", "wb") as pdf:    #储存
            pdf.write(r.content)
        origin = Pdf.open(i[0]+"-"+i[1]+".pdf")
        dst = Pdf.new()
        dst.pages.append(origin.pages[0])
        save_name=i[0]+"-"+i[1]+".pdf"
        dst.save(save_name)
#数error.txt的行数，统计错误
count = -1
for count, line in enumerate(open("error_list.txt", "r",encoding="utf-8")):
    pass
count += 1

print("输出完成,共%d个错误,请查收生成的文件"%count)
input("按回车退出")
