# namelist = []   定义了一个空的列表
# List(列表)
'''
namelist=["张昕喧","高子婷","刘熠"]
print(namelist[1])#通过修改里面的数字可以打印不同的元素
testlist=[1,"test"]
print(type(testlist[0]))#可以看到打印出来结果，1仍然是一个整型，没有被改变字符类型
print(type(testlist[1]))

for name in namelist:#这样可以打印输出字符串里面的元素
    print(name)

print(len(namelist))#len可以得到列表的长度
length=len(namelist)
i=0
while i<length:#也可以用while
    print(namelist[i])
    i+=1
'''

'''
#增: [append]、[extend]
print("---增加前名单的数据---")
for name in namelist:
    print(name)

nametemp=input("请输入学生的名字：")
print("---增加后名单的数据---")
namelist.append(nametemp)#在原来的列表后面增加一个数(nametemp)里面的东西

for name in namelist:
    print(name)
'''

'''
a=[1,2]
b=[3,4]
a.append(b)
print(a)#会打印一个[1,2[3,4]],这个叫列表的嵌套
a.extend(b)#    entend会将b中的元素注意加到列表a中
print(a)

#增  [insert]    将某个元素插到指定的位置
a=[0,1,2]
a.insert(1,3)       #第一个变量表示将数字插在哪一位，第二个变量表示要插入的变量
print (a)       #打出来是[0,3,1,2]

#删 [del]、[pop]、[remove]
del namelist[2]#在指定位置删除一个元素
namelist.pop()#弹出末尾最后一个元素,()里面不用写东西
namelist.remove(" ")#直接删除掉指定的元素
'''

'''
#改:
namelist_1=["张昕喧","刘熠","高子婷","耿恺婧"]


print("------修改前的元素------")
for name in namelist_1:
    print (name)

print("\n")

print("------第一次修改后的元素------")
namelist_1[1]="文晓茵"#改其中的元素就直接改就可以了
for name in namelist_1:
    print(name)

#查
findName = input("请输入你要查找的名字:")
if findName in namelist_1:
    print("该同学在列表中")
else :
    print("没有找到该同学")
'''

'''
list_1=["a","b","c","d","e","f"]
print(list_1.index("c",0,4))    #[index]可以查找指定下标范围内的元素，并返回找到对应数据的下标
# 如果找不到这个元素就会报错         范围区间[ , )   是左闭右开的
print(list_1.count("a"))    #可以统计某个元素出现了几次
'''

#排序和反转
'''
a=[1,5,3,2,4]
print("排序前：")
print(a)
a.reverse() #可以将列表中所有元素反转
print("翻转后：")
print(a)
a.sort()        #按升序来排序
print(a)
a.sort(reverse=True)#按降序来排---实际上是将升序排好的东西进行翻转
print(a)
'''

#列表的嵌套

schoolname=[["清华大学","北京大学"],["中山大学","华南理工大学"],["华南农业大学","复旦大学"]]
print(schoolname[1][1]) #类似于c语言中的多维数组
