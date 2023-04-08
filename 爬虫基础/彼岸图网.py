import requests
from lxml import etree
import os

def main():
    base_url = "http://pic.netbian.com/4kmeinv/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
        }
    if not os.path.exists('./piclibs'):
        os.mkdir('./piclibs')
    url_list = []
    url_list.append(base_url)
    for i in range(2,67):
        url = "http://pic.netbian.com/4kmeinv/index_"+ str(i) +".html"
        url_list.append(url)
    for url in url_list:
        print(url)
        html = getHtml(url, headers)
        tree = etree.HTML(html)
        li_list = tree.xpath('//div[@class = "slist"]/ul//li')
        for li in li_list:
            img_src = 'http://pic.netbian.com/' + li.xpath('./a/img/@src')[0]
            img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
            # img_name.encode('iso-8859-1').decode('gbk')
            # print(img_name,img_src)
            img_data = requests.get(url=img_src, headers=headers).content
            img_path = 'piclibs/' + img_name
            with open(img_path, 'wb') as fp:
                fp.write(img_data)
                print(img_name, "保存成功")

def getHtml(url,headers):
    html = requests.get(url=url,headers=headers)
    html.encoding = 'gbk'
    html = html.text
    return html

if __name__ == "__main__":
    main()