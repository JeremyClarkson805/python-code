def add_1(j, k):  # 闰年计算
    sum = 0
    monlist_1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(0, j - 1):
        sum += monlist_1[i]
    return (sum + k)
    # print(sum+k)

def add_2(j, k):  # 平常年计算
    sum = 0
    monlist_2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(0, j - 1):
        sum += monlist_2[i]
    return (sum + k)
    # print(sum+k)

def judge(j):
    if j % 4 == 0 and j % 100 != 0:
        # print("%d年是闰年"%j)
        return (1)
    elif j % 4 != 0 or type(j % 100) == int:
        # print("%d年不是闰年" % j)
        return (2)
    # elif---是如果前面的if符合条件的话后面的就不会再执行了
    # if则会遍历if语句

def sum_1(a, b):
    sum = 0
    for i in range(a + 1, b):
        # print(i)
        if judge(i) == 1:
            sum += 366
        if judge(i) == 2:
            sum += 365
    if a == b:
        return 0
    else:
        return sum


def sum_2(a, b, c):  # a,b,c分别对应传进来的 年,月,日
    jud = 0;
    sum = 0  # return这一天是这一年的第几天
    jud = judge(a)
    if jud == 1:
        sum = add_1(b, c)
        # print(sum)
    elif jud == 2:
        sum = add_2(b, c)
        # print(sum)
    return (sum)


def sum_3(a, b, c):  # 算Day_1
    jud = 0;
    sum = 0
    jud = judge(a)
    if jud == 1:
        sum = 366 - sum_2(a, b, c)
    if jud == 2:
        sum = 365 - sum_2(a, b, c)
    return sum

Day = jud = jud_2 = day_2 = day_1 = day_3 = 0
days_1 = {"year": 2003, "month": 8, "days": 5}
days_2 = {"year": 2002, "month": 9, "days": 13}
jud_2 = int(input("计算某个日期是今年的第几天输入1\n计算两个日期相差多少天输入2\n请输入:"))
if jud_2 == 1:
    a, b, c = map(int, input("请输入年,月,日,中间用空格隔开:").split())
    # print("%d %d %d"%(a,b,c))
    Day = sum_2(a, b, c)
    print(Day)
elif jud_2 == 2:
    days_1["year"], days_1["month"], days_1["days"] = map(int,
                                                          input("请输入日期一的 年,月,日,中间用空格隔开:").split())
    days_2["year"], days_2["month"], days_2["days"] = map(int,
                                                          input("请输入日期二的 年,月,日,中间用空格隔开:").split())
    Day = sum_3(days_1["year"], days_1["month"], days_1["days"]) + sum_2(days_2["year"], days_2["month"],days_2["days"]) + sum_1(days_1["year"],days_2["year"])
    if days_1["year"] == days_2["year"] :
        Day=sum_2(days_2["year"], days_2["month"],days_2["days"])-sum_2(days_1["year"], days_1["month"], days_1["days"])
    print("%d.%d.%d与%d.%d.%d相差%d天" % (
        days_1["year"], days_1["month"], days_1["days"], days_2["year"], days_2["month"], days_2["days"], Day))

