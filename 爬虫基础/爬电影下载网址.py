import requests
from bs4 import BeautifulSoup

# 爬取电影下载地址
url = "https://www.bugutv.net"
resp = requests.get(url=url)
resp.encoding = 'utf-8'
html = resp.text
# 用BeautifulSoup解析html
soup = BeautifulSoup(html, 'html.parser')
# 查找所有电影下载地址
down_links = soup.find_all('a', attrs={'class': 'downbtn'})
for link in down_links:
    print(link.get('href'))