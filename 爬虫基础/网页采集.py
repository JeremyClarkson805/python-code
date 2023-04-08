import requests

#ua--->请求载体的身份标识
#ua检测：门户网站的服务器会检测对应请求的载体任务表示，如果家安测到请求的载体身份标识为某款浏览器，则说明该请求是一个正常的请求。如果检测到的身份标识不属于某款浏览器，则表示该请求为不正常的请求(爬虫)，服务器有可能会拒绝该次请求
#ua伪装:让爬虫对应的请求载体身份标识伪装成某一款浏览器
def main():
    kw = input("请输入你要保存的网站的名字:")
    base_url = input("请输入要获取网站所对应的url:")
    # name = input(str("请输入你要搜索的东西:"))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
        }
    # print(url_1)  --->测试能否正确赋值
    # kw = input("请输入关键词:")
    url_1 = base_url #+ str(kw)

    # param = {'query':kw}
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url_1,headers=headers)
    response.encoding = 'gbk'
    page_text = response.text
    page_text = str(page_text)
    fileName = kw+'.html'
    with open(fileName,'w',encoding='utf-8')as fp:
        fp.write(page_text)
    print(fileName,"保存成功！")


if __name__ == "__main__":
    main()