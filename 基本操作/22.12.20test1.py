'''
sum=0
count=int(input("请问你要从1加到多少:"))
for i in range(1,count+1):#注意,在python里面()是[ , )左闭右开的
    sum+=i
print(sum)
'''

'''
def add_1(a,b):
    sum_1=0
    for i in range(0,a):
        sum_1 += i
        print("第%d次相加的结果是%d:"%(i+1,sum_1))
        #在print中输出多个变量的方法:
        #print("变量a,变量b"%(nane_a,name_b))
        
add_1(3,2)
'''
'''
def add_1(j,k):
    list_1 = [31,29,31]
    sum=0
    for i in range(0,j-1):#[0,3)---0,1,2
        sum += list_1[i]
    print(sum+k)
    return(sum+k)

add_1(3,2)
'''


def add_1(j, k):  # 闰年计算
    sum = 0
    monlist_1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(0, j - 1):
        sum += monlist_1[i]
    return (sum + k)


def add_2(j, k):  # 平常年计算
    sum = 0
    monlist_2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(0, j - 1):
        sum += monlist_2[i]
    return (sum + k)


def judge(j):
    if j % 4 == 0 and j % 100 != 0:
        print("%d年是闰年" % j)
        return (1)
    elif j % 4 != 0 or type(j % 100) == int:
        print("%d年不是闰年" % j)
        return (2)

def sum_1(a, b):
    sum = 0
    for i in range(a + 1, b):
        print(i)
        if judge(i) == 1:
            sum += 366
        if judge(i) == 2:
            sum += 365
    return (sum)

def sum_2(a,b,c):#a,b,c分别对应传进来的 年,月,日
    jud=0;sum=0
    jud=judge(a)
    if jud==1:
        sum=add_1(b,c)
        print(sum)
    elif jud==2:
        sum=add_2(b,c)
        print(sum)
    return(sum)

def sum_3(a,b,c):
    jud=0;sum=0
    jud=judge(a)
    if jud==1:
        sum=366 - sum_2(a,b,c)
    if jud==2:
        sum=365 - sum_2(a,b,c)
    return(sum)


jud = 0;
Day = Day_2 = Day_3 = 0
days_1 = {"year": 2020, "month": 10, "day": 1}  # print(type(days_1["year"]))#---type(int)
days_2 = {"year": 2025, "month": 10, "day": 1}

Day_2 = sum_1(days_1["year"], days_2["year"])
'''
jud=judge(days_1["year"])
if jud==1:
    Day_1 = 366 - sum_2(days_1["year"],days_1["month"],days_1["day"])
elif jud==2:
    Day_1 = 365 - sum_2(days_1["year"],days_1["month"],days_1["day"])
'''
Day_1=sum_3(days_1["year"],days_1["month"],days_1["day"])
Day_3 = sum_2(days_2["year"],days_2["month"],days_2["day"])
Day = Day_1 + Day_2 + Day_3
print(Day)

'''
for i in range(days_1["year"]+1,days_2["year"]):#计算两个年份中间年的总天数
    print(i)
    jud=judge(i)
    if jud==1:
        sum += 366
    elif jud==2:
        sum += 365
print(sum)
'''
