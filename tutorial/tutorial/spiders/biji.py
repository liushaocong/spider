# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from ..items import TutorialItem,BijiItem
from scrapy.http import Request
import re
import time

class BijiSpider(scrapy.Spider):
    name = 'biji'
    allowed_domains = ['seputu.com']
    start_urls = ['http://seputu.com/']

    def parse_item(self,response):
        item = BijiItem()
        time.sleep(0.3)
        title = response.xpath("//div[@class='bg']")[0].xpath("./h1/text()").extract()
        body = str(response.xpath("//div[@class='content-body']").xpath("./p/text()").extract())
        print(title)
        body2 = re.sub(r'http://seputu.com/' and r'www.seputu.com', '', body)
        item['title'] = title
        item['body'] = body2
        return item



    def parse(self,response):
        hrefs = response.xpath("//div[@class='box']").xpath("./ul/li/a/@href").extract()
        title = response.xpath("//div[@class='box']").xpath("./ul/li/a/text()").extract()
        for url in hrefs:
            tutorial = TutorialItem()
            tutorial['href'] = url
            tutorial['title'] = 'test'

            yield Request(tutorial['href'],callback=self.parse_item)

        url2='http://seputu.com/'

        yield Request(url=url2,callback=self.parse)

