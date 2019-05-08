# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FistbookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #书名
    bookname = scrapy.Field()
    #章节名
    title = scrapy.Field()
    #章节内容
    body = scrapy.Field()

    #用来排序 scrapy异步处理Request请求，Scrapy发送请求之后，不会等待这个请求的响应,他会同时发送其他请求或者做别的事情。
    order_id = scrapy.Field()

