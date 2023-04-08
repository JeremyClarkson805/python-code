import lxml
import bs4
import requests

def main():
    fp = open('./湛江市政府.html','r',encoding='utf-8')
    soup = bs4.BeautifulSoup(fp,'lxml')
    # text = soup.find_all('div',class_='newsList right')
    # text = soup.select(".newsList right>ul>a")
    print(soup)
    print(len((soup.select(".main>div a"))))
    print((soup.select(".main>div a"))[3].string)




if __name__ == "__main__":
    main()