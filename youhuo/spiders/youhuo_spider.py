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
    custom_settings = {
        'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'

    }
    def parse(self, response):
        text=response.body.decode("utf-8")
        sel=Selector(response)

        price_info=re.findall('PING_YOU_VIEW_ITEM =(.*?);',response.body.decode("utf-8"),re.S)
        if price_info:
            price_info=json.loads(price_info[0].replace('// 宽x高','').replace("'",'"'))
            origin_price=price_info['orig_price']
            current_price=price_info['price']
        print(current_price)
        print(origin_price)
        print(price_info)
        currency_code = price_info['currency_code']
        url = response.url
        categorys = price_info['category'].split('>')
        category_first_name = categorys[1]
        category_last_name = categorys[2]
        brand = price_info['brand']
        name = price_info['name']