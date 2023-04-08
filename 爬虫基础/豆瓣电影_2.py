import json

import requests

def main():
    url = 'https://movie.douban.com/j/chart/top_list'
    param = \
        {'type':'24' ,
         'interval_id':'100:90',
         'action':'',
         'start':'0',#表示从库中第几部电影开始获取数据
         'limit':'20'#表示每次取出多少部电影
        }
    headers = \
        {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'}
    response = requests.get(url=url,params=param,headers=headers)
    list_data = response.json()
    print(list_data)
    fp = open('../test集合/douban_xiju_top.json', 'w', encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)
    #json_dumps(dict)时，如果dict包含有汉字，一定加上ensure_ascii=False

if __name__ == "__main__":
    main()