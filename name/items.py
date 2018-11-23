# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NameItem(scrapy.Item):
    # define the fields for your item here like:
    # 第一页
    url = scrapy.Field()
    name = scrapy.Field()
    detail_url_list = scrapy.Field()

    # 第二页
    all_detail = scrapy.Field()
    name_url = scrapy.Field()

    # 第三页
    person_name = scrapy.Field()
    introduce = scrapy.Field()
    name_wuxing = scrapy.Field()
    name_wuge = scrapy.Field()
    name_analyze = scrapy.Field()
    name_match = scrapy.Field()
    person_detail = scrapy.Field()
