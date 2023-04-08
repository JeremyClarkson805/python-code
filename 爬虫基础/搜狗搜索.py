import requests


def main():
    # step_1 指定url
    url = 'https://www.sogou.com/'
    #step_2 发起请求
    response = requests.get(url=url)
    #get方法会返回一个响应对象
    #step_3 获取响应数据
    #  .text返回的是字符串形式的响应数据
    page_text = response.text
    #step_4 持久化储存
    with open('./sougou.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(page_text)
    print("end...")






if __name__ == "__main__":
    main()