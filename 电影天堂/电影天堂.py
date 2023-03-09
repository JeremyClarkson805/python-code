import requests
from lxml import etree
import re
import os
headers = \
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
        }

def main():
    base_url = "https://dy.dytt8.net/html/gndy/dyzz/20230215/63427.html"
    for i in range(1,101):
        page_url = "https://dy.dytt8.net/html/gndy/dyzz/list_23_" + str(i) + ".html"
        page_url = str(page_url)
        print(page_url)
        url_list = Geturl(page_url,headers)
        for page_url in url_list:
            Getpagedata(page_url,headers)

    # Getpagedata()

def Getpagedata(url,headers):

    paris = requests.get(url=url, headers=headers)
    paris.encoding = 'gbk'
    paris = paris.text
    # print(paris)
    # print("\n\n")

    #查找译名
    Findname_1= re.compile(r'◎译　　名　(.*?)<br />◎片　　名')
    name_1 = re.findall(Findname_1,paris)
    name_1 = str(name_1)
    # print("译名:",name_1)

    #查找片名
    Findname_2 = re.compile(r'◎片　　名　(.*?)<br />◎年　　代')
    name_2 = re.findall(Findname_2,paris)
    name_2 = str(name_2)
    # print("片名:",name_2)

    #查找年代
    Findtime = re.compile(r'◎年　　代　(.*?)<br />◎产　　地')
    time_1 = re.findall(Findtime,paris)
    time_1 = str(time_1)
    # print("年代:",time_1)

    #查找产地
    Findplace = re.compile(r'◎产　　地　(.*?)<br />◎类　　别')
    place = re.findall(Findplace,paris)
    place = str(place)
    # print("产地:",place)

    #查找类别
    Findtype = re.compile(r'◎类　　别　(.*?)<br />◎语　　言')
    type = re.findall(Findtype,paris)
    type = str(type)
    # print("类别:",type)

    #查找语言
    Findlanguage_1 = re.compile(r'◎语　　言　(.*?)<br />◎字　　幕')
    language_1 = re.findall(Findlanguage_1, paris)
    language_1 = str(language_1)
    # print("语言:", language_1)

    #查找字幕语言
    Findlanguage_2 = re.compile(r'◎字　　幕　(.*?)<br />◎上映日期')
    language_2 = re.findall(Findlanguage_2,paris)
    language_2 = str(language_2)
    # print("字幕:",language_2)

    #查找上映日期
    Findtime_2 = re.compile(r'◎上映日期　(.*?)<br />◎IMDb评分')
    time_2 = re.findall(Findtime_2,paris)
    time_2= str(time_2)
    # print("上映日期:",time_2)

    #查找评分
    FindIMDB = re.compile(r'◎IMDb评分(.*?)<br />◎豆瓣评分')
    idmb = re.findall(FindIMDB,paris)
    idmb = str(idmb)
    idmb = idmb.replace(r'\u3000','')
    Finddouban = re.compile(r'◎豆瓣评分　(.*?)<br />◎片　　长')
    douban = re.findall(Finddouban,paris)
    douban = str(douban)
    # print("IDMB评分:",idmb,"\n","豆瓣评分:",douban)

    #查找电影片长
    Findlong = re.compile(r'◎片　　长　(.*?)<br />◎导　　演')
    long = re.findall(Findlong,paris)
    long = str(long)
    # print("时长:",long)

    #查找导演
    Finddirector =re.compile(r'◎导　　演　(.*?)<br />◎编　　剧')
    director = re.findall(Finddirector,paris)
    director = str(director)
    director = director.replace('&middot;','·').replace('&','').replace('uml;','').replace('edil;','')
    # print("导演:",director)

    #查找编剧
    Findwriter = re.compile(r'◎编　　剧　(.*?)<br />.*?/>◎简　　介')
    writer = re.findall(Findwriter,paris)
    writer = str(writer)
    writer = writer.replace('&middot;','·')
    # print("编剧:",writer)

    #查找演员
    Findactor_1 = re.compile(r'◎演　　员　(.*?)<br />.*?(.*?)<br />◎简　　介')
    actor_1 = re.findall(Findactor_1,paris)
    Findactor_2 = re.compile(r'◎主　　演　(.*?)<br />.*?(.*?)<br />◎简　　介')
    actor_2 = re.findall(Findactor_2,paris)
    if len(actor_1) == 0:
        actor = actor_2
        # print(len(actor_1))
    else: actor = actor_1
    actor = str(actor)
    actor = actor.replace('<br />','').replace(r'\u3000','').replace('&nbsp;','').replace('&middot;','·')
    # print("演员:",actor)

    #查找简介
    paris = str(paris)
    Finddetail = re.compile(r'◎简　　介<br />.*?<br />.*?(.*?)<br /><br />.*?<a target="_blank"')
    detail = re.findall(Finddetail,paris)
    detail = str(detail)
    detail = detail.replace(r'\u3000','').replace('&middot;','·').replace('&ldquo;','').replace('&rdquo;','').replace('&mdash;','')
    # print("简介:",detail)

    #查找获奖情况
    Findaward = re.compile(r'◎获奖情况.*?<br />.*?<br />(.*?)<br /><br /><br />')
    award = re.findall(Findaward,paris)
    award = str(award)
    award = award.replace(r'\u3000','').replace('<br />','').replace(r'&nbsp;','').replace('&middot;','·')
    # print("获奖情况:",award)

    #查找链接
    Findlink = re.compile(r'target="_blank" href="(.*?)"><strong><font style="BACKGROUND-COLOR')
    link = re.findall(Findlink,paris)
    link = str(link)
    # print("下载地址:",link)

    data_list = "\n" + "◎译　　名　" + name_1 + "\n" + "◎片　　名　" + name_2 + "\n" + "◎年　　代　" + time_1 + "\n" + "◎产　　地　" + place + "\n" + "◎类　　别　" + type + "\n" + "◎语　　言　" + language_1 + "\n" + "◎字　　幕　" + language_2 + "\n" + "◎上映日期　" + time_2 + "\n" + "◎IMDb评分" + idmb + "\n" + "◎豆瓣评分　" + douban + "\n" + "◎片　　长　" + long + "\n" + "◎导　　演　" + director + "\n" + "◎编　　剧　" + writer + "\n" + "◎演　　员　" + actor + "\n" + "◎简　　介　" + detail + "\n" + "◎获奖情况　" + award + "\n" + "◎下载链接  " + link + "\n"

    #结果的写入
    if os.path.exists('./电影天堂最终版.txt') == False:
        f = open('./电影天堂最终版.txt','w',encoding='utf-8')
        f.writelines("----------电影天堂最新电影列表----------")
    else:
        f = open('./电影天堂最终版.txt','a',encoding='utf-8')
    f.writelines(data_list)
    f.close()
    print(name_1,"heve been save","\n")
    # f = open('testfile.txt','w',encoding='utf-8')
    # f.writelines(data_list)

def Geturl(page_url,headers):
    response = requests.get(url=page_url,headers=headers)
    response.encoding = 'gbk'
    response = response.text
    tree = etree.HTML(response)
    link_list_1 = tree.xpath("//div[@class = 'co_content8']//a//@href")
    url_list = ["https://www.dydytt.net/" + str(i) for i in link_list_1]  # 将www.dytt.net加到开头
    del url_list[-8:]  # 删除倒数八个没用的网址
    # print(url_list)
    return url_list

if __name__ == "__main__":
    main()
