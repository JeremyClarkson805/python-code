import csv
import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class PioneerSpider(object):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
    }
    driver_path = r"/home/laen/program/chromedriver_linux64/chromedriver"

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.url = "http://cy.ncss.org.cn/search/projects#"
        fp = open("pioneer.csv", "a")  # 把数据以csv格式保存
        self.writer = csv.DictWriter(fp, ["name", "school", "desc", "url"])
        self.writer.writeheader()

    def run(self):
        self.driver.get(self.url)
        # 等加载
        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.presence_of_element_located((By.XPATH, "//ul[@class='map-item-box']")))
        other_btn = self.driver.find_elements_by_xpath("//span[contains(@class, 'glyphicon')]")[1]
        other_btn.click()

        self.school = input("请输入想要查询的学校:")  # 按学校分类查询
        self.province = input("请输入学校所在省份(直辖市或地区):")  # 筛一下地区不然效率低

        # 等加载
        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.presence_of_element_located((By.XPATH, "//ul[@class='map-item-box']")))
        province_btn = self.driver.find_element_by_link_text(self.province)
        if province_btn:
            province_btn.click()
        else:
            self.province = input("请输入正确的省份(直辖市或地区):")

        # 循环点击下一页
        while True:
            WebDriverWait(driver=self.driver, timeout=10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='search-list-item']")))
            source = self.driver.page_source
            self.parse_list_page(source)
            WebDriverWait(driver=self.driver, timeout=10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='pagination']/a")))
            next_btn = self.driver.find_element_by_xpath("//div[@class='pagination']/a[@class='next']")
            if next_btn:
                next_btn.click()
            else:
                break

    def parse_list_page(self, source):
        """抓目标项目的详情页url"""
        html = etree.HTML(source)
        divs = html.xpath("//div[@class='search-list-item']/div[@class='project-list-info']")
        for div in divs:
            schools = div.xpath(".//div[@class='project-list-item-tags-text']/span[1]/text()")
            for school in schools:
                if school == self.school:
                    link = div.xpath("./a/@href")[0]
                    link = "http://cy.ncss.org.cn" + link
                    self.parse_detail_page(link)
                else:
                    continue

    def parse_detail_page(self, link):
        """分析详情页"""
        dic = {}
        reponses = requests.get(link, headers=self.headers)
        text = reponses.text

        html = etree.HTML(text)
        name = html.xpath("//div[@class='banner-top clearfix']/div[@class='info-box']/h4/text()")[0]
        desc = html.xpath("//div[@id='project']//p//text()")
        desc = "".join(desc)

        dic["name"] = name
        dic["school"] = self.school
        dic["desc"] = desc
        dic["url"] = link

        self.writer_dic(dic)

    def writer_dic(self, dic):
        """写入数据"""
        self.writer.writerow(dic)
        print(dic)
        print("=" * 100)


if __name__ == '__main__':
    spider = PioneerSpider()
    spider.run()