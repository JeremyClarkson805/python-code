#正则表达式的常用操作符(1)-----这些正则表达式在基本全部语言里面都有，而且都是一样的
'''
.   表示单个字符
[]   字符集，对单个字符给出取值范围   [abc]表示a、b、c，[a-z]表示a到z单个字符
[^ ]   非字符集，对单个字符给出排除范围    [^abc]表示非a或b或c的单个字符
*   前一个字符0次或无限次扩展    abc*表示ab abc abcc abccc abccc...等等
+   前一个字符1次或无限次扩展    abc+表示c至少要出现1次
？  前一个字符0次或1次扩展    abc? 表示ab abc
|   左右表达式任意一个    abc|def 表示abc def
'''

#正则表达式的常用操作符(2)
'''
{m}   扩展前一个字符m次    ab{2}c表示abbc
{m,n}   扩展前一个字符m~n次(包含n)    ab{1，2}c 表示abc、abbc
^   匹配字符串开头    ^abc表示abc且在一个字符串的开头
$   匹配字符串结尾    abc$表示abc且在一个字符串的结尾
( )   分组标记，内部只能使用|操作符    (abc)表示abc，(abc|def)表示abc、def
\d   数字，等价于[0,9]
\w   单词字符，等价于[a-Za-a0-9]
'''

# Re库主要功能函数
'''
re.search()   在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
re.match()   从一个字符串的开始位置起匹配正则表达式，返回match对象
re.findall()   搜索字符串，以列表形式返回全部能匹配的子串
re.split()   将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
re.finditer()   搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
re.sub()   在一个字符串中替换所有匹配正则表达式的字串，返回替换后的字符串
'''

import re
'''
#创建模式对象
pat = re.compile("AA")#此处的AA是正则表达式，用来验证其他的字符串
m = pat.search("CBAA")#search字符串是被校验的内容
#也可以这样写(没有模式对象)
m = re.search("asd","Aasd")#前面的字符串是规则(模板)，后面的字符串是被校验的对象
print(m)
#python里面区间左闭右开，他会找出来特定字符串在哪里，如果没有会返回NONE
#而且search找到第一个以后就不会再继续往下找了
'''

# print(re.findall("a","ASDaDFGAa"))      #前面字符串是规则(正则表达式)，后面字符串是被校验的字符串


# m = re.search("abc","ABabc")
# print(m)

# print(re.findall("a","ASDaDEFGAa"))
# #会找出所有符合条件的表达式
# # 前面的规则可以结合上面的正则表达式规则一起来使用
# print(re.findall("[A-Z]","ASDaDEFGAa"))#这个可以找出所有大写字母


#sub(起分隔作用)
print(re.sub("a","A","abcdcasd"))#这个是用A替换掉a---sub
#可以在前面加一个 r ，这样就不用担心转义字符不能被识别的问题
a = r"aa\bb\cc\dd"