import requests
from lxml import etree
import re

def main():
    base_url = "https://gz.58.com/ershoufang/p1/?PGTID=3d100000-0000-3444-f29d-bde4c7933c73&ClickID=1"
    # url_1 = "https://gz.58.com/ershoufang/p"
    # url_2 = "/?PGTID=3d100000-0000-3444-f29d-bde4c7933c73&ClickID=1"
    # for i in range(1, 10):
    #     url = url_1 + str(i) + url_2
    #     print(url)
    page_text = getHtml(base_url)
    tree = etree.HTML(page_text)
    # tree = etree.parse("./58同城.html",etree.HTMLParser(encoding='utf-8'))
    result_1 = tree.xpath("//div[@class = 'property']//h3/text()")#详情
    result_2 = tree.xpath("//div[@class ='property-content-info']//span/text()")#*室*厅*卫
    result_3 = tree.xpath("//div[@class = 'property-price']//span//text()")#总价格
    result_4 = tree.xpath("//div[@class = 'property-price']//p[@class='property-price-average']//text()")#*元/平方
    findtext = re.compile(r'.室.厅.卫')
    findprice = re.compile(r'...万')
    fp = open("58同城.txt","w",encoding = 'utf-8')
    for detail in result_2:#写一个表为下面正则表达式做准备
        fp.write(str(detail))
    fp.close()
    fp = open("58同城.txt",'r',encoding = 'utf-8')
    text_1 = fp.read(999999)
    inform_d = re.findall(findtext,text_1)
    # print(inform)
    fp.close()
    fp = open("58同城.txt","w",encoding = 'utf-8')
    for price in result_3:
        fp.write(price)
    fp.close()
    fp = open("58同城.txt","r",encoding = 'utf-8')
    text_2 = fp.read(999999)
    inform_p = re.findall(findprice,text_2)
    fp.close()
    fp = open("58同城_finally.txt", 'w', encoding='utf-8')
    for tittle,inform,price_total,price in zip(result_1,inform_d,inform_p,result_4):
        fp.write("卖点:")
        fp.write(tittle)
        fp.write("\n")
        fp.write("格局:")
        fp.write(inform)
        fp.write("\n")
        fp.write("总价:")
        fp.write(price_total)
        fp.write("\n")
        fp.write("售价:")
        fp.write(price)
        fp.write("\n")
        fp.write("\n")


    # for tittle,detail in zip(result_1,inform):
    #     # fp.write(tittle)
    #     # fp.write(detail)
    #     fp.write("\n")






def getHtml(url):
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'}
    html = requests.get(url=url,headers=headers).text
    # print(html)
    return html


if __name__ == "__main__":
    main()