# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.dialects.mysql import pymysql
from .spiders.connect import getConnect

class FistbookPipeline(object):
    def process_item(self, item, spider):


        name = ''.join(item['bookname'])
        order_id = item['order_id']
        title = ''.join(item['title'])
        body = ''.join(item['body'])

        connection = getConnect()


        with connection.cursor() as cursor:
                # 数据库表的sql
                sql1 = 'Create Table If Not Exists %s(id int,title text,body text)' % name
                # 单章小说的写入
                sql = 'Insert into %s values (%d ,\'%s\',\'%s\')' % (name, order_id, title, body)
                print(title)
                cursor.execute(sql1)
                cursor.execute(sql)
            # 提交本次插入的记录
        connection.commit()

            # 关闭连接
        connection.close()
        return item


