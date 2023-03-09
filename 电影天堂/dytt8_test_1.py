import requests
from lxml import etree
import re

url = "https://www.dydytt.net/html/gndy/dyzz/20230205/63396.html"
def main():
    headers = \
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
        }



    response = requests.get(url = url,headers = headers)
    response.encoding = 'gbk'
    response = response.text

    # tree = etree.parse("./dytt8.html", etree.HTMLParser(encoding='gbk'))


    tree = etree.HTML(response)
    introduce = tree.xpath('//div[ @class = "contain"]//br//text()')
    print(response)
    # 找出电影的发布时间
    time = tree.xpath("//div[@class = 'co_content8']/ul/text()")[0]
    time = str(time)
    FindTime = re.compile(r'发布时间：..........')
    time = re.findall(FindTime,time)
    print(time)
    #找出电影的别名
    FindName = re.compile(r'/><br />◎译　　名　(.*?)<br />◎片')
    name = re.findall(FindName,response)
    print(name)
    #找出电影的评分
    FindScore_1 = re.compile(r'<br />◎IMDb评分.(.*?)<br />◎豆瓣评分')
    FindScore_2 = re.compile(r'users<br />◎豆瓣评分.(.*?)users<br />◎片　　长')
    score_1 = re.findall(FindScore_1,response)
    score_2 = re.findall(FindScore_2,response)
    print("IMDb评分:",score_1,"豆瓣评分:",score_2)
    #找出电影的片长
    FindLong = re.compile(r'users<br />◎片　　长　(.*?)<br />◎导　　演')
    long = re.findall(FindLong,response)
    print("时长:",long)
    #找出导演
    FindDirector = re.compile(r'分钟<br />◎导　　演　(.*?)<br />◎编　　剧')
    director = re.findall(FindDirector,response)
    director = str(director)
    director = director.replace('&middot','')
    print("导演:",director)
    #找出编剧
    FindWriter = re.compile(r'<br />◎编　　剧　(.*?)<br />.*<br />◎')
    writer = re.findall(FindWriter,response)
    writer = str(writer)
    writer = writer.replace("<br />\u3000\u3000\u3000\u3000\u3000&nbsp",'')
    writer = writer.replace('&nbsp','').replace('&middot','')
    # writer = writer.replace('&middot','')
    print("编剧:",writer)
    #找出演员表
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
    #找出简介
    # FindIntroduce = re.compile(r'◎简　　介<br />.*?<br />　　(.*?)<br /><br /><br /><a target="_blank"')
    # introduce = re.findall(FindIntroduce,response)
    # print("简介:",introduce)
    # introduce = tree.xpath('//div[ @class = "contain"]//br//text()')
    print(introduce)

    #找出下载地址
    FindLink = re.compile(r'<br /><br /><br /><a target="_blank" href=(.*?)><strong><font style="BACKGROUND-COLOR:')
    link = re.findall(FindLink,response)
    print("下载链接:",link)
    information = dict();
    information['time'] = time
    information['name'] = name
    information['score_1'] = score_1
    information['score_2'] = score_2
    information['long'] = long
    information['director'] = director
    information['writer'] = writer
    # information['actor_1'] = actor_1
    # information['actor_2'] = actor_2
    information['introduce'] = introduce
    information['link'] = link
    return information

if __name__ == "__main__":
    main()

