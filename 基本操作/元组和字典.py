#Tuple
'''
tuple与list类似，不同之处在于tuple的元素不能修改
tuple卸载小括号里，元素之间用逗号隔开
元组的元素不可变，但可以包含可变对象，如list
定义只有一个元素的tuple，必须加逗号
'''

'''
tup_1=("abc","def","ghi")#创建了一个新的元组
tup_2=(50,)#注意后面加逗号，如果不加逗号的话会变成整形而非元组
print(type(tup_1))
print(tup_1[1])#也可以进行切片等操作
print(tup_1[-1])#-1的话会把最后一个打出来
'''


dict#字典
'''
字典是无需的对象集合，使用键-值(key-value)储存，具有极快的查找速度
键(key)必须使用不可变类型
同一个字典中，键(key)必须是唯一的
'''

'''
info={"name":"张昕喧","age":"18"}
print(info["name"])
print(info["age"])
#如果访问了一个不存在的数据(键)，就会报错
# print(info["high"])   就像这样会报错
print(info.get("high")) #如果没找到的话就会返回一个none
print(info.get("high","m"))#如果没找到的话可以给他设定一个返回值
'''
#info={"name":"高子婷","count":"2708"}
#增
'''
new_age=input("请输入年龄:")
info["AGE"]=new_age
print(info["AGE"])
'''

#删(del) (clear)
'''
print("删除前:%s"%info)#打印删除前的字典
del info["name"]#[del]是删除某一个东西
print(info.get("name"))#这样就把name和她后面的名字(高子婷)给删掉了
print("删除后:%s"%info)#打印删除后的字典

info.clear()#clear会把整个字典清空
print("清空后:%s"%info)
'''

#改
'''
info["count"]=2709
print(info["count"])
'''

#查
info={"ID":2701,"NAME":"吴桂熠","AGE":18}
print(info.keys())      #可以得到全部的键(列表)
print(info.values())    #可以得到所有的值(列表)
print(info.items())     #可以得到所有的项(列表)，每个键值对是一个元组
print("\n")
#遍历所有的键
for key in info.keys():
    print(key)
#遍历所有的值
for values in info.values():
    print(values)
print("\n")
#python的独特的for循环用法:
for key,values in info.items():
    print("key=%s,values=%s"%(key,values))