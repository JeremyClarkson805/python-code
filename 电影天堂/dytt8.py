import requests
import re
from lxml import etree
import unicodedata
base_url = "https://dy.dytt8.net/html/gndy/dyzz/list_23_1.html"
headers = \
    {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
    }

def main():
    url_1 = "https://dy.dytt8.net/html/gndy/dyzz/list_23_"
    for i in range(1,6):
        url = url_1 + str(i) + ".html"
        Second(url)


def Second(url):
    # tree = etree.parse("./dytt8.html",etree.HTMLParser(encoding='gbk'))
    response = GetFirstHtml(url,headers)
    tree = etree.HTML(response)
    tittle_list = tree.xpath("//div[@class = 'co_content8']//a//text()")

    link_list_1 =tree.xpath("//div[@class = 'co_content8']//a//@href")
    # print(link_list_1)
    url_list = ["https://www.dydytt.net/"+str(i)for i in link_list_1]#将www.dytt加到开头
    del url_list [-8:]#删除倒数八个没用的网址

    fp = open('dytt8.txt','a',encoding='gbk')

    for tittle,url in zip(tittle_list,url_list):
        print("正在收集电影:",tittle,"的信息")
        tittle = str(tittle)
        # fp.write(tittle)
        GetData(url)
        print(tittle,"的信息已保存完毕")
    fp.close()


def GetFirstHtml(url,headers):
    response = requests.get(url = url,headers = headers)
    response.encoding = 'gbk'
    response = response.text
    return response
def GetData(url):
    headers = \
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
        }

    response = requests.get(url=url, headers=headers)
    response.encoding = 'gbk'
    response = response.text

    # tree = etree.parse("./dytt8.html", etree.HTMLParser(encoding='gbk'))

    tree = etree.HTML(response)

    fp = open('dytt8.txt','a',encoding='gbk')

    # print(response)
    # 找出电影的发布时间


    time = tree.xpath("//div[@class = 'co_content8']/ul/text()")[0]
    time = str(time)
    FindTime = re.compile(r'发布时间：..........')
    time = re.findall(FindTime, time)
    print(time)
    # 找出电影的别名
    FindName = re.compile(r'/><br />◎译　　名　(.*?)<br />◎片')
    name = re.findall(FindName, response)
    name = str(name)
    print(name)
    # 找出电影的评分
    FindScore_1 = re.compile(r'<br />◎IMDb评分.(.*?)<br />◎豆瓣评分')
    FindScore_2 = re.compile(r'users<br />◎豆瓣评分.(.*?)users<br />◎片　　长')
    score_1 = re.findall(FindScore_1, response)
    score_2 = re.findall(FindScore_2, response)
    score_1 = str(score_1)
    score_2 = str(score_2)
    print("IMDb评分:", score_1, "豆瓣评分:", score_2)
    # 找出电影的片长
    FindLong = re.compile(r'users<br />◎片　　长　(.*?)<br />◎导　　演')
    long = re.findall(FindLong, response)
    long = str(long)
    print("时长:", long)
    # 找出导演
    FindDirector = re.compile(r'分钟<br />◎导　　演　(.*?)<br />◎编　　剧')
    director = re.findall(FindDirector, response)
    director = str(director)
    director = director.replace('&middot', '')
    print("导演:", director)
    # 找出编剧
    FindWriter = re.compile(r'<br />◎编　　剧　(.*?)<br />.*<br />◎')
    writer = re.findall(FindWriter, response)
    writer = str(writer)
    writer = writer.replace("<br />\u3000\u3000\u3000\u3000\u3000&nbsp", '')
    writer = writer.replace('&nbsp', '').replace('&middot', '')
    # writer = writer.replace('&middot','')
    print("编剧:", writer)
    # 找出演员表
    # FindActor_1 = re.compile(r'<br />◎演　　员　(.*?);(.*?)<br />　　　　　&nbsp;&nbsp;(.*?).*?<br /><br />◎简　　介<br />')
    # FindActor_2 = re.compile(r'>◎编　　剧.*?<br />◎.　　.　(.*?)<br />　　　　&nbsp;&nbsp;　(.*?)<br />.*?<br /><br />◎简　　介')
    # actor_1 = re.findall(FindActor_1,response)
    # actor_2 = re.findall(FindActor_2,response)
    # actor_1 = str(actor_1)
    # actor_2 = str(actor_2)
    # actor_1 = actor_1.replace("&middot",'')
    # actor_1 = actor_1.replace("&middot;", '')
    # actor_2 = actor_2.replace("<br />\u3000\u3000\u3000\u3000\u3000&nbsp",'')
    # actor_2= actor_2.replace(u'\u3000',u' ')
    # actor_2 = actor_2.replace("&middot", '')
    # re.sub('&nbsp','',actor_2)
    # print("演员:",actor_2)

    # 找出下载地址
    FindLink = re.compile(r'<br /><br /><br /><a target="_blank" href=(.*?)><strong><font style="BACKGROUND-COLOR:')
    link = re.findall(FindLink, response)
    link = str(link)
    link = link.replace('<br />', '').replace(U'\u3000', U'')
    print("下载链接:", link)

    # 找出简介
    response = str(response)
    FindIntroduce = re.compile(r'◎简　　介<br />.*?<br />　　(.*?)<br /><br /><br /><a target="_blank"')

    introduce = response.replace(r'\u3000','')
    introduce = re.findall(FindIntroduce, introduce)
    introduce = str(introduce)
    print("简介:", introduce)


    time = str(time)

    fp.write(name)
    fp.write("\n")
    fp.write(time)
    fp.write("\n")
    fp.write("IMDb评分:")
    fp.write(score_1)
    fp.write("\n")
    fp.write("豆瓣评分:")
    fp.write(score_2)
    fp.write("\n")
    fp.write("时长:")
    fp.write(long)
    fp.write("\n")
    fp.write("导演:")
    fp.write(director)
    fp.write("\n")
    fp.write("编剧:")
    fp.write(writer)
    fp.write("\n")
    fp.write("简介:")
    fp.write( introduce)
    fp.write("\n")
    fp.write("下载链接:")
    fp.write(link)
    fp.write("\n")
    fp.write("\n")
    fp.close()


if __name__ == "__main__":
    main()