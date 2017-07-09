# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BaiduTiebaPipeline(object):
    def process_item(self, item, spider):
        content = item['content'].encode('utf-8')
        with open(r'E:\jobInfo.txt', 'a') as f:
            f.write(content + '\n')
        return item
