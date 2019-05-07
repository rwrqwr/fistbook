# -*- coding: utf-8 -*-
import scrapy
from fistbook.items import FistbookItem


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ["xbiquge.la"]
    
    #开始爬取的url链接
    #http://www.xbiquge.la/paihangbang/

    #每本小说的链接
    novel_list = []
    #开始的链接
    start_urls = ['http://www.xbiquge.la/paihangbang/']

    def parse(self, response):
        '''
        parse()函数接收Response参数，就是网页爬取后返回的数据
        用于处理响应，他负责解析爬取的内容
        生成解析结果的字典，并返回新的需要爬取的请求
        '''
        item = FistbookItem()

        #xpath规则可以通过查看网页源文件得出
        name = response.xpath('//h1/text()')


        #
        listt= response.xpath('//ul/li/a/@href').extract()
        del listt[:10]
        listt = list(set(listt))
        '''
        item['bookname'] = listt
        return item
        '''

        for li in listt:
            yield scrapy.Request(url=li, callback=self.get_bookurl)


    def get_bookurl(self, response):

        bookurl = response.xpath('//dd/a/@href').extract()

        for url in bookurl:
            yield scrapy.Request(url='http://www.xbiquge.la'+url,callback=self.get_content)


    def get_content(self, response):
        item = FistbookItem()
        item['bookname'] = response.xpath('//div[@class="con_top"]/a[3]/text()').extract()
        item['title'] = response.xpath('//div[@class="bookname"]/h1/text()').extract()[0]
        body = response.xpath('//div[@id="content"]/text()').extract()
        text = ''.join(body).strip().replace('\xa0\xa0\xa0\xa0','\n  ').replace('\r',' ')
        item['body'] = text
        return item