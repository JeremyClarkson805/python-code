import requests

def main():
    base_url = 'https://www.bilibili.com/video/BV1sM4y1X7zy/?spm_id_from=333.999.0.0&vd_source=205259626d771a8c4b63b9b3a51918ba'
    datalist = getData(base_url)


def getData(base_url):
    headers = \
    {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
     # 'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
     }
    html = requests.get(url=base_url,headers=headers)
    print(html)
    html_text = html.text
    with open("../test集合/马兆海鸥.html", 'w', encoding='utf-8')as fp:
         fp.write(html_text)
    print(html_text)
    print("Done")




if __name__ == "__main__":
    main()