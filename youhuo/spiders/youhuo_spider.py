#coding=utf-8

from scrapy import Spider
import scrapy
import re, json
from scrapy.selector import Selector
class YouHuoSpider(Spider):
    name = 'youhuo'
    start_urls=[
        'https://item.yohobuy.com/51538524.html'
    ]
    custom_settings = {
        'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'

    }
    def detail(self, response):
        sel = Selector(response)
        nav_node = sel.xpath('//div[@class="third-nav-wrapper"]//dd/a/@href').extract()
        if nav_node:
            print(nav_node)


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
        colors = sel.xpath('//div[@class="chose-color row clearfix"]//'
                           'ul[@class="colors pull-left clearfix"]/li/@data-color').extract()
        print(colors)

        sizes = sel.xpath('//div[@class="size-wrapper pull-left"]/ul')
        sku_list = []
        for index, size_node in enumerate(sizes):
            data = {}
            size_list = size_node.xpath('./li')
            data['color'] = colors[index]
            print(index)
            data['sku']=[]
            for  size_li in size_list:
                sku_item = {}
                data_sku = size_li.xpath('./@data-sku').extract()
                data_num = size_li.xpath('./@data-num').extract()
                data_name = size_li.xpath('./@data-name').extract()
                data_info = size_li.xpath('./@data-info').extract()
                # print(data_sku)
                # print(data_num)
                # print(data_name)
                # print(data_info)
                sku_item['sku_id'] = data_sku[0]
                sku_item['sku_num'] = data_num[0]
                sku_item['sku_name'] = data_name[0]
                sku_item['sku_info'] = data_info[0]
                data['sku'].append(sku_item)

            sku_list.append(data)

        for item in sku_list:
            print(item)