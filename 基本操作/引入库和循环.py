'''
if True:    #这里的True首字母必须大写
    print("true")#python是用缩进来区分函数作用范围的，因此同一个条件下的语句缩进必须一样
else:            #所以建议直接用键盘上的tab键
    print("False")
'''

'''
score=int(input("请输入你的分数："))
if score>=90 and score <= 100:
    print("本次考试等级为A")
elif score>=70 and score<80:
    print("完蛋了！这次考试等级为B")
else:
    print("哟西")
'''

'''
导入模块
在python用import或from...import来引入相应的模块
将整个模块导入，格式为:import someodule
从某个模块中导入某个函数，格式为：from someodule import somefunction
从某个模块中导入多个函数，格式为：from someodule import firstfunc,secondfunc,whirdfunc
将某个模块中的全部函数导入，格式为：from somemodule import\*
'''

'''
循环 1.for...in
例如：for...in range()
for x in range(10):   #是从0开始的10个数
    print(x)    #这个会打印0~9的10个数字

for x in range(0,9,3):  #从0开始，步进为3，不能取到等于9
    print(x)
'''

# name="fuck you world"
# for x in name:  #这个是python独有的玩法
#     print(x,end="\t")

# a=["aa","bb","cc","dd"]
# for i in range(len(a)):
#     print(i,a[i])

'''
i=0
while i<5:
    print("当前是第%d次循环"%(i+1))
    print("i=%d"%i)
    i+=1
'''

'''
# 1~100的求和
用while循环
i=1
sum=0
while i<=100:
    sum=sum+i
    print("这是第%d次相加"%(i+1))
    i+=1
print(sum)
用for循环
i=1
sum=0
print(type(sum))
for i in range(101):
    sum=sum+i
print("第%d次相加的和是%d"%(i,sum))
'''