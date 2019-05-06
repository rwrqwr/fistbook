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

