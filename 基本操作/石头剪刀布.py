import random     #输入0~2的一个数字，与系统随机生成的数字比较后给出结果
x=random.randint(0,2)     #剪刀（0）石头（1）布（2）
i=int(input("剪刀请输入0，石头请输入1，布请输入2\n请输入："))
if x==0:
    print("电脑出了剪刀")
elif x==1:
    print("电脑出了石头")
elif x==2:
    print("电脑出了布")
if i-x==1:
    print("恭喜你赢啦!!!!!!")
elif i-x!=1:
    print("没想到吧！！！你被我打败啦！")