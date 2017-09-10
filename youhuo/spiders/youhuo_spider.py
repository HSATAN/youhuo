#coding=utf-8

from scrapy import Spider
import scrapy
import re, json
from scrapy.selector import Selector
class YouHuoSpider(Spider):
    name = 'youhuo'
    start_urls=[
        'https://item.yohobuy.com/51664144.html'
    ]

    def parse(self, response):
        text=response.body.decode("utf-8")
        sel=Selector(response)
        #
        # name=sel.xpath('//div[@class="pull-right infos"]/h1[@class="name"]/text()').extract()
        # if name:
        #     name=print(name[0])
        # origin_price=sel.xpath('//span[@class="price has-other-price"]/text()').extract()
        # if origin_price:
        #     origin_price=origin_price[0].decode("utf-8")
        # current_price=sel.xpath('//span[@class="promotion-price"]/span[@class="price"]/text()').extract()
        # if not current_price:
        #     current_price=sel.xpath('//span[@class="price-row"]/span[@class="price"]/text()').extract()

        # if current_price:
        #     current_price=str(current_price[0])
        price_info=re.findall('PING_YOU_VIEW_ITEM =(.*?);',response.body.decode("utf-8"),re.S)
        if price_info:
            price_info=json.loads(price_info[0].replace('// 宽x高','').replace("'",'"'))
            origin_price=price_info['orig_price']
            current_price=price_info['price']
        print(current_price)
        print(origin_price)
        print(price_info)