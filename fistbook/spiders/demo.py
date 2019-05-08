# -*- coding: utf-8 -*-
import scrapy
from fistbook.items import FistbookItem
from .util import get_tit_num,Cn2An


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ["xbiquge.la"]
    start_urls = ['http://www.xbiquge.la/paihangbang/']
    #开始爬取的url链接
    #http://www.xbiquge.la/paihangbang/

    #每本小说的链接
    novel_list = []
    #开始的链接
    

    def parse(self, response):
        item = FistbookItem()

        listt= response.xpath('//ul/li/a/@href').extract()
        del listt[:10]
        listt = list(set(listt))
        for li in listt:
            yield scrapy.Request(url=li, callback=self.get_bookurl)


    def get_bookurl(self, response):

        bookurl = response.xpath('//dd/a/@href').extract()
        a = 0
        for url in bookurl:
            yield scrapy.Request(url='http://www.xbiquge.la'+url,callback=self.get_content)


    def get_content(self, response):
        item = FistbookItem()
        item['bookname'] = response.xpath('//div[@class="con_top"]/a[3]/text()').extract()
        item['title'] = response.xpath('//div[@class="bookname"]/h1/text()').extract()[0]
        body = response.xpath('//div[@id="content"]/text()').extract()
        text = ''.join(body).strip().replace('\xa0\xa0\xa0\xa0','\n  ').replace('\r',' ')
        item['order_id'] = Cn2An(get_tit_num(item['title']))
        print(item['order_id'])
        item['body'] = text
        return item
