from lxml import etree

def main():
    tree = etree.parse('./湛江市政府.html',etree.HTMLParser(encoding='utf-8'))
    # response = tree.xpath('//div[@class="newsList right"]')
    response_1 = tree.xpath('//div[@class="newsList right"]//li[1]/a/text()')[0]
    response_2 = tree.xpath('.//div[@class="newsList right"]/img/@src')

    print(response_2)

if __name__ == "__main__":
    main()