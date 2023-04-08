# python中默认utf-8的编码，所有字符串都是unicode字符串
# 字符串可以使用单引号、双引号和三引号(三个单引号或者三个双引号)
# \  是转义字符  \\可以打出反斜杠符号
# \n换行  \t横向制表符 \v纵向制表符 \r回车    \b退格    \a响铃(系统会响一声)
# len(string)  可以返回字符串长度
# lower()转换字符串中所有大写字母为小写
# upper()转换字符串中所以小写字母为大写
# swapcase()将字符串中大写转换为小写，小写转换为大写
# max(str)返回字符串str中最大的字母
# min(str)返回字符串str中最小的字母
#capitalize()将字符串的第一个字符转换为大写
# bytes.decode(encoding="utf-8",error="strict") python3没有decode的方法，但可以使用bytes对象的decode()方法来解码给定的bytes对象，这个bytes对象可以由石头人。encode()来编码返回
# encode(encoding='UTF-8',errors='strict') 以encoding指定的编码格式编码字符串，如果出错就会默认报一个ValerError的一场，除非errors指定的是’ignore‘或者’replace‘

# 其他的可以上网查”字符串的常见操作“
# 常用的一般都在这里了


word='字符串'
sentence="这是一个句子"#比较建议用双引号
paragraph="""
        这是个段落
            缩进也会一起保存下来
                在三引号里面是什么打出来就是什么
"""
str_1="Cook say:\"Hello World\""#加\转义，这样就可以把句子里面的""给打印出来
print(r"hello\nworld")#前面有一个r (代表raw) 的话后面的内容就会全部保留下来
print(word)
print(sentence)
print(paragraph)
print(str_1)
print(str_1[0:4])#[起始位置:结束位置]&&[起始位置:结束位置:步进值]
print(str_1[0:6:2])#最后一个字符是不会打印出来的
print(str_1+"\"Fuck You World\"")#在str_1后面加上Fuck You World
print(str_1*3)#在后面*一个常数k，就可以重复输出k遍字符串
print("Fuck You \nNvidia")#\n换行符

