# -*- coding: utf-8 -*-
import scrapy
from fistbook.items import FistbookItem


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ["http://www.xbiquge.la/15/15409/"]
    
    #开始爬取的url链接
    #http://www.xbiquge.la/paihangbang/

    #每本小说的链接
    novel_list = []
    #开始的链接
    start_urls = ['http://www.xbiquge.la/15/15409/']

    def parse(self, response):
        '''
        parse()函数接收Response参数，就是网页爬取后返回的数据
        用于处理响应，他负责解析爬取的内容
        生成解析结果的字典，并返回新的需要爬取的请求
        '''


        #xpath规则可以通过查看网页源文件得出
        name = response.xpath('//h1/text()')
        item = FistbookItem()

        #建立一个items字典，用于保存我们爬到的结果，并返回给pipline处理
        item['bookname']= response.xpath('//h1/text()').extract()

        yield scrapy.Request(url=name, callback=self.get_bookurl)

    def get_bookurl(self, response):


        pass
