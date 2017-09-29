# -*- coding: utf-8 -*-
import scrapy
from ..items import BijiItem
import re


class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['http://seputu.com/']
    start_urls = ['http://seputu.com/biji1/1.html']

    def parse(self, response):
        item = BijiItem()
        title = response.xpath("//div[@class='bg']")[0].xpath("./h1/text()").extract()
        body = str(response.xpath("//div[@class='content-body']").xpath("./p/text()").extract())
        body2 = re.sub(r'http://seputu.com/'and r'www.seputu.com','',body)
        item['title'] = title
        item['body'] = body2
        return item
