'''
'r' 以只读方式打开文件,文件的指针会在开头
'rb'以二进制打开一个文件只用于读取
'w' 打开一个文件只用于写入.如果该文件已存在则会将其覆盖.如果该文件不存在就会新建一个文件
'a' 打开一个文件用于追加.如果该文件已存在文件指针会在文件的的末尾
    如果文件不存在回新建文件进行写入
'''

'''
f = open ("test1.txt","w")
f.write("FUCK YOU NVIDIA!!!\nAPPLE YYDS!!!\n")
f.close()

'''
f = open("test1.txt","r")
# content_1 = f.read(8)#表示读取五个字符
# content_2 = f.readline()#表示读取一行---这里没有s
# 没有s的readline每次只读一行
# content_3 = f.read(11)
# read方法可以读取指定的字符，开始时定位在头部，每执行一次向后移动指定字符数
# 读完全部可以直接输入整个文件的大小
content_4 = f.readlines()#这样会将整个文件都读进来变成列表,每行为一个元素
# print(content_1)
# print(content_2)
# print(content_3)
# print(content_4)
i=1
for temp in content_4:
    print("%d:%s"%(i,temp))
    i += 1


f.close()

import os
'''
os.rename()
rename("A","B")   A为原文件名，B为更改后的文件名
os.rmdir("A")删除文件夹
os.listdir("./")获取目录列表
'''
