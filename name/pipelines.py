# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class NamePipeline(object):
    def process_item(self, item, spider):
        return item


# 存到mangodb中
class MyMongoDbPipeline(object):
    def open_spider(self, spider):
        # 连接数据库
        self.conn = pymongo.MongoClient(host='127.0.0.1', port=27017)
        # 选择数据库, 没有这个库会自动创建
        db = self.conn.name
        # 选择集合
        self.collection = db.name_col

    def process_item(self, item, spider):
        # 过来一个item, 就应该写入到mongodb中
        self.collection.insert(dict(item))

    def close_spider(self, spider):
        self.conn.close()
