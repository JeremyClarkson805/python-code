import bs4
from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3
'''
bs4主要用于网页解析，用于获取数据
re正则表达式，进行文字匹配
urllib可以制定URL,获取网页数据
xlwt用于进行excel操作
sqlite3可以进行SQLite数据库操作
'''

#影片详情的规则(正则表达式)
findLink = re.compile(r'<a href="(.*?)">')#compile---创建正则表达式，表示了一种规则
#影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)#re.S(大写的S)---表示忽略换行符，让换行符包含在字符中
#影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
#影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)

def main():
    baseurl = "https://movie.douban.com/top250?start="
    #1.爬取网页
    datalist = getData(baseurl)
    savepath = "豆瓣电影TOP250_2.xls"
    #3.保存数据
    saveData(datalist,savepath)

    askURL("https://movie.douban.com/top250?start=")

#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):   #调用获取页面信息的函数10次
        url = baseurl + str(i*25)
        html = askURL(url)#保存获取到的页面源码

        #2.逐一解析数据

        soup = BeautifulSoup(html,"html.parser")
        #html为页面内容，html.parser是一种页面解析器
        for item in soup.find_all('div',class_="item"):#查找符合内容的字符串，并形成列表
            # print(item)   ---测试：查看电影item全部信息
            data = []#保存一部电影的所有信息
            item = str(item)#将item保存成字符串

            #接着用正则表达式来查找指定的字符串
            link = re.findall(findLink,item)[0]
            #[0]  是指在for遍历时，要两个同样的link当中的第一个
            # print(link)#输出影片详情的链接
            data.append(link)       #添加链接
            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)     #添加图片
            titles = re.findall(findTitle,item)#片名可能只有一个中文名，没有外国名
            if (len(titles)==2):
                ctitle = titles[0]
                data.append(ctitle)         #添加中文名
                otitle = titles[1].replace("/","")#去掉无关的符号
                data.append(otitle)     #添加外国名
            else:           #只有中文名的情况
                data.append(titles[0])
                data.append(' ')#外国名字留空
            rating = re.findall(findRating,item)[0]
            data.append(rating)#添加评分
            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)#添加评价人数
            inq = re.findall(findInq,item)#可能会没有评价，因此去掉[0]
            if len(inq)!=0:
                inq = inq[0].replace("。","")#去掉句号
                data.append(inq)#添加概述
            else:
                data.append(" ")#同上面一样没有就留空
            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)#去掉<br/>
            bd = re.sub('/'," ",bd)     #替换/
            data.append(bd.strip())     #去掉前后的空格

            datalist.append(data)   #把处理好的一部电影的信息放进datalist

    # print(datalist)
    return datalist


#得到指定一个URL的网页内容
def askURL(url):
    head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"}
    #这里用的是一个字典
    #head---用户代理，用于告诉豆瓣服务器我们是什么类型的机器
    #本质上是告诉服务器我们可以接受什么水平的文件
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html


#保存数据
def saveData(datalist,savepath):
    print("saving......")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建wordbook表
    sheet = book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)
    col = ("电影详情链接","图片链接","影片中文名","影片外国名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])#列名
    for i in range(0,250):
        print("正在写入第%d条"%i)
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])

    book.save(savepath)


if __name__ == "__main__":
    main()