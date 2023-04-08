import re
import requests


findinform = re.compile(r'<a href=(.*?)<span class="time">',re.S)

def main():
   base_url =  "https://www.zhanjiang.gov.cn/zfwj/index.html"
   getHtml(base_url)
   text_1 = getHtml(base_url)
   # print(text_1)
   # inform = re.findall(findinform, text_1)
   # print(inform)
   with open('湛江市政府.html','w',encoding='utf-8')as fp:
       fp.write(text_1)

def getHtml(base_url):
    headers = \
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
        }
    html = requests.get(url=base_url, headers=headers)
    html_text = html.text
    # print(html_text)
    return html_text

if __name__ == "__main__":
    main()