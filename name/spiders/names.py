# -*- coding: utf-8 -*-
import scrapy
from name.items import NameItem
import re


class NamesSpider(scrapy.Spider):
    name = 'names'
    allowed_domains = ['http://www.resgain.net']
    start_urls = ['http://www.resgain.net/xmdq.html']


    # 解析首页
    def parse(self, response):

        all_a = response.xpath('//div[@class="row"]/div[@class="col-xs-12"]/a')
        for oa in all_a:
            item = NameItem()
            item['url'] = oa.xpath('./@href').extract_first()
            item['url'] = 'http:' + item['url']
            item['name'] = oa.xpath('./text()').extract_first()

            # detail_url = item['url']
            # print('1' * 50)
            # print(detail_url)
            # print('1' * 50)
            # 循环每页
            for i in range(1, 11):
                detail_url = item['url'].split('.html')[0] + '_%d.html' % i
                # print('*' * 50)
                # print(detail_url)
                # print('*' * 50)
                yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item': item}, dont_filter=True)

    # 解析姓名详情页
    def parse_detail(self, response):
        items = response.meta['item']
        all_a = response.xpath('//div[@class="container"]/'
                               'div[@class="row"]/div[@class="col-xs-12"]/a')
        for oa in all_a:
            # items['name'] = oa.xpath('./text()').extract_first()
            name_url = oa.xpath('./@href').extract_first()
            name_url = items['url'].split('/name')[0] + name_url

            items['name_url'] = name_url

            yield scrapy.Request(url=name_url, callback=self.parse_person_detail, meta={'items': items},
                                 dont_filter=True)

    # 解析个人详情页
    def parse_person_detail(self, response):
        item = response.meta['items']
        item['person_name'] = \
            response.xpath('/html/body/div[2]/div/div[4]/div[2]/div[1]/div[1]/h3/text()').extract_first().split(':')[-1]

        print('%s正在下载...' % item['person_name'])

        item['introduce'] = response.xpath('//div[@class="panel-body"]/strong/text()').extract_first()
        item['name_wuxing'] = response.xpath('//div[@class="panel-body"]/div[1]/blockquote/text()').extract_first()
        item['name_wuge'] = re.findall(r'(\w+：\d+)', response.xpath('//div[@class="col-xs-12"][1]/blockquote').xpath(
            'string(.)').extract_first())
        item['name_analyze'] = response.xpath('//div[@class="col-xs-12"][2]/blockquote/div').xpath(
            'string(.)').extract()
        item['name_match'] = response.xpath('//div[@class="col-xs-6"][2]/blockquote/text()').extract_first()

        # print('*' * 50)
        # print(item)
        # print('*' * 50)

        yield item
        print('%s下载结束！' % item['person_name'])
        print('*' * 50)
        # input('+++')
