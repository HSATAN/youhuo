#coding=utf-8

from scrapy import Spider
import scrapy
from youhuo.items import YouhuoItem
import re, json
from scrapy.selector import Selector
import sys
import logging
if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding("utf-8")


class YouHuoSpider(Spider):
    name = 'youhuo'
    start_urls=[
        'https://item.yohobuy.com/51647398.html'
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
            spu_id = price_info['spu_id']
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

        color_num = len(colors)
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
        info_data = {}



        info_node = sel.xpath('//ul[@class="basic clearfix"]/li/em')
        for index, info_sub_node in enumerate(info_node):
            try:
                key = info_sub_node.xpath('./span[@class="keySpace"]/text()').extract()[0].strip()
                value = info_sub_node.xpath('./span[@class="value-space"]/text()').extract()[0].strip()
                info_data[index] = {'key': key, 'value': value}
            except Exception as e:
                logging.error(e)
        print(info_data)

        desc_node = sel.xpath('//div[@id="details-html"]/em[@class="details-word"]/text()').extract()
        if desc_node:
            desc = desc_node[0]
        print (desc)
        print (color_num)

        images_url = sel.xpath('//div[@id="details-html"]/p/img/@data-original').extract()
        print (images_url)
        item = YouhuoItem()
        item['name'] = name
        item['spu_id'] = spu_id
        item['image_urls'] = images_url
        item['description'] = desc
        item['sku_list'] = sku_list
        item['currency_code'] = currency_code
        item['color_num'] = color_num
        item['origin_price'] = origin_price
        item['current_price'] = current_price
        item['category_first_name'] = category_first_name
        item['category_last_name'] = category_last_name
        print('-----------------------------')
        print(item)
        print('-----------------------------')