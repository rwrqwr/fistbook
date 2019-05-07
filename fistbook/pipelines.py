# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FistbookPipeline(object):
    def process_item(self, item, spider):

        print(item['bookname'])
        print(item['title'])
        #for i in item['body']:
        #    print(i)
        #print(item['body'])
        with open('E:\\studypy\\test2\\'+''.join(item['bookname'])+'.txt', 'a+', encoding='utf-8') as f:
            f.write(item['title'])
            f.write("".join(item['body']))
        return item