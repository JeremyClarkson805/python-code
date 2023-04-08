import requests

def main():
    post_url = 'https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'}
    littlebear = input(str("请输入需要查询的词汇:"))
    data = {'kw':littlebear}
    response = requests.post(url=post_url,data=data,headers=headers)
    #json方法返回的是一个对象，如果确定服务器响应数据是json类型的，才可以使用json
    dic_obj = response.json()
    print(dic_obj)




if __name__ == "__main__":
    main()